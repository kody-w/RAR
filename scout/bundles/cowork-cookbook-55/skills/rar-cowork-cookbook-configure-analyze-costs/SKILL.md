---
name: "rar-cowork-cookbook-configure-analyze-costs"
description: "Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_costs", "rar_sha256": "b3d8795e657ade0abd0f9047a7edcce847e9d4f28acafe0c06f5e31a06f06682", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-costs:4613ffa50a240138d8fbd2c75ea762eb2b493f9539f0018951e3f5ba5070585d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_costs_agent.py` is
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

Analyze costs Configuration Bulk Setup — Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 b3d8795e657ade0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_costs_agent.py` first:

```bash
python3 configure_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_costs_agent.py   # or on stdin
python3 configure_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Configuration Bulk Setup — Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_costs',
    "version": '2.0.0',
    "display_name": 'Analyze costs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b14bd69f16ad29d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeCosts'
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
    print(ConfigureAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
