---
name: "rar-cowork-cookbook-adaptive-card-control-project-scope"
description: "Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_control_project_scope", "rar_sha256": "5675620bca86cec6b3e9a37c7a610a9c5eec079b5e557cf074b995eaffebb84e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_control_project_scope_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-control-project-scope:72b40ee86f6c028028436ce4ef38c2acc5225a197e28e0f4c9c93a37ab0c9057", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_control_project_scope`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_control_project_scope_agent.py` is
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

Control project scope Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-control-project-scope
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 5675620bca86cec6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_control_project_scope_agent.py` first:

```bash
python3 adaptive_card_control_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_control_project_scope_agent.py   # or on stdin
python3 adaptive_card_control_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Control project scope Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-control-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_control_project_scope',
    "version": '2.0.0',
    "display_name": 'Control project scope Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-control-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-control-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57de7c0c0db0367c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/control-project-scope'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-control-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardControlProjectScope(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardControlProjectScope'
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
    print(AdaptiveCardControlProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
