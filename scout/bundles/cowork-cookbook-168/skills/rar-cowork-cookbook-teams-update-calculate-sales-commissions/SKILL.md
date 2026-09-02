---
name: "rar-cowork-cookbook-teams-update-calculate-sales-commissions"
description: "Drafts a Teams channel post on calculate sales commissions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_calculate_sales_commissions", "rar_sha256": "94b74a63d58de4ebfb7ec3ef5bf5ef9771c2d93a2fbb846b8fee411db268afd9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_calculate_sales_commissions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-calculate-sales-commissions:759f6915d78170ebb98aa52dd30a0120d7069466b5a9497de91627067f2a4cf9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_calculate_sales_commissions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_calculate_sales_commissions_agent.py` is
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
