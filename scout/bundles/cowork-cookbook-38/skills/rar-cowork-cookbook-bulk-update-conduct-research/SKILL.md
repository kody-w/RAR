---
name: "rar-cowork-cookbook-bulk-update-conduct-research"
description: "Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_research", "rar_sha256": "f51a61f182eddae0a7fb0818173625a5514c85bbcfd77f1e9e599c5bcca2c460", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_conduct_research_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-conduct-research:2e6dbbe801ba9e1bc32af848b7207fe89961a150bbada87b6ea8b2446106c444", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_conduct_research`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_conduct_research_agent.py` is
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

Conduct research Bulk Field Update — Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_research_agent.py` and embedded as the fenced Python below (sha256 f51a61f182eddae0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_research_agent.py` first:

```bash
python3 bulk_update_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_research_agent.py   # or on stdin
python3 bulk_update_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Bulk Field Update — Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_research',
    "version": '2.0.0',
    "display_name": 'Conduct research Bulk Field Update',
    "description": 'Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd251af21f42fcb53',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConductResearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductResearch'
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
    print(BulkUpdateConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
