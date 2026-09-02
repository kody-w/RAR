---
name: "rar-cowork-cookbook-adaptive-card-correct-production-processes"
description: "Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_correct_production_processes", "rar_sha256": "4db0fbba4a41f4982a2503c386def931fb43a327bf56295eaeb19fdb5f5d5f5f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_correct_production_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-correct-production-processes:8a6c024645b389e7c124f8b92709380764e70f33641e92ca3837e2b20b999b14", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_correct_production_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_correct_production_processes_agent.py` is
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

Correct production processes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 4db0fbba4a41f498…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_correct_production_processes_agent.py` first:

```bash
python3 adaptive_card_correct_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_correct_production_processes_agent.py   # or on stdin
python3 adaptive_card_correct_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct production processes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_correct_production_processes',
    "version": '2.0.0',
    "display_name": 'Correct production processes Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-correct-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af24e4888ad5e13f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/correct-production-processes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-correct-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardCorrectProductionProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCorrectProductionProcesses'
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
    print(AdaptiveCardCorrectProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
