---
name: "rar-cowork-cookbook-demo-data-analyze-and-mitigate-risks"
description: "Generates and creates realistic demo records for analyze and mitigate risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_mitigate_risks", "rar_sha256": "583a9e85eaf017db6f0ebc7a81b3f8cf939cdd368bd514fbfc16665841f41bed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_and_mitigate_risks_agent.py` and embedded as the fenced Python below (sha256 583a9e85eaf017db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_and_mitigate_risks_agent.py` first:

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
    "version": '2.0.1',
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
