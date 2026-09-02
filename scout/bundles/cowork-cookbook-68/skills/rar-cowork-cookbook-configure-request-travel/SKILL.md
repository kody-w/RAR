---
name: "rar-cowork-cookbook-configure-request-travel"
description: "Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_request_travel", "rar_sha256": "f2397b52536cb7cbec0b7a9f50e900d26908c5a06522c6f15db2ff5714b00d32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_request_travel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-request-travel:d30952ba3aaa40a08b897ca08e5c29f27ee75be786fc0165a00929e797befe91", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_request_travel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_request_travel_agent.py` is
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

Request travel Configuration Bulk Setup — Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_request_travel_agent.py` and embedded as the fenced Python below (sha256 f2397b52536cb7cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_request_travel_agent.py` first:

```bash
python3 configure_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_request_travel_agent.py   # or on stdin
python3 configure_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Configuration Bulk Setup — Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_request_travel',
    "version": '2.0.0',
    "display_name": 'Request travel Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80b449ba83b48e6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRequestTravel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRequestTravel'
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
    print(ConfigureRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
