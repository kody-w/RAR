---
name: "rar-cat-agent-skills-regulation-monitor"
description: "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/regulation_monitor", "rar_sha256": "71a681e76f421b7dd2588d5388df0c864edcc7661eb979212c188cd6dcbde484", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["regulation", "monitoring", "compliance", "dashboard", "research"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/regulation_monitor`. The original RAPP
agent is preserved byte-for-byte in `regulation_monitor_agent.py` and in the RCI capsule.

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

Regulation Monitor — Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#regulation-monitor
  Upstream author: Jagmeet Chabra
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `regulation_monitor_agent.py` and embedded as the fenced Python below (sha256 71a681e76f421b7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `regulation_monitor_agent.py` first:

```bash
python3 regulation_monitor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 regulation_monitor_agent.py   # or on stdin
python3 regulation_monitor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Regulation Monitor — Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#regulation-monitor
  Upstream author: Jagmeet Chabra
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/regulation_monitor',
    "version": '3.0.2',
    "display_name": 'Regulation Monitor',
    "description": "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind…",
    "author": 'Jagmeet Chabra',
    "tags": ['regulation', 'monitoring', 'compliance', 'dashboard', 'research'],
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
        "upstream_slug": 'regulation-monitor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#regulation-monitor',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '455a25cb3f6e394c',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.286, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class RegulationMonitor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RegulationMonitor'
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
    print(RegulationMonitor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
