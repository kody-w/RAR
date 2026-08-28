---
name: "rar-cowork-cookbook-teams-update-analyze-financial-statements"
description: "Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_financial_statements", "rar_sha256": "45614052fe1778c05a8735a74d3ccd617ca6e4c56cf7f102681be2c88b85022b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_financial_statements_agent.py` and in the RCI capsule.

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

Analyze financial statements Teams Channel Update — Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 45614052fe1778c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_financial_statements_agent.py` first:

```bash
python3 teams_update_analyze_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_financial_statements_agent.py   # or on stdin
python3 teams_update_analyze_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze financial statements Teams Channel Update — Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_financial_statements',
    "version": '2.0.0',
    "display_name": 'Analyze financial statements Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '60ca8f82f98e1b1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-financial-statements'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-analyze-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateAnalyzeFinancialStatements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeFinancialStatements'
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
    print(TeamsUpdateAnalyzeFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOjSJLuv8LL/aGrh6rkFIgaa7NFBwgdgAQIUFdbFUdwSNynUG//7y+QlFnd2zPzptee2aqOFBDh4f65++ceQf764rRNlFcvn1804GSI6CRJHIEKcTIfmed9Xl3gj/ziwn+Il2dNFbttk1f1y8cXH9ReFRdNnGdw+qJygqZGHEQHTlojXuRkGUiQIq8bJM+gPCcZbgAJ4szJvNhJkLpxGpCCDE4av7Y10sdNBAcicdaAyvGauAMI7zvF/cvcqXwkyCukbGPvgkBFnBC8QjXA1UmLBNQvn3/+5eNLDL+/fP71xUucGt56uWtjFD5ci3+oILxpoL0rAKUkThbC4cUA0cjgdQEquFgKb/kgQJ5XH2qQBB+Rv/3t0jtVWP/4+UuGPD9fXsY/hzZDmgggTe7UDfARzykcN07iZnhF+KR3hhqpQNNW2QhUDW3IwtfHzO+S8gL5aXz24bHIawiaD19ecqiCM0L95eVHBKLw5aVqx++vo5Tiw4+vSd6D6sOP3+XUrXsGXjMKg1q/fn1eP8XCgd+HxsF91Z+g1IdTXfDl5XfGjZ+H3qOdcObL6zmPsw8PwUWVd2DEFHz48Z+J9SLgXZK4bv4tuT8/BEfA8aFNT8V//HgH+RcEfRr0LvOfL1tAt/4VS+Dwt+U+Ik+g/pnsO/7/TXQSZ6B+R/wfivtHE9CfkJ//qW3/asJHJPjysgAJTJDKcRPwGfn1q6Yu5z//4H+/+cMvv0HR/08xWt5W3l3C19TJ4gDUzdevP/9Q32//8MvPP7QFjDWYTl/bKvlHMv8Rrvd1/oDgc9SHP86F6xvZJcv7DHmPdOTXvPg/1W+vyNFJYv/7/foz8vt8GT8oMhrxtugDgt/lTA11/R2OP778Bokig9a03v0xzPL/+A9kF3tVXudBg2he3jYIdHATp2BUXo/iGoF/x9yuAMS1jiGwz3Ew/kcPjxrnAfLtP707bX7ynrSJNSMFfW3vHPT1yYNf33nw63ce/PaK6HCBvIpD+DRBDryqfskgzWXNuHhRgRpUHaQVd2jAJ0hIn8YvkC6Rb//2Gl/v4l6L4dud4uMHXx3m0shVdZuA19FeMwLZ0zoPEjK4Aq+FKyW5B9UKYsi2HyEOdZ5AYm5GbOpLnCSIH1cQiLwa7rIhfp9HYd++fXOdOvqSPciVQh5lo8bggHd1kE+foH1BEodR8yUDXpQjP/z62w/IfyH/atZd+LiGCtn+6R2o4VpTZARmW/soL6OrIZXcvfPrb0+UoZgM1jnoyziIwWMyjNYL8N8g11b8J3LCIC6AUEOY0yKvGsjYSNy8IlKAvOsLFx0fjZwejeXOBwXIfJB5A5TqQHPekczyBqlhSNbB8BFpa3Bf9ZtbOXcVU5j2TvMN2c1VWEHyBP43qnkfBCfnWQzhfw+Ix30opPqhRmZvIl4ReYxPpHAqp4gq57lG4Dz8AivH23Qo3EEy0H/Jxpp5j457sjzggYMgMt7TpZ9Gn8P6n0Jm8Ou3te9jnLHO6fd6V33J6mciONXoCg8WBrho2Mb+WB7+/gypOsrbxL/jBzUdJT294D+9co9B/l91DI8mY/5sMh71HfnSkjhBI/87nchdZVE8LEVeXy6Qpawf7AeUY9s0Qv7otGAvcJ98T5vv/cEbu7yR7JcsiWFcVMPfHyPvDniOeRBXW0G8DvzhLh96H0I5yr0H5xhsVTWGtfMle2PzjxCSO3VBEGAmw0gfA+xtwfHpm6YRTNfx+ntlvzsTmg3dDwMQKVo3gcERAOC7zohBVI0J9nQAjFQwJlsfxV70B6sQKB0GBJQ/eiKGgEPGv0Mn59BMmFtBlaffh8djvwS18FsPagv7UvCKmDBHxjipYWLCpmccA1H44S4KSQHEGKr4jnAdOcVDmbGVfSrojL7I0zFmfueB58PvUX3XZVQfSnVghEEs+5FufXB9ePZdz6evoLLpmIf3SX9099NW5Pdl5+9fsruO7wwP0zsZK/bvwEFgAMIgHvl0ZKcaMkwKngEEI+FenF8f9fVRwN91+fyn/v3DX2vx7xXT+KPnPiNR0xT1Zwx7VLm3IvcKuQGDMRIXoH4UvE+PYvTpmW6f3tPt0/d0+8MCD7w+I39NyT+IeEb3Z4R4xV/x8dE29sAYvs8PxGT+aWZ/osenX7ID+O7sZ0SMFJsMsMK+15u3IbDohBUIx8GP+lOPZauHlfJOuNAdX7L3gHimy8g94Vgs6/x3aXwvvCPZPBz2Vhfgo6yBa/tj4/bY2ySj+jV4+Zy1SfLxJXNS8Bf2NGMNgKELQRl3RDCNYD/UxOB+9d4bjRd/3MndEwwyg59/HvPsIzL2sR+R95b0I/K2Sbhvv7IW7pJ+HtvhcUk4FP54H/u+TXTBC9ydNUMxGvDY+Yxd2LM7/rMSY3pBjT0w1vX8PV/HFf8kBH4JQ1D9WYhy/+IkT9KAgTdW6bh5S/Ua6unDnucjAl0IUxBmFSTLFk748zJwnQpAxoesO5r7Hb/vZuUPW367w9A8to+/vryRx9MHz1YRDodZ+qkeCyIGwxUuCK8fgQWf/c+byKcgyHuwd4GS6AlD0PiEDADBslMPnzhTlpo4LO1TnuczBOs5DKC9CeMFbEDgJDMlXEB606k7neAk6UJ5jzj9Opb/eFSOdBxv6rEE7XOsw3iAwl3KAwRJ+CwF8AlHBdMpoCFO71MvkDSfFj8sHOF872dHZJ6G//riMjQcuaJriX985hh3dFibdeXI5VgmCJ2Mo4vKStbbuqlrVskbdb2etaFm7y6Us7HFpNjkKUGehOWhOKV02K+Y5Yqaq3UKAJ5w5spOtQPYHmwFrz1rq2FrNFvV7UTjpUMJJretjW3YldF6vb7V5WhDpMUZpvOGo/PWXcXunLpZohW3w1aI1XOTEJhAE1K70xjuoEjJPN1VtiVFLLHerMi6qjKTiMrFHjjHTXrUGS3P9OPMndLGYJbH2DGqofEtqSiT7TbZF6ucUzKdQH31RnAeNrGzLUdP0XJlbK+nzWRpM7uwkkBTupACXCspG9+FBl0v1UJmonR6jJRufoyPpOoVuLUrBnQarreZmYrRUiKWyTEZ8mOFT4LaKguPMAczIQU6uQhX0ywEo+/JOvK2E7NZnxerRCubKFwOF+Ia+6nlTMwYJ4HvkOcjt8WLW+FFc63Ylzs9Hm7y7pA1/rWIlOtxXsrrA4Et9ngh3miqPazTjcNaSpJ12dLnPfaSUGA/WxiKy1z7FJBC32V9kpTWyd9JtOOkfZDkGan4kNRyg2K4ZO3lTDOszdS9pOLhit2kanmoRZJxQqISqG3fUstkDaaykZHytd5cTuzRMbXEXvRTncNTR/b366sge9leLlHYo7felASsqvTApXYL/BaTLNsZ2VW8Zdvi7KtRdaUivqoXa1adNpfFzieFSJTky75eSDgxvdQVkTrnYHvjp4zdLvscl47s7UrZZ48SUnQTZdfkJqLLqdcdbYlifHtfy2i1Wub7kO78/XBLVNtWKszl/KNXbdqyVtXTVhHX8WlqrVP7tsf1fN8kp8PhQlZ6RhVn5lqkRKy73ZJpG6ooyq3ONbFFK+pkm9Irjt6y5OoiTvA8TnRshtl0SrFcj2mdOBs4oyC3wWGW1x1hXoUmuhCSlZxwQioErzJKGMWipJrWws5b/nrmzbUOduR50TsGzMhkTfIdhteFqeyJCaHnym3KXY0+lfKKneHzmC/mujHv5T6Pi3x61tZXKZ2IvnTm12m9NBe8tdfSrV1XbgpWy97T5Am1Oe8WFTqck5zMzhLQjoOVwyBmtuaGWGWJu7ImCrEeImZ/OHVZ6Z6EdeUfak7KaEqstEWyQHELVfuz7+5cYYVSZ3zY9OkRWyeeVcc3sc8Nu3bnclUXlSIXjOQdr26/FYnlnq97F8MXsyl1MMwALZmIHRgxr4vlfnHV67APHEfWWNPK0b6aMQdfaqj5Sk9veDKgWCwcTueZj1p9djkyrofXCeNxBdcxeJIfJ4bjmVnEBYRRtrioTY83wShFJpvGNUM5a8LabPhQ3axoaidYgoTeTKH02/l+3SlxcPVa0sn1mGKZy2GTiAH05TpD21oRtMuVo4Z8d+sHWZE3mnxkndm21Y96eKlb8ibOm13hxdokEstix3g3yD+mEWmJIuBHNNHj7U5PLbOc7MTwtvKwINmaji/KitpIuDxjLgQVBVWdqvtg7102t+2Z17tQdtFiZ6MXjyoFj2Kdbc+VirWIqelQRZxX9F7GUU3fX6ST5B4JIs17tJ7RBK9nXcppR9Gj00k/cUttVpn5LnE4GhtIa+8OXmanXXCd2ZG8Y3dassIDOXPxTarj+HpykzDZSslMU1F+IYnxfjY3SGa/u6Fn76x5oWxJQ76cLy5ZFJ+iJmw2ZOH2DUsznqz08+3mdDwcItg68IRBDuuZnlVz2jNxQYpTdYcbN+fSiZgyj1EFEBNvb1z8GvNqWrwluHklm1b1zdNwAstTllnUjYUhfwXNLboxvCWRNzdDg+PFxlFIaKdKyWhjhuOOkJ2tG33pTUAFttf2tSXMhYC6dJcetWC4tZh61Ckaq2WjS9Z7G16rsn/VlrNGkvyNQ17TwRtqOu+NAbWUMr055xawvVyvE4FO6fm2nrdliHkgWKQcN7Xw/uBdaudS0CmxXKNxsT3NTdgjusaanicbbzmELFHuZ8tCFyRhntuL1kmTU8I0AoZfN3G9WmsOq/lh7uXJVTv1fnbKQDzxzoZgHwxiIvJcf5KH9VFu5zgTV0eSUAR27eDcAkzO9GxTLpQ+P5NG6p1WwTHNdjPsdFZTO1bFWlB3wjm8pTjph4w1QUMrxTWsYeGua6px7bWQCvlcz1fxpr0wm83xeGuY5ZVC0YKU2sk+N7Oty+5U5hjx8YAWboMe7KE6B6XJuSC/wKIbHqPjBD9MSlgr1iA8k5sTm+OJq88Wq1LMFarRSmo27/VekPUN2DnYgZZOOBvavuURxm3aaS4/nLSuYSIqjWCctT0hLjG+R+cpXWTSaY1nDjNVRXO9v4alH7oaWrWFId6EapCFXbekeXO6WspUie5cAqT0YF7WdpHJwRKTeNqXQX695ANqN0nsOGJYi0F6iNywo1zH3DkG3DcFB6FjPevCsJfUcJV6Jtz2bHNsLtr5wJohHjbS5EZaPWcN6JVol1TC72IGK3DtwsH9EhVreTk93OQT4+6zM30NlcWtvuiLvig9ic3X06uDGZVhGM7htjissZNgkpGk8vPBbqiIo+pOWx2WG41XlCzA7BWJr694ZV7yyXKb1TnfKIuhKmpf3mRKsbXbOB9avo4WFIbdOInEDHOx10Cj7X1ydmwqKuNjJTueGLxtTXog0yA7FnhL4aA+gbM8AC3F3M46OfmaEM/SnOpA3K7C/Uxmbf5kKyBjm1s50fU+oPelcekXrjGslmZnTZjAcHd4Eh8lm5d9/dSojFd5uLgqlaO0J8rI2HvBsbS3Z8o1dkaZW511VGjCbo+GywXgqJ1B1y1ZXhH5W9ROTpaYacoaEuR1tS8hqnXgSZsEp439np3c5H2xuUXCIu0367ns9zHvGzUZEIvuUuyapo3MUNVqKgyGSaHurduZr/WknSaFXewGnsyZCXk4DKmXO5pixuh0aSSnjbakBUkPNW9L7evAuAiGaJmhv4gHMk6L2ylt5Tk+JJnEHbNGFFe0gJ2ZqMfZUwKtdeQrr1cn3E+FuJzmsA/RiXlr8aahkSh3VDiCYAtILSVMBPq0tiH1YiefZuRcPbUzLKbOa7OKz9KyNSWHbht6whlGs7qKIun7VUU66WZ5xDaZVAlda4jH1OUaPmMs4bBkYLNoJ+K6l5r9cbantauCs4Vazto6EuN001aDAcXSE5GNFvluoSpozbCV5nAsbNbD5YmoUywsQUXVrO/l0XZPeP5JtiojAYawi1xi79IzJfZP0qzeLUvHbeZyn5oprV4LTQObCKfzCxmeb4RU+l7d6BhvOkf1bMiaSJ/1YD6xvGYrzqNI3O5ss0UFextt5nPWnO1STSeKmpF0bOXcUDNZhvpNhVFCKXtXAOlQ75LNCr/2Hm5RfLHfHbeTeHMeyFnp6TvFdFyy6sUdJkH+91e5eglVuuOwDa35zMQkm/lhn0D6CKxd2cynp6Jz/XINSaXwyXi7tZaaKYcJWOdA5wWMn6Qn4UhVG7fwOdezCdnSjtRa7K+N18irNc2tvbLqZ2vLthdNSO8E90LvbxfzLIDp1c5P9VlMvcRKIGNkBBpHZX0TQ17d820d8O2iZlS407vwRl/M4yK8qlzNKKq4FhyRM05pFk9VQzzXg7BQaHmH5uttxwyBh7J5JVHDhXMO5zMzsftVdjwSRaBIfOicHMbRuZxh5jncv1Q6sec2thdS7t7b+s605+huQDcyqRwYriLdgBV0fFKVrWWKg3IbaAdtgvmRrRcxI+4oryV6WwekugD2cJzXSeEPE5HMlmVp6awjn/3ePAR8Plmxid5abZzyKHl1prpTaJeNKEgHyUlPBn5QY5WNYT9h6Ph+MZndpE05pbLe5RZ7uZ9JwqzV6hng2kk96LWDluV1zaQUUROL+IqD6ULEEhvSQAtvrRcn7JRSmT0zDXXKLM7e3LItwHYzcL4NrkpSFoXNLG7eLRZKg2HlCpWbrQs44jZddhUnrMkjs1myJjdTncjU8003vzKpschmukeEZsuhM4WJ4709Ve0q9Y3lglo4l+MO7Lte2uTYujOEfrWWsJhRz5mZMIzpwnzud/SG2lISqcxCjtqJbXPiy1WbqZMs8Ei4UdmJ1O7crJNkuvKMyaFLh8hb0ALryQ0xQ3MubBV6cOb2NY65dhmEU9Z1MMnCuul5srWZcGnciJlPYRKa0rMZviPN3bCC0X+9XNUDmp4Dr9LQW9oRHWaqCm7nczYXVXqd5FJV92BD9cFq718Y9DS48yohu5XOm7u9QgqmnzJk1008EzVOhEf3m87l9uy5UD3V5tyJtauXxJzP2Ow0JflIjTxrwOeSOBmkzNA6tSI3VxBycMdFWtreWK1nURDkpLAIllV1BWqwnC64cjb1+vqc9flO9YRGythur57X6q28CVkceMFpNqUXM7M+dXOdpI+mjwnnoMWCcH+IRTZUj+ExvDGAoAahB4fVjE81it8sVy5VwOQzeTUmxXyqsuzcPxrNsOymgWT1ZjLnrurUbBiiuVGBZcdCu0yn2UkG8Tlb29tVPiMttkgdlZ8Y6z5trQMWWhup47wZ1ZDtIT1xDK0TveTZTDsLt6i1X4nnMBDFc9XTdCbbijQoSgPQQOau1Y0wVz4V7nAhJJOVBVRPb88EXjUue7npFOgauIuPyhXYXq0ZXh/UnAXz2U6c8ptVJHT0Jmw4zI8Py1kiYZGOu9mBITUaVQ+z6zqhCF1llqY04eQ2OnRLHt+wgFOEEOVkEqOu/XbwiQyjfAVMJxcPNu18wHYZSigrhadKtye5K7pdVxznEcHWn+vOlY2MoXPkniMGufUpl1t1g9VhOynCSjTyG3rbkel+GtrAAHaYnnmDlI8+oaYBKlx3m4pcOkrioExZ0Ytug4kr2A9CSne6eMJxTeLtcWdKyMN8tT03ak22k8aHW9WkKbsovsgld7Dtgls1izMu0Wq+W+WbpWinZhffFrjCepFhkFPXazKDpFgSz6RM16dm2QsR5D//zGaqwYA+mqqrGWcSMhAWaEjfZlN+fuwjVeDyuUeF1zzOg9acpvIe7rgIPhODaE+akx1IFjogsm3vql5viWYP1Laqdguso4XNbpZ4jidylFKhh7lrbUtFwGq4eTm7YTlgp6HuvMV+ecX6YU0dColwvVRZq+v9+diRWoqjzCTbT/uCmCoqH+SRJAungavtUi+UXOMzazKdrbCDZBng4E8KbNXKOY2ytX5RUvbQJrfmCrltioZoc2i5OewjeZ7/6aeXjy/jMfXzsPmvv1kej/3+v50+Pg4K315D3Q+ageN/vq/1+X+g2y8fXyovhpo9zlzrpA2fB5P/7cT107/9FmMUMzxe347vz67N23F944TjbyW9xJnf1k01fK3zpL0f/n58cdt6/NWI+uvzkPvlbmZajCfmvzdrPM69v0v42uRfH++ZX8ZfXhhfCwE/fowYL8PncfTHF3+Arou9+ivFTL6Cqhhtfr4ZGQ9vx1cjL7/9X6uwzgH5JQAA -->
