---
name: "rar-cowork-cookbook-configure-analyze-safety-achievement"
description: "Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_safety_achievement", "rar_sha256": "643c77531c5044829d51f789e05b198b80e9a0e04d3c4a390b8fd23c49c53df3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_safety_achievement`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_safety_achievement_agent.py` and in the RCI capsule.

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

Analyze safety achievement Configuration Bulk Setup — Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-safety-achievement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 643c77531c504482…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_safety_achievement_agent.py` first:

```bash
python3 configure_analyze_safety_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_safety_achievement_agent.py   # or on stdin
python3 configure_analyze_safety_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze safety achievement Configuration Bulk Setup — Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-safety-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_safety_achievement',
    "version": '2.0.1',
    "display_name": 'Analyze safety achievement Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-safety-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-safety-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cdedf87341d7b1fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-safety-achievement'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-analyze-safety-achievement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeSafetyAchievement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSafetyAchievement'
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
    print(ConfigureAnalyzeSafetyAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
