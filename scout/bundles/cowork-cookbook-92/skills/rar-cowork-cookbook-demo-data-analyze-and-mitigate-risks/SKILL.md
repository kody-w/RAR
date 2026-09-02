---
name: "rar-cowork-cookbook-demo-data-analyze-and-mitigate-risks"
description: "Generates and creates realistic demo records for analyze and mitigate risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_mitigate_risks", "rar_sha256": "5eb1c5e06f064c416ee02de744bbb41e59cbabb54585f1f1c683f6abd3a76691", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_and_mitigate_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-and-mitigate-risks:084969280889e6b254f771ca0323d3004c36eeb5bd4cc69b99bd26d55484c00e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_and_mitigate_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_and_mitigate_risks_agent.py` is
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
