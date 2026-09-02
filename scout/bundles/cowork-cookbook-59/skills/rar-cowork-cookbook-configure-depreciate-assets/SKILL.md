---
name: "rar-cowork-cookbook-configure-depreciate-assets"
description: "Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_depreciate_assets", "rar_sha256": "23eba458705bdabe144d5143f483f1501264411a198d273462a285af20f1f185", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_depreciate_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-depreciate-assets:dcbdf46747d187ace9173a798a70932cfde976e8faa3be37aaf369d91bc7e191", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_depreciate_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_depreciate_assets_agent.py` is
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

Depreciate assets Configuration Bulk Setup — Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 23eba458705bdabe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_depreciate_assets_agent.py` first:

```bash
python3 configure_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_depreciate_assets_agent.py   # or on stdin
python3 configure_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Configuration Bulk Setup — Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_depreciate_assets',
    "version": '2.0.0',
    "display_name": 'Depreciate assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0357dd999ee742d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDepreciateAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDepreciateAssets'
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
    print(ConfigureDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
