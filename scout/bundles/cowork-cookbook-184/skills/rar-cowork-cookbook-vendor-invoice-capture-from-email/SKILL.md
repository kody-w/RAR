---
name: "rar-cowork-cookbook-vendor-invoice-capture-from-email"
description: "Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_from_email", "rar_sha256": "74aff5e7e60d62993665b35bb9bee48629a27e4eff7d50466256a2128df6d1c7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vendor_invoice_capture_from_email_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/vendor-invoice-capture-from-email:b532350cd6cbf8dc7decdb13b801d77725bb966f2b1b7fba981532af9042c217", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/vendor_invoice_capture_from_email`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vendor_invoice_capture_from_email_agent.py` is
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

Vendor Invoice Capture from Email — Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-from-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_from_email_agent.py` and embedded as the fenced Python below (sha256 74aff5e7e60d6299…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_from_email_agent.py` first:

```bash
python3 vendor_invoice_capture_from_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_capture_from_email_agent.py   # or on stdin
python3 vendor_invoice_capture_from_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Capture from Email — Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-from-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_capture_from_email',
    "version": '2.0.0',
    "display_name": 'Vendor Invoice Capture from Email',
    "description": 'Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'vendor-invoice-capture-from-email',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-capture-from-email',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'edf03ca890a66aed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-05', 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/vendor-invoice-capture-from-email', 'uses_skills': {'custom': ['vendor-invoice-capture'], 'ootb': ['Email', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_get_entity_metadata', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}, {'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VendorInvoiceCaptureFromEmail(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceCaptureFromEmail'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(VendorInvoiceCaptureFromEmail().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+15e5OiWLbvV+HmibhVfchKeYM5MRFXBUUFRFFEuzqyeGze74cIffq7342aWdXT0zPTEffPa1VmCuy93uu31mL/+mQ2tZ+VT69PGjBTZGHGceCDEjFTB5llbVZG8E8WWfAHsbO0LgOrqbOyenp+ckBll0FeB1kKtx/N2vZBhdQ+QILUyq6Im5UISMwgrpA2qH1E5eeIWdem7ScgrYeVZo3EA+E4iAByAakDdwTpJQtsUD0j4FqXpg0XggsoO8QNQOwgbpklNx6Q2jOS/MD0sd/0zCCtauSgyXP4vKqhMo5Zm883lewSmDXcYCI5XB6k3j+wRUpgZ6UDLxG+S80ksCuEZGhk/r83dyUGTj4wnYeJ4iCF1PIsb2JI13mBZgFXM8ljUD29/vzL81MAvz+9/vpkx2YFbz3pN3bLO7eZmddNCeZQJ2EwFNwdm6kHl+Ud9EoKr3NQQjsm8JYDXORx9bkCsfuM/Pd/R61ZetVPr19T5PH5+jT82zXpTdI6GwwA1TZz0wrioO5ekEncml0FFYWs08ESFXRq6r3cd36nlOXI34dnn+9MXjxQf/76lEERzMHlX59+QqDdvj6VzfD9ZaCSf/7pJc5aUH7+6TudqrFCYNcDMSj1y9vj+kEWLvy+NHBvXP8Oqd6DywJfn35Qbvjc5R70hDufXsIsSD/fCedlBp1ppjb4/NOfkYXRYkdxUNX/Ed2f74Tv/v78EPyn55uRf0HQh0IfNP+cbQ7d+lc0gcvf2T0jD0P9Ge2b/f+B9D0s3y3+T8n9sw3o35Gf/1S3f7XhGXG/PvEgDmCmmlYMXpFf3zRVmP38yfl+89Mvv0HS/5aMljWlfaPwlphp4IKqfnv7+VN1u/3pl58/NTmMNWAmb00Z/zOa/8yuNz6/s+Bj1eff74X8D2mUZm2KfEQ68muW/6/ytxdEN+PA+X6/ekV+zJfhgyKDEu9M7yb4IWcqKOsPdvzp6TcIEBCsysa+PYZZ/l//hciBXWZV5taIZmdNjUAH10ECBuH3flAh+0dSf9PWS0l6SZxvSHCHQAgRZhPXyKKEYILAfBg8PmiQuci3/2Pf4PyL/YDz0R353h7I92bfwehtQNi3G25/e0H2PuSblYEXpGaM7CaqCgEWovfA8RYbVZN8uQxMwQ00Byl2s+UAOFUTg78h3/4tl7cbwZe8G9T4mkK/QACH1GqQ5FlplkHcIeaAU1ZXgy8QXSGWlFkcW6YdIcOvJn8ZbHP0QfqwmA0rGbgCu6kBLDA2lNwN4qGklKDK4gvExcGOVRTEMeIEEPJhRetueA5t/ToQ+/btm2VW/tf0DsQkci911Qgu+BAY+fIlL4EbB55ff02B7WfIp19/+4T8D/Kvdt2IDzxUWBFuBoPBHCMrbaMgMDObe3EcwgLCzs1zv/5298QgXQoLD8ynAFbD22ZI7XsYDBrc3fPuG6jzICIoH5x+bzek9aFdkKCG1oI5Xj1/TQcSGVxatkEF3o1433w3/buz73wGn1QPG0I/fVTnWwQOzhyq6QuydJEPS0F1oV/rwaN+Bgu1A4ZSDFK7u3cEHy5MsxqpYN5UbveMNBVUdaD8zSpvBR4kEJzM+hsiz1RY57IY/hoMdGMPd2dpMDj+Ea3325BI+QnG2PSdxAuiDM0FkpulmfulWYHbOte8R8Stnbjvh8RNJAUtMhR0MPjoltG3yLvXdORR1JFHVb8b41bXka8NgeEU8v97pKFHGkw2WSx2wmKyF3hEUPa70z2+hwZzMPe9J4Xdys0+t2T93sG8g917GfiaxgGMibL7232lewvp+5o7tEJnOBC7djf6A7iUN7pBDQNziLSyHJLJ/Jq+1xtohyHJqgE6IX5EAxplHwyHp++S+hAkhuvvvce7daDmMJuQvLHiwEZcAJxb4tV+OaT1IyBglIIhxWEe2v7vtEIgdehQSB+BQgTQw7Am3UynwPQcnHLz8sfyYOjooBROY0NpYf6CF+Q4BA9MiQqxAGzLhjXQCp9upJAEQBtDET8sXPlmfhdmaPofApqDLzIYQuBHDzwewtQYChv4IeIgVXOIpK9pO4S4A653z37I+fAVFDYZYvC26ffufuiK/FgY/zbkPpTxe+2Bc8rQU/xgHFgwyqR6j7ioguiSgEcAwUi4tQ8v9w7g3mJ8yPL6h0nn818bhm41/fB7z70ifl3n1etodK+772X3xc6SEYyRIAfVowR/eSTWl0dx/DKY88sNFn5H+G6nV+SvCfc7Eo+ofkXwF+wFGx5JkPEQto8PtMXsy/T0hRqefk134LuTH5EwwCqEeqv7qG7vS2CJ80rgDYvv1a4aimQL6/INZG/V6iMQHmkCMTz1BiSrsh/Sd9BpcOvdax/FAD5KhzLjDC2lB4ZpKx7Er8DTa9rE8fMThCPwH0xZA97DUIXGGGYzmDawQ6sDcLv66NaGi3+YcYeEgkjgZK9DXsHaCjvrZ+SjSX5G3seW2yCYNnBu+3lo0AeWcCn887H2Y4C2wBOcE+suHwS/z2JDX/jo1/8oxJBOUGII/9Ugy3t+Dhz/QAR+8TxQ/pHI5vbFjB8gUdXmUJFhI/BI7QrK6cAG7nkoLDDlYBZBcGzghj+ygXxKUDSwB3AGdb/b77ta2V2X325mqO8D7a9P72AxfL83JPewgRv+865xsOl7tX8bKJvD/ltvdzPxrSN+g+oFQ1X/4ZE3tChv9zB8eoVQA56fBkOWAWzz+9v8/nQXB+rxvZeGFCBofKmGLmUEswhSgr1DPugQQcD7gcFwO3Bu64cvr3/SgP+L7H+1aJIgacx2GNtyOcdmHWA7Fk5aHIY7LMsStGWNGcYlLNxiXcscczjcYbpjjCJsAmehFIMnE/MhxQgffADl/zD0X58Knu4EYLkgaAZSYCnTdWnAAgZzGGI8JhmGtshBMAsAioO3TIIFFHBd1qEximHgNpPACc5xGQe3Bxnf29K7VG/vI8C7V+4o8AaBMwkGmQnTtDmbxSlnzJqMDUjMIm2AE9AkJMDoMelyHGToPH1sfXhmcNxd8SFoYUcK+8HLwOfXh6eHQGQouFKkquXk/pmNUNxkCNba+RZaMuBEb5dlQ+uZMsaJBs2TA6xyVbswlSjU5tmhrASlWwm4Yu+8zeLglIuNz48nKbtSG0fu5cNOizcEZ6BraTbFnMJO9mqK5pi0OBg7ZlrrdHE67rnS2CXOOpWbwjxW8bzUzwHV4PjSoGgTuFcLdJ1urYPEjP0ZveewU2UL4a7xD2QTJ6szxTX+sTUTkzwWyTXLiatwsjt8rWq4UIwcxcmdU+fMLse4SI6LEBRkEep+poN9o5cZj8/OAWldDintSMXhYgXrsatKpNAk+EEypHO3TLZnjemOVbSYMlpWzQmj4xZ4FpvnwlC59Y6utTI9JruD6166XaP2ko5RyyZJ4vOEKXbr0XZl+nqeZBImkyEGwooDajqnRqoRU5zgO+4l7VFDuwIq8pPOO89m44hY42p5rlTT1C0ziK5HuT7MVUfZRKXZ8a5vh23h4KUE3E1GSKnmt/65Mnm523YMSHs85fyJtZ/Oz6S9D7StOnNMfIXXczNOC9+ayM5WYU0zVmacE+H7ECQNRR8nNFeauos5+MFaC8HxyOETxl+Amkh8mZ1v19E4djwCbGfzdNf5SnHanYNVo/fxieU8f+sH8+mRmkx5uzGT67JAx6uJmgczy6lrv9Dw9oLTCSWqsZnrkkTFMZNaWJYf5sBcjCOek3eyZraGQxfKpjJO8ZoDq8JEz8ohZRRyYuKOzZRaq8eCfST57NQJcZcqgrIxtIYMfcm5XGmK4leKEdnpOMJL2tlGPKo15pRA0WQJzoqEhSvr0vnRrFIaRZO8KqkscnMxg1w/r1HuUknXnMGuUxNbc9ScY3eJFZDSLKOpII83UsEsj1puBPJ6tF9v0Gs7uyYcHqSHQ12HmHplcPzUV8fC7Cp6sw+XaKLGvX20jqvRZGloMUtFq4yJlCwJk0myWiZ5205cK9/s9uqVwMPyMJoAdSq71zX8r5touyajzKXcsThBR27HMjp63YhFUxcWfq1BxFH4UuFWSW1SJriuiZW4pkvlqCmBUy13tbHovS5OhbwwRofEQcUta2r0Wdp2eQ7i1ZI6C3gqTQNaErBQWlnraeymi0Y7youlAKZYrJ1CdTUV1Csglv7Sq7wFVmd0soStkX4grHQ6XYkCa2/s+eokGqOE52UlvohHTWpxIUEVf93tKt5YpJlkLK9zervK5J5U6gJbNVHK85vRYrRhAnsbkrsRYQud5083NnvRNHTUuyqPHk6NdKDd8DSfS8a1jXB/X6/3JQdHOmxsaZf9aXoSVnqcsz5OGvpKPZvz1hjvd4xetzq3wXRwVCfhuEIj+RDFymg3idstuq5dT3W78W4RUia5vnjbranNd04IAGjano0ZC0RiN5avJFni+eq4qrBjKWxOPKdwqO5fdBNCClYmTNgph4hm8W5dLqVsF6xDejxP5xMsLawtY3eCiZr4aF6hjDE9SiLZBhq5VpjFFfXWnLffNAVesSoIw4ZVq9zvkxnuK5Z3PXFW4F7xuKraLblfu9rZOMnYpt/v9vNK8VtNo+lZExiYV1Hs9DKpK7ptnb7h6Y7N9QglzJpKktwVvEZ2WRRbH/i0z1qZIaQkDNUTD9TrHovGQWDsi/1lq8Y8TaNj5jjaZJWdKxxfbcfMUjatWZVJeBKl5+WWZ7C4vaa4Ra+96WnedmQYVtN8XcoHDz2zDBt4KWobVKNexhtquhSl2TktyZShF4a807NsLgWnZFV0hNx7VhfG/LR1z/pmvMt6bkFGhT6l5eklXB4mE7/bkX7GCStLt1tHOAprSpitJit5gy8F3TzPD8eg4E8LG2PzdjERCuXckf2kjk9U2S9nTaWg9Nlqo8Cy82MFMzW3QRuNZKegmcg/xKqmmHuJZmyD7GkqWy2z/NTrkXrsARpq4dZEbfNwLnGROk2NyJmkJ2PEZa2Oku5BbtpKpWdCYdBXNJFjdZRShTqiT04VRjx2cJiLtFJagp0qkxUotu00BEZVztbyfHmZh3kZEKc+bTDezEQO62N7UlAZSlMoKvpMkKOqKQPGsgNqdojasU+tZME+QIc6suit+RWlTcMmW413qpnI5oY5VdRxhRK5ly/dhqspW+tc6kisKyGN6DjOo+NCSNVurW9G0iK3zKaYiIU4kXQZl+Kd0MxcdHPRemknySRtVExE2Xm/vzhcnAfMaT1OqkTebs4sN1sIPL9NdDk6aax4BG0cJ326dFV5VG91Lmclb+nMp/PNERNdnXXCzjywzJUitPN0bTda7l/kc2BoI9gxJadsJBzC43SbhVsSm8cd5SWUzukXarNYkxyzbtBAnthKyrZ9f5mtfAsQuarUMPulxTllVmdN40GB1nvyMAtP2nk/KyxxkZvjWpYxTTTJK6i1sO1ULpnI5jYay0e+OuoLvl8WeSr1l4CmrHyH2t2mX2e5LohLsuBnsNk/K5ZPLb3yHNfpGsOUahHsZc23sz7mMMtklM0knRPLmPIOfpZl8eUskqFryd1Ux3xPC6h2rgZatmP8Ixam0fqiz4+JUB66DWMayan0eLUNr9K1COYdwTX6LO+4ZpzTBZFkRx42v57uiktfdx1G3c2EXequzj45suvLNl8xoh4z0ZnbZxA65Xh5seMDfgpS31vqrGvHp5AZFYsKO0f9anFcsSfl5J8Z6riM5n3mLCpxHuvSYuLps9leqmXbGrmaOs40rKUx5aLBQf7Q7PakXdddGBkbcI1ndHoBzPgg7Nl4X1R2fGaUepRaJCZc1UXp91M+XYo774jm1Llnl+16BUFzK5VTzEabvcWcybxr5ztVPKA43vR2I/BONsW66ewiSuzRnx/kbDLrJkSySNuxLBT0MWjVw66R/SsfZ7TYnep0jrqH+ZKOeb1VZtNysZhqjbE8MDtp5NVeaOua1vT+QWa582a2TsCYPcWl3tCHiaFI18ww856WqAWPK0RsBrpropOWPe13MKvoTaGZhXXZmGBBtFVyvfTTuofoLEzUclbNl9vOFLYMSyujw0IGcZAwJ3CVlG7KBWDW5iNqt+cJKp0viITeCO7VwHmSrStKz7cVpk+WKV0Hu+RaGQu/mB98Ph8JqTgilKgUikKxE+7gX86YRtHzZc5PlHZhOdcql7UiRgOdDrbNXDnmuQ07Z2ydtfhKwq6F7hLmWk/G0sLwndmSDctj6O5GRrycFPN9FsvBjLJbr+o4Bpvu9uJl55A4E0vG6ljRDmxn6iZRmaJausLJuuL4omnnErqwLnMNY7W6wY6GTxPxhJMK/1RLNByaXIEoOmqfLQXbIfdqxBfnTo/Xms0QsP6set/ZzITtUrgSRGngR1IizNk+h9hlLS8zUpoK+QKGcRhX5Ggb2Y7LH1pMAYdQUli9WQstNHPeo9u0VWe1aTVi3mwE1Fgl6yWTld5qvnEE87rTW67T0qu0P3Ptoslm9Bm2xJ1UkZLqHMo9uqXXvN4vaKPn7f7qtN5kfwiooiAtZdvOU7Rwu6MXzVwfbQ1r30lCwjST65WBs8k54TBjGc6868rUinRZF95lqmss5Ue62MhnwtmKxEw5GIQ/n6fNTrRXNN0w5mFVzBaJeI21zjxKvQd0ncQWzmS8PdXNQT9Ep7PTbVy6PfOtPHZnkhgV24sS6R3e7jB8FIXz2QosuLCDmE5u6s6b7i1+slxMuhNsLNr9KTos+6Df8jS/CWi5sbYRazDc7KzhEM3n+uScXWj9kncztkxtdbs6zqKZGkvzaSXKPLUVLluzSGc4K/KHacNygR9Xk1RdCwkbbvKFaTAa7cGg4DzPEClguZt6z6x288khkIqx2mR9ZoekDxdF/GoV9JI697oE9kkSyxgxJ5FuiDlNN27wzd5D+e7EdmfRoeU5WfE9enF8N21pmaU4Y9o6rMlNr2F+WLZEjvl7ydnA7iYpl5aywEjC4fhtsIKtqzltamYyhiOK5/T6OdUEXcwX1sJIW3+SeyMJ8FwWLbcysym4nBg5jaeOt5My2nkHhUk8HifYCFuhtEYcj2sVa0bKwrObJmy8U89NezFd40RMmXIPOqupt6x1ctOtzfYBzbG4c+4xgBrlOKbHo9bj1hVM49Id9fxI3M+I+OLo6NwYo17MrsfY2grGfn7ySStfqysWs3GhgalSnmKb446jzBwts0iMR3F2lGxhFopWFMjuyfU07UrswZovNt2Z1TFX3MgW3q4Ih1151rZODdjMAd7v6xNtWnD0gL3iiaOv8Tjo19hWpi6ZiIWzGm9royUmIKUMNFO5dCy2ZHQ48OG86NGRh4p9VVYws0YJt3dU7litZxlzoZeAYGfXViaOHrpgCqkOcW7NZxZ7bDZs7cTFiCHH6Ty4SusgcqudMlG0fDICcAR1eNJIxxf3sFMC3GQPfJdKlx0zKcOq3+A1u+ZIIm5SEo4ILChmYAOdUYbsJXb1dh+dNm4z3vTmjAVzHEja0re0zR7s6MVKhGjJzEgxpQ6o4G037GLOoAF1rPGdAqycoZqKOUzchd3pV3pOTE0cnySjwFv1k4g6A2HvKxeBsN3NhIPwamDhOlP2aOmPUTJnTrJo7zrW6Dw1XxUSKTJqv4mnuwlYEttMX8kFVrfnk7qZ+mq61emScw+zBcuDancZccWmqrNtJbhi6S1qArDrXjBqOjXs8UmSLbtPqhG7r5Px3ClKF2QyW+rWbhQYiquMnStZM82OoMcdZbDelvK7sZj0LdslrRNet3g9m1xYpl3srvZu41rhNaeyUCwlyXREiHKmyFemUjFO6zCku206/KJbM4dt8DxabEql2gWbMj3ZF73iqM1p6q2ldLzCxAtwXc1r1UyEEddrjLopluIUVUlfyFAmZ7Ywct0pWVtlMFcpzQcSH5Kl6PSdkpCWiKIMzfaUoYrcfqKO+35kKnwfKEzE7S6RGNq1exkLwtgoFjFejtV8fIYjv0iuWZtoSFMdcVFzBEJ4WdOB0o9XxhpbJwF/mc1Fj0/9oqxLuRu1pLQ1R+aO6hpDVPmLVxAWt3Xz6Mp7h3jDXNQAoKN6ddhj5lEM7GNoA92yuyWJm6VoQyzNIqVgt/LqgJL6pKTOBIQCM1zgK2HqJn5SJoZH1kGRbC1MuS7cVa2SZd5kwBexi54tJqu5Q5L5CY6O7ExsOVvsjANNQRjnY3vjTYyNINE2M5Vkym4yXU1gh6bs5M5P+XoZTXfjNYEt4mmXjOtjRq/laqzYVABKzXGOzPTSc5OpFcoQLD01CCzeElc+qKmLN+65UYV36o5tLksrzCzvOGcMf8Y4Vyq3DiMi30UiHmpX7JLizblVZca0eaNVKgVz+9JiJ1ch3C+W2iTdM71X4kttjiXB3jbda905KirQobehnKvDjSdz/CJmKovvpbVdrtvJ5On56Xa0/fSK4xiNPz8NxxKPw4W/9G7a64P87UGK5Cjs+en/3YvT+0vM94PH21EDMJ3XG/fXvyDlL89PpR1Aie6vs6u48R4vS//h5fCXf/vGetje3Q/nhxPSa/1+MFOb3u2NepA6TVWX3VuVxc3tfTq0dFMNR8TV2+NY4+mmVpLXb++v0t+PI5w3mIzA/f5it87ecnOwc5AOx3/ACcwaPC69xzHE85PzOKZ+Ixn6DZT5oPHjJGx4nTwchT399n8BO0zvSwspAAA= -->
