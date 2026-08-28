---
name: "rar-cowork-cookbook-configure-request-travel"
description: "Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_request_travel", "rar_sha256": "f444e799a94b03b31928dc7b0bea08cbc313ce3ca6355dd07879782ea5e3591b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_request_travel`. The original RAPP
agent is preserved byte-for-byte in `configure_request_travel_agent.py` and in the RCI capsule.

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

Request travel Configuration Bulk Setup — Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_request_travel_agent.py` and embedded as the fenced Python below (sha256 f444e799a94b03b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_request_travel_agent.py` first:

```bash
python3 configure_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_request_travel_agent.py   # or on stdin
python3 configure_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Configuration Bulk Setup — Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_request_travel',
    "version": '2.0.1',
    "display_name": 'Request travel Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80b449ba83b48e6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRequestTravel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRequestTravel'
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
    print(ConfigureRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
