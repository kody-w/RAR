---
name: "rar-cowork-cookbook-report-analyze-account-payable"
description: "Builds a structured summary report of analyze account payable activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_account_payable", "rar_sha256": "9e100481aa8459188d6ca98e419cc4d88291edba2e8977749c0bcce6d31445f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 9e100481aa845918…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_account_payable_agent.py` first:

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
    "version": '2.0.1',
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
