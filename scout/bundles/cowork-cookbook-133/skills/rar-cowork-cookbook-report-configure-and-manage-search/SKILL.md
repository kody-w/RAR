---
name: "rar-cowork-cookbook-report-configure-and-manage-search"
description: "Builds a structured summary report of configure and manage search activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_search", "rar_sha256": "69cddb2f6273fc0e507243625f1108a1f6cb204aff50f98eacc4f634ad13c248", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_configure_and_manage_search_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-configure-and-manage-search:fe5314ea9dcdc4180435e484941e9e1a419f5b48d829e5819600f1d086ccafe9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_configure_and_manage_search`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_configure_and_manage_search_agent.py` is
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
