---
name: "rar-cat-agent-skills-power-automate-desktop-assessment"
description: "Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_desktop_assessment", "rar_sha256": "6c1fa43efa6dfc4b2812aa7a445ddbbd121f75290f2dbfee020c30425e347d3b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Ricardo Calejo", "tags": ["power_automate", "desktop_flows", "automation", "assessment", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/power_automate_desktop_assessment`. The original RAPP
agent is preserved byte-for-byte in `power_automate_desktop_assessment_agent.py` and in the RCI capsule.

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

Power Automate Desktop Assessment — Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment
  Upstream author: Ricardo Calejo
  Upstream version: 1.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_desktop_assessment_agent.py` and embedded as the fenced Python below (sha256 6c1fa43efa6dfc4b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_desktop_assessment_agent.py` first:

```bash
python3 power_automate_desktop_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_automate_desktop_assessment_agent.py   # or on stdin
python3 power_automate_desktop_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/power_automate_desktop_assessment_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/power_automate_desktop_assessment_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/power_automate_desktop_assessment/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Power Automate Desktop Assessment — Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment
  Upstream author: Ricardo Calejo
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_automate_desktop_assessment',
    "version": '3.1.2',
    "display_name": 'Power Automate Desktop Assessment',
    "description": 'Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.',
    "author": 'Ricardo Calejo',
    "tags": ['power_automate', 'desktop_flows', 'automation', 'assessment', 'governance'],
    "category": 'analysis',
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
        "upstream_slug": 'power-automate-desktop-assessment',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd026e3d4a8378798',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'word:assess'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PowerAutomateDesktopAssessment(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerAutomateDesktopAssessment'
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
    print(PowerAutomateDesktopAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
