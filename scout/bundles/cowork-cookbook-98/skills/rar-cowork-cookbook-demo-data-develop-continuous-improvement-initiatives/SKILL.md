---
name: "rar-cowork-cookbook-demo-data-develop-continuous-improvement-initiatives"
description: "Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives", "rar_sha256": "16da5c0953877283566e3c3a837d82aeae22aae2bf9fb641008e6ac28e124ef1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_continuous_improvement_initiatives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-continuous-improvement-initiatives:279a70733f128d17d0f26db07caf44b1b6cbfe16176fe538eff6ae2ff82eb44f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_continuous_improvement_initiatives_agent.py` is
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
