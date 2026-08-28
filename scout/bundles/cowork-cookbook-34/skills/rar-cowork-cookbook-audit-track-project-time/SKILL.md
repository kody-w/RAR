---
name: "rar-cowork-cookbook-audit-track-project-time"
description: "Audits track project time records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_project_time", "rar_sha256": "0092c0e80e3a93a591435cb13836924a89220eeeb9c54773ac3c1c590bd94a93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_track_project_time`. The original RAPP
agent is preserved byte-for-byte in `audit_track_project_time_agent.py` and in the RCI capsule.

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

Track project time Completeness Audit — Audits track project time records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_project_time_agent.py` and embedded as the fenced Python below (sha256 0092c0e80e3a93a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_project_time_agent.py` first:

```bash
python3 audit_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_track_project_time_agent.py   # or on stdin
python3 audit_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Completeness Audit — Audits track project time records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_track_project_time',
    "version": '2.0.0',
    "display_name": 'Track project time Completeness Audit',
    "description": 'Audits track project time records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d5647f2d833ebdd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditTrackProjectTime(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTrackProjectTime'
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
    print(AuditTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716adOjxrLmX9G894Ptq+4WEghQn3DEAAIhVrELuR1t9n0RiwB5/N+nkNSL77HvuSdiYtTd7yugKivzycwns4r+/c3pu7hq3j6+aYFTLg5Onidx0Cyc0l9Q1VA1GfhVZS74t/CqsmsSt++qpn179+YHrdckdZdUJZhO9H7StYuucbxsUTdVGnjdokuKYNEEXtX47SKsGiCiqPOgC8qgbR9r1FWeeNPzfuKUXrBwIicp227R9Hnw3nXawF94ceBl7QewZjA6s4D27eMvv757S8D3t4+/v3m507ZfdNBnDU5PBXSwPpiVO2UEHtcTMLUE13XQAGUKcMsPwsXr6sc2yMN3i//8z2xwmqj96eOncvH6fHqb/6h9uejiYNFVTtvNWjm14yZ50k0fFkQ+OFMLTO36pgSWLVqAVBl9eM78JqmqFz/Pz358LvIhCrofP71VQAVnxvHT208LgNKnt6afv3+YpdQ//vQhr4ag+fGnb3La3n0ADIQBrT98fl2/xIKB34Ym4WPVn4HUp8fc4NPbd8bNn6fes51g5tuHtErKH5+CgSdvQTk75sef/k7swz150nb/I7m/PAXHgeMDm16K//TuAfKvi+XLoK8y/37ZGrj137EEDP+y3LvFC6i/k/3A/7+IzhMQtV8R/0txfzVh+fPil7+17b+b8G4RfnrbB3lyA9Hh5sHHxe+ftRNN/fKD/+3mD7/+AUT/SzFa1TfeQ8LnwimTMGi7z59/+aF93P7h119+6GsQa4FTfO6b/K9k/hWuj3X+hOBr1I9/ngvWN8qsrIZy8TXSF79X9f9q/viwMJ088b/dbz8uvs+X+bNczEZ8WfQJwXc50wJdv8Pxp7c/ADEAAml67/EYZPl//MdCTLymaquwW2he1c/sUs7kNCuvx0m7AH/n3G4CgGubAGBf415MNmtchYvf/rf34MT33osTV85MOZ8frPf5NfbzLPi3DwsdyKuaJEpKJ1+oxOn0qXSioOzmteomaIPmBljEnbrgPeCf9/OXRVIufvs7kZ8fsz/U028P5kyebKRSx5mJWsCWH2ZrrDgoX7p7gNCDMfB6IDivPKBFmADufAesbKv8BphstrzNkjxf+AmgaUDs00M2QOfjLOy3334DDBx/Kp/UCS+ejN+uwICv6izevwfmhHkSxd2nMvDiavHD73/8sPg/i/9u1kP4vMYJcPcLe6Ahp8nSAuRSX4BhwC3AkYAoHtj//scLVCCmBCUKeCoJk+A5GcRiFvhfENZY4v1miy7cACALUC3qqukAHy+S7sPiGC6+6gsWnR/NjB1XoOj4QR2UflCCktTFDjDnK5Jl1S1aEHBtOL1b9G3wWPU3t3kUq6AASe10vy1E6gTqQ5WDH7Oaj0FgclUmAP6v/n/eB0KaH9oF+UXEh4U0R9+idhqnjhvntUboPP0C6sKX6UC4syiD4VM5V8BghuqRCk94wCCAjPdy6fvZ53N9BXnvt1/Wfoxx5iqmP6pZ86lsX2HuNM+SDVSZFlGf+DP5/+MVUm1c9bn/wA9oOkt6ecF/eeURg/o/NwHU94X/UacXn/oNtEYW/x8ah1kn4nBQ6QOh0/sFLemq/cRqbmlmTJ9dECjlj8UeefGtvH8hhy8c+anME+D4ZvrHc+QD4deYJ+/0DVhcJdSHfKAVwGqW+4i+OZqaZo5b51P5hYzfAYc+mAc4AKQqCOU5gr4sOD/9omkM8nG+/laYXzjNqIAIW9S9C5BZhEHguzOkXdzMGfRCG4RiMGfTECde/CerFkA68DiQvwBKzC4BhP2ATqqAmSB5wqYqvg1P5nYHaOH3HtAW9IzBh4UFkmAOhBZkHuhZ5jEAhR8eohZFADAGKn5FuI2d+qnM3Ga+FHRmDk6C4Xv8X4++Be1Dk1l5INPxnQ4gOczk6Qfj069ftXx5Cggt5uh4TPqzs1+WLr6vGf/4VD40/MrXIHvzudx+B80CZE3xjMWZfFpAICBmn8aBOHhU1g/P4visvl91+fhPnfWP/17z/Sh3xp/99nERd13dflytniXqS4X6ADJkBSIkqYP2Wa3eP1Lt/SvV3j/L4HfynvB8XPx7Ov1JxCuUPy7WH6AP0PxISLxgjtXXB0BAvSft98j89FOpBt98C5avCkBnM+QTKI9fq8eXIaCERE0QzYOf1aSdi9AA6t6DPgH6n8qv/n/lBmDnMppLX1t9l7OPMgq8+XTWV5YHj8oOrO3PTVYUzPuOfFa/Dd4+ln2ev3srHbCv+Pv9xszgIDIBCPPuBAANepUuCR5XwBjwIHHm73/eQcmPL07+jOC2A9o5zYMHXhnxIrh3c6NaAg6ZNwVzmXpSOtjKOH3ezdp2Uz2r99yDzP3Q12bpn1d9pCxYw68+zpn7bjE3tu8WX3vUd4svu4bH/qvswbbpl7k/nu0EQ8Gvr2O/bgrd4O3Xv1Dj1S7/jRLJzBozzzzNDfxvlPDwVu10gPkMVQAqVd6jQZiLYjs9iuc/mw0WbIJrD6qgP6v8DYNvqlVPff54mNI994S/v30hlZfzXv0fGA6y930718EViGuwILh+RiB49j/uDF/zAPmBDgVMhKDdxoMCHApgZwc7290agbeeu4ZxGN1tEAffbTZQEATuztsiGAY7Huytve0Ocv0dAmYAec/4/TwX+WTWZeM4Hu5ha8TfYQ7qBTDkwl6w3qx9DA6g7Q4OcTxAACxfp2aAO18GPg2a0fvapM5AvOz8/c1FETCSRdoj8fxQq53prLaC28Xs8gwtSbHcHXMoMRBcrfmVh8om3jeFp42wvJQ4eeuQ2jGmdITnjgdNvF3vHpwdQ54OLtyyH4g664WL5ksbLkbKPIqj1o9CGEYEPkqo4WKpkA0f9fDCq7ZR7RiHwzeTy6G1cnU5q+SsUWiV22kFt6c8V1kKH/i2Fl3RuIoTdxXqSy2cji3ks8HJ96b0oikOmuvWEOtccZ1yxmWO3bVCRecQ4ewFQoMzA61OTYIuaTI8NRO62uNnUy2YEfQ0THawxske+l0zmq3PWOqeP2tbWBHhoRGFUnStgwETiHbTdQ0jl1ii9f71UPFcraqG2rQhm2+mgI+z9NiacRAHzIVo94yDKNO+Me5rrcsTgVeRCrmblnbVBKEh0YRvOvSkau1S6sgbuk/6naFl4aYrjsJeIHD4yFVIYhq3g9YweXukmIJH/cs10zZ000tp6nT4EB+lstcEhyDAT7fW9xd8uJfazk8urtDZOic7sb5J8fYYFKhhOCziJicOvWamtjUzeXvdI8PukknRdbO3g/XRWR+2Gabr3H1Aa05jp3TtbGsPvi7jRpYEgZCuEIEq20S8aDQr7yI89U13i/uOvMQdSho14UQ5XXnaLRWVodJMUJvgRKLT5czJ0ib0uWPtDyhOB1VOFuhwvEFBITGXViSCSibdXVnbmeFSLq2ttjZ/5/brk0TesVN7qcrVKCd5ds2RJIGgRvS0fn06woZ9m6bjfRcp022zxpzE3qgX1t2cFQf3hGMz9Cq1PtERjpql0fDXKCvXnlKubU27JqVsWXYR1t1BV7KlewgTZEWSS4JIz8v8aJgperqny2Wgc7utdBL1BDGJ4GT3XcsPnVR3qLA1MXuSE7yVpOuU8f0aAqQT8hRrnfbhcVWNOrHhnPbkXFcYe4w2Yg41MmJjh2vOjRNdyvGK7DaFw3hcwlObwXeG2I3gkFSobrA4lQvM5GhgDGYTMm2mxMTYB3Gk7SLwdLMIeHrwU2mL8Y0nVDh7KlOozGk5oEm9i5HLZjhSnrgyuNspb7CMGO2TvVzfVXl7XmtUOFr2uurNFjXOK3ZJrDd1yUBLCLWWwvVQ746+Z13RJavJkHbroJvLOYbP7WOLmM61b2Vsnk1Ds4L25BIOjENY70XyBHObe5EmUwobfGDdkvScXMPrUq3jLRTSQd456vl8nzaOzIi3fMBSixfZpV/oG//qHor1LV7zStEjjM5sEWfbFRbP7Qy6WqPnTZJghpy5cnfF/ZzvI2ZXxwxH3JHTiXe1QuR7+SwMbNhXLJJZ0u7KItAloFRnUNHWOiUsS9/ETOoO/ZkPVsG4He4TQdxcortoHGOhOs+OoiJnQ4ExDp/r9V28OIVeSMQglbUZ75FG5g/RTWw1ZmDWUC9sc600l/t9sU12EEbczanWY9wdrru0J6G7fJeIXAoJr5Ji39zlpV0zd72/9Upbhupy5aPssIeTAiIGz5OOMslRxuEKev5qENSyPOhVHqD38DhdKTPQrohrukcqOmRCxjmdKw4jPayKbXDidwMFtphr2vKQEV8Fw/XCcHpu2v1tK7Z6aN9VMqh0xB5IHBqAofRtIGTTWReiyw0be7s3bkR8vAK9YItrvL6vhtFcKwF8pc+dRF/4jI9aeBRhz7OtfWRHo0Ya0D1WY7pITknvScWAuAoUby+8f7EZ3Rl2OrSSLRENBY7pZNS5680W9c/3cRUYdDKcoekKs9bqjBe5pRh4sbEuXZtSOkyqxyAwb6e9OV4G3/cHl2xFnhaWh3SFYpK4akbsEK7KjMYs0R7xKswZhZj6W8h0g0ZQgk37vFWk99qY2mOWGtetJU+Rqkjp7XCHtETJbbJDSEtc0R5JiukGO0b1tD3iiIOwIthkm1epU6UIs7VhXdCbY9hQFyaP47VCotWd42IMxOZ6a1IpWuNMzAfU/d7ENmfq0W4nByo33U9TQTDxWd5vAknrBTYpYbk485V0PjvbRrCX/EE+3PzytL24GzEMUEqLld0gH7Eo2wzoVq6iWBf2Wbve4KmpJ2kOXbBVveG5YmoTJkaUc3SCLh3vRsfMEW7d7exbwriPKWd3TsJbdj+wOc/cw1bPvQMb4zthcinprKpWyt6JLbkVa2V/2HTXVcNT+pHBEn/JHF0LGhKSc1MW3QnBEVZsYhSvdnNuM70h99ez0V5c6Szle3YHx6QQCRvklFOkZChbEpT4JR0SQ8HtEC7mLnXHHiZIsi9o1PbGlqBM3MKZrKhj0yzs65l2ieJw6oMp9JEe2lgQaWuTHUk3Suk3nqrs73BoZGV1xE3tUCrH7WG7uvQXF5J2Mt/JSn9IU3RTdwJ6oc6b3imuEE+Et3OfVmbiuN5esfcUB49WdhHvW9s1aaFyL+hFSadY3YTQhSeUM5vFt8wO8ymGgnxXDCIk2DtCbim9TESZshQIbc0rNxr8fksN1hHtNUadaCPd9ErYZCIXLiFOUy4VeYLuKza6W2g5YmiPswRpLFXCKo5zI2o7YepNzvqioM61ntjb7cZuLubtHmeDneoZLYV6HlaHfcuqaNawqX+5916o3TfLKdivLrpfCBQa6Lhr79AMYoL8RFN8auCQCCgv7iqFp32/Lt3S6owMOSyhE23Zas6z+9g+sdPoGdtO4/aOtxf4lJxYXcqv/Snap/QRtSN1zBX3CMGMqXMhgy+X3sFAmKDq8HrVH/R4fTWQw3ZJ0eTVi+k1fTXg3YFfhwdFOV9iV9f5c1StdUzWLk26M/Y5xdFldYJoajivYbSls4NXs9pQiSeLtneXSNM9ryZRqEJcx+BXopAjKlHu/VN2QgxFJJWKpsgjHFvb4QBfrmawXbXy8i6rax9fKswpb0frLLSUrGjeht3kiWXpdxWl03G7U2sQoIpOMY2QWZYx3LqYKNrJ2eKTWZjKgTMkmcfleBL6OwAdxdTIDUbJkkq5rJ1WUtFAlaAsXp7jS3OtNlEzFlOnxE02NuGW4/o9G58LrHZyo0/9O5pVB7/VO3Mj0zAsN9wISHzFhQfoRphZs7NwG3YtOTLFmNjeevFwiOyinviQc+5iATap2sXi6xPvp1fbZb3gXnK3XahA8D7X8bEXXNCuHhh+lef1kUQtHcZle1Mz/B497juFpKwzk3JhN60td3O49RjEy9a974/JMuAv5iocbrqJOnR64bqo2eGHUzbt4g7ZrJJQKjyGzstYJHCDkq8VRm19gbq2fGjseWI8mevICrN0WMIGrux4m+XXsneMOKiNaZ/Y+koJrcgLo997vM2MoLKOlGgyVCyqdZQyTnDNxG6Zp/lB9Cr9ZEkRTejtoRHNbXw7Qn61nvL6rjSGa2iS0vH5njO0IfJNecsIVLffm1NJpwgRJyXSHzfXc4PUVXm45XKrxKMtOtgYBRtV0Nj73sBwNXFyYhphaikLhzt2kMtj7NMoo6BL5RoblnDyO4bag9oqSV0lJes642RbuccBz6mDb9Cr7CquYrZCpWgIEkpxN2Y/bKSUulbUvuO1sil8sNehy3N7Zs4D6axIxK6dnQqlQr5hro1/FH2vODN2bbUgmAXeOk5HmWGn6/F43u1MPhexe01Tl75X2DW9GW5+us+gzZXEMntE0GVCdDfaYmnC28Yt6lZTmAkMbJrJrT3HDkqc02wdKOG9MrjdDlI2FCJwfJCdVWNnnsbhHt2bmsS2oJuVl6sg6vAKJeBkVQwmGsaIgDlh119XkpVb2nqESaw/H+m1sHR6QON3rG2slemXtiW3PYLFjMXkoNmSqxEtoayDIzLDxDEK7xDpq2NkYdm1JH0eHnBXXoGGu0kS0h4msYctBvV7J1Mhd/QLUehhVpX24wprekIEm2OLHakmXW+WtZFCPDt0/A1EUC3tIQy+Gci4W9Hj+e6acV8dBkvKzwGrUcgYnhWtawSKtCBsyvDDLYaRbRCEOBniQsvwKLZaHkNkI4oEdr+c8GJcO5J/A5sjAWw+6hPsR6BHlkgikv1tN6xJB4URCK8yhlUcZfCO9UrTMFmlx22yjKJEx5Odcia0LF3dISNvDiFPmjgqn4+TY3CNkSoIul/foi6ntVa+nba6eeNFb9Dt65Y2uYIJh+7uKV22Ypt9jZ0wtNkcV1sMktaAaDXhIDWlj0fEuXTPppiGYzeWQI8LeK57OnxrMcwd5MN5Hzj3psmrTV/UV3YNufvSOaNBvuxW6DhCKSmJVD+WpBiTzK7f1z7OcGv40oetJJL7ddesDJtHD2fyoDT39u6sd5iAb+S0LwuTwiZcCUTELVzsdEDPKUZKNEuwI9jFDeaIc/z2HKkULJM06BCqQtgcl/0h3CZoLcU2FcjaeIKRc5L3SZ+jXUyyY4qq1po95YrNgBQlxVAatmJs60G4zwWYDTx7uW+vZ61BCEulk9V1dwynwZbZPS4OPrmsemokR73qQPNkHftINcvTtByPLSZHA4YAU3Y78cpXiK8UYgnjfkmbEOEdb10+sHC497tLIoCuyZWta1Zw7eUuh1LF38N7PKmcKsY3qaJHAYcKdcmiKNllu5vVFwcdV/cJ2ExB3C1egu6wZC1pzYZpczCZEtEq5IRN0XbodSvYjMPSoHOiRSfIYU/NGECHVNpMVaizMiIfRjezDpVnwAeP1X3qBrYfVCjyA8ELfXamVvq0LMlEJfa5vYr4mx9UTMlNYhmfqnhy0bjYsTeW3izXQwLHhEOuArdnIxW/Oc2qLneuUFBoDDfXW4DanRwKaTlCPVZEIZRWYYiFZGfd+rMoDR6EdAlS7PvR3mAaexMbQe92SxJeJVWKiQ1GFljahYqwpw7naX+jGFrZlznXWMyKWfq7dEe7pmgJhi/CPncWQiFEBomA6AwRjDVunE734ZpIip632yF0g/qCF7LQWZ4VpNZ9h+NGurMTL53sEVMQiZL3KLGSGYoS+cOhNmiJTzlz7ff8mXHXXV3sOmldr72oM+1gMI/3Pt7p5VU92SAP9HPJrPW5uWUx0FynEdWztZKvo2XqpdfbEVTaiwah9P2mC9zArvP+ztUNqmKWcbtZPkZ6pksySCBAw2mQNjud0LC7D9XDCUEd32W5OuiGMBrvOOy7mWzArmyUqdBEhYRmMbVdj8fGFU5LnXBYtIZGKGTj/jLConOx9/eBljPktB3MrWJf9zVcaUR5RjCSXanHs4VaYAcAul9IvUFnWfPj3HPWS0Y+G1SwDwfJYxwM15OMIIiff3579zYflr4OqP/lq+T5BPD/2UHk88zwy2upxzFx4PgfH2t9/Neq/PrurfESoMjzcLXN++h1JPlfjlbf/91rjHnW9HwbO78tG7sv5/WdE83/ZegtKf2+7Zrpc1vl/eNQ992b27fz/2NoZ6088PvtYURRz6fZj4WeN54KV/Oo8HEvKecXQIGfOF3wuoxeB8zv3vwJeCDx2s8wuv0cNPVs3OulyHw+O78Vefvj/wK4BujBfSUAAA== -->
