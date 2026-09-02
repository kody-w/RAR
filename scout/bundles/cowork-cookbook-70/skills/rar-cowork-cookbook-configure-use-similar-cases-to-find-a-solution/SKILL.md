---
name: "rar-cowork-cookbook-configure-use-similar-cases-to-find-a-solution"
description: "Applies a bulk configuration change to use similar cases to find a solution from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_use_similar_cases_to_find_a_solution", "rar_sha256": "67a02fb38372f1dd14915eccf948a70af99cf7805624e086ecaa569187219454", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_use_similar_cases_to_find_a_solution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-use-similar-cases-to-find-a-solution:01d72244f6371c1f7ecf26861c3e8fc3bd8b929346f8d29801ff7002a1aa590d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_use_similar_cases_to_find_a_solution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_use_similar_cases_to_find_a_solution_agent.py` is
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
