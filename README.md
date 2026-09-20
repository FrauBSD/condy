[//]: # ($FrauBSD: condy/README.md 2026-09-19 13:28:24 -0700 Devin Teske $)

# condy

Conky launcher and wallpaper rotator. Detects fvwm, bvwm, GNOME, and KDE,
starts the matching conky rc, and sets the desktop with hsetroot(1).

Home: [FrauBSD/condy](https://github.com/FrauBSD/condy)

## Requirements

- `conky` (FreeBSD: `sysutils/conky`)
- `hsetroot` (FreeBSD: `x11/hsetroot`)
- A compositor is optional; conky's ARGB panel looks better with one
- Sample panel font: DejaVu Mono (`x11-fonts/dejavu`)

## Install

```sh
make install          # bin, man, and share/examples/condy; DESTDIR= supported
```

After install, `man condy`. From the tree, `make` generates `condy`
from `condy.in` (and `condy.1`); then `./condy` or `man ./condy.1`.

Foreword for commits in this repository: run `.git-hooks/install.sh` so
FrauBSD keywords expand.

## Sample theme

condy looks under `$HOME` for wallpaper directories and conky rcs. The
defaults match the files in this tree:

| Setting | Default (relative to `$HOME`) |
|---|---|
| `WALLPAPER` | `theme/wallpaper` |
| `TALLPAPER` | `theme/tallpaper` |
| `CONKY_CONFIG` | `theme/conky/ident.conkyrc` |
| `CONKY_GNOME_CONFIG` | `theme/conky/ident-gnome.conkyrc` |
| `CONKY_KDE_CONFIG` | `theme/conky/ident-kde.conkyrc` |

First-time setup (assuming default PREFIX=/usr/local):

```sh
mkdir -p "$HOME/theme" "$HOME/.config/autostart"
cp -Rn /usr/local/share/examples/condy/theme/* "$HOME/theme/"
cp -n /usr/local/share/examples/condy/autostart/condy.desktop \
	"$HOME/.config/autostart/"
condy load
```

Landscape images go in `WALLPAPER`; portrait in `TALLPAPER`. condy picks
one at random every `CONDY_DESKTOP_INTERVAL` seconds (10 minutes) and
uses the portrait set when the screen is taller than it is wide. Drop
your own files in those directories; the shipped PNGs are plain gradients
so the rotator has something to show. Rebuild them with
`tools/mk-sample-wallpapers.py` if needed.

The default conky rcs are a compact two-row ident (sysname, host,
root fs, cpu, mem, load): a 1200-wide 10pt panel for a 1280-wide display.
Host is `hostname(1)` with the last two DNS labels peeled when there
are more than two. Hires samples (`ident-hires.conkyrc` and gnome/kde
variants) are a 1536-wide 12pt panel with disks and net graphs, for a
1600-wide display. Point `CONKY_*` at those from `~/.condy.conf` if
that matches your display. Edit disk names and the `ue0` iface;
`downspeedgraph`, `downspeedf`, `upspeedgraph`, and `upspeedf` need
a literal interface name.

## Configuration

Optional overlays, sourced as sh (later file wins; assuming PREFIX=/usr/local):

1. System: `/usr/local/etc/condy.conf` (`-s file` to pick another)
2. User: `~/.condy.conf` (`-u file` to pick another)

A commented template is `/usr/local/share/examples/condy/condy.conf`.
condy runs with no overlay if `~/theme` is in place. Example user file:

```sh
WALLPAPER=theme/wallpaper
CONKY_CONFIG=theme/conky/ident.conkyrc
```

## Autostart

The packaged desktop file runs `condy load` at session start.

GNOME, KDE, and other XDG sessions:

```sh
mkdir -p "$HOME/.config/autostart"
cp -n /usr/local/share/examples/condy/autostart/condy.desktop \
	"$HOME/.config/autostart/"
```

fvwm / bvwm rely on `AddToFunc StartFunction`:

```
AddToFunc StartFunction
+ I Exec exec condy load
```

`load` is stop then start, so a leftover worker from a previous session
does not linger.

## Usage

```text
condy start       Start conky and the wallpaper worker
condy stop        Stop both
condy status      Show pids
condy restart     Same as load
condy load        Stop then start (autostart uses this)
condy cycle       Walk WALLPAPER or TALLPAPER at 5s intervals
condy pause       Freeze wallpaper rotation
condy resume      Unpause wallpaper rotation
condy unpause     Same as resume
condy reload      Pick a new random wallpaper
condy refresh     Re-apply the current wallpaper
condy set file    Pin a specific image
```

Options: `-d` (debug to `~/.condy.log`, repeat up to 5 times), `-l file`
(log path), `-q` (quiet), `-s file` (system config), `-u file` (user
config), `-v` (version).
