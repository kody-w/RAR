---
name: "rar-cat-agent-skills-power-bi-model-review"
description: "Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_bi_model_review", "rar_sha256": "d2a0cd620bbd24235f28f89f5f7fcdb1ebf7791ea5aaba31cf09e001caf52e86", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["power_bi", "dax", "semantic_model", "data", "review", "fabric"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_bi_model_review_agent.py` and embedded as the fenced Python below (sha256 d2a0cd620bbd2423…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_bi_model_review_agent.py` first:

```bash
python3 power_bi_model_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_bi_model_review_agent.py   # or on stdin
python3 power_bi_model_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/power_bi_model_review_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/power_bi_model_review_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/power_bi_model_review/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
