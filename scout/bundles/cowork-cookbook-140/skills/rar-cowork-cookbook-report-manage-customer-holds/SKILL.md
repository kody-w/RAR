---
name: "rar-cowork-cookbook-report-manage-customer-holds"
description: "Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_customer_holds", "rar_sha256": "e619196bde9c02cce00ac58b69095b4b085533b786970888f226add964edabed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_customer_holds_agent.py` and in the RCI capsule.

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
