---
name: "rar-cowork-cookbook-configure-use-similar-cases-to-find-a-solution"
description: "Applies a bulk configuration change to use similar cases to find a solution from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_use_similar_cases_to_find_a_solution", "rar_sha256": "d288e6198cb08facc3cf56368e8be2d15c2f9e841956157dc80d3c05f1412d4c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_use_similar_cases_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `configure_use_similar_cases_to_find_a_solution_agent.py` and in the RCI capsule.

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

Use similar cases to find a solution Configuration Bulk Setup — Applies a bulk configuration change to use similar cases to find a solution from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-use-similar-cases-to-find-a-solution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_use_similar_cases_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 d288e6198cb08fac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_use_similar_cases_to_find_a_solution_agent.py` first:

```bash
python3 configure_use_similar_cases_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_use_similar_cases_to_find_a_solution_agent.py   # or on stdin
python3 configure_use_similar_cases_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use similar cases to find a solution Configuration Bulk Setup — Applies a bulk configuration change to use similar cases to find a solution from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-use-similar-cases-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_use_similar_cases_to_find_a_solution',
    "version": '2.0.1',
    "display_name": 'Use similar cases to find a solution Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to use similar cases to find a solution from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-use-similar-cases-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-use-similar-cases-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '138a8a6704285ba0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-similar-cases-to-find-a-solution'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-use-similar-cases-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureUseSimilarCasesToFindASolution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureUseSimilarCasesToFindASolution'
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
    print(ConfigureUseSimilarCasesToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
