---
name: "rar-cowork-cookbook-report-issue-requests-for-information"
description: "Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_issue_requests_for_information", "rar_sha256": "eb04e1e9bce59cb627db433b5e1e6b478b39949f502ea9c0932e751cfe1a1ccb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 eb04e1e9bce59cb6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_issue_requests_for_information_agent.py` first:

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
    "version": '2.0.1',
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
