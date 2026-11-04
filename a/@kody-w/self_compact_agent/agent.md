# SelfCompact (@kody-w/self_compact_agent)

The brainstem compacts its own context: a gauge on every chat, hints as it fills, and at the cutoff every other tool waits until the model writes a note to itself that survives when old turns drop out.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/self_compact_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/self_compact_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/self_compact_agent/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@kody-w/self_compact_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@kody-w/self_compact_agent
Page: https://kody-w.github.io/RAR/a/@kody-w/self_compact_agent/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/self_compact_agent/agent.md
