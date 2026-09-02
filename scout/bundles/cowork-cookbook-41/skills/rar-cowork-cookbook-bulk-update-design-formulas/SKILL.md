---
name: "rar-cowork-cookbook-bulk-update-design-formulas"
description: "Applies a bulk field update across design formulas records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_design_formulas", "rar_sha256": "9d9b7fb0bbf1234bcaa3041e40b13d2e127420394fa36725f81091358ef3885e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_design_formulas_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-design-formulas:f6fba0c671c1b8760811aa075486d6a48f97fb5c5b12d80891113bcccebd45c4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_design_formulas`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_design_formulas_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
