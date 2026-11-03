# Grail layers

Updates that install OVER the unchanged grail (the Brainstem kernel) and can fail without breaking it.

- One-liner: `curl -fsSL https://kody-w.github.io/grail-layers/install.sh | bash`. It runs the grail's own one-liner first, then installs these layers over it.
- Each layer is applied in memory at start. The supervisor probes `/chat`, and if anything fails it starts plain grail.
- Undo: `curl -fsSL https://kody-w.github.io/grail-layers/uninstall.sh | bash`

| Layer | What it adds |
|---|---|
| `responses_models` | Models that only speak the Responses API (for example gpt-6.1-sol and gpt-6-luna) become usable in the unchanged grail. |

The pattern and the layer contract: https://github.com/kody-w/grail-layers
