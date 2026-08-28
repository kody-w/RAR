---
name: "rar-cowork-cookbook-ppt-exec-use-the-knowledge-base-to-find-a-solution"
description: "Generates an executive-ready PowerPoint deck on use the knowledge base to find a solution status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "30e220fe410d79d167d4beadc485b70f82c2e487594e2ef604b05892ac1691d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` and in the RCI capsule.

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
