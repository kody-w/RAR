---
name: "rar-cat-agent-skills-regulation-monitor"
description: "Configure once, then on a schedule sweeps a locked list of authoritative sources (auto-discovered at setup, confirmed by the user) plus any user-supplied seeds. Classifies each item, flags items relevant to the user's team using a light WorkIQ-derived profile, and renders a self-contained HTML dashboard. A tightly-bounded fallback web search is used only when a locked source is silent in the wind\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/regulation_monitor", "rar_sha256": "71a681e76f421b7dd2588d5388df0c864edcc7661eb979212c188cd6dcbde484", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["regulation", "monitoring", "compliance", "dashboard", "research"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/+16W7Ob1rbmX1Gv/WDnYC/uF3nXrmqEEAiBxEVCSHHK4Q7iKm4CcvLfeyJpLTsnye7TVf3QDy27EiTmHOMb129M8G8vdttERfXy5UWyw8z3mxkX2U5lv3x68fzareKyiYsc3OaKPIjDtvJnRe76n2ZN5OfgcmbPajfyvTb1Z/XN98sa/JIWbuJ7szSum1kRzB4q4sZu4g6sKtrK9evZR/Bz8dmLa7fo/Aost5tZ7Tdt+WnmTrqqDPzmDJOiWVv71U+zMm2B9Hy4f/1ct2WZxmBN7fte/TrjUruu4yAGon3bjWZx42efZkFqh/X9up5Vfup3dt7MmuJd6od61vh2Bq7jPJygx2HUzI5Flay1z55fAcTerKyKIE6B0XbuASk5+H0ys/bT4DPA2thxDlaJe0WeeXYdOYVdea8zdtZMwtLhs1O0YI83C+w0dWw3md18B+y2qwlmPeHwgCvTYXabnPruv4enphU10A5wx/kd9y3Ova8thmAUiJLf21mZ+vXLl59/+fQSg+uXL7+9uJMzQNR0P2xTewqhUuRxAwL96SW18xDcKgcQlRx8L/0qKKoM/OT5wez57eNk3KfZf/xHcrOrsP7py9d89vx8fZn+6O0DTFPYdQPAunZpO3EaNwOwPL3Zw+Tvpq3yu6eaCrj39bHzu6SinP1ruvfxoeQ19JuPX18KAOEO+evLT7OiAvqqdrp+naSUH396TYubX3386bucunUuvttMwgDq12/P70+xYOH3pXEw+2aoPPfUVfluXPpA+A/2TZ8H9Ke4p0u+PRZ/LECG/rXkyZ5/AbyPynGA3L8WC3wAdr68Xoo4//jUUYEqyG1QWh9/+juxoM7cZCqq/5bcnx+CI98G6frx6ZKfPt3D98sMetr2LvPv1ZYgYf5PLAHL39S9O+rvZN8j+19Ep6Ca6vdY/qW4v9oA/Wv289/a9u82gCbx9WXpp6DUK9tJ/S+z3+4p8vMH7/uPH375HYj+34ox7iU7SfiW2Xkc+HXz7dvPHx6V/OGXnz+0Jchi0HC+tVX6VzL/yq93PX/w4HPVxz/uBfoPeZIXN9CY32po9ltR/o/q99eZaaex9/33+svsx0qcPtBsMuJN6cMFP1RjDbD+4MefXn4H7SYH1rTu/TboH//4x0yJ3aqoi6CZGW7RNjMQ4CbO/An8PgKdDPydukblA7/WMXDscx3I/ynCE2LAGL/+T9duPtshaHqf6yRO0xqu3jvZt+zRyn59ne2BKMAsYZzb6UxnVfVrft80qSkrH/T37k4ijf8ZVPDn6WJqor/+Wdi3+77Xcvj13uSfnVbn1lNjqwG7vU4mHKf+/ADs2vnM7323BSJBvwb6J4qoPwHT6iIFPNdM5t7Bz7wYtA6gZHgQSJt/mYT9+uuvDmCLr/mjE+OzB90CU9v8Hc7s82dgSHCnpa+570bF7MNvv3+Y/efs3+26C590qIAGng4HCCVjt52BAmozsAzEAkQPdIe7w3/7/elOICb3qxkIz4NLp80gAQEfvfnWENnPGEnNHB/4FPgzK4uqmdgzbl5n62D2jhconW5NBBAVYBTw/HLiztydSN0G5rx7Mi8A94N41MHwaaLDu9ZfwRhyh5iBSrabX2cKpwK6KdKJv6sn/YDNIIDA/e+Rz3/k9sWbiNfZdkq5WWlXdhlV9lNHYD/iAmjmbTsQbs9y//Y1n8jUn1x1z5SHe8Ai4Bn3GdLPU8zBuJKBYvfqN933NfZEivs7OVZf8/qZ23Y1heI+8QyzsI29qeP/85lSdVS0qXf3H0A6SXpGwXtG5Z6D3yl99uT02TQMoMTs/49o/w+OaFPIWEHQeYHd88sZv93rp0cqTbCmLW++H2agnh5t4/sw9dYw33jja57GoC6q4Z+PlfcEfK559OJ2CpTO6rM3s6u73HtxTsVWVZP/7a/5G0EBn83u3RikytMs4P03hdPdN6QR8Nz0/fuwck/mypu8DgpwVrZOCoojAOG+O7GJqqnBPPMTVKo/JdstioFXf7RqBqSDggDyp3yNQcsAJHbP9m0BzARhD6oi+748njIFoPBaF6CNQG6+zo6gR0x1UoPGBCbEaQ3wwoe7qFnmAx8DiO8eriO7fIABefQG0J54KfZvP/r/eet7Td+RTOCBTNuzG+DJ28Qqnt8/4vqO8hkpIDSbutB90x+D/bR09iOP/vNrfkf4TmSguaXTCPKDa0BBVFl9z/WpN9egv2b+M33eyvf1MTA8JpJ3LF9mHLufsY9GfmfW2cfsjbPv9H74Y0y+zKKmKesvMPy+7DWMm6h1XuMC/hNN/+M7tX5+UusfhD7s/zL742nzD0ueufhlhr4ir8h0S45df0q25+fLrM3fO+PHH66fsbrHwvc+gS4+tXyQKVNa1qAF/vRsoO/BnBpcBtBOPh6mVvbGpm9LAKWGwKRp8YNd64mUpyZwlw3c/TV/D/izGABb5eE0CtTFD0V6HytA+J4t44317m0D6PamSTP0X6cD2mRu7b98yds0/fSS25n/N0e5ic1AGgKHTYc+UBBgWGti//4NGAJuxPZ0/cej/O5+YaePdK0bgAx0wzurPtLfDu+s+Wma1HPQMKbz1kTZj94GTol2mzYT0mYoJ2iP4900EL5Pi3/Weq9PoMMrvkxl+mk2TfaASN6G9E+zt2PTJNnPW3Ai/Xk6IEx2gqXgf+9r359OOP7LL38B43le+BsQ8dQipqbyMPd74tiPSJV2A9rcQZcBpMK9D0vTgFAP90Hiz2YDhZV/bcFE4E2Qv/vgO7Tigef3uynN47j928tbB3kG7zkAg+WgVD/X00wAgxoACsH3R/aBe/+d0fi5BTQ5MKiBPTRqUwzq01RAYKhDex5GMoxH4uA/AeIyFOF7rktTFOo7c3qOoZiLMozrUZ7reD7BEEDeI22/TbNOPMEg53SAzOdYQKAY4oGcwAjPYyiGckkaQ+y5Y5MOObed71sTUJdP2x62TI57n9InHzxN/O3FoQiwUiTqNfv4cDCE2jBBX5rKgnAEXmxy+ORcMHsrZBufxr11qW6lBpO3PJo3N2xz9UWDz5BxjdQb44RbAjtoERSOOBvICazREanVQyDvJDlZHVpWiIlbk5x8kWQ8vEsUKr7KeuOVh8wyqEE5BDE60Lfi0nVwm/srMbFprLwspFV+jc/uqjUJaqfd4rOTmvaZz+3OFPJe4lrjSB43+1Wdx9VRS736qF/qdefuiuKykepsw/WMubpmqIFz2ZLw1tIV7c0x0TmbTLz8iuwaiSuqpbQ/HE9muXNFOC+jKy0rW+V8Ks21E/f+uVnZ3fagVdlxWHlZgfNQo4AbcFNviv0Wl3A2tbYrWTQvYerBcc3csLK6eI5EE+24wyoVhZIhWV5MyciOu1rJyDPJxQmZNwpWudVxNV+axhm9oAvYh1VeTg5X2tIto5QFgi8o/nzyZdNcRXtgpFI3R6VKTJ+2OEdI1/tDQ5XLRepFC1rJyouKMaWQCf2u2x93fjtH8ZyCrQDe9aUXBDQ5dzu1mlMMvDIYWJW3c28eM5rdGYZiW+duvt46t8JruH0sya23PquugjfJqsxP/EIH47pwTHYj3LNYRswX7O7ar6ykaNvKRlcdJi9O9FHuh0S4KUed3HmVZG0g09tzx3DFNL0pnpZM78uI19kjhiuLdB6RVmdyhG45i/5QxodxiXMMdjWpg1ETxxOWNw2n1eUi032yCC+OM5oK5lFqKOjjepscym0VjSOl6pTScdBNzVPKOeWuW3EJUYukLXmLMcY5pfc8Z7ExSjdujpu4w7as44i0Etbm7ubsy+tSaPG6M+y1KJ22WiZ5aNVgo52Tfb1CkFREDuw1UQhNStWSFEI1G7YanhfwtilWKLIMl4WD79uE2gIMNY2NJ3FPO4phDxoqLrsEGiDtehhQeq3ut2MuHc7jFW6OkkOvjHV6KfXTXomsrllXi+M57j3LYTTTwMn5lVYUzBn3sZHWtXXeX9S5jN6asbaObaOq8oCdD9121R4pNLbMW4ak2C2N/OPZxKBzX6zBOEByQiXPV20Qw5Cekaixr8aTcb2YYiTGTkxCosMEHcHgFhTxB3NYwZAdDxdBuHFrM5mfcxfklrY5jIlRMyUdh5Cssu0uW99ksRch0VqmV+OkQby5PPVtvsfqiBpSqd42yWaZ0v1CIF2oR5PBWfbXYHGL1SbfBBu1XirnTjLWZLy6HVlO0H2TIli2PO1Cc51pCLPSBEhnmjQ/yXJphS2d+AhBRKwf+5f2FCsy33Q00p4ksgLdMnc3zs0L8DG+2MqY1vyZGNk8k7Is0KJlgLLwgrKtbH+rbTLLV/bhfHXGbSftCxjrlJHCBXQnRuOh29HC2aMPochBy2YMwpPs787C2mdvjlMeUbk+8Qjnq9WRXm8gYWeaogFx2tqIsGifaXy3sYSTeMWwOSb7prSMvN0VXZdaxGadmjNbqnCGehsfWhMnV0Y8OLZRSVVeL+D5cqQyUY7c+Njs84HTM7HwoU1VRpcVEUHRIUb3F69HYGRhrJN0G1sY6USHrR2MioBm9Fq4iUfLOVb2mMWcfiL8NceeaVer9ofs7JPXXBfkSClvSr5an/CzZS79krbw/UkZfJUWTKHEgl0gyuNxLnTe3sdvVM3TZ7Ui1OUGVfR4C/PyBu89DTvOrzVWcslhrgWiSl7QHO9iR3JixU6LESmKvoyxfSXGF/52WmXwjbmoZ8Fx6DYU+CKnxoMbDBoDGekpqHKoUruxwwd9QfCKFyEaz25OO91K86iPdwmxgMyF02d752gZBn9Y3yIcdTbi5hIW5Nr0DKPdJFtw7NFEPA3R+ShIAd7EOzLZMFo/sqYbWf6JtTglDgqMWqOUtF+dyTrEh4TlV8dia5yHaF2hmEklkkuE4r7gu34XJ9cVg3DqrWHcimmUtOSOhYypfBQH6GoOyk9Oz5udIrLpQRdPCSaq/Wq5pmA73oaYZNCnyNBLWjEk8qxFyXHRcNk60G1WI92e3m254UD2pwMnIxUHqbwEG+sDJiR4bF+9TRSZ65SVlsxlENFyqYRrA95gKkKdtgSpomZRp/110aD9jtvKEY/t7WqzghBoe4IKSOiXGrc4j1AuU7WESazWz8V1z3QVMIFTrrrvknazUFO6VZ31BXVpDj6XSQ3jatQckEQKzz0nqgslnEdUPXeTjpgTW1ZadIgE0a6eXEadzy1TqIZy03IZt5A2x4qeU5C/zph6d+n3KtGYDhO2jeERCIRqVJ3uCvxwRNZLQaNXV8hkLoYNG7KxLlbXUeX70ieUnVJd+GOzqIRIQQ82qVG5sFyiPOqkAq+NjqJZOwMaS20VB0nF8vMzxiEea1cjna54BbrK7uCauiKYfRyznHw7aKeEaK8MaujnK7U9C+ddVu4gIY65+ZIX9ylr87DGVoqm90an6xuZ0K/ImBqslSzqY39A+t2w3prpXjD2uKrGkR4veH05sMRaxAXzFikL09R5u1O0o3I4+TdBqoKBX0rwZW6SFAGmiTLcFQZ+DUOE5Cg6KPj+oDJpRogdPDfrKzEUFyhJQVbYzDXEBVE/GPaW9s+3dGfq7WEppmcBoo2oQsEoZzrrLFhEsrWFBaos4c2KjzJz5+bOBik2zq4kMKErsF1YKtyig/kkO7nVwhN3qb/0060oiS5Ei/465BFpjTEcmGhGeVT1C5NSQbjh97l2YfLt3OALBzZtSMvqHFatFUnhha6kNDvYmF2he+8mIHl6TqX9hkmdJUbsLoa0D9M15SkruA3IWI9WLq3FHC/DGCvALdHxy4TS0MRdplTN9hzcnK3k3BUbOFCty6njj6MtQSeLsNk+o4hUS5vAi22QTL3k8ttuiPUCaxB8MV4LpVnYfUa4W2wbCTJJby9XqNmriImtWtYbEIruOe4QL2/JEKQHMdrNk4u3rfxlcpTxbZ0hi82GJ+YyadJoWGlgiE21cNMcTqcwZ/kOqSQWPvJXGhn0vZ2WRlpJDbKTrvtwWNh6a4/uopQOEVZbUmgwWC2mviTH+ImSzoRoohgnw2cE39UjtlkdNePiQPujbTGYpuG+vaKI4+7K98yxOKUs1Fhkty8RhexCVoGwXqc2xyOTkewhytQwOQPejOAhU9T4wjCb20lcHvnE8kQKSfRLdq3b6NZs/bHkFCfHbyM9VGKJHIQM322pvKZgfYFUVxlUJlIbNNUiFHWMoFUi6y21sqmD2g16el3RlXUUtiN6LRcIXqyqq2ilkXsYzLNxtjZXtaiuW+6w8i6A0cOrxymtnScSut8EHjL3yiwazjd3g/NFBcVqBdWJGWmkZ1uIyHKts4mQC+as8FWhpp10pI6URQeCpLaq3molhFN55xmwb0gNasGBTeE2HMy389a/qLS8d7pT1ngwSi6lw1rCFDo/BGNeF8X2uF7tRsHOTwSLIXti580JT1viQdPbUMCcwl030F3CngA5yyf7eC73gpYlfUnuYGG/6mAZKtenZXbgV6eOlXzY4WyFWmr1IVSu8HYf1w4bh8xyDPO5Wxdz97gLg8hAzhfCXdM5xygJQmcGv5yXbcrPxdD3YJiBO4af16bpGNwpgKEI7ivSgm/HbDE0cIuc1PMqJDTG6c0Fdh2llD9xyNqinDHx4suw1xtYy1ZKEdHzOQKKkad9CSWJy44HY/lg+NS2EEoFHpgMUW44eVuquTSQgmxHCt1AOz9k6Jt8NvmcdebRAXGGXGT4YQPt/WRcVpRlUmsfgTt/jCF/sUQ5r+oKmAKf2AeHKsjnWYGRDbFJZFdxmLmNZYxy5dqRsban+kIVfn4zubk9ql1WZKKaE52gU/6xgE3UuqZwhcPMdhoPZc7mjNvycNRUsSO0fdBiDLR1zrFcUFbZ3FYh6N6qE192QLR1Y1r5cBVJlz6tQ2e+ty8RfMZP84A0vZNUXAkBks8MFkZBbLZoyWvzeajviNQuuEWs7ItRPN+EfsMPXLgW+oplYJ2TfWpDajYl8AG3LT3/4EYSF3rJreBxpq3MaBPrSLEjGvdI0CXDkoddfkRMj9eLTUHiUIfnMBze4HinnoKrHNeasmI0tDr6lCoeEm15iwowWNMLoiR2MU4VtUo30eYqH0iIiVQeR0yT6/ueWUI+TZydzql1DueCxZgkVR+Ma1teFQvMHKO85FIAnQFMkYgc0u7DLYqKlgSO7r6vYMQg8pk3ootCgxY+lKlHFRWDCNEbw2nXpC8KMAmtFzGeX2p/y7KkLfuNkvUlRmTNtqqruhSRvlcXcnM8L6JrbjG9uEURtkLJnb7MttpiheL7xtC9ou+RC0j6gMBgzUUQe+2pJSWt+N3eMjc4vOive6fCOdXnF4VIQGEdCHvbQ+jeSsbKQm6wQpJzB4so5SgGOEE19pzU5SCAc0fL0yF30Z3SpbW+oFVw4G6XVyxQjKqBLjgdo0faTWE3b9d4jlyObcJ1iXjkN0W4Uq+GWdNltSx9MjQlJNYTFZyCfBZMp2NhqOzRUgRjaZyd8rzgbGTplXh+sOjsMuTgtLYrwfi8HVh7g3JcPR+aVtWiBbmH0CtE7gXXUi+9y7O3neRB5hnqwXDr0z3NJeuM7NbGICgqoxz8lmaMkxGdTjQKG71XD90e3WxkHb/wWbAGE9Hg7WGowDqtTSAMX3iEf/MkwlTPJX5kBxjKWj4mz3vY0WRiaXU7yVVX6/X1AIEqp6JlX23Xp9tcPgAUcsgW6nofzefQuJivMIROTcLZaPQCi+U2hkGanwf22qmHbM76YSQv/bhzVdoLr0brDOsDOD2aDr4D/B2iCsXqnbEeIpHRzT4TD0Jz2Ga7CLWFxY0RwrIhr1kXW9HQLum4idfWHDpnluSd7KK3t5dUDtDObZCGGfXc2GHxca1WomBzUdr6NS9icbFRjIjaxExvHZoLhYIzOJPgviAqx5wnz601r9Y8etq1tuWn+SC0xu2qDzg2X+gbf7iMmzN6Q2J8Lm4hmzyKeB7HG8aC8tGvLsVeyRhGsnX1mrgxm3csWihIY8lcW4kNDO+6qx1cV2zHxJcjtKANOTk3g+E6VTtPxaKK/aIe9iZygfEd6Tl66iBbk7VVh+xSP5X9ztCC3AvznWqbPN5Sm/P5lO7WCkf73HJlLnGiX15rnDTgTnPMVc6f3CDdjJaqN+QGLvULLWGDYZH26QQnnIlxLIJIubJrr9ShZBz3ADpF5ZIXZKFsFlcr3Wgb/WRvR+nKyv3GxAZa1y5juOY85NwtQxMjKKfq4yPlFSK7O8N2s9zbY4VnnbV3oqU2ksJuHq2WLuL0N2SJJroJHZNg7rRiRW3Vy9Ifegrrg2GkYxUJNKK0pW6lDog5QjaM7odzsYbYZTssIp/h+lYND7cbpEsdHcgOvr1eynJp46sglZkbs0WDs+3sCVxNjuegauTufFKXF0KIeksG1bpD4bJm8Qu0hsmapRh5xfYiTQ69YusX75IemWiPM3O+aCuHZ+BVsPAJiUmZ/MDhRGWuw5iFSlSlRmfhISy/R5D9SvAQz1Ou9olBvSPGUPMFJxX0XnMLa5PFViLbBbW7lHqQKPGxt0hk1ZP4RY+dMQrnSQtOiCpNnCwB4yIS3mcKpPp2IISjul2ROmaM3ZkI8frc2U2ihla0aqEDstR6XKvACVHsicrofLOaw1YeIsTFCO2agP21A18lMFMN5JKnLyJV7vYtLJa4sOUIvCBHcllSW5g9X/qR1jagDbMvn16mZ97Pdwz/5t9FTM9x/689Tn48+X17iXh/zu/b3pe7ri//DsQvn14qNwYQHs/F67QNn4+U/+tT8c9/fhE1bRge/55geqHZN29vWBo7rB8g3raApc9N0xP+Ty9ukZVpfAf76eX9BfL0mN1/vCSekD1fXAFA+Cvyir38/r8A1U19yF4pAAA= -->
