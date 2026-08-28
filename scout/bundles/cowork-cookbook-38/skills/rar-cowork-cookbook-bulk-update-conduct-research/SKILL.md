---
name: "rar-cowork-cookbook-bulk-update-conduct-research"
description: "Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_research", "rar_sha256": "f51a61f182eddae0a7fb0818173625a5514c85bbcfd77f1e9e599c5bcca2c460", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_research_agent.py` and in the RCI capsule.

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
