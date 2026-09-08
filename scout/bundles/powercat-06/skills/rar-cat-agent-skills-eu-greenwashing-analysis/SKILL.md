---
name: "rar-cat-agent-skills-eu-greenwashing-analysis"
description: "Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/eu_greenwashing_analysis", "rar_sha256": "a134c53dbb6e99e2879716f7e8341eef10280ddd10792464cf9fae79edeb6b59", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Remi Dyon", "tags": ["compliance", "sustainability", "greenwashing", "eu_regulation", "marketing_review", "esg"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/eu_greenwashing_analysis`. The original RAPP
agent is preserved byte-for-byte in `eu_greenwashing_analysis_agent.py` and in the RCI capsule.

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

EU Greenwashing Analysis — Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#eu-greenwashing-analysis
  Upstream author: Remi Dyon
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eu_greenwashing_analysis_agent.py` and embedded as the fenced Python below (sha256 a134c53dbb6e99e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eu_greenwashing_analysis_agent.py` first:

```bash
python3 eu_greenwashing_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eu_greenwashing_analysis_agent.py   # or on stdin
python3 eu_greenwashing_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
EU Greenwashing Analysis — Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#eu-greenwashing-analysis
  Upstream author: Remi Dyon
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/eu_greenwashing_analysis',
    "version": '3.0.2',
    "display_name": 'EU Greenwashing Analysis',
    "description": 'Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections.',
    "author": 'Remi Dyon',
    "tags": ['compliance', 'sustainability', 'greenwashing', 'eu_regulation', 'marketing_review', 'esg'],
    "category": 'general',
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
        "upstream_slug": 'eu-greenwashing-analysis',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#eu-greenwashing-analysis',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd9597c05205098f3',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class EuGreenwashingAnalysis(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EuGreenwashingAnalysis'
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
    print(EuGreenwashingAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
