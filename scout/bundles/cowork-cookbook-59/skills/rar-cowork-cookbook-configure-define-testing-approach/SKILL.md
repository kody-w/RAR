---
name: "rar-cowork-cookbook-configure-define-testing-approach"
description: "Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_testing_approach", "rar_sha256": "8772853e8670629f4718753f10f6c731c220d428bdd049c850cf85f09a63c25f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 8772853e8670629f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_testing_approach_agent.py` first:

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
    "version": '2.0.0',
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
