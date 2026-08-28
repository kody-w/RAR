---
name: "rar-cowork-cookbook-ppt-exec-create-knowledge-base-articles"
description: "Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_knowledge_base_articles", "rar_sha256": "66283a5f09014fe95c1d546bb34f4377f27596aaecb46dec6abd15b4dd6fe90b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Create knowledge base articles Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 66283a5f09014fe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_knowledge_base_articles_agent.py` first:

```bash
python3 ppt_exec_create_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_knowledge_base_articles_agent.py   # or on stdin
python3 ppt_exec_create_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create knowledge base articles Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_knowledge_base_articles',
    "version": '2.0.1',
    "display_name": 'Create knowledge base articles Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-create-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '679a940a1c11f601',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/create-knowledge-base-articles'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-create-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecCreateKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateKnowledgeBaseArticles'
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
    print(PptExecCreateKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
