# Booth Loop Video (@cat-agent-skills/booth_loop_video)

Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/booth_loop_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/booth_loop_video_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/booth_loop_video/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/booth_loop_video_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/booth_loop_video
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/booth_loop_video/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/booth_loop_video/agent.md
