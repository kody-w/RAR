---
name: "rar-cowork-cookbook-configure-scrap-defective-production"
description: "Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_scrap_defective_production", "rar_sha256": "86be7310966b000bbaf92e7cf04845cce49e355ac2b28a886ec0e4b9ce6bc3c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_scrap_defective_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-scrap-defective-production:6475016463606634d61e29296c52c1867aa30b20b2b72a7c7970e5e19d0ba7e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_scrap_defective_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_scrap_defective_production_agent.py` is
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
