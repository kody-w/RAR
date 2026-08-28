---
name: "rar-cowork-cookbook-bulk-update-update-asset-register"
description: "Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_update_asset_register", "rar_sha256": "eba0a9a7cf9d54f377453283b6a860e45407fe8b73ba36454a458ac1c835ff21", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_update_asset_register`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_update_asset_register_agent.py` and in the RCI capsule.

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

Update asset register Bulk Field Update — Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 eba0a9a7cf9d54f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_update_asset_register_agent.py` first:

```bash
python3 bulk_update_update_asset_register_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_update_asset_register_agent.py   # or on stdin
python3 bulk_update_update_asset_register_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update asset register Bulk Field Update — Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_update_asset_register',
    "version": '2.0.0',
    "display_name": 'Update asset register Bulk Field Update',
    "description": 'Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-update-asset-register',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-update-asset-register',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31a68c652a5292d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-asset-register'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-update-asset-register', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateUpdateAssetRegister(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateUpdateAssetRegister'
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
    print(BulkUpdateUpdateAssetRegister().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
