---
name: "rar-cowork-cookbook-bulk-update-respond-to-non-compliance"
description: "Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_respond_to_non_compliance", "rar_sha256": "d957fb206b964afc3c48872245f1f08d95176abd5feb012c42e22809573a2b2d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 d957fb206b964afc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_respond_to_non_compliance_agent.py` first:

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
    "version": '2.0.0',
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
