---
name: "rar-cowork-cookbook-demo-data-review-call-center-performance"
description: "Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_call_center_performance", "rar_sha256": "c13299cb7d6bdf2856a4c0ee5d23501e83566d926b17c34acf077723b0d73b85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_review_call_center_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-review-call-center-performance:d7a9ed390c26d929b48be21d2a43957f03e401b7496f27e92090aa7f70c9f774", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_review_call_center_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_review_call_center_performance_agent.py` is
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
