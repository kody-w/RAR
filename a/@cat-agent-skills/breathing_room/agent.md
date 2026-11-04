# Breathing Room (@cat-agent-skills/breathing_room)

Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo…

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/breathing_room_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/breathing_room_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/breathing_room/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/breathing_room_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/breathing_room
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/breathing_room/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/breathing_room/agent.md
