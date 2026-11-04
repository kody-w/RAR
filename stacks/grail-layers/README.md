# Grail layers

Updates that install OVER the unchanged grail (the Brainstem kernel) and can fail without breaking it.

- One-liner: `curl -fsSL https://kody-w.github.io/grail-layers/install.sh | bash`. It runs the grail's own one-liner first, then installs these layers over it.
- Each layer is applied in memory at start. The supervisor probes `/chat`, and if anything fails it starts plain grail.
- Undo: `curl -fsSL https://kody-w.github.io/grail-layers/uninstall.sh | bash`

| Layer | What it adds |
|---|---|
| `providers` (seeded) | The one provider part: models that only speak the Responses API (gpt-6.1-sol, gpt-6-luna) and the models running on this machine (Ollama, as `ollama/<name>`, tools included) become usable in the unchanged grail. |
| `journal_tap` (seeded) | Every chat turn is recorded in the owner's Brainstem Journal on this device, by default; pause it from chat. No journal running: nothing happens. |
| `responses_models`, `local_models` | Status: **alias of `providers`** (one point, one occupant). Still served at their URLs for older shapes; not seeded. |
| `lispy_brainstem` (kernel, not seeded) | A whole Brainstem whose kernel is LisPy, as one file. Say "update my brainstem with @kody-w/lispy_brainstem"; it is tried in the lab first and "undo" puts the grail kernel back. |

## The one distro

Since 1.3.0 this pack is THE distro for everything new: summon it and you get your own Brainstem on the pinned grail with the seeded layers (`providers`, `journal_tap`) plus two agents that use them: `journal_recall_agent` ("what did I ask about X last week", pause/resume recording) and `fragments_agent` (paste once, address by hash, pin into every chat). From a terminal, `llm -m brainstem` reaches it through https://github.com/kody-w/llm-brainstem. Other distros stay focused on their one job and do not carry these layers.

Since pack 1.2 every entry is a **part**: `{id "@publisher/name", kind layer|kernel, point, file, sha256, locator}`.
The installer seeds the device's own rapp/1 chain from the `parts` list (one tile, gated as already proven), and from
then on the owner changes the shape through chat ("update my brainstem with …", "undo"). The older `layers` list is
kept as an alias for older installers.

The pattern and the layer contract: https://github.com/kody-w/grail-layers
