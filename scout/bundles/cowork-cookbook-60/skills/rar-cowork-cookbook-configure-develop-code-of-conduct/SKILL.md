---
name: "rar-cowork-cookbook-configure-develop-code-of-conduct"
description: "Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_code_of_conduct", "rar_sha256": "230a1edcd12c14a7eb1a771714ac509aa9ce0f9b55d5a65362eaac347084bfc0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_code_of_conduct`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_code_of_conduct_agent.py` and in the RCI capsule.

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

Develop code of conduct Configuration Bulk Setup — Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-code-of-conduct
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 230a1edcd12c14a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_code_of_conduct_agent.py` first:

```bash
python3 configure_develop_code_of_conduct_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_code_of_conduct_agent.py   # or on stdin
python3 configure_develop_code_of_conduct_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop code of conduct Configuration Bulk Setup — Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-code-of-conduct
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_code_of_conduct',
    "version": '2.0.0',
    "display_name": 'Develop code of conduct Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-develop-code-of-conduct',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-code-of-conduct',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd241ba8533ab72f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-code-of-conduct'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-develop-code-of-conduct', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopCodeOfConduct(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopCodeOfConduct'
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
    print(ConfigureDevelopCodeOfConduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
