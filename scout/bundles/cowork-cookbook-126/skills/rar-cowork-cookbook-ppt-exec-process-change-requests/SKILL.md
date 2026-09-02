---
name: "rar-cowork-cookbook-ppt-exec-process-change-requests"
description: "Generates an executive-ready PowerPoint deck on process change requests status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_change_requests", "rar_sha256": "b40e0067bec916ca1471015629e0e9092915debf0052cd2715436938f764b7dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_process_change_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-process-change-requests:d67bccf3615eb476eb71a97ee6132e0d7f1335110b9a2489fbd33b6613ee414a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_process_change_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_process_change_requests_agent.py` is
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
