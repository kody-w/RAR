---
name: "rar-cowork-cookbook-bulk-update-respond-to-non-compliance"
description: "Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_respond_to_non_compliance", "rar_sha256": "80cd127df347e3da78069a319900df4143e910c4743187c83be39ba21a078e15", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_respond_to_non_compliance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_respond_to_non_compliance_agent.py` and in the RCI capsule.

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

Respond to non-compliance Bulk Field Update — Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 80cd127df347e3da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_respond_to_non_compliance_agent.py` first:

```bash
python3 bulk_update_respond_to_non_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_respond_to_non_compliance_agent.py   # or on stdin
python3 bulk_update_respond_to_non_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Respond to non-compliance Bulk Field Update — Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_respond_to_non_compliance',
    "version": '2.0.1',
    "display_name": 'Respond to non-compliance Bulk Field Update',
    "description": 'Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-respond-to-non-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b7085560e05fbca6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/respond-to-non-compliance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-respond-to-non-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRespondToNonCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRespondToNonCompliance'
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
    print(BulkUpdateRespondToNonCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
