---
name: "rar-cowork-cookbook-demo-data-develop-support-transition-strategy"
description: "Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_support_transition_strategy", "rar_sha256": "907e43dce00749fa5745c515c397950479e70455819b36cc102c5782aee02475", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_support_transition_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_support_transition_strategy_agent.py` and in the RCI capsule.

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

Develop support transition strategy Demo Data Generator — Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 907e43dce00749fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_support_transition_strategy_agent.py` first:

```bash
python3 demo_data_develop_support_transition_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_support_transition_strategy_agent.py   # or on stdin
python3 demo_data_develop_support_transition_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop support transition strategy Demo Data Generator — Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_support_transition_strategy',
    "version": '2.0.1',
    "display_name": 'Develop support transition strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-develop-support-transition-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0764a5b90b0e472e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/develop-support-transition-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-develop-support-transition-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopSupportTransitionStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSupportTransitionStrategy'
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
    print(DemoDataDevelopSupportTransitionStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
