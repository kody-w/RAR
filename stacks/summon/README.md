# Summon (RAR stack)

Scan a RAR card's QR code with your phone, and it installs into your own Brainstem.

1. Drop `summon_agent.py` into your Brainstem's `agents/` (or summon it).
2. In chat: **"start summon"**. Open the pairing page it gives you and scan it with your phone (the phone must be on your Tailscale network).
3. Scan any card's QR code (`https://kody-w.github.io/RAR/s.html#<seed>`) and tap **Summon**.

How it stays safe: the QR carries only a card's seed. The sidecar looks the seed up in RAR, downloads the file, checks its sha256, and installs through the Brainstem's own `/agents/import`, which checks it again. Only notarized agents and verified stacks can be summoned. The sidecar listens only on this Mac and its Tailscale address. The Brainstem kernel is never changed.

## Summon by chant (no phone)

Drop `summon_chant_agent.py` into your Brainstem's `agents/`. Then say a card's seven words in chat:

> Summon by chant: SAGE ZAP SENTINEL PIVOT CRUX EXTINGUISH BIND

The seven words are the card's seed. The agent looks the seed up in this catalog, checks every sha256, and
installs through the Brainstem's own `/agents/import`. Everything is ready on the next message.

One chant, three sizes:

- **an agent**: one file lands.
- **a stack**: every agent file in a verified stack lands (`FORGE FUSE PANTHER BEREFT MARCH CREED TEMPER`
  brings both Claude Workflows agents). A retired, unverified or whole-Brainstem stack is refused in plain words.
- **a stack with an egg**: the agents land, the egg is fingerprint-checked and kept on the device, and the
  catalog's own egg hatcher (`@rapp/egg_hatcher`) is brought to open it. An egg can carry anything under rapp/1.

### A team's own catalog

A team catalog is a git repo, private if you like, with the same `registry.json` shape. It is read with your own
GitHub sign-in. Say "Add the team catalog owner/name" once; after that its chants work like any other, and the
reply says which catalog answered. A team card's seed can never equal a public card's seed.

### Keep a song as a card

Say "Keep this song as a card titled Morning Check:" and the song. It becomes one agent file with its own
seven-word chant, working on your device at once. "Publish" tells you what will be sent and waits for a yes;
then anyone on the team says the chant, hears the song word for word, or says "run it".

A verse can bring one the same way: "R, A, P, P, verse. Bring MANTLE JAB DUSK PULSAR FULCRUM REVOKE SHARD.
Check it answers. Show me. And seal."
