---
name: "rar-cowork-cookbook-adaptive-card-approve-budgets"
description: "Produces a reusable Adaptive Card JSON snapshot of approve budgets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_approve_budgets", "rar_sha256": "8728e39fd1bc49e97694abf9f54035a47b584aaf569decb7a0347f761ccde800", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_approve_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-approve-budgets:cb39b52a2186fd9b542dbc271f85abf990a4018ed5c993c5419ec17e78857135", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_approve_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_approve_budgets_agent.py` is
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
