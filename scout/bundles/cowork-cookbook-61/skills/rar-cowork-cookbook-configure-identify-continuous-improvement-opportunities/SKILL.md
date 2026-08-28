---
name: "rar-cowork-cookbook-configure-identify-continuous-improvement-opportunities"
description: "Applies a bulk configuration change to identify continuous improvement opportunities from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_continuous_improvement_opportunities", "rar_sha256": "ed202f404b981b95d4a40b4aafa907071d6485611149c021fd83072f58e8b7e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_continuous_improvement_opportunities`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_continuous_improvement_opportunities_agent.py` and in the RCI capsule.

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

Identify continuous improvement opportunities Configuration Bulk Setup — Applies a bulk configuration change to identify continuous improvement opportunities from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-continuous-improvement-opportunities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 ed202f404b981b95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_continuous_improvement_opportunities_agent.py` first:

```bash
python3 configure_identify_continuous_improvement_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_continuous_improvement_opportunities_agent.py   # or on stdin
python3 configure_identify_continuous_improvement_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify continuous improvement opportunities Configuration Bulk Setup — Applies a bulk configuration change to identify continuous improvement opportunities from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-continuous-improvement-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_continuous_improvement_opportunities',
    "version": '2.0.0',
    "display_name": 'Identify continuous improvement opportunities Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to identify continuous improvement opportunities from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-identify-continuous-improvement-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-continuous-improvement-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47e4765750aef6b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/identify-continuous-improvement-opportunities'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-identify-continuous-improvement-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureIdentifyContinuousImprovementOpportunities(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyContinuousImprovementOpportunities'
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
    print(ConfigureIdentifyContinuousImprovementOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
