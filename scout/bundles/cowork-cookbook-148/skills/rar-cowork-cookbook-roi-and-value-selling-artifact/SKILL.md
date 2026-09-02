---
name: "rar-cowork-cookbook-roi-and-value-selling-artifact"
description: "Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/roi_and_value_selling_artifact", "rar_sha256": "d4bf8fd4aa97770f8b9f268a6fef1aff49351f9ddd6309628e7c02d7f6f851d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "roi_and_value_selling_artifact_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/roi-and-value-selling-artifact:7f779b4b9b31a285ba5aaeaca708fe199d61aea6da54ca2bf164709779dd6b5a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/roi_and_value_selling_artifact`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `roi_and_value_selling_artifact_agent.py` is
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
