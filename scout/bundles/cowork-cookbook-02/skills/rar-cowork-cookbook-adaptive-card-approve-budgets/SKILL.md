---
name: "rar-cowork-cookbook-adaptive-card-approve-budgets"
description: "Produces a reusable Adaptive Card JSON snapshot of approve budgets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_approve_budgets", "rar_sha256": "4230dbd0ed9a7945dec12502b278070a9cda0696ef6afbc1f88d1e0d9b6c79a3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_approve_budgets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_approve_budgets_agent.py` and in the RCI capsule.

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

Approve budgets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of approve budgets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-approve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 4230dbd0ed9a7945…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_approve_budgets_agent.py` first:

```bash
python3 adaptive_card_approve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_approve_budgets_agent.py   # or on stdin
python3 adaptive_card_approve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Approve budgets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of approve budgets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-approve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_approve_budgets',
    "version": '2.0.1',
    "display_name": 'Approve budgets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of approve budgets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-approve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-approve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db1e0e6dc0e12218',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/approve-budgets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-approve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardApproveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardApproveBudgets'
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
    print(AdaptiveCardApproveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
