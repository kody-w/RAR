---
name: "rar-cowork-cookbook-blueprint-credit-and-collections-review"
description: "Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_credit_and_collections_review", "rar_sha256": "56bcdc20a1870820b0c53ed54e8319581617fc8ce58a93c03d5501bc88bbe0ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "blueprint_credit_and_collections_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/blueprint-credit-and-collections-review:c53068ae549158043ae1a8304d488b1fd3429b4c2055946daad679849992402f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "order_to_cash", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/blueprint_credit_and_collections_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `blueprint_credit_and_collections_review_agent.py` is
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

Credit & Collections Review Blueprint — Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_credit_and_collections_review_agent.py` and embedded as the fenced Python below (sha256 56bcdc20a1870820…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_credit_and_collections_review_agent.py` first:

```bash
python3 blueprint_credit_and_collections_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_credit_and_collections_review_agent.py   # or on stdin
python3 blueprint_credit_and_collections_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Credit & Collections Review Blueprint — Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_credit_and_collections_review',
    "version": '2.0.0',
    "display_name": 'Credit & Collections Review Blueprint',
    "description": 'Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'order_to_cash', 'advanced', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'blueprint-credit-and-collections-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba11a05153ec0c31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': '2026-08-20', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'order-to-cash/blueprint-credit-and-collections-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.474, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintCreditAndCollectionsReview(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintCreditAndCollectionsReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BlueprintCreditAndCollectionsReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6eXOrWLLnV2H8IqaqHr4Wu5A7OmKQhCRAYhGbRN0KFzuIVWwCauq7z0GyfW/1q+rpfjH/jBy2BMqTe/4yz8G/PdltExXV0+uT6ts5tLXTNI78CrJzD1oVt6JKwFuROOAXcou8qWKnbYqqfnp+8vzareKyiYscLJftuvGhJopryK18L26+ABZf3CJNfXciqaGJWZAWN8hJW7+s4ryBwG/xIWaSGDdQZecJYNHWTZH5VQ05wzs/yO/Lom4r/05ZdH7ltT7k2Kmdu/4zkOznUFkVgMavIRv6R8lpXDcvQGu/t7My9eun159/eX6Kween19+e3NSuwa2n5Ydqq7tMJvdW3/gc/S72b4AHEBkC4nIArsvBdelXQVFl4JbnB9D71Y+1nwbP0H/+Z3Kzq7D+6fVrDr2/vj5NP8c2n7SGmmJynQe5dmk7cRo3wwvEpDd7qKHKb9oqn8ypgefz8OWx8hunooT+Pn3340PIS+g3P359KoAK9qTy16efoKIC8qp2+vwycSl//OkFRMGvfvzpG5+6dS7AyokZ0Prl7f36nS0g/EYaB3epfwdcHxng+F+fvjNuej30nuwEK59eLkWc//hgDCLU+fkUsh9/+iu2buS793j9S3x/fjCOfNsDNr0r/tPz3cm/QPC7QZ88/1psCcL671gCyD/EPUPvjvor3nf//wPrNM5Bpn54/E/Z/dkC+O/Qz39p2z9b8AwFX5/WfhqD0rGd1H+FfntTZXb18w/et5s//PI7YP1/ZaMWbeXeObxldh4Hft28vf38Q32//cMvP//QliDXfDt7a6v0z3j+mV/vcv7gwXeqH/+4FsjX8yQvbjn0menQb0X5P6rfXyDDTmPv2/36Ffq+XqYXDE1GfAh9uOC7mqmBrt/58aen3wFM5MCa9oECoMr/4z+gQ+xWRV0EDaS6RQtgq82bOPMn5bUJA7X3ov5VFbj9/iXzfoXA3ancAUTYbdpA28qO0wmxLg94gYoA+vV/uXcwBLj5wNzZJ1a+PVDwDYDf23fY9lbdQenXF0iLgPSiisM4t1PoyMgyZIf+BLIATqcMqdvsSzeJBmrFD+g5rrgJduo29f8G/fovynq7s30ph8mkrzmIkQ0C50GNn5VFZVdxOkD2hFnO0PhfAN4CXKkAF8d2E2j605Yvk5/MCbEf3nNB6/F7321BC0kLF+gfxACjn0EC1EXavfeVOonTFPLiCuhTVMO9DwC/v07Mfv31V8euo6/5A5Rx6NGb6hkg+FQY+vKlrPwgjcOo+Zr7blRAP/z2+w/Q/4b+2ao780kGaHGPEILETiFelUQIVGmbAbIamlIEQNA9ir/9/ojHpF0OmimorTiI/ftiwO1bSkwWPIL0ESFg86Ti1Pnukv7oN+gWAb9A92YI6r1+/prfmyEgrW5x7X848bH44fqPkD/kTDGp330I4hRURXanvWfjFEy3qLwXiAugT08Bc0FcmymiUVE3IIFLP/f83B3ASrv5FsK8aKAa1FAdDM9QWwNTJ86/OoD15JwMAJXd/AodVjLoeUUK/kwOuosHq4s8ngL/nrOP24BJ9QPIseUHixdI9IE3odKu7DKq7Nq/0wX2IyNAr/tYD5jbUO7foKnF+1OM7tV9z7xHc4f+J/Rdc4ce3R36nACgry2GoAT0/8VgM1nFbLdHdsto7BpiRe14fqTgNLRNHnnMeWC4gMBw8m7O58DxgU0fqP01T2MQtmr424MyuGfdg+aBhEBdD4DM8c5/qv/qzjduQO5MyVBVU77bX/OP9vAMVAem1RPSgRJPJsAoPgU+3w17aBqBOp6uv40K0CMtJ/+AhIfK1kljFwp837vXRhNVU+W9xwskkj9VISgVN/qDVRDgDpIE8IeAEjHIaNBC7q4TQQWB8epRDp/k8TSAAS281gXaghLzXyBzyniQtSB+/hRyQAO88MOdFZT5wMdAxU8P15FdPpSZEuFdQRtUUB2H+ff+f/8K5O7UhYC0z8IEPG3PboAnbyAEoO76R1w/tXyPFFA1m4rkvuiPwX63FPq+i/1tKk6g4bcWASb/aQD4zjUA0ausvmclaM0geSOQue/pA/Lg3utfHu36MQ986vL6X/YOP/5724t7A9b/GLdXKGqasn6dzR5N8qNHvrhFNgMZEpd+/a1ffvnzYv3y6GF/YP/w1iv076n4Bxbvmf0KoS/ICzJ9tY9df0rd9xfwyOrL8vyFmL79mh/9b6EG4osMgNMUgWGChY8m9EECOlFY+eFE/GhK9dTLbgAX7lh4byqf6fBeKgBq83DqoHXxXQk/oKh+j90nZoOv8qkbeNMUGPrTNimd1K/9p9e8TdPnp9zO/H95ezSBM0hb4JJpazVBl181sX+/Ah4EioJEbe6Xf9xDSvcPdvoC7ezJhm+0HwXitB7Y4oAemdrNtMl6BrVke9Pg+AzIAdLHE15MBjRDOWn82DdNM9zngPdf5d6LGqCRV7xOtX1nD/5+ztWTlMdO576DzFuw1ft5muknYwEpePuk/dwYO/7TL3+ixvuI/xdKxBOuTEj0gAjf+xNTAJPKv7aghXuTGt/s+iaueMj4/a5e89ib/vb0ASXT58c88UgnsODfHf0miz9a9tvE35643Ae0uwPuI+6bDcI+tebvvgqnOePtkaRPrwCO/OcnsBgMSGBuH+/b8qeHUsCab8Mx4ACA5Us9jRozUGOAExgAysmSBIDidwKm27F3p58+vP71RP3PEeLVJXGEom2fJBYoSSMEbvuoTeMI4RE07aCBhxPYwiFcDCHJBUF5tu1R8wVNLBYLjECwAOhSg6zI7HddZugUD2DFp9P/u8P+04MNaC4YSQE+JOW4HtDDRuk5QmOIgwDdfY8kfBpHFySNUug8cGnXJ2l7gbsI7pEkgjouMMPxEdub+L3PmQ/d3j5m+o8IPfACqJJl8aQ5ZtuA3xwlvMXcplwfRxzc9VEM9ea4j5ALPKBpn/Anzu9L36M0BfFh/pTGYMQEA143yfntPepTalIEoNwRNcc8XqvZwrApbO4cIweuKP9MKlzVkkbBz/FaaZKaqqJ2e12K4aDOjxYr4EuWTK52JjHDrhE4dC0rEVwcF0mHS5m/MUbBmMPGbh2buDTy6Thzqc2q4EM3zYojH8QavFdLIRNUDBkEkqq2FI4R6ca+OqNiqik8C5ITrY+2XqTDlcI42Fu6Vp3Q82h0Mpincuu6MNf6jnZhRhQQzln6xLVcW6Ie6c1FmRtG3Et5RCkVzl9sROi1TryoV1UtMkPb6ua1T1ujzLkVcVgMYVFGFz/HSieydvselnfjlXZPewqGNxtPPo3zGXdUuuZ2dWpUWO7QzDBRuaDjtVl269WwGVqPrWR66bWsYbQDsudxVTOuCGdGN68l0Gt+bajV2jDcsPFYeb8gxlZNx1RbWjvdimM3XS39DZ+ec4nMy8bZp+ttv94zrX80QdmSw9Zvq8qKB53AD9XccuCouuFCfNjE7H5TJhEn9ge6Qu3yUhv21VRSAutuS6bgsSEZsyOf7QPL2ZmLOR1Gyj4kWZNglid/v5MLWcijiksxnG0vq7l3OSR7c7lJUKWHxeGqFKcYpjCWUZsiEE4cIoZr2vYOqnTTPb45bOuTXbk3j8eOi3OCCcdNthicgiph11l6J55t3NuKVsb4kLJpLgwRTY3HPdp72UDQ1HkZj3WBR1nqoLduhxDzM7m9yHx4s3B+LWWOU1Kpe7OHRk7UMi7RdIPcUN8vTKe9LpanM24c2YpiB24z66sbHcdeJ+7PFHmCV550imML9FhCScS5ttsSkdt71MYwslrww9YJYNKy4y1qkbnVe5Ez3rw4WGHSKBGHGbUZrXpwzmQrRpJKE1nV6bnNmUTl9phwCrtTGM2LU05oqdk1256LZ+hpsd6SwXhcz0S51iKySos1gV3HhNKz8UgXiwx1qf2AWDPTVLcEFnmVQhaXxjrINLMNtoeYSDnkZvMzJmLNRdqkG2zZNgjXnJaXQM9CKhtHXlud46RyT2asmMRav1nMTU90VGPtoy9ELY8pLLcVG3zVnVfbldI6ZC4mZEhry1FAc/fq36QOX2Wm52OUj6r+sWaLrXXdStogpgnVpoRzFEqY0mQ4z2LHmgsKqgU0sgnxY29qlenTEr3qMrBxOB9UbD4TwVQyll5/zncEujypDAJzimmJpiemCH8Fw2ooVNUZZ7RiCBbMMJt33GBWht3v5+0OZxBDV9PY5JnDiCmDgvJps+4w4YDRG3KmnASmPx3rAqHh2dCrR430/IqMW/m03TC+Wu2kjAgalFcSvUC5Ko1IAd02oje/oEqFtZ6wqcs95yTZzMLW5Yk5JPWxoiKSZk/kfpkLWIrOBa6gN91M4AlUUHV9NtNIPikQ5nqh+YHbJYZ6Q2QQu63cMLobzw6MhhFbMw9O43mx3UoYdR77DUtrBqeSCJVdG6G8pUsn3JfJXvSq3fYc5snJpwlxG18YmvQ2pek0WVMHtnG11y0PhsKhW9lbGCBDXXFXXayIte+0O7tDWfGKYJ5ErIlTrPdd280KLJTxcr/E8NbzVluR0lliYZXX0LklgVl4dX9phyOHrxlke+Lt+c25XeOUk7OgzYA9Xc6TwnG+4HYMH+FWzXZ26JAwvd5n7bU6zI3bEuSsuVuarFIz3jJkrzm22vizwkT00t2DVDPXEROWB9/D4k2TwKYzSvA1raqbssu1RCyraqMWBNLDhbznKIMgSmZlMAXl8jbQwDXovdrUkoSfXeYQo+eysW6bdEssEot0Fxgt+FZubOuSXNCwNlBtthcGgafr5rw2EnnWp0aR7gRxOI/tcBC4OblRypkB01Kw36/rKpPPcqrernQzX8Aaac1cGEY0kE1svpgPF5gVl+EcpekE5/fhNgkjoiwPOxE0LTTulmq1cKmq2Q/KqsdCzdig2dXdK/wuXe3lOU7D8my2n8kEOfcigz8mGNcSc34nsQXsNOLxIjOuNTKZtFuEGq2bm4Nt+7qwvPgkZVqH+a2T8LpI+74LHXZgpMa5FTQv7WDerodgH56t3oZPETmsb7Pc6OdIo7ljVjejWl4IeUfcVgWn1ttFWuX2ORklXOcDpiT7lSL6pmA5PcVSrb5IZ8utATogetUqjMoTEHnjumtXYhIranGVTPO4lRbmTEQPHSexfGgFJQxfakUx8t67aCV1jBRR5zems29nV4t1FwxyLdjuNB8LAlUog2XPoa3jQ7q61Ytbu3HpAKb02lyyW26bC7mG2+XqSLhDvKqta39uaX8z1+gYoAuNJI6C+BrBYRoupMXqpJ+3Aj8IhnG0OllDgxOsU0czp4rrTXXco3Xyt258dHt65Z9hw5Eacj6v9LxcFQnTK6bPxh55LTXHyNXUYjMDTa4xn8maT2Zlds6XHYmfrvFmoD0rJxIrOLGbxRXLKtNyV3wWEZ7aq6fTAc/0nvEOm3yrGwvUI0q5ACzsc9GrIuWxG9CarlJaBrE5V09XnVvDpb5MU8JYeoVatsoBOZJnkV3p173JcSUWXQtSqtjqdFiuVJi6LeeNiO1x/JiWS6wQqHxH+/u1z80csZMGVyE1LCuchKB2fhuyJ/3aGKZfLrQ6IUx4NgNbGYu2DlyYCFy5dK5Ha5EjoK3Kp/2BpnbB7hoKYnDiu+QgwkF91C89KkfeqdMPYYuMMnPcbBYyBm9XHKNsVwODUdKVZOaeIB3Lek1uz9uDrywOPL+Q9haqmuhxI1oFL1SIW6B0pNYnkSCj/Q0BGLvfR3OeCqyiL9lR2VKBa6yPmxPBhozqM5R1Po+dVCxdXbGWh3RXXzSJdBjQG9zUulGWusCwkuHYci/VnClkakxm9mJz4bKc2hNH0TvVnaMkA9PboHmOAblSiI47M5xktDixjSgepI0llOlad45mGoZcW+ghu/db0TqdeLkkYSkLZMpMSoO/ckoSqyv2VJlLXVjBZ8OGD6YqSsO4OPHVRbVF2rso4WCTKsbniuokt/VwYGC2ENNDlV3bWzwoxiZdJ3xq9/i1csKOsKxbeRymea8N1nxhqsaxy8TMOl6FajBRtMeq5ArX11BVJLO5eYqFWfx+pazlGtd3Eb4Zlcix7JmiXFiU9XdmYu949qClfoID30VsuB4kutJKDiTecn5oilgfXLPuVnHaV3gpaX6CtUlSE1oSbaKk6kacPhj5ucF7c7ezRGxbXDYh2yPVMthKa3KTnzCXNiuOLlKx2u4VE1Z0MHHWhqGxBrtTzNbKXU0MNP7c+ZlrIataF9BrqwvphR9PoucdycPRVpqbVh0D3ybYinN4Ew11Jt2AJEfdW8QAtArCdYO0UWs7YzKziLOGLhE6LJVyrSDyOfRnxDCe1tKF6JPurF8qcuWpJbuCd0PO+EN7EaTzXI1Xa14sQnE1U/j+aK7IzbpCL0hGW0h3volBo5nb4XKOycIFkzq+JNE9GATjS3S7iDrOc8t0OQPtbINIuogjOnKoBVgp05gbxUYyLgQWu7xxJKtgwXL7Rot6OmJsvCELObpcWOZCXBCQMPQaiTa+VHmjE8HRDV26ntZEMEXMvJN+QA1c2/eYrcdzNLYX2HkMhtaN1bG+7LRTL2GtVhxQQllylKLS25HPM7JhB5nCSSrZL1a7QhCtxpPEFs2QNtm5azDCrnAR72zVXaM7G77IcN2uD0aEG51/7eahm7ejeGPOOwnr1i4xiKtqM011vFViA8chm7VXk9kS7wo2OwlJgV/6JJ5LGOLO8tkm31UzaQRoJlbJsN46mXUuiz7eXLQzOXa3gDxg1Op6EvmQprcOji32hxUrNkYU5dZw3F+WK2q72FI5QacyI1bkkrIbXB6q/HRcNY2s1ZJPj00333cd5aonfD+D6YsE67qUSgq6wi14FsML6bprHJjdU36xwIadtcrbSrNxMxx3ugrv0UIV1w65GKylQM6IZqZsa21ZyDGcnBl+CSrTawUuWkQwUwq5yDJ82EjKnM+CXLYlytHnrRYOrr0TrvXFpTLtVnNepGxH3TSIdsSznXS2snM9NOxarggBtljHc+k9YZ/ly1DF8z6Z05sb3p2UE8bRp55c0kF2xj0v6m46ucXsPhWWQqdE247r5069363X1nmfnK9Fi8mnW7GNas8m5i2KZumsmmGuKbACy+tp2TOHYbmB23Xj0btS33ltgHhitIoWVwIpYmole655xLyLbeIpCeYovBrtZTkGZSyJ2KI1+gYfDvaNH2i2wf2IrXs3iFGtUIjorNbWrtjZel5bA00G8dhGOhta7EJjZ0HkC2acWrKBHHiYa0sGz0heG/uqXqF7eyniAIjXbE7srUDrxY6VFEdKjioYm8kj7/O8HAy9dAFb85E+KDN3T54Hg+yEAoMd9TxkK9bc63NvdyCvyHITkoTJkF4U5N0yVT2XsNC4mc2E6hLKRRXkVd02pjQ3MK50Mqkj56F2zsi83vRY7vAk2P/pbK/3uNAEZhCdtm5z8Ugc8U57RxqDJr0IrLRy8fCGwm4BowixHaLQoekNn7s7ZiLryDwpajOs0ZBgbpvbTdo5qljnYqjPA3zrk4aOzHOpqRJzWxwI4N5dZbizY+YCBLRvjJA30m7jRxtPrXuZW8eHYOQpaUi4E3jLU7lYDhUVZou0W6ON00WbjmBQbB5I+u5WYPKimQ17Mr3gssfMQZvp5vSJkRfjSFDiegxFqqH3nbGPllROc1EzG4urpUt9daGVWhOpnroJqILD82Uwy5aX3ZKbj+354s7UaIDZ0wrMchs5XJ9iYVexnjcDQ2/RU6i2iUXJtLNFkEaXmbnY1SWCLsOklKlOvhyPiMuzAeLIIiYm+jlLI7fcpkGF6tzIrGdeMbc7PtsNxHgNdUSa++EyDdBajYTc0mncvdob72Cccmx+JSpZbES8KtvCQ6O5pYaEkFZtBI+7wZUKztutCY/3giSSg+OWol2GaV3uNJDISj3TblsYcsp0VQZ2n8pYjEf+ZoplizqlIJi4EWOXuhoufZrsTnNLG48O0VKiFB66IT9qLklxpoL1A6GV3q6WXbpBbEsuvFOQiDwi3kaxP1Td5uya3SD3SnGViUgnMWSE0Thc554nLatwZ431dkSX6jnL6vNlKY2IpO7OMaHp5vFIFrMNS0rHdXkBW90jro+mLp9Osad1hLjPHELlk5JhmL8/PT/dn/k+vaIIRSyen6YHAe/H+f+NU99wjMu3d4b4HEGfn/7fHUM+jgQ/Hvrdj9h923u9S3/9t3X95fmpcmOg1+O4uE7b8P0A8h+OXb/8iyfCE5Ph8Rx7elLZNx8PRxo7vJ9bx7nX1k01vIEdVHs/tQa+b+vpv1rq6R+fXPD+dDcxK5u3T6kT1Xefi8rzq7emeHPtOgLXttdN7pjOUgGBH74f9j8/eQMIY+zWbzhFvvlVOVn8/hxqOqKdHkQ9/f5/AL2nLhXhJwAA -->
