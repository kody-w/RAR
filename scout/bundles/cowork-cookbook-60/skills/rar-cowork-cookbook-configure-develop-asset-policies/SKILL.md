---
name: "rar-cowork-cookbook-configure-develop-asset-policies"
description: "Applies a bulk configuration change to develop asset policies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_asset_policies", "rar_sha256": "32eb4ee5f83d1bd040295cd9f3b925843779a994d5cf15fbaaeca432787f5cdd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_asset_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-asset-policies:6ba9ae83e2f990cf55fa65a57d8e7905673a426dc804d5cd7043d1761a6660be", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_asset_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_asset_policies_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 32eb4ee5f83d1bd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_asset_policies_agent.py` first:

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
    "version": '2.0.0',
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
