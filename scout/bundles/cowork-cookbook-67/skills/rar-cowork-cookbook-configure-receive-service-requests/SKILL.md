---
name: "rar-cowork-cookbook-configure-receive-service-requests"
description: "Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_service_requests", "rar_sha256": "5c609b9b374f8488e26462ff1ffdc4a487005d2df897dd0545b13a2b17edafb7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 5c609b9b374f8488…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_service_requests_agent.py` first:

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
    "version": '2.0.0',
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
