---
name: "rar-cowork-cookbook-d365-forecast-to-plan"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan", "rar_sha256": "8c3f09ec36d5164e45cb836a5920a30e074735fc6c3fc23aed764c794cca42d0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_forecast_to_plan`. The original RAPP
agent is preserved byte-for-byte in `d365_forecast_to_plan_agent.py` and in the RCI capsule.

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

D365 Forecast to plan Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_agent.py` and embedded as the fenced Python below (sha256 8c3f09ec36d5164e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_agent.py` first:

```bash
python3 d365_forecast_to_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_forecast_to_plan_agent.py   # or on stdin
python3 d365_forecast_to_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Forecast to plan Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_forecast_to_plan',
    "version": '2.0.1',
    "display_name": 'D365 Forecast to plan Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-forecast-to-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-forecast-to-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd97c4f030e417561',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt+skill', 'upstream_path': 'forecast-to-plan/d365-forecast-to-plan', 'uses_skills': {'custom': ['d365-forecast-to-plan'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ForecastToPlan(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ForecastToPlan'
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
    print(D365ForecastToPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZOjSLblX2HimU1VPUUGCBBLtrXZSAgtILELSVSWZbGD2PelXv33cSRFZFZ3Vb/XZvNllBkZAtyv3/Wc607+9mI2dZCVL59fVNdMoa0Zx2HglpCZOhCTdVkZgV9ZZIEfyM7Sugytps7K6uX1xXEruwzzOsxSMH0JrYfUTEK7gjBiAW3C1ExtF/rfkNrkeTxATGCGKXQ0U9N3EzetIbfP3bKGKjvLXQeqM6gOXGiTla5tVvV0ncdAITd1PtXZJ/ALysvMdqsK+gQUad2yghbQAYXM0jWru7o4uMbeR7kV5JVZchd6DO0yqzKvhlZNFaaTDOkpizFrM878N2CO25tJHrvVy+eff3l9CcH3l8+/vdixWYFbL2tg1LtyWiYB1cAU8K8PnuUDcOF0DQzysjIBtxzXg55XP1Zu7L1C//mfUWeWfvXT5y8p9Px8eZn+KE16V7POgGzgCtvMTSuMw3p4g5ZxZw4VVLp1U6bATKgCEUj9t8fMb5KyHPr79OzHxyJvvlv/+OUFeLY0p/h8efkJykqwXtlM398mKfmPP73FWeeWP/70TU7VWDfXridhQOu3r8/rp1gw8NvQ0Luv+ncg9ZEJlvvl5Tvjps9D78lOMPPl7ZaF6Y8PwSBMrXtPkR9/+iuxduDaURxW9f9I7s8PwYFrOsCmp+I/vd6d/As0exr0IfOvl53y7t+xBAx/X+4Vejrqr2Tf/f8PouMpJT88/qfi/mzC7O/Qz39p27+a8Ap5X17WbhyCIjKt2P0M/fZVlVjm5x+cbzd/+OV3IPq/FaNmTWnfJXxNzDT03Kr++vXnH6r77R9++fmHJge55prJ16aM/0zmn/n1vs4fPPgc9eMf54L1T2mUZl0KfWQ69FuW/6/y9zdIN+PQ+Xa/+gx9Xy/TZwZNRrwv+nDBdzVTAV2/8+NPL78DVEiBNY19fwyq/D/+4ztsUe2sqSEQ4DpM3El5LQgrCPydart0J8QKgWOf40D+TxGeNM486Nf/Y9+x9pP9xFrYAXjz1XsCztc6u+fFr2+QBoRlZegDeI0hZSlJXyZABXAKFspLt3LLFkCINdTuJzD70/QFArj765/K+3qf+pYPv94BNHzgkMLsJwyqmth9m+w4B2761NqeELl37QZIjTMbqOCFADJfgX1VFrcAwyabqyiMY8gJwWKAKoa7bOCXz5OwX3/91TKr4Ev6AE0MenBIBYMBH+pAnz4BW7w49IP6S+raQQb98NvvP0D/Bf2rWXfh0xoSgOyn14GGnCoKgCX8ZmIdEBAQQgARd6//9vvTo0BMCkgPxCj0QvcxGWRh5Drv7lV3y0/ogoAsd3IiBOghK2uAxFBYv0F7D/rQFyw6PZqwOsgAkTluDsjLTe0BSDWBOR+eTDPAfiDVKm94hZrKva/6q1WadxUTUM5m/St0ZCTADFk8MWL5ZAowOUtD4P6P4D/uAyHlDxW0ehfxBglT3kG5WZp5UJrPNTzzERfACO/TgXATSt3uSzoR352g70XwcA8YBDxjP0P6aYo54OAEVLxTva99H2NO/KXdeaz8klbPBAcUDbxyJ+0B8pvQmWD/b8+UqoKsiZ27/4Cmk6RnFJxnVO45uL73FP/YHLCPFuJLgyJzHPr/uwOZrFxutwq7XWrsGmIFTbk+vD+1XZO6j04NtAUQSMFHpX1rFd6B5h1vv6RxCFKpHP72GHmP2XPMA8OaEhitLJW7fOAZ4P1J7j2fp/wsy6kSzC/pO7C/ghS5oxgIKSj+6OGz9wWnp++aBqDCp+tvJH+Pf+lMXgI5C+WNFYN88lzXsUw7AlqVU00+AwmS253qswtCO/iDVSAYNcghIB8CSoSgygD4310nZMBMUI53l38MD6fWCWjhNDbQFvS17ht0BmU1pVYFahn0P9MY4IUf7qKgxAU+Bip+eLgKzPyhzNQKPxU0n7H43v/PR9/K4CP4QKbpgCh/SbsJix23f8T1Q8tnpICqyVS490l/DPbTUuh7/vnbl/Su4Qf8AzyIJ+r+zjUQqMPkkZsTnFUAkhL3mT4gD+4s/fYg2geTf+jy+Z+6/x//vQ3CnTpPf4zbZyio67z6DMMPuntnuzcAJjDIkDB3qzvzfXpnqqny7v3Y98IevvkM/XsK/UHEM48/Q/M35A2ZHh1C250S9fkB9jOfVtdP+PT0S6q43wILls8SgI6TvwdAtR9k9D4EMJJfuv40+EFO1cRpHaDROxoD139JP4L/LAwA9qk/MWmVfVewd1YGoXxE6oM0wKO0Bms7U7fmu9PuJZ7Ur9yXz2kTx68vAAfdv9q1TGwAchJ4YNrggOqYUDB071dm44STG6bvf9zfifcvZjwVUDYx6wT9H9h7V9kpgT5TxfnhRACvEFDTr4O7Fd1UdVP7YAGrqgqQsTOpXQ/5pOdjVzN1WB/t1z9rcC9cgDhO9nmq39c7PL9CH13vK/S+D7lv59IGbMR+njruyeaH6R9jP7avlvvyy5+o8WzA/1qJJ6i83o0zrYnJJhP/xCYgrXSLBlCnM+nzzcBv62aPxX6/61k/tpC/vbzjxjNKz3YRDAcF+qmayBMG2QsWBNePPAPP/meN5HMSADfQ04BZlI15CO3aGOEs5gTu4gvbojDCXNAoYmKIi5A4iS08mwDjbBQzXYckcJukcds2cdSZlHik6NepLQgnRVzEczF6jtpAAXSxwOk5iZq0Y+KkaToIRZEI6TkA/79NjQA2Pq17WDO57qOnvWfnw8jfXiwCByN3eLVfPj4MTOsmeSYtJbDoknCvC3lfNoaecQimXs5nuhCPOCqvhG2lGQc5v1xZL1K5wtwHkbjV63IrBmt6mZLcrm1SJVGzRE2xkw7XbKgk3LCwR1iSLl62X/rbERhOxSE1sJWuzkWOD5wNfxN6J0azKuBhWFJHcbWThEVsE7S/vxTZmNg6D7Nne46cFavSctCTHFvONC58MR/CIiA3uLbAdV7d8vNTWaUFMxi6FLEenoTjVohvXLgXpVmmhkc3JCiPiaPCvGrsDPHwmdzAapD0vHScMxha4+Mem5l7dUSL23Fx6OdVRMSGfqTQE77lBsqT0oYUL9yMlFK8GYUZ5nmBu6fryljo+XaoisUZQFN5028Rd1WKPcoZwyEWCSWeZalUdLEmG7f5nraG08I184t1kwuPO1Q8IxZkwfYuLWLlBm/Ys37YGJfsEujyZWWYjd+u0MYgrqdhrgd7WbFKaSXku5g2PTi9ETx2sYeLEKbEdjPixbZjcYGhNKpeLsdZvSgSsT8xhTHAvipGG6bzd0cqGjiP2Tb6LXctJ1nvN1ocJPKB55clvDvr3VlvQd1cDiZ6S6hzV29kXCLiG3GI1VwuN/VQG6F1EIF/S+EwCwVtBQ/7A3uutthgrvpyk3JdUqjxwq2SVJuRcGGnIaVfGLvcCRK7rbjIL5Zi2azHw2Z3ETJCcEIcOe1Yoacb31p6F/TqOUIcdE0aEdcjKjftsu/HhbBQ+sDykICPz42l8olYVsg1P7exXZ37NdoO89vKQHibGilLAX2GsHXWGixRdkbCvRvYe2/j4b4vkOSOhYM97xBp6hjny8JfDjB5cgozvuq6HuSZuzueZ0fMwruxdnfD0nH4nXjN2C5l5k6rb4WTNZ8b83CuUU57Ik55J2qVvqb4G7UM2rY2+yzvEZjaoQiVjORgStTu0GnlJeiF3eIcmyZ86BSqm8tZrWwMmaSjyG9iQjeRht9n6IG5ZtKpP1e2GuKewGywlcK0xsE4GVl/dcRCHXl2j/rLoNok5+VC6/ii7hx+H1hZulzZ66WsaIsw60Jb7ZtVorBXca9HYXINC+akaJvAkReBrTEoiW95JpntLnTsa7sOEZe8ckNWp4Wy2VzFABUdWOkzr8N8CZYEdjuMphJjmXdcO2Qsnb0I9nZBkrcxO5eqxsU48+ZdqCTuXOKwPzOhUuTVPhdTwYszcWWtG62a2VGpHuF+vOiq0jhKrt6o9SLlhiq4Nat4szwwW0a9qepcmlGKSBDLfn/xs1CVucvGFi0kLDezxLCtqhjGnN6R8oBwS17gefLqwvXpUCoHuI1lz4yRgiXSak9HmLngfXkbyF7j1/R6xMP6MLcZQrgliLA6k3lKpWmZoizue5czwbEZNhS7+RIreHHg+Z3t1PQYe+aJ6Ff64qrWe7mOa/p0GEjratsgpwOePwwbk6g1PhVsQpMDl50Hl8Ak1YYNg5YHmdBdBVZcL2Ykd8Zh07kodO7eLpXu0J2zQNpCJ1FyExvxENXt0ombRUN5A6/No9ase4egZyROszusa8GOU5lHV31sDlHGZXts7mdeIrnULcVUUopg2V9tWKY+yGVnRkW4YdtEcLYkz0hrn97Ysxk7huwwWiJLEeKcgN2AGiSP8xLtRnIVJo+KTqwUeyMuKUMtY/YAd2wysyzpmihx2M+3pzoLNhg6JKZhCT1mV/5MkvllfjP98qbZ89kmcK39LTmz1CHsePkUclw1KDpXKARdXsNrJYg9d5VPFbU4+deuvsiZcwmJjZ2uXaOU1lR67gjaSw2CFjV4nG33iCVglDXnOCU8t9TQeyRyu0ZIHNH8xtvBi8zfiFhqr5quY1LKmc1uK6q+lTh+yigXYDgenmnFiiUZZ8q25XGcu66YGJSbjt5GuTC2rGIV/emwc/S8DmrBwdmOO+8wRnEY/twclG5wNSBKC3A6662i4Q++cnaWyplY2wIDY9d1E+zDbVefA7FbEbqrE8ZeOzOpWxiOYSgNGZCxjQrD9oilgPxWsDuggWKvNHMlJbCpbsRrYPbnml/BXYzOb+Y8S8urF51xrOt9caTdatHidM60VSrPFseLYjs7doyP/RzVse7aqVeNXq35Bp/nUknvSsQJsZo1hcMow1m+1YS9LSOAGPDL9qSiXCOZUuqVTS8r7jzQO7uYo5rb66uDvXZkecO7LItyUdScvB2a61Zxo/puqWCElwj2tamO26NaD1nhzq+znbCpuGUxn2GypamxIKsGDzOCv5mtxX1+2ef6fFPMbElU+ltoqMRKPVLlULAL9CAjtLCu9MV6t+T6hHTtVgrmai4RcsgRgXDskUh1UDtsRJQSN7Y6i/x+RURqutyJRp7hISsa4cUWwmt9KbMTCieHAqH39T7jQAiqkDUOVndeLjNdcod+nQ87cyfIIZ1H8mWc3RRGQ4xCrK8bQ8dvStTphq9eZvJyKEUwXFtFSeejPqatkpNaKyslXx+F4IYMfIz4snjj8c7U13Qxp0G+MedoQ6xvdO01g+9JN+d2tdfbcdDXcbEcNm1PlW69DRwz888IooisV6Lp4LXYeS0h3MpP9i4uKWK9hQl5t6k00vLHusIxVCp1w1hUXOzudsfLnohlApuRx1rmxsNlz5ZiLLjd0Wc2RLDMtLmSUG6Ez1Xdt3byoCxuWywzRdYXU5p0okIbN8w52y7dTB3mecLFl8TobwS9PhXxoivcoT7ojB84p0vBy7msGAfdsHWhm+ldYUZ5N+oMZReK7/Wb7NxnlHLgDpeWTy/2ItNFXjSM4XzeOEqserFkIj5nqgtuJXcx6CP8JT0OZ22lO0f/GiCcYTI8aRxpZSYxrUbchILTtqKezRdrdj/jNYGp7CjX++tN36jjzThbyzFfpmc+0onFmS+HPSzuKw3BiSEID3HMaWwCCkW6DbdibLZ2n8xRcxlxONOsOYtfVAXOrue9teecNWNqMBX4NpY4+7kakZtUWPe7TSzK4ypCqlsYheXO5/NKNYxlK5vWopGxEyHWVVYkaTvbX7kV3uZNsLXJ5KYJpVYNOydzWXIbBNTqTJD0gAoFYGNE2R6I7VVQjoLd5MQuiNa6XJJ4dp451TJnR9dDrhTXhIce2TD2iS3P0jYZwoVoDzoWK6nJ9jxdX9ALrxWHYhuZo+raJyFtDb/uxQRVNvBqSYJqoK/HwuHRgseLnD11fB7R6faS7HN7b8jtppBNgtprcbRytlmnGQsX2TZImCceEjaDUR133kzSsoUkn4gteozxoD4vyb0c2b20vRWDuV4cLFOa2cdA2h62iUsyu2zLhAt2aA+6chHX6nKz5gppTKzcHgQT6WMV9pcUXqpNm502vT8s9NFAQ80d+JI1Va4ye6NanGQbW7OX3XCaS7G72SRxvLzVGptTYZSLhV1zLEFrdd+bGaocqkhp0Pp0G6qxDTYdrdayEDazttjsqm1Dx81lq5faAV2G1UXbatZFTAYHDQwZZgHKrwNaW1oHN3B7DjY8duZ1FamgyNqOkZhZ7i8rLMOttliTlx5QQzR3BwSEoglaGa0QkiHGc4EXFN3ZG+/W1HFhwgumUFgMS0mnGXbFJc4d6zCz6YvTYIo0F1LLpT27t5nYv9GJORotNt94mReOKbu0bphy2u83SI+aDXfwQnJ7MUS4xHyg0QztbYNSMhkj3HVPdVFK83M699vuaIa+Z/bUcS3isX4uMdri6fB2WraGQ+Qjh2ttdAlJrisbIrwFBLHbLr1552CWW4exdYXTbC+MvGc0DjqLqeOOiUBH4nnU3qs4Fcn4RevB/RoW41PjN3xGFBe993GN98JQ3riFj8wzfefPs8NwHeUmkaqdEx0CD99QPbKVsJQ4mad55puMUEpL0KbZsnta0/vOF+UsT49aeUWLK/CQg3CUGoNGf08K9YqcseeAR641N3e0VhTtbGRyLqBlKqv8kk4bKwjUNFX8WWuUqqcM2oyBy+TQbWlgLOnsK2GBovPL/uJyNuemlJmz/Jhuz4dWmsHXJTOXk4TFSLLg4p5yw9DZNotZQKXOpaBxVBJU8bRyMP3WLI2Q4WBKOlg4v25Fspnhg8nEDZqRF/aMKBd0ozsJi1aXhZM0pxlC7Lp9atFgv0KQdl25oCNLRNDMrrQZ1pjaUgMbyIOirtm1OoZ7YZuKoRMKZXCbzSvYYnfL9HaqNHq2xTNzny/EMjyfM784rf00zbZlfLrucN5cHSXRt9ZsS1LXcd7HY0J2hyTNVZSpEZlM+duNnDW3DLelbmQQeGCQNKmTrp6vomBxYN1OMfxcxvdnkRyGruK9dclRRbmbYdluHAnneKphPBT3cX4TnVbGriJ51Bq5GlnNHandzuFHHj8apdCcbqbHYtfspES31jKNoGzjdIYmBLq2uNGxZrjhmJG4P8Ll9TxbZ4cad2hu1Nczps1Hgr5dW7+W5ux4luB6H19FlFs3JoNZjiKWR3Q7BgxZXg5l0lqESTeHNSs6Q09sM7yplS3tklE8rpH1SoTzRJvT3RlvlKWuSvh1thgjU4j24rpTbd5wHL2cBWeM3pQutRcof5tjF0L0AVSj5BV2ItDdOqjEtV5D9TNUUSkYO1x2Y23OFv6GTpqVxKZdWksouZf6laujESxeTrfIQ8XGz9eIZNkyPBtp+sBI7dBGu6vLwPTa55RuPzvytr+V+ItSHmLZLmdKtXZLJ9jesnOLKkW/JJm2D4hNvufCU87jrddahhZJ7GxvHA0Srpr+SKkmHIHmCdse8BBvqzFpCyo8jNeFzDrrBFsspQBWwRZVOFDhWI8TtR5nF7IczEtb01iRu6II2zKqjxiDB6lDL5LyNDSdDyrfpQDquhuNaq/jiloyThfsNotsW8FUl4UFfEqoRNAQoprbiXgJPBS+Npja5lptDvOFQYpHPHSFhXu0rCVGzrHV4XYkc933xnmGVnYCmHCNquRxdElsf2zb2TGrt9JldbTaI7NBzdvqhLneNmUzrcDGg656ra3tmiuCIrubLyIhLhjEQGVHZ4WIyGGplfTSx0IlAmS4D2wELs4MYhBlkknyHFveZnRwRqid35I7beUMHr9cLl9eX6ZT4udZ779+wzsds/0/O+17HMy9v9u5n7K6pvP5vtbn/0aPX15fSjsEWjzOLqu48Z+Hfv9wcvnpT18ETFOGx+vR6WVTX7+feNemP/3XnZcwdZqqLoevVRY39wPT1xfr+dLt6/PV3Mtd/SSvv95fVU+nofeXtpND//mkNEyntyiuE5q1+7z0n0e4ry/O85Xj18lqt8wn+54vF4BZ6BvyNn/5/f8CV1o5nWYlAAA= -->
