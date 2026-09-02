---
name: "rar-cat-agent-skills-power-bi-model-review"
description: "Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_bi_model_review", "rar_sha256": "29cae30baa09510e4c1adaf840d54147afc9476821ab7c5a1303194987097b7c", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "power_bi_model_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/power-bi-model-review:ef0aa495583f71977f1a5c79979d8e05a565ba5bf3c3f0e2588fdc287654ed16", "kind": "skill"}, "version": "2.0.0", "author": "Tim Karlsson", "tags": ["power_bi", "dax", "semantic_model", "data", "review", "fabric"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/power_bi_model_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `power_bi_model_review_agent.py` is
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

Power BI Model Review — Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-bi-model-review
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_bi_model_review_agent.py` and embedded as the fenced Python below (sha256 29cae30baa09510e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_bi_model_review_agent.py` first:

```bash
python3 power_bi_model_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_bi_model_review_agent.py   # or on stdin
python3 power_bi_model_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Power BI Model Review — Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-bi-model-review
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_bi_model_review',
    "version": '2.0.0',
    "display_name": 'Power BI Model Review',
    "description": 'Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged.',
    "author": 'Tim Karlsson',
    "tags": ['power_bi', 'dax', 'semantic_model', 'data', 'review', 'fabric'],
    "category": 'pipeline',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'power-bi-model-review',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-bi-model-review',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd7479319485ce4bf',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:review', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PowerBiModelReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerBiModelReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PowerBiModelReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
