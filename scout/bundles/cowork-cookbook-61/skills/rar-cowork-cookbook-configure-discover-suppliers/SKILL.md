---
name: "rar-cowork-cookbook-configure-discover-suppliers"
description: "Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_discover_suppliers", "rar_sha256": "f3ad0f3ab10e76b46826d62f9fa7f72ad74b5533facb63ff98d33b94ae60a74d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_discover_suppliers`. The original RAPP
agent is preserved byte-for-byte in `configure_discover_suppliers_agent.py` and in the RCI capsule.

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

Discover suppliers Configuration Bulk Setup — Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-discover-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 f3ad0f3ab10e76b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_discover_suppliers_agent.py` first:

```bash
python3 configure_discover_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_discover_suppliers_agent.py   # or on stdin
python3 configure_discover_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Discover suppliers Configuration Bulk Setup — Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-discover-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_discover_suppliers',
    "version": '2.0.0',
    "display_name": 'Discover suppliers Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-discover-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-discover-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf8ae9b64d22d60f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/discover-suppliers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-discover-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDiscoverSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDiscoverSuppliers'
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
    print(ConfigureDiscoverSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
