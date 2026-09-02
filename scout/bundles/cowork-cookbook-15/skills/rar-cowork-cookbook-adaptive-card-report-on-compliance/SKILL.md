---
name: "rar-cowork-cookbook-adaptive-card-report-on-compliance"
description: "Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_on_compliance", "rar_sha256": "5b0b5f4666f684c0daaa78bd7558b295a3263fa7b739c49ed211769811f3372f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_report_on_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-report-on-compliance:ad17d3db8bc1deebbb6858e98665ac597700d683feb72ae64aa23f23e80fa6a6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_report_on_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_report_on_compliance_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 5b0b5f4666f684c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_on_compliance_agent.py` first:

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
    "version": '2.0.0',
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
