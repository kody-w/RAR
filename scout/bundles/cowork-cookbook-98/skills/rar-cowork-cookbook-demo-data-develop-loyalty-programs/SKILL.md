---
name: "rar-cowork-cookbook-demo-data-develop-loyalty-programs"
description: "Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_loyalty_programs", "rar_sha256": "3278be9c760e820a97473196aebab3c3cedf0d92ca7a34274bdb2d441b95d294", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 3278be9c760e820a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_loyalty_programs_agent.py` first:

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
    "version": '2.0.0',
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
