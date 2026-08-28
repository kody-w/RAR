---
name: "rar-cowork-cookbook-bulk-update-identify-workplace-hazards"
description: "Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_identify_workplace_hazards", "rar_sha256": "e0ee9fe72edf26dc405fb0f9f15fe022d96c1277820bd99bb64758075e2100ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 e0ee9fe72edf26dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_identify_workplace_hazards_agent.py` first:

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
    "version": '2.0.0',
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
