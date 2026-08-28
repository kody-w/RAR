---
name: "rar-cowork-cookbook-demo-data-analyze-and-mitigate-risks"
description: "Generates and creates realistic demo records for analyze and mitigate risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_mitigate_risks", "rar_sha256": "5eb1c5e06f064c416ee02de744bbb41e59cbabb54585f1f1c683f6abd3a76691", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_and_mitigate_risks`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_and_mitigate_risks_agent.py` and in the RCI capsule.

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

Analyze and mitigate risks Demo Data Generator — Generates and creates realistic demo records for analyze and mitigate risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-mitigate-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_and_mitigate_risks_agent.py` and embedded as the fenced Python below (sha256 5eb1c5e06f064c41…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_and_mitigate_risks_agent.py` first:

```bash
python3 demo_data_analyze_and_mitigate_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_and_mitigate_risks_agent.py   # or on stdin
python3 demo_data_analyze_and_mitigate_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and mitigate risks Demo Data Generator — Generates and creates realistic demo records for analyze and mitigate risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-mitigate-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_and_mitigate_risks',
    "version": '2.0.0',
    "display_name": 'Analyze and mitigate risks Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze and mitigate risks in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-analyze-and-mitigate-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-and-mitigate-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39964105afc8d539',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/analyze-and-mitigate-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-analyze-and-mitigate-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAnalyzeAndMitigateRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAndMitigateRisks'
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
    print(DemoDataAnalyzeAndMitigateRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
