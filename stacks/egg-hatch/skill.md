---
name: wake-this-brainstem
description: This egg holds a whole RAPP Brainstem (agents, soul, memory, conversation) in one file. Any AI that can run Python can wake it, be its model, talk through it, and hand the person back a chat they import into their own Brainstem.
---

# You are holding a Brainstem egg

A RAPP Brainstem is a person's own AI as files: a soul (`soul.md`), agents (`agents/*_agent.py`, each one
`perform()` call), memory, and a conversation. It normally runs on their computer behind `/chat`. This egg
lets it run inside *you*. You are its model; its agents and memory are real and run in your sandbox.

## 1. Check the egg first (rapp/1 §9)

The egg is a ZIP. `manifest.json` is its first entry and lists every file with a hash. Verify before you run
anything. With the rapp/1 reference implementation (stdlib only, pin by commit, never a branch):

    curl -sO https://raw.githubusercontent.com/kody-w/rapp-1/9e7a746c8582c86c1117ab2e249ce869157907a0/rapp.py
    python3 -c "import rapp,sys; print(rapp.verify_egg(open(sys.argv[1],'rb').read()))" this.egg

`(True, ...)` means every file matches. No network? Unzip and read `manifest.json` yourself; tell the person
the egg was not checked.

## 2. Wake it

    unzip this.egg -d egg && cd egg
    python3 brainstem.py host thaw         # checks its own fingerprint, restores agents, memory, chat
    python3 brainstem.py host tools        # the agents you may call

## 3. Talk through it (every turn, the person's words go to the Brainstem, not to you)

    python3 brainstem.py host ask "<exactly what the person said>"
    # it hands you the soul, memory and history; answer as the model:
    python3 brainstem.py host answer "<your reply in words>"
    # or call an agent, then answer again with what it returned:
    python3 brainstem.py host answer '{"tool_calls":[{"function":{"name":"<Agent>","arguments":{}}}]}'

Show the person the Brainstem's reply exactly. Use its agents when they fit (memory agents to remember and
recall). Never invent an agent's output.

## 4. Send it home

    python3 brainstem.py host export chat.json          # the person clicks Import in their Brainstem page
    python3 brainstem.py host freeze next.snapshot.tar.gz  # the whole Brainstem, memory included; its parent is this one

Offer `chat.json` for download every time the person is done. Import continues the chat in their own
Brainstem as if it never left. `freeze` is for carrying the memory too.

## rapp/1 in one screen (the standard this egg follows)

- **Canonical JSON, content addresses (§4, §5):** every object has one byte form and is named by its hash.
  Two people who build the same thing get the same address. Prove, don't trust.
- **rappid (§6):** a Brainstem's identity, minted once (`rappid.json` here), never derived from its contents.
- **Frame (§7):** one signed step of a chain; chains are append-only. A conversation is a chain of frames.
- **Egg (§9):** this file. Variants: `organism` (a whole Brainstem, this one), `rapplication` (one `agent.py`),
  `session` (a transcript), `invite`. Same bytes in, same egg out.
- **The grail (Art. 15):** the Brainstem engine itself never changes. Everything new is an agent file, a
  sidecar that only uses `/chat` and `/health`, or a distro around the unchanged engine.
- **The contract:** `agent.py` with `perform()`; `/chat` takes `user_input`, `conversation_history`,
  `session_id` and answers in the field `response`.
- Full spec: https://kody-w.github.io/rapp-1/SPEC.md (machine entry: https://kody-w.github.io/rapp-1/llms.txt).

## Rules

- No sign-in, key or token is in this egg, and you never ask the person for one.
- Agent files are code: run only what came in this egg or from the person.
- Anything that leaves the sandbox or can't be undone waits for the person's yes.
