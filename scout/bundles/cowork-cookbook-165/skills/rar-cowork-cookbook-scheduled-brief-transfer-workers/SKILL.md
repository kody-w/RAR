---
name: "rar-cowork-cookbook-scheduled-brief-transfer-workers"
description: "Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_workers", "rar_sha256": "f27035799b60461791d64bead09324c38e1a7dcaaa36152ff6dbda033daa051a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_transfer_workers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_transfer_workers_agent.py` and in the RCI capsule.

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

Transfer workers Scheduled Email Brief — Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 f27035799b604617…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_workers_agent.py` first:

```bash
python3 scheduled_brief_transfer_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_transfer_workers_agent.py   # or on stdin
python3 scheduled_brief_transfer_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer workers Scheduled Email Brief — Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_transfer_workers',
    "version": '2.0.1',
    "display_name": 'Transfer workers Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-transfer-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f8c71f75a13d0a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/transfer-workers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-transfer-workers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefTransferWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTransferWorkers'
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
    print(ScheduledBriefTransferWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
