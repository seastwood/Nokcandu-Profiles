# Nokcandu Game Profiles

Settings people shared to make Windows games run on Apple silicon Macs with
[Nokcandu](https://github.com/seastwood/Nokcandu). **Browse and search them at
[seastwood.github.io/Nokcandu-Profiles](https://seastwood.github.io/Nokcandu-Profiles/)** — or in Nokcandu itself under
**Game Profiles**, where one click applies a profile to your game.

## How it works

- **Each profile is an [issue](../../issues) in this repo.** Its 👍 / 👎 reactions are the votes ("works for me" /
  "doesn't work for me") and its comments are the discussion. Games are listed with the most 👍 first; profiles many
  people report as broken are tucked away.
- **Share yours from Nokcandu:** open the game's page → **Share This Setup…** → **Submit on GitHub**. Everything is
  filled in; you just click Submit. To update it later, edit your issue; to remove it, close it.
- **No waiting for approval.** An automatic check publishes valid profiles within the hour and comments on the issue if
  something needs fixing.

## What a profile contains

The complete setup that made the game work: which program to run, graphics mode, launch options, extra settings
(paths inside the game's app are written as `{app}/…`), raw mouse, performance switches, needed fixes (like the
cinematic fix), drive letters, whether it needs a disc image, plus a rating, notes, install steps and what it was tested
on.

Profiles are **settings only** — never files, downloads or scripts — and settings that could make Wine load code from
outside the game's app are rejected. That's checked here when a profile is submitted and again inside Nokcandu before
it's applied, so trying someone's profile can't harm your Mac.

## Good to know

- Only use games you own. Profiles don't include game files.
- Games with kernel anti-cheat generally can't run under Wine; online play with anti-cheat is at your own risk.
- Bugs or ideas for the app itself go to [Nokcandu's issues](https://github.com/seastwood/Nokcandu/issues).

Profiles are shared under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (public domain) so anyone can
use them. The catalog scripts are MIT licensed like Nokcandu.

Built-in optional component IDs: `cinematic`, `d3d8to9`, `directx9-extras`, `borderless`, `cursor-visibility`. These reference code shipped with Nokcandu; profiles cannot provide DLLs, scripts, download URLs, executable patches, or config-file edits. The component fixes require a Nokcandu version with component-fix support and a standalone managed game environment. Applying a profile previews unavailable fixes; each installed component has its own Undo in the game's Fixes panel.

Schema 2 profiles (Nokcandu 0.9.9+) preserve `rawMouseFrameSync` and an optional `gameDisplay` object containing only `recipe: "bf1942"`, a supported `[width, height]` resolution, and a boolean `menuCorrection`. BF1942 recipes require a BF1942.exe match and are checked again against the target installation. No patch bytes, config commands, or executable files are shared. Old schema 1 profiles remain valid. Performance settings retain `lowLatency` as well as the other documented controls.
