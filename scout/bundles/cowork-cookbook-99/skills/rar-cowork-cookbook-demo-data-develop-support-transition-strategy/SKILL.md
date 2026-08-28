---
name: "rar-cowork-cookbook-demo-data-develop-support-transition-strategy"
description: "Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_support_transition_strategy", "rar_sha256": "cabfe29b2be8d0477d26830dc86952274222d4a4d0cc87c56d1c2eafc1e6e117", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 cabfe29b2be8d047…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_support_transition_strategy_agent.py` first:

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
    "version": '2.0.0',
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
