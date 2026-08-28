---
name: "rar-cat-agent-skills-regulation-monitor"
description: "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/regulation_monitor", "rar_sha256": "094fa86c7092388fb65e3ce1e381c016d4d8b9fb2ddcdb92be6e720016a6b0e7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Jagmeet Chabra", "tags": ["regulation", "monitoring", "compliance", "dashboard", "research"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `regulation_monitor_agent.py` and embedded as the fenced Python below (sha256 094fa86c7092388f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `regulation_monitor_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
