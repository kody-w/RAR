---
name: agent-files
description: Use single-file Python agents (*_agent.py) as your own tools. You become the host - you list the agents, decide which to call, run them with run.py, and answer from their results. Use when the user hands you an agent file, a folder of them, or asks you to "run this agent", "be the brainstem", or "use my agents".
---

# Agent files: you are the host

An agent file is one Python file ending in `_agent.py`. It holds a class with:
- `metadata` - a function schema: `name`, `description`, `parameters`.
- `perform(**kwargs)` - does the work and returns text.

Anything that reads the schema, picks a tool and calls `perform()` is a host.
In this skill, **you** are that host. No server, no install.

## The loop

1. **See your tools.** Run:
   `python3 run.py list`
   (or `python3 run.py list <folder>` for the user's own folder of agents).
   Read each tool's `description` - that is how you decide when to use it.
   If the output has `context`, treat it as background for the conversation.
   If it has `broken`, tell the user which file failed and why.
2. **Decide.** For the user's request, choose zero, one or several tools,
   exactly as you would choose any function to call. If none fits, just answer.
3. **Fire.** Run:
   `python3 run.py fire <Name> '<json arguments>' [folder]`
   Arguments must match the tool's `parameters`. Use `'{}'` for none.
4. **Read and continue.** Use the result. Fire another tool if it helps,
   up to 3 rounds per request, then answer the user in plain words.
5. **New files are new tools.** If the user adds or changes an agent file,
   the next `list` or `fire` sees it. No restart.

## Rules

- Run `list` before the first `fire` in a conversation, and again after any
  agent file changes.
- Never edit an agent file to make it work; report the error instead.
- Read an agent file before its first run if you didn't write it or the user
  didn't vouch for it. It is code running on their machine.
- Show the user what you fired, in one line (`Fired: Name {args}`), then the answer.
- If you can't run shell commands, read the agent file and tell the user the
  exact `fire` command to run, then continue from the result they paste back.

## What's in this folder

- `run.py` - the only machinery: lists and fires agents. Standard library only.
- the `*_agent.py` files - the agents (they can also live in an `agents/` folder).
  run.py has the shared base class built in. Drop in any `*_agent.py` to add a tool.
