---
name: "rar-cowork-cookbook-report-engage-in-conversations-with-customers"
description: "Builds a structured summary report of engage in conversations with customers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_engage_in_conversations_with_customers", "rar_sha256": "206cf7cc1709c9ef71b9380b6574f43d84c95b2e36370713461d1e9db48328a0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 206cf7cc1709c9ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_engage_in_conversations_with_customers_agent.py` first:

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
    "version": '2.0.1',
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
