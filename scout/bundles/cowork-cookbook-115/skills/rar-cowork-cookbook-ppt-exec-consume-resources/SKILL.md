---
name: "rar-cowork-cookbook-ppt-exec-consume-resources"
description: "Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_consume_resources", "rar_sha256": "df06a75c24277eb660e7f9b4f8280ba22f8a4f69891f723240da0e736ab5f563", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_consume_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-consume-resources:60eba46661400e82daa01553bb6a5251e97509991d3f4c6618e978921ff7d8e6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_consume_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_consume_resources_agent.py` is
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

Consume resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-consume-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_consume_resources_agent.py` and embedded as the fenced Python below (sha256 df06a75c24277eb6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_consume_resources_agent.py` first:

```bash
python3 ppt_exec_consume_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_consume_resources_agent.py   # or on stdin
python3 ppt_exec_consume_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-consume-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_consume_resources',
    "version": '2.0.0',
    "display_name": 'Consume resources Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-consume-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-consume-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea103b789df6d959',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-consume-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConsumeResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConsumeResources'
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
    print(PptExecConsumeResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
