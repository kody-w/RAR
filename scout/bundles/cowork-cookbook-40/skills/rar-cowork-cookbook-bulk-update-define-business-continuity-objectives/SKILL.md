---
name: "rar-cowork-cookbook-bulk-update-define-business-continuity-objectives"
description: "Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_business_continuity_objectives", "rar_sha256": "8a97b92ac8a83fddf2ad98a358bc11696decd7d5cf4636fa4defaecfd67bf23f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_business_continuity_objectives`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_business_continuity_objectives_agent.py` and in the RCI capsule.

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

Define business continuity objectives Bulk Field Update — Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 8a97b92ac8a83fdd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_business_continuity_objectives_agent.py` first:

```bash
python3 bulk_update_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_business_continuity_objectives_agent.py   # or on stdin
python3 bulk_update_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Bulk Field Update — Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_business_continuity_objectives',
    "version": '2.0.0',
    "display_name": 'Define business continuity objectives Bulk Field Update',
    "description": 'Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c3aa56f9b3e5c04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineBusinessContinuityObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBusinessContinuityObjectives'
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
    print(BulkUpdateDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
