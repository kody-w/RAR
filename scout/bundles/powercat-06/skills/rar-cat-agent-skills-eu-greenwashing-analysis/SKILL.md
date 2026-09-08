---
name: "rar-cat-agent-skills-eu-greenwashing-analysis"
description: "Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/eu_greenwashing_analysis", "rar_sha256": "a134c53dbb6e99e2879716f7e8341eef10280ddd10792464cf9fae79edeb6b59", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Remi Dyon", "tags": ["compliance", "sustainability", "greenwashing", "eu_regulation", "marketing_review", "esg"]}
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
