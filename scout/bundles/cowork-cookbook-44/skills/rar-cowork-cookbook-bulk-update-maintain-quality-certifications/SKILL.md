---
name: "rar-cowork-cookbook-bulk-update-maintain-quality-certifications"
description: "Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_quality_certifications", "rar_sha256": "6a42c919547b8084f266ef5b380172e0a1f766c0deec8bfbf10922b6ea70dda5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 6a42c919547b8084…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_quality_certifications_agent.py` first:

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
    "version": '2.0.0',
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
