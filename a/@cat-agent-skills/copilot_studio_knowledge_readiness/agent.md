# Copilot Studio Knowledge Readiness (@cat-agent-skills/copilot_studio_knowledge_readiness)

Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_knowledge_readiness_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_knowledge_readiness_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_knowledge_readiness/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_knowledge_readiness_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@cat-agent-skills/copilot_studio_knowledge_readiness
Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_knowledge_readiness/
Plain text for AIs: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_knowledge_readiness/agent.md
