# Microsoft AI Platform Advisor (@cat-agent-skills/microsoft_ai_platform_advisor)

Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/microsoft_ai_platform_advisor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/microsoft_ai_platform_advisor_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/microsoft_ai_platform_advisor/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/microsoft_ai_platform_advisor_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/microsoft_ai_platform_advisor
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/microsoft_ai_platform_advisor/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/microsoft_ai_platform_advisor/agent.md
