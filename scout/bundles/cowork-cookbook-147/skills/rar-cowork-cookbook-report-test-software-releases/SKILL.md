---
name: "rar-cowork-cookbook-report-test-software-releases"
description: "Builds a structured summary report of test software releases activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_software_releases", "rar_sha256": "4d36f0465635e3d084653670a5da1717bf86752e61e86c43785311cc023311db", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_test_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-test-software-releases:7a1514d4a6bac420229085c9514f3d03840b8eed3bc84038c802e27565c824bb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_test_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_test_software_releases_agent.py` is
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

Test software releases Summary Report — Builds a structured summary report of test software releases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 4d36f0465635e3d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_software_releases_agent.py` first:

```bash
python3 report_test_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_software_releases_agent.py   # or on stdin
python3 report_test_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test software releases Summary Report — Builds a structured summary report of test software releases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_software_releases',
    "version": '2.0.0',
    "display_name": 'Test software releases Summary Report',
    "description": 'Builds a structured summary report of test software releases activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-test-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f20dd5b4d9c1733',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/test-software-releases'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-test-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTestSoftwareReleases(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestSoftwareReleases'
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
    print(ReportTestSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
