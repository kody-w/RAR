---
name: "rar-cowork-cookbook-configure-develop-code-of-conduct"
description: "Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_code_of_conduct", "rar_sha256": "f044ee7da58a0a765d2683481b919fb11830634d2b9ca17f8143e9b85fac4a4e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 f044ee7da58a0a76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_code_of_conduct_agent.py` first:

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
    "version": '2.0.1',
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
