---
name: "rar-cowork-cookbook-ppt-exec-use-the-knowledge-base-to-find-a-solution"
description: "Generates an executive-ready PowerPoint deck on use the knowledge base to find a solution status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "30e220fe410d79d167d4beadc485b70f82c2e487594e2ef604b05892ac1691d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-use-the-knowledge-base-to-find-a-solution:a431f56decad7ba02a5d58b70798b406f595bd768b983b058b6df7dc4251e698", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` is
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

Use the knowledge base to find a solution Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on use the knowledge base to find a solution status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-use-the-knowledge-base-to-find-a-solution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 30e220fe410d79d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` first:

```bash
python3 ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py   # or on stdin
python3 ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use the knowledge base to find a solution Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on use the knowledge base to find a solution status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-use-the-knowledge-base-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution',
    "version": '2.0.0',
    "display_name": 'Use the knowledge base to find a solution Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on use the knowledge base to find a solution status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-use-the-knowledge-base-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-use-the-knowledge-base-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9743482596a658d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-the-knowledge-base-to-find-a-solution'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-use-the-knowledge-base-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecUseTheKnowledgeBaseToFindASolution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecUseTheKnowledgeBaseToFindASolution'
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
    print(PptExecUseTheKnowledgeBaseToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
