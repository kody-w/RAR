---
name: "rar-cowork-cookbook-bulk-update-prepare-to-go-live"
description: "Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_prepare_to_go_live", "rar_sha256": "7b8e7b62df2700f4168580c6be955c943952611450b7aa77da2ed555e75cffd4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_prepare_to_go_live`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_prepare_to_go_live_agent.py` and in the RCI capsule.

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

Prepare to go live Bulk Field Update — Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 7b8e7b62df2700f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_prepare_to_go_live_agent.py` first:

```bash
python3 bulk_update_prepare_to_go_live_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_prepare_to_go_live_agent.py   # or on stdin
python3 bulk_update_prepare_to_go_live_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare to go live Bulk Field Update — Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_prepare_to_go_live',
    "version": '2.0.1',
    "display_name": 'Prepare to go live Bulk Field Update',
    "description": 'Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-prepare-to-go-live',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a53fa905475fb98',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/prepare-to-go-live'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-prepare-to-go-live', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePrepareToGoLive(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePrepareToGoLive'
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
    print(BulkUpdatePrepareToGoLive().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
