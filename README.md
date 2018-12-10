# Goto Tool

A convenient tool (I hope) that:

1. Let you add bookmarks of FS directories, and
2. Let you jump to one of these bookmarks afterwards.

## How to Use

```
Usage:
    goto <mark>       chdir to some bookmark set before

    goto -x           bookmark current directory (using basename)
    goto -l           list all bookmarks

    goto -a <mark> <path>
                      add or modify bookmark <mark> point to <path>
    goto -d <mark>    delete bookmark <mark>
    goto -r           reset all bookmarks
```

## How to Install

`make install` and `make uninstall` to install and remove this tool.

By default, this tool will use these directories: (create if not exists)

- `$HOME/.config/goto-tool`: where the bookmarks are stored
- `$HOME/.config/bashrc.d`: where to install the Bash script
- `$HOME/.bin`: where to install backend Python script

To use this tool, you need to source `$HOME/.config/bashrc.d/goto.bash` in
your shell. We recommend to put the code below in your `bashrc` to achieve it.

``` sh
# Source definitions within $HOME/.config/bashrc.d folder
for file in $HOME/.config/bashrc.d/*; do
  [ -e "$file" ] || continue
  source "$file"
done
```

Also, add `$HOME/.local/bin` to `$PATH` in your `.profile`

``` sh
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

The bookmarks is stored as a JSON file in `$HOME/.config/goto-tool/bookmarks`
and will not be deleted by default when uninstall.
