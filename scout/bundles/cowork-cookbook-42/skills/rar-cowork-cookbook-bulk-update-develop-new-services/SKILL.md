---
name: "rar-cowork-cookbook-bulk-update-develop-new-services"
description: "Applies a bulk field update across develop new services records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_new_services", "rar_sha256": "d2996087d358825a392f703268320601e4c2733d18c777beba5eac77ad3e3ea7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
