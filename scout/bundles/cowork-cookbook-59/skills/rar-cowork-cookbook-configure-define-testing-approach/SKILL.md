---
name: "rar-cowork-cookbook-configure-define-testing-approach"
description: "Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_testing_approach", "rar_sha256": "4e4bbebe39bdc84bd09bdcc1300a72016e3f98e7e66b12a9c0e2d18e2ff30e99", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_testing_approach`. The original RAPP
agent is preserved byte-for-byte in `configure_define_testing_approach_agent.py` and in the RCI capsule.

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

Define testing approach Configuration Bulk Setup — Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-testing-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 4e4bbebe39bdc84b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_testing_approach_agent.py` first:

```bash
python3 configure_define_testing_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_testing_approach_agent.py   # or on stdin
python3 configure_define_testing_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define testing approach Configuration Bulk Setup — Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-testing-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_testing_approach',
    "version": '2.0.1',
    "display_name": 'Define testing approach Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-testing-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-testing-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80d324ffacc2507d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-testing-approach'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-define-testing-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineTestingApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineTestingApproach'
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
    print(ConfigureDefineTestingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
