---
name: "rar-cowork-cookbook-demo-data-develop-loyalty-programs"
description: "Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_loyalty_programs", "rar_sha256": "ea04d21783f58d42d20aa18ff8b7da9fa929571f4b9f513c8cb1e69b34eeee92", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_loyalty_programs_agent.py` and in the RCI capsule.

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

Develop loyalty programs Demo Data Generator — Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 ea04d21783f58d42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_loyalty_programs_agent.py` first:

```bash
python3 demo_data_develop_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_loyalty_programs_agent.py   # or on stdin
python3 demo_data_develop_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop loyalty programs Demo Data Generator — Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_loyalty_programs',
    "version": '2.0.1',
    "display_name": 'Develop loyalty programs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e110ebf1fbfcd5d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-loyalty-programs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopLoyaltyPrograms'
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
    print(DemoDataDevelopLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
