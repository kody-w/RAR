---
name: "rar-cowork-cookbook-teams-update-pay-taxes"
description: "Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pay_taxes", "rar_sha256": "86f487af575ffdf83ee66b2438e272e5768a8825fb341de59d5789bf84d78b15", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_pay_taxes`. The original RAPP
agent is preserved byte-for-byte in `teams_update_pay_taxes_agent.py` and in the RCI capsule.

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

Pay taxes Teams Channel Update — Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 86f487af575ffdf8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pay_taxes_agent.py` first:

```bash
python3 teams_update_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pay_taxes_agent.py   # or on stdin
python3 teams_update_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Teams Channel Update — Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pay_taxes',
    "version": '2.0.0',
    "display_name": 'Pay taxes Teams Channel Update',
    "description": 'Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2eecc6126be717c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePayTaxes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePayTaxes'
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
    print(TeamsUpdatePayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
