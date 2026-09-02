---
name: "rar-cowork-cookbook-lead-qualification-consistency-check"
description: "Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_qualification_consistency_check", "rar_sha256": "55e84afa7b1ea56b2b27eab723f388fb6ae26a48595ab757f25c3a324c3afb76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "lead_qualification_consistency_check_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/lead-qualification-consistency-check:658f6aaeec69ed8fa7cbf296e99531f5897873516075b565fe26372ccf3b3b63", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/lead_qualification_consistency_check`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `lead_qualification_consistency_check_agent.py` is
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

Lead Qualification Consistency Check — Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-qualification-consistency-check
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_qualification_consistency_check_agent.py` and embedded as the fenced Python below (sha256 55e84afa7b1ea56b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_qualification_consistency_check_agent.py` first:

```bash
python3 lead_qualification_consistency_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_qualification_consistency_check_agent.py   # or on stdin
python3 lead_qualification_consistency_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Qualification Consistency Check — Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-qualification-consistency-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_qualification_consistency_check',
    "version": '2.0.0',
    "display_name": 'Lead Qualification Consistency Check',
    "description": 'Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'lead-qualification-consistency-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-qualification-consistency-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e18c74d7ad5bc1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-qualification-consistency-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:check'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class LeadQualificationConsistencyCheck(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadQualificationConsistencyCheck'
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
    print(LeadQualificationConsistencyCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOi2JruX6F3f6iqNjNlFMwTJ+IiIIoIAgpKZUUm8zwPAtX133uhe+fQp073qRv3wzUj3QxrPesdnndY4O8vVteGRf3y8UXzrBzirTSNQq+GrNyFmOJe1An4UyQ2+A85Rd7Wkd21Rd28vHtxvcapo7KNihxMZ0LPSRroHnrtPD/1LLeBrNqDbC/KA6jqrDTyI899ILtR8+0CgG2ipvXyNh3fPW43Xe1bjtd8N86x5nUAftSGUBY1zQxa1FBvBZ0H1Z7VgLsfgFTeYGVl6jUvH3/97d1LBI5fPv7+4qRWAy69iEAs5XtE5m1xZ3xoABBSKw/A0HIEhsnBeenVflFn4JLr+dDr2c+Nl/rvoP/4j+Ru1UHzy8dPOfT6+fQy/1O7HAKWgNrCAvBAS6u07CiN2vEDRKd3a2yA1G1XA50sqAF2zYMPz5nfkIoS+vt87+fnIh8Cr/3500sBRHjI/unll9kEn17qbj7+MKOUP//yIS3uXv3zL99wms6OPaedwYDUHz6/nr/CgoHfhkb+Y9W/A9Snf23v08t3ys2fp9yznmDmy4e4iPKfn8BlXfRebuWO9/Mv/wzWmc2cApv/S7i/PoFD4Deg06vgv7x7GPk3aPGq0FfMf75sCdz6VzQBw9+Wewe9GuqfYT/s/9+g0ygHBH6z+J/C/dmExd+hX/+pbv/ThHeQ/+mF9dKoB+ywU+8j9Ptn7cQxv/7kfrv4029/AOj/FUYrutp5IHzOrDzyvab9/PnXn5rH5Z9++/WnrgRc86zsc1enf4b5Z3Z9rPODBV9H/fzjXLD+JU/y4p5DX5kO/V6U/1b/8QHSQei63643H6Hv42X+LKBZibdFnyb4LmYaIOt3dvzl5Q+QJHKgTec8boMo//d/h46RUxdN4beQ5hRdCwEHt1HmzcKfw6iBzq9B/UU77EXxQ+Z+gcDVOdxBirC6tIX42opSCMTD7PFZg8KHvvwf55FR3zuvGXU5Z8nPP2S4z863hPR0/ZcP0DkESxd1FES5lUIqfTpBVgDy5bzoY0zTZe/7eV0gU/TMOyqzn3NO06Xe36Av/8pCnx+YH8pxVuZTDrxjAZe5UOtlZVFbdZSOkDVnK3tsvfcgz4KMUhdpaltOAs1fXflhtpARevmr3RxQUrzBc7rWg9LCAcL7EcjN74DrmyLtQXacrdkkUZqCXF8DUxX1+CgBwOIfZ7AvX77YVhN+yp/pGIOeNadZggFfBYbevy9rz0+jIGw/5Z4TFtBPv//xE/Sf0P806wE+r3ECteFhM0DpFBI0WQKFK+gyMKyBZnIA4z389/sfT2fM0uWgyIGomkvYYzJA+0aGWYOnh97cA3SeRfTq15V+tBsom8AuUNQCawGfNO8+5TNEMZfSe9R4b0Z8Tn6a/s3fz3VmnzSvNgR+8usie4x98HB2plPU7gdo70NfLQXUBX5tZ4+GRdMC6pZe7s58ADOt9psL86KFGkCaxgf1uWuAqjPyFxtAz8bJAH2s9gt0ZE6g2hUp+JoN9FgezC7yaHb8K2GflwFI/RPg2OYN4gMkecCaUGnVVhnWVuM9xoEu4MEIUOXe5gNwC8q9OzSXdm/20YPOD+bN1R36obxD39V36FHgoU8dCiM49P9FvzILTfO8yvH0mWMhTjqrtyfD5l5rVvjZnoGuAQJdxzNcvnUSb0nnLR1/ytMIeKUe//Yc6T9I9RzzTHFdDRRQafWBP4d3/cCNWkCN2dd1PdPZ+pS/5X2g4EzzZrYliOBkzgfF1wXnu2+ShiBM5/NvPQD0ZN1sIsBnqOzsNHIg3/PcB/XbsJ799eoPwBNvDjIQCU74g1YQQAccAPgQECIChAW14WE6CQTIbNcH278Oj+bOCkjhdg6QFjjX+wAZM6EBKRvgXtAezWOAFX56QEEZoEABRPxq4Sa0yqcwc//7KqAFUPsIEO87+7/eAtScywtY7WvcAUzLtVpgyTtwAQir4enXr1K+egqAZnMMPCb96OxXTaHvy9Pf5tgDEn5L/6Bhnyv7d6YBCbvOmgcxQc0FHA+LzHulD+DBo4h/eNbhZ6H/KsvHf2j5f/5ru4JHZb386LePUNi2ZfNxuXxWv7fi98EpsiVgSFR6zaMQvv8hdN5/V5/eP7LoD9hPU32E/pp8P0C80vojhHyAP8DzLTFyvJm3rx9gDub95vYen+9+ylXvm5/B8kUG5JzNP4Lk+7XAvA0BVSaovWAe/Cw4zVynQLbJH3nuUTC+cuE1TkAazYO5OjbFd/E76zR79um4r/kY3JoTEEg5AC/w5q1POovfeC8f8y5N373kVub9i1ueOe0CxgKDzJslEDugXWoj73EGFAM3Ims+/nHLJz8OrPTJ7KYFklr1Iz+8RooVPNL7u7lXzkFumfclc23Jv2+VZsnbsZxFfW6D5pbsa7/2j6s+Qhms4RYf54gGdRX01u+gr23yO+ht4/LYDuYd2Ln9Orfos55gKPjzdezXXaztvfz2J2K8duz/RIioeS0WT3U991uqeHiutFqQES+qCEQqnEc/MZeAZnxUvH9UGyxYe1UHarg7i/zNBt9EK57y/PFQpX1uS39/eUs28/GzoXhyDkz4S43fbJq3gv15BrdmiEd79rDUw1+fLUCNuTB/dyuYu4zPTxq/fATZynv3AibPtEmj6bEZf3lKBFT51hQDBJB33jdzo7EEUQiQQPkvZzUSkDO/W2C+HLmP8fPBxz/tpP+3BPJxRVD+yrI8z1mtPZfyLdKxfXS98tZrAkN8glqTFIkRyAomCZtYEb6HrjASdRwfszF7hQFBGoCUWa+CLJHZE0CFr+b+v+rwX54YoOqgxAqAEIRH4RaQzkY8i1jZqI2SnmWTKOZjFOXbKwvIZeEUsSbAVYL0UcLBLAzFwbdvk6sZ77W/fAr2+a2Xf/PNM5cASbIsmsVGLcuhHBLB3TVprRwPg23M8RAUcUnMg4k15lOUh4P5X6e++md231P3mb2gtQSNXT+v8/urv2dGrnAwcoc3e/r5YZZr3VrhpD2E10W98m7HmEoEVUg7OD+PLRytKIyXPBon27Lk+DtnJpFcnraawEosmZauKDC7cXPKNL9yO5/OFq4FK/wRbxzNlK9yh5GpoqjMMQ8qr8mXl5Mg1Zm/OWzjhDxg+9bVrqN5XMptdCBu9XKx3PfrUsolPVXtQo94hygHQQ8aUyTCE5Jo++xCnZGkcv0moHytsllqGsnSsAh8j7lpTt7NtWFg5jkrJZXut3WfZdvkLtQ1Z8WJlcfD2s9ZauFf84VwbpfrXowWBLPG6GoVdMF0TX1badJqWt9wA0VTM0h6T7tPXmH2uIDppUXQDusfzMOIo/EC5tfOyGG4KLWqoGvt3ce2q5sTTtlFavZRVycsWirboGTUHLeO7tSp1irI2caIQklrxgNBV3m1OhBxelvnSAeCT1vrRwMZd5mX7EOhuE2omofeQKRHdFvtJfl2V0RdNxlvVBAyCUK95rl9hhI4xQpnPc+C6cjQ9XInnxX0emKaYGdbhN4YDaYg+9TZrS1hQZ+F8BIuUFI8rMwqYzjDuG5Zb2QX6GYTyUO00DhPuvWGkRLWWUmTK25tcNHRJX3hwz4jB3JKhnxzZChliE7yRd+tEZrAkuqaNqTU3gkYZwO2qDC1S2yEynbw2rwRLHxS8dvUR5zLr9ucv61DJL359UaoShy+mvFhp6ALMb+yHl031/ZScO7RvjFLebgZmtCwDJOH161+m5aorG1xNiVjpkk2iqrueDx0xsZEECNcbxS4XyBgs5qhun6tCOOgZntZkAcnGwx84xNMCtPNod0lvSabAr9ip/B4GLV1WYFAXcRi0208n9Gw27Lf+N6dKs+ZEo4X39lVcWSfluViGSWGOnhRq606MQcscbWFueS91eUsNO1e7MdrlOGwxq8Lh9dOZSPdz6WsMCmx36oFvOt24b6NJ59hUdY6l6HWHRTFQtc32aHEscqaixLQSLDpFKzhaTZU011CT9oBpTNyZ3JKcLMzNx5uTcIOTXm33dBSZCE21+bUb7b27orE9iQiQ8zxoPHkozjhohvBDPuFcNGuipew4tpZbLzM364B/YndoHZTUNV64mPL++F6MpbG4ha1LHZc+iQZ8Th2TlEpUAJkh3LeauTr6MYOMU7GPHkRa0akt2J8Wd8p1zVcLr9W3ugUa/hg7qsqqG+VFXAnUyE2NrEXjMXSHs5YKR3XZ4Y773xsOBPrbZa5TIx4soCGtE1XiLBKVuVQebF1qHxdFW6auqNkstpxS2oT6YuqumhyKBKSkmFWMJhMsvHziBHh0ylgliKnOiNy5gd8w5O1uhiIZAyZdXUS9ylXcWqux/dACPdBtbXj2pyCq0qvpYjZBjuRcy2Gj7w0PbVX/sgvboYOM9ZITVrMd2apaEllivUhVzemvD9NUhc0MakMbOT1iIZkol67OZVcVl1xzRiJXYJ6tonwqeTd1ikLHOnv7a7fr0ZfM2w0dBYU2ySO0J96j6V2Q4G48FFWFxv4dCyLUTH0xvUu90WT4PD5ePeNSN3uC0sYb2rcT12e0TuBoaTVhTzTGkXK6OHU8xo+cCZ8qXzerQmwAIe6hCgjoxdP+2aJaljgVlXCkMXyoHpwsKwp+nQm1/x0oJo4oPdOUuJW7m2vxrk126NdNcoVjoIrn+65y16XvGos2vtZ2+bb471Rspiu6/54SVREu+9a8+ZshgGnbe6QxrcpkDZSg9PbzlkrIxmJx+haMk20ck9Ts/L7c5AnUZQzERyulviygAv40K9W47536dsljhOdEZfTgtrod283XY/G3ReOIUsWOenD+GI5ndf5wfMHJ18PbHaQBwVO+Fbuq9VRuzNxwTkHM2enrbOA9yJzsZbhPVd2UVr4+yznEqNb3zkbbGozrzBsfqzGZrQSzXGpSGc4QUCH4pIH8pYYrK1o4mc08aoDU6xLEDHclQA2kkXq0MunpIgG0mkFmUGTrl/vdmQe5NxSGtMJt5eqVp4W2GEf2ku4pLqMXvCIFqddva4uQs7eSknfOlRW12lwo3qVAuzU+FWv6RN70Mjccu7bemtnd40JW1YiOXXRD8g+PtTsankd180g3S/jUaF3+jFFl8xqjVHIbU0orZyJQ+F5F9G8cevTVU7Gztnp/c65GnpYLy9oN1z9LUIsl+R+TRdFwdSASu26prNKlotlKvjNYZXC0mUZpKJdSORdSZqRVic8HGojCpI4CzemJfJIlW5VnTa4EXf3FVwCgtFc6N/kSohZ8cCSJkfYg5ws0DgkmCJh0ENm8FWvbjcaVaLH/VWhe3QfbOXN+XS915lBoaZtiqvgHhhyEiVsxYWdsd7cnBPLGpdhm/fcTpiOyFHJcQSTez46XO0t2tm9mjLV2AsG3CKhwW7U0hNv7WXRjpIaHZWrWU2bDHHvLl6eidhJb0aFMtLK5cqTGoiejtiNRWp6dmHjhX7ZTCxyZUJUKAxFglXiJhWMHsWGuAebuMOtyIxMrXk6Lv31jV6KZ1fD1oUGB+RFEs8n3BPPxg233F6CnWB1Ri50aQU8SDu6okiVDvZjTTMWo+aIvu9jMOF2esYEQoXqtJjEZ1ushQXn9JpJIF3G4RMq+/lWL089MTnC7WjvqQNoNwPEMgvd4OMVTXmgkmzVIJT0gG4uHGZPZS/etPTmTRs4EjdH7bxzNtra2xELtcWUTN7QnqyN7HnaVg3nRqtTzhyLtW4mJeHq3CUT+BqmLjk2lBcslge+5U43eH2WQy0OMPnCO5XGHasiZTKhUOW6vGwZaS86mjshonWRYOQIh+RuQwpyxIabI8zfLxKH3wR4cxKv5VXfGBekrQzCu20iktvVsY0qtyKhbM6C93SylE74lbykFX1T/D0zkHRbcju2OuXexm8ksBmLOpwoz8rquMLs2zjwh02aDgui1LTLftUN7mLR0X260bdqBuc3pS2pVqmn42ByDDBwOaaXndxftmJyjxp5czvors0bNerh6CFXVtRw0IijkQ2JIiH5Nr6G28N1qJXUPLsGPqQLTzpdkrRsscHhyXGzdSkC2x/sxm5TAdthRGAkqIMeeWZ5kq+Hs3h20r3bV1JUmyAguRu/p9T+fIdPG3N75o64Z7CGt4rT5cbmznosRInboqVEHu0dkWYhK6bxDiGpq8ov07o/bALlnBcnCzSzWsze2S6Qh4veNDFbToNyMDKSromLpzoMoBm173O15MZEYEGCptBxv70cS2PyEWcSrBTdnZgtdqTjPWpq15pCyksMmlOY2bZDyHf6bnk7N8IRvY8SIiYifaDR6LbeBdLkqE6NR75zlBehVm23AVkyLkEwPr0/ChwuG1WUcZWjJ8lwWByN4yqYfDnYpqWhsdjED/3VUEHrXiS5Fjt7G7sMycWs+NW6v7GCku5yc7XnrjirpmzeCA4pn9SrdOX7cqm69JHvGGwRxRG3m/hQ8KnViFq8lp8YYsKNY8UtGt8kFP3CwwO5BJaWq60sc0yeoSI/MVltFspeoEtzv3ZWjKRTW297jymtvt3CWLyZEki+ydoFjVQx1gdEj5yFJtQFymS+oQsXU4iavT6BRnsI8NLma2+P4Y2PseGNWp7vS1vTO3SsaZVc7EGA5rxOELkhnRh1XUw0cYgxgdP1DDuqfAia62Tbb/0gC5XcqDR+zES7LpM8FdM2q4zyki0KREjKzN4BR2KcWDe8cmXDAukUYZly1qWhwZSSDDziGGtTW8lmL8hEh6TkkiMXQ3XEBP9sX+sau5MVv6jG5WkTYa7iMekS2yL+JrHXASpLockT+JTRJXYhC2zH58bBXWqkyN3VgMjCqVMmmfdSE5bWJku47Ugs7MUREXG54Q2GdpusVkcSbWhCTCpRsGE82271uKewUbndyPQg7bUFbQ4LI9/jd4S3zvhiotJuGImjRe4pc9iT2CWWYWujoOtidxrr/grKe5PDJH3du2a5QPDFzk48XHJ9vzH97e4C9n81tr76Q4sfd1MWdU29WCnXRSaTIb3xZR3dHkUpyJ1rqi4CZxDhsdi2FTflBI0nKKuwepScKu7qDpJ4Op5R5hLKoz1sjjQm5J2eoHHHeyydp3cnU6sVSLvEVcXl3clibbpRgwvTXXFyYvP9tr81IL7ZU40f1sTdIKTNFSfup1zPPYqAa2p7x/prcF4ne7CJCu/BfVisVqyYD5PZwLFmbPne467WSrbctXc7bcXNqk8vWxQmPY2TzrcVsplccSlZS37Z3qjL/nLjw1WZ0keQhRYxa5O4WF52LurDrrRhkXU1IKqe2D0Ph1ch3tvG1NT1faVbvUtwU7gqcBx3M9ff5b0okAHYHk62yeF9MFzJENRWmjK7vckNXK8f4kat1ns7njCkBxVrtw7DFRURSYsovEwWmtbQmLJGr/kG1JPKtDa1NiwGdHMwdwo/eXV09gTnHjnqJLpyHoKNXhG7vsD63tIL7m7IS8Up3Q5RykdsXzaeM9ycvWtfVhl1aHYsfUfr4lDYSzthCYJVGrOdFuOChgsr23k3pEcXlkxqpBm1cHZu1oJAnZspY5BVXKYUUefFbqMx7lhfcQZvx0WtYI67vuojOjUYmd6okI3OK4rjEcoN7HOpIC1DkwilssqqC8gTqt6FTKuFRpRMWThunCMboJbZ90TC5LvFYsIOVZarNtoaYVCxR/uIbWCwLYfNnt9nWEMzEVnowwmG61HnNwRNqdFCSSjUuoXHciVhm2MVViWpLAb1GkqNbXfcyZExVFIT7jTFxpLMN02cG/61R5D8tGjvaoNvlujC26l7z9n0qjKK+OnIHLClNUxnSV4ezltaMtsljMq5qSCyvu5gb3k0/bBQWa9d0rZ8a5ZKxVFqOKhEwNjU5myFmb0we/LshGo9lVx8MJ3mLnGg/Z4wGDXD4HDOpXM6gFx3SqI9slkaer7bqVWUowoiwdVgWdI5HwrswmOFpl7T2wZTK2vbnAoW9Er4/l7gVnoZavzW1LmBgO1pPtmxvlqRDfBKzd22zLgo+iZ0sW3FXE2wF6guV+F4xpJr78kX2mBp815exPNtT/hhph+6pdCOabXprkdQRRKcl0p01cOHwwXTI2RnXlMxto9yn415qWF3F/YKWvB1Y8xvOzRow3WY3DGDkguNQNwGseQQc+ULet7bQbZdpiGzkgYSNMT9yCrJDjkTpNDu0C69n44r68bqdxnOcEmvRup+NPewMm6Dck01dx1PyuMYj5tcWkphTHX4ZprO8N5FHNc4sNZUr6QpMxI8Xx4Umn559/J4p/zyEYFJAnn3Mj/Sfn2l8FcfKgdTVH5+RcNICn738v/uWefzuePbK8fHo34g3cfH6h//mqC/vXupnQgI9XwU3aRd8PqI87891X3/rzxtnhHG5+vx+Q3p0L69l2mt4PFAPMrdrmnr8XNTpN3jcTgwedfMP5Np5l9SOeDvy0O5rJzfVFidG7XPC03pOe3ntgC6Fa33Mv+EZX7p57mR9fU0eH158O7FHYHfIqf5jK2Iz401/zgOqPr6+mt++ju//3r5478A872IgwwoAAA= -->
