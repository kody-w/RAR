---
name: "rar-cowork-cookbook-adaptive-card-report-an-injury-or-illness"
description: "Produces a reusable Adaptive Card JSON snapshot of report an injury or illness status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_an_injury_or_illness", "rar_sha256": "a21b01ffceb13a2197f99807ba6a7c96f2ddec6ffe8ed0b97f9c85326d13b106", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_report_an_injury_or_illness`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_report_an_injury_or_illness_agent.py` and in the RCI capsule.

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
