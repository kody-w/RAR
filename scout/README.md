# RAR skills and workflows for Microsoft Scout

Copilot plugin install:

```text
copilot plugin marketplace add kody-w/RAR
copilot plugin install rapp@rar
```

Start with the Toasted RAPP skill manager and converter:

```text
https://github.com/kody-w/RAR/tree/main/scout/starter
```

The starter makes Toasted `SKILL.md` the default and normalizes raw skills through valid RAR agents. The manager hotloads verified skills into `~/.copilot/skills`, which Microsoft Scout can read in place. Bounded GitHub-import shards live under `bundles/`; each factory or rapplication workflow has an isolated directory under `workflows/` containing only that workflow and its companion skill. See `catalog/catalog.json` for every import URL.

Generated: 1716 reversible Toasted skill(s), 218 bounded skill bundle(s), and 40 disabled workflow template(s). Canonical RAR agent bytes remain under `agents/`; `scout/` is removable compatibility output.
