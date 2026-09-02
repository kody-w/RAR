---
name: "rar-cowork-cookbook-configure-identify-workplace-hazards"
description: "Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_workplace_hazards", "rar_sha256": "718ef5475e26a77341c68b49a45a3b1b63e3b16b6e4239364c84529c3ae942d8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_identify_workplace_hazards_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-identify-workplace-hazards:0f4a13e40d8cf646a6e95115dc11e0b06d2c3d03bf7b8cbe5b7f12259c313e9b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_identify_workplace_hazards`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_identify_workplace_hazards_agent.py` is
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

Identify workplace hazards Configuration Bulk Setup — Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-workplace-hazards
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 718ef5475e26a773…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_workplace_hazards_agent.py` first:

```bash
python3 configure_identify_workplace_hazards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_workplace_hazards_agent.py   # or on stdin
python3 configure_identify_workplace_hazards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify workplace hazards Configuration Bulk Setup — Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-workplace-hazards
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_workplace_hazards',
    "version": '2.0.0',
    "display_name": 'Identify workplace hazards Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-identify-workplace-hazards',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-workplace-hazards',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '700ef15654dd09eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/identify-workplace-hazards'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-identify-workplace-hazards', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureIdentifyWorkplaceHazards(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyWorkplaceHazards'
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
    print(ConfigureIdentifyWorkplaceHazards().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
