---
name: "rar-cowork-cookbook-workforce-headcount-report"
description: "Builds a headcount report by department, location, and worker type for the current period."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/workforce_headcount_report", "rar_sha256": "6bbec9cfc5c3d27f5aceecb3d0519217f4ac491024db1147940da486949d8c0d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/workforce_headcount_report`. The original RAPP
agent is preserved byte-for-byte in `workforce_headcount_report_agent.py` and in the RCI capsule.

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

Workforce Headcount Report — Builds a headcount report by department, location, and worker type for the current period.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/workforce-headcount-report
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workforce_headcount_report_agent.py` and embedded as the fenced Python below (sha256 6bbec9cfc5c3d27f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workforce_headcount_report_agent.py` first:

```bash
python3 workforce_headcount_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 workforce_headcount_report_agent.py   # or on stdin
python3 workforce_headcount_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Workforce Headcount Report — Builds a headcount report by department, location, and worker type for the current period.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/workforce-headcount-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/workforce_headcount_report',
    "version": '2.0.0',
    "display_name": 'Workforce Headcount Report',
    "description": 'Builds a headcount report by department, location, and worker type for the current period.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'workforce-headcount-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/workforce-headcount-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '208d7a75d7b4f12b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/workforce-headcount-report', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'verified'},
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


class WorkforceHeadcountReport(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkforceHeadcountReport'
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
    print(WorkforceHeadcountReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6eZObWJbvV+Hl/GFXy042sbmjI0ZCQohVQiAhlStc7PsOQlBT3/1dJGXaNVPVrzvijbwkiHPPfn7n3Ev+9mJ1bVjUL19eDp6VQxsrTaPQqyErdyG26Is6AT+KxAb/IKfI2zqyu7aom5dPL67XOHVUtlGRg+XLLkrdBrKg0LNcp+jyFqq9sqhbyB4g1yutus28vP0EpYVjTWs+3WVMEoC4dig9yC/ARehBTlfXgBQqvToq3FcgyrtZWZl6zcuXn3/59BKB65cvv704qdWAr15OgAdY63j8m2jtLhksTK08ABTlAIzMwT1gCSgz8JXr+dDz7mPjpf4n6G9/S3qrDpqfvnzNoefn68v0R+vyu2JtYTWt50KOVVp2lEbt8Aot0t4aGmBr29X5ZH8DfJQHr4+V3zkVJfSP6dnHh5DXwGs/fn0pgAp3b3x9+QkC5n99qbvp+nXiUn786TUteq/++NN3Pk1nx57TTsyA1q/fnvdPtoDwO2nk36X+A3B9xMr2vr78YNz0eeg92QlWvrzGRZR/fDAu6+Lq5VbueB9/+iu2Tug5SRo17b/E9+cH4ylBgE1PxX/6dHfyL9DsadA7z78WW4Kw/juWAPI3cZ+gp6P+ivfd//+NdRrlXvPu8T9l92cLZv+Afv5L2/7Zgk+Q//Vl5aXRFWSHnXpfoN++HXZr9ucP7vcvP/zyO2D9/2RzKDpQGROHb5mVR77XtN++/fyhuX/94ZefP3QlyDXPyr51dfpnPP/Mr3c5f/Dgk+rjH9cC+Uae5EWfQ++ZDv1WlP+n/v0VOlpp5H7/vvkC/Vgv02cGTUa8CX244IeaaYCuP/jxp5ffATbkwJrOuT8GVf4f/wHJkVMXTeG30AFgA0AlgA9R5k3K62HUQODvVNu1B/zaRMCxTzqQ/1OEJ40LH/r1P507Gn52nmgI92+o8+0d8b49EO/XV0gHHIs6CqLcSiFtsdt9za1gwjQgray9xquvAEfsofU+Ax6fpwsoyqFf/5rpt/v613L49Y6b0QORNHY7oVHTpd7rZNEp9PKn/g6Ac+/mOR1gPWFuCvkRgNBPwNKmSK8AzSbrmyRKU8iNamBqUQ933sBDXyZmv/76q2014df8AZ849MD7BgYE7+pAnz8Dg/w0CsL2a+45YQF9+O33D9B/Qf9s1Z35JGMHIPzpf6ChcFAVCNRTN7UKEBoQTOCGu/9/+/3pVsAmBx0DRCvyI++xGORj4rlvPj7wi88YQUK2B1wJ/JpN/gOYDEXtK7T1oXd9nx3q3rWKpp3alJe7Xu4MgKsFzHn3ZF60UAOSrvGHT1DXeHepv9q1dVcxA4Vttb9CMrsDPaJIwX+Tmo9mZuVFHgH3v2fA43vApP7QQMs3Fq+QMmUgBBqlVYa19ZThW4+4gN7wthwwt6Dc67/mUyP0Jlfdy+HhHkAEPOM8Q/p5ijlo3Bmofbd5k32nsaZOpt87Wv01b56pbtVTKBwA/UBo0EXu1AD+/kypJiy61L37z3u06mcU3GdUHjn4lsPQez+GHg0Z+tphCDqH/vdmhUn+YrPR1puFvl5Ba0XXzg+/TMPLRPiYd0DrfrIANfC9nb+BwRsmfs3TCAS5Hv7+oLx780nzwJmuBsZrC+3OH4QS6DfxvWfalDl1PeWo9TV/A19gCnRHGuBsYB5I2ylb3gROT980DUHtTfffG/E9MrU7OQNkE1R2dgoi7Xuea1tOArSqp2p5OhmknTdVTh9GTvgHqyDAHUQX8IeAEhHIfwDQd9cpBTATFIpfF9l38mgab4AWbucAbcF06L1CJ5DwU9AbUGVgRplogBc+3FlBmQd8DFR893ATWuVDmWmgfCpoPWPxo/+fj74n6F2TSXnA03KtFniyn6DS9W6PuL5r+YwUUDWbSuq+6I/BfloK/dgj/v41v2v4js6gUtOpvf7gGghUSNbcU3ACmgaARfY9Ax+d9PXRDB/d9l2XL/9jhv74743Z9/Zm/DFuX6CwbcvmCww/WtJbR3oFZQ6DDIlKr/nenT6/19jnR439gePDQV+gf0+rP7B4JvMXCH1FXpHpkRQ53pStzw9wAvt5ef48n55+zTXve3SB+CIDFT45fZiK/61XvJGAhhHUXjARP3pHM7WcHnS5O1gC/3/N3zPgWR0Ai/NganRN8UPV3psmiOcjXO+YDh7lLZDtTmNV4E2bjXRSv/FevuRdmn56ya3M++ebjAmyQXoCP0y7ElAoAIzayLvfWZ0bTc6Yrv+4YVLvF1Y61VIxtb8Jn98h8q64WwOtpuILogmlAR56edCGDzCcCnDq8TawrWlAx7zvlCZwBMwfm5BpIHqflv6nBvcaBuDjFl+mUv4ETZPtJ+h9SP0EvW0b7nuwvAP7pp+nAXmyGZCCH++07/tB23v55U/UeM7Lf63EE18eSG/ZU7uZTPwTmwC32qs60N/cSZ/vBn6XWzyE/X7Xs33s+H57eYOQZ5Se0x0gB7X6uZk6HAxyGAgE949sA8/+jbnvuRKAHZg+wFLStj2HcXyHcHAXo3zCcjzPsXEXIVAGQyl/bjlzBkWwuWuj6Jxi5ohrzWmSmTMu7SAu4PfI1m9TA48mbTDLcmiHQucuQ1mk4+GIjTseiqEuhXsIweA+TXtz74elCcDKp4kPkyb/vY+g9xR9WPrbi03OASU/b7aLx4eFmaNFYlSshPaMIv3Ayum5dVJSqUaandByyLgfeYt1V7E4nm6HsnC3B9tWNeFyMpI6XAYrYp1Ty13T0oTAHi9uZlumr/FLLI2juccTODnbDyexaDd4aadWyl6O86RJG0oDlVk6lVggrR+3KQpzxBxX5aFLTtKpvlW4qgyCnuo6egpNNHFi6ahYpLQl19JKuC1ISoz4Uhf3fFek8zLR7U3AacbQBUOEeDFyc65SQ/i5NGdgRHSueEnRR6TBQ6C5q62FsiWPWunaY7+yDaMSx9xUdXylzKTLUTpjh4rgu8vctnR7x6scSwzVPhCXAklbhc4NjhkvqWrfbDXshvLnzlS0wC5upsGLaFpovriP1mVdnm7INjQ6Wuq6bNgVjBEQSG1xJnbV+axl03yRJBbwQr5dszJtzyxCb45sdeo7ZLhul4v5ZUM5BTuYYmiHF9I8oOWZXlwoOcSDLUsuK9gOqjPFGQJ8rtKTEA64xq2MMeZSLtP3DXmUo+KEk/PEVAzj2NyOZjvfr9y9Lw/q7VgvWyUrFAv1BqeUFvYwWMzOvmLE4Em3oyxgjdMP4n7cLDIZzSVkjzZmplfoNbulDkktI7E7m3GebnAA1liPjYmk1f5Oi4aLKYgK5ruE1Lm9hTk749CNbXi7dgeyq7noSA6UYytJUGXrcetS/Q219pUe1Cd3Mzb1YM1H5kavbWFfj4u1Vp/Oc2K1zkUc8dVMKhBmKTOwjbeVmF5Q081L2uTFDarCEkJJjM5H+6Mv8u1sbQodgunaDXO1nNz0I2cychnPeZ4KdVoPZ9wKZgdgzFE7nOGQlp2VTcDSVdDQwDGtWC3HiDRZkIpuYA85a29S/MjE0V7gRULZlCARM+rW2MfldSMRpyvnhjPUv7qXRCSS5qhj7IIqhYNX7jECMQsBj0ixCZ3jwfB2hb7dueuWlAxR2Bw06SAn+TqyAzvRRE0/ettqE1TbSAU7BSni17uYlKOWw8W2WdWzkU+TdToeugNX4pfFXAEOO2bMArtia30ZeRemPAHXJ4Fvrm72zi0uvbCzHbgmhs0CxRGES2GJp1g4LTrJvPhxyYsrfSAOp+GiDLo4W0cyMUc5yt5je/so0JcOoI5KVl2qy+L2XFOadjjibL0yZoimuIZkVTqrYP3VS5Mzd2sLTnFPlV4SDJ2zoR6fXI8vw6VkdOP2jJIeWhI+ViSc5SVoUaFhd0X2VdPUyytq9LJmi6JoMUKNxlVmROFJO1ekTs/icYjEuPMPZHvg3E4T4IHwWtJguBiedyWTbFLOhefLXssje0jYOXWhkvVscSl7j8V1xQ5u3nC22l12mPOOIyRBE6o1vbTIdrzl3M4x1FwqOMSd9XqAb/leijbOjLnSt52KlynH45cq1sd9G+9dQXbJlEXWs0gomHSLC5G/cDmbhUU3yEGhjCWP7FL6xGAMAWPXa00dqc3VusG43JJCU5VBWuYxuqAYss+3/g2rL7NQd0SXEIlbsbYVA1P764ZdnpBoGa0Cak0wsIAvtgJGWJewz02KoTejKrI2ZsxmWCLtJIVbrjc1J0fodl2Py/JC63LlZbE6ru2T1GJE3e6N9MA3ttLq2EjV8loo6H6hS1ZjxxdjU4lZowTaJpcyrup3wTlkO+1yrjeoki1RPGxzfmcbTW95diMVLdv6Gkpew2YgcJ6mBocn1O6GzpjdqoUZ70yjy6wuvGvmzxRxtymJ0w1M3oW/yvNFBLBs5ftDrDknkhpTrBuW/YjHSDy76TMv5zHLH+ObtcvpG1PsQsU4thewE2rHw2bpBXvK6AQ265yhnVcV6AGNq9QJczrT+AELO0NbrRYbc88Ws1mT5Ani+Doxp4VziRqEMq4ZMbhRF3aeJdkKO+JBvaUKW6rJODsyzcG4nHAeXVRFlsCV04n1zLrxmopGKxq7SZvDbKZlwmU4B5rLeSeGys+RIRwvaEJK1cYk95jWt+4ZS/VWkNCoxlDfrah1iFGScQtq/OAlZIjPb/pJYtzYDi7RisXzWuYJ2yqHEh36cWY2cBQhnOLt1n0nKc0hJ0cdLwx6Ty2MWcXyItZRK5oy1tWCy9bNDG18Iwn3jutfsdI4XVaW6a2JBeaeWyIQF5wsRhFaCxWZFxt/g9S8uUtnAV5dxcu4GBQyQBCPXq33qVmUjpKcSPra73eg93jicdyLCO5edqUR9rzBLxq8WXauqSflbQ3vXKwZykFNtiHJqwvCMemEUFzFwOXU6reYg2WLq5OfzcxnxSFPWkIJNplo1nmvWzOcK1Sl1i09LcLzduAuJ2EQlsH1qlmLQ2YwlFQ6WYxwlM/ltRIBRPZyTdSRs1hXaEXrRlZytzDMK5WVczXe8/IlodS1i22sy9XNjtVWUDbc8rqnG7b0+zVfRIjbKvrYWGriJ462Xlxu4hU/m9gokEiCqgWxlvK6XB+aXYq7CzQTT87hhOpHPVeq2SG0KZr2vStvJpS4EuUOU7ELM94QMPU0o9nyV4vrrg1/GsGMYq9UQj2dr0Iyz+YYRsmwIeg8tl177OnIoLQkRs1+v+83/ZDt1ppVav2OKfztEOo2ss4jw5cyxk8ue3+4KYvlstC2c2PdEaMcb4/aMJPkKCWumYm0UsrGnGfwhVBsMmFI1VYVMzDAoEaecyYwFetLVgwR7JaWp3Rmz1VJyLOjrXqL23YbZ+FGLfP6FhCE3CPC1kOOkbXs5pe9YV5CW9LVLN6SRMkuNa6sA6HLR5GnSIbNji5h6vlaMUrVKM9G2h7HIJNxKRTWF9Fz0bMsFPxytzUWJDxcUz3Lrh2+uZ16fJFGAOC3TbpdKpddqMvqfkOkZssC7DO25xBWafnqcmYuuWVZlMYBoxlVuXrCoKlHZEgFXd5o+C7vjH65PqfR8eYagb2KwQRVLlJFrtbY6KRdm6yp841rZZjWxmiF+by8vMDRnD7VCmvyeyoP6ZFE2DaRzIxqTkG8ik6OXgl7bbSqLaqbiL7dGMGhM05519rmGKZE5MSzsgpnt9Usoo0SdKhVQASjczwPlVgz0qIzl0rZVcdVFyWxu8/SE4AFYjyi3FayRyWNwx0cq2KyBcA65myWCfusRfTTUuTCFgewt6+w3c1JNhnIp2EIxGDbSyHtDwuzUo5DHe3TJLJXGkzr+2hnJstd6FaitzX3QUcYh9MiYELGvXHBuiV2M3ZOLESJKRzJxs/r5axnF4kkwwjlI5a6H7RYJvINpe7zU9VWxWaxGsOajNhQM7erstXb+NJIlFAhWrnMUCA/TrXl6MirsyTo2ex4lrfGqgnCdtyU9KGgVFIThT0J5y4xWmcxFg/XuOPaPEaQ20GDbdDiFphIUWax9vcWhZ0unTxgidss6kOzWXOY7O42VBuFS3prjtUytjK2wygNX87wY2A3hKrGVqLSraFphD2MhB0tEdb14S0XUHSPWJoz4AJ+tU8i0zLH62nGbspbpYKpO3aPRSO1w7xFyF1LOGvlcGUyAhcoR7edzjzpchufT2BUnQ9iZmz9Bq10p07VXWF0SdIiF95DD72QFIV0okQlqELTj/EmhY9ZIuvuCj2IxMw2eF9A1CJHE6LcX4MtXWxgiW5pxIk4Ps3qeZnBjm/1IbnsriAwq2CXXmWGV2Hckzmf2Gj0yZWtsxp3eENRUra3kyXt3NLmMheFUSX6nXajAvhq1xIcLM9NUu+DVUeicAQmqyseJV6bUu55F/VXu88VPkqV9rBfRcKOhaMdbeuRelgOSF/Ci3C5KwCsXy8XYj8aKz1u+3Gj7vn5Kt36p4O4quThAh97jz8pNdqrpENJzblHiZitz/PNinJE7FxIneJLB2aux1EzsN7ldBBCjpFnwF5HlgaaL80W4/slylRM4anziC27edzA3drb0JQ9vyZLOOGpLZIGozUEeTaY+Mntvfk+O8WYqRVStKVUbdPG+LnVZn5dpBxc5zNnU28aUrWRhXBeitSWTxiGD5GdrfrVdFKI2HzbxtR629Vsq64U28Sb64hbCtlFLDsOsGHQrkaBzBiv6f7W68aZ9TsX1y32POMETzpsA8qSNbUoXStvjg0jrzAUWLIoZEaRbzuc9qM4YQuCbATHApsiS17T/RKbr9VlcyjFDI8d4xZZ9Ko5XOYZjyoJGKNaC4sEUtdW62asiWueI6Sc6eqWcpdkfXJorOhWjIFkclnEuGwvjPlVWZVBn5xW2OG8MlSO8Oj8uAlme2oVkYdZjBDaxsspl8xsNu/o7maMTulSqnWAOX4DWMGnVVPjDt5zGyE5zu2DrPgzZ4b1uInYF4WqbSz2r/swqtXePy36teLXS0SNV0dkrs74HWjU0SxqPCKXjv1KR7Od2y3wsGg2WIARpK37yLIt20S/6i7YCWGoncjtgZqp3OBKyZFU8SiPF7vlISILybcZoRqRW6Dtd8kZBoP+vFqmTh7MvWQWUUJdCWCu8IhVq9fhaseySEc4scHfcgy+1PNTRtU+jM1LnOrb1pfPwc7vT0ODG4VnHK5LOEIXCr2zffi4lBjUPHrn3osP8dpJ3dFE4oUX2zbDwzPHhvl4S91ALvr+AcMrNlBcEK+F4q3LGAA+QSiwS82xCj/XWh8fcRW1lwxlzgd6gSzWvWi0tLmDw6AcuChaq0mD4hi+n3lE7A5nCr1IHG3SR8QaTXKpHfN2Xiy8ML/MF7sIDnrtNu3JLx0RWgsv29e0Ml9JCIZTGJKv8/NJtKueC9hz3M1oKa9Ou3NFq7zHZOjO4xh4d46XxJ6jwoUn1XvlcmXCJXeclUwvW8Glv0TMTr6yszZE5a709YAM03qgrv0qksjttevqdQ3vEOqwPJiY3hDdapZke6JOkKtJnwZ8lHEPYFmGU+pRGIMz1/hRVa0qJLGaju3q6y1ZVFd4a2581xkbFxVuMxVenAtWVS8lxmxlbYvcEIEzbVK87eYRoRvaRZiXMJBbyHyNISrY2gvUPsmlylFBO+PwhFWXWJIvFot/vHx6mQ53n0e0/8LL0+lc7P/b8dzjJO3t5cz9bBTI/XKX9eVfUeaXTy+1EwFVHseOTdoFz6O6/3bo+Pmvj/OndcPjHeT03ujWvp1bt1Yw/b7MS5S7XdPWw7emAMNOdP81GLtrpjf4zfRLHg74+XI3JCvvR5hvbEGhe9/aAmjdgquX6d369CLEcyOrfbsNnkevn17cAUQhcppvOEl88+pyMu75amA6t5zeDbz8/n8BQMq3qW8kAAA= -->
