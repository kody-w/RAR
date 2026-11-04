# Prompt Extractor (@kody-w/prompt_extractor)

Extract the prompts shown on screen in a video by OCRing it frame by frame, merging scrolled and repeated views into one entry each, so prompts demoed in a screen recording do not have to be transcribed by hand.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/prompt_extractor.py -o ~/.brainstem/src/rapp_brainstem/agents/prompt_extractor.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/prompt_extractor/

Before chatting, rename prompt_extractor.py to rar_kody_w_prompt_extractor_agent.py in the agents folder so the Python loader discovers its _agent.py suffix.

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@kody-w/prompt_extractor.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@kody-w/prompt_extractor
Page: https://kody-w.github.io/RAR/a/@kody-w/prompt_extractor/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/prompt_extractor/agent.md
