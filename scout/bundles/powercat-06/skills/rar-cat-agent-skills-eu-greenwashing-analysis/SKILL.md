---
name: "rar-cat-agent-skills-eu-greenwashing-analysis"
description: "Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/eu_greenwashing_analysis", "rar_sha256": "6200a163f12cc7b5b12ef9742949a0bfe927e668231f5965e68fcd1f77cb7238", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Remi Dyon", "tags": ["compliance", "sustainability", "greenwashing", "eu_regulation", "marketing_review", "esg"]}
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
