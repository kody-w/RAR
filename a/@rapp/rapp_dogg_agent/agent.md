# RAPP DOGG (@rapp/rapp_dogg_agent)

Hotload one file and a brainstem knows rapp/1 exactly instead of guessing. Pulls the current protocol canon — frame rules, identity minting law, kind families, egg determinism, the exchange contract, and the vocabulary with each term's status — from a public, static, unauthenticated DOGG anchor, and injects it into the system prompt every turn. Read-only: installs nothing, executes nothing it fetches.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/rapp_dogg_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_dogg_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/rapp_dogg_agent/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@rapp/rapp_dogg_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@rapp/rapp_dogg_agent
Page: https://kody-w.github.io/RAR/a/@rapp/rapp_dogg_agent/
Plain text for AIs: https://kody-w.github.io/RAR/a/@rapp/rapp_dogg_agent/agent.md
