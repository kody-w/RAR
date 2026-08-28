---
name: "rar-cowork-cookbook-adaptive-card-report-on-compliance"
description: "Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_on_compliance", "rar_sha256": "1c821d2ab7e98b6b90d42b929eae8e709031e892df96200851626d9633a8823b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_report_on_compliance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_report_on_compliance_agent.py` and in the RCI capsule.

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

Report on compliance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 1c821d2ab7e98b6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_on_compliance_agent.py` first:

```bash
python3 adaptive_card_report_on_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_report_on_compliance_agent.py   # or on stdin
python3 adaptive_card_report_on_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on compliance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_report_on_compliance',
    "version": '2.0.1',
    "display_name": 'Report on compliance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-report-on-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74a15870069b7c8b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/report-on-compliance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-report-on-compliance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardReportOnCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReportOnCompliance'
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
    print(AdaptiveCardReportOnCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
