---
name: "rar-cowork-cookbook-ppt-exec-identify-production-resources"
description: "Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_production_resources", "rar_sha256": "02be841600a1bd0c3f3f0ba1133a7096eca0e684d4932501912d7923794362af", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_production_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_production_resources_agent.py` and in the RCI capsule.

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

Identify production resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 02be841600a1bd0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_production_resources_agent.py` first:

```bash
python3 ppt_exec_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_production_resources_agent.py   # or on stdin
python3 ppt_exec_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_production_resources',
    "version": '2.0.1',
    "display_name": 'Identify production resources Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a04d7e7860c40fa3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecIdentifyProductionResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyProductionResources'
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
    print(PptExecIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
