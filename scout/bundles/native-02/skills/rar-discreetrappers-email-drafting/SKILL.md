---
name: "rar-discreetrappers-email-drafting"
description: "Drafts an email with proper formatting and sends it to a Microsoft Power Automate flow endpoint for processing and delivery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/email_drafting_agent", "rar_sha256": "b068d41da7ee04fa27d8ff0b267977914aab1eae186017ad47572e2b2c6cb399", "source_kind": "rar-agent", "source_commit": "4a5ea1bb2d453217e8cf5ad16c44542a06d6066d", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "email_drafting_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/email-drafting:b30dd658d5172a7468941edd1136c25e460b255386e50390322fcb870c5b17df", "kind": "skill"}, "author": "Bill Whalen", "tags": ["integrations", "email", "power-automate", "microsoft"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/email_drafting_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `email_drafting_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
