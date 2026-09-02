---
name: "rar-cowork-cookbook-configure-develop-sales-catalogs"
description: "Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_sales_catalogs", "rar_sha256": "21175272b2fc65993e2db4066ac109b65184794040d72a18bad0245d65694bf3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_sales_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-sales-catalogs:597f37ae61cce466eeaeb9fe9d013eb8725f72f3c727b7a85b543d886602c2c1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_sales_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_sales_catalogs_agent.py` is
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

Develop sales catalogs Configuration Bulk Setup — Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 21175272b2fc6599…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_sales_catalogs_agent.py` first:

```bash
python3 configure_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_sales_catalogs_agent.py   # or on stdin
python3 configure_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Configuration Bulk Setup — Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_sales_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop sales catalogs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a413df5a0fdc726b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopSalesCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSalesCatalogs'
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
    print(ConfigureDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
