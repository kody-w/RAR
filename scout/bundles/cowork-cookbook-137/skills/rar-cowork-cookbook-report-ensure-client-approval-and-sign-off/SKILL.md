---
name: "rar-cowork-cookbook-report-ensure-client-approval-and-sign-off"
description: "Builds a structured summary report of ensure client approval and sign-off activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_ensure_client_approval_and_sign_off", "rar_sha256": "b90d45cad92cfa811ebe91a356a9c64c8a29901133586b5e2b3604ea943f480d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_ensure_client_approval_and_sign_off_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-ensure-client-approval-and-sign-off:d8059c0ee96dbd7ba274797e947a3f2fa9b778446a7d8f1dff4d595b6bdb6d18", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_ensure_client_approval_and_sign_off`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_ensure_client_approval_and_sign_off_agent.py` is
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
