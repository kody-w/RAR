# CopilotStudioTranspiler (@discreetRappers/copilot_studio_transpiler_agent)

Transpiles RAPP Python agents to fully native Copilot Studio solutions without Azure Function dependency.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/copilot_studio_transpiler_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_transpiler_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/copilot_studio_transpiler_agent/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Required environment variables: AZURE_TENANT_ID, COPILOT_STUDIO_CLIENT_ID, DATAVERSE_ENVIRONMENT_URL
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@discreetRappers/copilot_studio_transpiler_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@discreetRappers/copilot_studio_transpiler_agent
Page: https://kody-w.github.io/RAR/a/@discreetRappers/copilot_studio_transpiler_agent/
Plain text for AIs: https://kody-w.github.io/RAR/a/@discreetRappers/copilot_studio_transpiler_agent/agent.md
