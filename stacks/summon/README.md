# Summon (RAR stack)

Scan a RAR card's QR code with your phone, and it installs into your own Brainstem.

1. Drop `summon_agent.py` into your Brainstem's `agents/` (or summon it).
2. In chat: **"start summon"**. Open the pairing page it gives you and scan it with your phone (the phone must be on your Tailscale network).
3. Scan any card's QR code (`https://kody-w.github.io/RAR/s.html#<seed>`) and tap **Summon**.

How it stays safe: the QR carries only a card's seed. The sidecar looks the seed up in RAR, downloads the file, checks its sha256, and installs through the Brainstem's own `/agents/import`, which checks it again. Only notarized agents and verified stacks can be summoned. The sidecar listens only on this Mac and its Tailscale address. The Brainstem kernel is never changed.
