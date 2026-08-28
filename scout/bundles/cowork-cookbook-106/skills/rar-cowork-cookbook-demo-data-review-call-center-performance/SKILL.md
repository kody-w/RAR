---
name: "rar-cowork-cookbook-demo-data-review-call-center-performance"
description: "Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_call_center_performance", "rar_sha256": "c13299cb7d6bdf2856a4c0ee5d23501e83566d926b17c34acf077723b0d73b85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_review_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_review_call_center_performance_agent.py` and in the RCI capsule.

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

Review call center performance Demo Data Generator — Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 c13299cb7d6bdf28…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_call_center_performance_agent.py` first:

```bash
python3 demo_data_review_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_review_call_center_performance_agent.py   # or on stdin
python3 demo_data_review_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review call center performance Demo Data Generator — Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_review_call_center_performance',
    "version": '2.0.0',
    "display_name": 'Review call center performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-review-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-review-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '106101c3cb43cd0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-call-center-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-review-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReviewCallCenterPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReviewCallCenterPerformance'
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
    print(DemoDataReviewCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
