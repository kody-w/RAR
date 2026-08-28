---
name: "rar-cowork-cookbook-bulk-update-prepare-to-go-live"
description: "Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_prepare_to_go_live", "rar_sha256": "57bcd271f599dbd0e5d431dea947e0df0f64946e28bdaa00bf891b505aca554e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 57bcd271f599dbd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_prepare_to_go_live_agent.py` first:

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
    "version": '2.0.0',
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
