---
name: "rar-cat-agent-skills-power-automate-desktop-assessment"
description: "Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_desktop_assessment", "rar_sha256": "6c1fa43efa6dfc4b2812aa7a445ddbbd121f75290f2dbfee020c30425e347d3b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.1.2", "author": "Ricardo Calejo", "tags": ["power_automate", "desktop_flows", "automation", "assessment", "governance"]}
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
