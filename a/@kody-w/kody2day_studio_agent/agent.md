# Kody2day Studio (@kody-w/kody2day_studio_agent)

Make the daily Kody2day episode: the day's digest → Claude writes the RAPP lesson, Copilot refutes it, the education-shorts pack renders a narrated 16:9 explainer plus byte-sized Shorts → queue with YouTube metadata.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/kody2day_studio_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/kody2day_studio_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/kody2day_studio_agent/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@kody-w/kody2day_studio_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@kody-w/kody2day_studio_agent
Page: https://kody-w.github.io/RAR/a/@kody-w/kody2day_studio_agent/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/kody2day_studio_agent/agent.md
