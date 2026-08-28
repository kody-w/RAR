---
name: "rar-cowork-cookbook-scheduled-brief-calculate-sales-commissions"
description: "Schedulable morning-brief email summarizing calculate sales commissions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_calculate_sales_commissions", "rar_sha256": "6acb3e480cc6f56c01fd7c49738797ca62f3e5d82e1d4c57a3cd44c1277a029a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_calculate_sales_commissions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_calculate_sales_commissions_agent.py` and in the RCI capsule.

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
