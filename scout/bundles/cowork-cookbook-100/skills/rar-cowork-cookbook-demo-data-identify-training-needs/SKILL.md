---
name: "rar-cowork-cookbook-demo-data-identify-training-needs"
description: "Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_identify_training_needs", "rar_sha256": "52ebcd10aff3e1da542739856f9bb9ba9b1d6c7eb446e586548b5f07bac735a4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Demo Data Generator — Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 52ebcd10aff3e1da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_identify_training_needs_agent.py` first:

```bash
python3 demo_data_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_identify_training_needs_agent.py   # or on stdin
python3 demo_data_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Demo Data Generator — Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_identify_training_needs',
    "version": '2.0.0',
    "display_name": 'Identify training needs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9686183a09c31980',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataIdentifyTrainingNeeds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataIdentifyTrainingNeeds'
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
    print(DemoDataIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
