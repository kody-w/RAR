# Assistente CLT para RH (@cat-agent-skills/clt_hr_assistant)

Assistente de legislação trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde dúvidas sobre férias, 13º salário, aviso prévio, jornada e tipos de rescisão, e calcula verbas rescisórias com memória de cálculo completa usando as tabelas oficiais vigentes de 2026 (salário mínimo, INSS e IRRF, incluindo a Lei 15.270/2025).

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/clt_hr_assistant_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/clt_hr_assistant_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/clt_hr_assistant/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/clt_hr_assistant_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/clt_hr_assistant
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/clt_hr_assistant/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/clt_hr_assistant/agent.md
