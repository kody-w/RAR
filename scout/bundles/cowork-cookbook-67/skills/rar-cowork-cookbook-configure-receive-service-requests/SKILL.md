---
name: "rar-cowork-cookbook-configure-receive-service-requests"
description: "Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_service_requests", "rar_sha256": "4b0d0a801f36436f5fd927ddd817709b745136f7ece1f5a22bf765cd24c09229", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_receive_service_requests`. The original RAPP
agent is preserved byte-for-byte in `configure_receive_service_requests_agent.py` and in the RCI capsule.

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

Receive service requests Configuration Bulk Setup — Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 4b0d0a801f36436f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_service_requests_agent.py` first:

```bash
python3 configure_receive_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_service_requests_agent.py   # or on stdin
python3 configure_receive_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive service requests Configuration Bulk Setup — Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_service_requests',
    "version": '2.0.1',
    "display_name": 'Receive service requests Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-receive-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd940a21f8f71b390',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/receive-service-requests'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-receive-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReceiveServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveServiceRequests'
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
    print(ConfigureReceiveServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
