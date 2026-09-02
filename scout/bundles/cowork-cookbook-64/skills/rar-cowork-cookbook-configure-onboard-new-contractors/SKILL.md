---
name: "rar-cowork-cookbook-configure-onboard-new-contractors"
description: "Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_onboard_new_contractors", "rar_sha256": "1f1dbfe356a18d80b8bff0b074120888c940cbac118bdb94709aaea014e2b2e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_onboard_new_contractors_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-onboard-new-contractors:67a157dd5fc5f922a6d3642c9aa6da0f581ca18250f616a4263ea8c26b427e8f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_onboard_new_contractors`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_onboard_new_contractors_agent.py` is
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

Onboard new contractors Configuration Bulk Setup — Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-onboard-new-contractors
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 1f1dbfe356a18d80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_onboard_new_contractors_agent.py` first:

```bash
python3 configure_onboard_new_contractors_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_onboard_new_contractors_agent.py   # or on stdin
python3 configure_onboard_new_contractors_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new contractors Configuration Bulk Setup — Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-onboard-new-contractors
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_onboard_new_contractors',
    "version": '2.0.0',
    "display_name": 'Onboard new contractors Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-onboard-new-contractors',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-onboard-new-contractors',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a8a7440a353b2b4b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-contractors'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-onboard-new-contractors', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureOnboardNewContractors(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureOnboardNewContractors'
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
    print(ConfigureOnboardNewContractors().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
