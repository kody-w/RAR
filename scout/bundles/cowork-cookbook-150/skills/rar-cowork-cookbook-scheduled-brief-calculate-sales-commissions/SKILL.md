---
name: "rar-cowork-cookbook-scheduled-brief-calculate-sales-commissions"
description: "Schedulable morning-brief email summarizing calculate sales commissions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_calculate_sales_commissions", "rar_sha256": "0ce8fee1baa0d19da6f9670f4918487cfa2fb62765d86a1669566fe2cdadc12b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_calculate_sales_commissions_agent.py` and embedded as the fenced Python below (sha256 0ce8fee1baa0d19d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_calculate_sales_commissions_agent.py` first:

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
    "version": '2.0.1',
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
