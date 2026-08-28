---
name: "rar-cowork-cookbook-ppt-exec-monitor-regulatory-compliance"
description: "Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_regulatory_compliance", "rar_sha256": "e5a2fac8660854bc7be558be52d5d1d26137bab96c21a65a1317019252972494", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_regulatory_compliance_agent.py` and in the RCI capsule.

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

Monitor regulatory compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 e5a2fac8660854bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_regulatory_compliance_agent.py` first:

```bash
python3 ppt_exec_monitor_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_regulatory_compliance_agent.py   # or on stdin
python3 ppt_exec_monitor_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor regulatory compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_regulatory_compliance',
    "version": '2.0.0',
    "display_name": 'Monitor regulatory compliance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '42e1cdb2cacad103',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-regulatory-compliance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-monitor-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMonitorRegulatoryCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorRegulatoryCompliance'
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
    print(PptExecMonitorRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZfaSLrmX9HN+8Gui51oX9ynzxkhgQCBJNCCRLmOS/u+oA2kmvrvEwIy7brV3bdrznwY7MzUEvEuz7tGBL+92F0blfXLlxfVtwtIsLMsjvwasgsP4sprWafgT5k64Adyy6KtY6dry7p5+fTi+Y1bx1UblwWYLviFX9ut34CpkH/z3a6Ne/9z7dveACnl1a+VMi5ayPPdFCoLKC+LGBCCaj/sMhtcDYB+XmWxXbg+1LR22zWfHo/81oeucRtBbmTXbXOXrbWzNC7Cz9WdaFECxq9AJv9mTxOaly8///LpJQbXL19+e3EzuwGPXpSqXQLJ9g/Wx3fO3DtjQCKzixCMrQaASwHuK78OyjoHjzw/gJ53Hxs/Cz5B//Vf6dWuw+anL18L6Pn5+jL9O3YF1EY+1JZ20/oe5NqV7cRZ3A6vEJtd7aEBmrddXQB1gLY10OX1MfM7pbKC/j69+/hg8hr67cevL2U14QxA//ryEwQA/PpSd9P160Sl+vjTazaB/fGn73Sazkl8t52IAalfvz3vn2TBwO9D4+DO9e+A6sO8jv/15Qflps9D7klPMPPlNQEW+PggXNVl7xcTjh9/+mdk3Qg4QBY37b9F9+cH4Qh4EdDpKfhPn+4g/wLNngq90/znbCtg1r+iCRj+xu4T9ATqn9G+4//fSGdxAULhDfF/SO4fTZj9Hfr5n+r2ryZ8goKvL7yfgZirbSfzv0C/fVOVJffzB+/7ww+//A5I/49k1LKr3TuFb7ldxIHftN++/fyhuT/+8MvPH7oK+Jpv59+6OvtHNP8Rrnc+f0DwOerjH+cC/nqRFuW1gN49HfqtrP6j/v0VMuws9r4/b75AP8bL9JlBkxJvTB8Q/BAzDZD1Bxx/evkdZIkCaNO599cgyv/zP6F97NZlUwYtpLpl10LAwG2c+5PwWhQ3EPg/xXbtA1ybGAD7HAf8f7LwJHEZQL/+L/eeQD+7zwQ6r6r225Qavz2T37fvye/b9+T36yukAeplHYdxYWfQkVWUr4Ud+iDRAc5V7Td+3YOc4gyt/xlko8/TBRQX0K//HoNvd1qv1fDrPZXGj0x15DZTlmq6zH+dND1FfvHUy31P6T6UlS6QKYhBkv0EEGjKrAdZbkKlSeMsg7y4BhBM6XyiDZD7MhH79ddfHbuJvhaPtIpBj9LRzMGAd3Ggz5+BckEWh1H7tfDdqIQ+/Pb7B+h/Q/9q1p34xEMBSf5pFyDhVpUlCMRZl4NhwGTAyCCJ3O3y2+9PiAEZULQgYMU4iP3HZOCnqe+94a2u2c8oQUKOD3AGGOdVWbcgV0Nx+wptAuhdXsB0ejVl86hspjJX+YXnF+4AqNpAnXckQa2CGuCMTTB8grrGv3P91antu4g5CHi7/RXacwqoHWUGfk1i3geBycCsAP53b3g8B0TqDw20eCPxCkmTZ0KVXdtVVNtPHoH9sAuoGW/TAXEbKvzr12Iqlf4E1T1MHvCEU0mP3adJP082nwoyyAle88Y7fJZ9D9Lula7+WjTPELDryRQuKAmAadjF3uR7f3u6VBOVXebd8QOSTpSeVvCeVrn74P5fNgnLty7jx/6Cn/qLrx0KIzj0/0FPMmnBCsJxKbDakoeWkna0HuhO3dRkhUcDBhoDCLjYI5K+NwtvqeYt434tshi4Sj387THybpPnmEcW62oA4ZE93ukDhwDoTnTv/jr5X11Pnm5/Ld5S+yfgAvc8BgAAwQ2cf/K5N4bT2zdJIxDB0/33Mn+3b+1N2gOfhKrOyYC/BL7vOTaAtI0mqN+sAZzXn+LvGsVu9AetIEAdYA3oT1aIAZwg/d+hk0qgJgi3oC7z78PjqXkCUnidC6QF7ar/Cp1A2Eyu04BYBR3QNAag8OFOCsp9gDEQ8R3hJrKrhzBTh/sU0J5sUebAYX60wPPld0e/yzKJD6jant0CLK9T+vX828Oy73I+bQWEzafQvE/6o7mfukI/1qC/fS3uMr5nfBDx2VS+fwAHApGWP7xuSlgNSDq5/3Qg4An3Sv36KLaPav4uy5c/tfUf/1rnfy+f+h8t9wWK2rZqvsznj5L3VvFeQazMgY/Eld9M1e/zFISfn2H2+XuYff4eZn+g/gDrC/TXJPwDiadrf4GQV/gVnl7tYteffPf5AYBwnxfWZ3x6+7UAq4J3Sz/dYUq52QDK7Xv9eRsCilAItJgGP+pRM5WxK6ic9wQMbPG1ePeGZ6yAhFGEU/Fsyh9i+F6IgW0fpnuvE+BV0QLe3tTChf60xMkm8Rv/5UvRZdmnl8LO/X93aTMVBOC0AJFpVQQCCLRFbezf795bpOnmj0u7e2iBnOCVX6YI+wRN7SzIg2+d6Sfoba1wX4IVHVgs/Tx1xRNLMBT8eR/7vm50/BewQmuHapL+sQCamrFnk/xnIabAAhK7/lTky/dInTj+iQi4CEO//jMR+X5hZ890ATL6lLvj9i3IGyCnBxqgTxCwHwg+EE8gTXZgwp/ZAD61f+lAbfQmdb/j912t8qHL73cY2scq8reXt7TxtMGzYwTDQXx+bqbqOAe+ChiC+4dXgXf/l73kkwpId6CLAWR8wkZBH0CTJEwTuONSjk8QNPiFeoSHeCiJYJRjOwzpoohNEjaCIRSMMCiBMhSKMzig9/DQiUceT5KhNqDnUgjuMZRNuj4GO5jrIyjiUZgPEwwW0LSPA5Dep4Ii6T3Vfag3Yfne1k6wPLX+7cUhcTByjTcb9vHh5oxhYyfKOUb2DEGUvRszaXsTjWoJ95lyiuuuTdnxWOGCiomrYbE+bxL7dBGvGCd4mcYfFrNYY8IC9ed7Hs6OcSXBjbvocO4wEPRwpued5+K2WOYJfKhM9bKtDavV9fV2hu5WsnOpOHpkD1Qw+MOtieqrQVYCIsz1egNTq+5oOst50HeecpSzyy495r2gxjpL1gdTaeewJJ+Qw9brXZ+wUIw/kniEbzdMLElCd6rNrCU3nCsYhDuYG6RWR03v1qHPH8ggcBq8H8/kuR8dpiCG0TUV2mlG48Kqp3R5WUcJcrmczk13kqW4qU7WucbCC4ddBOw6bHK4dLgdfF5pYus7CIOHsdlE3GLBHqVzVdmEPMbMXhyI284G8Ko3eSBYXyazXN3Dlm26cQ7nGi/X6andng+9sbZXmG4jN2Z1SdeKxJyrWY1WyE6v6gSp0ktDbOmb4EtoGu0pS9+kNFELxeksmHVkiEZ4SbMOKXbODk34q1Sgi5geglI9Zwdsq4+ongpztzmdWq+CbxIHr5Jw7oy7TXe0kVhKFeDQFnZWQZ3eHiT4wDOuf1p6zQblraC1HMNGcEI1tJYtVW3u6cLGEzH5gjaBnKRaGKtCd8PHEA4wl7+cVcqX9RlKF0Vx2IeSJgPWYLFTDytUxoIFpdTbYV8LBnrMyDka41wK4iNfCsaqNzeh0dSj6ogwem3cnSLObDmSr0Iu95TrnVI+pXTEMfbkqdP7W3Yk6dW+W56TirsWMx3fcsIaGcXV6VQx/JaaY4ppFCIqXYIjLTV9c2vGPiaWxh5Wl/VG9Y3z6azXlRToW6nDVdsLC+M8oxpJ8INtNgvC6zyRzcZS8DCwZJ3KD6moz+n1LYmdoFcSZtk0CSBIIHTAnjf7HjWrrMubrDKPDcyptKSLXLS4WS2a4uhlZ++tgY/1IJFKi+bThc5FJgvqsKEyhnpEhkuwt5QVzG2IRNDz7OqxRHPJguuZ1SxhMLaqtEktNWi89Cge+crZUJdYttqLmRmaSON7IXW1FqGGBNhhJvRFccquPJWmm7ObYrGxJQgxdenCauZrYbsklWE7Rr5KIEawaJclRaQz3m0iRUZ6spxfBZyvRMLn1EiJ4fiKUbxxu1A72mXj0L41OgqLUaV6/C3CKe14Fex2SS7OUT+vBI3oxHw/943geL55SmysQWgbl+5KVOHBjbNxYczW8KrDinx2dPz0nMl9n1xcdXex6/G6z0+hSa821crotaEfUdzS5pwhcCAQwpTtKjfh/RjzpXpzkqN1Jvk5au8Qi3MXUW4LKKwopY3X0sm9IONq5I5bCq5nN+M0EjFTy/1OT7tU7fPzcNimF7uzwxg7zT36lKA31XJ1urmiOKuvKUbjuqZtCp7zNtlsECk+bwqWhmHrJOuGwnfInpIU8RyrSw8t8sOFl/zkNtdHL4YvMDFLNRUu4oPdSUxXsV1Ih8RBKvTFce2H1JrR3OUsVkl75WOULLPMIO/4LUbbXUTT1cateazDrTIVr3nfUgv1MGsW5LLZDtjQEFyiuZqAuwu0EslxZZlZEqGYJaTmFr3VwJb+8pAz6nnIMbpfJ7NtbXmGmMRtu1UMI2sIPKTLTcVxIduSIToQRqAnDHs68Y4rczGbRqoVS2eDQy9RXrsG1utF6a7YDSMPm0uk8lqJGie0Wppifr7iyVU0BGHrEdZB2LVOzUW+7HOIF8IX7eQdy7DtN5aU9I7rw83OOJAbBCmwEZ7L2JyYtWOkXU5wK5mRhi2zdWnPddK0qfUSX4KUyHDj4UYx5UbKvJESqMNyeaQ7PaE1fgfD7nnEkhm9X5pKxtPVJVqZTj8WzjJizwO3VvNo4yKamUcLm8tNlUiRyMtlYt4fTgWnY7fFlbPVOOyTEDYCbYHPiuSGazfbuhHSsJTk+FafuQNcbdbyFueAly5vV6rmAls7xXlyQw75er+QknNFFqs5PIixtRZVmz5vTBSZr1b7eFtsZTpf2bGZbZtNKBXMLCiulW7eVroqNjK+GNaJ02aNSLS8aWWXJVXH5xTZ+cSW2S1jNsMdgtnqDZftBq8aFy5ajm14EpKTECFy7SPm3PYUvFvi+qjXPEz4qIUSjn2KsE4VOGO9N0VU3ApyO/b5rtl2uL/ackWwiuZxc2BNc0zHE4JrCO7vZ1cT2VVHPo/mB32RDbmGw0KUy0nESlusudgomguHnSqpTC8gq57T9RzZZbiX5/zsgDPnNNuUrulmukNjC44s2Qw0AqyR1hs+4dX9EItUsrZ15eSuHLpqqKBYoGxtXKrNatZqZtXkmVUrhzk9WuT1aq10jLZkdw2fO0Tswk0SawJ7JjXnIJeOjwswcrzazdEa8ga2Z8d5Pe4lKSpShJFCIRfN2kRbp0OyGdmYaZoYcMLh5dY0Yj32RgYpJXandR5Sp56N0TsMjfapdFNHKopID67k42F9M6IaY5tVuklESVkFPNqL+K1EInmM1h5gtTPqzGpi9cgpZSp7YnzabxeiMtNW7QCSaU0ehsNNt/ltNZ+jK6a7uJIolaJ85G5kEq4WV1/zGb48q2dk5xn7EMe1Eb6ODAiN0Flsmqtv7HcN31zlvjkvaeG2HyvFb6Vb15inmmT0vsL8Ubyay8HTqBNKSSM+JvvZZukcix3V1YvUKvnjmnV4PkHRzOVmK/y0BpYWTCtqNlZC7MyaphSbx236dmHMkrvspbMG1gUnmF2XsrE5IAkXbwoj23UL3LsiPA2zZq8jW5Io+6O+Hvu1UJ3LvtWpg7VfJJxHo/3WKdGy1LSltyfYeWVTkbJz5Wyz9NVwh6ja6WoXlipG6s1PDwPVbudLWfaBz6H4QhWcSKrYeUZos3FRCGklbyRkdMYo2ZgMG3akKNy0iKePO09R9sZ2dwbdnphVPOntlEMYpKOh3Q6wt90O552hWVlvY/Fxf9MScUxRGjkKgkmupILgBh1txXrw6xV/Oe78QjbEahWcYMJ2Mi4zNyfcRmm4F2Yaeubm8GW5cc1TT57h2b7fIfVyNQrOep20u+pCdoYz5gLiyd5WmW2SLQ+aPtjzxiqP+2XMY1sbNlKM6RbZIpiBfgPXjvvET2gn1mLdAoVmr1wTd8uGWkdaZBhcSt5Q07ayT6Vy4ItAXqT41lAkIkAPYLWT751e54JEZ+QjMh5FIc7P58ZfSbvDkLO7hdHKyxmLGOkiXNqjKjXGLW1wdaWjJ6aaLS8Gd65AjyhpY8HWjps3mK9gzpEP9XJcUrvA5Urk2J4FVrwJAiqPDjqGlRdbQmbxF//sogJZM/3JmF9FerlB1vDQVllZwwM+gG4pHAkYX6n8qvEFJTrV2f6yd1qu25+jwbGZmF4kyiDsZ75DrDhckYM6N1t1ZRAgWLmzHuaL9cxUFA70z0h/PlfSvL5sWyJCWgOuDstdh2kyaHsW1Iw2OeoUq2O78Ei/W1JcIvaIOIaRF5ZNCydDi5z1kr0ezxG8XoAperpxd8we48p6b4QnUXBWQ+lejC06RxorRFzTY7lLQuWnTihAlZZTkyhYeNxyC0+N5/wKKYW1Ru6XKd6UAb/HNVG92RiicoMZCUcjNAYkMKxzFymDB+umwxMkQvmLo4EsmMwCWXC9GCKzV7PkZo5sxl2r6+yyvtx63aVOW4mSnCgIaDdYFUvaz5i2b9EKk5d5netz1IB9TNQQZ9503s01rwRMZajNJw4Ksji5iw/b6mIGnexViFghcGPHTUkqWyU03ORyvVFVXbShUjTnrkMvynZ+s8jlsSPybN9oZCLdHLo9LxmLFa7O9bJtpIoWaHutdrDDhjm9Zsw+xtiemREDadf8mnSZU3Tdr7EjaNsdJh1myOqU91GpSZQ8m5GhcGOD4uBSsErGFOZZPOzPbIpOGGZ+vc7tmt1QbTBH5jOxyJjAJynK7Ot6cROP1EyHQe9jHHhYOer+sdo70rK5jA29EIml286uvXo4Wspsvi1N/rTki7WT5ns3VK67nYVt+9UCWxP7+YVcR0WODGQR7JnVVRpyqoIvpLK43jD2FHb+lVzJu4EhtDHe3TjVOg2rKGvXgb4hekdnaNnim5uBWmwvzsFqYsyQtXVWVpRrBWzL9N0s3BEDoWGnY7WTtFpdXscuIseeL9hrJYKyIYTdJmkIy0YVJkbWBN0Ny4Dx5mOIWBl1rAPruGOl05lldkHkejyKFeS6zTfdaDNeubCQlWIJSLanFKQNgsFqZ2USk/hV2TuMd7xlu57sVvvZbVweF0F8RkdUWXW30avzvbDrViCKt8yy1hok3mO1whjn8HT1WTbx9YJCt6iKoQYxNEXf7HkP5WhKzeWAS6w6Cg63iEJXGytnLqjV0BqFSOl6DPcr+5YzZU3xzVgTF7O44pKQyBvKW5Alf3G01ilote1Oi+PBt8jDhdkuLigznC1lu4j2h6shYvS81LeIMFpZ0eOD3GDluhFnI7ZNnD2DZei4cBKpJ8jBtEp8OMUjefDymS9ldSiXe9wxneM8wTZWz7gLrEW7I3pmZjhGhQc8unn8NaG5K9esD7O9ZGrhbXTREMd2pHijstO83/l2e6NKig1Dk3cszztIQ0cusf1sJmLbPO+oudPa4qr0iDazTslAIKxzc5VonbKlHHN9i7A7yqKS43KRbea3HXw5HQdUw2fKcXHbZhiiKaSPCg7peJzjbxb4EWVmGzHumBbkGfW6Gz2kmDkeCBJ6Rwa8v+MVbx7I1YEuMxdm2tO+9zR77tn7Xpcj2jR4CcPQ3uqoEaviBYF4PRzM8cDF8FiYU7Ml2hH+7EKv8Li+JtpyCeNioZZ1c6SZuSsvImOGJ8c27zu1mTFtQE6NI+1fs2A1zilHpEMrC3febbbeJYYS37oZ4uENGlIaE4qHcz2yh8ykAp3rI8xhWNbe1/Fpw2GXGhYa6ZDsDTJHyl0qM9TJ7demqxL1SucXoLmX1oyhlLQHOnl5faPTFeIsR2pJYSBCVvF15YoYh6IL2bxarVoGouO1dui041Lwz/KCB92IxXBcwWBWu8BOREV752PLoB5RerTi9nK47GKsAQtP5jhagUVIW6SX4nXnmsyq1mifcobF0uNdbujVVDSlfHeu7XqmX+RoFrn9WcIZZL5fEL22C316IXfbEvbS3aG8ppilHxpJweKO7fVMPKm+6J1rZuYGh6M3mmvXTSrmctUyBFuXGM0TQEXKSSuWZf/+8ull2pR+bi3/xUPlaZ/v/9l242Nn8O246b6t7NvelzuvL39VsF8+vdRuDMR6bK82WRc+tyH/2+bq53/vqGKiMTzObKcTslv7ticPnGD6BtJLXHhgKQ6kacqsu2/yfnpxumb6JkTz7bmZ/XJXMK+mnfE3haZd2/thwbe2/PY4WH6ZvqcwHfr4Xmy3/vM2fG45f3rxBmCt2G2+YSTxza+rSdnn0ce0Rzudfbz8/n8ASoi1lu4lAAA= -->
