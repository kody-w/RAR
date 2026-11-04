# WordPress Publish (@kody-w/wp_publish_agent)

Publish or update a post on a self-hosted WordPress site via the REST API. Idempotent by slug, so re-running updates instead of duplicating. Credentials are read from the environment and never stored.

If your person asked you to load it, any AI (or person) can, in three steps:
1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
     curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. Hot-load, no restart: save this file into the Brainstem's agents folder:
     curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/wp_publish_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/wp_publish_agent.py
   The next chat message can use it.
3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/wp_publish_agent/

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Required environment variables: WP_URL, WP_USER, WP_APP_PASSWORD
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@kody-w/wp_publish_agent.py
Browse in RAR: https://kody-w.github.io/RAR/#agent/@kody-w/wp_publish_agent
Page: https://kody-w.github.io/RAR/a/@kody-w/wp_publish_agent/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/wp_publish_agent/agent.md
