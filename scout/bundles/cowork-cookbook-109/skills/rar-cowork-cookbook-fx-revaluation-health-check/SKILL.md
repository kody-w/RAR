---
name: "rar-cowork-cookbook-fx-revaluation-health-check"
description: "Reviews FX revaluation configuration and last-run status, and flags any monetary accounts that look misconfigured."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fx_revaluation_health_check", "rar_sha256": "f07e99f99ba79a79dd9976eb3781050b351ec9276a018af83893e60084185355", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "fx_revaluation_health_check_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/fx-revaluation-health-check:bfee7d4bdd47f16ef204e1c0b4f8189a21b70003b5ab61b6e46647867f1abd31", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/fx_revaluation_health_check`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `fx_revaluation_health_check_agent.py` is
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

FX Revaluation Health Check — Reviews FX revaluation configuration and last-run status, and flags any monetary accounts that look misconfigured.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/fx-revaluation-health-check
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fx_revaluation_health_check_agent.py` and embedded as the fenced Python below (sha256 f07e99f99ba79a79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fx_revaluation_health_check_agent.py` first:

```bash
python3 fx_revaluation_health_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fx_revaluation_health_check_agent.py   # or on stdin
python3 fx_revaluation_health_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
FX Revaluation Health Check — Reviews FX revaluation configuration and last-run status, and flags any monetary accounts that look misconfigured.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/fx-revaluation-health-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/fx_revaluation_health_check',
    "version": '2.0.0',
    "display_name": 'FX Revaluation Health Check',
    "description": 'Reviews FX revaluation configuration and last-run status, and flags any monetary accounts that look misconfigured.',
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
        "upstream_slug": 'fx-revaluation-health-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/fx-revaluation-health-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d8e3f98dfee6332',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/fx-revaluation-health-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:check'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class FxRevaluationHealthCheck(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FxRevaluationHealthCheck'
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
    print(FxRevaluationHealthCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
