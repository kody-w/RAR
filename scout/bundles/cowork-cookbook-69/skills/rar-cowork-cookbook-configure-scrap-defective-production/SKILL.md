---
name: "rar-cowork-cookbook-configure-scrap-defective-production"
description: "Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_scrap_defective_production", "rar_sha256": "86be7310966b000bbaf92e7cf04845cce49e355ac2b28a886ec0e4b9ce6bc3c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_scrap_defective_production`. The original RAPP
agent is preserved byte-for-byte in `configure_scrap_defective_production_agent.py` and in the RCI capsule.

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

Scrap defective production Configuration Bulk Setup — Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-scrap-defective-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_scrap_defective_production_agent.py` and embedded as the fenced Python below (sha256 86be7310966b000b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_scrap_defective_production_agent.py` first:

```bash
python3 configure_scrap_defective_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_scrap_defective_production_agent.py   # or on stdin
python3 configure_scrap_defective_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective production Configuration Bulk Setup — Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-scrap-defective-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_scrap_defective_production',
    "version": '2.0.0',
    "display_name": 'Scrap defective production Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-scrap-defective-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-scrap-defective-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fff1efb887008ee0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/scrap-defective-production'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-scrap-defective-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureScrapDefectiveProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScrapDefectiveProduction'
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
    print(ConfigureScrapDefectiveProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
