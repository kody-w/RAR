---
name: "rar-cowork-cookbook-vendor-invoice-three-way-match-status"
description: "Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_three_way_match_status", "rar_sha256": "ab6de39d29ae627d5cc4f914fb2adb470a2375a1c6b2776d99665b90d903e804", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_three_way_match_status`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_three_way_match_status_agent.py` and in the RCI capsule.

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

Vendor Invoice Three-Way Match Status Report — Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_three_way_match_status_agent.py` and embedded as the fenced Python below (sha256 ab6de39d29ae627d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_three_way_match_status_agent.py` first:

```bash
python3 vendor_invoice_three_way_match_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_three_way_match_status_agent.py   # or on stdin
python3 vendor_invoice_three_way_match_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Three-Way Match Status Report — Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_three_way_match_status',
    "version": '2.0.1',
    "display_name": 'Vendor Invoice Three-Way Match Status Report',
    "description": 'Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-invoice-three-way-match-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a903f9e2efd4ea5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-invoice-three-way-match-status', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'vendor-invoice-query', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class VendorInvoiceThreeWayMatchStatus(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceThreeWayMatchStatus'
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
    print(VendorInvoiceThreeWayMatchStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abOi2LrmX6H3/ZBZ151bmSFPnIhWQEEFFBXByooshsUk8yBDdf33Xqi5M+vcqtunOjraHLbKWu/8Ps+7YP/2YjV1kJUvn18OwEqRlRXHYQBKxEpdhMvarLzCH9nVhv8QJ0vrMrSbOiurl9cXF1ROGeZ1mKVw+6IJY7dCLKSqrbqpkBLkWVkjmYfcQOpmJRKmtyx0QHUXXQcgLOH/JQCfWqv/lFi1E9y3AsTyrTCtamSnPtb6WeaO8hwAlVVvUDPorCSPQfXy+edfXl9C+P7l828vTmxV8KsX/a5Peqg7jirOVi+PCg5306CA2Ep9uDLvoe8p/JyD0svKBH7lAg95fvpYgdh7Rf7zP6+tVfrVT5+/pMjz9eVl/KM16egIUmdWVQMXcazcssM4rPs3ZB5Dt0ar66ZMH2Epw9R/e+z8LinLkX+O1z4+lLz5oP745SWDJlhjYL+8/ITA2H15KZvx/dsoJf/401uctaD8+NN3OVVjR8CpR2HQ6revz89PsXDh96Whd9f6Tyj1kUIbfHn5wbnx9bB79BPufHmLsjD9+BCclxlMqJU64ONPfyXWCYBzjcOq/rfk/vwQHADLhT49Df/p9R7kX5DJ06F3mX+tNodp/TuewOXf1L0iz0D9lex7/P9FdBymsJy/RfxPxf3Zhsk/kZ//0rf/bsMr4n154UEc3mB12DH4jPz29bATuJ8/uN+//PDL71D0/1HMIWtK5y7ha2KloQeq+uvXnz9U968//PLzhyaHtQas5GtTxn8m88/ietfzhwg+V338416o/5Re06xNkfdKR37L8v9R/v6G6FYcut+/rz4jP/bL+JogoxPflD5C8EPPVNDWH+L408vvECMgoJSNc78Mu/w//gORQ6fMqsyrkYOTNTUCE1yHCRiNPwZhhcC/Y2+XAMa1CmFgn+tg/Y8ZHi2G2Pbr/3TuIPnJeYLk9IF2X59o9/UOcV8hFny9Q9zXBzr++oYcofCsDP0wtWJEm+92X1LLB2k9Ks5LUIHyBiHF7mvwCYLRp/ENhFDk139L/te7qLe8//WOoOEDpzROGjGqamLwNvp5DkD69MqB2A864DRQS5w50CQvhAD7Cv2vsvgGMW6MSXUN4xhxQ4jFkAP6u2wYt8+jsF9//dW2quBL+gBVHHmQQzWFC97NQT59gr55cegH9ZcUOEGGfPjt9w/I/0L+u1134aOOHQT4Z1agheuDqiCwy5oELoMJgymGEHLPym+/PyMMxaSQzWAOQy8Ej82wSq/A/Rbugzj/hJEUYgMYZhjiZKQtiNRIWL8hkoe82/tktBHLgwzSkwtymAqQOj2UakF33iOZZjVSwVKsvP4VaSpw1/qrXd5pDSSw3a36V0TmdpA5shj+N5p5XwQ3Z2kIw/9eDI/voZDyQ4Usvol4Q5SxLpHcKq08KK2nDs965AUyxrftULiFpKD9ko40CcZQ3ZvkER64CEbGeab005hzyPIJRAS3+qb7vsYa+e1457nyS1o9G8Aqx1Q4kBCgUr8J3ZEW/vEsqSrImti9xw+Ud0nPLLjPrNxr8EHWyJOtkTtdf4J8jdwJG3kwNqI9hokvDTZDCeT/26gxGjhfrTRhNT8KPCIoR818BG4chcYAP6YnyPgIrJ5Hk3yfAr5hyDco/ZLGIayCsv/HY+U93M81D3hqShgdba7d5UPTYOBGufdSHEurLMcitr6k3zD7FUbhDlAwG7BvYV2P5fRN4Xj1m6UBbM7x83f+vqeudEfHYbkheWPHsBQ8AFzbcq73iMF2esYc1iUYI9wGIYzej14hUDpMP5SPQCNC2CAQ1++hUzLoJuwkr8yS78vDe8LKzG0caC2cNcEbcoYdMVZFBdsQjjbjGhiFD3dRSAJgjKGJ7xGuAit/GDOOp08DrWcufoz/89L3Cr5bMhoPZVquVcNItiOsuqB75PXdymemoKnJWCL3TX9M9tNT5Edq+ceX9G7hO5LDVo5HVv4hNAhsoeRRbiMSVRBNEvAsH1gHdwJ+e3Dog6Tfbfn8Xybyj39vaL+z4umPefuMBHWdV5+n0weTfSOyN4gDU1ghYQ6qJ6l9evbVp39ppk+PPvyD8EesPiN/z8A/iHjW9WcEfZu9zcZLW6h8LNznC8aD+7QwPxHj1S+pBr4nGqrPoG0jlMY9ZNF3Xvm2BJKLXwJ/XPzgmWqkpxYy4h1YYSq+pO/F8GwUiNupP5Jilf3QwHeChal9ZO4d/+GltIa63XEw88F4bIlH8yvw8jlt4vj1JbUS8O8dV0aYhxUL4zGec2DvwFGnDsH9k9W44RiU8f0fT2Tq/Y0Vj+2VjZQ5Yvo7iN4dcEto3diPfjgi+ysCjfbr4O5TO/bkOBfY0Meqgizrjk7UfT5a/TjOjKPV+9z1Xy24tzXEIzf7PHb3KzLOyK/I+7j7inw7gNxPdWkDT2A/j6P26DNcCn+8r30/cNrg5Zc/MeM5ef+1EU/Ieb07Z9kjRY0u/olPUFoJigZyojva893B73qzh7Lf73bWj7Pjby/fUOWZpeecCJfD9v1Ujaw4hbUMFcLPj6qD1/7vJsinEAiFcHiBUiybcgHOuhhrAQqjXdJxCI9FCc/GLNcm6JmF4TRpoQ5lYzRNuSxLUaTNzlx2hgNmRkB5jwL+OvJ/OBoGZh6UiGKOi1MYSRIsSmMW61oEbVnujGHoGe25kC2+b71CJH16+/BuDOX7MHuv1ofTv73YFAFXikQlzR8vbsrqFrTc1gJ7UlLAJD1qj5+KU4LS+01TL0XXWy8Sv6m2ssLFnh9Voabw+rKK1KttoUE2n2rrSX+kRU/luUlILjtstj9ZqpTKyTEeyLifMCQW+OHcnG64fs3DWcSwXAoN10rfROgurHHJN6qsM4hic7qcjWVzyPsTUXreFFV2m3iWxH4QGDrf+XjM4WKtra4pF6u9tt6X+R6frK0r7kQKqFDNKjLNOeT45VR2ExKYDTNAdLHFg3ZO+RbwV8zeDRXmpDZDTQTMueHkMF0JErsGErNB9TMXJ3rBDpkTymf1jAWlGcQScKj87BG80WyLkotPhsQedoZz2CokzZmNuymLzSXYd2c91rmtemTIy26nHYLKKOTguDu0PqbVqrZImgtlnnty75+bpb2iovZoaaRnGueLwt40a4OnhzrTpzpligvrsIKIJE/MJDvJO2bbW/mQnTnqfGjM/oYt/d7U6xRYtlRFTslbNTr0so+dO6nO5lxTaVOli2U22ooTexOf1wGDn+gzzVnHNQoF6t6mWHKM4cSHhCsGs6APU8lOiF3AL8PjmSsvyiJDA/qUnY/5zjG2y2JWN1MLV6hbvG9Fu7fVhS5d2vAYHoaYmJvY0K1RajqYluq6884wlguOudQNOU17rs3OzsLa2V27Ox85et01A62s9aHZntGgD/WzfTMPqY5dnFNh9JW39Ra0kcdme75wxo4XtXyVqzJOZhuX9CJDNPAlFLlP0kTY8qDpuh1xckpPY6hSjo6YMIhsA7Cs0BP9gqnxVbjtOGzDbAm8ZffHIdvXybqnuG6gFt0Ww1fbRqWqHLvkzTZC1XrD8AKzvEyW2kTQtJIWh+AQTX22co75hGl2BNe26hAbpZH07r5HFbeeSJOTbWJLHhybLL/qbRPp5YGUQvYiK6GP8iuZN+Nl21vCbr4WLPZaxxq2UNgZkx/UfUeifKZGVd/eAkff68m21ISdI2SEPF8BfrPJBkUqhcr27RkncCuK2Rvy8rQQzHN3ifQE8ELrhMoF39QyXzJoFKeGeBNBf+zFLDWlTmCEcilKDdCyixfap4QTq5WVssZOwLDtcnUrjCOxcrrq0tep0U8n08zg2BtRzbBbGZkFCgymiDtQbiWN8/3awa8OfgwzYhClNLhtN3NjVUX+4nCqb3tZZN3l4TKRa2JvNgEn9VFbkJIJKKnrDe5kaVQ8NfotdVO665y8lZhgwX7X41xou1SMUbPqPDK58ItJUVnukc0vkmDpq3ypMVZZn7blZU3hm8DbJNgp0jXs6ABLOROFKTJXYZMtd/vJJDc5e9gYeuU0XCtM2QKP3KWk7adybYR9pB0kvjeIgLlIUs6vj3aZ7Cd6Rw7rULjdtnP0wi27uihsy5V1Fbp5kLYEV2ziY47L6umkzc8WNyPPwdCdMfmi4Q1QGZza92nJdLFWoCZLpElmrW5ee6ErqrxSc0MR60QPrTgE0/kAqBCLKO1oNbHDXkVfjQEHpt5kI8/BhAGi1fmkiqoHP+FKWznwNkl3hUxtRJe9Fvy1rdJrtxLYFcXlQbAghzLD2bnWOWlWpLc2q+Zx6pBtKvKzG7RpnWii7l7ikh2i3ayanZy9R/RrYU5wQRLpA6nMcs4AwSXiWnfRcPvl2pLQY2bauuolZFlPhIuyOi3kVSzgq1DWV0sIrVJkqnK1XbTU3gx44XyRin1YauniBETRZBrpsLcqClQz7pbvwa0HyfnSe4OyZnfUBvIGOfHSEmPUzW3RYYXjejvvcDhdcntQKrxnJWy5g1qD9dRgmJWzFbe3myqa9joMoEDbE0VsMhFM9pTdrlx/nrKSGC7bk4LvthuMXPPz0F+qqETtySaVy/OmWkq3ZVQ0s1QaUpXgrD7XTqCZh9RcX9pJpKETJaIJZzctnEvRlkXoYFmgzLrFRdIY/GgNczCHtbCQTZWcpzeJ3KW5hh48g1/venqQTyJT8qp4qKJmyfvVnObUizakS4c7pPFSZnTJ2OorhS205Xk2MOb2mqvc1AK1fLUO4na5R2t7Gi4Oe4ZcNlarD7lyABPa3Hc7Uq2CuK26TkpTb90PGBrGyo6RqwtsK9ZdNXRrHxqLblFUmFD6IchuvjrrmB1deah7KslgbTjkpTnZze3QbTsn5nQh6Ejbc1BxcxLQvVQLwgStwInQYp/AKn5zVVBxLx2ojTwrXWHm210aF6h+1Em6dWYymYa5h8ULS5FP2UK52o5UzANGHDpR1fqw2OooAfxoLXaHYMb5a+KkW+uhOl/zgDk6piBtJFWzSZcBOBj6eGftw41eSSuj25zNySqy6QrTt1KsDZa+cGYLwGAgCcLVagoRyO6yw5Jimdt5gGhxTALLyieWdHKEVVSgqobJHmvy3HzGJbeLPQz4FhaoqQGZrOl9xqqUHM+lk7WBs8KcI51CEeOdAG7r5Cj4035Yq9balVczX0KFrWCKcyvgwzl1Oyy0XhCirpB2Vpue6qkl5JLMcICyp267t+yIvZ3taNG2+i5p5wlxU2eb0XCZSuow3MRBnjHszvTWGMsYDJWnxdwIaJ/lrfSGa3Pn3OJ5oSjoELnmpEH1NBlWSrfDzEabyTWFqRiW75fNZjVfLkF9xRhp0wphPj9v2IEMaWPT6NeKZ4Vr5ZrBTTrxxWaLYiBFRV/O96JXVOJydnY3engJ+MojlFDVk6CeXRrV2fQasQfXmEuu12SVdERxDM9lcJitj4t5fd3u+3y1oFdwvD9tw6107g0F6E1FAsn2w5UpH9B+XRJ9MNk4ZC4dZjp14JpMP5q5hpU1UyW8RF2EgMvCdibrFTWgIkGpza1YWVm8zW5d3DhMpmUFbZb2WjYbY25NemvpZ9JpNVtR+zUVSqgHYiZ35P5qNnDsiMItFuaGzKGno8tvnOK4EcGwLo/rjNvnUe9Q8sydBrtF3NLMWp9z1JRlFgZ+OsK5iOSca5QEtJtAHrP8ljpoba/HWsYVtnBNfSNTIBCt7fLCRee9bh+N6cohfMbo0XniEc1OFJNAVTLXCJg1VfJYvzxFOa7v46DjDZ4KTyeHcYX2cqOc61n0D8VyhYeFPaBtXx1xc6eVfrZe5bx0WncQ+eZ4N4QX1UkuRQ4mLQF5zo6a08YAYn4mO4unD4sjkLwl4DCBsk3JmBJ8U4ZS4XvkrMy58xxtwsNqXcpKQ6iHTJgH6pb0rx29x/kNV/CSH136glhbGbtMT02kCWs0abtmWlRqJLCLY2aboRGuZo544YQglKYnty5neqtOsCnRRgKhOTp7M0GpXq/hfJb3g6MM+5Ov7nstkvN0Q6t72oUJZU1o6e5YFC1aC0HjwINCo61nvo4fCjjEh94JTiGKftqJbbkuK3S1JxfXIcH4JbfCZgFNbkKnzAWi5svJAqP1JvKuQT9pZgY24Q9Hfb1kp35xHcz8dp742lDq4EAr3QrMIsWXlvoMjnZkkJupl2FzGQKut5e0U6tjuKOY1rQDi220dfsWdUzat6OMQ8VbZQp7wLF7nxWPtt662nyjJGhSYpzgbcFQkx3axwB357iXs2jLLBdaw1YF8Az3xClMzeNOww45HrGu7U/VSdjgZapR3FBHU+MkW35BXLbAYleWY/mk6wKjwhNuprY7dWFxZzojQ64rb0GOudM+zEqpCQsykQMfn9OsGnSQJ1J2o7Bm2M+nDIRo5qCAcABrXacIphTw6mQ1IhwOTyDYOazQTHEgi5500JkjuzczddoMVUkryb488gzBb52+PRmpG/keHw3B1MNwYyrwi1w+d3N4sMAnm3RGA0C5xCqtUR+zBfe28TB1pWMxt1D9iDG2e56ShC3tVxxK4+264wdVDTQcay56tncdpVgIHRlO/KUgxuuaM7f8ddddxEXXbF15W+MbisA20Wlp9gocYnZuy9WLE99EEwOl+0jkZAigl9VhHS+ZrVMtcVdWepY+8RRdtjHG3IB/mzBhsXC6spo2Algx9BbOW1umBnJ0WPFSJjNedtm5FxzDfV/OVhWWQso+1pOlP9vVBSqq2K2alWzlkV3XBvH+ArAFDYtmLbBgl7OOEuLp5ebJmrLoadtgg3BbzAc7jNSBsQ2cSQajWJGA3ks3m52TUd6QnkbhPeWZ62I+3+HnMmeWssdlzZIQ9u7gayqRgja9ahUj8D06NSLNF+h1yjM3jd2olBSLMPOw/zaxT0lr3658uL3q3PkZDyuGWjjw5H2dyBXjLjo3Ww7HWWwvNpP1NQ20bmB1bQZ2YqYHFE/szxWDVhOtuc6SXb6PMG4rL6ndkutaJjkr0dF0zd3StaYJukAZkByX0XQqR+G6cIyUZdRGmwwEHW/lbolXtNbhp2pQ+JU12PEcozsd49abtaDT9lFWPJZhsRY/t/ZFpUvD4LflCWJhQtBXvNUXQRQMaMRqOEG4h7TG51q6vdzSabwxlZwoV9g004f9Gbf3brlT/CvFNxTaW2SJWQmMt9/xqVn5QbGDYhe3xQ0IYI/O22PCRgVsJoCthf3qFE3EXeMQ6ipciQGxw9dy0RQX+sjasxTDKFFlNN671NYEX6aYd6HpVTKUuwaOjHhJpd4pCxxves2vFyz2YJeAvcfRC5q4YTfKWtAw44GX9cA/RHqVuqgxSxZNbNuMOJ0oBl9tJrel266oSVx2zn5hd3CkEGYEl6C2g8bX6aRvXSrDrmc5KCgSoyXuFk6XKWEl/nlxuO4KagLbXG1P2qC1YQqwnqbpdr3FtNXkphAQhBh2ZrEmh4bbwST3gss3ODHfBdNDm3LKlgmGeghmEimj3hlb5y56A2iyxVDcEN3KYU/Rlj9Hkz4dAMgEN+UJZzMh8tCCGEFOSH9hEvMyoE7ro7m73LT4GM+nenKq1UjG6/iaiTiEQCsXq3jnBBab07GodalgDIYRTbBWmbDX9kAMCpG3Bj5c2FJc56Bp2WszyDiwT6szTq/0FOf3C8arNqEysw7rM64aS6NtJXTP9OgppXGBpBNFrhckwddrlT+fq9uGF/fu0oXnOdoLzNWUWs+psN/elB2Jtc6SLnFBbYciSkhMNc6Ey98IHk5yDX+Vs/l8/s+X15fx/vHzLvDfe6w73nL7f3bn73GT7ttTofsdWGC5n++6Pv9Nu355fSmdEFr1uM9ZxY3/vCH4L3c5P/1bjxRGEf3jmen4GKurv907ry1//O2flzB1m6ou+69VFjf3m62vL3ZTjb+HUI2/quLAny9395J8vIX8eFT4/Y5lnX3NrTGcYTo+lgFuaNXg+dF/3vV9fXF7mKXQqb7iFPkVlPno5vPpBPQOe5u9oS+//2/QtZ3USyUAAA== -->
