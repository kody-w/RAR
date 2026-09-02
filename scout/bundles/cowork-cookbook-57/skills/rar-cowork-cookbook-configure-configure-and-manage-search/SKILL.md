---
name: "rar-cowork-cookbook-configure-configure-and-manage-search"
description: "Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_search", "rar_sha256": "c7de73ae119f54dc13653e2528b7dc94dfa33e09ce24cf2d01c397bfdf9352a9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_configure_and_manage_search_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-configure-and-manage-search:01c8f663064475af1a6295be7102617d052ac679c0e401c595b93d01b60188c8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_configure_and_manage_search`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_configure_and_manage_search_agent.py` is
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
