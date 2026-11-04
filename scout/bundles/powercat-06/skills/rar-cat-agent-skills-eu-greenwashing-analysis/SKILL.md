---
name: "rar-cat-agent-skills-eu-greenwashing-analysis"
description: "Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/eu_greenwashing_analysis", "rar_sha256": "6200a163f12cc7b5b12ef9742949a0bfe927e668231f5965e68fcd1f77cb7238", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Remi Dyon", "tags": ["compliance", "sustainability", "greenwashing", "eu_regulation", "marketing_review", "esg"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eu_greenwashing_analysis_agent.py` and embedded as the fenced Python below (sha256 6200a163f12cc7b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eu_greenwashing_analysis_agent.py` first:

```bash
python3 eu_greenwashing_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eu_greenwashing_analysis_agent.py   # or on stdin
python3 eu_greenwashing_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/eu_greenwashing_analysis_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/eu_greenwashing_analysis_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/eu_greenwashing_analysis/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
