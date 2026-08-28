---
name: "rar-cowork-cookbook-adaptive-card-approve-budgets"
description: "Produces a reusable Adaptive Card JSON snapshot of approve budgets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_approve_budgets", "rar_sha256": "8728e39fd1bc49e97694abf9f54035a47b584aaf569decb7a0347f761ccde800", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 8728e39fd1bc49e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_approve_budgets_agent.py` first:

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
    "version": '2.0.0',
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
