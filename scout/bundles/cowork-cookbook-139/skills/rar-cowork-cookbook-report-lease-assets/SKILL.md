---
name: "rar-cowork-cookbook-report-lease-assets"
description: "Builds a structured summary report of lease assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_lease_assets", "rar_sha256": "5bb64e6ac01d714788f768099caa57c04483058d58ba26e154f94b6bc5d71de6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_lease_assets`. The original RAPP
agent is preserved byte-for-byte in `report_lease_assets_agent.py` and in the RCI capsule.

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
