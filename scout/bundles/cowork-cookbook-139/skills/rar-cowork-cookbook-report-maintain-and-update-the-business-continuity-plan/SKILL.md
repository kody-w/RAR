---
name: "rar-cowork-cookbook-report-maintain-and-update-the-business-continuity-plan"
description: "Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan", "rar_sha256": "1096cdf33c530254cf8458b0e7fb14f976a487bb6e06db14f1a8e2596c1a120c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_and_update_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Maintain and update the business continuity plan Summary Report — Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 1096cdf33c530254…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_and_update_the_business_continuity_plan_agent.py` first:

```bash
python3 report_maintain_and_update_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_and_update_the_business_continuity_plan_agent.py   # or on stdin
python3 report_maintain_and_update_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and update the business continuity plan Summary Report — Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan',
    "version": '2.0.1',
    "display_name": 'Maintain and update the business continuity plan Summary Report',
    "description": 'Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-maintain-and-update-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'deb6979754c5f54d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/maintain-and-update-the-business-continuity-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-maintain-and-update-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportMaintainAndUpdateTheBusinessContinuityPlan(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainAndUpdateTheBusinessContinuityPlan'
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
    print(ReportMaintainAndUpdateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5uiyJbuX3FyPnT3UJVyR2o/+3mOKAKCooCgdPWTzSW4yP0q2tP/fQI1s6pnuuecvWc+HKsyFYhY8a7bu1aE+duL07VRUb98edGBk08EJ03jCNQTJ/cni+JS1Al8KxIX/ky8Im/r2O3aom5ePr34oPHquGzjIofTuS5O/WbiTJq27ry2q4E/abosc+rrpAZlUbeTIphkTpy38Ocuvyt9pwWTNgITt2viHDTNfY047+L2OilTCMjx2rgfry5xG03aonXS5tOkrUHuw/dRilsDJ/GLS968QlBgcLIyBc3Ll59/+fQSw88vX3578VKngbdetDuQzRPEPPcPdwhGBLgngMXH+ju4PBQIf4dwZnmFZhqvS1AHRZ3BWz4IJs+rHxuQBp8m//ZvycWpw+anL1/zyfP19WX8p3X5Xc+2cJoWWsZzSseNU7jM62SeXpxrA40EjZY/LRjn4etj5jdJRTn5+/jsx8ciryFof/z6UkAIzuiDry8/TYoarld34+fXUUr540+vaXEB9Y8/fZPTdO4ZeO0oDKJ+fXteP8XCgd+GxsF91b9DqQ9vu+Dry3fKja8H7lFPOPPl9VzE+Y8PwWVd9CB3cg/8+NNfifUi4CVp3LT/T3J/fgiOgONDnZ7Af/p0N/IvE+Sp0IfMv152jK1/RBM4/H25T5Onof5K9t3+/0l0OgbXh8X/VNyfTUD+Pvn5L3X77yZ8mgRfX5YgjXsYHW4Kvkx+e9N3/OLnH/xvN3/45Xco+v8qRi+62rtLeMucPA5A0769/fxDc7/9wy8//9CVMNaAk711dfpnMv/Mrvd1/mDB56gf/zgXrn/Ikxym9+Qj0ie/FeW/1L+/Tkwnjf1v95svk+/zZXwhk1GJ90UfJvguZxqI9Ts7/vTyO+SM/MFg42OY5f/6r5NN7NVFUwTtRPeKrp1AB7dxBkbwRhQ3E/h/zO0aQLs2MTTscxyM/9HDI2JIfb/+H+/Op5+9J59OH7T49s6Jb5DN3h6c+Ablvb1z4ts3TrxHzq+vE0hYMNfjMM6ddKLNd7uvuROCvB2hlDVoQN1DknGvLfgM6enz+GECSffXf3LFt7vw1/L6651x4weXaQtp5LGmS8HraAsrAvlTcw8yNxiA18F108KDIIMYkvInaKOmSPuR8yHSJonTdOLHNTRSAcvEKBva9sso7Ndff3WdJvqaP4iXmDxqTTOFAz7gTD5/htoGaRxG7dcceFEx+eG333+Y/Pvkv5t1Fz6usYNF4ek5iHCtq9sJzMQug8OgU2EYQJq5e+633582h2JyWByhn+MgBo/JMJIT4L87QBfnn3GKnrgAGh4aPRsNDtl8ErevEymYfOB9FsWR76OiaSc+KGFNA7l3hVIdqM6HJfOinTQwXJvg+mnSNY+C+atbO3eIGaQEp/11slnsYHUpUvhrhHkfBCcXeQzN/xEej/tQSP1DM+HeRbxOtmPsTkqndsqodp5rBM7DL7CqvE+Hwp1JDi5f87G0gtFU90R6mAcOgpbxni79PPocFnTYA8Bi/b72fYwz1kDjXgvrr3nzTBKnHl3hwaIBFw272B9Lx9+eIdVERZf6d/tBpKOkpxf8p1fuMbj5R/sL/dmiPDqDydcORzFy8v9DMzOqMxcEjRfmBr+c8FtDOz3MPIod3fFo3UZ5MNYeKfWtr3hnpXdy/pqnMYyZ+vq3x8i7c55jvtNSm2t3+VAtaOZR7j1wx0Cs6zHkna/5exWAkCd3yoO+g1kOs2AMvvcFx6fvSCOYyuP1t47g7ujaH5WGwTkpOzeFgRMA4LuOl0BU9Zh8T3fAKAajwS9R7EV/0GoCpUOfQPkTCCKG6QRtdzfdtoBqwrwL6iL7Njwe+yyIwu88iBY2uuB1YsH8GWOogUkLm6VxDLTCD3dRkwxAG0OIHxZuIqd8gBl74ydA5+mL7+3/fPQt3u9IRvBQpgODBVryMtKyD4aHXz9QPj0FoY4h9vDRH5391HTyfbH629f8jvCjEsDET8c6/51pJjDhsuYeaiNvNZB7MvAMHxgH95L++qjKj7L/geXLf9kO/PiP7RjudfbwR799mURtWzZfptNHbXwvja+QNWB59OISNM8y+fk92z7DhT4/su0zBP35Pds+f8u2z/f27vvlHtb7MvnHIP9BxDPSv0ywV/QVHR8psQfGUH6+oIUWn7nTZ3J8+jXXwDfXw+WLDBLl6JErrMsfdel9CCxOYQ3CcfCjTjVjebvAinonZqjn1/wjPJ6pA3k/D8ei2hTfpfS9QENnP3z5UT/go7yFa/tj8xeCcauUjvAb8PIl79L000vuZOCf2yKNZQPGNLTPuNeC2QXbqzYG9yun8+PRSOPnP24Y1fsHJx0TsBhL8FgjPhj4rpBfQ7RjxobxWCk+TaASIWTOUcfLmLVjn+FCnRtIzsAflWqv5ajFYws1tnMfvd5/RXBPfMhYfvFlzP9Pd5L+NPlosT9N3jc9951l3sFd389jez/q/FD9Y+zHftgFL7/8CYxnt//XIJ6k9CgDjjuWvFHFP9EJSqtB1cEa6494vin4bd3isdjvd5ztY7/628s77zy99OxN4XCY4J+bscpOYWzDBeH1Iwrhs/+trvUpFtInbI+gXAxlac8PCMKjCBSnSC+YkdTMRQETuBgZsAztkDPGdWmA0v54B3NmAKfgJMzBcNSD8h4h/jZ2GPEIFaABIFgM93yCximKZDEGd1jfIRnH8dHZjEGZwIcV5tvUBLLvU/+HvqNxPxroe/w+zPDbi0uTcKRINtL88VpMWdOZ4oyrRQpyRJFhmJJRR1nFdgtQEzFnlbqhuz23FdpzuTod6obTqeTsZLrgHFsZvS13+wgpNDbp28wvQSIv09KKdJILqcY7+rmNBOKWnTWrvcGRvNXMwnqq2de8iBmjW8uxlSRDTRJyafCxHKxlyrWqbaVsyPTqYUiL1csgNtbOqm70fjedQXftK53EpchJ0dzUsbRKLm5Z4ShZrSxxWhj5Sq/0nvZlvEqdWJYbZqOvNIeKUyShdCrtV6mV3vJ1dNmcyxmr3lrW7280K7QD0isYvkciMCfK9crI0tO5dlKzSOpTsd3ZJr6YdSSTyzSXIIleYrG2k8CSkLDVsERmPk4m6xRNpqW4ExtEuq1IdNAbLDIjsKY4b+XIl2y53NpDHbm6ueKORz5tzbWg1HzYNW5RZR1WYGpHxQ0u70pAd+s1lS88fZ1c5NyXOY6IwO2mmrFkHWhjUJWKN9ay0UT1TVprOQ0qS8d8m+IWxnJFzdtCWlQztaGjWQpW5yjoo71ydG7u1QjLXnaUlqdDCi0r4VT3JsGn/hp1N7Zvewfs5u0u0WJY1wu/y8KZc7Ej62iW28WRWVeNu51iiIsGizRSQ23hpIcw1/lGy258iPenHT9Nz4F5LijstjT1JFTWKn50OnVgLQsPOFp1h3BpKSmundkct4ajSrauJVayBgSSrg3VOmrVVW6PhjavZ8f2QCbuwuXVYGrLS8lcXw4BK+8LpQtI5cKoa08hBNfeNxylMPws8vEGq+l2kaE7aSow7gFTh6qqdWMBKwDnZW6Kn1ZqsyYTwUSToXEKjD0W+HBjzxmmhc6ZwMDZ72ZCugX+EdyispOXmErKs9WKNbWZcCYlEV8mAmVKcVoTS/ZECcaUOgUXmwv9vMkPZBszluccJX5oBuISG87KtOxOzrXd6loBC/o0aLaDal0kyYxqvoQq7znJVBJrb1Jos/aW3GpN7EpV1c40KpO7BlH0KNxQmoUb0ZFXgOjMxTkZL+Sgwfjk3BhtOCe1TNBX3rzLpJYbrBNl5/tUFaVbAzi6Xx8c8YilxNnFp7k0ixl6I3WJYWkDr/JiEmgOvpN6RUM3KYbFR22Ji4ExJW4ml25wVEOIGyKRBXZybCJs+2F6Ea0+K7AD2tXLU2v1NSKnF1ApkrFIhzzBEz27ZglJi1IakZdgfiyUgJ0P07rp5GmrqLognUq8M+WLmsRyEctJoZpcNV+c5mCTWv4NbTZqn5dcSenxKUemfXbW1fKqittqbcdTZacLy9a2UfrMtgW5VuStrBvkbJazPkWc4zV+ptrUdrLknJmEjlhgJ/O9za8raY8Gu1Ama+9qXHC5FsuVEpcimR4NB10PB6Tjeavcx7a5uwqrZCXT2JbrOjSmS7HfyKeE92aKlfDHjuFslQAn1o/iXXIg1uuDIcrnTWdGXBltrNIsmsrncxHZ16mrKc5GCC9zjw1orFLxM8/sMLnc+polhRRBTXOPPhx3eZlht+wcq9cF1c3O7vq2tntHw/pBzdlZOeuv5bRZ1g3hHpb7y+1GHBKbdPEh7TWpx4Fny/EK7wCx4g5BeFioYl/beyGkok142yXE8hxxyvoaxNf9bJERy2qNHmU+cGMEdPuFneXc4eIPiQVcx5EMnTuF+p7T/HW93mrTuaUDm1mcOkWeh4etTi9kEHgLJ4pINN2Iuuixp4vUOIe9Vmh7dGGt9y40q7WaSfHC0QpOrIBdrkPD0PLogIiiPeskRwfNdbYtBKaESXVtumMN/VJDwDSN6C51BbkyY3c7U7Ijd9sFJXtIUnG1RU1Qi17CSAmm9gZ/u0wDQVr6Rw8MOMYteFuREeAHQS+mK3KG6APZipBvuoQbYlISMiJPDe8QzXV9Keo53P1hBjaH4OTCWlDHg3DiLl3RIdbpdmX2my5MbWOmKYmw2NVdDHO50igNu67N1QGtD2K1sTna4KNWvvBmdAiPmmUJJm846nkBGx2hnzM79SgXBIsifsnJJMhnlnEmSdcKmmBfEdctOJCuBtv2IWz1hGr8usIyjRJMrxbaqp+BqcAjQ3gSV7fKlTeGKDGGukxOZyJxYkvYqJWnHE06mZ03QiswJLLGhaXK2Wwwtwdxk1aKZZqXA63ferZlfF0ZltFCZonM7ZObsExlfluShuLh+73mHiPcKIG5ZKodsrY4D3To0mluLglqqea2h1U6mGpqGKbKyxVOEbCoMWgUcAlXHi9D7vvFerMC3kzaSzTAa1XJM9iJJzSZFNd9dY0aadN6obbndyESy9RVVujbYKvH/HI8rWSTLjbLXTyr0i2sd3luDNshDxdsWIq1tCJEwKDVpi1iLS8UN2IlPt1IUqe13O169A5m42lUzfJ94uZ+Rle8TgtTgTjvEyXNKLWdnuJpbi9Q04jRQ3rasYJJNzHqOMzFms8Lcwuuw7nJio3aaqvqBm7owkDpMvaWMZhX8pRfHC00QwMPUU5LvsSqM4Kv1lgktmGWLE9oZPKHo7QQ9zyH2tniFkqYIB4uOypSqQBBbX1vVxxbrBAmRHFWFSqG8MQ5l7DmXOnDWW1rTG9NsUrPlKbbMNFZ2rPTKTKNsY4uQ4TPOWyx6gxy2uFpwg+Ys9t1BUr2m22aU5jl6O4ssPhei+zc1W/Mgc6VdlFKqD1nTBr3h2ox45pqvzr3m4J3g+u2TRguC8gY1ZX5Zm1sPE0FvZEgxWyoBeF800jqmE4pvYRdXNv20soYYNNQq2Gu6NS+kI7pio7P4mGjp3inyhm5q2bJdnGgyllUCCvpqsoLRd4T/tXUwHrDUpYzzcklvZCoen0SylKjUWwwpltJN2MPTaor15DrveifeIYL4+y8v5yw9aZc8Lqaz24XSZwyZ48uz5tqhye4q8knZO3G3e1yPm0UxV7FPWFby1WV7I3rlt/pqsnKgWfyw9HeCQJpbmzQlLw5MPFN8hQYnSCyQ8Ex7GK+Z1KLXNhXxgtPyzrGqgGdK+WUuFgIqZHkpYvCUqZKHbdn7FWQFCFBT1ZK78Hcqa9rG+Xp8/G0XQCmsJEDFiFZXiPcBg1nxM3lBJ3qCEXMNBkr/EN8ORdrYW3oW6p299LpSrrGtlp4x2ZjCnxJkws0E0I9S8S8KlyOGga6LCWkjGPYr2tL7zBEunbYM9db7KsL3NqldXQO+TNCiF6V9r5jbG8hKiLZbNagl7jbXB1SMqfFrj8vNDqVl0xyiJS5jAnafl2fd+q2tx1DWoAIKGQIt7BGrsAmctuFTTvEhX8qMmPOlTFP304nYto6onYFYYmuO80deEcVm2ixv/C7bqc0033N+hZCz6h5LpLaCWfzvccO+6MtZUeqqixKjBeiZK815HBtV8SKaVWnCMJ1763Wx2OiLqn5qa+o0j1E/Wllo87eLhxt1lCH8GAuZwF6PVDbNNvOKcoZIBNqt17qBL3KDX2v9icmaKxu2583Lak0ri2xSkOFVdO0Qehq9ux4MHaBchRvzvnoaYIzb5IDcsDtsj6JZl3t5zdRyDWJ8wZLIHqK7Nju3O9QFbGN+XqfnxPc3wpGtXKGC7o+5SahLiSRA0UBzmVen7owXmWEQ5kot+i7m2OxJA1hutfiFFQddvFWU61j0SoOmGu9TZt2SXgd0lfHlvPd+VRF4o6o6y29uLXn6fGwAZFM2u6pE6lyqJIUXWHxBSF3GhNeSJHkXNztjgqIZ+LRxqcwLzHO31rYxlbsZtHwM/HM+OXGMZVpJAYoifGHwRYukbdaxdMb6LHItvTdPiY8gu7VPlhMNUTxxRghO0Y4MMzMmU8NnzBTCiPt5gwSMUJWlt2eC2LO5BeSPw/KFJmdt8hFXFyTKF5Og/iIqHkYiqpcMNkRwyPLmHu7eImBa4iajbSb3w4WEyo0Sylk1GzR7fRyjPNwzzr5xbRvZrSwB/wkWWImkvPk5B8AqYSbhTZNQyBas/5wqWiPqaOTTuk+IZEqCBFiLjCrUJ2qlGH08saTjKK2eXOd8cHlpsz2LcoKitgaO+Z84YzpzGR3vs/B8CSnTLOMRPWK0PSiTtxz3zRnXdhu4MZmlWcBC1BhVUWbzbrHb4ejATc3PElv/SuT4MeApqa1KC5UVVeqze7EZZKU9xcWcnkjzBiVYc/rQrZcZ9puNFsT3ZNp4+7ZQYIUdyiNMW79PPZ7dJmpuZuyYt0razbMivl82jhdfjkMsHsiLbjVIlSOZ2KT8tRIuF0MQjlOU2G5V/CbsKLomDy0qObk5rBa8palcOj+NifccN+sqNqZb/tVSc3m5MKdVk3pkMwtZi5KlpcLfGGimp3LkMKRRlwOJLLc7PbTZFXszGBT1O1WXuKq5nJitki5fPCqzgi4S0mqDUEXzY7xo52yKlE2JnZXhVzGkXzhkNKimKvE9EqjbYiFq96SJB/AbXNaujWXHW99posbNeFJ97jdbof6vE27bk7j7lFmWos5lYbDq3P/2O8zWFJ2TSOApg+3U3V6LBXzwq8RVAEMec2WJ+Cw7U3mAjSNcJSw6Fux3cxduveyymHVtsOlZrunaFkiQRTL7MK9GFjEhHyhyltYNZdwqMvH86U8TLltEchLrTlHJJizsbuuqw5yTSNoLtMvFSBxhY8j7kzhfMpu+2kVbJuOZogb6Dx6OnCARUTuuD63CkIVIruleYIKLoGv4Ft8R1JBRmsbVkjxm2e1WV1uAk8XCGYXxEuClSRkKiORDynriJ7D6zlcWRu5CFe7ysFqpdp57G2Ha+2hO5019ObTWRpw7Dogr9s5yiekcsA8a7djyTIWzh2vpk1KEETsBbbvXoZbfOumBuP35mpH84cDpZM7WuSKK9ybTbFW5gV3tT2K2bIAuL2pYYsz6wKXaO2YbX1kz7R13vCaC+cwm6NNOaGGerv2UtdVsmYolchvyXxVRwtVqfer9ZnNhpWJnDB6Q+clbIPYTZPPkVmFb5EU6AG4pjWWg30gWnstaFlgKAFHMNcLp9RbQq+5IC1rvPGyjCZggBLqzce6PXX0G0o/eeyGH/rZZX20K2nl+ivE8Lb73grU1bZE2GEDqLOh7IE6Z3QjxNJauYbDQdSIfcOpx8FZ9FcFKZPZQXWCob2e1F0fO9RtiQo+0wSCdmOOy8tu1m5vqYzK+/n85dPLeDL9PF/+n34FPR7e/a+dIT6O+96/k7qf7gLH/3Jf68v/GOkvn15qLx5x3k9Vm7QLn4eN/+lM9fM/+RXHKPT6+A54/KJtaN/P8lsnHP8C6iXO/a5p6+tbU6Td/bD308sHbqi4B99f7ibIyvEI+4EDfnD8LM7vh+5vbfH2OGIGL+MfR4xfIAE//nYZPk+fP734V+jj2GveCJp6A3U5GuD5rQnUG39FX7GX3/8DMB5W+nImAAA= -->
