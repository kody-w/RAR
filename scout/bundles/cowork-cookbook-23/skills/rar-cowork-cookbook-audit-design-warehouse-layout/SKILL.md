---
name: "rar-cowork-cookbook-audit-design-warehouse-layout"
description: "Audits design warehouse layout records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_design_warehouse_layout", "rar_sha256": "4592cab07ab4948118c5fb3db75c7e423f97b64ce5d4fe884dd34188fffe87b7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_design_warehouse_layout`. The original RAPP
agent is preserved byte-for-byte in `audit_design_warehouse_layout_agent.py` and in the RCI capsule.

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

Design warehouse layout Completeness Audit — Audits design warehouse layout records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 4592cab07ab49481…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_design_warehouse_layout_agent.py` first:

```bash
python3 audit_design_warehouse_layout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_design_warehouse_layout_agent.py   # or on stdin
python3 audit_design_warehouse_layout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design warehouse layout Completeness Audit — Audits design warehouse layout records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_design_warehouse_layout',
    "version": '2.0.1',
    "display_name": 'Design warehouse layout Completeness Audit',
    "description": 'Audits design warehouse layout records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-design-warehouse-layout',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-design-warehouse-layout',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b827adba283ba279',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/design-warehouse-layout'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-design-warehouse-layout', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDesignWarehouseLayout(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDesignWarehouseLayout'
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
    print(AuditDesignWarehouseLayout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71a+bOi2JL+V5w7P1T3WHVF2etFR4wgIIiC7NLVUc2+L7Ko0NP/+xzUe6t6Xveb9yImxloUOCdP5peZX+YBfntx+i6umpfPL2rglDPOyfMkDpqZU/ozurpWTQa+qswF/2ZeVXZN4vZd1bQvH1/8oPWapO6SqgTT172fdO0MnEyicnZ1miCu+jaY5c5Q9d2sCbyq8dtZWDVATlHnQReUQdveF6qrPPGGx/nEKb1g5kROUrZgWp8Hn1ynDfyZFwde1r6ChYObMwloXz7//MvHlwT8fvn824uXO237psjmrob5poV4VwJMzZ0yAmPqARhdguM6aIBGBTjlB+HsefRDG+Thx9l//EcGzIjaHz9/KWfPz5eX6Y/Sl7MuDmZd5bTdpJpTO26SJ93wOlvnV2dogb1d35TAvFkLMCuj18fMb5KqevbTdO2HxyKvUdD98OWlAio4E6JfXn6cAai+vDT99Pt1klL/8ONrXl2D5ocfv8lpezcNvG4SBrR+/fo8fooFA78NTcL7qj8BqQ/fucGXl++Mmz4PvSc7wcyX17RKyh8eguumugTl5J0ffvwrsXcf5Unb/VNyf34IjgPHBzY9Ff/x4x3kX2bzp0HvMv962Rq49V+xBAx/W+7j7AnUX8m+4/8/ROcJCN13xP9U3J9NmP80+/kvbftHEz7Owi8vmyBPLiA63Dz4PPvtqyoz9M8f/G8nP/zyOxD9v4pRq77x7hK+Fk6ZhEHbff3684f2fvrDLz9/6GsQa4FTfO2b/M9k/hmu93X+gOBz1A9/nAvW18usrK7l7D3SZ79V9b81v7/ODCdP/G/n28+z7/Nl+sxnkxFviz4g+C5nWqDrdzj++PI7YAfAIk3v3S+DLP/3f5/tE6+p2irsZqp3Z6a+7JIimJTX4qSdgb9TbjcBwLVNALDPcSD+Jw9PGlfh7Nf/9O7s+Ml7suPCmXjn64P/vr7z39cH//36OtOA0KpJoqR08pmyluUvpRMFZTctWDdBGzQXQCXu0AWfAAl9mn7MknL26z+U+/Uu4rUefr0TafLgJYXmJ05qAXm+TnaZcVA+rfAAyQe3wOuB9LzygCphAqj0I7C3rfIL4LQJgzZL8nzmJ4C1AdkPd9kAp8+TsF9//RUQcvylfJAoPHtUgXYBBryrM/v0CdgU5kkUd1/KwIur2Yfffv8w+6/ZP5p1Fz6tIQMqf3oBaCio0mEGsqovwDDgIOBSQBl3L/z2+xNZIKYEZQv4LAmT4DEZRGUW+G8wq9v1pxWKzdwAwAugLeqq6QAzz5LudcaHs3d9waLTpYm74wrUID+og9IPSlChutgB5rwjWVbdrAWh14bDx9lU7KZVf3Wbe+0KCpDeTvfrbE/LoFJUOfhvUvM+CEyuygTA/x4Ej/NASPOhnVFvIl5nhykOZ7XTOHXcOM81QufhF1Ah3qYD4c6sDK5fyqkgBhNU96R4wAMGAWS8p0s/TT6fyi1gAL99W/s+xpnqmXava82Xsn0GPIi6ewUHqgyzqE/8qQz87RlSLQjI3L/jBzSdJD294D+9co/BzV80BvT3zcC9ds++9Ctoicz+vzqKSbs1xykMt9aYzYw5aMrpgdrU8EzoPnokUN7vi90z5FvJfyOMN978UuYJCIFm+Ntj5B3r55gHF/UNWFxZK3f5QCuA2iT3HodTXDXNFMHOl/KNoD8C197ZCLgCJC0I6imW3hacrr5pGoPMnI6/FesnThMqINZmde8CZGZhEPiu42VAq2bKpSfkICiDKa+uceLFf7BqBqQD3wP5M6DE5BdA4nfoDhUwE6RR2FTFt+HJ1AIBLfzeA9qCjjJ4nZkgHaaQaEEOgj5mGgNQ+HAXNSsCgDFQ8R3hNnbqhzJTE/pU0Jl4OQmu3+P/vPQtfO+aTMoDmY7vdADJ68SlfnB7+PVdy6engNBiio77pD86+2np7Ps68rcv5V3Dd/oGeZxPJfg7aGYgf4pHLE401AIqKYJn+IA4uFfb10fBfFTkd10+/13f/cO/1prfS6D+R799nsVdV7efF4tH2XqrWq8gQxYgQpI6aB8V7NMj3z6959unR779QegDo8+zf02xP4h4xvPn2fIVeoWmS2LiBVPAPj8AB/oTdfqETFe/lErwzcFg+aoA7DbhPoCS+V5M3oaAihI1QTQNfhSXdqpJV1AG72wKXPClfA+CZ4IAsi6jqRK21XeJe6+qwKUPj72TPrhUdmBtf+q+omDaleST+m3w8rns8/zjS+kUwf+2G5lYHcQoQGLawIBsAZ1MlwT3I2ARuJA40+8/7rSk+w8nf8Ry2wEVnebOCM/ceFLdx6mNLQGbTFuGqXQ9aB5sdJw+7yaVu6GedHzsUKZu6b2V+vtV78kL1vCrz1MOf5xNbe/H2XsH+3H2tqe4b9HKHmyqfp6658lOMBR8vY993zy6wcsvf6LGs5n+CyWSiT8mxnmYG/jfyOHustrpAAfqighUqrx70zAVyna4F9S/Nxss2ATnHlRGf1L5GwbfVKse+vx+N6V77Bh/e3mjl6fznt0hGA7y+FM71cYFCG6wIDh+hCG49q/1jc/JgAtB6wJmIyi58hwXwh0XIRFiuSQ8NHRh38VRDw+QFRySuIshXoD6SBgQBOL7MLIkiDAER7iLA3mPSP46Vf9kUiiAwgAmlyvPh7EViiLkEl85pO8guOP4EEHgEB76oFx8m5oBKn1a+bBqgvC9hZ3QeBr72wvQBYzcIi2/fnzoBWk4uC26XWyRDeavC2XhaKq28+yqyN3edw8ndzlKErLM8NE8rrjolPDH3E7ORwEquqW9CgdmW9IyU8qX4wYRAhjo2UiCJJ+YiPWswyB7BMGyR43CRGYI6pXgLIuzZiCuYOzQYd7tSsly+dw0hvp4QxpF8mljvggza04UPMqjRn1qxn3KJrntJXh2PprqbicfrNuY4ta+6o2M6+s9csh951yoq1zn+90hOZN7iTr7cpkPXohn5MFCT/B2vjhYLImxSGewp5JhE8FUfDcUVGO8BOeurviVYA87Q8KUYm7Yscdip3PuD5LeQK3t5rhNB72/awiWGSoEA6ERyix2NMUYOp9tkcPo1tLoShT1pPdOrmoUBlLr0IphOVJ3LDVINFVucBob6kvnHLSmt9niSM7FfTlP9ykGdQpr27xWkorAMWqfZ2dz32BrTaCVFktGOd/HFlKeUwSCL/J6pw43WGBzer0Q2NAeNzZxG8uBtBMjcF0/FSQzadqSPN7Iw1DplZX0CJSdVz4nsqZjkXtvu13so1Yxr64rnDdcu/JS2ql3loENTrw/wma+hF0dl5cwtdqpXXsdzscxXhfMshQgzWjLxDo3oZFW6HLcHJV+p9iI5s9RvBxovjI9ypFcZZBNbYcLt37ED4Ih9qK5jLFY712TyudNO1Tx4ZLrvdlv4AuNppTdCoTNLw5Vs2fCmoDEPXFZgh4W3kJ6m+/lPWNynZ0m3r5GJVQV5+1ZJKCbvcVdklQ8d3c+72XZFiWHbY3W4mO/SNa+v9tIWs7WWrEsNaGRikMjYfvzEkX7HXz2TQPhBFhMEWmLHOW9LOxvSJ1AC2jLobfDZXGbzwtvnyaoji3ttjTJvPbKQMK3Hq1IVn9O9yMzF9Bt7Z9T45B2ES4ktxXNMfvTcj8snPh20XsmoKWx03htvlO1Ej56xFlZstTg2VaWb3hnoPO25ABAHrdeb6iOzbzFfkfxJVLYTHyN9i13bCI849U80/WlXcbxfsuMfTA4MI3JkYihak0izVLhjiSjmUGyu5a3Alu2AyME66gJ+yEUyEovqBzFAkJueYixHfhcy/MFf/AvLiGJ/gXt1oFrGbDQtXI9pFv1ggS1b8s7qO6kvbDaEQ0PFaTKR3p1W2BKNnerfidneUMh3DJiOh7WDWOTzTOUw/HyIDiCUiloM78wViwFzW6zsowWsC1I8SIbih3hMQ1biHNO2tSmDa1SUuocpqrZ3LAJn41bc+UjSBLoWGl26kpPcncVQwPk2Dd91woue6Y2kCwndFRA3DBvTna2ieoSiaxUYXnquOijShGUhrIWK/7MeGbO6AIeNsYAlwhjeorX8sIK4s3sbFuQV60Md7vx9+cgNpNaH7rRDFqIt6m92qzOR+D4khOOcO8cNie+SMMtYRhFo2pdgUIe1p7cM+qhSIiicsxs260Q2/mQHy5rr+mRngjVnbYsQLEa5uttPqJ4BIc0epWHHo/W2KH1l8LO4/rW0MbjNo5Kzjrnm0UWHY2C1Ym8Po2Eu96VHOBdSko9ndqyNz9x5gsWjRgITySGQMwGnc+TOlv2h0Ykw9Kxsbwfy2RzuFYKQW9iVHGFfbCIKHVeiPuT6Zf6bWDqDcW58iXe64jk9sUVjR0P4Dc/nLn+wATUqaQ8nE8WJtIKyfqs6vShalVFp3Iuleh2fpBQ1D1CCWnzhB0dXOfku20jhcpKEw/5uMew+WhDuDyiw0JWVY3XTQQ6EcuFIBiZIQtd2VuufMy2fFVJciiPV5TYR1K/QshoLrI0I27IxVzIGAkekbkaIhguLfqMuiUIz9lWma+QerM+R4y0FLFj3V9srtIj5xA0luLVV3o51zC1jkUDuvoetYMLJM1OO8ZZ+bohpXo6pk1EgwJWm5WE6dimz9mNdUobKlhqRWBaXBdfEVUgzbmvbOZnfsyPzbbU5LiLbtdVW5AXdi3dOB9GA5OG9cuNlTN6L6Dwubq6Z/jEChDqxmjVioW6bP0TVh14/Lhmk83+VjSl6kAt299ShsjNxdba4Awn2DZRljJMnM6d414PzYrg9L7oi1vIbVA61ONjSJ97/axdFyqGlKcYV7hUxWALE+NMVKnSLfjUXgostTuonI36gxGWx8WJEmQrlinlPBxOAZbrZ7pBGAnUTchx6jrdJuNWMpaNV/mRd2R0SWpWuMANV50rKObIbUzYP6KLJsqI6xbE+DlWiooPo/a6lJhmfR1oEUlKRLdhlhs8GbKxlKSOGHXqCNNjb70do1K618TVARGFBLHayzLuAlfe6Z2w5XVujAXrIAlL0SGRXBAwWmaZhIlWB7gf96NQiXM76KRjv01TuiBTEbNFa9U7xZk4r8MW7vPKSLzQA+5NaQEezchWFXyNW4xcuTZn5WGibmtYzVCW9ijTmFMNaWHNkbcwYw0CdLjxPsX0Q1pE1ki1rdopO0VgOBo5Jzwmq6wyMGaK1q3cI6V+WUC2erQrmobGBR5d4arEFRIx4yzCwt1a3zBK3Ztet67NWnL6iDYM397ACzglBaPB4pxhUg30UUFUwOZhi+zSJbGUpAQG8Ae5tRzzwUQx2dxfFNC7Q12+ajDPwLhM4eeUM5KX3rqt+eNV5zlc82Gad2vnuicrnyfiVNTlkNZDbbiFme2rZGqedkhg0EOp2fm5t2o25Y75pk/SdWGMbKyNtrXHPEu74SfMhnakEuLa4qiWYm3JyHrIWk+pB0YFtKipkFcbjsPROCM6B2uzlfR8LCmk2tHbgdpB1FUHjUnYng1tS2/neXQVuDq1hyuV9RinbpcVBbYKibVcSWPCqsw6Xxy0mCKWXLC2z8zlyIk46/ibiHPzcbCwAxyWVZKQB2RfOOrp1jkqvY0oCW9GTfFE0Y4WlLYrPbMGPerAYyWc34jtic8Ky5cToxrI4JTtCYxYGRsU1/Nyt1iuomLlr12YxdmyPrbq4JrKwcyyucX20Yrz89IoiNwoU03jeXKAPSJZGeJxN+RsZ+3F9eifg0FaYJwE7exVo65JXGDycryhoJexuBZmrDO7YCTOguXtJpRUFd0emNQuRn0gF+tc4rGcYDCt3rYJ6GW6zCcum/BoGldQ9sletOPdbgnn/JkXyv2mwb04VyqG6q9bI91kbdusTgtcOp/FfWOWCsyFB1i3zna4L92mI0m0WuG7QXMpC9H5UFguaDfu4HAe7k/cYSfTIYKcGLpTlvkwOKxu63hlaoDjGpwCQbPFDdgEYbaz4PPI6fxJgNqYCdfofsihS1JvbihuG4YZVCZP7w2UivdKFaWsap7zfVQUcc577DEJE21dX0ud1pl+t92Dlj6/1PJmVTgojWSY7S6FuVMt4zXWOji7ozu1b0aJh6+USkm1Z/RIcyGaKiuaegvxRywrNlp1lcG2Ad2gVOLPeVJ2rrVJdiWXbxRC2/rtUTpLQ2X4vMETzLCEwvU1Qghu0CxofzsRK2a739nHC5dfr67OXHLN6vkw1ZwN5RwEKiYtMkKWYm6wgp8OxmE3VmJnF1ikYdh51yCGuN2hZ0Mki8tOFw1ZN3emjcfXPqxy0C3VoAKtV7dKAhaoZYufJWK80MXNDjL0ausaDuXiMDod3xyJJO7X8E0/CS2zW1ZVTBRml1upsNQcV4GLYcI4VH0B1eSCIYJOtZylD0U0jRJo0u54g6RFrVhraFuEOcUecWQpLdNUGk3SJBZbf2hX225pICsS2+w3YTcaibCA46tn2CSEX9p0jnA7vLVAxWZLl4v79uRQbFQHuQ8ASQ1erOcpVXZXR1sAlsevKT90OElKG8zuRnvuEnsYRRxTctf0YdSL7ODuCTutBjWEMGsR8xG2KJAzxGjIvJUTVtm03dJs19fzUgicq9TMS5QaT0TorD1yMCxPtEALRsX59mhapauUuwOmh9uTSizdw2ZVLW4IejjTFrxAOWuxJpa79gAoYDsXZOqaeNBttC+QIPbjyT/Sayl0jNVS0H3KRPqBo6MW2eE1sVkF8lWoNV6iohV9C05a0Ocrmze3xRZhMi/M4GSNbACkN5+9ubdyiIxQIpfDHstpq1Agf6PgK4bDUmG9OZVeV8M5J63tVm8HKRtBNTVRR+QGN8+vh8wiR+yQaGgwbjz/ZiHKcRySZZet6TmOq00mFpe+TVVO7TYBA3OoxClkj2xZ8bZv0ewwQq6qMeQWcQ7k0IkLybmYC/JEkEqUSpSNjtS+W7OHYlOTBHeDZHcVZv7+toVIcbm6AldejHVkwizY86ArK8dbjrQkYkCvROb4CJnYi1A+WRpOH7LtulTUSxl5ImFziLU2aFiiGJxWziU68LcgATsukuivFUXNnau8hdwkbpNLhvVxvL2mjoFnZZkdqy26d6hDeLiie0pXgyIvRGtreaFDERCdm1f9kggIoqveYrkmAnl7PcXnLXncGzlt8Ctnb9WtolFrkwGuJZqrt6M2VRefxc0cPoFaZpb8qRsJ0EJDddUewygvpHkh4QPOHruRGVv0JhBWO3L0DVvbOXGry3TkjL23azRo461Qiw2bRJqnDoo5kOvfMpn3cKUgGGaJ5xEOGu9mx2xglFA2CijZjbyiNNBI769uipsWy657jr7izuVyszOuVIJ5Awvn4qJvWhNlgSkH/1ZS0Op4gewLtS627ZpO8Iq9LiC4acm9ulsT6ZagDfikq3I236ZQmmn2gTS0oLwkKzH0kaN7iw5UbyFyjGwv4jwljGITin0yr/EcLsMrElEXNi7nxGVrVgFEt1F4sTbdCvQypHAtoOslPxWbVehhZCZ2jCurl24O+o6iSct1hd96JPVDVRwTxqLFC83ujxsr3mmmMAqBPx9h5nq+nJQKYxsywxQJ3txijK15IdLrHdKHlzS2Mi67NfQqTjvoDJ8dq5PzItVFOMRQDopBU7niLwewmgJJbpit55VkMtWxPqhX3+k3Qr6bw2U+YkF3OVhd0982/qCOeiQKuLKwaVQWdbBjjomQpTz9JgdCQFy967r1eOPq75h6z3swjzVDWVbjWSmPxWk/DB5oPpoTjOmAuvGdGa0CNJ5LbdSGHWtW4uKwxI3TRkRyRCBb3yAGZrWyjr64sGO35BaUkc9vS7u/dsxxK0pNeqDzxIhv2c1f7DKuWiS5VrqaPFrDWvKXA7KJ19KYnzrZoZnkcMgHj8FldeQXibg5F+NuK0jIjRy3h+VYW3tvnt96Mk1upqUT8zRczGN9UarZer3+6aeXjy/TXdPn7ep/7mHzdCvw/+yO5OPm4dvjqvtN48DxP9/X+vxP6vPLx5fGS4A2j/utbd5HzxuU/+Nu66d/+Ixjmjo8ntxOz9Nu3dvN/M6JpreNXpLS79uuGb62Vd7fb/Z+fHH7dnr7oZ1ekPHA98vdnKKepN1Xe5neQgDmTU9sv3bV1+c7G/fT01OiAGylu+B5GD3vPX988Qfgk8Rrv8IY+jVo6snI50MTYNvqFXpdvvz+30stRyPAJQAA -->
