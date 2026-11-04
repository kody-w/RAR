---
name: "rar-discreetrappers-email-drafting"
description: "Drafts an email with proper formatting and sends it to a Microsoft Power Automate flow endpoint for processing and delivery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/email_drafting_agent", "rar_sha256": "65ba2c8d5d2817d99fdf6463b1da6e4722a6a627b8b3a77120999bf930fb80e6", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Bill Whalen", "tags": ["integrations", "email", "power-automate", "microsoft"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VZeZOaWLv/KpTzR5LXToPiArl3bl0FV0BQRMDpqYTlsMkmHFTMm+9+z1E73enuTM3cStVrpaqV85xnX34P+dqwKhhkReNTYxjGMaEHVgzSxl3DBaVThDkMsxSd8YXlwZKwUgIkVhgTxxAGRF5kOSgILysSC8Iw9dG5S5QgdUsihATMCIuQQqfIysyDhJIdEfGgghmiBoQXZ0cCkeZZmELMA7NzQFk+8nFBHB5AUd8jZcDJSvIYlI1Pf/x51wjR98anrw0ntkr0qDHCKl00RHcHPkghuhJbqY/O8hpZh+1BmmJF0SMXeMTt1/sSxN4d8a9/7Y5W4ZcfPj2kxO1TVnYEHEj8TlzP7n0A37+7PX334YkQmfkjDcyeH9uZW78gwI+ekzjOCwLHeXdH/PHncy6vaOzXRCgIlhMkyP7yBfGzk5eXkDOzAlqpA17ceTpAV96lOMgx1vqZ5UX9zGH48xvBBcDZEaH3MtzaSiTCknCy1Av9qgDujxfRhTSDBA7HfY5vfrZuNz9XRfxCCv4UAFZFSkRllt67VZKX77++JsKfh0YJLViVD41P6Dsoiqx4aNz9jDZBCWj54Eo8kgYz8bMi66PV54G2lqXBevQZGwLSQ1hkKfYncbCK0LJjgK3DJjxZeE8oMbBKgKyCuB5sgFIOENUlw2GA6C2cq/cPjdfafPvB0c89dE3A+xKi4nz/4S3PWCGSubHiCoywte9/Zus6AMT3hCZyq7ASAFHMkGIF2FchMuFSiI6VYsk2QLWfwxrp++FN1WD2y7RCJfQLFMJ19stUuhTtP1XqR46YxecAJjGqtItuBchjywHv3z08pLjI/tsu/ufdq2uXjvvZxf0NXXwjzVGKX6OI0/b29e4tMphhCpi9eeg4+NBx3jy0r6f2z46RNZfzRwvfpHrWhTDxs59vkiM/W64FLUz70+J+6lKY7OnXTys8LKdIP0y8LirwRuX9+Ojby2gEwHJBUf4sElyWQmTRx3Wd37qIledx6Fh4kJK4Xb0s91cSClDmWVrifowzDJSwRD2xhG/k50/65d2lL/7+LHHuHvX+/fb3rf7yKPj+2jE/O5mL2lpK/NGmqDuiTbX//HWNuKwcPOz/diu+oI5rDZS47aKp+2LC3Dh6VRzXf8H20UjM97vBEJzgH59aFEX9+XYv/qEe4xL8RyaS99AYIzeghoOsxzDrBsaubnnlkXtCvcghcBxRCb0V3m+/3FNPT8HJATkkRpc/KPsJqyReOu5vOe3vOuylswYIrWJiInOcqkCNGjkBjYP34MO3V0X4ofENAcsUHVcOVhbjyt9+ewZfVSerIFFUKQwTgM1c4wmO/kE0HQqAkGoZYhhwpUNYFndhbHXmEV/+1w0RmgYArlA3QJTks9JEaODzBQh8uSfwpMmK0A9TKyZWA0V5SC9HWE6OYgCKA4q+XUPwEWGJj/gLLtAvb7G7z+svl8mECLCOK26GhlReVjG4x/rrAUhv2joY15+AUyF2ceYg2R5Ks/IOhz2LD+CKVsodXhBcNPEcmBX1hTfyxyfM7MuXL7ZVBg/pFW/TxHV5KElE8F0d4uNHZIQXh34AH1LgBBnx7uu3d8S/ib+6dWGOZSgI7d+8jTScq/KCQGi1uuJdHDrU2S7e/vrt5krEJkUFgWITeiG4Xo7DdIfR59Wv6nTwsd3tPWKz6/zA+CyE98TMI77ri4TiI4TZiAD1YrSd5KgAQerUiKuFzPnuyQtKQ+2+9Oo7BPbAReoXG6ENrGLy2UHkXwiJU1DFZjEuW6TmhQhdzlI0KuLvUb8+R0yKdyUxfGRxTyxwvl3ASB4U1k2GZ13jghL+8fplBUvB8SHFOxPArroMoqt7EBHyjHML6Uccc9QrksS6LHBX2Rca1ExcYp1ZSHjxgLrANbGtAofCyfCSRvhV6OK5+1+3lCqDrIrdi/+QppjTLQruLSqXHPwPr5VoLgNkTuNTiobGXSNF0O7lOok3x0fMV+Kl86odDMHl1zMMg3/+uDTLly9WfE+IIUoZlJpP5JcKI7DEEgcsRKkEsXuKEisWoihfGEIEIxAnDGKRLqhF3R5YRWHV+DdCZH9H8NW9luuiii5xJWTEkOP+oSgE7l7LwomEZ+510UWicKwv4nCS4ZUPRTdMnbhCYMJKa7wgwcsEv2R8HKPoIY4oBS+Wv9Li/23fPzXvCTv+lcDZ07ocoyKMf7QYv6pIq6Tx6Y8GykP067o2oy8BaiKNP9+w74bX33bs40sI1LTAK0mvLcpecxk9d8wji7wIEwsVLareMA9xm33NDvF73G+wOY9qXqTccuHJnOx6iO6ghQZe37N8/Q7gb2VzG4iIvLCKjyVuE2TrnkLc0O9ru0dnf2tU3u6UgYWaN7rU69pW22HcrttmWn2XZT3X63V6tN1yrR7o9Nttq2f12n2bsWmr32+1KZZlbY+lKc9mKNBD/MqsKhzwGfe/EOthO5TX6rEtxgOAtdttukcxgPJottf3EE+6DVwGoSD76eouTN2bcVclsQ+/T+1Lt7ja+LVh9zqIctopZ4PrhyObm63RJqNFMCfZnmNaQ7Ycd3oOve5oDsfSrGXnix3X5rZi2XcWYLYYaLY9WalzfbeLNj3ZW0asMGX9A7VbUIs5TNaifqpo0I/Gk6VZ7hyle+qmHi/HKSO5h0NzYBR719g0B7vDCVTTVJhDnjP2S57ZqtpYP0bxfM9tfMkdddg1NZVrdj2Wl3XGAnHTDuMNo2+yc5NdwP6wcs+6XHBLriedgCHRWWWuymGu8rq4tLOVJGo7sFy41LE9lM5aSKmd0zIbtmaFs94qDhPMwUQ1NX6yPCcy73KLvI5njG8e+setQQWbg8JY9C7b9Cin79sOPWbkJRyFTl17Uam6Mpzq66LTI0HUlYcj6A6KkT7OV+39LGbHM3PXXDKH9SCfOjQ8d1zX3k65Q6dprMx+uBTDOMncVXQkRSbkV6GlFlI1zQR7KZLBMDlz3rw3ckS6HbRXB1XSBpTpR9qY1knTT2AVUFxZjfTSbvZtZ6Kul5ZR+1vorXv0pAsOp4XItaZ2Py5aw62rDM3trr3TJuctjbwQrk92op4jlRHYkywc4qhHB3Q5z5SNeqKlSbBRBnq04cPDUgbSAGzLoZ1aGzkoJ2HKdadlfeJBc+hIVavO+gFlDZb2uAWMhWge2X2X4beTQbj3RG64kmbHaCClRb+9jqRw3XU0KvDbAzvrtJi94HOqK8ENbQ6ysTFxtlp/Mh6Yi6mkHjZJt6OQR+swn3THUktd5RYVip1lsZmS9bzbB2cmjloTT2GVlCQVO1kl7qY1A+ZyLhiRL2+7btYBo5jXTkW+UyFJksaZtMTmNK3Tguk2q5lhUCdSPpwPvKqQUcySvt6kT/UskJRj6An8VIoPYXO3sLZz5yiohr/0DmYVcnNJ5ePpanYM5dnEA8el5wNtPveZuJp5hpTKIGC84X5+MsShRFUtT2iZJdiNhvsVqJatbbZlymANs9M+TzyU45VwMvNZxnHbqrMfpn1rOem096MW0P0cLHyhFZaz+aC7G9WAa3epja1MN6dc5KijuD3LyVA6rkktmo2TauTZvO4fi1I6WrsDp4YVaQfChmttZVlUT/JhCY/Bxkc1UpjmQB3G1FGRnV3HzDVpUsb7pjN2T6YRnUeCPV/GuVQXqVfnpgCp2onnndXSP3MdLVqYo5Vy0tTB2lR72VSrNlWXm4yYcZaLmlV0eZ0G1XzK55Ky3p6a9WG5n3vlstbWbKGfmyv3zFm2GUd2HkejhWEiDBIF/f2Go86RsSenWtuEcCDKSxb6kSHyoedWomwuTbe9TjiHF9h5d6F1POBTOYgmw8VeoNdbaX5qi0mbK1a9XdPVOChn5JZyyVUke2A17LAmp+4MaaCftPXIBLXK7JapqjkybZ/NJd8Wp4Kt7ZViPCs1wd5uqVxgN/U2HnpBP1kkhQ6FfJEkXlW2CskbGo69p0rZSMfGqqLawUlYhqnYFTNBF0brbGHMKS3pd3bsPlZ9YTcqIFQ8B0bIlsl0XQOQJ9NzxIbbNeUvtTKKpi3bagV2sp7wQy0R08VcBMOgnQrNtG9LE9FmduJM1Vsy6XXLiVK1Dua2DTKNVaR4RNmOeR749qkHkuG87DSVE/SmSWcHS9WT+DQZrrb8Dk5lnj+lpsgqp+M+B+NidAxQ3jrWPggDzl3UXh0MWHGsl4NOi5tMJKa2/DW5JcHR1kF3naiDxVk9anG4MLZ1lBmMtlBEv9S0cZfNNqyrpwI7WqoZWIkZchzrCxt11dRMPjx6LTnLhajZ5EdFPPMLWIU07DcFvnJ0UTn4NrnTPENbGdD2tui0TPX20EW9md+47SRax9tWK8x65Hi+P2cKqEv53OQ2bWG/QVPtcOQdoz1l51nX8JoDN5nPqziL6aO3ZsyW1/JXc2cyZ8MiWBiCw02dbLKZkM1zi0XFXhU5A2jTXbukYxRoxubdsSCOSD/tkpUgbByaabbV8Y6q5tvFupkb4fG4ivN1axN16tmZo5lpe1Wd1ZxVOmoIpkNyq0l83Zyd1lLXmh2zKh/0FHtI94HWOm2GXT3fFylX7KfG6eBqs8MhCqfpxmpPLGOzMrJRHaYHRem19IhfqGGyBnPKZC1en1YgCDItnZCS0+nLHu0ZHXE8lpArLZ03hkkr2ibKQq52dLw/psLgLCzkkj4GKyWXKegdrTQEPD3mTPeoVaahsxI96G0GjCAoO6tzDCMvNN3TDmzapQBJhzluArEeSgNT0XnoF/19zlS0vDRHaU0eeLhJipG0OuYyZ3PmsfKX4xmvU+eh6AV7eWrmO1JYDsq55SnDUpKMtSB0Dn2ZGk3cXafH2ytun+574XjjudIYqn73BKtCyHbubjtIxTLuavvpZtclpzPtuCK7kaGGipJ12kooKVTPG0fudho65cy2W7rLe/NqGFFkb5T5ZKeWaBLavVNOj0/l1GHaUchvNMpDvbdNUifqfPDT+DCRk/6ITWljEet9UOcdeUeryxYd5VnvuKeb3fOmFx10sV/1xkrJCpmuwZ65PCxZo7kH7eqEJmtSi1XcYvXUWq76bsvoeukerJtJspL04YIJpwuWNeuy1y8HJ14soL+ohky9UOY9dzGYhxsB9rVDq1pSS7hQ65VYzXp5xGidRVvsNKXVgQ+ajueuqIWkp6N+3GxyqdKyNEY/sXKvQ1vUdBzNi76xoc/NcE6Wkb0KPQ8BsHWX8aYnY+X2YDHbQyCQ+tpOjoabLcrZSN9BY8oa+T5d87HvcpUy4vypKTq9eTHqMs0scXWzOWPH/YSXSCYiV+y5lCepZ9RUgFDhId/tmanqyyojoZXXimYDdiTJabRdWuyhs5jr+ihjZg7CmL8jqIq3ztua+5N3RhjP/jJYfUXA2QHJvOxVf6CdwnI/XWR9+pkCaK0onBCJvy4HZVz5N1j9uBoU19Xg44XDR/dpVS/r6ysWvGKe4ONeDy0f/89xI0RP/cK6vt67uzoA7/f4DcLHx/fn6EHy+HIBq3J5sXfZWpA6SKFv/wdHMf49Mh8AAA== -->
