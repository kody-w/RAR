---
name: "rar-cowork-cookbook-configure-recognize-project-revenue"
description: "Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_project_revenue", "rar_sha256": "8ef9e3dc9d3ed5d17591a06de013272527471aeeb6c357fa0301400521851189", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_recognize_project_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-recognize-project-revenue:8b520bb22e8ef7644224ec2603b6cc25dcb779b216a634cd74a072e49e509a13", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_recognize_project_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_recognize_project_revenue_agent.py` is
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

Recognize project revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-project-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 8ef9e3dc9d3ed5d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_project_revenue_agent.py` first:

```bash
python3 configure_recognize_project_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_recognize_project_revenue_agent.py   # or on stdin
python3 configure_recognize_project_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize project revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-project-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_recognize_project_revenue',
    "version": '2.0.0',
    "display_name": 'Recognize project revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-recognize-project-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-recognize-project-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a6a8adeb311d11f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/recognize-project-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-recognize-project-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRecognizeProjectRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecognizeProjectRevenue'
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
    print(ConfigureRecognizeProjectRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
