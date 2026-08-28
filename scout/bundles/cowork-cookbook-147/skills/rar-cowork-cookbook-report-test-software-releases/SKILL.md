---
name: "rar-cowork-cookbook-report-test-software-releases"
description: "Builds a structured summary report of test software releases activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_software_releases", "rar_sha256": "2f6f5813a2717b8ff0b6e5964e50dce6fb2ec77a9b04b72066fe7724708ee48c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_software_releases`. The original RAPP
agent is preserved byte-for-byte in `report_test_software_releases_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 2f6f5813a2717b8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_software_releases_agent.py` first:

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
    "version": '2.0.1',
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
