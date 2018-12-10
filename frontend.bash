#!/usr/bin/env bash

BACKEND="_goto_backend"

_goto_complete()
{
  local cur

  COMPREPLY=()
  cur=${COMP_WORDS[COMP_CWORD]}

  case "$cur" in
    *)
      COMPREPLY=($( compgen -W "$($BACKEND --search "")" -- "$cur" ))
      ;;
  esac

  return 0
}

_goto() {
  if [ -z "$1" ]; then
    cd "$HOME" || echo "Can not go to home"
    return
  fi

  local dest
  dest="$($BACKEND --query "$1")"
  cd "$dest" || echo "Fail to chdir into $dest" >&2
}

usage() {
  cat <<'EOF'
Usage:
    goto <mark>       chdir to some bookmark set before

    goto -x           bookmark current directory (using basename)
    goto -l           list all bookmarks

    goto -a <mark> <path>
                      add or modify bookmark <mark> point to <path>
    goto -d <mark>    delete bookmark <mark>
    goto -r           reset all bookmarks
EOF
}

goto() {
  case "$1" in
    -h|--help)
      usage
      ;;
    -x)
      [ $# -ne 1 ] && { usage; return; }
      $BACKEND --add-mark "$(basename "$PWD")" "$PWD"
      ;;
    -a)
      [ $# -ne 3 ] && { usage; return; }
      $BACKEND --add-mark "$2" "$3"
      ;;
    -d)
      [ $# -ne 2 ] && { usage; return; }
      $BACKEND --delete-mark "$2"
      ;;
    -r)
      [ $# -ne 1 ] && { usage; return; }
      $BACKEND --reset-marks
      ;;
    -l)
      [ $# -ne 1 ] && { usage; return; }
      $BACKEND --list-marks
      ;;
    *)
      [ $# -ne 1 ] && { usage; return; }
      _goto "$1"
      ;;
  esac
}

complete -F _goto_complete goto
