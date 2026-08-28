---
name: "rar-cowork-cookbook-report-inspect-manufactured-goods"
description: "Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_inspect_manufactured_goods", "rar_sha256": "0a1e285f6a92d6e810810de9b36e0d055f2e2ad5d602e449c4a08be06cb17c3f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_inspect_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `report_inspect_manufactured_goods_agent.py` and in the RCI capsule.

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

Inspect manufactured goods Summary Report — Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-inspect-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_inspect_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 0a1e285f6a92d6e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_inspect_manufactured_goods_agent.py` first:

```bash
python3 report_inspect_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_inspect_manufactured_goods_agent.py   # or on stdin
python3 report_inspect_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect manufactured goods Summary Report — Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-inspect-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_inspect_manufactured_goods',
    "version": '2.0.1',
    "display_name": 'Inspect manufactured goods Summary Report',
    "description": 'Builds a structured summary report of inspect manufactured goods activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-inspect-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-inspect-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '466ad6fb0378e92f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/inspect-manufactured-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-inspect-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportInspectManufacturedGoods(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportInspectManufacturedGoods'
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
    print(ReportInspectManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716e7OaWJf3V2HO/JH0mByQm5CnumoQREEuAoJipyvhskGUm1wE7Le/+7tRc5Ke6Z7n6aqpMedEkbXXff3W2pvz24vXNseievn0YgEvR5ZemiZHUCFeHiJ80RXVGb4VZx/+IkGRN1Xit01R1S8fXkJQB1VSNkmRw+XzNknDGvGQuqnaoGkrECJ1m2VeNSAVKIuqQYoISfK6BEGDZF7eRt6TLC6KcWXQJNekGZAuaY5IUzReWn9AmgrkIXwf9fEr4J3DosvrVyge9F5WpqB++fTLrx9eEvj55dNvL0Hq1fCrF/MuUnqIU3+QthyFweWpl8eQrhyg+Tm8LkEVFVUGvwpBhDyv3tcgjT4g//Ef586r4vqnT59z5Pn6/DL+M9scaY4AquvVDTQl8ErPT1JoxivCpZ031NB4KDd/eibJ49fHyu+cihL5ebz3/iHkNQbN+88vBVTBG337+eUnpKigvKodP7+OXMr3P72mRQeq9z9951O3/mn0LWQGtX798rx+soWE30mT6C71Z8j1EUUffH75wbjx9dB7tBOufHk9FUn+/sG4rIoryL08AO9/+iu2wREE5zSpm3+J7y8PxkfghdCmp+I/fbg7+Vdk8jTojedfiy1hWP+OJZD8m7gPyNNRf8X77v//wjpNclC/efxP2f3ZgsnPyC9/adv/tOADEn1+EUCaXGF2+Cn4hPz2xdos+F/ehd+/fPfr75D1P2VjFW0V3Dl8geWYRKBuvnz55V19//rdr7+8a0uYa8DLvrRV+mc8/8yvdzl/8OCT6v0f10L5dn7OYTEjb5mO/FaU/1b9/oo4XpqE37+vPyE/1sv4miCjEd+EPlzwQ83UUNcf/PjTy+8QIfIHMo23YZX/+78jahJURV1EDWIFRdsgMMBNkoFR+e0xqRH4M9Z2BaBf6wQ69kkH83+M8KgxhLSv/xnccfJj8MRJ9AF3X55Y9+VHrPtyx7qvr8gWMi6qJE5yL0VMbrP5nHsxyJtRaFmBGlRXCCf+0ICPEIg+jh8geCJf/ynvL3c2r+Xw9Y6ZyQOfTF4asaluU/A62rc7gvxpTQBhH/QgaKGEtAigOlECYfUDtLsu0ivEttEX9TlJUyRMKii1gJA+8ob++jQy+/r1q+/Vx8/5A0wJ5NEXahQSvKmDfPwI7YrSJD42n3MQHAvk3W+/v0P+H/I/rbozH2VsIKw/owE1lC1dQ2B1tRkkq8eu0kDouEfjt9+f3oVsctjIYOySKAGPxTA7zyD85mprxX3EKRrxAXQxdG82uhYiNJI0r4gUIW/6PhvYiOHHom6QEJSwK4E8GCBXD5rz5sm8aJAapmAdDR+QtgZ3qV/9yrurmMEy95qviMpvYMcoUvjfqOadCC4u8gS6/y0RHt9DJtW7Gpl/Y/GKaGM+IqVXeeWx8p4yxiQY4wI7xbflkLmH5KD7nI/NEYyuuhfHwz2QCHomeIb04xhz2OBhv4bt9pvsO4039rXtvb9Vn/P6mfheNYYigI0ACo3bJBzbwT+eKVUfizYN7/6Dmo6cnlEIn1G556D017OA9RwcHl0c+dzi2JRE/m9HjFFFbrk0F0tuuxCQhbY13YfrxjlodPFjdBr5wfx5lMn3/v8NPb6B6Oc8TWAeVMM/HpR3hz9pfrDH5Mw7fxht6LqR7z0Zx+SqqjGNvc/5N7SGKiN3aILxgJULM3tMqG8Cx7vfND3C8hyvv3fue/CqcDQaJhxStn4KkyECIPS94Ay1qsaCejoeZiYYXdsdk+D4B6sQyB16H/JHoBIJLBHou7vrtAKaCWspqorsO3kyzkNQi7ANoLZw0ASvyA7WxJgXNSxEONSMNNAL7+6skAxAH0MV3zxcH73yocw4mz4V9J6x+NH/z1vfc/iuyag85OmFXgM92Y2gGoL+Edc3LZ+RgqpmY9XdF/0x2E9LkR+byj8+53cN33AcFnM69uMfXIPAIsrqe6qNWFRDPMnAM31gHtxb7+ujez7a85sun/7bOP7+703s935o/zFun5Bj05T1JxR99LBvLewVIgFsY0FSgvrZzj4+6+rjj3X18V5Xf2D88NMn5O8p9wcWz5z+hExfsVdsvKUkARiT9vmCvuA/zt2P5Hj3c26C70GG4osMwtzo+wH2z7eu8o0Etpa4AvFI/Ogy9dicOtgP77AKw/A5f0uEZ5FA1M7jsSXWxQ/Fe2+vMKyPqL2hP7yVN1B2OI5jMRi3Kumofg1ePuVtmn54yb0M/CtblBHiYa5Cb4w7G1g1cLxpEnC/8towGV0yfv7jRky/f/DSsbCKsV2OeP6GoXf1wwrqNlZinIyo/gGBKscQEUeLurEax5nAhxbWEF5BOJrQDOWo82MLM45Tb7PWf9fgXtAQicLi01jXH5BxLv6AvI24H5Bvm477Pi5v4a7rl3G8Hm2GpPDtjfZtn+mDl1//RI3ntP3XSjzB5gHvnj+2p9HEP7EJcqvApYX9MBz1+W7gd7nFQ9jvdz2bx37xt5dvePKM0nM2hOSwcD/WY0dEYSZDgfD6kXPw3t+fGp8MIADCoQVywLwpwBkqoj0WD2nATDH4EwLWJ2iAhRhFRTjAvZAKaQwHJMkGpIcxPsDowJ/OAiKC/B6p+2Xs+8moFMAiQLBTPAgJGqcokp3OcI8NPXLmeSHGMDNsFoWwR3xfeob4+bT0YdnoxrcB9p6pD4N/e/FpElKuyFriHi8eZR0PJRRfOyqTPTaZu+jEIJzSzq6HYQOcwWbCaVCmJVbQYYvNVlOfM3g7K9auNLe0mj7hEb1YEfymTtm248qkXIfskqJVBicb2+YSZj+ZbA6+LS5swSGdKjVL2fGGix4M1e5SqdWik/NNchXpphRxRZ3a3o5MowilxM2anZ6Oi3K/3FeqloleeNiohH6cUUDeouXawZu+8tr0sujSgAjO60u7FhQ2PbvZwYmkQWWBmHRAIKngesOoaFUxLGpfgmueztgcq4mEdqzF1Lx4klVf6F1frrHWXya7rMjtNF9nwaxcbiknE4c9Ju7lqSXs1a5mc/QiBxReHc5Vri6j1WHoAX2WD+KlrXbKcJG0o1fteY6z6ZRiSscWw2ANWmxtmy12buvqPMxWLsyIhE53rJJjMOucIE6c7XznZf1y3s9isCWU0KoyK7NvmUPxMnaScJ0X16Z1YFeXEpvsd8Awzt3kYigez1VXoWoLQSbgfFBNE6nd7qrbzgrEDd3Ll2ZLK6nt1PukpXf1cY0pMu5eNDbA5kwQ1Qnf29W80bJYoylvYOXCBUx2GXYCWtVEObGVeagovHbpeNroj2qpOyvxJlDnXeZXXbSb4LxHCwlf+MS2SXH/FEdH053x2IHYdqDOnME4hTkBLCoP9OtydZGtsLXJKpfDvXDpNb52itiZaDNHE3dd1gs5ilvFsLDAUiDK5KbbKkpmQjDYCmPKvicmGzny8rPSNnmzc2pAGup1Qs28TN6JB4e2/FMQFAo249ptPb2cViej3MunHLNO58Xy5Meepks6HVS4LLdr4hJ6zkKXCelEaytmt1E36+n2uBcPaLzSqUHNcwadHAchvunTwMJxLWkOnq9Qu/q26y7OLqVsX5uqVusc3cYTZH5/lXprN0RFevQXVbaabVuByQwl2/W2xM0Pt4Ky6uDoE2XeBanoWtVRFU0bF6rtQgHcYtA53JrLWduri6uoEtysWMiiknZJ7fFSsmaaodcvagCUYpCYfXCxO/16s3TctwF/IKUuB5ZSAUuL/W7gjri8XGwkN93gODiwF6d1uvxmkNFJ8RpOt7UluUUjdEnYgbJaAgLFhzX0Kiofg80lGcThSvoZzViH69q9CS66CER3Fq+nNx5wZb9j6eOJ3R9sB8V3nL5Rm/TsGBlvHZcnwpxPPGw4befVJmGMyBaHpvDDEFysGzVjdGeJrxa0YCR5ppA9xMsF7U0vIsHuLJIfykaXTxKm7UN3AfW1KqLZe+sSFGRR6lpGhE6wtgaet/m8AJF9NjWKksupHs3TpTspV2RzwZZ1FPepVJwxJuHoM1hsUmUOo+L5B9Cf+X6jH3bGcrFy+UqRziFhHU4RlRynSwk35yDOTbsNAVUMSRJyAywF0FviQVcn8XXBgFU3b5R2Q+2mbVUwuJtTaHGbN5c1uVy2qO5t9ZN4O9CHJpiWZKzHuEPYOB/2wMdj2CRErMIrYoaW82Ez3V/hnmcpSDN7tub3bdhgtNDm16XleoAm8MkgznPS6Qei4g+Cb9oGGTPubOpvC4XUhbN5mzF7XDK2+tY+mAxROTh7Ks+ipgKP32xl8Qo1IAqOmReLjZvJe0uWUW6aeXRNJQd9v12R4BwsLFU7rwr8ogRiVm7U4wVwgm8liUyqJ6dIh3zfLz1m6u5XczvpeY1Mhn4H3X3a8C2j6SzlG4uYdWmG4rQgITWfPKhtRU7T9pCpNI2eKmcAuc9QmyXb98ssDFEitCzbTX2sPzqn2mLPhrPaV8FNYtEg5ruWpE7NZDmHgHaTMfbMZsYEoNvDfkYZEYExArmwxLPdYFdlnZGlwLXxQp9KnkHVe2NFidI6zwOK2OnBvIH9smhto/QNqY0dd8sYni3yetUm61y+mJQ5HWRWU7HK3keLcE6Y+qkKDli8qVZLZ0lJsisakWMdbHdzwRiyvhyvM7nAqUGOmWh9cJfdXlqdJsZpquFrxjGxo8WRnum7gRw3Fkm5N9giFkRkpwdl1RYly4kxx591Kl/v9RotHSUSxDk5XIblXrgtF+buwOCa7jv6HggF1ig4vToXqBwW+/mCtVaCusvJpBQnJ6qeVPWJcTlpu7+wA8vkbleURs8o6zBSen6x8Gpwqw79fhscJ73eAe1ScY0Ytnu2sawDhwcLpTfSZn9ylEXmReUML9NpZ+gmybtlVWne1QSFtBA5d75dTNGcWWlaIS8rm9fM4maIG8OiPJTfJlI0X6o23Me0tCWH8xXMpWJj2XoMnM0avWznde9fTupOHvJYnhVrwQwLO2P25SVoSkHa7jpDXomajHszzyxzKz0ssJ1vFbUdh2Rws9nWNHKG8M69QDZyulaG5nqIL9fQxaZBV3FRS7R54SRBFAiGK/Ay0e1i3+gUabZfbArR2fAUui0ymNIwOapKNavjEm8x/jJRJQGC8NU0K+48I09afM4U4wD3n51p7yTNW90S5zZZxNPN+iRW6kYjNuUKw2XPOJD6hvBWu9scbbLMMDs12sztec0JKc7Sw3Sm0AviQleKerGwXCAI4jTRicJv8rmaGdGRJ0oa01YWz7t022xAhUHFpmlOUbDPTOlVpe7PA7M9+W54AZS4O7YLaxPvMgafdjzfzYOLISZXdHIAuJWnB59DzeXBUhY6m3SRPPFBLrNbXljbYrCru8HR+iE1s6AnwcQmzylV+ZFayvlQQ4SclbJdlvL22LbAOpPtmnY03qbkLilwUeoBz6UXEQulqalZMnUrG1oztH5h3sybSg63Pr14Qz7xDLKUQgxezFtSNuy9tJA5o81OEnmYylwRYJgN56vbejVjelO9GMkl3xRUhlnZJonYS8MYuMAPkx210nAn7unUXTBHk70al4mz8dY793A9CDxjB2ZYl+vM4QhHZjaHNovphPXOusUvsi5qr0vvKNVLbk2i3iKLzWbOTjoSP9z0c9s73HCYGSygfGGhDJ62WZOl3pnFunQxSLwvGk2dSX52OqUoWF1wm+3mRZ7zfUFKjKnpmqeC+bI5xfnO9s14zW6zzGIznldb7UxeCzlGZdgaZNGg9Li31xHB8QS2jUUtKw6T06nPL5KysnfzfmstpGkvtL4uaCrqVcaFUdNbeNPs9YrZHhK681aUpUdnLUdPcXPScZwX0Qk3K8mTXyi7aO0Zaax5iVSshmGnNP5MsrOFXe9rQm60YFHSHeedNHK9CZiL4Hhl0APPPer1xNOueM4X/cZY0EtcSsljs5rjxlFyk810xWIYRAt8ipLFaSGBaMrGM6AIxxKfr0v+Fu18g9W3Z/Xs3tYUXiirhgPVdnpRyQWhr7PKPOsrivPKS3NRTBN1xQMGy+VCdeszZce2c8KE7WBTTZptOLGkWmm2Nfeo1OrWJd8Ohn51Z1G9azXzxN0YDdPqBJwzz1qvNvJeWuK7aMkKJ6qYzSnUlHbSNlhV4mYVbFWcqIXTdCpJ/knYXs5c61UnH+15MThVt6tNW3ZfkpqmGoUjF5eEnGs00LY7PmXEwpn5VeSvzaAnzFWr7LyQDI3rnlmuwmOxmfFN1cCNTOWXRw+zI7+bTauiJZtpvcdJxUKDtplcFNCp7CHqST6LF2l7YbVrT+cAk3YHNwyX5qy+kWLCecC+6tUhZva+i0c5EddZJm1KerBPbnytJyuzqG/BsJhVw2YtbDq094cTZggTvgditL801E7aGGVTbHoQAlpkT5g1Q+EM6PSLw/52mM4v8Wwy04eq0QbNc6Occ/3Jbn5iZk0gkMFcUWb0wKBkF9WyNZGFKNlEZBJtG3dVdsYaEJlm1ua0Licu6TmeTSzoRJWDhoNeW1xb3lKiNppHku6U07XOOrf1ld/mccOp143qYxycU0qlsEw36Ce+yuha75VtOKF221XvuHO/K1C9jVlCWt9kV6N0MTKuazUobmpJnUMp2+dYw6ylHe154g1zc5acUkI1A+w2CntymvSnbUkAKRApfDq1i71ABAf8rO4OlnvAjyg7zSN/ws+H835rhWyg6cRBZVe0p4VDozCtd93PJnUQSZSbElEHOkEyzMiP6X1kuiELQzJbbTmjwacz3x2GRN111Q3O/VNmpWBT/DTJM40n14wBAjJqfRxEXZvjvJ9wCtOvJ8AUN33iJ66JKQF53tby6rIRMVOdo0GNzg5ll8zjWz/sygmbBHa70OCg1QuUPYTSvAsHdeWahgvL1pvrURjT6hkVZtJyIk9I+sZT/cxqCmZS+oU1F6YzKaIxbwNHEJVkc8bY1QymTsw2xrJN6Z5wnt+sDTFI2eHgEpp2xGPGmVYT314QPe3oO3XDJPqZLq8gIG4Kic42p9Y430TfrOp8dbBu6kQtG621FfcqE35xtjFz3zSqNOtumU4vaVzw5Sr0afIQQgSWAkJwsn5eqKqrA8a/6KggXGz2Sm47GvcHlGpbzgJtvwW1RnkKqAtNk9m6pQWLwIfyulV0SmxaXKo1g+rXEgmOyZoV/G47PRLx3AgX7pXVM2fW+ouEE9Y9GucF2QpOfTqSgGMTqM0ljTAlmRu+jwoKkOaFP6VaVxdmw82PjurEO4TT/axm2jVFYcOUZsxlaxDejj3tNrRkL6/MKW5ppVHIqltODk6yp1Wl4Uk/UvbmYkJZYYUD1ECj7Hyc1dfZPJudmsgQ596ac8iuTDiXKQ9ec93F6/00cpfT3SyBnV7bs1unVog0OgmYYBhbrrLseYCieZJL67Vj0NZtH/mhaM7yKaE0cZrzPKHTDq3q9Vw8DikGMH1l5PGEQ3GmMA6D700UdWXMmsExt37fDHi49f2rb4UQ5E8ZnoHCSt29gYq8uLkGnC4c0VYMo91xE8k4wwQc1wSSIYced1XRGpcu+RAT5/4CcjOrsG5gFHogDkesos3ZLriC+nbjAuCbDtVWfUd04YQ5cdZsOx/25KyjtElzOmOETRLujqIDWJKbc7gjbXlOTDuFJxWjDHC33jXrCE793mki7/XQP9Azy2BvbWvHgSRo1DKhaxPYS/i+tsS4xFG7E1nMErGztee8CNsfSWG616WwPzNos6lZBqqoo7GGo/Mjc7RijuN+/vnlw8t4Yvw89/3XH+GOx2z/a6d9j4O5b89/7ieuwAs/3WV9+hs6/frhpQoSqNHjTLNO2/h5APhfTjQ//tMHB+Py4fFcdHxQ1TffTsgbLx7/ruclycO2bqrhS12k7f1Q9cOL39bj3xjU45+hBPD95W5WVo5HxQ+Jz2PkL03x5Xn6+zI+/h8fvYAw8Zpvl/HzfPfDSzjA2CRB/YWgqS+gKkcjn08hoG34K/Y6ffn9/wNOXebZLCUAAA== -->
