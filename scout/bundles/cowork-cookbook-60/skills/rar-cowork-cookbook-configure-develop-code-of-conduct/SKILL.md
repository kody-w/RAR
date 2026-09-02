---
name: "rar-cowork-cookbook-configure-develop-code-of-conduct"
description: "Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_code_of_conduct", "rar_sha256": "230a1edcd12c14a7eb1a771714ac509aa9ce0f9b55d5a65362eaac347084bfc0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_code_of_conduct_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-code-of-conduct:af305db46c024e18e258e56ddb33489c31204235945914a4041346c1c1190bd7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_code_of_conduct`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_code_of_conduct_agent.py` is
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

Develop code of conduct Configuration Bulk Setup — Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-code-of-conduct
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 230a1edcd12c14a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_code_of_conduct_agent.py` first:

```bash
python3 configure_develop_code_of_conduct_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_code_of_conduct_agent.py   # or on stdin
python3 configure_develop_code_of_conduct_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop code of conduct Configuration Bulk Setup — Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-code-of-conduct
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_code_of_conduct',
    "version": '2.0.0',
    "display_name": 'Develop code of conduct Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop code of conduct from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-develop-code-of-conduct',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-code-of-conduct',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd241ba8533ab72f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-code-of-conduct'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-develop-code-of-conduct', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopCodeOfConduct(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopCodeOfConduct'
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
    print(ConfigureDevelopCodeOfConduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
