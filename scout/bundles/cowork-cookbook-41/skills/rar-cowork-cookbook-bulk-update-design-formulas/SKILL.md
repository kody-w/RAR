---
name: "rar-cowork-cookbook-bulk-update-design-formulas"
description: "Applies a bulk field update across design formulas records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_design_formulas", "rar_sha256": "b3de0a39f30bf1b4f5ab6baef91786d3a219277dc648f0550c48fec5d7fb458f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_design_formulas_agent.py` and embedded as the fenced Python below (sha256 b3de0a39f30bf1b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_design_formulas_agent.py` first:

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
    "version": '2.0.1',
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
