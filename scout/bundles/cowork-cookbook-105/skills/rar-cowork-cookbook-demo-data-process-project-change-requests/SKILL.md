---
name: "rar-cowork-cookbook-demo-data-process-project-change-requests"
description: "Generates and creates realistic demo records for process project change requests in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_project_change_requests", "rar_sha256": "abb88388acbeff36bd29f85b42aa013ae2170423b524d3c1ae705ae1995818ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_process_project_change_requests`. The original RAPP
agent is preserved byte-for-byte in `demo_data_process_project_change_requests_agent.py` and in the RCI capsule.

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

Process project change requests Demo Data Generator — Generates and creates realistic demo records for process project change requests in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-project-change-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 abb88388acbeff36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_process_project_change_requests_agent.py` first:

```bash
python3 demo_data_process_project_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_process_project_change_requests_agent.py   # or on stdin
python3 demo_data_process_project_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process project change requests Demo Data Generator — Generates and creates realistic demo records for process project change requests in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-project-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_process_project_change_requests',
    "version": '2.0.1',
    "display_name": 'Process project change requests Demo Data Generator',
    "description": 'Generates and creates realistic demo records for process project change requests in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-process-project-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-process-project-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '126e78977cd089ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/process-project-change-requests'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-process-project-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataProcessProjectChangeRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProcessProjectChangeRequests'
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
    print(DemoDataProcessProjectChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
