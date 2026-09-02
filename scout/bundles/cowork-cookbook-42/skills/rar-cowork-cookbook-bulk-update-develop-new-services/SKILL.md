---
name: "rar-cowork-cookbook-bulk-update-develop-new-services"
description: "Applies a bulk field update across develop new services records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_new_services", "rar_sha256": "d2996087d358825a392f703268320601e4c2733d18c777beba5eac77ad3e3ea7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_new_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-new-services:5c78d0017377a9b91ba85007b1a42efadc4e850113cd38aa9f7a884545216de9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_new_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_new_services_agent.py` is
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

Develop new services Bulk Field Update — Applies a bulk field update across develop new services records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-new-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 d2996087d358825a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_new_services_agent.py` first:

```bash
python3 bulk_update_develop_new_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_new_services_agent.py   # or on stdin
python3 bulk_update_develop_new_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new services Bulk Field Update — Applies a bulk field update across develop new services records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-new-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_new_services',
    "version": '2.0.0',
    "display_name": 'Develop new services Bulk Field Update',
    "description": 'Applies a bulk field update across develop new services records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-develop-new-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-new-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac48b6717c1b07d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/develop-new-services'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-develop-new-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopNewServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopNewServices'
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
    print(BulkUpdateDevelopNewServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
