---
name: "rar-cowork-cookbook-adaptive-card-report-an-injury-or-illness"
description: "Produces a reusable Adaptive Card JSON snapshot of report an injury or illness status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_an_injury_or_illness", "rar_sha256": "66d110c138baf97fca7a87d0d2b21c5ce7111bc770321830c71f6447f485efdb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_an_injury_or_illness_agent.py` and embedded as the fenced Python below (sha256 66d110c138baf97f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_an_injury_or_illness_agent.py` first:

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
    "version": '2.0.1',
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
