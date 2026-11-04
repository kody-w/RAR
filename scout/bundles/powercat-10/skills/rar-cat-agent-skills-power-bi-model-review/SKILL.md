---
name: "rar-cat-agent-skills-power-bi-model-review"
description: "Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_bi_model_review", "rar_sha256": "d2a0cd620bbd24235f28f89f5f7fcdb1ebf7791ea5aaba31cf09e001caf52e86", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["power_bi", "dax", "semantic_model", "data", "review", "fabric"]}
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
