---
name: "rar-cowork-cookbook-configure-implement-new-features"
description: "Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_new_features", "rar_sha256": "f9ffee7195c0cfd7b95026a60c30e5f9ac75e46e67c3126f1217d5b858ab19a4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_implement_new_features`. The original RAPP
agent is preserved byte-for-byte in `configure_implement_new_features_agent.py` and in the RCI capsule.

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

Implement new features Configuration Bulk Setup — Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-new-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 f9ffee7195c0cfd7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_new_features_agent.py` first:

```bash
python3 configure_implement_new_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_implement_new_features_agent.py   # or on stdin
python3 configure_implement_new_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement new features Configuration Bulk Setup — Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-new-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_implement_new_features',
    "version": '2.0.1',
    "display_name": 'Implement new features Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-implement-new-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-implement-new-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21434cd3e49b1e5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/implement-new-features'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-implement-new-features', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureImplementNewFeatures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureImplementNewFeatures'
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
    print(ConfigureImplementNewFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
