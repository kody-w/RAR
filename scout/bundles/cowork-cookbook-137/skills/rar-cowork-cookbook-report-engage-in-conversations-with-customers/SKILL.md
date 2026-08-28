---
name: "rar-cowork-cookbook-report-engage-in-conversations-with-customers"
description: "Builds a structured summary report of engage in conversations with customers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_engage_in_conversations_with_customers", "rar_sha256": "e3e00d706c0e802bf32a04de0d1b33a59972fc8f64464ce3d49fbaf5cce05f1d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_engage_in_conversations_with_customers`. The original RAPP
agent is preserved byte-for-byte in `report_engage_in_conversations_with_customers_agent.py` and in the RCI capsule.

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
