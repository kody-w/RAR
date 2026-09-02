---
name: "rar-cowork-cookbook-report-manage-customer-holds"
description: "Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_customer_holds", "rar_sha256": "e619196bde9c02cce00ac58b69095b4b085533b786970888f226add964edabed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_customer_holds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-customer-holds:e0f3c3bdbcba5843d8fdad6af5cc9feb87f674e73817a13e021e3f8b7ff2bcd6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_customer_holds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_customer_holds_agent.py` is
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

Manage customer holds Summary Report — Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 e619196bde9c02cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_customer_holds_agent.py` first:

```bash
python3 report_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_customer_holds_agent.py   # or on stdin
python3 report_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Summary Report — Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_customer_holds',
    "version": '2.0.0',
    "display_name": 'Manage customer holds Summary Report',
    "description": 'Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '077655d5f62ce28c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageCustomerHolds(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCustomerHolds'
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
    print(ReportManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
