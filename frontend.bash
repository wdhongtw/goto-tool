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

goto() {
  if [ -z "$1" ]; then
    cd "$HOME" || echo "Can not go to home"
    return
  fi

  local dest
  dest="$($BACKEND --query "$1")"
  cd "$dest" || echo "Fail to chdir into $dest" >&2
}

complete -F _goto_complete goto
