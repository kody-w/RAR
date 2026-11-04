# ExamplePrivate (@kody-w/example_private)

Demonstrates the RAR private-agent stub layer — metadata only, with source resolved from a private GitHub repo at install time.

GATED LISTING: this public file is metadata, NOT executable agent code.
Do not copy the .py.stub into the agents folder. Your person needs read access to kody-w/example-private-rar and their own GitHub credentials.

1. Brainstem: if http://localhost:7071/health does not answer, run:
   curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
2. In your paired Brainstem chat, ask:
   rar install @kody-w/example_private
   It resolves the private source using your own gh auth access. No restart is needed.
3. Open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".

Can't run commands (a web chat AI)? Give your person these steps.

Only load code you trust. If that filename already exists, keep a backup and inspect it before replacing it. Configure any required environment variables and dependencies before use.
Dependencies: @rapp/basic_agent

Raw file: https://kody-w.github.io/RAR/agents/@kody-w/private/example_private_agent.py.stub
Browse in RAR: https://kody-w.github.io/RAR/#agent/@kody-w/example_private
Page: https://kody-w.github.io/RAR/a/@kody-w/example_private/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/example_private/agent.md
