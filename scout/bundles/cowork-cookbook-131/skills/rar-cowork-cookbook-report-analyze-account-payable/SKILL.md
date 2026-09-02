---
name: "rar-cowork-cookbook-report-analyze-account-payable"
description: "Builds a structured summary report of analyze account payable activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_account_payable", "rar_sha256": "e33ed2a30a16c171f576e91458a5862a01208c50fb4737a180cb82bef63fa1d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_analyze_account_payable_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-analyze-account-payable:5767edc557010c64ecda99c0fee6c73dd97ec05d9dd304362bb5c1ca38d0935b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_analyze_account_payable`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_analyze_account_payable_agent.py` is
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
