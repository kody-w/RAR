---
name: "rar-cowork-cookbook-configure-test-prototypes"
description: "Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_test_prototypes", "rar_sha256": "0a7e9b457301b167b8c011c6a5f42d9baeaf61e5480f54e3af69880336791b18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_test_prototypes`. The original RAPP
agent is preserved byte-for-byte in `configure_test_prototypes_agent.py` and in the RCI capsule.

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

Test prototypes Configuration Bulk Setup — Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-test-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 0a7e9b457301b167…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_test_prototypes_agent.py` first:

```bash
python3 configure_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_test_prototypes_agent.py   # or on stdin
python3 configure_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Configuration Bulk Setup — Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_test_prototypes',
    "version": '2.0.0',
    "display_name": 'Test prototypes Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d0cad7720372edb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureTestPrototypes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTestPrototypes'
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
    print(ConfigureTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
