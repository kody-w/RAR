---
name: "rar-cowork-cookbook-demo-data-develop-continuous-improvement-initiatives"
description: "Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives", "rar_sha256": "16da5c0953877283566e3c3a837d82aeae22aae2bf9fb641008e6ac28e124ef1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

Develop continuous improvement initiatives Demo Data Generator — Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 16da5c0953877283…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 demo_data_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 demo_data_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Demo Data Generator — Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives',
    "version": '2.0.0',
    "display_name": 'Develop continuous improvement initiatives Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1963f90b52570d0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopContinuousImprovementInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopContinuousImprovementInitiatives'
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
    print(DemoDataDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
