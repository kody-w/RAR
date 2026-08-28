---
name: "rar-cowork-cookbook-ppt-exec-use-the-knowledge-base-to-find-a-solution"
description: "Generates an executive-ready PowerPoint deck on use the knowledge base to find a solution status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "9e6c1806b93f3621d0ef03940dfeda2ff9efeecbec41412f099c56392e44ee1c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 9e6c1806b93f3621…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` first:

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
    "version": '2.0.1',
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
