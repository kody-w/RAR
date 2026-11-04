---
name: "rar-cat-agent-skills-regulation-monitor"
description: "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/regulation_monitor", "rar_sha256": "ce654fcd227627fd462961af89fec4cb8c416bc90754779e76bfa97cde0fbd2b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["regulation", "monitoring", "compliance", "dashboard", "research"]}
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
