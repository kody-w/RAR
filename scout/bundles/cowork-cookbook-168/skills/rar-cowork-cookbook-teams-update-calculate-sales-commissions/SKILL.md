---
name: "rar-cowork-cookbook-teams-update-calculate-sales-commissions"
description: "Drafts a Teams channel post on calculate sales commissions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_calculate_sales_commissions", "rar_sha256": "94b74a63d58de4ebfb7ec3ef5bf5ef9771c2d93a2fbb846b8fee411db268afd9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_calculate_sales_commissions_agent.py` and embedded as the fenced Python below (sha256 94b74a63d58de4eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_calculate_sales_commissions_agent.py` first:

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
    "version": '2.0.0',
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
