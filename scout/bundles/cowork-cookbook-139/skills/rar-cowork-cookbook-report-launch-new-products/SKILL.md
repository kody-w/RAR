---
name: "rar-cowork-cookbook-report-launch-new-products"
description: "Builds a structured summary report of launch new products activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_launch_new_products", "rar_sha256": "645251e2c6dc8aa39b15de0c5e0e20f2721e49469d10f72d6906688224251167", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_launch_new_products`. The original RAPP
agent is preserved byte-for-byte in `report_launch_new_products_agent.py` and in the RCI capsule.

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

Launch new products Summary Report — Builds a structured summary report of launch new products activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-launch-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 645251e2c6dc8aa3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_launch_new_products_agent.py` first:

```bash
python3 report_launch_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_launch_new_products_agent.py   # or on stdin
python3 report_launch_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch new products Summary Report — Builds a structured summary report of launch new products activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-launch-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_launch_new_products',
    "version": '2.0.1',
    "display_name": 'Launch new products Summary Report',
    "description": 'Builds a structured summary report of launch new products activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-launch-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-launch-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4190f1ce49267b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/launch-new-products'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-launch-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportLaunchNewProducts(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportLaunchNewProducts'
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
    print(ReportLaunchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
