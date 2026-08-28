---
name: "rar-cowork-cookbook-ppt-exec-process-change-requests"
description: "Generates an executive-ready PowerPoint deck on process change requests status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_change_requests", "rar_sha256": "b40e0067bec916ca1471015629e0e9092915debf0052cd2715436938f764b7dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 b40e0067bec916ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_change_requests_agent.py` first:

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
    "version": '2.0.0',
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
