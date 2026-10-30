# Zsh Prompt Studio

A visual builder for zsh prompts. Arrange segments, pick shapes and colors,
watch a live terminal preview, then copy a single self-contained `.zsh` file.

Open `prompt-studio.html` in a browser. Nothing to install.

## What it makes

- **Segments:** OS logo, user@host, directory, git, exit status, command
  duration, clock, jobs, Python env, Node, AWS profile, Kubernetes context,
  and custom text or command output.
- **Styles:** powerline (arrow, round, slant, flame, pixel separators and
  caps), capsules, or plain text.
- **Layout:** one or two lines, `╭─ ╰─` frame, right segments on the top line
  with a filler, transient prompt, prompt character colored by exit status.
- **Presets** inspired by Powerlevel10k, Starship, Pure and Oh My Posh, plus
  palettes (Tokyo Night, Catppuccin, Gruvbox, Nord, Dracula, Rosé Pine…).

The generated file has no dependencies. Git info comes from a single
`git status --porcelain=v2 --branch` call per prompt.

## Install a generated prompt

1. Use a Nerd Font as your terminal font
   (`brew install --cask font-jetbrains-mono-nerd-font`).
   Ghostty has the icons built in; Terminal.app and most others need the font.
2. Press **Copy .zsh** in the studio, then:

   ```sh
   mkdir -p ~/.config/zsh && pbpaste > ~/.config/zsh/prompt.zsh
   echo 'source ~/.config/zsh/prompt.zsh' >> ~/.zshrc
   ```

## Building

`prompt-studio.html` is generated from `src/studio.html`. The build inlines a
subset of Symbols Nerd Font Mono so the preview shows real icons:

```sh
pip install fonttools brotli
python3 build.py path/to/SymbolsNerdFontMono-Regular.ttf
```

The font comes from [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts)
(`NerdFontsSymbolsOnly.zip`), MIT licensed.
