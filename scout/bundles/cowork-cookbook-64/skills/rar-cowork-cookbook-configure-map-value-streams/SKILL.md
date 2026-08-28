---
name: "rar-cowork-cookbook-configure-map-value-streams"
description: "Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_map_value_streams", "rar_sha256": "1458777452e6cca9511e50bae53cf570a089687150c4980dd9134d4856d01bf0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_map_value_streams`. The original RAPP
agent is preserved byte-for-byte in `configure_map_value_streams_agent.py` and in the RCI capsule.

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

Map value streams Configuration Bulk Setup — Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-map-value-streams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 1458777452e6cca9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_map_value_streams_agent.py` first:

```bash
python3 configure_map_value_streams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_map_value_streams_agent.py   # or on stdin
python3 configure_map_value_streams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map value streams Configuration Bulk Setup — Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-map-value-streams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_map_value_streams',
    "version": '2.0.0',
    "display_name": 'Map value streams Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-map-value-streams',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-map-value-streams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ffb53fe67eb4147',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/map-value-streams'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-map-value-streams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureMapValueStreams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMapValueStreams'
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
    print(ConfigureMapValueStreams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
