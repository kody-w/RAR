---
name: "rar-cowork-cookbook-configure-track-project-fees"
description: "Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_project_fees", "rar_sha256": "97dae94ae66e2a55ebe42c4794dfa0721a2557e1594718b7711c184ecdc04bc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_track_project_fees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-track-project-fees:3d1b10530355b145c1a5e03b51314119fe40ca299028611f306036ac81ae9170", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_track_project_fees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_track_project_fees_agent.py` is
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

Track project fees Configuration Bulk Setup — Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 97dae94ae66e2a55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_project_fees_agent.py` first:

```bash
python3 configure_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_project_fees_agent.py   # or on stdin
python3 configure_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Configuration Bulk Setup — Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_project_fees',
    "version": '2.0.0',
    "display_name": 'Track project fees Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94e234b33eb0c408',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureTrackProjectFees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackProjectFees'
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
    print(ConfigureTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
