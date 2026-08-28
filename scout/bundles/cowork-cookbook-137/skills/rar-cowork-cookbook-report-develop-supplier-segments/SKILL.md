---
name: "rar-cowork-cookbook-report-develop-supplier-segments"
description: "Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_supplier_segments", "rar_sha256": "95f1bd5b691a32b2ebe95343659c693078719d6f5721f31f844b59cca47efb16", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_supplier_segments`. The original RAPP
agent is preserved byte-for-byte in `report_develop_supplier_segments_agent.py` and in the RCI capsule.

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

Develop supplier segments Summary Report — Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 95f1bd5b691a32b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_supplier_segments_agent.py` first:

```bash
python3 report_develop_supplier_segments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_supplier_segments_agent.py   # or on stdin
python3 report_develop_supplier_segments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop supplier segments Summary Report — Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_supplier_segments',
    "version": '2.0.1',
    "display_name": 'Develop supplier segments Summary Report',
    "description": 'Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-supplier-segments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-supplier-segments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c0a665999e95fbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-supplier-segments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-develop-supplier-segments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDevelopSupplierSegments(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopSupplierSegments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportDevelopSupplierSegments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+ZOi2Jr2v+Lk/FDVY1WKICB140YMi8omKKAIXR3V7Pu+CPbX//t3UDOreqZ77r0RE2NVpgvnvPv7PO/B/O3F6tqwqF++vKielc92VppGoVfPrNyd0cW1qBPwVCQ2+Jk5Rd7Wkd21Rd28fHpxvcapo7KNihxsp7oodZuZNWvaunParvbcWdNlmVWPs9ori7qdFf7M9XovLUpwpSzTCOhpvCDz8hZsdNqoj9pxdo3acNYWrZU2n2Zt7eUueJ7MsWvPStzimjevQLs3WFmZes3Ll59/+fQSgdcvX357cVKrAR+9KHeNzEOb+lSmPnWB3amVB2BZOQLnc/C+9Gq/qDPwkev5s+e7j42X+p9m//EfydWqg+anL1/z2fPx9WX6p3T5rA09YK3VtMBfxyotO0qBF68zMr1aYwNcB6HIn3GJ8uD1sfO7JBCMv0/XPj6UvAZe+/HrSwFMsKbIfn35aVbUQF/dTa9fJynlx59e0+Lq1R9/+i6n6ezYc9pJGLD69dvz/VMsWPh9aeTftf4dSH3k0Pa+vvzg3PR42D35CXa+vMZFlH98CC7rovdyK3e8jz/9lVgn9JwkjZr2n5L780Nw6Fku8Olp+E+f7kH+ZTZ/OvQu86/VliCt/4onYPmbuk+zZ6D+SvY9/v9FdBrlXvMe8T8V92cb5n+f/fyXvv1PGz7N/K8vjJdGPagOO/W+zH77ph429M8f3O8ffvjldyD6H4pRi6527hK+ZVYe+V7Tfvv284fm/vGHX37+0JWg1jwr+9bV6Z/J/LO43vX8IYLPVR//uBfoP+VJDnp59l7ps9+K8t/q319nZyuN3O+fN19mP/bL9JjPJifelD5C8EPPNMDWH+L408vvACDyBy5Nl0GX//u/z/aRUxdN4bcz1Sm6dgYS3EaZNxmvhVEzA/+n3q4BhtRNBAL7XAfqf8rwZDEAtF//07mj5GfniZKLB9h9eyLdtzek+/aGdL++zjQgt6ijIMqtdKaQh8PX3ArAtUlnWXuNV/cATeyx9T4DHPo8vZhF+ezXfyT6213Kazn+egfM6IFOCs1NyNR0qfc6eaeHXv70xQGQ7w2e0wEFaeEAa/wIYOon4HVTpD1AtikSTRKl6cyNauB2AeB8kg2i9WUS9uuvv9pWE37NH1CKzB6c0CzAgndzZp8/A7f8NArC9mvuOWEx+/Db7x9m/2/2P+26C590HACmP3MBLORVWZqB3uoevDElFgDHPRe//f4MLhCTA3IBmYv8yHtsBrWZeO5bpFWW/Ayj2Mz2QIRBdLMpsgCfZ1H7OuP82bu9T/KaEDwsmhYwWAkoycudEUi1gDvvkcyLdtaAAmz88dOsa7y71l/t2rqbmIEmt9pfZ3v6APiiSMGvycz7IrC5yCMQ/vc6eHwOhNQfmhn1JuJ1Jk3VOCut2irD2nrq8K1HXgBPvG0Hwq1Z7l2/5hMzelOo7q3xCA9YBCLjPFP6eco5IHfA1YBr33Tf11gTq2l3dqu/5s2z7K16SoUDaAAoDbrIncjgb8+SasKiS917/IClk6RnFtxnVu41yPzlHKA+Z4YHg8++djC0XM3+T6eLyUByt1M2O1LbMLONpCnGI3DTBDQF+DE0TfJA9Tya5Dv3vyHHG4B+zdMIVEE9/u2x8h7u55of3FFI5S4f5BpYPsm9l+JUWnU9FbH1NX9DamDy7A5LIBugb0FdT+X0pnC6+mZpCJpzev+dte+pq93JaVBus7KzU1AKvue5tuUkwKp6aqdn3EFdelNkr2HkhH/wagakg+AD+TNgRARiDGJ3D51UADdBJ/l1kX1fHk2zELDC7RxgLRgxvdeZDjpiqooGtCEYaKY1IAof7qJmmQdiDEx8j3ATWuXDmGkqfRpoPXPxY/yfl75X8N2SyXgg03KtFkTyOiGq6w2PvL5b+cwUMDWbeu6+6Y/Jfno6+5FQ/vY1v1v4DuKgldOJi38IzQy0UNbcS21CogagSeY9ywfUwZ12Xx/M+aDmd1u+/LdB/OO/NqvfufD0x7x9mYVtWzZfFosHf73R1yvAAUBhTlR6zZPKPj/b6vNbW31+a6s/yH2E6cvsX7PtDyKeJf1ltnyFXqHpkhg53lSzzwcIBf2ZMj6vpqtfc8X7nmOgvsgAxk2hHwF3vlPK2xLAK0HtBdPiB8U0EzNdARneMRVk4Wv+XgfPHgGQnQcTHzbFD71751aQ1UfS3qEfXMpboNudJrHAmw4p6WR+4718ybs0/fSSW5n3TxxOJngHlQqCMR1pQM+AwaaNvPs7q3OjKSLT6z8ewOT7Cyud2qqYqHLC8ncAvVvv1sC0qQ+DaEL0TzNgcQDwcHLoOvXiNA/YwMEGYKvnTh60YzmZ/Di8TIPU+5T13y24tzPAIbf4MnX1p9k0EX+avQ+3n2Zvx437AS7vwHnr52mwnnwGS8HT+9r386XtvfzyJ2Y85+y/NuIJNQ9wt+yJmiYX/8QnIK32qg5woTvZ893B73qLh7Lf73a2j5Piby9vaPLM0nMqBMtB235uJjZcgEIGCsH7R8mBa//yvPjcD9APzCtAAIH6S9tFbYxYWghsw57tESiyQjCUcDACgfA1viRczEdxeOkjS3+9WtngkmOtcM+3lxiQ9yjcbxPlR5NNHuR7CLGEHRfBYBRdEUsctggX7LAsF1qvcQj3XUAQ37cmADyfjj4cm6L4PrreC/Xh728vNrYCK9lVw5GPB70gzhau47YS2kSNeYZ5WXB2BFW2W9AnzRLlAtMYl84CE3GLnNy6SSSXQlIyscTArWFRfXH0HW4+miucHZXteMKwaMSuwbkXcz7B3TnOdp4jb08XBeP01abQq2yXVVVJ0ftR1q0lq4clhGC3y2WHGJlQnWui7/oeZ/NYHcbrLbi1OjZ27SYaIA7R7La0Gnb0oMtY8+alabGrtcx6XVhWlzKIz1mroH0sjeiY6j0jXrbwhQ8xKU7nhBy3hOvfOoI84b5/6PC9Z/Tnhk+rbAxjbZchVSptUlvYgxfasVkN54N5Yg/rrSeNJ2h7Pp79+FqZVhWjy83SGTfCRrDhW07Bvu5vnTSl7WFfYGZF1LRkWnQ4BK1spRcy1I7LJczbqlJl6naMsKFL7daNjxaxHYYGExYCBnfKPhe1PaVnLoeyl2iDQktr5K5tuA+1PF3SPBRztb0Uz8dqxA5nway6dn2juLDdhBm0oWi3p82YMXeryy09AazZ1a7mmPxKwdp1ZDF51IWKM8z1w87CLAMSOR2ps0SO4zkMoMe6ijZaMXqj+6xgWSJUnnXJW/SIfcIP6VXIVjcdbtTqeAuZnbPEb5B2bi6dHQ19NiwdDKeiqjMucZ7ukHzeS2F72evxDvPiasj8TQK39aqnS5yuTYjQaQSC22glZApquaFQG/ph24eupBVaQ6UxujDjah3tczXEIUpOxfSwHq64TKkLU4CvoaFBtaNFW0RYpnCrCBl04BZ7Dy5hszm73jk7wXl2ho355TyUrakNnNyEfIaxfL2i+Gpz/5Er0VUsq9HmmX6e0wyxNue3Yb5lFvQogvQOqrcIF3uH4dFFd0jU6yjfEi3X9bFd1qNuHjhJvfl7c1vqrZnthGPqi/XZgDptIzfxZmvy81DfNmpr+K2LI51Jt56YnI7kLvaiVBjGbS6nC2qA9dLKjOtZsg25dI7t6njgRsYUNintRAbvrc1OQVRu3B3rYXuCDJTNzpo+YMkwrLqYi013LWoktmhs1FQ4Z4XCirdzkquS8s7eNugFlfFU6l952g/nHiptL5QE5cZqJyttCvX5NiPww7okAsO98IxC5OvmthexLFpL53S+T3xH2krrRAlPEqun62FvlsaVhoZIJctgXGBKMq+rzjpkac9oJowkRJWelfXxSiSqmbROkXA0su43l9Cza4y66ecsaVzfR0/cxUDySwnt16gr2POQ7DW97bq1rSW0vhRJ53badnXZqNqa24juCjkFnRYdBOEWn3v/fKHiJPC2ZIqx+ZK5aqbUmTtzXDGctoA3PSjv436YE8kpGlWd7hcr82SsG4jXdVTk2ivroutWyTYXkaaXLbOts+FCKFCK1Yah8RSZqZfNfpmudDXbbqpNgmd6dKthTxckRj67SBwjLZzt0TkBcSsM23vrU6a1jO1dZI91vZHjqaU8mrAX0Xy8ItPFcnvVMF4wi7T2m2PYoe5C3hCHwYqIVd0fDW0L91gSJMxFlppNJ0E3LRaTY4ffFA7HQPWo2NoMpYxSY5odb0LtOuF2M6wT3lus4utowJEmn2E0RvFex2FJ8E+c0hYmBk7L8X6zg0jW0K/UyCoWpnH9iiQKq7T39gBXBsGcYjI6JnsuA+6314uVGD3JrClaTzcbzSoo5CyewzTa72/lLSPJcldtbbQ4BcFObHVvt3YcAlWvYXnqGogkKMtrRivPrqhrFrpQIqpu+X4fr1D/Is13McOq/LBcowTPK8myX+5SvSM4mJJOrhyWGbVYGAHluzeEtYs9ozjRBVYPc8J1/cMlHxXmhlolmx1SZl1U4Va3+7GsjZDUR5pVM75wlmIhroKIV8XQGS2yJWF4fdGCSt6FBSUWkr7vj5vz4ERY5WQlrecegPRwriqShW8RshvdzcHANNpdabiiqhRZUSN+5nHd2gjiwUPkwugGOTPMdQEnhW8q1eaqecMepavNcLVJEbE7szMbrA3GLEpSkhtqaZ77O4awrLFz5XMRW4qwxHprF9rdkYjJ5Gjoe8ArlRCsCFje3wAuOh4c1uTA8AfrhC48U+CvVJBkvR24DtSi9SUNiauy5RJnW2VwyWUnn2gYd3NpyZBWCSR0/CTesam4AfP7Vb85x2ATlrEJd/Nqc0j8TOQPZnhgLIGQ+g5Ly4ppuY3WlK4K+FDl3KujIgufFqEwZgIaKo5qejOL/kQy6pqjONjqYJnNs5qONyJ6LFKKj3KI27deIPAbl8qkpF7mVHbjQVsknFtcsNM6oc8HYW3nQgkz6jVTE/y2okjIZPvuMh48calSOkIllmhcN90YmrBhu86tLDhtCXPlch5cRwmZ3yRlaUqMr3F8CVgVXrc60ppuqhIEn1WFLhkHQl/CbpQoGZ5Y8cbQZHxbiQWKpsQ1YAEjiXS50ApYwvYhx9VVmSHY5iCSR2wwHcFiq0pyC05YJ2iRNlcL2xTba6fzFH8SNoA36UB3KFKYpxsRMXz3cijZEyxYpILKPWKw+npYLHudLdCNmKcF5c+Zsa5Pjsvd5JLBDznnzueHfpCJhaOPMR8o3LHFvJo4QkGQyXV1Q6rWwksq6RbdWUPNnCPaM7rPN7gFI1bewpfCVjYxtx36Lm1IJQz2W5VqIBa3z23CrXTF8HHKMc+gQ7mWHf3chgapMhzTCXBoe2T5JmfE8ymu2ATQaikzqttnp2REL+qBBrluzxd2f0T0Mk3WtQ7zOllGWr6lEul4LUQmu0kCJCM79nS0PG9tuUY5J7vbRl8OIuKfCndnrcpFllCic+E5YRWY8ngiTZGeX4Moi41rW6m8uuV5dI8iyemA4OtsVymCEB2KZQqN2T66ukLTcNB223rXNUvC1RAAWhjQqDY9b7sWfB2Md12b7qVraURYm1SFGnhzbXVRNLllYlPvVTKkIvka2x52oTlts+9Yq7gZG/3S9wOBG8vV9eyWaiig5Qi3KLY0juGoKQV6oUSM3lJnsUuSk7DYlqXWhLEpy+zc4Htoe4uYgchXu1tPDavV/LyJ4WipsZQcFbrNndTcLoUwpsfBsTleUW4DpFC5n6jKyqOE8mR7dNofWGZERBcidp7MJWEi6Ta75TnprFH5Kh1MMArhlxDq6IuMF2dhFd2oIYAONofCGkyMWxoWcIvbnxfFoY9pWggIY749hSIpLHfKUbyt5pfdRT/yG24Esy52tKw1r1UQLezHoMDt4WjBClfvk7SwC4nq8LXvhAe2oA66FAlzbnssOsukSZ7ZaYRCuBLVsG3LEiE30Ozlphkw0lxBJR35VNSRNIMuWoIy/G4/Zo7Ve4wLuVUcBikcoHLGhIXFM94KMKcn4DUJTpsnWhIdb1e2HAoGBp9qcu92MuNk58qpIUGcrVm2W56Y1OXS5Igtcnd+A0zU77eXAQnAsGY5Vsn1/do8RXZqw0hx8sNls01bbmFQkuLpYm0Pp6vdwRLLGnEoc7JcGTRqdYfucLi5o5jmWud5MrWEWie4ZHQk9Ju+WJ23tpBelZA12+FWFdt6R3BtaY9ItayWc2QI5pUU4u55jXbtqnS7LVHxCtEyV6KL/BLRKd8OFodwrBC8cFgaacNrbpxu5Ok46uvlXIbwc1jhYsqeG1c84iS82qaS3dXZXtzuFmxvIguRJ/eoS53VVceIttZD4yawLDRz5S2hsIAhcY/010ca2fZDkd10HxtIfLsryAWPL+3kAh9crpf6mLqsL6nb42VrkEfER84tuuTcNpg327DnTzsxrpDrIr2iQt7h+IKIAKOkGBeJHTNfiIsVpuqEuyryhvcv1kbai4uM3y4xgTH1LFjHB0WVybquRvbEJvPQxmnzuI6uVkKsigtz3LA5awchOGv5Aa2ES+VcdMGVzwmdWrn2ONfAeeDWdttA3PKaGoOplMH9o73TQ4RfiBaBareMuwmeuVP5dEtIrtqcW1Gi1zuOwRY0Aapi2UAI64Dx9KRDnotELI3jAtYnIrHo9gt1J3HFfr84LmTs1rc9SZo6j9Zy2Omx1cBeQ7i7DtXDha7Z0W2hH2TI3oP6XB8MKgWs0BhgblEMl4HxHD1oe6XdDbhtzIdorxg6ke9tFml77eZLVmVvl7cANZbYgGxu7XoRu32yh6HjaUW7HaGOVrNeGIPKRzhl5E2CRSkSegM7QLeFgBRHnQmY5a1mBnSLS3ZRSV4daR2nFjWrUI2Obxj2WuntUbRg2SNIMJoTGXxs1goxEMn2FkOprewIXhMjRUPw6pJDGNf0qziE2WvUgiMR6thzotx7jnLpNtmx3nj07gaGloYFOWFXlrC05/5JYFcMlYk5slZY3T8hUn8ZsRUOGKsLGsS0PbvND2f1tof3aC/NT6Ld84htJM7qeGnb/RVfw5k832FwbPO1a4OZlbASmXMQcpnJFL/fGzK1Niy5Z+LKIYKVymHYGfXgdUfqXjfU/W7ntNsAPrGXATdEr0Latqlcyy7FRodqPYyry3FrymJt0L0CO5u5QV1p4daF7aFGjvgJ29MCtY5ZQmnioQiVqxfH2FEQu8xLoJ5ibpob9w4X4vRBR66rNTbirj+5Zi6IixjMe9qDV3BEEoudLdxcIUSV3XqJS83eW8rQQoWUOYKiF+VC96qclk3qAuxfiq4AI9hhsQ4bcX1mPAKh7cup97WIFLzdaaDcHVkS6rV13f2ibgQPk6rtbWt1nd2NKjgcZ/ZCuh0lipfppeRvtdvCFYy4QCmmXEY4bgfVIQJz295dNYvihCJWqZBDuKl21YVaHFetvGdWh7XLG4HonmCnczwAX4lAaNZxXFL9nEhF+AaJAHIqqjime7Hy1XKeaxl5CK8LJMra+lr4Ca47ckCebU4bXIvs94sG5qp8TJDSPjFyvL+AcWDFLlMZDaEaU8Dy3mtuN9JRbCWa41FzPMwXGZRcd5d5QWrIYLHmhm+drsDz7kYiPhHR5xw/gB/6qpDOuO5USNAlnbXqqiaKjVAu1omYIZf9bQdTcg+OuUxLSXFnub3FbFSJ39LHDe6b692i4hkwOvG9dGja4SizNU7KxsDItW8fWJl3tRiTVvMYa4eFQJLky6eX6b7x8+7vP/0l7nS37X/tpt/j/tzbd0D3+66e5X656/ryz5v0y6eX2omAQY8bm03aBc/bgP/ltubnf/TdwbR7fHwvOn1VNbRvN8lbK5j+qOclyt2uaevxW1Ok3f3G6qcXu2umvzBopj9CccDzy92prJxuFz8Ufr9F2RbfSmsKYpRPX714bmS13vNt8LzD++nFHUFaIqf5BkL5zavLycPn1xDAMfgVel2+/P7/Aa5VNAQmJQAA -->
