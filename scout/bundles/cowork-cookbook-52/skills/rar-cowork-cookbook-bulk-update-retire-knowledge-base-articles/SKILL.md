---
name: "rar-cowork-cookbook-bulk-update-retire-knowledge-base-articles"
description: "Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_knowledge_base_articles", "rar_sha256": "0328fecd011624f784a0743174855242f8b85295d23cbc3024d2c054f1368acf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retire_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retire_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Retire knowledge base articles Bulk Field Update — Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 0328fecd011624f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_knowledge_base_articles_agent.py` first:

```bash
python3 bulk_update_retire_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retire_knowledge_base_articles_agent.py   # or on stdin
python3 bulk_update_retire_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire knowledge base articles Bulk Field Update — Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retire_knowledge_base_articles',
    "version": '2.0.1',
    "display_name": 'Retire knowledge base articles Bulk Field Update',
    "description": 'Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-retire-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cc920a1430606841',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/retire-knowledge-base-articles'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-retire-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateRetireKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetireKnowledgeBaseArticles'
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
    print(BulkUpdateRetireKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
