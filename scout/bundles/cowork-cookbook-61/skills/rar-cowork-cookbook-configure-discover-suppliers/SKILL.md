---
name: "rar-cowork-cookbook-configure-discover-suppliers"
description: "Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_discover_suppliers", "rar_sha256": "f3ad0f3ab10e76b46826d62f9fa7f72ad74b5533facb63ff98d33b94ae60a74d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_discover_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-discover-suppliers:a0e69a716439431b3144fe538cda0df5b11d5a6180a2b3676c0b07b7eb30712f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_discover_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_discover_suppliers_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
