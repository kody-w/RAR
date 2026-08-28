---
name: "rar-cowork-cookbook-configure-identify-workplace-hazards"
description: "Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_workplace_hazards", "rar_sha256": "718ef5475e26a77341c68b49a45a3b1b63e3b16b6e4239364c84529c3ae942d8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_workplace_hazards`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_workplace_hazards_agent.py` and in the RCI capsule.

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
