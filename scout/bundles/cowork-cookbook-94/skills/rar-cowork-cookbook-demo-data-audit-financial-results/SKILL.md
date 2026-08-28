---
name: "rar-cowork-cookbook-demo-data-audit-financial-results"
description: "Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_results", "rar_sha256": "cf3e04d010009694280b9047bd53a563c23e92c162531cc13c6828354dc8c986", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_results`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_results_agent.py` and in the RCI capsule.

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

Audit financial results Demo Data Generator — Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 cf3e04d010009694…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_results_agent.py` first:

```bash
python3 demo_data_audit_financial_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_results_agent.py   # or on stdin
python3 demo_data_audit_financial_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial results Demo Data Generator — Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_results',
    "version": '2.0.0',
    "display_name": 'Audit financial results Demo Data Generator',
    "description": 'Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-audit-financial-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31737e587fdb041a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-results'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAuditFinancialResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialResults'
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
    print(DemoDataAuditFinancialResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bOjRrLuv6J77g+2r7pb7KCemIgHWkBikwCxuSfa7CD2TYD8/L+/QlKftu/M3BlH3Ih3HO4jVFWZWV9mfplVnF/fnL6Ly+bt85saOMWCdbIsiYNm4RT+YlMOZZOCX2Xqgv8XXll0TeL2Xdm0bx/e/KD1mqTqkrIAy9mgCBqnC9rHUq8JHp/Bryxpu8Rb+EFegkevbPx2EZZAQ+8n3SJMCqfwEicDY22fde0iKRbOogVC3HJcdAEY7h7zu8ZJiqSIHvKrJCu7ReuB4SYp20/AnGB08ioL2rfPP//tw1sCPr99/vXNy5wWfPW2Beq3TufQs9b9N6XKUydYnTlFBKZVE0CjAM9V0AClOfjKD8LF6+nHNsjCD4v/+q90cJqo/enzl2Lx+vnyNv+n9MWii4NFVzptFwAYnMpxkyzppk8LOhucaUak65uinfcIwCyiT8+V3yWV1eKv89iPTyWfoqD78ctbWc3oAqi/vP20AGh8eWv6+fOnWUr140+fsnIImh9/+i6n7d1r4HWzMGD1p6+v55dYMPH71CR8aP0rkPp0qht8efvd5uafp93zPsHKt0/XMil+fAqumvI2u8kLfvzpn4n14sBL50j4t+T+/BQcB44P9vQy/KcPD5D/tli+NvQu85+rrYBb/8xOwPRv6j4sXkD9M9kP/P+b6CwpQNB/Q/wfivtHC5Z/Xfz8T/f2Py34sAi/gNDOkhuIDjcLPi9+/aqedpuff/C/f/nD334Dov+lGLXsG+8h4WvuFEkYtN3Xrz//0D6+/uFvP//QVyDWAif/2jfZP5L5j3B96PkDgq9ZP/5xLdB/KdKiHIrFe6Qvfi2r/2h++7TQAYf4379vPy9+ny/zz3Ixb+Kb0icEv8uZFtj6Oxx/evsNEEQBdtN7j2GQ5f/5nwsx8ZqyLcNuoXpl3y2Ag7skD2bjtTgBxNQ+crsJAK5tAoB9zQPxP3t4trgMF7/8H+9Bmx+9F22uZub76gPu+fqgvK/vlPf1RXm/fFpoQHDZJBEYyhYKfTp9KZwoAMwHlFZgWtDcAJ24Uxd8BET0cf4wE+Uv/1L214eYT9X0y4M3kyc/KZvDzE1gRvBp3p8RB8VrNx6oAsEYeD3QkJUeMCdMAKt+mPm5zG6A22Ys2jTJsoWfAEIH1WB6yAZ4fZ6F/fLLL67Txl+KJ5mii2eZaFdgwrs5i48fwb7CLIni7ksReHG5+OHX335Y/N/F/7TqIXzWcQKs/vIGsPCoytICZFefg2lzBQHk6/gPb/z62wtdIAYUqAXwXRImwXMxiM408L9BrXL0RwQnFm4AIAbw5lXZdHPBSbpPi0O4eLcXKJ2HZg6Py7YDpa0KCj8ovAlIdcB23pEs5iIFQrANpw+Lvg0eWn9x50oGTMxBmjvdLwtxcwIVo8zAP7OZj0lgcVkkAP73QHh+D4Q0P7QL5puITwtpjsdF5TROFTfOS0foPP0y19nXciDcWRTB8KWYa2MwQ/VIjic80Vy+5zL9cOnH2eeg3ueACfz2m+7oVeL9hfaob82Xon0FvtMEj+IOTJkWUZ/4czn4yyuk2rjsM/+BH7B0lvTygv/yyiMG6X/SD8yVezGX7sWrxZirX49AMLb4/9tzPIxmWWXH0tpuu9hJmmI9wZwbpRn0Z28Fqv9T2Jw43zuCb3zyjVa/FFkCIqOZ/vKc+XDBa86TqvoGIKbQykM+MAyAOct9hOccbk0zB7bzpfjG3x/Arh5kBTwEchnE+hxi3xTOo98sjUHCzs/fa/kLt3nnIAQXVe9mANEwCHzX8VJgVTOn2MsRIFaDOd2GOPHiP+xqAaSDkADyF8CIBGANOP4BnVSCbQJow6bMv09PZv8BK/zeA9aCTjT4tDBAlsyR0oLUBG3OPAeg8MND1CIPAMbAxHeE29ipnsbMzevLQGf2RZmD+Pi9B16D3+P6YctsPpDqzLT6pRhmovWD8enZdztfvgLG5nMmPhb90d2vvS5+X2j+8qV42PjO7SDBs7lG/w4cEH9N/ozomZ9awDF58AogEAmPcvzpWVGfJfvdls9/17H/+Oea+keNvPzRc58XcddV7efV6lnXvpW1T4AdViBGkipoHyXu44zXx0eGfXzPsI+vDPuD4CdOnxd/zrg/iHhF9ecF/An6BM1DQgISE4Dx+gFYbD4y1kdsHv1SKMF3J78iYSbXbAI19b3SfJsCyk3UBNE8+Vl52rlgDaBGPqgWuOFL8R4IrzQBTF5Ec5lsy9+l76PkArc+vfZeEcBQ0QHd/tyiRcF8eslm89vg7XPRZ9mHt8LJg3/j1DKzPghVAMZ81gFpAzqeLgkeT+/dz/zwx7PaI6EAE/jl5zmvPizmTvXD4r3p/LD4dgx4HKyKHpyDfp4b3lklmAp+vc99Pwi6wRs4d3VTNRv+PNvMfdar//17I+Z0AhZ7wVzJy/f8nDX+nRDwIYqC5u+FyI8PTvYiibZz5roMOP6V2i2w0wddzocFcB1IOZBFgBx7sODv1QA9TVD3oAD683a/4/d9W+VzL789YOieB8Rf376RxcsHr2YQTAdZ+bGdS+AKhClQCJ6fAQXG/nyb+BIA+A10KUCCF6IBhPkQDEHQmlhjCAW5awgjXR9HHZxAPQQN1ogHEwiOwp4Hox5BIRSKY75HeWuKAPKecfl1LvTJbBTiOGCMhDF/TTqEF6CQi3oBjMA+CXThazSkqAAD+LwvTQE5vnb63NkM43vHOiPy2vCvby6BgZkc1h7o589mtdYdAhgsxe6SJMKovlIUtK4mqO0Rj7OM4oLlyJmR2HSajFHRzlB37EREFvg6yQ4pyfL0CVLDNl2O6LbOBdujUsLgR+dII10aBVxFCj6Jb+VzsoGM3CfSsvVV8q6InZiJjWEY5t4iLyPWsG3FJbWXmfxUackaXq8cEqt4RA2SWrmsmGJlS5Uhx7uqUTvdaptLklyMSWsRSMjPQ3o8uBLBqzmLYbdM502jp0ZTEFAl5/Odtj2GDsLRkFygxFoWKCIoGooKk5VoNsm43lBm3SnscUr4ZDDcC1I5BKJ1imPg3OHcWkSJhJie7yfTj/hNvmZzCxcMAwt7KxNA8OebxL2oumHy8cWsRq/lsrpKW7PmY+3ER1GvQjDCsnDaVCGvx7JHHKC60Rx82o1T7Bu64wZX6OKeOldplhlxwSPIP+lcYBdavbNJ0zvbV6HSeQvPvLPqH1QpZXov18VdN9589xj0HkVXgiB4qXHZbbdjbxExlQXscTgxGWLYnSTB/RkmjytjEypeDfN77NbDzU6xcdjd8deTKdEhx5Fi1Ors4GpVvTVuZltsnPzE87otpSEpMcpJ7bREbLi7UV0wHoqviX1ocBYmGaKoa/ReyV3YYfiFO2yhe4+SQmMW46Yp3C7yb105Cs1xr+f2zV5nYmlfZayNELGWNuu1iMO+0YgwuzQTBodg/xhVxm550ENk0HOrvQ+QtxaXVj0Wq4Q4GmpvJrygae048tyFusaVhcdZdwjOS2vloxC8X/Y134+UlHaYFQhmbBX2naGVPmMQJUnhoy5Jsh3kropLoUrCuFZqd8/gat8xsY2ECTHBbqkDx54y47BaR5sTxfnXxA1vp+2aE8Vrgl9wuLmFOwhBsQpLyKHzdc42NDFL606vdQuSjcMJcbfWoaLH6w49rviTsdIwP21MUacqGTv6QdYdx+l4kw2TmYpYEq1Ncms5oz4Y2P44WHS/312kMLWV4LhDD/dyd9hLcJS01obYXGJ3n0mGjXkaMx7QwqvFQb6Rjmy4TnBw1jsbLLnZLMyVV2qGYSiCa6KlF/KYUve73rXXVMorZEnTOze9lDZc3la3pTBZsCrcjodiWAo3w14fdc+opxV3PojOxd1IjZjVci9hh9Ye3TNHw6lDN7S2gq4ShTJnPTRq/5ytPNU58cNG3vNmvrknRaODI1Leu+Tm6t6hTuxu/E5jURSBJyrRFfca6149hJPOuz7USISj93noQGm0h3WH8lmlw1tixKX8XGfL5mq2LFFQWxvuIbceLjt6jexXY23JN/6MF617JjwvVZZ8Gia232Xn6/6GQsdE56Ubf11qOu6dA1FFesSQlqtRwcdIZbybS0v2xAd+mvmIYQ1+lZ1SpTjsIf1YaLntEdOQbXewcHPGTQHxXqhvg8o+C9HV3VLhCBtOd5SWbq7cKzjuqmO94pa3jbVimv3dYm3fvmojl1w7AWna3TpvzY4l/KXQDL55Q2/qmgr7aMXg1Em+Mwy04jdHtmshYjueQ1a17IBI5aW6368xfZzQJrG351G3sISyBNhtSgGTt62GroaoPaRb9ihN8HZcra9VGnTqxdmQ1wsuFci9SLaqxmMHOhLkC6uGB4FPFY2Cc7Fhhh12pC/X8qroVnfVnKyfSO/KDTBJ77pK0eHmKqmRRbjWLj3j9dBzW5tRD8X1Lu3Fnc4f1jw5oGSR3Rh1D9/3xJ3ml/pIkDZi4aaN7nMszn0/dLuWPIHhlcz5w2XMa88Pb1x15EW1weDeL1pVi866qZUgp1YrMd0MLE5eO2TPYPX5PuLLpZ+bRNnfbtmUU9bpxEFlyHO4AvGHrkFH17tEdGEwnJpLJQUpuR7vD0Svq8fhapFmsrwSia0c9h2dEBu9OI10dtYPeE8cao8IT46yOTHsGpzBYUu47WWaPIYMDO2wksNN9rBdlvw1gnLYzolsv4bsju2CU9QcC9F23bUSGmqTbbM0Pajetib5aWc25RClPJ/T5Z1Ut1w/1l036IW2d0QkPnd2Y2SlRhTomVYPrbuxb/7RVtKAZFV/SNe52FvOQQwGlcKKEzpZtUfZpcBVuIjbYgxnRZnU8o6gWV2p9Sk2T/0SXvXkdc/IoRDLnW/L3Aa5Ce0lIZpjD5iyxWQ5kxU1QGK/VtWSPUZBzx+FHII1hS6udUiZfDepVLqmL2cIVvMe0uVM2SmRRtzyJiVj8n7JQsemrhdZghQV2rHqbdB2Gy6yTntxvTv2LWWYHZ7s+S3U77CJaHn4aidwt1FyM9Hpbb1JjGUeniT0plm2q7KKsb7S6pJ3NG6CncG+soxe7NxdC2nJuVpNdgI4FpLWMruWzz2rdRvEbwTCIgGlSZLX8cOJ6JoU32MJi5br3eHcB1QWcWdv6QX6yBBnbJfd6j1XrZS0YmhTUY2gpDhhv29owLlDsCcMh8attJB2HbINrDSps4Tnz6eYzg/LdqrsYcc2YyWaHoZg/crZVQcPonvCBpXCd9stWSENqUy0frLPtOdxhSmeMeds+Kox+nulh5AguJIhPi3XGUQeoA2vxWiybdTmVq+3njxBNS4Fyljd2lBreFzqq7V3X+dC6m/qtRv6jl6yxh7g3NzUxFlS+0j1L5HAMCYF+e0e9FEGs0qkc2ocbGJvEYk+rU53IhpZr1VH/sakgF6rbMxOvUWT8VhtjO5S19urkzBHy7/rDMzXexKGtV4yhExnT6aWXUq4wRjpEsaRiLm94d7P5V5EdtDIadYJVBz8sLSsvSCNOnO95Xati4Z3KD2EUQ5K05TnbUkPfaIFZe/5QiYVWlg10rCh+kCFMgobVgx0ue0do3YqWliKchvplHXl2UuTY5K7OaD3w+YQHFUISXP1Dh1OE5+baxZVMP9aj4iaH+9VNEoyVnfJRow0HPQNN7rxZOvImS5f3bRif7gwZ/+qIpZxBHCH7UZtdCJK7gk/wbpHImFYaVuQDrydYafqgg84ZfsYkTUlBFPKWR+9hlk6U8a03Epw5BA+HhXPv3acqRJGXSUKF0z2kq8KlGscTlwdIHkQ+pSs8Sm1Yok/WwWdQSgdeUfsdpZH0vfgLj5cvEFvKGUnxKHM9Ni5FgC6Z2l/nZIxq3LcvqHHhiURJhy9dagg+bSrtzpUpzvkpsKwoiZMoyu3YIcwaBqxwxBkpexGuzZD7KiRi8qESk6r49Pm0BW1fsFs2zX7bQepLlvakTQa+XI/JbijintBKRFrPLqUCymb4rKfKPYipkWt2ZDSLtl1QbXN8XxNQ5NHci9D92shs46ydqq0CD80JHlvCiy+NG5rMnWkiP3SInfanRVXPOANl8MYKMLEfi2wuOovSSTPmGMUFzFKmmKdbSjQmyp+zd78vuzYjBW4zUHoV4oMYeIRk1eY2MhJAqrNGg/kfUGHqr46smc484Q9e8TWgkeYE1MJlqXFEUYxVmp5d2gPAkuE6os4na+arDXT5PvXJanQsGnfz/S+3OSXVZrTuc/dSATULOsSMyJoqwjEN7YJNFWbiNhN9+WGTTQdOW3i3GHz4HLZI7At946csHG9HorrOSXb49jzct/d6g17VpgDpenULnNX+ugf70q17H2GPt9xoe+iICB0DDSQXLdsUDOGdMxYIk4R3i+6xaP5JN8n7B5UYZeh/TYhWB71+vZsCQFy2vrWJG7arPQJLECKXV1yKmitk/VgKCsmniSTL7y710nMen+FVzVk4CeTvdDKzsnty6CcEvmerCZ40KDzFhknjK8plBtcSHNh1D/QcU+fqJNp9sJ5S6ZN7bSbsLqunQMNTh1csxlvK59fGkTThdtz7iJ6B8M0XMVLn7n3jJALNx+OTgqOuzeSdMlVIlCxEVemEa5gbSUjWXcKCHs9mvAycd3NEk68OKCD25mNoX2YYMR+pd0Y1xsio4eWjEQkm7PVns6oWLfHfb+BDpNHjafzNdkO+XpwGe9yXQoHQvZxt6r0FkdRcYwEqwcgEOz17g1ODadJ6hEtmUkBVY2rWEiaVLnklr2iwZHhAApZcKFrJkA1dXleXSGLbFoxTw0RKTuX2YLIXELgxEMRZHOA4rQZoFiEkDJoybs9iKy6Hc2xFKoK8ZKjwy1h93pzzcBBl90KH8chzs5KKCkkLSrH3To4VZ23naDCvoXiKMUwQZrbOBFyeusmV/m+dk2UyoWwZvEAGw43d30mr1WPByOBTlNoHWuaPqFyg1P7Tbg59Bm2O0v3SJGxLDgWpZKsd/4EU8hJFXfc8bqlbkrHs8RBM3M86I8455y3GJ4duVN2tnhMcBjxFAygzwyTLBNOO9MLbYbCtozR2reNimAXw1/to1Vw2oId7qw+Wl8YRJCOQhhuUQnfiTvGci06GhSpv5+YodzJCcKW7Ylcx2xdI/jmtDzl5mBkm27kqLJr4faOhqZV7/tdThW2FCRNbg+GoGypBjG9KFhPqRZLXn9dbW4845KY1jidV0j3phoLMjpj8bRmL/ehW4mWPGKWs7zS68lDIswUMH4kE49A96uTYa1hiQZ9OtP2cn91cNPfNgXn62R619BA6IxqH9ecX4wmA/XKqSSDDSOyFM0LSYSO5jlYmv14iOipDYcjcbqXsHugQq7krHxyiapYyw1DIQk6DGhCO5x/u9w2QxgYpEvIBRkKy3yNkxlq3ljMjFbxcF8F5vZ6OREn6Hi7h3FNoD5KgNbpDIqs0hPkUjYPPW4QI4tKZLfcrkjBhIjdGS3CwUCorMCyg6GKt40knjUtql227sfwfsNTjN2bZCJxqmQGo05t0Sy8atBWW63brTla1ApN+gMhyQ6Lrbc63heIa3pGThnTBEHmIKnBOjiI4mW5XcajI3ocxDJQttmK960+4jHB+bla164n9ca9drU16bi9BtJegK3NIB3u/bi+F7VysoYld42WgpPf6D6wAptGNgyPqcUGQRjZHeyLbaLwsTvera3MHZUjc8UvXdxrXKVAR6TFg6NNyiI2BdLddzmXRskV4JWoJSszClsa4hBeU9fhaMWrfH/z3VQ2UVe+FByNMqILzk46CtqZC1rdYmFzEWABL6qO63p8OImE7W3vA0tMHpu0Y3Bh2Zxgkn1U4St4AO28eoS51PSc1SQkxAlz814e1MBH8lE2DTG4robtvjghDqemNE3/9a9vH97mK+fXxfG//154vsr7X7tRfF7+fXuF9Lg0Dhz/80PX5z9h098+vDVeAix63pu2WR+9Lhn/263px3/55mFePj1fts7vusbu2xV750Tz3wq9JYXft10zfW3LrH9c3H54c/t2/sOF9uvrgvrtsa28et52v7Yx38c+Lv+/duXX5yvht/nvCub3N4GfOF3weoxe98hg7QT8k3jtV5TAvwZNNW/09Spjvn2d32W8/fb/AOmIUgKUJQAA -->
