---
name: "rar-cat-agent-skills-regulation-monitor"
description: "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/regulation_monitor", "rar_sha256": "094fa86c7092388fb65e3ce1e381c016d4d8b9fb2ddcdb92be6e720016a6b0e7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "regulation_monitor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/regulation-monitor:fe537b4039edbbf4a465087fc1250ec3d47330c27a5714b1898d6dc99055f9da", "kind": "skill"}, "version": "2.0.0", "author": "Jagmeet Chabra", "tags": ["regulation", "monitoring", "compliance", "dashboard", "research"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/regulation_monitor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `regulation_monitor_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
