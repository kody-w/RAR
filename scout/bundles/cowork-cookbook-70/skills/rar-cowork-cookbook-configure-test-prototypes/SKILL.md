---
name: "rar-cowork-cookbook-configure-test-prototypes"
description: "Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_test_prototypes", "rar_sha256": "377bab98b3b6198a711932e9adde45cd674fd74faf1fd3be5cada1f0ef5d2a70", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 377bab98b3b6198a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_test_prototypes_agent.py` first:

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
    "version": '2.0.1',
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
