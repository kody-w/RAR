---
name: "rar-cowork-cookbook-bulk-update-design-formulas"
description: "Applies a bulk field update across design formulas records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_design_formulas", "rar_sha256": "9d9b7fb0bbf1234bcaa3041e40b13d2e127420394fa36725f81091358ef3885e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_design_formulas`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_design_formulas_agent.py` and in the RCI capsule.

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

Design formulas Bulk Field Update — Applies a bulk field update across design formulas records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-design-formulas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_design_formulas_agent.py` and embedded as the fenced Python below (sha256 9d9b7fb0bbf1234b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_design_formulas_agent.py` first:

```bash
python3 bulk_update_design_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_design_formulas_agent.py   # or on stdin
python3 bulk_update_design_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design formulas Bulk Field Update — Applies a bulk field update across design formulas records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-design-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_design_formulas',
    "version": '2.0.0',
    "display_name": 'Design formulas Bulk Field Update',
    "description": 'Applies a bulk field update across design formulas records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-design-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-design-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b94051365663f8b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-formulas'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-design-formulas', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDesignFormulas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDesignFormulas'
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
    print(BulkUpdateDesignFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
