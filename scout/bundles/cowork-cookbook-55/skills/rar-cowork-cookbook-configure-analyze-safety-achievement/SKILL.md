---
name: "rar-cowork-cookbook-configure-analyze-safety-achievement"
description: "Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_safety_achievement", "rar_sha256": "296036988eae31f6e4debc99df2499eb95e6166a1417e265a846d775a299a833", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_safety_achievement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-safety-achievement:2d14431b1277d0a850f523ff7f9999b789adefbc538b0e9de35c3ef04d8442c0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_safety_achievement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_safety_achievement_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 296036988eae31f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_safety_achievement_agent.py` first:

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
    "version": '2.0.0',
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
