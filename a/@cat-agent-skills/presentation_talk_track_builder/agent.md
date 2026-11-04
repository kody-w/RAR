# Presentation Talk Track Builder (@cat-agent-skills/presentation_talk_track_builder)

Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/presentation_talk_track_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/presentation_talk_track_builder_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/presentation_talk_track_builder/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/presentation_talk_track_builder_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/presentation_talk_track_builder
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/presentation_talk_track_builder/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/presentation_talk_track_builder/agent.md
