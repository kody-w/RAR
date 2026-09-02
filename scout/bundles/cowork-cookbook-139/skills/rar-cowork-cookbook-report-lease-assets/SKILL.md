---
name: "rar-cowork-cookbook-report-lease-assets"
description: "Builds a structured summary report of lease assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_lease_assets", "rar_sha256": "5bb64e6ac01d714788f768099caa57c04483058d58ba26e154f94b6bc5d71de6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_lease_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-lease-assets:0a2c2803d85270a26c3375e48a05fc5b39b436f9460c84a1ec797d986cdd047f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_lease_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_lease_assets_agent.py` is
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

Lease assets Summary Report — Builds a structured summary report of lease assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-lease-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_lease_assets_agent.py` and embedded as the fenced Python below (sha256 5bb64e6ac01d7147…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_lease_assets_agent.py` first:

```bash
python3 report_lease_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_lease_assets_agent.py   # or on stdin
python3 report_lease_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lease assets Summary Report — Builds a structured summary report of lease assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-lease-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_lease_assets',
    "version": '2.0.0',
    "display_name": 'Lease assets Summary Report',
    "description": 'Builds a structured summary report of lease assets activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-lease-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-lease-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b4ed588bad8055b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/lease-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-lease-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportLeaseAssets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportLeaseAssets'
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
    print(ReportLeaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
