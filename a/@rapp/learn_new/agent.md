# LearnNew (@rapp/learn_new)

Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/learn_new_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/learn_new_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/learn_new/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@rapp/learn_new_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@rapp/learn_new
Page: https://kody-w.github.io/RAR/a/@rapp/learn_new/
Plain text for AIs: https://kody-w.github.io/RAR/a/@rapp/learn_new/agent.md
