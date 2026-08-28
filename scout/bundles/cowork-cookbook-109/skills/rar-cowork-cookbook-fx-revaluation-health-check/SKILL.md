---
name: "rar-cowork-cookbook-fx-revaluation-health-check"
description: "Reviews FX revaluation configuration and last-run status, and flags any monetary accounts that look misconfigured."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fx_revaluation_health_check", "rar_sha256": "074470bed1987d3bb38dd96076aef7c7cab53c60933d47df5772f95ca5cb657d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fx_revaluation_health_check_agent.py` and embedded as the fenced Python below (sha256 074470bed1987d3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fx_revaluation_health_check_agent.py` first:

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
    "version": '2.0.1',
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
