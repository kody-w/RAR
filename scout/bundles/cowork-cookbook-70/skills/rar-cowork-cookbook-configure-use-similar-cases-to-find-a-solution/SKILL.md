---
name: "rar-cowork-cookbook-configure-use-similar-cases-to-find-a-solution"
description: "Applies a bulk configuration change to use similar cases to find a solution from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_use_similar_cases_to_find_a_solution", "rar_sha256": "67a02fb38372f1dd14915eccf948a70af99cf7805624e086ecaa569187219454", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_use_similar_cases_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 67a02fb38372f1dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_use_similar_cases_to_find_a_solution_agent.py` first:

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
    "version": '2.0.0',
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
