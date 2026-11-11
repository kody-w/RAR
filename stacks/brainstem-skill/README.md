# Brainstem skill (staging)

One page that makes any AI RAPP compatible. Hand an AI `SKILL.md`; it asks for one yes and then:

1. writes one small file, `rapp/kernel.py`, and checks its fingerprint;
2. that file fetches what it still needs from this catalog, fingerprint-checked;
3. it writes a short standing note into the AI's own always-on instructions (`AGENTS.md`, `CLAUDE.md`,
   Copilot's or Gemini's). From then on the page is never needed again.

After that, each turn, the AI reads its `rapp/agents/` folder fresh, uses what is there as tools, brings
new ones by a seven-word chant, and can answer in a Brainstem's chat shape. On the person's ask it can also
listen on a Brainstem's address (`kernel.py serve`), with that AI doing the thinking.

**Off switch:** delete `rapp/agents/`. The next turn removes the standing note; the instructions file is
byte for byte what it was before.

**Build line:** asked to build something and get it ready, the AI writes one agent file and runs `kernel.py ready`.
The file must describe itself, answer a real call with the expected words, and only then is handed,
fingerprint-checked, to the person's Brainstem on the same device through its own import door.

Nothing here touches or replaces the Brainstem kernel. It is the same contract (`agents/`, `perform`,
`/chat`, `/health`) honoured by a hundred-line loop, for AIs that are not a Brainstem.

Seen so far (2026-11-10, one Mac): Claude and Copilot each hatched from the page; Copilot, in a later session
with no page, ran a song and brought an agent; the off switch restored the instructions file exactly; and
five messages sent to this loop and to a real Brainstem gave the same reply shape, agent outputs and loaded
agents, 16 of 16 checks. Windows is not yet tried.
