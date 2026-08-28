---
name: "rar-cowork-cookbook-bulk-update-maintain-quality-certifications"
description: "Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_quality_certifications", "rar_sha256": "a5afc80aeabc4bb37e843b08aa2abba43ec0af662593a69920d335a47a54798f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_maintain_quality_certifications`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_maintain_quality_certifications_agent.py` and in the RCI capsule.

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

Maintain quality certifications Bulk Field Update — Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 a5afc80aeabc4bb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_quality_certifications_agent.py` first:

```bash
python3 bulk_update_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_maintain_quality_certifications_agent.py   # or on stdin
python3 bulk_update_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Bulk Field Update — Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_maintain_quality_certifications',
    "version": '2.0.1',
    "display_name": 'Maintain quality certifications Bulk Field Update',
    "description": 'Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a3529012e63bc27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMaintainQualityCertifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMaintainQualityCertifications'
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
    print(BulkUpdateMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
