---
name: "rar-cowork-cookbook-adaptive-card-define-preliminary-budgets"
description: "Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_preliminary_budgets", "rar_sha256": "5ba0ebe3136855128ba8f298a1e98ea08781bd63db30a852e66c93eda1e4a7a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_preliminary_budgets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_preliminary_budgets_agent.py` and in the RCI capsule.

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

Define preliminary budgets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 5ba0ebe313685512…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_preliminary_budgets_agent.py` first:

```bash
python3 adaptive_card_define_preliminary_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_preliminary_budgets_agent.py   # or on stdin
python3 adaptive_card_define_preliminary_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define preliminary budgets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_preliminary_budgets',
    "version": '2.0.0',
    "display_name": 'Define preliminary budgets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-define-preliminary-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46f6a44b76d4c226',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/define-preliminary-budgets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-define-preliminary-budgets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefinePreliminaryBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefinePreliminaryBudgets'
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
    print(AdaptiveCardDefinePreliminaryBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
