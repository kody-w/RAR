---
name: "rar-cowork-cookbook-configure-identify-continuous-improvement-opportunities"
description: "Applies a bulk configuration change to identify continuous improvement opportunities from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_continuous_improvement_opportunities", "rar_sha256": "ed202f404b981b95d4a40b4aafa907071d6485611149c021fd83072f58e8b7e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_identify_continuous_improvement_opportunities_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-identify-continuous-improvement-opportunities:fb42f99a6e1d71d55d3d7f4727ac8b1ceb615723da17682a1e7a809042860cda", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_identify_continuous_improvement_opportunities`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_identify_continuous_improvement_opportunities_agent.py` is
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
