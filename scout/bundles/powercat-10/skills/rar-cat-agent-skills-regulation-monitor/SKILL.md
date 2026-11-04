---
name: "rar-cat-agent-skills-regulation-monitor"
description: "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/regulation_monitor", "rar_sha256": "ce654fcd227627fd462961af89fec4cb8c416bc90754779e76bfa97cde0fbd2b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["regulation", "monitoring", "compliance", "dashboard", "research"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `regulation_monitor_agent.py` and embedded as the fenced Python below (sha256 ce654fcd227627fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `regulation_monitor_agent.py` first:

```bash
python3 regulation_monitor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 regulation_monitor_agent.py   # or on stdin
python3 regulation_monitor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/regulation_monitor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/regulation_monitor_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/regulation_monitor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
