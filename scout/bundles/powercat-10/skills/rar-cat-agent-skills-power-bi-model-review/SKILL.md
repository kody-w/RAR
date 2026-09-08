---
name: "rar-cat-agent-skills-power-bi-model-review"
description: "Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_bi_model_review", "rar_sha256": "e64985886d803c3a693e66c6c88de9e55e8272a0255c7f5e47df71428d507619", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["power_bi", "dax", "semantic_model", "data", "review", "fabric"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/power_bi_model_review`. The original RAPP
agent is preserved byte-for-byte in `power_bi_model_review_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_bi_model_review_agent.py` and embedded as the fenced Python below (sha256 e64985886d803c3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_bi_model_review_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
