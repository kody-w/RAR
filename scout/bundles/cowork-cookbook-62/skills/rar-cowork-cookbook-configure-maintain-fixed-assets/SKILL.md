---
name: "rar-cowork-cookbook-configure-maintain-fixed-assets"
description: "Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_fixed_assets", "rar_sha256": "0d8437ae559813180707a2271e5316d0cfa2b49185907e0b6e887729d32e2a7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_maintain_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-maintain-fixed-assets:88d86864e8f764591c92a077ff97b893418b8aeb54bfb55e706aa4ee57cf8173", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_maintain_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_maintain_fixed_assets_agent.py` is
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

Maintain fixed assets Configuration Bulk Setup — Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 0d8437ae55981318…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_fixed_assets_agent.py` first:

```bash
python3 configure_maintain_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_maintain_fixed_assets_agent.py   # or on stdin
python3 configure_maintain_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain fixed assets Configuration Bulk Setup — Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_maintain_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Maintain fixed assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-maintain-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-maintain-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b96abe3654e63ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-maintain-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureMaintainFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMaintainFixedAssets'
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
    print(ConfigureMaintainFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
