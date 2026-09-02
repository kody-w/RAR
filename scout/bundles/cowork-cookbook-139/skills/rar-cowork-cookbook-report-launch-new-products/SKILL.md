---
name: "rar-cowork-cookbook-report-launch-new-products"
description: "Builds a structured summary report of launch new products activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_launch_new_products", "rar_sha256": "55ec75f407b62140c98814ef880395df52216817e6b90f8e20fdc06edfc2d0ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_launch_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-launch-new-products:86b5356d8205af6041eed476bdd9d01e991c6afeef1877ee00db577a7a990a86", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_launch_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_launch_new_products_agent.py` is
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
