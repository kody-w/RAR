---
name: "rar-cowork-cookbook-report-inspect-manufactured-goods"
description: "Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_inspect_manufactured_goods", "rar_sha256": "ba895d6ea3f7082c3d5fc4b92d1d1f6af012810120f9dac144dcf43081e1cec9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_inspect_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `report_inspect_manufactured_goods_agent.py` and in the RCI capsule.

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
