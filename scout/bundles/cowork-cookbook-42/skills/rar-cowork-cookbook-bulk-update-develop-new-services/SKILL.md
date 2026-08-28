---
name: "rar-cowork-cookbook-bulk-update-develop-new-services"
description: "Applies a bulk field update across develop new services records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_new_services", "rar_sha256": "8dc78317504273e4d629335227f343ffc113e2b22ff26970adca5bc0ad9e1925", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_new_services`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_new_services_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 8dc78317504273e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_new_services_agent.py` first:

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
    "version": '2.0.1',
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
