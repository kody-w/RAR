---
name: "rar-cowork-cookbook-bulk-update-define-testing-approach"
description: "Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_testing_approach", "rar_sha256": "67847eaf68a4869e4d2a8fe63372ab2af201219963ae01b6f3a6edf61f28a1ab", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_testing_approach`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_testing_approach_agent.py` and in the RCI capsule.

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

Define testing approach Bulk Field Update — Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-testing-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 67847eaf68a4869e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_testing_approach_agent.py` first:

```bash
python3 bulk_update_define_testing_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_testing_approach_agent.py   # or on stdin
python3 bulk_update_define_testing_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define testing approach Bulk Field Update — Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-testing-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_testing_approach',
    "version": '2.0.1',
    "display_name": 'Define testing approach Bulk Field Update',
    "description": 'Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-testing-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-testing-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ef18c3412cdef16',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-testing-approach'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-testing-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineTestingApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineTestingApproach'
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
    print(BulkUpdateDefineTestingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
