---
name: "rar-cowork-cookbook-report-inspect-manufactured-goods"
description: "Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_inspect_manufactured_goods", "rar_sha256": "ba895d6ea3f7082c3d5fc4b92d1d1f6af012810120f9dac144dcf43081e1cec9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_inspect_manufactured_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-inspect-manufactured-goods:35e79ac24f92b1adc78202a8d01041eed0668bc94a475c16551abe4fb81fd025", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_inspect_manufactured_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_inspect_manufactured_goods_agent.py` is
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

Inspect manufactured goods Summary Report — Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-inspect-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_inspect_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 ba895d6ea3f7082c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_inspect_manufactured_goods_agent.py` first:

```bash
python3 report_inspect_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_inspect_manufactured_goods_agent.py   # or on stdin
python3 report_inspect_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect manufactured goods Summary Report — Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-inspect-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_inspect_manufactured_goods',
    "version": '2.0.0',
    "display_name": 'Inspect manufactured goods Summary Report',
    "description": 'Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-inspect-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-inspect-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '466ad6fb0378e92f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/inspect-manufactured-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-inspect-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportInspectManufacturedGoods(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportInspectManufacturedGoods'
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
    print(ReportInspectManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
