---
name: "rar-cowork-cookbook-adaptive-card-establish-banking-relationships"
description: "Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_banking_relationships", "rar_sha256": "32f7dc08492402fe68cd9a30c20a409bd3fb4d331de40a156d7137761a01c607", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_establish_banking_relationships`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_establish_banking_relationships_agent.py` and in the RCI capsule.

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

Establish banking relationships Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 32f7dc08492402fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_banking_relationships_agent.py` first:

```bash
python3 adaptive_card_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_banking_relationships_agent.py   # or on stdin
python3 adaptive_card_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_banking_relationships',
    "version": '2.0.1',
    "display_name": 'Establish banking relationships Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a32fcec0833829c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardEstablishBankingRelationships(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishBankingRelationships'
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
    print(AdaptiveCardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5ebSJPmX9HWfLB7sEsIhAC/p89ZhJAQSEgCXYB2HzeX5H6/Q2//900kVbk9/b4z27P7YWVXlRCZkRFPRDwRmej3F6OuvLR4+fKiACOZbIwo8j1QTIzEnrBpmxYh/JOGJvyZWGlSFb5ZV2lRvnx6sUFpFX5W+WkCpx+L1K4tUE6MSQHq0jAjMGFsA95uwIQ1CnsiKAdpUiZGVnppNUmdCSgrOMwvvYlpJKGfuHBmZIzySs/Pygm8XdXlxEmLCYhNYNvjED+Z2EbpmSkUWX6CNww/gn/hmDMw4vIVKgY6I84iUL58+eXXTy8+fP/y5fcXKzJK+NHLm1KjTtybBsuHAvKf14eSIiNx4ZSshxgl8DoDBdQmhh/ZwJk8rz6WIHI+Tf7938PWKNzypy9fk8nz9fVl/CfXyaTywKRKjbIC9sQyMsP0I7/qXydM1Bp9CQ2v6iIZwSshxIn7+pj5XVKaTX4e7318LPLqgurj15cUqnBX+OvLTyMEX1+Kenz/OkrJPv70GqUtKD7+9F1OWZsBsKpRGNT69dvz+ikWDvw+1Hfuq/4MpT5cbYKvL38ybnw99B7thDNfXoPUTz4+BGdF2oDESCzw8ad/JdbygBVC+Kv/I7m/PAR7wLChTU/Ff/p0B/nXCfI06F3mv142g279O5bA4W/LfZo8gfpXsu/4/wfRkZ/AvHhD/J+K+2cTkJ8nv/xL2/6zCZ8mzteXFYhgkBdjHn6Z/P5NOXLsLx/s7x9++PUPKPq/FKOkdWHdJXyLjcR3YM5++/bLh/L+8Ydff/lQZzDWYOZ9q4von8n8Z7je1/kBweeojz/OhetfkjBJ22TyHumT39PsfxR/vE6uRuTb3z8vv0z+nC/jC5mMRrwt+oDgTzlTQl3/hONPL39AskigNbV1vw2z/N/+bbL3rSItU6eaKFZaVxPo4MqPwaj82fPLCfw/5nYBIK6lP7LeYxyM/9HDo8aQ6n77n9adTD9bTzKdGk8a+mZBHvr2ToXfnlT47Qcq/O11coaLpIXv+okRTWTmePyaGC5IqlGBrAAlKBpILWZfgc+QlD6Pb0au/O1vrfPtLvI163+7FwD/wVsyux05q6wj8DraffNA8rTSgjUDdMCq4WpRakHVHB8y7yeIR5lGkPmrEaMy9KNoYvsFBCQt+rtsiOOXUdhvv/1mQj7/mjxIFp88iko5hQPe1Zl8/gxtdCLf9aqvCbC8dPLh9z8+TP7X5D+bdRc+rnGEzP/0EtTwXodg1tUxHAYdCF0OKeXupd//eCINxSSwCkKf+o4PHpNh1IbAfoNd4ZnPGLGYmADCDaGOs7So7gWqep1sncm7vnDR8dbI7V5aVhMbZCCxQWL1UKoBzXlHMoFlsYTOKJ3+06QuwX3V38zCuKsYw/Q3qt8me/YIK0kawV+jmvdBcHKa+BD+96B4fA6FFB/KyfJNxOtEGuN0khmFkXmF8VzDMR5+gRXkbToUbkwS0H5NxvoJRqjuYfKABw6CyFhPl34efQ67gxgyhF2+rX0fY4z17nyve8XXpHwmhFGMrrBggYCLurVvj2XiH8+Qgt1BHdl3/KCmo6SnF+ynV+4xyP0XvYPy6B1+7EC+1hg6m0/+f2lVRjuYzUbmNsyZW0046SxrD3zHTmv0w6M5g43CXfI9l743D2/U88bAX5PIh8FS9P94jLx75TnmwWp1AUGUGfkuH4YExHeUe4/YMQKLYox142vyRvWfIER3XoNOg+kNw3+MurcFx7tvmnrQ0PH6e9m/exhiCWMCRuUkqyF+1sQBwDYNK4RaFWPWPV0CwxeMOLeeb3k/WDWB0mGUQPkTqIQP8wiWgzt0UgrNhDA7RRp/H+6PzVT28LA9ga0seJ3cYOKMwVPCbIUd0TgGovDhLmoSA4gxVPEd4dIzsocyY/f7VNAYfZHGMJ7/7IHnze+hftdlVB9KhcxbQSzbkYdt0D08+67n01dQ2XhMzvukH939tHXy55r0j6/JXcd36oc5H90D+Ds4E5hrcXkn2ZGySkg7MXgGEIyEe+V+fRTfR3V/1+XLX1r+j39vV3Avp5cfPfdl4lVVVn6ZTh8l8K0CvkLCmMIY8TNQvlfDz2OV+vyebZ+f2fb5h2z7YZEHZl8mf0/RH0Q8I/zLZPaKvqLjrZ1vgTGEny+IC/t5qX2ej3e/JjL47vBnVIzcG/Ww/L4XorchsBq5BXDHwY/CVI71rIUl9M7E0CVfk/egeKYMJPrEHatomf4ple8VGbr44cH3ggFvJRVc2x47OxeMG6BoVL8EL1+SOoo+vSRGDP7mxmcsEDCEITDj1gmmE2yaKh/cr94bqPHix03gPdEgQ9jplzHfPk3GZvfT5L1v/TR520nc92lJDbdSv4w987gkHAr/vI9932Ga4AVu46o+G414bI/GVu3ZQv9ViTHNoMaQ4MtRl7e8HVf8ixD4xnVB8Vchh/sbI3qSB4RrLOF+9ZbyJdTThg0RpPVmTEWYXZA0azjhr8vAdQqQ17BW2qO53/H7blb6sOWPOwzVY4/5+8sbiTx98Own4XCYrZ/LsVpOYcjCBeH1I7jgvf+7TvMpDHIgbG6gNBxzSNtCqTmNzVHMAQvKsmkDRy0MNeYobdq4Y85tHJ/ZYI4aM2JhkzOcJBczA51ZC5SE8h7x+m3sD/xRQYA6AKdnmGXjC4wg5vSMxAzaNuakYdgoRZEo6diwTHyfCtW0n1Y/rBwhfW96R3Sexv/+Yi7mcCQ/L7fM48VO6auxwLdm1anIsLAZaaC3AjgrpV0dlAjY/bYoa29P8mVUCbnUSpVnh5yCqmKr3vZxKQcS4a86L8nPDmMuVbQRI5RINnPqrOySZVtUU2JVui7L6QnWMPMQL1ZaRji9OkhKtu62s1stkbsTuRfaCxZhYbNj+02zPCexXlY0gug3WoyuhnDZDoGHXT2P6W7H29FHaLDP8OEUIxftVqw7vjmg9aKMlFzH9pp/vsXCsE5EWtFvnBgnYL+OvATpiEJ1bx12kH3nmGSYczxXhONo0gFvCKTp+XCHA1YwUnwbWPv1Qg+UPMKuMaH7+5mCB0uNSOT9tIvLnZtXbOiZ2VmoD+eILNZmLWzb3p8uXT/trkqk2AnRm+V1iLVG8bNLrO8paSmASBDAvgp6VaRd0lPrWjYib0tVFytVbTlQedSujKHF9pmE7C4RtksOQHB5S1mep/1xiXvgpKrCrY3kZTEQTLo4adudbBD9yVnQmOWFKHngT6pIbOlwz4b+ysGIvj70kZvMWjLPLhiudTt2tp4D0ShTNJUtH8Hx1ar3C3W3NPQ652Z7ni6X5qZyN9PzBUhaAzZrFFWu15k2OzeEesMIboY0qO7j7nHVHRNZDCXr3EXLEqlTXqVmCmXr65I+HpeuLmzdql9nMg3Mfo3V+FI2AhTcbHweF12ZEnQkRZUZDEzQ52gsI4f9lMuHwE7FpEe2jViI8n5ZBGtc47tqva67y+0qHSMzFykZMVUGci9mzU+lML3WQsueblS04q1LnQb9sUuOM21XBZsY3TbEcceZHEk1Z0nGgrQ/efZyIN0KVslup6Mze1A7+JPNZmd8Vd+a5TEkpcJVnOHUYLrjus6WwXEq4y47c3GcroQFGIQVuZ/OazVVd7JHp6HbOxS5rhHtHGb6ZoU1ESpTjUKuY0/npShd7Hh9axTDJpUV8aLvxSZQlJU1VZmEda+G7fdyLxZMaTEZmTAsK13JZIkqoXVdzGWUWc2lee7XkRH4S2zAOk7ngAcXPe3WfpuCK78vVtlwW3Z73Kkts1VBUNDYSS+ul1vqc7N1mPpaH2r0frZt9hjXDEf/tlwh/HWHNEluy+susWXHzhOXvwTK4E0R/IioCEteSyoS4gSD1VwnB5sqTJ603MHNBSasUb8o2F3URXss8EupkLQFUxRLg8OP1OGA7Y/yeYeZaLu5qvryzF6NQNllW8LV5K3giMM0mdlUk3P21nL7i8wHU5LKUP/SqUG2vtStk+Miryc3zN6n09z0vW0sh5ZoBMPOuQYxmDGVSBmGktksRG8qtPHljHJbRjjuOV4DYDmjz3lJBEWs+gvfaZUBCfQaM5XSQygPTRT/KnbTnotDToouF4F0ChtdO7o2q1c56zYmU+nsZtOcCL1KwYHDTkMUzrqlxKlmn7ZFbFy4+hZm195Erzdtt97nZJ4cBBQybVJQtTisK5xMZuGlt1M8v0o04VwJR9ry1KEQBzFYmsCFoJ7N63Sbza4GXeAXdUldpB25dtxwsaLnV9eudlsdX2MXjqgyotDMjkFowYsG4TSsRdQ6yTZT5PV6LiHLa+CvelwKlMsSjwZQ5mC6X7Y+i6OyeMHi2Zxyuhnsy644bAU2ul8cbbcJt/pykyorBlBp5deOY7DzmW0u/ZrnW4bdZ2d9Q9rqLs/qPb7bL7tYyDn30KJpDKk9kl3bKLSDqQxY0FgoI3uWfktihTlpc6zyD8qco8KZt1a6wGA2pYjSRTk7gm4DOiIWCexcTKUG0rLV7Ki5tVpeRYX2F8igZML+2MJuQMUGVFgO4j4QSHVBHRxJW1WFd9SOcXfykmHNDzNLUASCkm6BPKPoKdf4HHVtWC8Nq6BxNlmpnFh8DhttEwuGKJY1LknEWRjGV8Y53RDUNy3nHB9qzjd2V3dHrefUTTc3pyyXhQzvlpdUQZPdJlIAo18Tb58e6EW4lsWrIqdIpp99Le7CGYWzU5Ltgy4R2rUlXhlMlz08HZwZZe+imXpyCM6+7LXVfB3g4ryrqe3tLNVBXKdVLSWnfJjNjt5W2653K9vJRN0LdbCqDhyLzXi7vLWU2Z7joSILjtXRJJjvG3NvWiU2pOZFC05nbklasWRuoqhzhqHO6hZw+vbiCAf6TGnKpdTqkywUWq2k/hrmXnbLqKk7HFCEuXjxKRJRRGJTfRWnW6KMQR+JJgzr0JoflzGaXw6ouBdVNjHTa+epYSPo4krZxJ3FobKDUVvlvPM2fWrEuSy67JJmZtszJjluBlqix/2r0JXNahE3qGiJsbbuVd3NI62QjOl80DtLoFhfQ0L+uFpo+IZQZU5uIb0dKIErGX+F4C6WljW7QdbTvXJq8TVuV/uAxZbTJLvVc5MT5MbJ5Gp6U8nZqRKU6rzdT2MatZVUWZihGVy0U10syZ2RLXYV5QlhV4s3VefwDD2F9GYeoz5bSsAVrjFTH7NLey2PSrVbsdUtdCuuxniZgUl+9XtRYL3zmsPQfq1tuWUxrRi+T3GtmhpctDVQBlvYUzqiMB6wc/4S8VvComR3I3FHAYs9dJ9bi6j2czEQ56zI7ZzpFA8rk5ZL0Veu+Y2pmUNQCRQRyj19UeHWQzcD3tQRx1AVHHSxme+1gz4TSbqmLT3zEs44uIJPmyIFNizXX7ds21pdk+H7yhMkb06tlejGmBf2ZMkyaIaQyC6wl+D8vpHzbDGIsK0G56MLNL33dmAvbl0Lu+Qc7+E77aAsYrmJbIkcrpafThNQr8UhcC7ZgjlZXnO2qU0pNKFWcOo5hHQtEqurkMzypUhaF0UjZ7GRKSLCcBIk1cu2Q1lN6hVRpRWzW5/hXjuLyiUaxfOVfD6u9cvUmi+6Hk3Wm8W8ElozGWLfV+U9sbcI+cgAWSeJwltqcakykW9szh7KznLpIASiftynC8oOBd+iqtWi4TS547uTgN+kctcZ3QoV5ZAsFyRqFwLrqmrZ80as+bho9JXQ4+phj1gyXrtFAgbSZs3LDj3RCe2DK3I5OHwClktd6lQtlGarTZtcODWGPRU2465T/rgN1mESXk2BwOoGpFap2ESOBbqNazmhx1PzJMyjuQEVrzieSwlfSrrY2/JLsENXeUSkzMwQ0FtHGla0hltgIhncgGN4FVcSyRZV/BCAxD/UWX5IuPm8vPJKdjovKNG4eVzIXn3fsDNqlQtiUwZcY54u3gm/bK9VlBpk6t228iHfzHY5uGS2ad6GDTnQZ4Wz+mpzSoBM+vqmEIJ9O0W4tp8rUmMdlIPdkoLtdIIYY9eLifYCSbsRJcj5qvbJTSbzFd5GuDQ7q+mltZcSLO+nPDoOSh5L+b64rPabK0aWyakFcNpmWDpHCWNa7bgpGiOvFFz1hixT2L4ozxa70Xs9XE91JKuStCaqud9HKjfFGG+GEhmSLL2jgwd6ZKD9DaS75oKEOqs3usqGusRduzoE1y43CE4ND6eV7O4LZq+x86xdpvNyt8rMteIl/R7ofQWMQsIaIdK82TKmT5LDy2xDCczO3FsDLpXsNeAZr3J9h5S7ObISIQHetgN/XGrKRuIBIuz082VYuMsaI/T9YPlmiV9RWeKXFEKa/EqhI9XZbfduztwW02BWHbJpsdAg2xgMYvALr7laJCakZGEGpldaTnGI5rRIHBy7KebTy1pVj2J1pBfW7nhrTgpF7mhrlTgYWXGbzdA0XlOWJze95IC07eHc5DqvOMah105IjPT1iRFdb74gSDOCHXpRE3kQG2XJseJ5G11PjUiysaw2/ZRxmCxHeFMoztscwXlGJW26Q6tyvbKYBgGHxsLgXkIwb1MtnCpZA3bMSbV459A22EwgU1ufg2WwH2BiST5X7ATK8kyMs8lEPdNGEAInbab4gp0uWHujarmDNc28nibODrs4zh5B0g1FHOtoFcqYX7lbzggVsFK1dCvoa1K7KHrLEA7NmhLHuYOGBBCYdLtdbnDYF9raMeW32zZruGW/Xu9p36rOphDZNYFtm45ZuXk52BjNuxAXXIJbDFb0hx5rwMUi/b2fxHjG9DnCNsZ+gUf+2lm5SwpcnePykDhuvSHyxQro0poCmsNVdFNDeiAMQsaBnDdKszpr86HxyKFZJUybbY+RVrv1LdGpQUg1Uq0PQ2YTgrPAKRVuCXa9iyGocGQkmWAQcsrO55umOBQAmfsmW/DkZTX44kbjZ5FIHoRKm/ZWhWRmhNqMTzezFc8XYDDnKEnALQMXHWBNbiz/tts22OGSa4f2ti7C45n1uHMJC8iWrAqk0LnT9lDs+J5Yw81/GkXAjPpFE4KMOQY766Aha6Xll8GpK8hyw3Q7cmtHg3ds9rHlHBgKLdZq60f+do2rlDZV3dY68JrsL/iFe+wkUcERwjKlcsW28y3a3jQBBOahLUv+4Le8aIgzkzYv/BXf4NtzM533By5Jr6WAbA7IBoOUvKtiBVdMMKBx0kmDqO2SUojVgbFasOrTc7YGjjwNjrJukotzkSOIglXYFPZ+C+4gHIv2JExpjcblVkpWp+N8bslxyXPXZKc5tAT3mtzlXDrmhtmnaxfDznbUjW1XvNiRYnFrDIzskXWP7m2wqHfLzqY9kQZq6A63kmFLErZTUxSodrE/i8wi4KmbFVGo6xIHL6ez2QpTnZt1rJw2kXLb2lbUaZPjPLZaUrsZ7Auo/U7IKlxDzmQ1U50WY1bObnW0p86hOlEpQyfk1urpNC+mBGqAhcS2SH8jG7wUerK267rj1WZhnaZIj9G4x0kE3q9L26fpcH7sNvyVj7dC2a4PkayWU6KYqtaZLWhvE6S3pnZzmiEZnMRtBuW4TrxUlHqc0lTRr309r5qTS9iWToQS3ifNtUZ5A69shZVAAYsHGAaXWfB20jIMqu9YS9jj8jKBW9RUXpi5E9Xnnizg9rFWg6CuCXKtrRhvNwAPGXjMPqScza/mC1EkMxYgZ5twCWapl950iaa3sPVaKsgbcQmiStkvmGGJ3RS3RWaknUfL/kaH5MWqDhe4p4X75jhqDuvGJWcEyUTwJpq1KikYqx0vRKCa1yd66KclbRyuuHO4qOet6cbraeSxhNQVgnl1em8p8os1RYdYQKowMmNbqpdEu6rm8UpH3EoMWNn2ZbZFaSBxLNVfal0mtlLczLUOcVgzXhzaXY3H/UaCzSMIpi1r8ewUzNmQYZiff3759DIeTz8Pmf97j5vHo77/ZyeOj8PBt8dQ9wNmYNhf7mt9+W/q9+unl8LyoXaP89Yyqt3ngeR/OG39/LeeZIyi+sez3fE5Wle9HdlXhjt+fenFT+y6rIr+W5lG9f3w99OLWZfj9yfKb89D7pe7uXE2npj/YN54lnt/oPCtSr89nkK/jF9xGJ8PAduHHfDz0n2eR396sXvoR98qv+EL4hsostHw5+MRaC/2ir7OXv743yn65uE1JgAA -->
