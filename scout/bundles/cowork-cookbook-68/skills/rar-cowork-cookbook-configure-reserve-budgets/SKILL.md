---
name: "rar-cowork-cookbook-configure-reserve-budgets"
description: "Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reserve_budgets", "rar_sha256": "75c1e518be4af43832e65b525c6d7ddc82605985bc5463a3f6651c3f0e12ba6b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_reserve_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-reserve-budgets:c5781e6506ada321ae09d70a08e8f209e39aa313751b4eeaf5bc945ae8a83bb7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_reserve_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_reserve_budgets_agent.py` is
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

Reserve budgets Configuration Bulk Setup — Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 75c1e518be4af438…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reserve_budgets_agent.py` first:

```bash
python3 configure_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reserve_budgets_agent.py   # or on stdin
python3 configure_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Configuration Bulk Setup — Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reserve_budgets',
    "version": '2.0.0',
    "display_name": 'Reserve budgets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b36e23b46df8ccb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReserveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReserveBudgets'
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
    print(ConfigureReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
