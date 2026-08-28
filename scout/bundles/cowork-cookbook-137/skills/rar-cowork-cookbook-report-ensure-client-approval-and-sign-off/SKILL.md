---
name: "rar-cowork-cookbook-report-ensure-client-approval-and-sign-off"
description: "Builds a structured summary report of ensure client approval and sign-off activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_ensure_client_approval_and_sign_off", "rar_sha256": "b90d45cad92cfa811ebe91a356a9c64c8a29901133586b5e2b3604ea943f480d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_ensure_client_approval_and_sign_off`. The original RAPP
agent is preserved byte-for-byte in `report_ensure_client_approval_and_sign_off_agent.py` and in the RCI capsule.

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

Ensure client approval and sign-off Summary Report — Builds a structured summary report of ensure client approval and sign-off activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-ensure-client-approval-and-sign-off
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_ensure_client_approval_and_sign_off_agent.py` and embedded as the fenced Python below (sha256 b90d45cad92cfa81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_ensure_client_approval_and_sign_off_agent.py` first:

```bash
python3 report_ensure_client_approval_and_sign_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_ensure_client_approval_and_sign_off_agent.py   # or on stdin
python3 report_ensure_client_approval_and_sign_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Ensure client approval and sign-off Summary Report — Builds a structured summary report of ensure client approval and sign-off activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-ensure-client-approval-and-sign-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_ensure_client_approval_and_sign_off',
    "version": '2.0.0',
    "display_name": 'Ensure client approval and sign-off Summary Report',
    "description": 'Builds a structured summary report of ensure client approval and sign-off activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-ensure-client-approval-and-sign-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-ensure-client-approval-and-sign-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f757bd751ba425c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/ensure-client-approval-and-sign-off'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/report-ensure-client-approval-and-sign-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportEnsureClientApprovalAndSignOff(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEnsureClientApprovalAndSignOff'
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
    print(ReportEnsureClientApprovalAndSignOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
