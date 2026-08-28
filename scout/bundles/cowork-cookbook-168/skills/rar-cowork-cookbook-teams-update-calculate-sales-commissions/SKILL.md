---
name: "rar-cowork-cookbook-teams-update-calculate-sales-commissions"
description: "Drafts a Teams channel post on calculate sales commissions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_calculate_sales_commissions", "rar_sha256": "f1165b5fd4c7d87878f3fb234f06b5e8b8889e2ab2f52196d8006cc15b0d8cf6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_calculate_sales_commissions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_calculate_sales_commissions_agent.py` and in the RCI capsule.

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

Calculate sales commissions Teams Channel Update — Drafts a Teams channel post on calculate sales commissions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-calculate-sales-commissions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_calculate_sales_commissions_agent.py` and embedded as the fenced Python below (sha256 f1165b5fd4c7d878…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_calculate_sales_commissions_agent.py` first:

```bash
python3 teams_update_calculate_sales_commissions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_calculate_sales_commissions_agent.py   # or on stdin
python3 teams_update_calculate_sales_commissions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Calculate sales commissions Teams Channel Update — Drafts a Teams channel post on calculate sales commissions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-calculate-sales-commissions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_calculate_sales_commissions',
    "version": '2.0.1',
    "display_name": 'Calculate sales commissions Teams Channel Update',
    "description": 'Drafts a Teams channel post on calculate sales commissions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-calculate-sales-commissions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-calculate-sales-commissions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f36ad046a59fa9e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/calculate-sales-commissions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-calculate-sales-commissions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateCalculateSalesCommissions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCalculateSalesCommissions'
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
    print(TeamsUpdateCalculateSalesCommissions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
