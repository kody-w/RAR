---
name: "rar-kody-w-connected-solution"
description: "Turn an agent stack (a folder of BasicAgent *.py files + optional metadata.json) or an explicit list of sub-agents into ONE import-ready Microsoft Copilot Studio connected-agent solution: an orchestrator plus one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. When an agent.py carries its compiled CapIR (t2p-capir/1.0) \u2014 or one can be recompiled from its seeded data \u2014 each sub-agent ALSO gets a REAL deterministic capability topic that runs the same steps as the agent.py's perform() (trigger -> the user's real query -> filter the seeded records -> branch -> respond, plus the document for artifact capabilities); only the data is mocked, so flipping the in-topic Table() to a live Dataverse / SharePoint connector is the one-line move to production. No code deploy. Bot names are auto-capped to 42 chars and orchestrator channels default off so it imports and publishes fully headlessly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/connected_solution_agent", "rar_sha256": "63b3de4722f83a981745927a80ad07804dfc42815b05c79314d8a6850908aa0f", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/connected_solution_agent`. The original RAPP
agent is preserved byte-for-byte in `connected_solution_agent.py` and in the RCI capsule.

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

Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "capir_mode": {
      "description": "How to build the deterministic per-capability topic inside each sub-agent (the topic that runs the agent.py's perform() logic on STATIC synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else real seeded data, else SYNTHESIZES static stand-in records from the agent's inferred data shape \u2014 so EVERY agent.py maps to a self-documented topic; 'static' uses only real seeded data (no synthetic stand-in); 'embedded' uses only an embedded CapIR; 'off' emits instructions-only sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
      "type": "string"
    },
    "credentials_path": {
      "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE (under a top-level 'Values' object or at the root). Used only for deploy; the secret is never echoed back. If omitted, env vars / ~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
      "type": "string"
    },
    "deploy": {
      "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot Studio (Dataverse) environment and publish every bot (sub-agents first, orchestrator last) \u2014 no pac CLI needed, stdlib only. App-registration credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file \u2014 NEVER from chat. Default false (package only).",
      "type": "boolean"
    },
    "environment_url": {
      "description": "Optional override for the target Dataverse environment URL (e.g. https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
      "type": "string"
    },
    "orchestrator_channels": {
      "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false (headlessly publishable). True requires a maker-portal publish.",
      "type": "boolean"
    },
    "orchestrator_name": {
      "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
      "type": "string"
    },
    "output_path": {
      "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
      "type": "string"
    },
    "publish": {
      "description": "When deploy=true, also publish the bots after import (default true). false imports without publishing.",
      "type": "boolean"
    },
    "publisher_display": {
      "description": "Solution publisher friendly name (default 'Default Publisher').",
      "type": "string"
    },
    "publisher_name": {
      "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
      "type": "string"
    },
    "publisher_prefix": {
      "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a distinct solution instead of updating ones that already exist.",
      "type": "string"
    },
    "solution_display_name": {
      "description": "Solution friendly name.",
      "type": "string"
    },
    "solution_name": {
      "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
      "type": "string"
    },
    "stack_dir": {
      "description": "Path to an agent stack folder. Each BasicAgent *.py under it (or its agents/ subfolder) becomes one connected sub-agent; metadata.json (name/description/features/starters) shapes the orchestrator.",
      "type": "string"
    },
    "subagents": {
      "description": "Alternative to stack_dir: explicit sub-agents, each an object with agent_name, display_name, description, instructions.",
      "type": "array"
    },
    "version": {
      "description": "Solution version, e.g. 1.0.0.0.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `connected_solution_agent.py` and embedded as the fenced Python below (sha256 63b3de4722f83a98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `connected_solution_agent.py` first:

```bash
python3 connected_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 connected_solution_agent.py   # or on stdin
python3 connected_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/connected_solution_agent",
    "version": "1.0.2",
    "display_name": "ConnectedSolution",
    "description": "Packages a BasicAgent stack into an import-ready Copilot Studio connected-agents solution zip, optionally publishing via the Dataverse Web API.",
    "author": "Kody Wildfeuer",
    "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import io
import os
import re
import sys
import json
import ast
import base64
import uuid
import zipfile
import logging
import urllib.request
import urllib.parse
import urllib.error
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger("connected_solution_agent")

# BasicAgent base — use the RAPP runtime's when present, else a minimal shim so
# this file also runs standalone (python connected_solution_agent.py <stack_dir>).
try:  # the RAPP runtime's base when hosted; a minimal shim when standalone
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:  # minimal fallback
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", self.__class__.__name__)
                self.metadata = metadata or getattr(self, "metadata", {})

# ============================================================================
# Embedded Copilot Studio solution templates (verbatim from the proven packager)
# ============================================================================

DEFAULT_ICON_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACLz2ctAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA"
    "AXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAADiGSURBVHgB7X1rjF3ZldZa+7rclXeFJFL+9W0N"
    "A8oMMM4PgoKY9DUiAw0MVS0BQySkcqNJmABKuyEJCQnYFYYJYhBth0ciAtj+AZFgkNMZQovMCFdP"
    "hCIBI3cGhdYwKK7+1zAdUk3aHcf2PYu993ru606yXa7HNTqru3zvPfecffbZ+9vfep5zAUYZZZRR"
    "RhlllFFGGWWUUUYZZZRRRhlllFFGGWWUUUYZZZRRRhlllFFGGWWUUUYZZZRRRhlllFFGGWWUUUa5"
    "3wTh/wN5/T/8L7N8JeuJaEZEUyJYy5sJBkIkyC/EF5pf8//1PQ3EB5O+yj/6fz62vCbIr+Uw4rb4"
    "EG5P96vtQmkXd2iCJ2+cPbkDe5C1s5fXrv/f1Y0JwMM0DCdyv6cJcI2bp5fyea7ld8/nrnxxsjJ5"
    "5sa5R3bgPpf7FoBrF66uDTduP05zOl0+MtAqWpAcVOU/FJDxZmLAYN1MAYAMTv5H4UUCTAjvy6sc"
    "iwWAZduAdfMkPbQX8K1++OlZ7vtmflsW0Ztp4bw05DPmDhvwyfp7cXJ8Zet+BuJ9CcA3/JP/upFH"
    "/0KehTUDUpmfPIsFgGUfm0SmrwoaWGQusIk2hhMuk+/tO6hsyk1QBXHeGwcBO/+d/+7P/5HTcBdS"
    "GO+7L7/mTD74NBj4wYBegCfvsWJ9qFcR+y0dwouTYb5143OP7sB9JgnuM3nj5379yTwbl/M0rCEy"
    "8fDkDfhqy6lAsn6BMpXEG3lflD9AAaYBFRLaLJejMSFDWgDOQBcUYFa9xybn4C5k5SNfOfHd76xe"
    "zW9Pe8eRwAgZK+sVnMfP/GXer64G2XugzQHTldWfuzyD+0zuKwC+8Z/++oUMtNPCZ5XZTBUysEQ7"
    "CouZ1Saf0EjNmM80cQGqwxAr4zlKGXjkKoNCv3IDW3ejelc/+h82c2P/MYN8Csqw5Gulqlo5eb0S"
    "XieyCevyITKLgvLiKFcxnQNeWfngU5twH8l9o4Lf+PmrZ7IOOsM2nqtYsYlIbTtTu5VNSO0/djrk"
    "/0SgdmLdp+K2vhbVOwjLgKvEIgPZ5noADfIF7nx36+RD0CmF+SZIV8WGkyXD56qMrjw7kE5OBZtc"
    "a9tv6R/qePA3hb1P3frs+iW4D+S+YMC1z2cvdxjOgoCPkYfGgiLtG2Gs+E3ZP6meY4MOhU3FtKq2"
    "ne4ss4vuOgM4J8qG/O82dMrqx65MM/guK/8ypVXVCoozEazfOQXX9+QUjLoTX15lRWeT+XBu5S9d"
    "PgH3gdwXAKQhXYA6zug0xOCRmXJjrgqK+kV5DzyDxc0w3iQGIXsWclhzUlAwCj6RVMuz2ud2M19u"
    "QfeF3LqQm5oik5YSMt6piCi+U89JjMHogZRtyCuNBIQ8EmtwGy7AfSBLD8A3/rOrj+fhndYP1eCB"
    "6q8q4gwQZNjkqTCV7PMmrogjTr5XuzEoMTD+JLKoC9RzUkALPttr+61+7Cun8svDQBjRxVqVV5SZ"
    "oLK21BnWKFIAqiCNr0VWmGoH0E0njn/g8llYcllqAK599uo0hzpOm9opwKvcRmieR4EjGrtVEbBB"
    "Q4rg6hqF0YC9aFVxdU51ltkgFFVJ+pWoOzlLHr2L0C9n+NTk6pNbLJ0ntv9AyVbZdyfv/5LvH2xS"
    "vUgzB1iVk32s7x+H05fXYIllqQE4rAxnisoC81kDfVQqYoAN5i2gTCG0Xmp0J1DYjTzOx5sx6sQA"
    "YjBPB2OT+fjszDwDHfLaj//qBkC4DmmBV1BElcn519D33nzz3J946Ob5P/nmlCYP5U5dVKtBLtWc"
    "JQwhJV949d3ayisV+EsrCEsqhf2GFfpm440OYu4YnMRrNc8XPPNBjTquezfptwi2gf0A9TDNIyZt"
    "W9qvwedBEbPz3bN93u/qx371Qo7rnCLxfAtl53My9ZGzs+jiT938B4+cfbV2jn/ol8/mk58ZSGhz"
    "MKsB5TpAfGKlU240wR++/blHt2EJZWkZkFaoGtGS2cDAWB41pmFxAVnkgq0r9j1qjoPa1RYjvoAN"
    "YaKFcCzua9YaqiOTB+4p6L0WpA11e6VHlcncZOCFkLftfD/wFbn5mZ8+W4Le6nfFQDU3jws2qjQ7"
    "X14WXEoArv3zq6fyy6y1xsXO03Cw2eNo7oEpHoghGDKV3KAMLAZCbE8yjQRt5lpbGJGBzLvNAb4I"
    "HbL6yV+Z5abWIEZRECx9CIq/iib4Cz+8RXpKnAxiexSlHSFrV8wyPPUqZ5MP/NIGLKEsJwMir1jU"
    "2L9CKBQOAFg4xUx5WrSnUJ0IYvc3hFzEDhTPWNNdDAyBefR22dlxFt7J3u829MiAmyBQ53NgsFdJ"
    "SauAc+fG33/kh7aZNfezYEEAkjXErjRik2Pk6+R4Up7oyZNwavkckqUD4NqFq2dqSZX7uJpaM981"
    "BosVdJqb1QEXZnSnFkOgF9H2oZYYqzh5GrlWXceH5iMTbkOnYGFyzfEyiaPleQHUVMNsznW3qY5L"
    "4hbEq9aO2olJA9UDX9L0+PHhroolDkOWCoAZfNNsWD9e3qOyW8xO8BdE5DE9G2c2htADzzoVWlAC"
    "HvogU8ioDMsYQ8suyIag4kkd5YKXbeiQon7z2acQda91lU+sp0sIl3raRJw8aDljkD4CelKO3EaW"
    "beo5533S0oVllowB8UwerDfzW5lxcSBc/QbmAN0UbDz3Ae0o90xEjaPaTrWYgVOp0gKRVgWAgl1U"
    "PBrbzml4Bnqkql+5GlC2Sm7W2ite61G/dc9sz4VgdnF8dcGJYSvhGKVHB37B6trKdXgSlkiWBoCV"
    "/QA2baJJckykDOf7Vj3mvp8SDEqUF405XTNVPFq0mcx+cuYE4CCzeZK8X5ITSdi6fLndm/3IB8zu"
    "3Ggq2DdgXzxx9fTlaR6cGYbCM35PqN61ML7EnaxYO47f5rElKttaHgZEvFJfYrhFXu9wLmwfc/6i"
    "iwIAUXWCYI9TXi2WPYcfQ7icIdGyFOeq0o8EdAk65HVnv3Ki2LKhR0BmC7pnXkA9IHaFdOZwfKYm"
    "gpgHADG+FOq2eMVRqWNEK3aQfUosEZZElgKAmf1O5eGaWoGBx7KUwEwN1s9KiRIWIdlBclokcJQ5"
    "NyB6PacpQJlAYLIwYErKATDd4aCsrPRVvwzzyabXH2qhAGH0E6R/37759/5oV0gnEW4SBZ4LhTwA"
    "FrGKnlNwvHSFVb0yW3n/5VOwBHLkACz3duSBqivS43CeG8UY5yOyMk0O8TPgsJkBcVrUCw7pOwrQ"
    "488hXsY2onkJjQNU0V3ASM/sfryz8LTeICUeEhcKWPhF4nd6n8evdbVXnIdi/1kKDp3Oxf3SNhXs"
    "5lSZY5XIAFtCXUvgkBw9Ax5Lxeudkpc7sfKQ2B2F7IPYb+okoNlvWibP/3h8r352DIFWSStAEYO9"
    "5Hy4SFKg6a2UulTl6tkr0/xywuNzBhDxXNUGze8nqYv9VuD4hl5jVqtgoSRwIJqbpkxvCxb8Gly3"
    "TI+/whGHo5QjBeDaF57LaleCzkF5gAaNzQHIiX8ZYrLiNwFKKBYlqZZRe0+DD5b6xfb8RiASbxT7"
    "SWxAqS5hX7p+QZN5F1hoPmzwVYCrPsL2AmXz6ur1PvWbcN1cIe6U1EOqDxU0hVyDaQ+0deh6mJfA"
    "6dWfuzyFI5SjZcBb3zujHoZMFksMEKOGWKj1dhHJYizB4RAbEC18Ix6zMiVaop73Bq4NkCSJkCFR"
    "0FpJbyreudGpfvMZ14OqlwJWBkrCiHvc3j376G5Pm8X7Nda0+CFKjQ6afwGouhnk3hGUSJMV6Jo1"
    "k2Uth3GONCxzZADMtt+JPBibgMFR4DyHVrSgq5jwB3aPrAWdIagas+i8yABjGzpT7hlzC5LjjTQZ"
    "ihLqh271W2J16KofY3CbYgAT55d62jz+4S+v50PXWgZHBbXeT4Uh5mc2Iei9Vh5tAmVAfosbR3k3"
    "3dEx4CRd1tlGqQNAm32CEDaxmJ4wANuHHq8z417ScWiWnA24OBRWp+rAbXOnrGndGQJR8nn/NFyE"
    "HpkPM+6i/IFROSM5qcas/253tTmkDTdwXa1GMZWhy0VXMiYNgNp1W8BUUDgHdgKPQo4EgGv/8jdO"
    "FSN4YbM6A2heaBF0KAV0gkVYowoW2614e5IuccAhuDNCmsqSsgMLu4jNB3p3mqo8ev76J04+Cx2S"
    "G94ELZNCcvJbDMBk9Xvj7/Y90QBBA9ru9CsKxQasJolEDkhTdWgxAw2AakSAd9BlXdp/4C8+dSQO"
    "yaEDkB0POhMApSDBJkiCDjeuQ5FyKJlSWphOD/iH4lJsXRs+DoMB6OX84ASCwsDgnztzv8X7LaES"
    "7YvqPvQ+qhOQv7zY1eaHn57lfR+Uw3AhEG2OE4mXo+cEO08tWtB1Z2EhvjBHICU6exRhmSNgwNub"
    "+cKnYsyxj8m2FsSgMYR4KnglIC9xrgm0WygAYqRFIx9s0aUQiNDUnsUIXSWZGJCl1fIpDXgJekTU"
    "r/G10o34BQR+3wrQrWe62kTJJzdFB0lITdmQWktCTisIq8/MMUa00eI/NVjy39rxm3Do1TKHCsC1"
    "L1ydwhDSQJ6vtWxGVFSE4M5JEB8+US8BrJHegpMhTRsXoTUVC/TQLHZ1lMvE7bz8N39yGzokpbQO"
    "CgmPtOgpKdkNSfD1XvVLQwg+K8w0/GkB7dR4ueKQoMUfFwfWQzly2XwAUfpbhx2WOVQApmHljBW5"
    "lA0BWGiFfaxqw/2+QiFw5yLn/QFtaesmDGnfBry0COYQSGt3FpbMk7sNHbJ29spaPmBDl4c42sw8"
    "CaxOQr641NPm6z7y5RNmK9vlLWRS+LLE6Wa701jNq641iEWgt7SiUqJb2eXjHCcX4BDl0AD4ln/1"
    "Gxt5aE7pZx4VCZVoKEbTX/rYCUcDH7MAHh5eeVQHNlFeOSyoWFTy0Y8e5KEGd+hqvzolQ1f45WZx"
    "FNRIqPSXJJCN8ggbMxnKc4+2e9q8jcc22aFC8NSbWhqyaJKbEs1iRL+WWpDARQl8ZWyNkhku9leb"
    "mq3+lV+ewSHJoQFwwPQkxPssEPkJVBQuPwd9PaCnr2CzJtploSihfq8aPLIZaFhGbC8HL6IqSTmA"
    "3E7UO+NYDe++8jfe05WpyLJu14HKeE40Pvm4c/0XfqrLoy75ZPSb9ALFiz+Lxm6NNlG2I0uPCyEC"
    "SH0ZKoBJ2dqPLTfsDYcWnD4UAL7lC984BSClSayCIgOCpNO4uAAsC0GNziXbDzDmOMXOG3RFS7s2"
    "XSmZd6uRQPWXZV+ePPmzaG7ZL/U/96UEdFW9yQbjbfc+a9/7Atofe3qaDzkhKwm1kNWBeIdBgtG5"
    "AAzgT8L+svBAs0MSrLYYlaj1/HrigQ9+6VAckgMHYAm75PE/Uz+IFxvtYU2XLVSxFJG9KH6wmFZg"
    "NGQzC1ABLUa1mEeabtP5954IX4k+0n2t1RyZoN7sxywf/ya9HJCSMEM+SgimACBRXz6ZVtYFFKBP"
    "RfDqFqHaFNSxLlqPEHLiETw6owgGbNKfHi1MaofXxXco1TIHDsA0mRfwTSHkOYqQE1yIpogefZV2"
    "dOWK0gBdzTEksyAStdXjOdSDKUSHZT/pRqBaqGBc+d68t1BgExfZyC4pRfW5c+Pn37vd0ybCsHFH"
    "k9I7MZxjrR+AaYBkLC+ecH5J5Pk6gXUSMIMWB6FeC7COwTetzCdn4IDlQAH49suZ/QhOqaemowLg"
    "F2xbHH9Riy14rUH1yjNhMCrVYBMCs4GEd9g8FNsRie44D9gCwaTTur179mRfoUB2QNQh8jbVPiO9"
    "EMo27nZPe+UxbsDl/JzdAJA6P1XqABaUFpYEjSqrdjU7hh1mOw4sfKNsDcFT00QQ4xPw9Orpp6dw"
    "gHKgALx5a37GKjfUBUQtfQLwAXWNYEzH4rV+UkwpKSQBptk0flIrOJA5YeqLpwMMoQjLKJg3LARJ"
    "fcHn1//tr85KYL32PSGpxwHSL5Tcb3k74O2uNgFuzeTq0cDHKXBSD0eAQ8Z+XnABbjeCq2wGFLkJ"
    "o7YgtvsIqCV9QzSfX4ADlAMD4Fv+9TcK85U/0uKBKjx0C/EUCss4ZImquHYmDWUplFHvxqnsQI5a"
    "JTjSmAs7GKTMIIwA+q/GJt3AX4E+thqQNpGBZh64A8Mur5xk58bZPvWbe7kZk8hkVS1hUMiB6WCz"
    "3Lcey2AjBSdYgNoZUgbVGLH+4ys2M/Hq6YMLyxwYAIsRi+5chIp0yV+CfjQ4CQPy4bjQHraWtkyB"
    "paIUi3Z4c98H8wcHaEMCj6HIdCEnke9we/fj796BnusEmpFBDqEhE4g+UV8+uQS08/4zW6DSUHAa"
    "uPA22ckQxNxVOw8sBGOFChBVLoR9EX3V81iCHYJ1AsuvD+CBseCBAPB3/NJ/fzxfyZRNPi+fBw82"
    "K81TeLYx60u0/JutYEYZufpezOUC3hGkNjQIMqp6rF94XjbuDN6Lwi0XoUNe93f+04l8kgdJ6hgr"
    "24MUToBdacX3beyrJ7xx89YGKd6wDZBX0IEytTK86FaM9xurfej3gJj5LdeOQU035zBmlLGvhQs4"
    "Pf6hL5+BA5B9B2BxPPJLjSFZOlyWZ92h/JvEI9V4nhrsEr6w/ewmIVC1Yr60KyMkY0Mw3esSGa42"
    "qZVIZF6ytcw0gStD3326MNw+xUeS+JtqD1iP1eX69s2zJ7s8akyTdTEJzHy2MaA2e2HRI4BoPljM"
    "iUEnbSljAoDFOsv/ye1UzY4E54aA6wkL+E+vHUBYZt8BeGsYzpSgs1haVt3M35IvL/M6PV2mTImq"
    "axtm0WfFAAVvEyHeySZbgjcMclOHe4ZOjRBsUVFMdcdne9Vvjlk8bL2wlWMxv2hS9AGau/swBGCR"
    "OhaWDWETBkw1gME9mDMyDBqQj2zv46SgFrolYVgJyOu42livXYcH9p0F9xWANewCbEBb5SSq2+Hj"
    "BSGVpms6zB5zn3zEwGqSnA0GZKhDUqZVlYNiByVXudpmVftJJ1K2eXn1JeiQ1U9/LV8rnVDPE8GZ"
    "2cM+mh/su/PttZ+sT1Jd47wtes+sYQOmmibkC055WPR3PSo19X8QQzaqg5N6OH4JvpJlSIQR85Cd"
    "3m+HZF8BeAvggnKM2iICKKM+kO1lp0FdE0uH8dga+AQ1rocoxLdkF7OtfdLJgmG6n5CbMkViRAL6"
    "nHATxTQ4tg0dgnhbMhULDGzrzBYbrHYWNAyE6wwgKWs2Neish6JOESOQ+BJtXaLhzVSBbAssCopg"
    "SqgNgzIpNkaEU0C+2v0NTu8bAN/yb3O+t9yMLR5vsmpjCQjXvQIDysrVi9Z7NuK1m60TLWhs7BRP"
    "4dXAdCKzK91WtOH7Po4H6A3w+eX56x99V1ehQLaMNmJD9TypbV84pDugnY9/WDuO5t0KZSUFJjeu"
    "9Ybs+qNsMwcNOA2n6UAMFrdY5sFdD05PGPdkIA3MWf5mr/1r/37fHna5fwyY0hlWgRp2AYjxP+YK"
    "UYl0R5TFwGjerLkEwmZKLBSydQo+bsAcGfQyL2cmub1SDm5sIiayeltFX+43q9984CxysYViFrzx"
    "nNq62NXmJ6/k9ughY5zaNzOXVRNg1KJ8vWJvlm3JuFwwk6RYVawTUbnBO1Lv2HV+0DZR9Rgo87Y5"
    "4ZPlhxZhH2RfAPjWp36z0PIUzIggM/gZJFqRIq6HQ6hevX5pXjBaWMUCMVZhLJrIlDto0F4sPxld"
    "tGnR85H60f5vcvtGshhdttoEhhlJf42JbQGAgz6/zid9j3JLE9iMCNP4Ekb1CAE5pibA0VjfUxxd"
    "Blhlz3B3HLjHy6Mmf6DOCKt+CvafKB/t3vTGy6v7Ui1zzwAsjscA9LizjVzU4o5qu8XUY91AoIxp"
    "oZRY2xZsPF3KwNrIyIDkPhHyYHawJclPT3rjjqM2yPMvP/HubeiSYRPJDX4ABzqG9/kcz/TezE5y"
    "55vRVWAoBYnatOLkyZlTZHNgoMkiTFpY3rKn28hGmGbS2P5Jv7ZLJCMLBufj+8GC9wzAW5N0Jnfn"
    "zer5+QUiLHpyrFUhblWfV8ZAFC01A8fgMsIDO09QvyFDR8YaUQVrvSBqPMPAIv4i9tX+Ve8XcVbY"
    "U2xH6YMhXa3Z8ii3iz1tvu7slfK7btPIYxDCU0CWK6zkzzYbxXNbaVZKbq3I+BAsLLZalKrwCoyr"
    "40ZyDv5M7vDI/hxThLVXrr/mngtX7wmANehMdMoG3emgdnaQmBIFp0NoXsI00ZoBZTH9BNqatucx"
    "O1GwcrLmpGCfKarCpCdSEJKzCXBG5hJ0yGQyzMxmjNmV0nixM0nNLMSVTvWb5RSEBJBM9aKKpQCU"
    "Ruva2KA8rgRCyVlykJo6VUVh5oOfUk5rEQOIrAsa0uKvctOn6m2j9yD3BMD5JF2xqHqETshr18VJ"
    "4vrHooQF0SHRglWfCf9RQjC15JEuNU7qO1TmwIYw68l54JSdvB/8FK5u9ZuPXPfgMIVUiiwfiQLk"
    "cz3b+yi3AfE9qgHCiAT9mAJYBH2ullFr+/T6azBAestdFvBAeMpY4EkHexOklmHTdkGcnKDLy9/k"
    "3sIyewbg27703Kl8mdOwmmzKGW2aCTfnQvKxFFearUwPyQCE1WtAVhE9IB/08R2k65q1vLvMaCsW"
    "RH0Ym5K31Vmnt/bklbXM6ut6fdZubTqRMKKcua+cSx/l5iVqyVJpFgdUs6JeT9ADtij9ESDVGiFx"
    "JHiYzIYGdDCRORkAbq4AxoXO+IvgdMZ0pqbZ6sd+ZQZ7lD0DkNJk03radJo7amkuapUKaMyJQh1R"
    "3U+dSFczWnRqQPSBImXHaAfqLnIXjpJTBCFCMAeKDqkTP+8Lv8znD8xQqqDiOpH+o5llub/p2K3t"
    "njZxktbF3tW7fY3OxUauY0a+ULFtwFguRKKDExjULITqGG5KE0nuxxAusgN4LMFmcZESaM8suCcA"
    "vv3pa9OCfNA6OwuvKGNRy2r8ORh15iNg1NU1eMrBZTuXgdgBrqAiACuEM0YjivvYILLGxMYxZvWb"
    "t3/niT/QFX7Jjsy6nsvVIUJkBAHPzvWP9j1LJu+8IcOlsLb5hgXi0ssD2+hAMHK3nb0oQb/H0LAx"
    "nx6jRQmksVdkdAj7ieoqTrYPqLc/26tHvCcAzodbM1WrcgU6uWigkouM75u3uHAfhzglqBkUCIBx"
    "NSN4BNDolYcSksTl7uguaHvBgtIvchPDl6BTcisbCnhGO0TQkXY2v+tqsz7KrS5k8CuyK/OQklwp"
    "L3FfU40TJaeGqGsMz6j5YQ2lMKhA83eoKhm4OoZDqKJyxQFHdeOwWXwK8hvfe8M67EH2BMDc63WZ"
    "aBkkM23DIMi8JON5CCsSRX26jRejLKLffP1CsINklzognm6yR7k19hPEJqtqJIxGQdl27DJ0yOt/"
    "8WuzfJ41ir00G9VgqafvC2ivTGagR6pODNde75OOGQpTp1hznTIwzeLWfdVrVbAhLnYUPFwFoQLJ"
    "ZojwDoeF+6BxGYosiqUwYw+yRxuQ1mwZhZRXBQJRMBaAf2I1DpBmO8DSdhBRqBekrCJQ1YOdFQ2x"
    "2My89VDaIgMdgj2LRuc0r/bJrUmX/ZfjOJsWp4wgDM6X2G3XXv5437Nkcq82oz0V6J6XqD63xts3"
    "D07tGFv18txoa08toLJpoRZQNYWynqnsFKwWLI/Eltbt2NpLbG50cqdyCnuQPQEwn2+qPSoxryRP"
    "cAajeDe1SOOAxosCOh2nyFYMorDwhLgMNOo/yCgFtkOI3ORxsIBdYxAd9TyU27tPvLOrUCCVMnnU"
    "SkTUNB7ZGdxReqanvdVPX5lSvfPN7WPhGh4z8DVVPWzjLwaAHkCCnbjK3aN2VSTqiDQ6AZJjXkhY"
    "yuCDHWdpVDOrPZkcX3Ojh2cD8sUB6aPSBiurDyaYEBlDygsUbKLEaSEbADcddRLqWzTKa4Aq2RFW"
    "QxTwrefUPkiWBaLBmdRWTBehQ17/5NcK+KaWABOfB9VaQ+Trqe2mSz1tTiCoX51+DwqHcawLz276"
    "iMSna0rHQxejPA+Q9DtxdwVPwtoJLcQShwbdRZaOaKwzBqLd1pbu35Ft6ZU9AhB3AQKtAxgzUWQf"
    "7W5dbxJhoQgOhqCFSIqoKSfb1dBWA513MyZEZV1V3xF8KMeiPxZXxpR5bIKTZ6DnatF+8837jRBY"
    "CDQT9PzLH3n3dk+b+YB1CKwlTOMqPYLD6MfxCtjAFORYWZj8yZhQmUCHNUS/7GLQlir3T7xo3jl5"
    "6AoNxKJzMD4I5a5lb04IwM4dlK/pOBAWcv0BynR6DbpNQcFt2ljJqwEn3FEn73XAxDlxKpD9pNpZ"
    "JyCqFTtfqdP74Dt3oE9m0cQI9FPPk9QmuIufcc3HrlfGLOm7FAAW/gdcLEpQ9DftgBp7Skr1TTJA"
    "g4b+IngC42KI9YCBTs3MhA6vEEnjU3OvpfGvwx5kbzZgzhy0iV8NHGiME9Bvf0S3uCxXqcEFsH0a"
    "4961QpsvroFei29bKZTNR51MHfh4YGwcqmOCnU+9f90//s+l7H5qPQNwdcSgM2JO0BfQfsMv/Jr8"
    "6AzpUxqIbPIhjgO3byYDuKqr9Y3Y+C0Us1E6vsZcr6ImBZTSCCnjVjwlYBtH7z9WxvXFZ3+s9qEz"
    "7tnK3hiQhq/LBVBzWSk8Bk3pGrhMnntN6HaJHIPoVcyOkwW+AvPc1IVFr6AJekPdBCZAa5MnzvKp"
    "lQjwWF+o5PZwSs0Am1wM81rOx7bf7nc+/Ae72pyXO99URWI7HBBsX7M5In+3jp6NG7mWdSCntlQL"
    "ARrQGEEkWarG8IzM6m8k8BAMsBMCgI1GKSeZT/rSmYuyJwC++MiPbudO7zK5u+uhlxQ9OKOjVsjC"
    "LE06Tb4NdqRPiHlzrXNCFFdlAJ1Shs4KKb7Loc/2qt8hpYcb4khO7pFxBuiufCkyQzNJuK+E4XHC"
    "KVHDhDoAth0bE0fuwkMPxehFe4EugLFYLf0OQXtdsNwygtuR+rUxrdjrofJaXrt/wnZR7sELTufs"
    "wkSit0rhc/Xikte0uRFFAblqynGbtDAoYJMV4orlNBIO0eAt6Xb1TpNFy1EZgDqfer/22a9N8zEn"
    "+Aokwc9lWEI6auhTTun2VVO//tNfzeCjaRMZYJIORhxgZCn5bTgKboKPW3lJSRnRhrwJbcmYBGeP"
    "TSINJXGYByJYMYI59ieZhvP4b+qLJrya7BmAt19J53Ovd8E6Hi4aAuthCLskdUYIEX9w+80OgSF1"
    "OxmG2f5kwJMBGIL1Lp6wPLGgYLbvF4qGOfJvviFaaKcuLuUhdMt1Aqt9+eRJ2qzTn0xRmBOnAGid"
    "OHOiWg+ZkUmLC9dvMzCGJlXMYIH9MhaJHGJeNVTPFW6uiqZS7bD60GihmudvnHm4azxfTfYMwN1H"
    "H9rNemcLaqerHqQQZJYaKZ0z1KchmGXoSzECzUIbZlyjqw3ZJ7h0ZHaLpbAIWlsb3RbgoQfc2f1A"
    "351vyLaaMBIJODRjEIoSsvfbG9DOR870HQmDc9cRzc5VTuTd+DLAmRHMKqTGPmPgxLyRfIthLEFU"
    "s/GuhVt0HzZtEZp8r42vOIx2PMFJuAe5p4LUF//4j57LfdqxwASK7iNfu2ZLu9kKHkAxFJr5oxOg"
    "tiPZf+xI2HveHdT7tplKiSh4h9SCOauLvgeEF/VLxPdpQPAg/URg/IGdPzrz+l/86izvP1UtYMhp"
    "MiGvUqShbKZ9UbvZwOPgkg7ZHzXebwhZGYu1tizE4dJytYQeWQgx1fx3ca+2n8o93xOSe/5YVI3o"
    "g9Pu6L6cryxQbwTCSrb9vZMyumS5XAh2oJ6rLUqw0EOk2zJ+NFyCDpkPk5l5PxhBF21bbnkydDog"
    "mVFVbSureDP+HgNj8dmT2Jsyvrq7mwOwcNegtio3nYNnm3zczGRPcbziK4TBQy1sAB3z3eMrtAX3"
    "KPcMwOoRA2y3j18jsCdg1W3lH3M4jLfkc2Az2eDcwBOuKE0e86PAqWirOYz+Iph5UK/tvv/3b0OH"
    "pJQ2o/0T246BWyqPcnui91FucjN7CvlxHa9g8zmL2ZGKWl1eTnYp5GYVSDYo4CEEH1H7V9lxEDAm"
    "zSyBs7Lsrwvfj07pXPevx/8A2Zf7gnNPt9AmBJqVhgFY8aLqZn96qA0iKOHEeJgONoiaZ7WEFvMS"
    "YxuVITCe0g+nzlBJVb/AxQcgbZLGnlPDIgUAF3vaXH2yeNQ45Y5oDll62YANdByZcVLjeOizcw0N"
    "kfkaz8EXnQ5pTPGp3WwGoTmINZyToppv2+T+7LzyiZ/cgn2QfQFgYUGqLNhihUVZQ158sNsdwJis"
    "TdFZlkQrRBBiC+RZk8XVboBV0Kahr1BgDsdnpngwdk8n00E4udX3m2+TkvsVkBAuLDAAA4WqhLq0"
    "lMUwZjzIrpH7kjwMpYBJHpaSI/hEnD2BsHrDlPFo2g1fDYh9BLgl3IJ9kn17NMcxuP0YaLiCL4ca"
    "g1VBtKByA5zcHqwfgH9ePNTEmedZPzvIsAU2RAB7i/TS7vvfuQ0dkiawHvto4DCWkTR8CWh3qt9s"
    "aK0LrLzD1WECY9l6xuTFFTLf4CGUcGFm3RBG5RjsGkvv6XwooBI0dZyRFUOHdeHGMWST4/on3nMR"
    "9kn2DYAvPPKOndzJ857vBfNW0TkRbRL0QLR/4nqFVs35wGhIx8IE4FkEHU+/Oskb8+2gXXG6tQtX"
    "y2++rZv3J2SjCyuaC/PsBfa0WdRvfjnpC1IQJ+/5mhKHd3QBp2A/o8QB5bMH5FFDL9auNY2+KFGN"
    "FQ2DoQ1646y5GWRsSra/DOwDmIlmH2VfH892+4FjW7m7L6nuMk5SKi8ij8dw50REBzowIrhZw16g"
    "bmrrDknsvsBQYNUgpL8L0vmjM3OCh8u5krToKhJMPaqsrPQ9eHJlUqpp0Ct57OoIzWYlKdZIXmQR"
    "xk11n7ISkT29qvaWbNDcwZHQjQNZztYGxDSHjB7XdE1D0TsulTsX98PxiLKvANw9mYPTBOfuVLW8"
    "YknVsq3CMNDKkyGSrxvtVQDmy5usLWNXOydZq6JGtqFDcIANyQhUqRMhcTA9tyyw7oB2tgA3Ne5i"
    "WjSW0AdnB+MTv0CuQ3YTW66iQtkz7tPahnLl3FfPmNj/wnSySHUVq3KKNqW8fX4FJluwz7Lvj+i9"
    "fePY+cKCZrsx+EDfavxZPns+NTlD8lfoZe8Y0lU1Ie+3QaExJ9gqF9UhrFp2S1/cfawvU5HPv2Ez"
    "peqLXP0awjtzv8WjBpBfUW+S/ABaagVRzSXz6PWmJGY9Oa1oAjkm3KYJ5hGHPC5PL1qEStpPoI4L"
    "qZr11QvB7uNTybnPdz+6+C5k3wFYUnSZxs4GFrNXXuTuYfFgEqhS0ZGqq91IwLBkpja6DQNmz4Sn"
    "KKBPqMSl513qN9t/szx5b+Jf7QRj3NAD0HMOnU89nd+azBRAeg2mBfQaBHSgwySFCqCsy+ck1Htv"
    "wMKSGAYFklReeIxUYrGiimULL120uvp6LlLVHZiPbK5w5/pf/0Pn4ADkQH6m4bf/2I+cz1e5w4sO"
    "zYZw+yLmexyd8RWDSjERK88dDs8EsJmOPq2VeMWGmff+6iVumpdr6hGcZT0/eu3lD/YFtEkrnzEA"
    "WM8WFiKY8gMAM1MErPJTteZ4JS1C0HAKWF/5Di4wrxllHPRY9r49YuVFEa5+VeOYCp5kQjkgObgf"
    "qskpOrct7OoQjeUwDBpGTQIg1pA+ucBWpZTah9BCC2CbCEdxiU9m9bsDHULl93kDuQICRTsIVE0h"
    "PQOdki9jA+BV+ifea9UC6MUUVnoVNQi0iwvBQ1PRLhXq99wumt2oXy20F7Y3Y6f2Y9XxX7z+4Xdf"
    "ggOSAwNgCU7nYXgGwbxXFHVGZjS7pS9emEg9iMT8kpUK0IQlJPTSRvdBsSfeXHk76XtGX1G/ua0p"
    "ADQGPVgQGEEZPM378slv+EdX1w283CZZP2EhwIzQBNVdIziY+BhhshTZOcTwUgCWhnbQXF1oNAy5"
    "qWxj2IAR4PiAT8AByoH+WGFJ0ZVXu25svqOgchpj2gEAjdZSCwg0nh/0hrKreooO1s5CgXLnWwRI"
    "UEa+Sy2I2NntVL84mW+wmSBNCcmpaq19Ts42ykamHFAgp4sh/B6ddsjBR4G4dbgt/y5VQqrCw+2w"
    "Hvj24ILeg4J48SAcjygHCkBN0dWh8M0+2LUHyR8qXj+j7RoMRYeCDprNAzmAm3OUf3F79339d77p"
    "WTCep1HpUCpPt6FfZv5Us7CYFOQJo63VZib0fJGQZZFFdQzW54Xtfi6BIal/591BDcOA2eZkTIs7"
    "OX65BQcsB/6D1TVF53d1sVgaCKKn1Qyy2EONs8Lz4U8JsMkTsuB2kXyQsdf7PZH7+KBRH5oNKlPn"
    "bJ0o9bX5eVXpDC7N1kjnUEwKUtOkyb+GfkjWJ9KajQcEFtNYCvjiCYAMCymq2SSBbyUFZsAaGkoJ"
    "tnrTjPciBw7AkqIb5vAZW66sLZAfxAgGMvT8qth7GmSWhkLONASjg92o8TQwQA846YrVQSmT50kg"
    "bHS+VyjLhO/u/uw7+0rvadjUybYfJ6/3AccYJWDDfHIdEfBoiwvVY4005iGpeG8MOmJRzg/xnFqU"
    "ULrErcQ+lJX3/HeeePdFOAQ5cAAWmb9mcpbKXXQKmMRJkcELn8PyZTFjiT9YTEw9Rt7eHIZgKah6"
    "mp3d9+X8dI/wr5OLZUBSgQNigYUQCvarX+Rq6pCvEbODPN4p14nRlkOwfK2xm8b/MI5VtAttUWME"
    "WsO88tMLYay4S4vpwaKOE6QDdTyiHAoAS4ouDXReU3F1YoF/IkovvfVogdWzqhLgmUwS2Y+qyp5U"
    "L8pSjZu8Z5+q/MLVKZQ739QjdQPc10PSRwFDt/qlon7RMjMQY4vuwTIkteiBHQD1XE3jolUA1f18"
    "yupbBXQsSoBg1ThLquEHen9LCN+gxhsz+C71PrBzP+RQAFjk5uqxc/mCX7IgNPBDSmKKCaMakuNQ"
    "980TNYiNTDFgI+CQ4zibmrfMO3+hKO+4oWlaZQe1CaRJtIB253P/sue9gYGFNPUFFj6iCHA9tYSm"
    "pCgBmLWCXeraQp5mWscvhaKEhTviNLNBSTMdaoMaFxv7idbACc234BDl0ADIhQp4VocdjRXqJx40"
    "fxtUiaxUijWXyQ1zV2F6CNZCgT/7432FAin9Kdf03ka0JeX77d58cqawdQWNpnVBWkqoGhZcVXox"
    "gVUw2xHuiGFzDpCG7dLVvbFBsHFEqYNBLVSVQWrc4vIuwdnDcDyiHBoAi3CKDnfU0A6mjMQqjCnA"
    "h5vA4ldQftKAC7o0Sk1hUdtxqc9WW/vCc9M8ACf5LCwovynXSGWxvt8RyR71NB//YD1M5tWfKe3V"
    "NcG9J0vVGRBrRyRJnv+diOOSQlAa7dEedoM5BtsSQrwxDI4AOzxXJsnT/RGuHbt9vOsa91MOFYBF"
    "snp8zOtxPUkvX6Ol/qOhrstfDBojAwniGnh4dKn3zrcJ3Jq5sSRnl0w9AMaYJHbnkwfYqMotqEPU"
    "BybZ/xq3k7ahuQ+XYIHRFMiRxdSuNLgljFUs0MRHRW2LCQBi0jiQ+cI/tftEd8x03+TQAVjvossB"
    "Yqd+aADAYx0oyAzlSEsUFBIfG8IxOy/+md+7DR0yh/LcP4nIKRBVjSWweCOWgHZnPjkft17uVOOO"
    "ub2LDIKmvErU7GIs04F6xzjoAIEDW1WqwjkJ6yWJl1r+HLxPKFklC+vksMuH3nURjkAOHYBFJnPa"
    "8kBqAJioo+BicKGWvLf5SMnTC/JTAigMkD3DZ3r6UNQvlsfuArTgxkDGAoKsoy52tZnVb0bTw6Gv"
    "7ufbAguncRbkRRTSgHxeoOYZLQpKK68ia1xjo4FWOYQkizXETo19dYENAI/CEcmRAPCFkqLjmJrH"
    "wIqQxsAAFgxyGVVs8CFv7JFwdWA7f3Sm/OQqxELYCBBRd7a98843kHQeh5TQS+qtfArseX8QihJ0"
    "AfK1Bs8Xmke4ATil+gN22qIEvw4M2jv5ry/p9dn7HC24/pfftadn++2HHAkAi0zmk8fKa50sSXnx"
    "o88i/wFEBhFF1dwDonaM7LT7rT/9Y50PCSo/uaVONUILxMDEiM92q99JKWiw/qCFd8TmU/CAQgAR"
    "Fm5UEtWql74ASo0Xen2gt1i/c2dH2yF9Xgz6fmpvlu8S7X+Z/d3IkQHwhUce2smDcU4nwh7Sk7RU"
    "nPdT0EHkJKWDsIsM/DZ0yNrlq2t533UtFABsbicVAgSpVOn7zTcOaONsUeUqU8UbyMUeDOoXwRdU"
    "rOSBZh80IIdsXgr0aIB3lV5HzSpeilgVUXmzdRePKT4QOTIAFrl1LG2VB13yJymA5A+Ixg46UR68"
    "VcvZftdCf9Aldarf+WSG4I+mALAJgRpjtIxCZsrO33yDW7lNBkxTQSMqOVyL/7CgXgtZkBnhjsoW"
    "2U9KqMBsktSoVDVB7OZ9bpOwcVzMIall0zvpeDoPRyxHCsASnM4jcg5sPRNEJgKIRQn8Pb9FCMNv"
    "+71hvtqZqVhZ13yvN2BqChXcUAPa7+yzjzKjWqzF7KukxaPmiWp4CUOYRoCiuV9lPoLopAlRyt6e"
    "/RBVq/eZyEPPCc0EMAqtalsrsbP63eq+UesA5UgBWOT2sbwKMX3btCo2uGqIQCtorOJZmEIMue2d"
    "8szCDslRsA2dIG5Wz4sgT2TRSuzum9nzvhvOXG5CgJkN9lniRpa31mtQ5qOwwNp4ojgdnLXAyLQO"
    "4IWMiFwfhXxwOXbnOz/7zkuwBHLkAKyFCkCfCjaPDaznLbH9rY+UIBrgVAHT99TTt15+bpYPWDOG"
    "ldxxy1qsztLQp9Lh+PGHGydiwR7za1NEgFMlur1GkfGM1Twwb+5Zam1WvRK1pZvz8WeM58cJnoQl"
    "kSMHYJH/9d4fKTez77RsIR5dFE3U0yAspUyYoy8rfQ5IPmJTvEi5TyJ4wXWSVDPj8y++ry+gnTG7"
    "AbGrkf1aVlS1asUBjFLxdiVn2zSO6I8mUUCJV2vKwkI74EweFoRceWXJPIIXu736Q5ClAGCRgYbH"
    "0O07s/MoFEuaJ1ifiQfMVjyNz+4+0ln7B1ynZ6AAdwIaldz5JFU+vtz5hhFsjd0Hdk+QcF2NL6Mx"
    "GC0yZAq1gACBQUlVM8MV0NlQM4jkWSKM48Ztv5RSdvyWSJYGgC++twSny6RTVEcWybeiBBldDT7L"
    "s+ye7zlHVb8IU/1s4Qjw+0CMVDrzyWtf+G+z3MhaMCGseX2ivKpLe8wHInhJGUYV7Y8u0fyxBq0Z"
    "wWqCcLtBFcfSLbRyLTcHeHtaKvYrsjQALJJ165aFIoQbal41GOe+ujWjZKGGH94+P6HeJxOcJVxl"
    "VThe680np4nkk6VNjKqPoHEWMPyKEyjbR+YDQq/4trWGkVltP7PtdEBA2M6y21bZoxXiWc8cedhl"
    "UZYKgIUF8xBuOzhQfn/YTCUHCgvKfj/xw9qeXr62lhubgajamFlopAKlL58sB8wgpLqcTsEfwaFB"
    "Zo3xJfHmI2OamiSP10D4X/EX7/sF3QYGPkgY15P8ilP1ms8uG/sVWSoAFske2mMkRrqyiqxop4QI"
    "Qh7t6Vuf/q3ZD2r35cmtM6p+rRKF1C5j4eri8m3fnW9v/TfPzZDbxEahiv1moPEQS7hQMHWcghNk"
    "RQhGehiyKW4jCtiaqua2fXFnmCev7W7+xCVYQlk6AL5wMqfogM773azg2QrJAVuy3uvdyr3FF97+"
    "9LXpq7X51i//VgYfnUYHhP1Z2qtMajXg0+63Hv3dffnkROtm5IUwkdpeXJSQSK+DPHuDdbvyIjS2"
    "Whsgd9MgmA4UKl0kbrgQplLwS4zzr8KSyjFYQrmVPbXjA53KU7gmlg6oUQVi5dRYhH1XjfYH5zS/"
    "8ran/8fW8Qk8e32+srsy3JplhG4CSeWL7G/kCaBPTwVNl2WU3M0NORtqJnCDaBlDy+oAxAsA/oac"
    "FUnuwisBErEQCQxcFhgHoGDuoWNWd6bF9mt8s5z64u6f/32HdpPR3crSMWCRev9IZkEpS/e8KYaK"
    "FQAM4QvBI03zh39xc45Xj8Htb+bvLgDWp5M6O2A8E0G4qZtZpdP7fdvlb5zIh02dTdXui5+tHB/M"
    "uVBIesiFCRz1WEmZoZgD6sC0KrxxPpQ9tRDVbMSyz+RwbzK6W1lKABa5mdK5PHkv2WTJoFLIB1dB"
    "9PnhG78xTEqopRPnQ8Dgno3uV3e69OKj79ju6d98KJUvXhjh9mq0wwCaFFjwDorw0xfAOkixKqdW"
    "sSTLapDajAIwbdQ+SymWlu3z4qStu3g0yZHI0gKwsGCevMecNURVhQnEJuwgisp/9FR28UmXqlfB"
    "HYB5rbL3ysqwBb2SsmoHJSj2ZfgZK7BQxQMQYnlux6VYHAC+wCTWaWm4EAdsnimtBAt+Z6GAlFtL"
    "eA3ScBGWXJYWgEX+98mHvphH/JIMqUyQpbQUeBS0k7MMf2IHQIvg+MZuv/Ec5N6I+n7YeqEzm1LU"
    "b87FnHBq1dP5I9dQTQPL55LTtvXV+2x2aPDLa5/JMO7FF8myG+aERNavi7JUuyw5+xVZagAWWQU8"
    "XX4OPrkNx++UabSOUNkmVATbfhJDJMFhVMFcWgznX/zpd5zt7BIMeOxxu6ssebpDzQGzNw0QascB"
    "RHsU7DhtC8EWl5oFCY3VNDSlgWZSexEErF68sLX7M7/nEtwHgnAfyPTKtbXvAV3Jg37CbgABrmKR"
    "h6GLdtUHJ+i85LeDP9JXs1+2f91Ol377kd/1GHTK2y8/N701wW+y95n/HQbV/dp2cEe9QCE86sGz"
    "cKJYQZeP7YOa4/ZQjXm6IeJov45CftwAl/7Pn/vx7us5all6Biyyk+3BBwBPJhguuXklj5lRm8rV"
    "T30lBM+NRuM/+YOH8qdP3Q34ityapDNyouCRU8xQBFbDWJQqTgLEegtgp0l7hKrPXbd7n8EatyIK"
    "Pw8vBvrM/QS+IvcFA0Z5+5X/eSrPyJn8dloIYIBQvzQoG0pogzjwRxQ5r37x9UyMT8gvffafO7Pf"
    "7WPpGijRkQTKB5ITgv9kU2Uv82/8WYNOhUxqwWciNMZjKtezuGutZ1yUXRzwsW/9zI8tbbzv+8l9"
    "B8Aib79SMh7zWQ5ynSmxP1JVpS5HVInkk59le5JDLS/81O+8CHuQt/y73yzge7AN+grRVvCRsRyf"
    "WGr39Mfu/T5eBS00fQbSp33JEWZe+DxJaFCKaHO8NJ0b0ur53c5q8GWT+xKAUTIYZ3kq1gciDgxn"
    "gACR1iLtZHfwWcThmfkwPFuKHWCPUtJ5udGz1FiQYJyEFIwxyWpgu5u/mC3Htp5mY7w5wEX7Tj6W"
    "AH2+psl2Gm491VuxM8ooo4wyyiijjDLKKKOMMsooo4wyyiijjDLKKKOMMsooo4wyyiijjDLKKKOM"
    "Msooo4wyyiijjDLKKKOMMsoo+yn/Dz5AVzqUvk9+AAAAAElFTkSuQmCC"
)

SOLUTION_XML_NATIVE = """\
<ImportExportXml version="9.2.26023.151" SolutionPackageVersion="9.2" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <SolutionManifest>
    <UniqueName>{solution_unique_name}</UniqueName>
    <LocalizedNames>
      <LocalizedName description="{solution_display_name}" languagecode="1033" />
    </LocalizedNames>
    <Descriptions />
    <Version>{solution_version}</Version>
    <Managed>{managed_flag}</Managed>
    <Publisher>
      <UniqueName>{publisher_unique_name}</UniqueName>
      <LocalizedNames>
        <LocalizedName description="{publisher_display_name}" languagecode="1033" />
      </LocalizedNames>
      <Descriptions>
        <Description description="Auto-generated publisher" languagecode="1033" />
      </Descriptions>
      <EMailAddress xsi:nil="true"></EMailAddress>
      <SupportingWebsiteUrl xsi:nil="true"></SupportingWebsiteUrl>
      <CustomizationPrefix>{publisher_prefix}</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
      <Addresses>
        <Address>
          <AddressNumber>1</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
        <Address>
          <AddressNumber>2</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
      </Addresses>
    </Publisher>
    <RootComponents />
    <MissingDependencies />
  </SolutionManifest>
</ImportExportXml>"""

CUSTOMIZATIONS_XML_NATIVE = """\
<ImportExportXml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <Entities></Entities>
  <Roles></Roles>
  <Workflows></Workflows>
  <FieldSecurityProfiles></FieldSecurityProfiles>
  <Templates />
  <EntityMaps />
  <EntityRelationships />
  <OrganizationSettings />
  <optionsets />
  <CustomControls />
  <EntityDataProviders />
  <connectionreferences>
{connection_references}
  </connectionreferences>
  <Languages>
    <Language>1033</Language>
  </Languages>
</ImportExportXml>"""

CONTENT_TYPES_XML_NATIVE = '<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/octet-stream" /><Default Extension="json" ContentType="application/octet-stream" />{overrides}</Types>'

CONTENT_TYPE_OVERRIDE = '<Override PartName="/{part_name}" ContentType="application/octet-stream" />'

BOT_XML = """\
<bot schemaname="{bot_schema}">
  <authenticationmode>2</authenticationmode>
  <authenticationtrigger>1</authenticationtrigger>
  <iconbase64>{icon_base64}</iconbase64>
  <iscustomizable>0</iscustomizable>
  <language>1033</language>
  <name>{bot_display_name}</name>
  <runtimeprovider>0</runtimeprovider>
  <template>default-2.1.0</template>
</bot>"""

BOT_CONFIGURATION_JSON_NATIVE = """{{
  "$kind": "BotConfiguration",
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": false
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

ORCHESTRATOR_CHANNELS_BLOCK = """
  "channels": [
    {
      "$kind": "ChannelDefinition",
      "channelId": "MsTeams"
    },
    {
      "$kind": "ChannelDefinition",
      "channelId": "Microsoft365Copilot"
    }
  ],"""

ORCHESTRATOR_CONFIGURATION_JSON = """{{
  "$kind": "BotConfiguration",{channels_block}
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,{publish_on_import_line}
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "isLightweightBot": false,
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": true
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

GPT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>15</componenttype>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

GPT_DATA_YAML = """\
kind: GptComponentMetadata
displayName: {display_name}
instructions: |-
{instructions_indented}
gptCapabilities:
  webBrowsing: true
  codeInterpreter: true

aISettings:
  model:
    modelNameHint: GPT5Chat

  extensionData:
    lastUsedCustomModel: {{}}

declarativeSkillsMetadata:"""

BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>{component_type}</componenttype>{description_element}
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

CONN_REF_SET_XML = """\
<botcomponent_connectionreferenceset>
{entries}
</botcomponent_connectionreferenceset>"""

INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>9</componenttype>
  <description>{description}</description>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{orchestrator_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

INVOKE_CONNECTED_AGENT_DATA = """\
kind: TaskDialog
modelDisplayName: {display_name}
modelDescription: |-
{description_indented}{inputs_block}
action:
  kind: InvokeConnectedAgentTaskAction{input_type_block}
  botSchemaName: {child_schema}
  historyType:
    kind: ConversationHistory"""


def _connected_inputs_yaml(params):
    """The orchestrator-side typed inputs for a connected agent, from the source
    agent.py's perform() params. Per the Copilot Studio connected-agent schema:
    `inputs` (AutomaticTaskInput list) sits at the TaskDialog root and `inputType`
    sits INSIDE the action block. These populate the connected agent's Inputs
    panel and let the orchestrator pass the params when it delegates. Returns
    (inputs_block, input_type_block) — both '' when there are no params."""
    params = params or []
    if not params:
        return "", ""
    inlines, props = [], []
    for entry in params:
        pn = entry[0] if isinstance(entry, (list, tuple)) else entry
        required = bool(entry[2]) if isinstance(entry, (list, tuple)) and len(entry) > 2 else False
        name = re.sub(r"[^A-Za-z0-9_]", "", str(pn)) or "input"
        inlines.append("  - kind: AutomaticTaskInput\n    propertyName: " + name)
        props.append("      " + name + ":\n"
                     "        displayName: " + name + "\n"
                     "        isRequired: " + ("true" if required else "false") + "\n"
                     "        type: String")
    return ("\ninputs:\n" + "\n".join(inlines),
            "\n  inputType:\n    properties:\n" + "\n".join(props))

INVOKE_CONNECTED_AGENT_DEPENDENCIES = '[{{"type":"bot","schemaName":"{child_schema}"}}]'

SYSTEM_TOPICS = {
    "ConversationStart": {
        "display_name": "Conversation Start",
        "description": "This system topic triggers when the agent receives an Activity indicating the beginning of a new conversation. If you do not want the agent to initiate the conversation, disable this topic.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnConversationStart
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_M0LuhV
      activity:
        text:
          - Hello, I'm {{System.Bot.Name}}. How can I help?
        speak:
          - Hello and thank you for calling {{System.Bot.Name}}. Please note that some responses are generated by AI and may require verification for accuracy. How may I help you today?"""
    },
    "EndofConversation": {
        "display_name": "End of Conversation",
        "description": "This system topic is only triggered by a redirect action,\nand guides the user through rating their conversation with the agent.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: Question
      id: 41d42054-d4cb-4e90-b922-2b16b37fe379
      conversationOutcome: ResolvedImplied
      alwaysPrompt: true
      variable: init:Topic.SurveyResponse
      prompt: Did that answer your question?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition-0
      conditions:
        - id: condition-0-item-0
          condition: =Topic.SurveyResponse = true
          actions:
            - kind: CSATQuestion
              id: csat_1
              conversationOutcome: ResolvedConfirmed

            - kind: SendActivity
              id: sendMessage_8r29O0
              activity: Thanks for your feedback.

            - kind: Question
              id: question_1
              alwaysPrompt: true
              variable: init:Topic.Continue
              prompt: Can I help with anything else?
              entity: BooleanPrebuiltEntity

            - kind: ConditionGroup
              id: condition-1
              conditions:
                - id: condition-1-item-0
                  condition: =Topic.Continue = true
                  actions:
                    - kind: SendActivity
                      id: sendMessage_4eOE6h
                      activity: Go ahead. I'm listening.

              elseActions:
                - kind: SendActivity
                  id: yHBz55
                  activity: Ok, goodbye.

                - kind: EndConversation
                  id: jh1GMT

      elseActions:
        - kind: Question
          id: PM68ot
          alwaysPrompt: true
          variable: init:Topic.TryAgain
          prompt: Sorry I wasn't able to help better. Would you like to try again?
          entity: BooleanPrebuiltEntity

        - kind: ConditionGroup
          id: KNxYBf
          conditions:
            - id: DPveFP
              condition: =Topic.TryAgain = false
              actions:
                - kind: BeginDialog
                  id: cngqi4
                  dialog: {bot_schema}.topic.Escalate

          elseActions:
            - kind: SendActivity
              id: GrVHEW
              activity: Go ahead. I'm listening."""
    },
    "Escalate": {
        "display_name": "Escalate",
        "description": "This system topic is triggered when the user indicates they would like to speak to a representative.\nYou can configure how the agent will handle human hand-off scenarios in the agent settings..\nIf your agent does not handle escalations, this topic should be disabled.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnEscalate
  id: main
  intent:
    displayName: Escalate
    includeInOnSelectIntent: false
    triggerQueries:
      - Talk to agent
      - Talk to a person
      - Talk to someone
      - Call back
      - Call customer service
      - Call me please
      - Call support
      - Call technical support
      - Can an agent call me
      - Can I call
      - Can I get in touch with someone else
      - Can I get real agent support
      - Can I get transferred to a person to call
      - Can I have a call in number Or can I be called
      - Can I have a representative call me
      - Can I schedule a call
      - Can I speak to a representative
      - Can I talk to a human
      - Can I talk to a human assistant
      - Can someone call me
      - Chat with a human
      - Chat with a representative
      - Chat with agent
      - Chat with someone please
      - Connect me to a live agent
      - Connect me to a person
      - Could some one contact me by phone
      - Customer agent
      - Customer representative
      - Customer service
      - I need a manager to contact me
      - I need customer service
      - I need help from a person
      - I need to speak with a live argent
      - I need to talk to a specialist please
      - I want to talk to customer service
      - I want to proceed with live support
      - I want to speak with a consultant
      - I want to speak with a live tech
      - I would like to speak with an associate
      - I would like to talk to a technician
      - Talk with tech support member

  actions:
    - kind: SendActivity
      id: sendMessage_s39DCt
      conversationOutcome: Escalated
      activity: |-
        Escalating to a representative is not currently configured for this agent, however this is where the agent could provide information about how to get in touch with someone another way.

        Is there anything else I can help you with?"""
    },
    "Fallback": {
        "display_name": "Fallback",
        "description": "This system topic triggers when the user's utterance does not match any existing topics.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_LktzXw
      conditions:
        - id: conditionItem_tlGIVo
          condition: =System.FallbackCount < 3
          actions:
            - kind: SendActivity
              id: sendMessage_QZreqo
              activity: I'm sorry, I'm not sure how to help with that. Can you try rephrasing?

      elseActions:
        - kind: BeginDialog
          id: 5aXj5M
          dialog: {bot_schema}.topic.Escalate"""
    },
    "Goodbye": {
        "display_name": "Goodbye",
        "description": "This topic triggers when the user says goodbye. By default, it does not end the conversation. If you would like to end the conversation when the user says goodbye, you can add an \"End of Conversation\" action to this topic, or redirect to the \"End of Conversation\" system topic.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Goodbye
    includeInOnSelectIntent: false
    triggerQueries:
      - Bye
      - Bye for now
      - Bye now
      - Good bye
      - No thank you. Goodbye.
      - See you later

  actions:
    - kind: Question
      id: question_zf2HhP
      variable: Topic.EndConversation
      prompt: Would you like to end our conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition_DGc1Wy
      conditions:
        - id: condition_DGc1Wy-item-0
          condition: =Topic.EndConversation = true
          actions:
            - kind: BeginDialog
              id: dn94DC
              dialog: {bot_schema}.topic.EndofConversation

        - id: condition_DGc1Wy-item-1
          condition: =Topic.EndConversation = false
          actions:
            - kind: SendActivity
              id: sendMessage_LdLhmf
              activity: Go ahead. I'm listening."""
    },
    "Greeting": {
        "display_name": "Greeting",
        "description": "This topic is triggered when the user greets the agent.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Greeting
    includeInOnSelectIntent: false
    triggerQueries:
      - Good afternoon
      - Good morning
      - Hello
      - Hey
      - Hi

  actions:
    - kind: SendActivity
      id: sendMessage_abmysR
      activity:
        text:
          - Hello, how can I help you today?
        speak:
          - Hello, <break strength="medium" /> how can I help?

    - kind: CancelAllDialogs
      id: cancelAllDialogs_01At22"""
    },
    "MultipleTopicsMatched": {
        "display_name": "Multiple Topics Matched",
        "description": "This system topic triggers when the agent matches multiple Topics with the incoming message and needs to clarify which one should be triggered.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSelectIntent
  id: main
  triggerBehavior: Always
  actions:
    - kind: SetVariable
      id: setVariable_M6434i
      variable: init:Topic.IntentOptions
      value: =System.Recognizer.IntentOptions

    - kind: SetTextVariable
      id: setTextVariable_0
      variable: Topic.NoneOfTheseDisplayName
      value: None of these

    - kind: EditTable
      id: sendMessage_g5Ls09
      changeType: Add
      itemsVariable: Topic.IntentOptions
      value: "={{ DisplayName: Topic.NoneOfTheseDisplayName, TopicId: \\"NoTopic\\", TriggerId: \\"NoTrigger\\", Score: 1.0 }}"

    - kind: Question
      id: question_zf2HhP
      interruptionPolicy:
        allowInterruption: false

      alwaysPrompt: true
      variable: System.Recognizer.SelectedIntent
      prompt: "To clarify, did you mean:"
      entity:
        kind: DynamicClosedListEntity
        items: =Topic.IntentOptions

    - kind: ConditionGroup
      id: conditionGroup_60PuXb
      conditions:
        - id: conditionItem_rs7GgM
          condition: =System.Recognizer.SelectedIntent.TopicId = "NoTopic"
          actions:
            - kind: ReplaceDialog
              id: YZXRDb
              dialog: {bot_schema}.topic.Fallback"""
    },
    "OnError": {
        "display_name": "On Error",
        "description": "This system topic triggers when the agent encounters an error. When using the test chat pane, the full error description is displayed.",
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnError
  id: main
  actions:
    - kind: SetVariable
      id: setVariable_timestamp
      variable: init:Topic.CurrentTime
      value: =Text(Now(), DateTimeFormat.UTC)

    - kind: ConditionGroup
      id: condition_1
      conditions:
        - id: bL4wmY
          condition: =System.Conversation.InTestMode = true
          actions:
            - kind: SendActivity
              id: sendMessage_XJBYMo
              activity: |-
                Error Message: {{System.Error.Message}}
                Error Code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}

      elseActions:
        - kind: SendActivity
          id: sendMessage_dZ0gaF
          activity:
            text:
              - |-
                An error has occurred.
                Error code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}.
            speak:
              - An error has occurred, please try again.

    - kind: LogCustomTelemetryEvent
      id: 9KwEAn
      eventName: OnErrorLog
      properties: "={{ErrorMessage: System.Error.Message, ErrorCode: System.Error.Code, TimeUTC: Topic.CurrentTime, ConversationId: System.Conversation.Id}}"

    - kind: CancelAllDialogs
      id: NW7NyY"""
    },
    "ResetConversation": {
        "display_name": "Reset Conversation",
        "description": None,
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_OPsT1O
      activity: What can I help you with?

    - kind: ClearAllVariables
      id: clearAllVariables_73bTFR
      variables: ConversationScopedVariables

    - kind: CancelAllDialogs
      id: cancelAllDialogs_12Gt21"""
    },
    "Search": {
        "display_name": "Conversational boosting",
        "description": "Create generative answers from knowledge sources.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  priority: -1
  actions:
    - kind: SearchAndSummarizeContent
      id: search-content
      variable: Topic.Answer
      userInput: =System.Activity.Text

    - kind: ConditionGroup
      id: has-answer-conditions
      conditions:
        - id: has-answer
          condition: =!IsBlank(Topic.Answer)
          actions:
            - kind: EndDialog
              id: end-topic
              clearTopicQueue: true"""
    },
    "Signin": {
        "display_name": "Sign in ",
        "description": "This system topic triggers when the agent needs to sign in the user or require the user to sign in",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSignIn
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_ypjGKL
      conditions:
        - id: conditionItem_7XYIIR
          condition: =System.SignInReason = SignInReason.SignInRequired
          actions:
            - kind: SendActivity
              id: sendMessage_1jHUNO
              activity: Hello! To be able to help you, I'll need you to sign in.

    - kind: OAuthInput
      id: gOjhZA
      title: Login
      text: To continue, please login"""
    },
    "StartOver": {
        "display_name": "Start Over",
        "description": None,
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Start Over
    includeInOnSelectIntent: false
    triggerQueries:
      - let's begin again
      - start over
      - start again
      - restart

  actions:
    - kind: Question
      id: question_zguoVV
      alwaysPrompt: false
      variable: init:Topic.Confirm
      prompt: Are you sure you want to restart the conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: conditionGroup_lvx2zV
      conditions:
        - id: conditionItem_sVQtHa
          condition: =Topic.Confirm = true
          actions:
            - kind: BeginDialog
              id: 0YKYsy
              dialog: {bot_schema}.topic.ResetConversation

      elseActions:
        - kind: SendActivity
          id: sendMessage_lk2CyQ
          activity: Ok. Let's carry on."""
    },
    "ThankYou": {
        "display_name": "Thank you",
        "description": "This topic triggers when the user says thank you.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Thank you
    includeInOnSelectIntent: false
    triggerQueries:
      - thanks
      - thank you
      - thanks so much
      - ty

  actions:
    - kind: SendActivity
      id: sendMessage_9iz6v7
      activity: You're welcome."""
    },
}


# ============================================================================
# Packager: orchestrator + connected sub-agents, with the 42-char name cap,
# 100-char schema cap, and optional channels (default off = headless-publishable)
# ============================================================================

MAX_SCHEMA = 100


_CONNECTED_INFIX = ".InvokeConnectedAgentTaskAction."   # 32 chars (incl. both dots)


_MIN_ACTION_BUDGET = 26   # always leave at least this many chars for the action suffix


MAX_BOT_NAME = 42


def _cap_bot_name(name: str, preserve_suffix: Optional[str] = None) -> str:
    """Truncate a bot display name to the 42-char limit, keeping a trailing word
    like 'Orchestrator' intact when present."""
    name = (name or "").strip()
    if len(name) <= MAX_BOT_NAME:
        return name
    if preserve_suffix and name.endswith(preserve_suffix):
        budget = MAX_BOT_NAME - len(preserve_suffix) - 1
        head = name[: -len(preserve_suffix)].rstrip()[:budget].rstrip()
        return f"{head} {preserve_suffix}"
    return name[:MAX_BOT_NAME].rstrip()


def _sanitize_schema(name: str) -> str:
    """Lowercase alphanumeric fragment for a bot schema name."""
    return re.sub(r"[^a-zA-Z0-9]", "", name or "").lower()


def _pascal(name: str) -> str:
    """PascalCase alphanumeric fragment for a connected-action schema name."""
    parts = re.split(r"[^a-zA-Z0-9]+", name or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _xml_escape(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _indent(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(f"{pad}{line}" for line in (text or "").split("\n"))


def _yaml_display_safe(text: str) -> str:
    """Make a one-line value safe as a bare YAML scalar (no colons/quotes/newlines)."""
    clean = re.sub(r"\s+", " ", (text or "").replace(":", " -")).strip()
    return clean.replace('"', "").replace("'", "")


# ============================================================================
# CapIR -> deterministic capability topic (the 1:1 conversion)
#
# A converted agent.py compiles its perform() to a CapIR (t2p-capir/1.0). When a
# sub-agent carries that CapIR, the packager emits a REAL Copilot Studio topic
# that runs the SAME steps perform() runs: OnRecognizedIntent (the agent's real
# triggers) -> Question (the user's real input) -> SetVariable Table() of the
# SEEDED records -> Filter by the real query -> branch -> SendActivity, plus a
# document render for artifact-producing capabilities. The control flow is real;
# only the DATA is mocked. Flipping the in-topic Table() to a Dataverse /
# SharePoint connector (binding.connector) is the one-line move to live data, and
# the same filter/respond/document logic runs unchanged. This is the opposite of
# an actions:[]+modelDescription "gamed" topic.
# ============================================================================

def _yaml_dq(text) -> str:
    """A YAML double-quoted scalar: robust for Power Fx expressions and message
    text (escapes backslash/quote, encodes newlines)."""
    s = (str(text).replace("\\", "\\\\").replace('"', '\\"')
         .replace("\n", "\\n").replace("\t", "\\t").replace("\r", ""))
    return '"' + s + '"'


def _pfx_str(value) -> str:
    """A Power Fx double-quoted string literal (internal quotes doubled)."""
    return '"' + str(value).replace('"', '""') + '"'


def _pfx_safe_text(text) -> str:
    """Strip literal braces from message text so Copilot Studio does not parse
    them as variable bindings (unparseable {...} fails publish). Template tokens
    like {Topic.X} are added AFTER this, so they survive."""
    return str(text).replace("{", "(").replace("}", ")")


def _capir_topic_fields(records):
    """Stable union of record field names (the Table()/filter columns) when the
    binding omits an explicit field list (recovered / recompiled CapIRs)."""
    fields = []
    for r in records or []:
        if isinstance(r, dict):
            for k in r.keys():
                if k not in fields:
                    fields.append(k)
    return fields


def _numeric_metric_field(records, fields, hint=None):
    """Pick the field numeric-threshold queries compare against (e.g. "assets
    above a 30% failure probability" -> a real `Value(field) >= 0.30`). A field
    qualifies only if it parses as a number in EVERY record (so Power Fx Value()
    never errors). Prefers probability/score-like names and 0..1-ranged fields;
    honors an explicit binding `metric_field` hint."""
    if hint and hint in (fields or []):
        return hint
    if not records:
        return None
    numeric, ratio = [], []
    for f in fields:
        vals, ok = [], True
        for r in records:
            if not isinstance(r, dict) or f not in r or str(r.get(f)).strip() == "":
                ok = False; break
            try:
                vals.append(float(str(r.get(f)).strip()))
            except (TypeError, ValueError):
                ok = False; break
        if ok and vals:
            numeric.append(f)
            if all(0.0 <= v <= 1.0 for v in vals):
                ratio.append(f)
    pool = ratio or numeric
    if not pool:
        return None
    for pat in (r"p_?fail|prob|likeli|risk", r"score|rate|ratio|pct|percent|conf"):
        for f in pool:
            if re.search(pat, f, re.I):
                return f
    return pool[0]


# The load-bearing perform() constants (t2p-capir/1.0 CAPIR_CONSTS). The topic
# reads these off the CapIR when present so it mirrors the agent.py's numbers.
_CAPIR_TOPIC_CONSTS = {
    "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


def capir_topic_action_name(capir: dict) -> str:
    """The custom-topic schema suffix for a capability: Handle<Pascal(key)>."""
    key = (capir or {}).get("key") or "capability"
    return "Handle" + (_pascal(key) or "Capability")


def capir_topic_data_yaml(display_name: str, capir: dict) -> str:
    """Render a capability's CapIR into a REAL deterministic Copilot Studio topic
    'data' YAML that goes INSIDE the sub-agent: OnRecognizedIntent triggers ->
    Question (slot) -> SetVariable Table() of the SEEDED records -> Filter by the
    real query -> ConditionGroup on the match count -> SendActivity, plus (for an
    artifact capability) a SetVariable that renders the document from the matched
    (or fallback) records exactly like perform()'s artifact step. The synthetic
    records live IN the topic and the control flow runs deterministically; only
    the DATA is mocked. Structural 1:1 with the generated agent.py's perform()."""
    capir = capir or {}
    consts = dict(_CAPIR_TOPIC_CONSTS)
    consts.update(capir.get("consts") or {})
    binding = capir.get("binding") or {}
    fields = binding.get("fields") or _capir_topic_fields(binding.get("records"))
    table = binding.get("table") or "records"
    records = binding.get("records") or []
    customer = str(capir.get("customer") or "the customer")
    response = _pfx_safe_text(capir.get("response") or f"Here is how I handle {display_name}.")
    # triggers + grounding facts + the artifact doc come straight from the steps
    triggers, facts, doc = [], [], None
    for step in capir.get("steps") or []:
        op = step.get("op")
        if op == "trigger_match":
            triggers = step.get("queries") or []
        elif op == "knowledge_lookup":
            facts = step.get("facts") or []
        elif op == "artifact":
            doc = step.get("doc")
    prompt = None
    for slot in capir.get("slots") or []:
        prompt = slot.get("prompt"); break
    prompt = prompt or f"What would you like help with for {display_name}?"

    # Power Fx: a real Table() of the seeded records, a real query Filter, a real
    # count, then a real branch -- the exact perform() path.
    recs = []
    for r in records:
        if isinstance(r, dict):
            cells = ", ".join("%s: %s" % (f, _pfx_str(r.get(f, ""))) for f in fields)
            recs.append("{" + cells + "}")
    table_pfx = "=Table(" + ", ".join(recs) + ")" if recs else "=Blank()"
    conds = " || ".join("(Lower(ThisRecord.%s) in Lower(Topic.Query))" % f for f in fields)
    text_clause = "(%s)" % (conds or "false")

    # numeric-threshold support: a query like "assets above a 30% failure
    # probability" sets Topic.Threshold (number, %-aware) + Topic.Direction
    # (ge/le) and the Filter does a REAL Value()-comparison on the metric field,
    # not just text containment. Falls back to text match when no number is asked.
    metric_field = _numeric_metric_field(records, fields, (binding.get("metric_field")))
    threshold_actions, filter_inner = "", text_clause
    if metric_field:
        num_re = r"\d+\.?\d*"
        thr_pfx = ('=If(IsMatch(Topic.Query, "\\d"), '
                   'Value(First(MatchAll(Topic.Query, "' + num_re + '")).FullMatch) '
                   '/ If(IsMatch(Topic.Query, "%"), 100, 1), Blank())')
        dir_pfx = ('=If(IsMatch(Lower(Topic.Query), "above|over|greater|more than|exceed|at least|higher|>"), "ge", '
                   'If(IsMatch(Lower(Topic.Query), "below|under|less|fewer|within|at most|lower|<"), "le", "ge"))')
        threshold_actions = (
            "    - kind: SetVariable\n"
            "      id: setThreshold\n"
            "      variable: Topic.Threshold\n"
            "      value: " + _yaml_dq(thr_pfx) + "\n"
            "    - kind: SetVariable\n"
            "      id: setDirection\n"
            "      variable: Topic.Direction\n"
            "      value: " + _yaml_dq(dir_pfx) + "\n")
        num_clause = ('(!IsBlank(Topic.Threshold) && If(Topic.Direction = "le", '
                      'Value(ThisRecord.' + metric_field + ') <= Topic.Threshold, '
                      'Value(ThisRecord.' + metric_field + ') >= Topic.Threshold))')
        filter_inner = "(" + text_clause + " || " + num_clause + ")"
    filter_pfx = "=Filter(Topic.Records, !IsBlank(Topic.Query) && " + filter_inner + ")"

    grounding = "\n".join("- " + _pfx_safe_text(f) for f in facts)
    ground_block = ("\n\nGrounded in what you told us:\n" + grounding) if grounding else ""

    # artifact (op==artifact): render the document from the matched-or-fallback
    # records, exactly like perform()'s artifact step (hits[:pdf_records] with a
    # data[:fallback_take] fallback). Materializing the real downloadable file is
    # the live-data flip -- a Create-file / Convert-to-PDF flow over these records.
    doc_actions, doc_block = "", ""
    if doc and fields:
        cells_pfx = ' & " | " & '.join('"%s: " & Text(ThisRecord.%s)' % (f, f) for f in fields)
        source = ("If(Topic.MatchCount > 0, Topic.Matches, FirstN(Topic.Records, %d))"
                  % consts["fallback_take"])
        document_pfx = ("=Concat(FirstN(%s, %d), %s & Char(10))"
                        % (source, consts["pdf_records"], cells_pfx))
        doc_actions = (
            "    - kind: SetVariable\n"
            "      id: setDocument\n"
            "      variable: Topic.Document\n"
            "      value: " + _yaml_dq(document_pfx) + "\n")
        prepared = _pfx_safe_text(consts["pdf_prepared"].replace("{customer}", customer))
        footer = _pfx_safe_text(consts["pdf_footer"])
        safe_doc = _pfx_safe_text(str(doc))
        doc_block = ("\n\n[" + safe_doc + "] " + prepared + ":\n"
                     + "{Topic.Document}\n" + footer
                     + "\n(In production, a Create-file / Convert-to-PDF flow over these "
                       "records delivers the real " + safe_doc + ".)")

    hit_msg = (response + ground_block
               + "\n\nI found {Topic.MatchCount} matching record(s) in the "
               + table + " data (synthetic demo data - no customer data needed)."
               + doc_block)
    miss_msg = (response + ground_block
                + "\n\nNo matching record in the " + table
                + " data; here are reference examples to ground the answer."
                + doc_block)
    trig = "\n".join("      - " + _yaml_dq(t) for t in triggers) or ("      - " + _yaml_dq(display_name))

    # intake: ask for the value to filter on. We intentionally do NOT read an
    # orchestrator-passed `Global.<param>` here. A connected agent can only
    # reference a global it has DECLARED as external-settable, and the solution
    # package format gives no reliable way to emit that declaration — referencing
    # an undeclared Global makes Copilot Studio's topic checker throw a
    # PowerFxError ("Identifier not recognized"), which blocks publish. The
    # orchestrator still DECLARES + PASSES the typed inputs (see the connected
    # action's inputType); the agent's generative layer receives them, and this
    # deterministic topic captures the value it filters on via the Question.
    intake_actions = (
        "    - kind: Question\n"
        "      id: question_query\n"
        "      variable: Topic.Query\n"
        "      prompt: " + _yaml_dq(prompt) + "\n"
        "      entity: StringPrebuiltEntity\n")

    return (
        "kind: AdaptiveDialog\n"
        "beginDialog:\n"
        "  kind: OnRecognizedIntent\n"
        "  id: main\n"
        "  intent:\n"
        "    displayName: " + _yaml_dq(display_name) + "\n"
        "    includeInOnSelectIntent: false\n"
        "    triggerQueries:\n" + trig + "\n"
        "  actions:\n"
        + intake_actions +
        "    - kind: SetVariable\n"
        "      id: setRecords\n"
        "      variable: Topic.Records\n"
        "      value: " + _yaml_dq(table_pfx) + "\n"
        + threshold_actions +
        "    - kind: SetVariable\n"
        "      id: setMatches\n"
        "      variable: Topic.Matches\n"
        "      value: " + _yaml_dq(filter_pfx) + "\n"
        "    - kind: SetVariable\n"
        "      id: setCount\n"
        "      variable: Topic.MatchCount\n"
        "      value: " + _yaml_dq("=CountRows(Topic.Matches)") + "\n"
        + doc_actions +
        "    - kind: ConditionGroup\n"
        "      id: hasMatches\n"
        "      conditions:\n"
        "        - id: hasMatches_hit\n"
        "          condition: " + _yaml_dq("=Topic.MatchCount > 0") + "\n"
        "          actions:\n"
        "            - kind: SendActivity\n"
        "              id: replyHit\n"
        "              activity: " + _yaml_dq(hit_msg) + "\n"
        "      elseActions:\n"
        "        - kind: SendActivity\n"
        "          id: replyMiss\n"
        "          activity: " + _yaml_dq(miss_msg) + "\n"
    )


@dataclass
class SubAgentSpec:
    """One connected sub-agent (one agent.py promoted to its own bot)."""
    agent_name: str           # e.g. "loanoriginationassistant"
    display_name: str         # e.g. "Loan Origination Assistant"
    description: str          # routing description the orchestrator selects on
    instructions: str         # the sub-agent's gpt.default instruction blob
    # The capability's compiled CapIR (t2p-capir/1.0), records already injected.
    # When present, the packager emits a REAL deterministic topic INSIDE this
    # sub-agent that runs the same steps as the converted agent.py's perform(),
    # instead of leaving the behavior to the gpt.default instruction blob. The
    # instructions remain as the persona/router fallback.
    capir: Optional[dict] = None
    # The source agent.py's perform() params [(name, description, required), ...],
    # declared as typed INPUTS on the orchestrator's connected-agent action so the
    # Copilot Studio orchestrator passes them when it delegates (the agent's
    # "Inputs" panel) — the contract, structurally, not just in the description.
    params: Optional[list] = None


@dataclass
class ConnectedSolutionSpec:
    """A single solution bundling an orchestrator + N connected sub-agents."""
    solution_unique_name: str
    solution_display_name: str
    orchestrator_display_name: str
    subagents: List[SubAgentSpec]
    orchestrator_instructions: str = ""   # synthesized if empty
    publisher_prefix: str = "rapp"
    publisher_unique_name: str = "DefaultPublisher"
    publisher_display_name: str = "Default Publisher"
    solution_version: str = "1.0.0.0"
    managed: bool = False
    orchestrator_schema_suffix: str = "orchestrator"
    # When True the orchestrator auto-publishes on import. Leave False so the
    # import itself never depends on the (slower, fail-prone) publish step.
    orchestrator_publish_on_import: bool = False
    # When True the orchestrator declares MsTeams + M365 Copilot channels. This
    # requires a maker-portal publish (headless `pac copilot publish` 409s on the
    # channel registration). Default False = fully headlessly publishable.
    orchestrator_channels: bool = False


class ConnectedSolutionPackager:
    """Assembles a multi-bot connected-agent solution zip from a spec."""

    def __init__(self, spec: ConnectedSolutionSpec):
        self.spec = spec
        # publisher_prefix is the one untamed length input feeding the schema caps
        # below; bound it to Dataverse's 8-char prefix limit so no schema exceeds
        # MAX_SCHEMA for ANY direct caller (perform() already caps it). Mutate the
        # spec too so the CustomizationPrefix stays consistent with the schemas.
        spec.publisher_prefix = spec.publisher_prefix[:8]
        prefix = spec.publisher_prefix

        # Connected-agent components are named
        #   {orch_schema}.InvokeConnectedAgentTaskAction.{Action}
        # and the full schema name must stay within Dataverse's 100-char limit.
        # Cap the orchestrator schema (reserving room for the action suffix) so a
        # long stack name can never push a component name over the limit.
        suffix = spec.orchestrator_schema_suffix
        base = re.sub(r"stack$", "", _sanitize_schema(spec.solution_unique_name)) or "agents"
        orch = f"{prefix}_{base}{suffix}"
        max_orch = MAX_SCHEMA - len(_CONNECTED_INFIX) - _MIN_ACTION_BUDGET   # 42
        if len(orch) > max_orch:
            keep = max(4, max_orch - len(prefix) - 1 - len(suffix))
            orch = f"{prefix}_{base[:keep]}{suffix}"
        self.orch_schema = orch
        # Whatever room is left after the (capped) orchestrator schema + infix.
        self._action_budget = MAX_SCHEMA - len(_CONNECTED_INFIX) - len(self.orch_schema)

        # Assign a unique schema name + connected-action name to each sub-agent.
        self._children = []  # list of (SubAgentSpec, child_schema, action_name)
        seen_schemas = {self.orch_schema}
        seen_actions = set()
        # Children need room for a ".topic.<Name>" suffix within MAX_SCHEMA. The
        # orchestrator schema is capped above; children were NOT, so a long
        # solution + capability name overflowed the Dataverse 100-char limit.
        child_base_max = max(4, MAX_SCHEMA - 35 - len(prefix) - 1)
        for sub in spec.subagents:
            base = (_sanitize_schema(sub.agent_name) or "agent")[:child_base_max]
            child_schema = f"{prefix}_{base}"
            n = 2
            while child_schema in seen_schemas:
                child_schema = f"{prefix}_{base}{n}"
                n += 1
            seen_schemas.add(child_schema)

            pascal = _pascal(sub.display_name or sub.agent_name) or "Agent"
            action = pascal[: self._action_budget]
            n = 2
            while action in seen_actions:
                tag = str(n)
                action = pascal[: max(1, self._action_budget - len(tag))] + tag
                n += 1
            seen_actions.add(action)

            self._children.append((sub, child_schema, action))

    # -- public ----------------------------------------------------------

    def package(self, output_path: Optional[Path] = None) -> bytes:
        buf = io.BytesIO()
        overrides: List[str] = []  # /data parts for [Content_Types].xml

        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            # 1. solution + customizations (connector-less, empty RootComponents)
            zf.writestr("solution.xml", self._solution_xml())
            zf.writestr(
                "customizations.xml",
                CUSTOMIZATIONS_XML_NATIVE.format(connection_references=""),
            )

            # 2. Orchestrator bot (router) — instructions list the sub-agents
            self._write_bot(
                zf,
                bot_schema=self.orch_schema,
                display_name=self.spec.orchestrator_display_name,
                instructions=self._orchestrator_instructions(),
                overrides=overrides,
                is_orchestrator=True,
            )

            # 3. Connected-agent delegation components (under the orchestrator)
            for sub, child_schema, action in self._children:
                self._write_connected_action(
                    zf, sub, child_schema, action, overrides
                )

            # 4. Each sub-agent as its own connectable bot — now carrying the REAL
            #    deterministic capability topic (1:1 with its agent.py) when a
            #    CapIR is present.
            for sub, child_schema, _action in self._children:
                self._write_bot(
                    zf,
                    bot_schema=child_schema,
                    display_name=sub.display_name,
                    instructions=sub.instructions,
                    overrides=overrides,
                    capir=sub.capir,
                )

            # 5. Empty connection reference set (no connectors in this topology)
            zf.writestr(
                "Assets/botcomponent_connectionreferenceset.xml",
                CONN_REF_SET_XML.format(entries=""),
            )

            # 6. [Content_Types].xml — every extensionless /data part listed
            zf.writestr(
                "[Content_Types].xml",
                CONTENT_TYPES_XML_NATIVE.format(overrides="".join(overrides)),
            )

        data = buf.getvalue()
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(data)
        return data

    @property
    def bot_schemas(self) -> List[str]:
        return [self.orch_schema] + [c[1] for c in self._children]

    # -- bot writers -----------------------------------------------------

    def _write_bot(
        self,
        zf: zipfile.ZipFile,
        bot_schema: str,
        display_name: str,
        instructions: str,
        overrides: List[str],
        is_orchestrator: bool = False,
        capir: Optional[dict] = None,
    ) -> None:
        """Write a complete bot: bot.xml, configuration.json, gpt.default, system
        topics, and (for a sub-agent carrying a CapIR) the REAL deterministic
        capability topic that runs the same steps as the converted agent.py."""
        # Copilot Studio caps the bot name at 42 chars; keep "Orchestrator" intact.
        display_name = _cap_bot_name(
            display_name, preserve_suffix="Orchestrator" if is_orchestrator else None
        )
        # bot.xml + configuration.json
        zf.writestr(
            f"bots/{bot_schema}/bot.xml",
            BOT_XML.format(
                bot_schema=bot_schema,
                bot_display_name=display_name,
                icon_base64=DEFAULT_ICON_BASE64,
            ),
        )
        gpt_schema = f"{bot_schema}.gpt.default"
        if is_orchestrator:
            # The connected-agent root needs the channels + isLightweightBot config
            # or its post-publish provisioning fails with a 409 ExternalServiceException.
            poi = '\n  "publishOnImport": true,' if self.spec.orchestrator_publish_on_import else ""
            channels = ORCHESTRATOR_CHANNELS_BLOCK if self.spec.orchestrator_channels else ""
            config_json = ORCHESTRATOR_CONFIGURATION_JSON.format(
                gpt_schema=gpt_schema, publish_on_import_line=poi, channels_block=channels
            )
        else:
            config_json = BOT_CONFIGURATION_JSON_NATIVE.format(gpt_schema=gpt_schema)
        zf.writestr(f"bots/{bot_schema}/configuration.json", config_json)

        # gpt.default component (instructions)
        gpt_folder = f"botcomponents/{gpt_schema}"
        zf.writestr(
            f"{gpt_folder}/botcomponent.xml",
            GPT_BOTCOMPONENT_XML.format(
                schema_name=gpt_schema,
                display_name=display_name,
                bot_schema=bot_schema,
            ),
        )
        instr = instructions or f"You are {display_name}. Help the user with their request."
        zf.writestr(
            f"{gpt_folder}/data",
            GPT_DATA_YAML.format(
                display_name=display_name,
                instructions_indented=_indent(instr, 2),
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{gpt_folder}/data"))

        # system topics (one set per bot)
        for topic_key, topic_data in SYSTEM_TOPICS.items():
            schema_name = f"{bot_schema}.topic.{topic_key}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(bot_schema, topic_key, topic_data),
            )
            zf.writestr(
                f"{folder}/data",
                topic_data["data"].format(bot_schema=bot_schema),
            )
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

        # custom per-capability topic: the REAL deterministic behavior, INSIDE
        # this sub-agent (1:1 with the converted agent.py's CapIR steps). The
        # orchestrator stays a pure router and never carries one.
        if capir and not is_orchestrator:
            action = capir_topic_action_name(capir)
            # keep "{bot_schema}.topic.{action}" within the 100-char schema limit
            action = action[: max(4, MAX_SCHEMA - len(bot_schema) - len(".topic."))]
            schema_name = f"{bot_schema}.topic.{action}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(
                    bot_schema, action,
                    {"display_name": _xml_escape(display_name),
                     "description": f"Deterministic handler for {display_name} "
                                    "(seeded records + the real user query, 1:1 with the agent.py)."}),
            )
            zf.writestr(f"{folder}/data", capir_topic_data_yaml(display_name, capir))
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    def _write_connected_action(
        self,
        zf: zipfile.ZipFile,
        sub: SubAgentSpec,
        child_schema: str,
        action: str,
        overrides: List[str],
    ) -> None:
        """Write the orchestrator's delegation component for one sub-agent."""
        schema_name = f"{self.orch_schema}.InvokeConnectedAgentTaskAction.{action}"
        folder = f"botcomponents/{schema_name}"
        description = sub.description or f"Delegate to {sub.display_name}."

        zf.writestr(
            f"{folder}/botcomponent.xml",
            INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML.format(
                schema_name=schema_name,
                description=_xml_escape(description),
                display_name=_xml_escape(sub.display_name),
                orchestrator_schema=self.orch_schema,
            ),
        )
        zf.writestr(
            f"{folder}/dependencies.json",
            INVOKE_CONNECTED_AGENT_DEPENDENCIES.format(child_schema=child_schema),
        )
        inputs_block, input_type_block = _connected_inputs_yaml(getattr(sub, "params", None))
        zf.writestr(
            f"{folder}/data",
            INVOKE_CONNECTED_AGENT_DATA.format(
                display_name=_yaml_display_safe(sub.display_name),
                description_indented=_indent(description, 2),
                child_schema=child_schema,
                inputs_block=inputs_block,
                input_type_block=input_type_block,
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    # -- xml helpers -----------------------------------------------------

    def _topic_botcomponent_xml(self, bot_schema, topic_key, topic_data) -> str:
        schema_name = f"{bot_schema}.topic.{topic_key}"
        desc = topic_data.get("description")
        desc_element = ""
        if desc:
            desc_element = f"\n  <description>{_xml_escape(desc)}</description>"
        return BOTCOMPONENT_XML.format(
            schema_name=schema_name,
            component_type=9,
            display_name=topic_data["display_name"],
            bot_schema=bot_schema,
            description_element=desc_element,
        )

    def _solution_xml(self) -> str:
        return SOLUTION_XML_NATIVE.format(
            solution_unique_name=self.spec.solution_unique_name,
            solution_display_name=self.spec.solution_display_name,
            publisher_unique_name=self.spec.publisher_unique_name,
            publisher_display_name=self.spec.publisher_display_name,
            publisher_prefix=self.spec.publisher_prefix,
            solution_version=self.spec.solution_version,
            managed_flag="1" if self.spec.managed else "0",
        )

    # -- orchestrator instructions --------------------------------------

    def _orchestrator_instructions(self) -> str:
        if self.spec.orchestrator_instructions:
            return self.spec.orchestrator_instructions
        lines = [
            f"You are {self.spec.orchestrator_display_name}, the orchestrator for the "
            f"{self.spec.solution_display_name} workflow. You route each user request to the "
            "right connected sub-agent and never answer specialized questions yourself.",
            "",
            "Connected sub-agents you can delegate to:",
        ]
        for sub, _schema, _action in self._children:
            one_line = re.sub(r"\s+", " ", (sub.description or sub.display_name)).strip()
            lines.append(f"- {sub.display_name}: {one_line}")
        lines += [
            "",
            "Routing rules:",
            "- Read the user's request, pick the single best-matching sub-agent from the list, and delegate to it.",
            "- Pass each sub-agent only the inputs it needs; do not paraphrase or pre-answer its work.",
            "- If the request spans several sub-agents, handle one sub-agent per turn and confirm before moving on.",
            "- If no sub-agent fits, say so and ask a clarifying question rather than inventing an answer.",
        ]
        return "\n".join(lines)


def generate_connected_solution(
    spec: ConnectedSolutionSpec,
    output_path: Optional[Path] = None,
) -> bytes:
    """Build a connected (multi-bot) solution zip from a ConnectedSolutionSpec."""
    return ConnectedSolutionPackager(spec).package(output_path=output_path)


# ============================================================================
# Build sub-agents from an agent stack (agents/*.py + metadata.json) and validate
# ============================================================================

def _humanize(name: str) -> str:
    name = re.sub(r"_stacks$", "", name or "")
    name = name.replace("_", " ").replace("-", " ").strip()
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _humanize_class(name: str) -> str:
    name = re.sub(r"Agent$", "", name or "")
    name = re.sub(r"_agent$", "", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = name.replace("_", " ").strip()
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _safe_literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


# Class-body literals a converted agent.py embeds. CAPIR is the compiled CapIR
# (perform()'s spec); SYNTHETIC_DATA holds the seeded records (the build keeps
# them OUT of the CapIR binding, so we re-inject them); the rest let us recompile
# a CapIR when one was not embedded.
_RECOVERED_ATTRS = {"CAPIR", "SYNTHETIC_DATA", "KNOWLEDGE", "RESPONSE",
                    "DOC_NAME", "CUSTOMER", "TRIGGERS"}


def _parse_basic_agent(py_path: Path):
    """AST-extract (display_name, agent_name, description, module_doc, params,
    recovered) from a BasicAgent .py — `recovered` carries any embedded CapIR /
    seeded records used to build the deterministic capability topic."""
    src = py_path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    module_doc = (ast.get_docstring(tree) or "").strip()

    cls = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and any(
            isinstance(b, ast.Name) and b.id == "BasicAgent" for b in node.bases
        ):
            cls = node
            break
    if cls is None:
        return None

    self_name = None
    description = ""
    params = []  # (name, description, required)
    recovered = {}  # class-level CAPIR / SYNTHETIC_DATA / ... for deterministic topics
    for sub in ast.walk(cls):
        if not isinstance(sub, ast.Assign):
            continue
        for tgt in sub.targets:
            # class-body literals the build stage embeds (CAPIR = {...},
            # SYNTHETIC_DATA = [...], KNOWLEDGE / RESPONSE / DOC_NAME / CUSTOMER / TRIGGERS)
            if isinstance(tgt, ast.Name) and tgt.id in _RECOVERED_ATTRS:
                val = _safe_literal(sub.value)
                if val is not None:
                    recovered[tgt.id] = val
                continue
            if not (isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "self"):
                continue
            if tgt.attr == "name" and isinstance(sub.value, ast.Constant) and isinstance(sub.value.value, str):
                self_name = sub.value.value
            elif tgt.attr == "metadata" and isinstance(sub.value, ast.Dict):
                # Walk the dict node key-by-key: the metadata literal contains a
                # non-literal value ("name": self.name), so literal_eval on the
                # whole dict fails — pull the literal keys we care about directly.
                for k, v in zip(sub.value.keys, sub.value.values):
                    key = k.value if isinstance(k, ast.Constant) else None
                    if key == "description":
                        dv = _safe_literal(v)
                        if isinstance(dv, str):
                            description = dv.strip()
                    elif key == "parameters":
                        pv = _safe_literal(v)
                        if isinstance(pv, dict):
                            props = pv.get("properties") or {}
                            req = set(pv.get("required") or [])
                            for pn, pinfo in props.items():
                                pdesc = (pinfo.get("description") if isinstance(pinfo, dict) else "") or pn
                                params.append((pn, pdesc, pn in req))

    stem_name = re.sub(r"_agent$", "", py_path.stem)
    agent_name = stem_name
    display = _humanize_class(self_name or stem_name)
    if not description:
        # First paragraph of the module docstring.
        description = re.sub(r"\s+", " ", module_doc.split("\n\n")[0]).strip()
    # Statically infer the SHAPE of the data this agent works with (the dict keys
    # its perform()/helpers read & write) so we can synthesize matching static
    # stand-in records — no execution, no domain rules.
    recovered["INFERRED_FIELDS"] = _infer_record_fields(tree, exclude=[p[0] for p in params])
    return display, agent_name, description, module_doc, params, recovered


def _stack_subagent_instructions(display, description, module_doc, params) -> str:
    """The sub-agent's brain: self-documents the agent.py end-to-end — its purpose
    and its FULL input contract (what the orchestrator passes to delegate). Generic
    for ANY agent.py; no domain assumptions."""
    lines = [f"You are the {display} agent.", "", "# Purpose"]
    lines.append(module_doc.strip() if module_doc else (description or f"Handle {display} requests."))
    lines += ["", "# Inputs the orchestrator passes you"]
    if params:
        for pn, pdesc, required in params:
            tag = "required" if required else "optional"
            clean = re.sub(r"\s+", " ", pdesc).strip()
            lines.append(f"- {pn} ({tag}): {clean}")
    else:
        lines.append("- No structured inputs are required; use the user's request directly.")
    lines += ["", "# How you answer",
              "- Run your deterministic capability topic and ground every answer in its seeded records.",
              "- That seeded data is SYNTHETIC stand-in data for your real source system, so you load "
              "and run end-to-end with no live connection. Swapping the topic's Table() for the live "
              "connector takes you to production with no change to the logic.",
              "- Stay in your lane: if the request belongs to another connected agent, say so and let "
              "the orchestrator route it."]
    return "\n".join(lines)


def _contract_description(description, params, limit=850):
    """The orchestrator-facing routing description: the agent's purpose PLUS its
    input contract, so the Copilot Studio agent knows what to pass when it
    delegates. Self-documenting, generic, length-capped for the component."""
    base = re.sub(r"\s+", " ", description or "").strip()
    if params:
        ins = "; ".join("%s (%s)" % (pn, "required" if req else "optional")
                        for pn, _pd, req in params)
        base = (base + " Inputs to pass: " + ins + ".").strip()
    return base[:limit]


# t2p-capir/1.0 — the load-bearing perform() constants, mirrored so a recompiled
# CapIR carries the same numbers the agent.py uses.
_CAPIR_SCHEMA = "t2p-capir/1.0"
_RECOMPILE_CONSTS = {
    "word_min_len": 3, "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


# Envelope / structural dict keys that are NOT data columns, so schema inference
# never mistakes the result wrapper for record fields.
_ENVELOPE_KEYS = {"status", "agent", "data", "parameters", "properties",
                  "required", "type", "name", "description", "items", "enum",
                  "error", "result", "results", "success", "ok", "count", "as_of_utc"}
# Objects whose `.get("x")` calls are NOT record reads (input kwargs, env, etc.).
_SKIP_GET_OBJS = {"kwargs", "self", "metadata", "os", "sys", "environ", "params", "config"}


def _flatten_record(r):
    """Flatten one record to top-level scalar fields (the Table()/filter columns):
    a nested dict is merged up one level; lists/dicts are json-encoded to strings."""
    if not isinstance(r, dict):
        return {}
    out = {}
    for k, v in r.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                out[str(kk)] = vv if not isinstance(vv, (list, dict)) else json.dumps(vv, ensure_ascii=False)
        elif isinstance(v, list):
            out[str(k)] = json.dumps(v, ensure_ascii=False)
        else:
            out[str(k)] = v
    return out


def _infer_record_fields(tree, exclude=None, max_fields=14):
    """Infer the SHAPE of the data an agent.py works with by statically scanning
    its code for the dict keys it reads/writes: `rec.get("field")`, `rec["field"]`
    and `{"field": ...}` literals. Excludes input-param names + envelope keys so
    only genuine data columns remain. 100% static — no execution, no domain rules."""
    exclude = set(exclude or []) | _ENVELOPE_KEYS
    keys = []

    def add(k):
        if (isinstance(k, str) and k and k.isidentifier()
                and k not in exclude and k not in keys):
            keys.append(k)

    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            obj = node.func.value
            if isinstance(obj, ast.Name) and obj.id in _SKIP_GET_OBJS:
                continue
            a = node.args[0]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                add(a.value)
        elif isinstance(node, ast.Subscript):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                add(sl.value)
        elif isinstance(node, ast.Dict):
            klits = [k.value for k in node.keys
                     if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "status" in klits and "data" in klits:
                continue  # a result-envelope literal, not a data record
            for k in klits:
                add(k)
    return keys[:max_fields]


def _synthesize_value(field, i):
    """A clearly-synthetic, generic value for `field` on row i — typed by the field
    NAME's TOKENS only (token-matched, so "age" never fires inside "message"). No
    domain knowledge. Deterministic (index-based, no RNG)."""
    f = field.lower()
    toks = set(t for t in re.split(r"[^a-z0-9]+", f) if t)
    if toks & {"prob", "probability", "score", "rate", "ratio", "pct", "percent",
               "confidence", "likelihood", "fail", "risk"}:
        return round(0.15 + 0.7 * (((i - 1) % 5) / 4.0), 2)   # 0.15 .. 0.85
    if f.startswith(("is_", "has_")) or toks & {"enabled", "active", "flag", "bool"}:
        return (i % 2 == 0)
    if toks & {"date", "time", "utc", "timestamp", "datetime", "created", "updated"}:
        return "2026-01-%02dT00:00:00Z" % min(i, 28)
    if toks & {"id", "guid", "uuid", "code", "ref"}:
        return "%s-%04d" % ((re.sub(r"[^A-Za-z]", "", field).upper()[:4] or "REC"), i)
    if toks & {"count", "qty", "quantity", "amount", "price", "cost", "value", "age",
               "days", "years", "hours", "num", "number", "level", "index", "size",
               "total", "kv", "voltage", "pct"}:
        return i * 10
    return "synthetic %s %d" % (f.replace("_", " "), i)


def _synthesize_records(fields, n=5):
    """Generate n self-documenting STATIC stand-in records over `fields` — the
    synthetic data that lets the topic load and run end-to-end with no live
    connection. Generic for any field set; swap the Table() for the live connector."""
    fields = [f for f in (fields or []) if f] or ["id", "label", "detail"]
    return [{f: _synthesize_value(f, i) for f in fields} for i in range(1, n + 1)]


def _resolve_capir(recovered, display, agent_name, description, params, capir_mode):
    """Decide the CapIR a sub-agent's deterministic topic is built from — the
    topic that IS this agent.py's perform() running on STATIC stand-in data, so
    the Copilot Studio orchestrator gets the same result it would by chatting the
    brainstem and invoking the agent.py.

    Policy (capir_mode):
      off       -> never emit a topic (instructions-blob only)
      embedded  -> only when the agent.py embeds a CAPIR literal
      static    -> embedded, else recompile ONLY from real seeded data
                   (SYNTHETIC_DATA); do not synthesize a stand-in
      auto      -> (default) embedded, else recompile from SYNTHETIC_DATA, else
                   SYNTHESIZE static stand-in data from the agent's inferred data
                   shape. Maps EVERY agent.py to a self-documented topic."""
    mode = (capir_mode or "auto").lower()
    if mode in ("capture", "always", "run"):
        mode = "auto"
    if mode == "off":
        return None
    synth = recovered.get("SYNTHETIC_DATA") or []
    embedded = recovered.get("CAPIR")
    if isinstance(embedded, dict) and embedded.get("steps"):
        binding = dict(embedded.get("binding") or {})
        if not binding.get("records"):
            binding["records"] = synth
        if not binding.get("fields"):
            binding["fields"] = _capir_topic_fields(binding.get("records"))
        out = {**embedded, "binding": binding}
        out.setdefault("customer", recovered.get("CUSTOMER") or "the customer")
        return out
    if mode == "embedded":
        return None
    if mode == "static":
        return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                          params, records=synth) if synth else None
    # auto: always map — real seeded data if present, else a STATIC stand-in
    # synthesized from the agent's inferred data shape (its perform() field reads).
    records = synth
    if not records:
        fields = recovered.get("INFERRED_FIELDS") or [p[0] for p in (params or [])]
        records = _synthesize_records(fields)
    return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                      params, records=records)


def _recompile_capir_from_meta(recovered, display, agent_name, description, params, records=None):
    """Build a CapIR for an agent.py with no embedded CAPIR — mirrors T2P's
    _compile_capir shape from its records (real or synthesized), KNOWLEDGE,
    RESPONSE, DOC_NAME, TRIGGERS plus the parsed metadata. Same structure and
    perform()-parity constants as the generated path; only the source differs."""
    records = [_flatten_record(r) for r in (records if records is not None
               else (recovered.get("SYNTHETIC_DATA") or []))][:10]
    knowledge = list(recovered.get("KNOWLEDGE") or [])
    triggers = list(recovered.get("TRIGGERS") or [])
    if not triggers:
        triggers = [display] + ([re.sub(r"\s+", " ", description).strip()[:60]]
                                if description else [])
    response = recovered.get("RESPONSE") or description or f"Here is how I handle {display}."
    doc = recovered.get("DOC_NAME") or None
    key = re.sub(r"[^a-z0-9_]", "", (agent_name or display).lower().replace(" ", "_")) or "capability"
    fields = _capir_topic_fields(records)
    prompt = f"What would you like to ask the {display} agent? (a keyword, id, or value to filter on)"
    binding = {
        "connector": "table",
        "table": "rec_" + key,
        "library": display + " Library",
        "fields": fields,
        "key_field": fields[0] if fields else "id",
        "row_count": len(records),
        "records": records,
    }
    steps = [
        {"id": "trigger", "op": "trigger_match", "queries": triggers},
        {"id": "slot_query", "op": "slot_fill", "slot": "query"},
        {"id": "ground", "op": "knowledge_lookup", "facts": knowledge, "into": "Grounding"},
        {"id": "lookup", "op": "record_lookup", "source": "binding", "from": "query",
         "into": "Matches", "take": _RECOMPILE_CONSTS["example_take"],
         "fallback_take": _RECOMPILE_CONSTS["fallback_take"]},
        {"id": "respond", "op": "respond", "template_kind": "standard"},
    ]
    if doc:
        steps.append({"id": "artifact", "op": "artifact", "doc": doc,
                      "from": ["Grounding", "Matches"]})
    return {
        "schema": _CAPIR_SCHEMA,
        "key": key,
        "response": response,
        "customer": recovered.get("CUSTOMER") or "the customer",
        "binding": binding,
        "slots": [{"name": "query", "entity": "StringPrebuiltEntity",
                   "prompt": prompt, "required": True}],
        "consts": dict(_RECOMPILE_CONSTS),
        "steps": steps,
        "expect": list(triggers),
        "triggers_owned": True,
    }


def _subagents_from_stack(stack_dir: Path, capir_mode: str = "auto") -> List[SubAgentSpec]:
    agents_dir = stack_dir / "agents"
    if not agents_dir.is_dir():
        agents_dir = stack_dir
    subs: List[SubAgentSpec] = []
    for py in sorted(agents_dir.glob("*.py")):
        if py.name.startswith("_") or py.name == "basic_agent.py":
            continue
        parsed = _parse_basic_agent(py)
        if not parsed:
            logger.warning("  - %s: no BasicAgent subclass, skipping", py.name)
            continue
        display, agent_name, description, module_doc, params, recovered = parsed
        capir = _resolve_capir(recovered, display, agent_name, description, params, capir_mode)
        subs.append(SubAgentSpec(
            agent_name=agent_name,
            display_name=display,
            # description carries the input contract so the orchestrator knows what
            # to pass when it delegates (self-documented, like the agent.py).
            description=_contract_description(description, params) or f"Handle {display} requests.",
            instructions=_stack_subagent_instructions(display, description, module_doc, params),
            capir=capir,
            params=params,
        ))
        logger.info("  + %s%s", display, "  [deterministic topic]" if capir else "")
    return subs


def _load_stack_metadata(stack_dir: Path) -> dict:
    mpath = stack_dir / "metadata.json"
    if mpath.is_file():
        try:
            return json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _orchestrator_instructions_from_metadata(meta: dict, subs: List[SubAgentSpec]) -> str:
    name = meta.get("name", "the agent stack")
    desc = meta.get("description", "")
    lines = [f"You are the orchestrator for {name}.", ""]
    if desc:
        lines += [desc, ""]
    lines.append("You route each user request to the right connected sub-agent and never do their specialized work yourself.")
    features = meta.get("features") or []
    if features:
        lines += ["", "End-to-end flow this stack supports, in order:"]
        lines += [f"- {f}" for f in features]
    lines += ["", "Connected sub-agents you can delegate to:"]
    for sub in subs:
        lines.append(f"- {sub.display_name}: {sub.description}")
    starters = meta.get("starters") or []
    if starters:
        lines += ["", "Example requests you should expect:"]
        lines += [f"- {s}" for s in starters]
    lines += [
        "",
        "Routing rules:",
        "- Pick the single best-matching connected agent for the request and delegate to it; pass it the inputs named in its description.",
        "- Calling a connected agent gives you the SAME result you would get by chatting the source brainstem and letting it invoke that agent.py — each connected agent's topic runs the agent's deterministic logic on its seeded sample data.",
        "- If a request spans several connected agents, handle one per turn, show its result, then continue to the next.",
        "- If a required input is missing, ask for it. The seeded data is synthetic stand-in data; do not invent records beyond it.",
        "- If no connected agent fits, say so and ask a clarifying question.",
    ]
    return "\n".join(lines)


def validate_connected_solution(zip_path: Path) -> bool:
    """Structural checks that the connected solution is import-shaped."""
    ok = True
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = set(zf.namelist())

        for required in ("[Content_Types].xml", "solution.xml", "customizations.xml"):
            if required not in names:
                logger.error("  X missing %s", required)
                ok = False

        bots = sorted({n.split("/")[1] for n in names if n.startswith("bots/")})
        logger.info("  bots: %d (%s)", len(bots), ", ".join(bots))

        # Every connected-action must reference an existing child bot.
        actions = [n for n in names if ".InvokeConnectedAgentTaskAction." in n and n.endswith("/dependencies.json")]
        logger.info("  connected-agent actions: %d", len(actions))
        for dep in actions:
            child = json.loads(zf.read(dep).decode("utf-8"))[0]["schemaName"]
            if f"bots/{child}/bot.xml" not in names:
                logger.error("  X action %s -> missing child bot %s", dep, child)
                ok = False
            data_path = dep.rsplit("/", 1)[0] + "/data"
            if data_path in names:
                data_text = zf.read(data_path).decode("utf-8")
                if f"botSchemaName: {child}" not in data_text:
                    logger.error("  X %s data does not invoke %s", data_path, child)
                    ok = False

        # Every extensionless /data part must be declared in [Content_Types].xml.
        ct = zf.read("[Content_Types].xml").decode("utf-8")
        data_parts = [n for n in names if n.endswith("/data")]
        missing = [p for p in data_parts if f'PartName="/{p}"' not in ct]
        if missing:
            logger.error("  X %d /data parts missing from [Content_Types].xml (e.g. %s)",
                         len(missing), missing[0])
            ok = False
        else:
            logger.info("  content-types: all %d /data parts declared", len(data_parts))

        # Each bot needs gpt.default + the system-topic set.
        for bot in bots:
            if f"botcomponents/{bot}.gpt.default/data" not in names:
                logger.error("  X bot %s missing gpt.default", bot)
                ok = False

        # No botcomponent schema name may exceed the Dataverse 100-char limit.
        schemas = {n.split("/")[1] for n in names if n.startswith("botcomponents/")}
        longest = max(schemas, key=len) if schemas else ""
        if len(longest) > 100:
            logger.error("  X schema name too long (%d > 100): %s", len(longest), longest)
            ok = False
        else:
            logger.info("  schema lengths: max %d/100 (%s)", len(longest), longest)

        # Copilot Studio rejects bot display names longer than 42 chars.
        worst_name, worst_len = "", 0
        for bot in bots:
            bx = zf.read(f"bots/{bot}/bot.xml").decode("utf-8")
            m = re.search(r"<name>(.*?)</name>", bx, re.DOTALL)
            nm = (m.group(1).strip() if m else "")
            if len(nm) > worst_len:
                worst_name, worst_len = nm, len(nm)
        if worst_len > 42:
            logger.error("  X bot name too long (%d > 42): %s", worst_len, worst_name)
            ok = False
        else:
            logger.info("  bot names: max %d/42 (%s)", worst_len, worst_name)
    return ok


# ===========================================================================
# Autonomous deploy to Microsoft Copilot Studio (Dataverse Web API, stdlib only)
#
# Self-contained so this one file, dropped into any brainstem, can BOTH package a
# connected-agents solution AND import + publish it into a real Copilot Studio
# environment — no pac CLI, no third-party packages. App-registration credentials
# come ONLY from env vars or a settings file, never from chat, and the secret is
# never echoed back. Same proven path as the T2P deploy agent: service-principal
# token -> ImportSolution -> PvaPublish (children first, orchestrator last).
# ===========================================================================

_DEPLOY_AUTH = "https://login.microsoftonline.com"


def _http(url, data=None, headers=None, method=None, timeout=300):
    """Minimal stdlib HTTP: dict data -> form-encoded (OAuth), else JSON bytes."""
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    elif data is not None and not isinstance(data, (bytes, bytearray)):
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(body) if body[:1] in ("{", "[") else body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body
    except Exception as e:  # network / DNS / timeout
        return 0, str(e)


def _extract_dyn_creds(creds):
    """From a settings dict ({IsEncrypted,Values} or bare), a Values dict, or a
    JSON string -> {client_id, client_secret, tenant_id, resource} or None."""
    if isinstance(creds, str):
        try:
            creds = json.loads(creds)
        except Exception:
            return None
    if not isinstance(creds, dict):
        return None
    vals = creds.get("Values", creds)
    cid, sec = vals.get("DYNAMICS_365_CLIENT_ID"), vals.get("DYNAMICS_365_CLIENT_SECRET")
    ten, res = vals.get("DYNAMICS_365_TENANT_ID"), vals.get("DYNAMICS_365_RESOURCE")
    if not all([cid, sec, ten, res]):
        return None
    return {"client_id": cid, "client_secret": sec, "tenant_id": ten, "resource": str(res).rstrip("/")}


def _deploy_creds(kwargs):
    """Resolve app-registration creds for deploy — env / settings file ONLY, never
    from chat. Returns (creds_dict, source_label) or (None, None)."""
    candidates = [
        os.path.expanduser(kwargs["credentials_path"]) if kwargs.get("credentials_path") else None,
        os.environ.get("RAPP_DEPLOY_SETTINGS"),
        os.path.expanduser("~/.rapp_deploy_settings.json"),
        "local.settings.json",
    ]
    for cand in candidates:
        if cand and os.path.isfile(cand):
            try:
                c = _extract_dyn_creds(json.load(open(cand)))
                if c:
                    return c, cand
            except Exception:
                pass
    c = _extract_dyn_creds({"Values": dict(os.environ)})
    if c:
        return c, "process env"
    return None, None


def _sp_token(client_id, secret, tenant, resource):
    """Service-principal (client-credentials) token for the Dataverse env."""
    code, t = _http(f"{_DEPLOY_AUTH}/{tenant}/oauth2/v2.0/token",
                    data={"grant_type": "client_credentials", "client_id": client_id,
                          "client_secret": secret, "scope": resource.rstrip("/") + "/.default"},
                    headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200 or not isinstance(t, dict) or "access_token" not in t:
        raise RuntimeError("service-principal auth failed: " + str(t)[:200])
    return t["access_token"]


def _dataverse_action(resource, token, action, body=None, method="POST"):
    data = json.dumps(body).encode() if body is not None else None
    return _http(resource.rstrip("/") + "/api/data/v9.2/" + action, data=data, method=method,
                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                          "Accept": "application/json", "OData-MaxVersion": "4.0",
                          "OData-Version": "4.0"})


def _import_solution(resource, token, zip_bytes):
    """ImportSolution (unmanaged, overwrite) then PublishAllXml."""
    code, r = _dataverse_action(resource, token, "ImportSolution", {
        "OverwriteUnmanagedCustomizations": True, "PublishWorkflows": True,
        "ImportJobId": str(uuid.uuid4()),
        "CustomizationFile": base64.b64encode(zip_bytes).decode()})
    if code not in (200, 204):
        raise RuntimeError("ImportSolution failed (%s): %s" % (code, str(r)[:400]))
    _dataverse_action(resource, token, "PublishAllXml")


def _find_botid(resource, token, schema):
    qs = urllib.parse.urlencode({"$select": "botid,schemaname",
                                 "$filter": "schemaname eq '%s'" % schema,
                                 "$orderby": "createdon desc", "$top": "1"})
    code, r = _http(resource.rstrip("/") + "/api/data/v9.2/bots?" + qs,
                    headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    rows = (r.get("value") if isinstance(r, dict) else None) or []
    return rows[0]["botid"] if rows else None


def _publish_botid(botid, resource, token):
    """Publish ONE bot via the Dataverse PvaPublish Web API action. PURE HTTPS —
    no pac/CLI/subprocess — so this agent.py runs identically in a local brainstem
    AND inside an Azure-Function-hosted brainstem (no binary to ship)."""
    code, r = _dataverse_action(resource, token,
                                "bots(%s)/Microsoft.Dynamics.CRM.PvaPublish" % botid, {})
    if code in (200, 204):
        return {"bot_id": botid, "status": "publish_requested", "via": "PvaPublish"}
    return {"bot_id": botid, "status": "publish_failed", "via": "PvaPublish", "error": str(r)[:160]}


def _publish_connected(bot_schemas, resource, token):
    """Publish every bot — CHILDREN first, ORCHESTRATOR last (a connected-agent
    root cannot publish until its invoked sub-agents are published)."""
    if not bot_schemas:
        return []
    orch = bot_schemas[0]
    order = list(bot_schemas[1:]) + [orch]
    out = []
    for schema in order:
        botid = _find_botid(resource, token, schema)
        if not botid:
            out.append({"schema": schema, "status": "not_found"})
            continue
        out.append({"schema": schema, **_publish_botid(botid, resource, token)})
    return out


def _run_deploy(zip_bytes, bot_schemas, orch_display, kwargs):
    """Import + (optionally) publish the connected solution into Copilot Studio.
    Returns a result dict with a human `summary`; never includes the secret."""
    creds, src = _deploy_creds(kwargs)
    if creds and kwargs.get("environment_url"):
        creds = {**creds, "resource": str(kwargs["environment_url"]).rstrip("/")}
    if not creds:
        return {"status": "creds_missing",
                "summary": "NOT deployed — no app-registration credentials found.",
                "how_to": ("Set env DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / "
                           "DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE, or pass "
                           "credentials_path=<local.settings.json>, or place "
                           "~/.rapp_deploy_settings.json. Secrets never travel through chat.")}
    publish = bool(kwargs.get("publish", True))
    try:
        token = _sp_token(creds["client_id"], creds["client_secret"],
                          creds["tenant_id"], creds["resource"])
    except Exception as e:
        return {"status": "auth_failed", "summary": "NOT deployed — service-principal auth failed.",
                "error": str(e)[:300], "creds_source": src, "environment": creds["resource"]}
    try:
        _import_solution(creds["resource"], token, zip_bytes)
    except Exception as e:
        return {"status": "import_failed", "summary": "Import FAILED.", "error": str(e)[:400],
                "environment": creds["resource"], "creds_source": src}
    published = _publish_connected(bot_schemas, creds["resource"], token) if publish else []
    npub = sum(1 for p in published if p.get("status") in ("published", "publish_requested"))
    summary = ("Imported into " + creds["resource"] + " and "
               + (("published %d/%d bots. " % (npub, len(published))) if publish else "skipped publish. ")
               + "Open Copilot Studio, select that environment, open '"
               + orch_display[:42] + "' and use the Test pane.")
    return {"status": "deployed", "summary": summary, "environment": creds["resource"],
            "orchestrator": orch_display[:42], "publish_enabled": publish,
            "published": published, "creds_source": src,
            "test_in_studio": "https://copilotstudio.microsoft.com"}


# ---------------------------------------------------------------------------
# RAPP agent wrapper
# ---------------------------------------------------------------------------

class ConnectedSolutionAgent(BasicAgent):
    """Generate a connected-agent (orchestrator + sub-agents) Copilot Studio solution."""

    def __init__(self):
        self.name = "ConnectedSolutionAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn an agent stack (a folder of BasicAgent *.py files + optional "
                "metadata.json) or an explicit list of sub-agents into ONE import-ready "
                "Microsoft Copilot Studio connected-agent solution: an orchestrator plus "
                "one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. "
                "When an agent.py carries its compiled CapIR (t2p-capir/1.0) — or one can be "
                "recompiled from its seeded data — each sub-agent ALSO gets a REAL "
                "deterministic capability topic that runs the same steps as the agent.py's "
                "perform() (trigger -> the user's real query -> filter the seeded records -> "
                "branch -> respond, plus the document for artifact capabilities); only the "
                "data is mocked, so flipping the in-topic Table() to a live Dataverse / "
                "SharePoint connector is the one-line move to production. No code deploy. Bot "
                "names are auto-capped to 42 chars and orchestrator channels default off so it "
                "imports and publishes fully headlessly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "stack_dir": {
                        "type": "string",
                        "description": "Path to an agent stack folder. Each BasicAgent *.py under it "
                                       "(or its agents/ subfolder) becomes one connected sub-agent; "
                                       "metadata.json (name/description/features/starters) shapes the orchestrator.",
                    },
                    "subagents": {
                        "type": "array",
                        "description": "Alternative to stack_dir: explicit sub-agents, each an object with "
                                       "agent_name, display_name, description, instructions.",
                    },
                    "solution_name": {
                        "type": "string",
                        "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
                    },
                    "solution_display_name": {"type": "string", "description": "Solution friendly name."},
                    "orchestrator_name": {
                        "type": "string",
                        "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
                    },
                    "orchestrator_channels": {
                        "type": "boolean",
                        "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false "
                                       "(headlessly publishable). True requires a maker-portal publish.",
                    },
                    "capir_mode": {
                        "type": "string",
                        "description": "How to build the deterministic per-capability topic inside each "
                                       "sub-agent (the topic that runs the agent.py's perform() logic on STATIC "
                                       "synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else "
                                       "real seeded data, else SYNTHESIZES static stand-in records from the "
                                       "agent's inferred data shape — so EVERY agent.py maps to a self-documented "
                                       "topic; 'static' uses only real seeded data (no synthetic stand-in); "
                                       "'embedded' uses only an embedded CapIR; 'off' emits instructions-only "
                                       "sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
                    },
                    "version": {"type": "string", "description": "Solution version, e.g. 1.0.0.0."},
                    "output_path": {
                        "type": "string",
                        "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
                    },
                    "deploy": {
                        "type": "boolean",
                        "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot "
                                       "Studio (Dataverse) environment and publish every bot (sub-agents first, "
                                       "orchestrator last) — no pac CLI needed, stdlib only. App-registration "
                                       "credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) "
                                       "or a settings file — NEVER from chat. Default false (package only).",
                    },
                    "publish": {
                        "type": "boolean",
                        "description": "When deploy=true, also publish the bots after import (default true). "
                                       "false imports without publishing.",
                    },
                    "credentials_path": {
                        "type": "string",
                        "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE "
                                       "(under a top-level 'Values' object or at the root). Used only for deploy; "
                                       "the secret is never echoed back. If omitted, env vars / "
                                       "~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Optional override for the target Dataverse environment URL (e.g. "
                                       "https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, "
                                       "default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a "
                                       "distinct solution instead of updating ones that already exist.",
                    },
                    "publisher_name": {
                        "type": "string",
                        "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh "
                                       "publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
                    },
                    "publisher_display": {
                        "type": "string",
                        "description": "Solution publisher friendly name (default 'Default Publisher').",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        stack_dir = kwargs.get("stack_dir")
        subagents_in = kwargs.get("subagents")
        if not stack_dir and not subagents_in:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide 'stack_dir' (a folder of BasicAgent *.py + optional metadata.json) "
                           "or 'subagents' (a list of {agent_name, display_name, description, instructions}).",
            }

        meta: Dict[str, Any] = {}
        if stack_dir:
            sd = Path(stack_dir)
            if not sd.exists():
                return {"status": "error", "agent": self.name, "message": f"stack_dir not found: {sd}"}
            subs = _subagents_from_stack(sd, capir_mode=str(kwargs.get("capir_mode") or "auto"))
            meta = _load_stack_metadata(sd)
            fallback = _humanize(sd.name)
        else:
            subs = []
            for s in subagents_in:
                dn = s.get("display_name") or s.get("agent_name") or "Agent"
                subs.append(SubAgentSpec(
                    agent_name=s.get("agent_name") or dn,
                    display_name=dn,
                    description=(s.get("description") or "").strip() or f"Handle {dn} requests.",
                    instructions=s.get("instructions") or "",
                    capir=s.get("capir") if isinstance(s.get("capir"), dict) else None,
                ))
            fallback = kwargs.get("solution_name") or "Connected Agents"

        if not subs:
            return {"status": "error", "agent": self.name, "message": "No sub-agents found to bundle."}

        short = re.sub(r"\b(Agent\s+Stack|Agent|Stack)\b", "", meta.get("name", "")).strip()
        unique = re.sub(r"[^A-Za-z0-9]", "",
                        kwargs.get("solution_name") or meta.get("id", "") or fallback.replace(" ", ""))
        display = kwargs.get("solution_display_name") or meta.get("name") or f"{fallback} Agents"
        orch_name = kwargs.get("orchestrator_name") or f"{short or fallback} Orchestrator"
        orch_instructions = _orchestrator_instructions_from_metadata(meta, subs) if meta else ""

        spec = ConnectedSolutionSpec(
            solution_unique_name=unique or "ConnectedAgents",
            solution_display_name=display,
            orchestrator_display_name=orch_name,
            subagents=subs,
            orchestrator_instructions=orch_instructions,
            orchestrator_channels=bool(kwargs.get("orchestrator_channels", False)),
            solution_version=kwargs.get("version", "1.0.0.0"),
            # publisher controls — a fresh publisher_prefix mints brand-new bot
            # schema names (an isolated, clearly-distinct solution), instead of
            # updating bots that already exist under the default 'rapp' prefix.
            publisher_prefix=re.sub(r"[^a-z0-9]", "", str(kwargs.get("publisher_prefix") or "rapp").lower())[:8] or "rapp",
            publisher_unique_name=kwargs.get("publisher_name") or "DefaultPublisher",
            publisher_display_name=kwargs.get("publisher_display") or "Default Publisher",
        )
        packager = ConnectedSolutionPackager(spec)
        out = Path(kwargs.get("output_path") or f"{spec.solution_unique_name}_connected_solution.zip")
        data = packager.package(output_path=out)
        ok = validate_connected_solution(out)

        # autonomous deploy: import into Copilot Studio + publish the bots
        # (children first, orchestrator last). Creds come ONLY from env / a
        # settings file — never from chat.
        deploy_result = _run_deploy(data, list(packager.bot_schemas), display, kwargs) \
            if kwargs.get("deploy") else None

        capir_topics = sum(1 for s in subs if getattr(s, "capir", None))
        msg = (f"Generated '{out.name}' — {len(packager.bot_schemas)} bots "
               f"(1 orchestrator + {len(subs)} connected sub-agents, "
               f"{capir_topics} with a deterministic capability topic), "
               f"{round(len(data)/1024,1)} KB. Validation: {'pass' if ok else 'fail'}.")
        if deploy_result:
            msg += " " + deploy_result.get("summary", "")

        data_block = {
            "solution_path": str(out),
            "size_kb": round(len(data) / 1024, 1),
            "orchestrator_schema": packager.orch_schema,
            "sub_agents": [s.display_name for s in subs],
            "capir_topics": capir_topics,
            "deterministic_topics": [s.display_name for s in subs if getattr(s, "capir", None)],
            "validation": "pass" if ok else "fail",
        }
        status = "success" if ok else "error"
        if deploy_result:
            data_block["deploy"] = deploy_result
            if deploy_result.get("status") not in ("deployed",):
                status = "partial"
        else:
            data_block["deploy_hint"] = ("Pass deploy=true to import + publish into your Copilot Studio "
                                         "environment automatically (creds from env DYNAMICS_365_CLIENT_ID/"
                                         "SECRET/TENANT_ID/RESOURCE or a settings file via credentials_path).")
            data_block["m365_exposure"] = ("Set orchestrator_channels=true and publish the orchestrator "
                                           "in the maker portal for M365/Teams exposure.")
        return {"status": status, "agent": self.name, "message": msg, "data": data_block}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target:
        print("usage: python connected_solution_agent.py <stack_dir> [output.zip]")
        sys.exit(1)
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    result = ConnectedSolutionAgent().perform(stack_dir=target, output_path=out_path)
    print(json.dumps(result, indent=2))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
