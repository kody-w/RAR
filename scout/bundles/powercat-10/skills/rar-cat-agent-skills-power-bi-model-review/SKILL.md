---
name: "rar-cat-agent-skills-power-bi-model-review"
description: "Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_bi_model_review", "rar_sha256": "e64985886d803c3a693e66c6c88de9e55e8272a0255c7f5e47df71428d507619", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["power_bi", "dax", "semantic_model", "data", "review", "fabric"]}
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
