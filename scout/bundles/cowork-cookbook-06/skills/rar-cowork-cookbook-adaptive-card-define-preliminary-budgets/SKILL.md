---
name: "rar-cowork-cookbook-adaptive-card-define-preliminary-budgets"
description: "Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_preliminary_budgets", "rar_sha256": "5ba0ebe3136855128ba8f298a1e98ea08781bd63db30a852e66c93eda1e4a7a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_preliminary_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-preliminary-budgets:e2613f9daebf6563ef67ce43cb8b1a1d7685df7c445c1949bb030e78a9583ab6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_preliminary_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_preliminary_budgets_agent.py` is
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
