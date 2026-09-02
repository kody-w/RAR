---
name: "rar-cowork-cookbook-report-engage-in-conversations-with-customers"
description: "Builds a structured summary report of engage in conversations with customers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_engage_in_conversations_with_customers", "rar_sha256": "e3e00d706c0e802bf32a04de0d1b33a59972fc8f64464ce3d49fbaf5cce05f1d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_engage_in_conversations_with_customers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-engage-in-conversations-with-customers:eafdf6c42d6bd2f693c48b0532be283646e3846da8047f43ade8d146a1cb8778", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_engage_in_conversations_with_customers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_engage_in_conversations_with_customers_agent.py` is
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

Engage in conversations with customers Summary Report — Builds a structured summary report of engage in conversations with customers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-engage-in-conversations-with-customers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 e3e00d706c0e802b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_engage_in_conversations_with_customers_agent.py` first:

```bash
python3 report_engage_in_conversations_with_customers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_engage_in_conversations_with_customers_agent.py   # or on stdin
python3 report_engage_in_conversations_with_customers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engage in conversations with customers Summary Report — Builds a structured summary report of engage in conversations with customers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-engage-in-conversations-with-customers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_engage_in_conversations_with_customers',
    "version": '2.0.0',
    "display_name": 'Engage in conversations with customers Summary Report',
    "description": 'Builds a structured summary report of engage in conversations with customers activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-engage-in-conversations-with-customers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-engage-in-conversations-with-customers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af68f9e273ee7671',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/engage-in-conversations-with-customers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-engage-in-conversations-with-customers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportEngageInConversationsWithCustomers(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEngageInConversationsWithCustomers'
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
    print(ReportEngageInConversationsWithCustomers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
