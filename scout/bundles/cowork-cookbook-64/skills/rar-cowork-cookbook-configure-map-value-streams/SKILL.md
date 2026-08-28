---
name: "rar-cowork-cookbook-configure-map-value-streams"
description: "Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_map_value_streams", "rar_sha256": "f9539fc0733b1d152b9d0395901f37b328ee860a6920473cab958e5065db5ef2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 f9539fc0733b1d15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_map_value_streams_agent.py` first:

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
    "version": '2.0.1',
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
