---
name: "rar-cowork-cookbook-ppt-exec-create-knowledge-base-articles"
description: "Generates an executive-ready PowerPoint deck on create knowledge base articles status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_knowledge_base_articles", "rar_sha256": "4c70c784753dd2e19eddc75812c046cbb60d83bf49e2e7c993f3afdc2f1698a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 4c70c784753dd2e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_knowledge_base_articles_agent.py` first:

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
    "version": '2.0.0',
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
