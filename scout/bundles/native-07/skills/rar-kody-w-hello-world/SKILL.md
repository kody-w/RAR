---
name: "rar-kody-w-hello-world"
description: "Says hello to the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hello_world_agent", "rar_sha256": "dacc1cacd80777c63efa1e7ea140fca761df3a6f0df5d0bf116748ea30823009", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "kody-w", "tags": ["tutorial", "hello-world", "starter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/hello_world_agent`. The original RAPP
agent is preserved byte-for-byte in `hello_world_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Hello World Agent — A friendly greeting agent that demonstrates the basics.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "name": {
      "description": "Name to greet",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hello_world_agent.py` and embedded as the fenced Python below (sha256 dacc1cacd80777c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hello_world_agent.py` first:

```bash
python3 hello_world_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hello_world_agent.py   # or on stdin
python3 hello_world_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/hello_world_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hello_world_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/hello_world_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Hello World Agent — A friendly greeting agent that demonstrates the basics."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/hello_world_agent",
    "version": "1.0.3",
    "display_name": "Hello World",
    "description": "Greets the user by name with a canned hello message; a starter example touching no external systems.",
    "author": "kody-w",
    "tags": ["tutorial", "hello-world", "starter"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


class HelloWorldAgent(BasicAgent):
    def __init__(self):
        self.name = "HelloWorldAgent"
        self.metadata = {
            "name": self.name,
            "description": "Says hello to the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"}
                },
                "required": []
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        name = kwargs.get("name", "World")
        return f"Hello, {name}! Welcome to the RAPP Agent ecosystem."
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61XWZPquBX+KwrzcGeG7sbGGDedmlTYms0sxmYNqduyLe9IRvKC6dz/Htlw71RNJnkKxQO2zvKd72ziswbTxCO09lYLiV0857Wnmo2YRf048Qnmr3VYMOChKCIg4V8PgZQh+sLl0BWe4wix2ts//vlU8/nv2ttnzYog469q41JlR2hkd12EEy4fQezyg7jgDjF/jhF1CD3zVzZywOPpZ4Yi5wn8+muYQ+qyX8Dz3wBL6NsJg8cHwzMCv4H7+YuLkp9PtfLdqfYETrXK46n2y+/yFCUpxcA53SE9gc9S+ttfwA5FFuG2HmGtu6sVqLACZBFWsASdX0612jceG+YQUqtkpAztp5/A3LcoYcRJgG6RNAE0xYnPMeATNjyfAf4tbVKUIcp8M0IPuZiSAFWGAHHAx9/vpDcqfr/mJfavsITw8QIMrk+o7/oYRhW4E66OStsxRTwJGbKBWSTomRP3XP4APgYf/2HrJS4+AMR2eVoF2p8AC8YsjdBLCXjnIfyAZ0EM0BVZKbcVEYs7dnye4SceCCNRxrkqg2OhH0XA9imPhNCiss0JeCuNfXx8mJB5J3xPswTutcQaXOAHHPD8zCNwIt/1khNGlkfAl89vX8C/wP/SqoyXPla8wh70coRTfbkAvBbSMxfjzPNcIWhX9H5+e/DIzWBEAU+G7/jorhz5OET2d1L1cfe5KbeBiTiZnMhzTGjiYxf4yQuYOOAHXu60PGIAAo+wBNgoRthG2Cq4VcjD+cEkJglgMPGZUzyVTVN5/TAprCCev1pc/APM+ytegSQqy5DDrIS4MsE+p/9HyvGPzvvCQO+7iRewKAsMxJDC2KPw4cOB97wQCr6rc+MQYJSfcNmnqKQKllV4p4cLcWasR0qfy5wD3hpnnlj23XclAxNecgaB3Dk9YfaoZEjLVFiEQymAm/o2xBb666OkmEfSyK7440hLS48s2I+sVDVYtSaomvfRg6e0KYgt0AUO9TnBEbdMEapScg+qZJuzfyZlc3Jg96zy4vMtVo6nyLcQh1h7w2kUPVUj4k/HUkneGfGAWDm+eIPySZT4qHq6K33+YSQu4H1qVIC4haSIS9McBkdX+8YHBkWXlHNp30fj45yYZeuX8ySOYHIffZ817hraMIEP54/pwMUppM+spLAhvgjcC3++twI/+69z4yHHPMiLuZys0LJEC1r2q6AoitWWkANFpCAotgTHgkpbtB0Jth3BdmRbMB1RbCutVwQl4bUpCUKH22MkpRb6WtaDX/rm3kIe53PCo//9mL+yH6DvQEoafoypMrgH9s+a2W6ViWixSff+6Tfq291tp5hrr19/Lc7nW/9d1/pSIHu97po3x0rXRsFcz4eZq/Xm+mw8iUxVQkcJbqMc79beq2vIYdhOhWQWpXNXMcNhd5PdVo1FZ945BPWVKfYVMc8CV+kWzkyX9KBY7Pt5FE96K6qSfO+Q8fQmdGNv10x0daN09y6JNei6K5TYdLvND8LSxYoyndy8o9Z+5XYEqNcVa39WoynqCvpcoMN+a0DxxTHb03FanDf70aaeQLaYRP6YHkUj7c9HNM/3vqstjAUMi8KbF7vNaKA3HNVZGMSk9KC42iWZmssWUmV03tT1+CJ3Yhm7TrCLmOQ0FKG+fUcTGaVeeAl6cGNvdzMJjovz61S3Q6NnNuvb+FW1Nq336b6xu6kLpm6lA5nidYaSYOEMj5ZuGPLrgcJR1hy8m5vm1Tnv8zVNj8oNBYtRXzO7xaLZmNCsm47J5dwaZVZnRQ/rkaFqLLusoqOQ3bIVwWZ9rqfxXo9Elhzft8OtzpTd6NxCdYvyykuNbdSe0YPfOuQDBY/9RDZE7ZKNj5pod/puAg1pNpziizEeF8v86PKq7jdGbO1s8mkv1PqvClLtzmAcqnbcM7rvw5mINxkOB+pISLJg3t8NKMo7XivEM4vPDCv228Gqk9vboNc+GpslBw8vxXw5yq/bDTOlYdFYi6gv085+J+v6INECa3iMjEaj2HmN1WJnwczfLxtqw5nOBcNutC7W6B1fCWssDLcpo4xN+uIQuhcNHwftenPYZNp2Ms4nqUtMLQmPytkLVlpErpt1PLK2aniZuHS+g8mFkVZ3b02n7eNFF6mpBtiIgm1/0V0jOT5vYKflioqi3dbjvMh83x7MmvJEQTdzNmu+m4WT+IOxjtlRmDaT2UR0pZRKImZ7ZWVGgdiaip6e64EvXCmpe3MvVEd7g99xTBceJ8o+G+F4HwR2ZG6c4ULYNANB8MM0z+zO4cx87YxtIZ1Iq1HGTPkgZ+owbPDquzVdNxXymx6OZ80A7o32SO13Fit301EPiw4VVl686BFJ8i90NT46/c5hY4ymqnxFbKNvDgNXflW0bQKJSgtkNJJ1uJTIcLrtk5uYrbRc1sb7gyOHKGYhbC/N1vpSLEWiGTBduKKN3sf+ZjoM49TcaG7XbfVWUWjeZrZX17b0MnKbxWwy7y1VK5AmDbRsMDKY+flYd6AhCLO4dy2ytD6Rb63booBXiy5FwyGvO70jHbuO441bi/A6ofgG6dnbTHQVd2wvJx6T8gNqJztnp8aKFIz6RFuw/fTW6lzHaYTbt75gm2vxdktUb9+JWGPaJy1llLTrYrPVzK3LaOFpPf1gXVZOvS7Um0Sa4I0Eu9v1jUw01ThOLH6FKUR4mMa9sI72o7bctN34NuYVbEwV3EUTIseJMBT9dmeN98txfEt0t53fOj0SC8VyMBp1lHrXs4iPWi3XO9Y3853qXXbL+mugy71O2MhWcpiHfMz+9hsf1+Vuf6zCP7solgP9/7Y77iuAXwtweSHgu5DvRWi/Vb7e/tQ7X5bU8rnv+8pjUeo+lsp94T1XWs+VVnle3C9SBCfomnzf9Al0y/8ktSTltyAfRlzwD2oJpHzfl96q63m1brnHF6n27d+laZyOEQ0AAA== -->
