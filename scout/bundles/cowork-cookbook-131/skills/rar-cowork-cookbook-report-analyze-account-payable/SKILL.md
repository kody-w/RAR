---
name: "rar-cowork-cookbook-report-analyze-account-payable"
description: "Builds a structured summary report of analyze account payable activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_account_payable", "rar_sha256": "e33ed2a30a16c171f576e91458a5862a01208c50fb4737a180cb82bef63fa1d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_account_payable`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_account_payable_agent.py` and in the RCI capsule.

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

Analyze account payable Summary Report — Builds a structured summary report of analyze account payable activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-account-payable
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
      "type": "string"
    },
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 e33ed2a30a16c171…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_account_payable_agent.py` first:

```bash
python3 report_analyze_account_payable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_account_payable_agent.py   # or on stdin
python3 report_analyze_account_payable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze account payable Summary Report — Builds a structured summary report of analyze account payable activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-account-payable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_account_payable',
    "version": '2.0.0',
    "display_name": 'Analyze account payable Summary Report',
    "description": 'Builds a structured summary report of analyze account payable activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-analyze-account-payable',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-account-payable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec299e982b748756',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-account-payable'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-analyze-account-payable', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportAnalyzeAccountPayable(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeAccountPayable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ReportAnalyzeAccountPayable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
