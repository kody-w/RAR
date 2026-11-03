# Claude Workflows

Run a Claude Managed Agent, including dynamic multi-agent workflows, from Brainstem chat.

- Templates are agent configs (the arguments of `client.beta.agents.create`) saved as JSON in
  `claude-workflows/templates/`. Write them yourself, or let WorkflowBuilder (`workflow_builder_agent.py`, in this stack) assemble one
  from a name, what it makes, plan steps, phases and output files.
- "Run <template> on <task> with a $N cap" starts a background job with a hard spending cap; chat never blocks.
- "Status" shows the team runs and phases as they happen; "results" lists the files it made.
- Your Anthropic key comes from `ANTHROPIC_API_KEY` or the macOS Keychain (`CLAUDE_WORKFLOW_KEYCHAIN`,
  default `anthropic-api-backup`). It is read at run time and never written anywhere.
