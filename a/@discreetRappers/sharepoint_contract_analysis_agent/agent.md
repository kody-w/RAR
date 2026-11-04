# ContractAnalysis (@discreetRappers/sharepoint_contract_analysis_agent)

Analyzes contract documents in Azure File Storage with Azure OpenAI — clause extraction, risk flagging, and comparison.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/sharepoint_contract_analysis_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/sharepoint_contract_analysis_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/sharepoint_contract_analysis_agent/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Required environment variables: AZURE_FILES_SHARE_NAME, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT_NAME, AZURE_OPENAI_ENDPOINT, AZURE_STORAGE_ACCOUNT_NAME
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@discreetRappers/sharepoint_contract_analysis_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@discreetRappers/sharepoint_contract_analysis_agent
Page: https://kody-w.github.io/RAR/a/@discreetRappers/sharepoint_contract_analysis_agent/
Plain text for AIs: https://kody-w.github.io/RAR/a/@discreetRappers/sharepoint_contract_analysis_agent/agent.md
