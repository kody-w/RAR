---
name: "rar-cowork-cookbook-adaptive-card-report-an-injury-or-illness"
description: "Produces a reusable Adaptive Card JSON snapshot of report an injury or illness status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_an_injury_or_illness", "rar_sha256": "a21b01ffceb13a2197f99807ba6a7c96f2ddec6ffe8ed0b97f9c85326d13b106", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_report_an_injury_or_illness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-report-an-injury-or-illness:f0f0ad90ebbea5765696221a5aecb302b4bf93fc006062044bf5d1fb92a058ff", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_report_an_injury_or_illness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_report_an_injury_or_illness_agent.py` is
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

Report an injury or illness Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of report an injury or illness status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-an-injury-or-illness
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_an_injury_or_illness_agent.py` and embedded as the fenced Python below (sha256 a21b01ffceb13a21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_an_injury_or_illness_agent.py` first:

```bash
python3 adaptive_card_report_an_injury_or_illness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_report_an_injury_or_illness_agent.py   # or on stdin
python3 adaptive_card_report_an_injury_or_illness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report an injury or illness Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of report an injury or illness status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-an-injury-or-illness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_report_an_injury_or_illness',
    "version": '2.0.0',
    "display_name": 'Report an injury or illness Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of report an injury or illness status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-report-an-injury-or-illness',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-report-an-injury-or-illness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40e4a9020c181714',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/report-an-injury-or-illness'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-report-an-injury-or-illness', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardReportAnInjuryOrIllness(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReportAnInjuryOrIllness'
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
    print(AdaptiveCardReportAnInjuryOrIllness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
