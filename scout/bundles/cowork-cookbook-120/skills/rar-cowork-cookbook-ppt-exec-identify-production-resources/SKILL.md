---
name: "rar-cowork-cookbook-ppt-exec-identify-production-resources"
description: "Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_production_resources", "rar_sha256": "e22ad46413af05f943f43acbffbcfd770b21422d6c8943c77d5a995ec9b669c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 e22ad46413af05f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_production_resources_agent.py` first:

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
    "version": '2.0.0',
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
