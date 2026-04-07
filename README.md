# Template for `tangnano9k` development

Open-source suite for synthesizing, Place & Route, and flashing for `tangnano9k`

~~this slop works!!~~

## Prerequisites

Install `openFPGALoader`, usually available in Ubuntu repository.
If needed, enable [udev rules](https://trabucayre.github.io/openFPGALoader/guide/install.html#udev-rules).

Install `uv`.

## Howto

1. `uv sync`
2. `uv run main.py`

## Commandline Options

Append `--skip-synthesis` to only flash to device and skip synthesizing/P&L.
Append `--write-flash` or `-f` to write to the flash.
