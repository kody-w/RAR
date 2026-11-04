---
name: "rar-discreetrappers-email-drafting"
description: "Drafts an email with proper formatting and sends it to a Microsoft Power Automate flow endpoint for processing and delivery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/email_drafting_agent", "rar_sha256": "65ba2c8d5d2817d99fdf6463b1da6e4722a6a627b8b3a77120999bf930fb80e6", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Bill Whalen", "tags": ["integrations", "email", "power-automate", "microsoft"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `email_drafting_agent.py` and embedded as the fenced Python below (sha256 65ba2c8d5d2817d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `email_drafting_agent.py` first:

```bash
python3 email_drafting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 email_drafting_agent.py   # or on stdin
python3 email_drafting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/email_drafting_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/email_drafting_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/email_drafting_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VZeXPaypb/KiruH0ketiV25Jk7NSCxSkICoY34lqOltaENqQWIvHz36QYcO7ZzK3cqVY9KlUF9+uzL7yhfa2YJ/TSv3deGQRQRmm9GIKnd1BxQ2HmQwSBN0Bmbmy4sCDMhQGwGEXEIoE9keZqBnHDTPDYhDBIPnTtEARKnIAJIwJQwCSGw87RIXUhI6QERD0qYImpAuFF6IBBplgYJxDwwOxsUxRMfB0TBHuTVHVIGHM04i0BRu//8100tQN9r919rdmQW6FFthFU6a4juDjyQQHQlMhMPnWUVsg7bgzTFiqJHDnCJ66+PBYjcG+Jf/9oezNwrPt0/JMT1U5RWCGxI/Elczu48AD9+uD798OmZEJn5Iw1MXx5bqVO9IsCPXpLY9isC2/5wQ3z+6yWXNzTWWyIUBNP2Y2R/8Yr4xcnrS8iZaQ7NxAav7jwfoCsfEhzkCGv9wvK8euEw/PmDYHxgb4nAfR1uZcUTQUHYaeIGXpkD58eL6EKSQgKH4y7DNx/N683HMo9eScGfHMAyT4iwSJM7p4yz4uPXt0T481AroAnL4qF2j76DPE/zh9rNz2hjlICmBy7EI2Ew4x8lURutHgfKWhQG69EjNgQk+yBPE+xPYm/mgWlFAFuHTXi28I6QImAWAFkFcT1YAKUcIMpzhkMf0Zs4V+8eam+1+faDo1966JKAdwVExfnx03ueMQMkUzWjEoywtR9/ZuvaB8T3hCYyMzdjAFHMkGI52JUBMuFciLaZYMkWQLWfwQrp++ld1WD627RCJfQbFMJ19ttUOhftP1XqR46YxaMP4whV2lm3HGSRaYOPHx4eElxk/23l//PhzbVzx310cH9DF99Jc5TilyjitL1+vXmPDKaYAqbvHto2PrTtdw+ty6n1s2Nkzfn8ycJ3qV50IUz84ue75MjPpmNCE9P+tLifuxQme/710woPiinSDxOv8xK8U3k/Pvr2Oho+MB2QFz+LBJMmEFl0u66yaxcxsywKbBMPUhK3q9fl/kZCDoosTQrcj3GGgQIWqCcW8J38/Em/vDn3xT9fJM7Nk95/Xv++11+eBN9dOuajnTqorSXE5yZF3RBNqvnX72vERWnjYf/LrfiMOi41UOC2i6buqwlz5eiWUVT9DdsnIzHf7wZDcISf7xsURf31fi/+oR6jAvxHJpL7UBsjN6CGg6zHMOsKxi5ueeORO0I+yyFwHFEJvRfeb7/dU89PwdEGGSRG5z8o+wmzIF477pec9qsOe+2sAUKrmJhIbbvMUaNGTkDj4CP49O1NEX6qfUPAMkHHpY2Vxbjyjz9ewFfZTktI5GUCgxhgM9d4gqN/EE2HHCCkWgQYBlzoEJbFXRhbnbrEl/91AoSmAYAr1A0QJfmiNBEaeDwDgS93BJ40aR54QWJGxGogSQ/J+QjLyVAMQL5H0bcqCG4RlrjFX3CBfnmP3V1WfTlPJkSAdVwxMzSksqKMwB3WX/NBctXWxrj+COwSsYtSG8l2UZoVNzjsabQHF7RSbPGC4KCJZ8M0r868kT/uMbMvX75YZuE/JBe83SIuy0NBIoLv6hC3t8gINwo8Hz4kwPZT4sPXbx+IfxN/d+vMHMuQENq/ehtpOJfFBYHQannBuzh0qLOdvf3129WViE2CCgLFJnADcLkcBckWo8+LX+Xp4LbZ6T5hs8v8wPgsgHfEzCW+64uE4iOE2Qgf9WK0nWSoAEFiV4iricz57skzSkPtvnCrGwT2wFnqFwuhDaxi/Ggj8i+EwEioYtMIly1S80yELqcJGhXR96hfniMm+YeCGD6xuCMWON/OYCTzc/MqwzUvcUEJ/3T9vIIl4PCQ4J0JYFedB9HFPYgIeca+hvQWxxz1ijg2zwvcRfaZBjUTh1inJhKeP6AucElsM8ehsFO8pBFeGTh47v7XNaUKPy0j5+w/pCnmdI2Cc43KOQf/w2slmssAmVO7T9DQuKklCNq9Xifx5viE+Qq8dF60gwE4/3qBYfDPH5dm8fzFjO4IPkApg1LzmfxcYQSWWOCABSiVIHZPXmDFAhTlM0OIYATihEEs0gW1qOsDM8/NCv9GiOxXBF/cazoOqugCV0JKDBnmH4pC4O6tLJxIeOZeFl0kCsf6LA4nGV75UHSDxI5KBCbMpMILEjxP8HPGRxGKHuKIUvBs+Rst/t/2/VPznrHj3wmcPa/LESrC6EeL8auKpIxr959rKA/Rr8vajL74qInU/nrHvitef9+xTy8hUNMCbyS9tSh9y2X00jFPLLI8iE1UtKh6gyzAbfYtO8Tvab/B5jypeZZyzYVnc9LLIbqDFhp4ec/y9TuAv5bNdSAi8tzMbwvcJsjGHYW4od+Xdo/OfmlUXu8UvomaN7rU7Vhm0+47HafZb/QcmnYdt9vutqyGY3ZBu9dsml2z2+xZfatl9nqNJkXTtOXSLcq1+hToIn5FWuY2eMT9L8B6HNJ8i+TdQqTL8zF65FwNuCiC/fR9Mp87wsWOrzWr20aU03YxG1w+DFlXN3qTDBf+nKS7tmEO6WLc7tqtdVuxGbpFm1a22DJNZsMXPXsBZouBYlmTlTzXtttQ7YruMqS5Ke3tqe2CWsxhvOa1Y9kCvXA8WRrF1pY6x07ismKU9AVnv68P9Hzn6Gp9sN0fQTlNuDlkGX23ZPsbWRlrhzCa7xjVE5xRm15TU7Gi12NxWaU04NVmEKl9TU1PdXoBe8PSOWliziyZrnAEutBKS2NVDDOZ1filla4EXtmC5cKhDs2hcFICSm4fl+mwMcvt9Uay+/4cTGRDYSfLUyyyDrPIqmjW94x977DRKV/dS32ztU3VLmX3PMtujfviEo4Cu6rcsJAdEU61dd7ukiDsiMMRdAb5SBtnq+ZuFtHjmbGtL/v79SCb2i14ajuOtZky+3ZdXxm9YMkHUZw6q/BA8v2AXQWmnAvlNOWsJU/6w/jEuPPuyOZbTb+52suCMqAML1TGLY00vBiWPsUU5UgrrHrPsifyemnqlbeB7rrbmnTA/rjgmcbU6kV5Y7hxpKGx2Ta3yuS0aSEvBOujFcunUO5z9FHk9lHYbfmtYp5KqnxsCRNflQZaqLLBfikCYQA2xdBKTFX0i0mQMJ1pUR1ZUB/aQtmo0p5PmYOlNW4AfcEbB3rX6bObySDYuTwzXAmzQzgQkrzXXIdCsO7YCuV7zYGVthv9HecxsiNAtWUM0rE+sTdKbzIeGIupIO/VuNOWyIO5n086Y6EhrzKTCvj2MlenZDXv9MCpH4WNiSvRUkKSkhWvYkdtzICxnHN66ImbjpO2wShilWOebWVIkqR+Ik2+Pk2qJO936uVM16kjKe5Pe1aWyDCiSU+rt47VzBekQ+By7FSI9kF9uzA3c/vAybq3dPdGGTBzQWaj6Wp2CMTZxAWHpesBZT73+lE5c3UhEYHfd4e7+VHnhwJVNlyuYRRgOxruVqBcNjbppl/4a5ged1nsohwvuaORzVKG2ZTt3TDpmctJu7kbNYDmZWDhcY2gmM0Hne2oAkyzQ6mWNFWPGc9QB35zEuOhcFiTSjgbx+XItVjNO+SFcDC3e0YOStLyOZVpbESRl4/ifgkPvuqhGskNYyAPI+ogifa2bWSKMCmiXd0eO0dDD08jzpovo0yo8sStMoODVGVH8/Zq6Z2YthIujNFKOiryYG3I3XSqlGrZYSaj/jjNeMXMO6zWAuV8ymaCtN4c69V+uZu7xbJS1nSuneor58SYlhGFVhaFo4VuIJwR+r2dylCnUN+RU6VpQDjgxSUNvVDn2cB1Sl40lobTXMeMzXL0vLNQ2i7wqAyEk+Fix7XWG2F+bPJxk8lX3W3dURgopuSGcshVKLpgNWzTBiNvdWGgHZX1yACV3N8uE1mxxZZ1MpZsk59ylrKT8vGsUDhrs6EyjlarTTR0/V68iHMNctkijt2yaOSCO9Rta0cVop6M9VVJNf0jtwwSvsOnnMaN1ulCn1NK3Gtv6V0ke9x2lEMouTYMkS2T6boCIIunp5AONmvKWypFGE4bltnwrXg9YYdKzCeLOQ+GfjPh6knPEia81d/yM1lriKTbKSZS2dgbmyZIFVoSohFl2cZp4FnHLoiH86Jdl47QncbtLSxkV2CTeLjasFs4FVn2mBg8LR0PuwyM89HBR3lrmzs/8BlnUbmVP6D5sVYM2g1mMhH6lemtyQ0JDpYGOutYHixO8kGJgoW+qcJU7ysLifcKRRl36FSlHS3h6NFSTsGKT5HjaI9T5VVdMdjg4DbENOPCep0d5dHMy2EZtGCvzrGlrfHS3rPIreLqykqHlrtBp0WiNYcO6s2s6jTjcB1tGo0g7ZLj+e6USqAqxFOdUZvcTkVTbX9gbb05pedpR3frAyeez8sojVoHd903Gm7DW83tyZwOcn+hczYztdOJOiHrpwaNir3Msz5oGc7aIW0974JW1hlz/Ij0kg5Zcpxqt/r1pjzeUuV8s1jXMz04HFZRtm6oYbuanZhWf9pclSc5o6W2HIDpkNwoAlvVZ8e10DFnh7TMBl3JGrZ6QGkc1WFHy3Z5wuS7qX7cO8psvw+DaaKazYmpqys9HVVBspekbkML2YUcxGswpwzaZLVpCXw/VZIJKdjtnui2XL3Nj8cCcqWpsfowboSbWFqI5bYV7Q4JNzhxC7FoHfyVlIkUdA9mEgC2NWYM56CUhq7RQmvQVQd9jpO2ZvsQhG5gOMctUJsFB0m7f1B9vhoKA0PSWOjlvV3WL1vi0hglFblnoRrnI2F1yETGYoxD6S3HM1ajTkPe9Xfi1Mi2JLccFHPTlYaFIOhrjmvveyI1mjjbdpe1Vswu2XWDseo6whjKXucIy5xLt852M0j4Iuoou6m67ZDTmXJYkZ1QlwNJSttNKRAkquuOQ2czDexiZlkNzWHdeTkMKbI7Sj2yXQktElrdY9YaH4up3W+GAasqlIt6b5OkjtRp7yXRfiLGvRGdtPRFpPVAlbXFbUteNlphlnYPu1a9c1K74V7je2V3LBU0l2oK7BrL/ZLW6zvQLI9ossYVX0YNWkvM5arnNPSOm+zAuh7HK0EbLvrBdEHTRlV0e8XgyPI59BblsF8tpHnXWQzmgcrBnrJvlEtqCRdyteLLWTcL+0p70eTbdWG1Z/267ToraiFoyagX1etMIjVMpa8dabHbbpnUdBzO856utk71YE4WobUKXBcBsHWn706P+srpwny2g4AjtbUVH3QnXRSzkbaF+pTWs12yZiPPYUppxHhTg7e783zU6dfT2NGM+owe92JWIPshuaJPhThJXL2ifIQK99l215/Knij3BbTWmuFsQI8EMQk3S5PetxdzTRul/ZmNMOafCKrizfK6yv7kvRDGs78NOl8QcLpHMs+702e0N5jO/VnW/c8UQKtDbgdI/GUBKKLSu8LqJ/ifX+D/7ZnDrfO8jhfV5TUKXiOP8Gl3h6aH/3e4hrZ+4OXm5RXezcUBeIfHbwlun96Rowfx0wsErMr55d15M0HqIIW+/R98S1XLFh8AAA== -->
