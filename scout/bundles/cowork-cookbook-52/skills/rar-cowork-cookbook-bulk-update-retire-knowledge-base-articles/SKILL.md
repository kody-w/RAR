---
name: "rar-cowork-cookbook-bulk-update-retire-knowledge-base-articles"
description: "Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_knowledge_base_articles", "rar_sha256": "9372c88b18d705f592bb5f71ad1acffce360903786eedc90d037c17d77e8b8f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_retire_knowledge_base_articles_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-retire-knowledge-base-articles:e8536cde3ffe6e708a523637c89fbe042405e17a6e204f91bcc9e2b4839b06a0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_retire_knowledge_base_articles`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_retire_knowledge_base_articles_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 9372c88b18d705f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_knowledge_base_articles_agent.py` first:

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
    "version": '2.0.0',
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
