---
name: "rar-cowork-cookbook-roi-and-value-selling-artifact"
description: "Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/roi_and_value_selling_artifact", "rar_sha256": "d4bf8fd4aa97770f8b9f268a6fef1aff49351f9ddd6309628e7c02d7f6f851d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `roi_and_value_selling_artifact_agent.py` and embedded as the fenced Python below (sha256 d4bf8fd4aa97770f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `roi_and_value_selling_artifact_agent.py` first:

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
    "version": '2.0.0',
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
