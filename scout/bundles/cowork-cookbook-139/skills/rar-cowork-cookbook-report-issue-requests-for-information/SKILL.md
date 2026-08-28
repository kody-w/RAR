---
name: "rar-cowork-cookbook-report-issue-requests-for-information"
description: "Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_issue_requests_for_information", "rar_sha256": "0c27848498550aad395aa68fe53103c48a8b87b4c925f7641189692e07c9537b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_issue_requests_for_information`. The original RAPP
agent is preserved byte-for-byte in `report_issue_requests_for_information_agent.py` and in the RCI capsule.

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

Issue requests for information Summary Report — Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-issue-requests-for-information
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 0c27848498550aad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_issue_requests_for_information_agent.py` first:

```bash
python3 report_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_issue_requests_for_information_agent.py   # or on stdin
python3 report_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Summary Report — Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-issue-requests-for-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_issue_requests_for_information',
    "version": '2.0.0',
    "display_name": 'Issue requests for information Summary Report',
    "description": 'Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-issue-requests-for-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-issue-requests-for-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34399004cb5965ac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-information'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-issue-requests-for-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportIssueRequestsForInformation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIssueRequestsForInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportIssueRequestsForInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
