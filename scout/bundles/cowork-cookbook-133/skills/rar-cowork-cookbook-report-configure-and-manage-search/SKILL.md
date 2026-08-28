---
name: "rar-cowork-cookbook-report-configure-and-manage-search"
description: "Builds a structured summary report of configure and manage search activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_search", "rar_sha256": "69cddb2f6273fc0e507243625f1108a1f6cb204aff50f98eacc4f634ad13c248", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_search_agent.py` and embedded as the fenced Python below (sha256 69cddb2f6273fc0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_search_agent.py` first:

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
    "version": '2.0.0',
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
