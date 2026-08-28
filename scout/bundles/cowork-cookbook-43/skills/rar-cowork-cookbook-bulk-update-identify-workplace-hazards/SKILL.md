---
name: "rar-cowork-cookbook-bulk-update-identify-workplace-hazards"
description: "Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_identify_workplace_hazards", "rar_sha256": "0c27341de897204406e505305df73e2eb4de47b4193b27e394638e58c1034c86", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_identify_workplace_hazards`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_identify_workplace_hazards_agent.py` and in the RCI capsule.

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

Identify workplace hazards Bulk Field Update — Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 0c27341de8972044…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_identify_workplace_hazards_agent.py` first:

```bash
python3 bulk_update_identify_workplace_hazards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_identify_workplace_hazards_agent.py   # or on stdin
python3 bulk_update_identify_workplace_hazards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify workplace hazards Bulk Field Update — Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_identify_workplace_hazards',
    "version": '2.0.1',
    "display_name": 'Identify workplace hazards Bulk Field Update',
    "description": 'Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-identify-workplace-hazards',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5c604dc98e59509e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/identify-workplace-hazards'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-identify-workplace-hazards', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateIdentifyWorkplaceHazards(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIdentifyWorkplaceHazards'
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
    print(BulkUpdateIdentifyWorkplaceHazards().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
