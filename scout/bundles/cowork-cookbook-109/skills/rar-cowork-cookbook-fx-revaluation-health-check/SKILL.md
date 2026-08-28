---
name: "rar-cowork-cookbook-fx-revaluation-health-check"
description: "Reviews FX revaluation configuration and last-run status, and flags any monetary accounts that look misconfigured."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fx_revaluation_health_check", "rar_sha256": "f07e99f99ba79a79dd9976eb3781050b351ec9276a018af83893e60084185355", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/fx_revaluation_health_check`. The original RAPP
agent is preserved byte-for-byte in `fx_revaluation_health_check_agent.py` and in the RCI capsule.

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
