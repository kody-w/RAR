---
name: "rar-cowork-cookbook-report-ensure-client-approval-and-sign-off"
description: "Builds a structured summary report of ensure client approval and sign-off activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_ensure_client_approval_and_sign_off", "rar_sha256": "15601c2f6369c66d8c5d40335a2d4afe3b0b9821e3d531d1200bf52631775f47", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_ensure_client_approval_and_sign_off_agent.py` and embedded as the fenced Python below (sha256 15601c2f6369c66d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_ensure_client_approval_and_sign_off_agent.py` first:

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
    "version": '2.0.1',
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
