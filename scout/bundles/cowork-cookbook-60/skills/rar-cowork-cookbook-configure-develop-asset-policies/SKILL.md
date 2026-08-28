---
name: "rar-cowork-cookbook-configure-develop-asset-policies"
description: "Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_asset_policies", "rar_sha256": "d3fcdcff440d11c0ba2a7fec70899aa0235276c1465151186b10049413294c16", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_asset_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_asset_policies_agent.py` and in the RCI capsule.

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

Develop asset policies Configuration Bulk Setup — Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 d3fcdcff440d11c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_asset_policies_agent.py` first:

```bash
python3 configure_develop_asset_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_asset_policies_agent.py   # or on stdin
python3 configure_develop_asset_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop asset policies Configuration Bulk Setup — Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_asset_policies',
    "version": '2.0.1',
    "display_name": 'Develop asset policies Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-asset-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-asset-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68621f893f2abfd6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-asset-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-develop-asset-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopAssetPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopAssetPolicies'
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
    print(ConfigureDevelopAssetPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
