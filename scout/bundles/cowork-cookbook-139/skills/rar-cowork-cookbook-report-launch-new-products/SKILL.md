---
name: "rar-cowork-cookbook-report-launch-new-products"
description: "Builds a structured summary report of launch new products activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_launch_new_products", "rar_sha256": "55ec75f407b62140c98814ef880395df52216817e6b90f8e20fdc06edfc2d0ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 55ec75f407b62140…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_launch_new_products_agent.py` first:

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
    "version": '2.0.0',
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
