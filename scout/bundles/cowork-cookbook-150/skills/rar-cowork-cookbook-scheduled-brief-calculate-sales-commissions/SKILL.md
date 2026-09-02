---
name: "rar-cowork-cookbook-scheduled-brief-calculate-sales-commissions"
description: "Schedulable morning-brief email summarizing calculate sales commissions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_calculate_sales_commissions", "rar_sha256": "6acb3e480cc6f56c01fd7c49738797ca62f3e5d82e1d4c57a3cd44c1277a029a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_calculate_sales_commissions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-calculate-sales-commissions:b8151a7d540c60fb4317d235b8b261315e64b0fd4e9ff62d17200115645a3488", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_calculate_sales_commissions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_calculate_sales_commissions_agent.py` is
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

Calculate sales commissions Scheduled Email Brief — Schedulable morning-brief email summarizing calculate sales commissions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-calculate-sales-commissions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_calculate_sales_commissions_agent.py` and embedded as the fenced Python below (sha256 6acb3e480cc6f56c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_calculate_sales_commissions_agent.py` first:

```bash
python3 scheduled_brief_calculate_sales_commissions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_calculate_sales_commissions_agent.py   # or on stdin
python3 scheduled_brief_calculate_sales_commissions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Calculate sales commissions Scheduled Email Brief — Schedulable morning-brief email summarizing calculate sales commissions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-calculate-sales-commissions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_calculate_sales_commissions',
    "version": '2.0.0',
    "display_name": 'Calculate sales commissions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing calculate sales commissions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-calculate-sales-commissions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-calculate-sales-commissions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6cc31e554946bde',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/calculate-sales-commissions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-calculate-sales-commissions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefCalculateSalesCommissions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCalculateSalesCommissions'
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
    print(ScheduledBriefCalculateSalesCommissions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
