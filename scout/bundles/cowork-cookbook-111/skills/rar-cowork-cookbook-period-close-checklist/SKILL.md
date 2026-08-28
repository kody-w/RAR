---
name: "rar-cowork-cookbook-period-close-checklist"
description: "Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/period_close_checklist", "rar_sha256": "c05be623a9f7a688bc6868900007691a0701dfc09f1afd7620a2fb03621bda9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/period_close_checklist`. The original RAPP
agent is preserved byte-for-byte in `period_close_checklist_agent.py` and in the RCI capsule.

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

Period Close Checklist Generator — Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/period-close-checklist
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `period_close_checklist_agent.py` and embedded as the fenced Python below (sha256 c05be623a9f7a688…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `period_close_checklist_agent.py` first:

```bash
python3 period_close_checklist_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 period_close_checklist_agent.py   # or on stdin
python3 period_close_checklist_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Period Close Checklist Generator — Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/period-close-checklist
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/period_close_checklist',
    "version": '2.0.0',
    "display_name": 'Period Close Checklist Generator',
    "description": "Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'period-close-checklist',
        "upstream_url": 'https://coworkcookbook.com/recipes/period-close-checklist',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3a2559184fc7b56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/period-close-checklist', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PeriodCloseChecklist(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PeriodCloseChecklist'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PeriodCloseChecklist().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
