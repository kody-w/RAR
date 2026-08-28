---
name: "rar-cowork-cookbook-configure-identify-continuous-improvement-opportunities"
description: "Applies a bulk configuration change to identify continuous improvement opportunities from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_continuous_improvement_opportunities", "rar_sha256": "ec6b21e4a1eb9ec15d7d45a3445d5515a22d2e6caaf52e4d15a12b288cc6c23e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 ec6b21e4a1eb9ec1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_continuous_improvement_opportunities_agent.py` first:

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
    "version": '2.0.1',
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
