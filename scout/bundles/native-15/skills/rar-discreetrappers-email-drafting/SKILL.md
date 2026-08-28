---
name: "rar-discreetrappers-email-drafting"
description: "Drafts an email with proper formatting and sends it to a Microsoft Power Automate flow endpoint for processing and delivery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/email_drafting_agent", "rar_sha256": "b068d41da7ee04fa27d8ff0b267977914aab1eae186017ad47572e2b2c6cb399", "source_kind": "rar-agent", "source_commit": "4a5ea1bb2d453217e8cf5ad16c44542a06d6066d", "author": "Bill Whalen", "tags": ["integrations", "email", "power-automate", "microsoft"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/email_drafting_agent`. The original RAPP
agent is preserved byte-for-byte in `email_drafting_agent.py` and in the RCI capsule.

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

Drafts an email with proper formatting and sends it to a Microsoft Power Automate flow endpoint for processing and delivery.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "attachments": {
      "description": "Optional. List of attachment file names or identifiers.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "bcc": {
      "description": "Optional. List of email addresses to BCC.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "body": {
      "description": "The full body of the email. This can include any content the caller desires.",
      "type": "string"
    },
    "cc": {
      "description": "Optional. List of email addresses to CC.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "importance": {
      "description": "Optional. Importance level of the email.",
      "enum": [
        "low",
        "normal",
        "high"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The subject line of the email.",
      "type": "string"
    },
    "to": {
      "description": "Email address of the primary recipient.",
      "type": "string"
    }
  },
  "required": [
    "subject",
    "to",
    "body"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `email_drafting_agent.py` and embedded as the fenced Python below (sha256 b068d41da7ee04fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `email_drafting_agent.py` first:

```bash
python3 email_drafting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 email_drafting_agent.py   # or on stdin
python3 email_drafting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
from agents.basic_agent import BasicAgent

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/email_drafting_agent",
    "version": "1.0.0",
    "display_name": "EmailDrafting",
    "description": "Drafts professional emails and sends via Microsoft Power Automate flow endpoint.",
    "author": "Bill Whalen",
    "tags": ["integrations", "email", "power-automate", "microsoft"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import os
import requests
from typing import Optional, List


class EmailDraftingAgent(BasicAgent):
    def __init__(self):
        self.name = "EmailDrafting"
        self.metadata = {
            "name": self.name,
            "description": "Drafts an email with proper formatting and sends it to a Microsoft Power Automate flow endpoint for processing and delivery.",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "string",
                        "description": "The subject line of the email."
                    },
                    "to": {
                        "type": "string",
                        "description": "Email address of the primary recipient."
                    },
                    "cc": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional. List of email addresses to CC."
                    },
                    "bcc": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional. List of email addresses to BCC."
                    },
                    "body": {
                        "type": "string",
                        "description": "The full body of the email. This can include any content the caller desires."
                    },
                    "attachments": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional. List of attachment file names or identifiers."
                    },
                    "importance": {
                        "type": "string",
                        "description": "Optional. Importance level of the email.",
                        "enum": ["low", "normal", "high"]
                    }
                },
                "required": ["subject", "to", "body"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

        # Get Power Automate URL from environment variable
        self.power_automate_url = os.environ.get(
            'EMAIL_POWER_AUTOMATE_URL', '')
        if not self.power_automate_url:
            import logging
            logging.warning(
                "EMAIL_POWER_AUTOMATE_URL environment variable not set. Please configure it to use this agent.")

    def perform(self, **kwargs):
        subject = kwargs.get('subject')
        to = kwargs.get('to')
        body = kwargs.get('body')
        cc = kwargs.get('cc', [])
        bcc = kwargs.get('bcc', [])
        attachments = kwargs.get('attachments', [])
        importance = kwargs.get('importance', 'normal')

        try:
            # Check if Power Automate URL is configured
            if not self.power_automate_url:
                return json.dumps({
                    "status": "error",
                    "message": "EMAIL_POWER_AUTOMATE_URL environment variable is not configured. Please set it before using this agent."
                })

            if not subject.strip():
                raise ValueError(
                    "The 'subject' parameter is required and cannot be empty.")
            if not to.strip():
                raise ValueError(
                    "The 'to' parameter is required and cannot be empty.")
            if not body.strip():
                raise ValueError(
                    "The 'body' parameter is required and cannot be empty.")

            body_html = body.replace('\n', '<br>')

            email_draft = {
                "subject": subject,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "body": body_html,
                "attachments": attachments,
                "metadata": {
                    "importance": importance,
                    "isHtml": True
                }
            }

            headers = {
                "Content-Type": "application/json"
            }

            response = requests.post(
                self.power_automate_url, json=email_draft, headers=headers)

            if response.status_code in [200, 202]:
                return json.dumps({
                    "status": "success",
                    "message": "Email draft sent to Power Automate successfully",
                    "response": response.text[:1000]
                })
            else:
                return json.dumps({
                    "status": "error",
                    "message": f"Failed to send email draft to Power Automate. Status code: {response.status_code}",
                    "response": response.text[:1000]
                })

        except Exception as e:
            return json.dumps({
                "status": "error",
                "message": f"An error occurred: {str(e)}"
            })
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
