---
name: "rar-cowork-cookbook-roi-and-value-selling-artifact"
description: "Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/roi_and_value_selling_artifact", "rar_sha256": "328c4cf6dc3edc82223dc490e950980648a84136cbe85adecb39b6ebabac2cdb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/roi_and_value_selling_artifact`. The original RAPP
agent is preserved byte-for-byte in `roi_and_value_selling_artifact_agent.py` and in the RCI capsule.

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

ROI and value selling artifact — Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/roi-and-value-selling-artifact
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `roi_and_value_selling_artifact_agent.py` and embedded as the fenced Python below (sha256 328c4cf6dc3edc82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `roi_and_value_selling_artifact_agent.py` first:

```bash
python3 roi_and_value_selling_artifact_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 roi_and_value_selling_artifact_agent.py   # or on stdin
python3 roi_and_value_selling_artifact_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
ROI and value selling artifact — Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/roi-and-value-selling-artifact
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/roi_and_value_selling_artifact',
    "version": '2.0.1',
    "display_name": 'ROI and value selling artifact',
    "description": 'Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'roi-and-value-selling-artifact',
        "upstream_url": 'https://coworkcookbook.com/recipes/roi-and-value-selling-artifact',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22e4fe0ca920da55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/roi-and-value-selling-artifact', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RoiAndValueSellingArtifact(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RoiAndValueSellingArtifact'
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
    print(RoiAndValueSellingArtifact().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
