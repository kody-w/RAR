---
name: "rar-cowork-cookbook-period-close-checklist"
description: "Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/period_close_checklist", "rar_sha256": "c05be623a9f7a688bc6868900007691a0701dfc09f1afd7620a2fb03621bda9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "period_close_checklist_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/period-close-checklist:95d1de050ae3c179795b0fd64a7f5488d7f4763fd232c5be11d9ccd6c6277ce7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/period_close_checklist`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `period_close_checklist_agent.py` is
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
