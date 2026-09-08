---
name: "rar-cat-agent-skills-power-automate-desktop-assessment"
description: "Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_desktop_assessment", "rar_sha256": "6ff056fe92c6b801457fd674f9e59f20cb8d232458838a03d7506839420897ec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.1.2", "author": "Ricardo Calejo", "tags": ["power_automate", "desktop_flows", "automation", "assessment", "governance"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_desktop_assessment_agent.py` and embedded as the fenced Python below (sha256 6ff056fe92c6b801…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_desktop_assessment_agent.py` first:

```bash
python3 power_automate_desktop_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_automate_desktop_assessment_agent.py   # or on stdin
python3 power_automate_desktop_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6Z7PbVpbtX+Hc/mB5KF1kEFCXqx4TSCSSAIlouWTkHIhABI//+xyQvFdytz3d8+pVPVolE8Q5e6+d1t4H0G8vVtuERfXy+UWOHKtyi9naSr24ePn44nq1U0VlExU5uL2sa6+uZ6ei86rZsm2KzGq82cark6YoZ1buzsLBriJ3Zj3ugV2zsipiz2nqWRc14cy7Ra6XO94n26o9d+ZHuRvlQX3fW1ZRUUVNNIIblZd5bvSQELSRa4E9rwCP11tZmXr1y+eff/n4EoHvL59/e3FSqwY/vdyBveF6wnpgzry8AdtTKw/AunIA9ubguvQqv6gy8JPr+bPn1YfaS/2Ps//8z6SzqqD+8fOXfPb8fHmZ/pPbfNaE3qwprLoBYB2rtOwojZrhdbZMO2uoAf6mrXJg16xuKmDh62PnN0nAXz9N9z48lLwGXvPhy0sBINyN/vLy46yogL6qnb6/TlLKDz++ppOFH378Jqdu7cm9kzCA+vXr8/opFiz8tjTyZ1/Pp+36qavynKj0gPDv7Js+D+hPcU+XfH0s/lCUH2d/Lnmy5yeA95EwNpD752KBD8DOl9e4iPIPTx1VcfPyKcIffvwrsU7oOUka1c2/Jffnh+DQs1zgradLfvx4D98vs/nTtneZf622BAnzv7EELH9T9+6ov5J9j+w/iE6j3KvfY/mn4v5sw/yn2c9/adv/tOHjzP/ysvHS6Abyzk69z7Pf7iny8w/utx9/+OV3IPpfijkXbeXcJXzNrDzyvbr5+vXnH+r7zz/88vMPbQmy2LOyr22V/pnMP/PrXc8fPPhc9eGPe4F+JU/yostn7zU0+60o/6P6/XWmWingpPff68+z7ytx+sxnkxFvSh8u+K4aa4D1Oz/++PI74J4cWNM699uAP/72t5kYOVVRF34zOztF28xAgJso8ybwlzCqZ+DPxBqVB/xaR8Cxz3VPhpwQF/7s1//jWM0nKwCE9alOojStoXIq+q9PTvW+ug9i+2q9M9uvr7MLkAzYM4hyK53Jy9PpS36XMWktK6/2qhtgKntovE+goD9NX2ZRPvv1X8r+ehfzWg6/3kk6elCfvGYn2qvb1HudDNRCL3+a41j5zOs9pwUa0sIBcPwIMPZHYHhdpDdAm5Mz7qbN3AgQS1NUw102cNjnSdivv/4K2kP4JX/wNDZ79KAaAgve4cw+fQJ2+WkUhM2X3HPCYvbDb7//MPuv2f+06y580nECFj7DARBy5+NhBsqrnSwGkQKxBdxxD8dvvz+9C8TkoO2B4EV+5D02g/RMPPfN1ef98hNKkDPbAy4G7s3KomoA+c+i5nXG+rN3vEDpdGtqD2FRNzPXK7186osDkGoBc949mRfNrAY5WPvDx1lbe3etv9qVdYeYgTq3ml9n4voEmlGRgr8mmPdFYHORg3aevifC43cgpPqhnq3eRLzODlNCzkqrssqwsp46fOsRF9CE3rYD4dYs97ov+dR3vclV9+p4uAcsAp5xniH9NMV85hQZoAK3ftN9X2NNLfNyb53Vl7x+Zr5VTaFwQCcASt86/t+fKVWHRZu6d/8BpJOkZxTcZ1TuOfgXY8m3AWD2pUVhBJ/9fx5jJqzL3U7e7paX7Wa2PVxk4+FDp8ibCedjHgPzxAwk0qNevs0YbzzyRqdf8jQCCVENf3+svHv+ueZBUW0FoMhL+S4fhB1YPcm9Z+WUZVU15bP1JX/j7Y8g0HeSArBBCYMUnzLrTeF09w1pCOp0uv7Ww+9RrNzJFSDzZmVrpyArfM9zbctJAKpqqqxnJECKelOVdWHkhH+wagakg0wA8mcARAQcD7j97rpDAcwEReVXRfZteTTNXACF2zoAbehV3utMA8UxJUgNKhIMTtMa4IUf7qJmmQd8DCC+e7gOrfIBpqiSN4DWRNeR133v/+etb8l8RzKBBzIt12qAJ7uJXV2vf8T1HeUzUlNeTOV33/THYD8tnX3fXv7+Jb8jfCd0UNXp1Jm/c80MVFP2SMCJlGpALJn3TB+QB/cm/Proo49G/Y7l82y9vMyWDwa7N5zZh+ytld27nvLHmHyehU1T1p8h6H3ZawCqorVfowL6p+71t3uL+fTWYj49W8ynby3mDzoe7vg8++NR5A9Lnqn5eYa8Iq/wdEuInKkc3xr051mbvzPEh+++P0N3D43nfgRsNlEfSJwpS+vQc++jhux9i+0bBUwuH0D/fO8qb0tAawkqL5gWP7pMPTWnDvTDu2zg/S/5e/yftQFYOw+mllgX39Xsvb2CaD6C9c7+4FbeAN3uNI8F91NQOplbey+f8zZNP77kVub9O6efieJBigLvTYcmUCxgvmki734FrAI3Imv6/sdD3/H+xUofqVw3ACYIzL3VPErDCu6t5OM03OaATO60CvrYg/PBwcpq02aC3QzlhPNxIppmqPcB65+13msX6HCLz1MJf5xNw/DH2ftc+3H2dtK4HwvzFhzifp5m6slOsBT8733t+znW9l5++RMYzxH7L0BEE31MhPMw91sWWY+wlVYDKFCRBQCpcO4TxNQ16+HeXf/ZbKCw8q4taJPuBPmbD75BKx54fr+b0jxOqL+9vLHLM3jPmREsB2X8qZ4aJQTKASgE149UBPf+L6bJpwTAh2CYASJI34cJ0vdo1CFtClhOLHyXXOA+7RG0j8KOTbkohuIERWGUBWPugoBJCqNxFKbohecAeY+U/jrNA9GEiqAXPkzTqI8jKOyCFEFx16VIinSIBQpbtG0RNkFb9retCajZp6kP0yY/vg+2k0ueFv/2YpM4WLnHa3b5+KwhWrUWBm43vU5XpBtwI5Uc3NLkBtJSeVKwd10uHpZZ35SNsuu2qXkNuZ25F/vDYGYqUitLr0ggg5tnREr0p1g3sEvRomHGCOL8khI+jNNIf5bktYhl8sJ0ZEbTpIV2jnulySu2vjGhrfNoifBraH/KoUV4w4tLgCpWNEdCU5fqcg8aFXJJuFuzkg1F9RCkDu1KrpUiBq3zrNZqVLkHo+xvgoMdY5EUBUj3KHF3zY0WTuxt4Z6pjpPJo1At5nP/pCO93egCpVU2TbhQrCiLhcnLTGolbGm4Sn3eZLy7U5m6kTV5PKo8B0ki1hWikB/s3VrFCvh8izfnvYkuAi3yrruCXZnqWVnlpaOnw+Dx6cXm8i0ZsUrV1ewhMSp+s7AG9XxLz0gmFYVtnocy313kg2bomg07NwuDse11UXpUNxoIb2k3wybOZiZ2XXc7DKkXshWn8erIk2FCSltB3MNRr7JpK0CquUcpYr5an+0llWjKdrPBD8k8dLL5YK8hd33SuKZGggVzKRarub61JYdsxXWtYhqSsAppahVzPi+0RGxiOpM0PjcODa6ubpqd6e1BBGlg1RnrM7srhtnETaYKdEn227xW12uXVcZdXa7jkzZ4fXulKfTY5LpzkKWtuCDGs2st/D1qLExqX9BNxh5M0a7j/eKU5Mk6I5rFesubugESh3f1tO1H3ebl7kblpbbr4IFtoKFXM6kFvqW2vVPPPRS5TO6Iazdz+oxEeZ7SodbLtm2TaDIK5YR3ga/YejMfEK2ooQPLZF5NmGmqeY5PmLJsjkSFMHkttqWItLmu15xpRHh7MNhurCUhswK/vhnsHjdHSsnxsx9sbYgsWKogcR8SZTONYoaovJ1+nifj3Ci8wlubZ0CuCheej+71FpFaCF/lElOT9OjGJIsoe2M4RlR99NWE1x2bHS34uEwXtLebS7vwSvRJtu+Vlu5ySTirpGKbO32Uh+Q2MFguHaXoeHGP9XZl3eCAE/q+ig75ylmuJVswXVWOSB2vMnzv7o7Lvmm2yrjSl/KOqJIRGjNxS43OHLm0zIE83sZw2NyaTPPTjNTR0d53Ix3xFKLkvELHNDwviWqHeoN4HLSWW1U8nPOZKwvQGYoFUlWjBXXmmXbJ2Lf1Iuu9fY0swrI9rU7xkJtVx7bpCkcziEfS5WXvLVfdoZgfcFzRNwf0eskksRHSo7nnBxSxWSgt2cBE0kJ2CmbJtcoJumHyDTGs66lWrgpWHkhgK98qFcvD3OCtEFoChLWR4nJQZMAa8pw7jGoQzrnbvkb1WrGXTE7FFkoqgZzIBIIkbrWn47XoO97ALM5LIXDJ8nQ1OYHsO7ewgtjCQ62ttoM6qMci4eAdl9irPYkeLTg4sS1SojrZXDYU5mWqcMpyuYWQk3zFWAij/P2SzzeL3Sbomo3ExX5vkgdHU+i0tszDIBGsJ4v2CpXnUZ84fpNKFdmnDYqL5yDFhCZrlm62Wdb5dZ+oENcLlotI8LgNFWjunzEyy6kdyGuYoubQvMdyrF25iKYoUcLgK6mwxnrRr7b82pa2O7a9NcKe0Uw5iPBudSJsfs+HyfI2jHxC6KW1PxerVKy46yISdf/k7xj5BHy/kMszzaVWkAXLHD9cQZ7JZ0E4HErSc4KTtLU0spMMqDIKg0A5Z+wDNt+2WGKamiSNI7akWLq51fhZS1ZWKCAiOBAie85SQ2tdp4VBKTyaSiOV9X5NK/iQsAsmTXchq9s6zCO+GRF7gd8uQ4Q+S0Ebtgc5XOIElovWvi+tYbeDhZoScR1PQqLvi1GZw3Ea+sFlx3hRJwK+qwvYzxRxHaeCkxAFV4/Vmo1VLRr0Y6MVZn+sklhzAvzsIOf+ihZDehqlpFxtC/928SmnubKBrVwA84BUvJgH7uxoNIvxI4Mzm+S2iI94fTKhcji02GUTuw3Kr8ltPA8MPFgtduEoozYUDRgSlKsdC4Ua320Jsd1WXBGvQOFwarbmLHaXE3SNVgzirXY9Xuf1fpV6XK5JxQ5m0HhECrpTRFzMWkYSaVuCGI13XBY9U9EY8UWfS6YyXM+jt/XiNBCMUI4taSP2Z0Y3yHNsLGBFYEfNTTqZXpaLYyoxanImC8ZYEauyuu0XXGvYW+VIpyqzvnUrRVqpxlYg46IzA2UumN2BbbKqQJIkaa1kgVsOy1Ji4B/VVRXT0noeipFHqW2kiWctVot8BETErQwkOVZQvFENxXTXZLJdsLW2m69xMNuguHS6ikK/NtbXa+RwJrc0kPHIBBfSFgZ8zQQxrRIkXtg7LjgWBpa6YVBtZZ3dNUF2pr2jLy7nF4rPLwQ1gAbItuE+StbKbZcYa6RItlnlY5l0dHj8eGYdquoIxL7R/tjoONRRghdy+gHbgbrX9wizylSG47F0rijoQaLqgy9Bh9Ul2DLWnDiIeJUIwyHkKY0YLO98JJrhSMlLrlirDc7cMivm+gXI5pQygvNB2s0bk7WvkS9ZbYFQ4cE8zT3vshQvW4Ipk8bILtpIGFd2B+fpLekvKmXaNLpAT7IzhkinWesY8k/5fqeo3eDDJN44Hi4i7lEgbUW/LN12E1670144jvuVOF43voy0ndtnC5dlaDyS5zxxxeaUbcSCr/exQ3fqnLXNBS0x8S3awazrE9vYPOilGedDta4oTuT77RxbhkY7F0jhmEW6zCY8J1NaspTXToyvtsHR1wkxJ9ze8KutgoYItiJ5hkzrJRem6dqJFPzq4mKaMLLoJBLbFt1WvCQbX5SJsCpgHC6jOpN5SPGVoVbccwJxwbkIXLUhYq2PIx50sjgEE6POCB5PY5e9PAqnFV8Uq9VCtJZN4KFSMdiLTbwjMmXIdRpbQ8S1sE61QTipMATX614fROOKqd7evrKXY7sxmRtMNe1GDDdSKK0Ovheslry5hcwl6OQXaRRWoXiAvd7FHS1RdwwZS8xRRnctMzhH1VH9JRHXQhapOXIiuuv6Eo2Kh55l08l0VTY1Kl471VExIrFZ5B3GKg3FqnGl75XRcaQjX9KkzPTmgYhGeU6226ACVBF1Fwc+2PhFV/dy2ZEmIZm6m2ZMW1/r07BR7UueoBbfIoIAVcdhqFaMocqqorgnfOVbo+3hKBs25LAxbUJFmjr19QFyWtCIVA5Ch+1adQ52RBCIDnkWkpsX31Xp1otPi/25uRlZ40IIEfMJe9iJi1wZ6bwtmoNumO3oGXuDWp5gNWCupAxUjAs7QqiKMq/n2sPZYBOgiKsWlmbG8V7Kt2hJH9GdziAQU+s7dI0Lo1LrwZ7zwYFgl66L69nekLfhTMZ8hzfo0sFGaK8fT7rcFvtOazLdPXCcY5zKbJf7cie57YFqc9btbAgS3dN83aJ8zYjkAprrUN8EBoNlrU8hWAPbtsGsa1mqaG21qw4cLnrruaSQo52t1ulg9wQtiddjgAwOHu+JY0nDF24ct9Qy3V7qjJYuS3CQgQjzcDXDfAwyX4wZ8sCnaxOxYY8Oe1RBh4JjT/aCKq9YujsFXK07O4TL9n43H51zQ3YHci3M8aJbhafbbl8IUHu8BpnoBrdFuVydjmhbyRsMPdInLbzeNpu4dbAdshP4+QLGHa7rNGpBEtYhHglSQGF7n1p71E3bAiL7ORbLG2eN9fmybpbMIduENMXAi0WDnSItk0KyTXFbZIx1VmcoDg7XvofSNxCla9jorbMRdgsNxWETpecHbS7Hwmq5wy6XfrGPxm0/5657KeyjHu0TMtSpiNWK/nTpdHPJK9eY3a2CjXi7uOQO5yShJrTCWLq04SUKyo24kq2dDVpLeSUhF9ZiLhbqcQpdE6uaXJ0r54iFqwNl8Z6PUHPPF8oS3RptQCs6YwQmSYyj1dKwJpZBwIQHpYZSbRVecJc5IbIBYSbIY60c0Qs1528BexXGrbBYOBkyDpirGxHTsmDQv3JqZGfnThPOmzomL+Ckc+ASDneljD0Npbtn/eq6ay8oOEY75q3fHjnRzouNv/Q2Ln30ar84+psuJhPEWQ1zKwMjxWDG+j5rjhy/cmCuRi0THKYTvtrP51eMi7Kjcqq1kgmvezXq8xWMSDk8b9VlxjhLhhnP6vnkKrGykANZOhUGVKxaG9nyGUxvN5HO1dfGb5miNlvmFjK33RLekUcwr/UFmrveoidOFkLX+Xi7HcvhcrtE3QhDeVPpJ35pm5jDmPi8rYXUxVqNYwMia/UDyiHjKeNUFJIXVNfelHoN3bRFdCBoQb2ay4pYIeH6yq4uZGpWRxqDFP1qMJLLwuYBQYp92G46ityNXZrS2jaAM40YJSltll5HjtbJGZdUSYXK5mqUSu8Eu6iRgurkVHassJKnzBvr1hp9zkA9fqOWxm7bQkMCGUCp4Dp0H283ph6Yh/VuP1/z/sWZGzUrUbBDGsM2HldJEoUXhOTHFRZvI1/IVa1zzT0t2XZ1Mk9NE1bOQVtd90NENhY8ZtDiWs2PN7sYMXg9X6bVGOibXl6T4SFskVsRwOa43h1PA7G1CY3ir6dhC90cjep8uUlPBCiyAeexBh8Wgo/a9c6IB5uAOUxJStYaRrwFfRcc2XMho2Kaa2NGo8ebV7pwkRt7hPSOSgGy8lhTZODWoVjCohDg4l4i94fTSQFnL+qIdL6TXvUISYfDteeEWN0LXOSXNn5buEV2OyoMuaKwSNbnxlIrr55T8J3p8Meo7IdtQeow05DISYhqdvQ0n1X0jjS8zCoLmPLByU2bl/R49eyB7OqrqHn75FBuUNWDmyTH/OpEWYi3z+1bZLEGBENWtSm8Y7YdOLJnSpa6rjBhjRpLtB6GwdRytYMaf0VDstAvChVbwTbWCbzqx2lxiW3b05WWShUTTlvQKm4t7doh4qC75mT6G7xNyZab63POz4t+s1jXFiXUlrcwjZThHbJz1jdW2egw4kY5Wg5Qs4RcJlU0xw9Xg1a5CbHD+AhtbMJ1kpDO58uDaRS+JO3EgSA31TlP63GJMVtauB6WBl1kK0kL8Xi7StDjTlm3WeqQGWuaczAzDLvwiIt6jwq24x93hpm04XIVLGqHO9lo5pAuGM3g3dKHFVILfNGVc2ZDndQVbeCmiyAnR9A755aRN6tsmxqjqTkuzNcFrxryjdsNkjvOz5C66LcV2y7X7foQe+Lu0p4SozudLxyEeUKFHMEp97ohMcY2bWioV5hP7Li4vOWDILYImmI1vQhGbxXA1uicFiF6Q/3gCOe9jx2ChZ8ZHMpD0E2RN9ahqhseSUQHEruckW0+x3oJF+j1ad/0yDKdy+qZZYPT1b3Ma7TT1eVqSyPbXsrcvX7hs+R00NXmdrxJUmQdYXjPE0NTpMQavR7jglJ0YsWmtTp3V47lgnaxo3DjZAo1ixCYv4k6tIOZA0kRab9YyLhytMsi508lJ9LgGOrJN08dRSfAjpy31pULTKLLKoQtAV8sstpXMYg6+KtSPuZLtSRotUPm8NmE25QmSkg86YMkYgR97JZFSuae0+qWF/vddrE6Cn04To8rf/rp5ePL9Fj5+Uz/3389Pz0q/X/2xPbxcPXtld79ybpnuZ/vuj7/LzD98vGlciKA6PFguk7b4PkQ9x8fS3/6l2+Jpv3D46X39PKxb95efzRWMP17sH/w1eOh/x2ZnxZdDa6/vc6dLr4XHEzvnR+2AsjP90sAKfaKvKIvv/83N/48YSInAAA= -->
