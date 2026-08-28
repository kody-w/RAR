---
name: "rar-cowork-cookbook-report-configure-and-manage-search"
description: "Builds a structured summary report of configure and manage search activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_search", "rar_sha256": "38a3137ffc78ce703e57fb84122a8d2e9949da83cb48d6b4b95ca4c1caf4b061", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_search`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_search_agent.py` and in the RCI capsule.

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

Configure and manage search Summary Report — Builds a structured summary report of configure and manage search activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-search
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_search_agent.py` and embedded as the fenced Python below (sha256 38a3137ffc78ce70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_search_agent.py` first:

```bash
python3 report_configure_and_manage_search_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_search_agent.py   # or on stdin
python3 report_configure_and_manage_search_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage search Summary Report — Builds a structured summary report of configure and manage search activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-search
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_search',
    "version": '2.0.1',
    "display_name": 'Configure and manage search Summary Report',
    "description": 'Builds a structured summary report of configure and manage search activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-configure-and-manage-search',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-search',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0d81884e9e3bf4f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-search'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-search', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConfigureAndManageSearch(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageSearch'
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
    print(ReportConfigureAndManageSearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
