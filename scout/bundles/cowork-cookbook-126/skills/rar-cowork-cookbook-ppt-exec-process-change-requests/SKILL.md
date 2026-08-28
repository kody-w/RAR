---
name: "rar-cowork-cookbook-ppt-exec-process-change-requests"
description: "Generates an executive-ready PowerPoint deck on process change requests status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_change_requests", "rar_sha256": "dc7704e016eda6c6c1b52ce20fd89d72122b663ced8b1d4ea075c846f536010c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_process_change_requests`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_process_change_requests_agent.py` and in the RCI capsule.

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

Process change requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on process change requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-change-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 dc7704e016eda6c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_change_requests_agent.py` first:

```bash
python3 ppt_exec_process_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_process_change_requests_agent.py   # or on stdin
python3 ppt_exec_process_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on process change requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_process_change_requests',
    "version": '2.0.1',
    "display_name": 'Process change requests Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on process change requests status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-process-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-process-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bc71cd79cc75cd2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-requests'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-process-change-requests', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecProcessChangeRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProcessChangeRequests'
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
    print(PptExecProcessChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
