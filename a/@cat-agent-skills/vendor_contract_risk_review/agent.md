# Vendor Contract Risk Review (@cat-agent-skills/vendor_contract_risk_review)

First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/vendor_contract_risk_review_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vendor_contract_risk_review_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/vendor_contract_risk_review/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/vendor_contract_risk_review_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/vendor_contract_risk_review
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/vendor_contract_risk_review/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/vendor_contract_risk_review/agent.md
