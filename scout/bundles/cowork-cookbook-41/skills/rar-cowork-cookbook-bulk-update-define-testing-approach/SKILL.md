---
name: "rar-cowork-cookbook-bulk-update-define-testing-approach"
description: "Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_testing_approach", "rar_sha256": "64e351eaf58f88a44dbe451f4a62677216b4d430bd5defc3179bf68fde9d491c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 64e351eaf58f88a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_testing_approach_agent.py` first:

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
    "version": '2.0.0',
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
