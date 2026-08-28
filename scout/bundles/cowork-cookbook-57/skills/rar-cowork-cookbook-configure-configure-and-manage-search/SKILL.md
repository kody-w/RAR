---
name: "rar-cowork-cookbook-configure-configure-and-manage-search"
description: "Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_search", "rar_sha256": "c7de73ae119f54dc13653e2528b7dc94dfa33e09ce24cf2d01c397bfdf9352a9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_manage_search`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_manage_search_agent.py` and in the RCI capsule.

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

Configure and manage search Configuration Bulk Setup — Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-search
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_manage_search_agent.py` and embedded as the fenced Python below (sha256 c7de73ae119f54dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_manage_search_agent.py` first:

```bash
python3 configure_configure_and_manage_search_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_manage_search_agent.py   # or on stdin
python3 configure_configure_and_manage_search_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage search Configuration Bulk Setup — Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-search
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_manage_search',
    "version": '2.0.0',
    "display_name": 'Configure and manage search Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-configure-and-manage-search',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-manage-search',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a527140413121df5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-search'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-manage-search', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConfigureAndManageSearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndManageSearch'
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
    print(ConfigureConfigureAndManageSearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
