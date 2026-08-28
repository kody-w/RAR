---
name: "rar-cowork-cookbook-demo-data-process-project-change-requests"
description: "Generates and creates realistic demo records for process project change requests in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_project_change_requests", "rar_sha256": "f3e1034392d9c3b36c3ccd1b35fbd584be763deb5a5d8bf8b8da6c32162687e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 f3e1034392d9c3b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_process_project_change_requests_agent.py` first:

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
    "version": '2.0.0',
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
