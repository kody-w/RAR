---
name: "rar-cowork-cookbook-demo-data-process-project-change-requests"
description: "Generates and creates realistic demo records for process project change requests in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_project_change_requests", "rar_sha256": "f3e1034392d9c3b36c3ccd1b35fbd584be763deb5a5d8bf8b8da6c32162687e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_process_project_change_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-process-project-change-requests:112fd67dc0f48a7423e0d6484fd701924dc0194d8aed73e02fcecf065057fbe2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_process_project_change_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_process_project_change_requests_agent.py` is
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
