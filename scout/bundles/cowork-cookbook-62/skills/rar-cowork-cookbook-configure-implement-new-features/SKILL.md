---
name: "rar-cowork-cookbook-configure-implement-new-features"
description: "Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_new_features", "rar_sha256": "7bd79a6fd58f08698e5f5cb6eab62f943f82a5cfef5c14f9d41fabce621f8ed1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 7bd79a6fd58f0869…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_new_features_agent.py` first:

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
    "version": '2.0.0',
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
