---
name: "rar-cowork-cookbook-dashboard-analyze-production-costs"
description: "Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_production_costs", "rar_sha256": "3f462464337e553334dc28bd287184c3af81b461ab00dbfa1ab976b6f62c1ad2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_production_costs`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_production_costs_agent.py` and in the RCI capsule.

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

Analyze production costs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-production-costs
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 3f462464337e5533…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_production_costs_agent.py` first:

```bash
python3 dashboard_analyze_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_production_costs_agent.py   # or on stdin
python3 dashboard_analyze_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production costs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_production_costs',
    "version": '2.0.1',
    "display_name": 'Analyze production costs Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b8bb1b6a440ce95',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-costs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-analyze-production-costs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardAnalyzeProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeProductionCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(DashboardAnalyzeProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZOjVpbvv8LL+VDlVlUKsVMdHTEIhIQkEAixuhxldhD7KiGP//d3kZRZdrs9PX7xPowqKhPEuWc/v3PuJX95cfouLpuXLy9q4BTQ2smyJA4ayCl8iC0vZZOCX2Xqgv+QVxZdk7h9Vzbty6cXP2i9Jqm6pCzAcrkp/d4LWsiB2iALP0/ETlIEPpQUXdA4XpcMAbQ5iXvId9rYLZ3Gh8JykuRk4y2AqjuDiRsQ1HYt9Bkqq6BowXpAM0JuU17aoPkEFSXEoQQOOR4Q10JFEPhAijtCXRxAQxJcguYVqBdcnbzKgvbly48/fXpJwPXLl19evMxpwVcv3JsOzEO8/C6dnYSD9ZlTRICwGoF/CnBfBQ1QNwdf+UEIPe8+TrZ+gv72t/TiNFH7w5evBfT8fH2Z/h374q5XVzptB9T0nMpxkyzpxleIyS7O2EJN0PVNcXcccG8RvT5WfudUVtA/pmcfH0Jeo6D7+PUFOKdxJoW/vvwAAT9+fWn66fp14lJ9/OE1K4EnPv7wnU/bu+fA6yZmQOvXb8/7J1tA+J00Ce9S/wG4PsLsBl9ffmPc9HnoPdkJVr68nsuk+PhgDEI5BIVTeMHHH/6MrRcHXpolbfc/4vvjg3EcOD6w6an4D5/uTv4Jmj0Neuf552IrENa/YgkgfxP3CXo66s943/3/T6wzUALtu8f/Jbt/tWD2D+jHP7Xtv1vwCQq/vnBBBoqtcdws+AL98k2VV+yPH/zvX3746VfA+t+yUcu+8e4cvuVOkYRB23379uOH9v71h59+/NBXINcCJ//WN9m/4vmv/HqX8zsPPqk+/n4tkK8VaVFeCug906Ffyur/NL++QrqTJf7379sv0G/rZfrMoMmIN6EPF/ymZlqg62/8+MPLrwAiCmDNAwMmhPiP/4DExGvKtgw7SPXKvoNAgLskDyblT3ECkKm913YTAL+2CXDskw7k/xThSeMyhH7+T+8OpAASH0A6fwfAb0/w+/Yd/L7dwe/nV+gEOJdNEiWABDoysvy1cKKg6CapVRMAKBzusNcFnwESfZ4uJqj8+d8z/3bn81qNP99hPnkg1JEVJnRq+yx4nSw04qB42uOBzhBcA68HIrLSA/qECUDWT8DytswArHeTN9o0yTLITxpgetmMd97AY18mZj///LML9PpaPOAUhR6to50Dgnd1oM+fgWFhlkRx97UIvLiEPvzy6wfov6D/btWd+SRDBsj+jAfQcKseJAjUV58DsqmJAPh1/Hs8fvn16V7ApgC9DkQvCZPgsRjkZxr4b75WN8xnBCcgNwA+Bv7Nq7LpAEZDSfcKCSH0ri8QOj2aUDwGPob8APQuPyi8qS05wJx3TxZlB7UgCdtw/AT1bXCX+rPbOHcVc1DoTvczJLIy6BllBn5Mat6JwOKySID73zPh8T1g0nxooeUbi1dImjISqpzGqeLGecoInUdcpp77XA6YO6CBXr4WU38MJlfdy+PhHkAEPOM9Q/p5ijlozTnAAr99k32ncabOdrp3uOZr0T5T32mmUHigFQChUZ/4U0P4+zOl2rjsM//uP6DpvXM/ouA/o3LPQebPZgPhn2eK934Ofe0ReIFB/7vmkbsx6/VxtWZOKw5aSaej9XDypNcUjMccBuaCuxL3gvo+K7whzRvgfi2yBGRMM/79QXkPzZPmAWJ9A3Q4Mkfoze7mzveetlMaNs2U8M7X4g3ZPwFH3WEM2AtqHNTAlHpvAqenb5rGwF3T/fcufw8zcB9IDJCaUNW7GUibEDjCdbwUaNVMpfcMDMjhYCrDS5x48e+sggB3kCqAPwSUSIDLAfrfXSeVwExQdWFT5t/Jk2l2eoQJaAum1uAVMkD1TBnUgpIFA9BEA7zw4c4KygPgY6Diu4fb2KkeykyD7lNBZ4pFmYOk/m0Eng+/5/tdl0l9wNXxnQ748jIhsB9cH5F91/MZK6BsPlXofdHvw/20FfptC/r71+Ku4zvog8LPpu79G+dAIJPz9o60E261AHvy4JlAIBPujfr10Wsfzfxdly9/mO4//rUNwL17ar+P3Bco7rqq/TKfPzreW8N7BagxBzmSVEH7vfl9flba5++V9vleab/j/HDUF+ivafc7Fs+0/gItXuFXeHq0T7xgytvnBziD/by0PmPT06/FMfge5WcqTKibjVNRv7WgNxLQh6ImiCbiR0tqp052Ac3zjsEgDl+L90x41gmA+CKa+mdb/qZ+770YxPURtvdWAR4VHZDtT9NbFExbm2xSvw1evhR9ln16KZw8+B9taaaGALIVuGPaCgG3g3GoS4L73ftoNN38fmt3rykABn75ZSqtT9A0xn6C3ifST9DbHuG+7yp6sEn6cZqGJ5GAFPx6p33fN7rBC9iWdWM1qf7Y+ExD2HM4/qMSU0UBje8QO7WtZ4lOEv/ABFxEUdD8kcnhfuFkT5xoO2dq2Un3Vt0t0NMHA9AnCAQPVB0oJICPPVjwRzFAThPUPeiN/mTud/99N6t82PLr3Q3dY/f4y8sbXjxj8JwUATkozM/t1B3nIFGBQHD/SCnw7P9hhnxyABgHJhjAAg0xAsEIDEXJAMdRFMV8D6FcH6HIBYV5qBNSCxcjFo4Lw74bOuCCJgmXCAnEWzg+Avg9UvPbNAQkk1YBHAYovUA8HyUQHMfoBYk4tO9gpOP4MEWRMBn6oA18X5oCgHya+jBt8uP7ODu55GnxLy8ugQHKDdYKzOPDzmndIc29K8Uu3RAh057ptLvudF8aWr0r2sXG8CROkvJiPSKzHFvHVioo6eJ4YhhHCxfBzpJhNWzT2YjPWKZSi41K9jdR6sVUjHjPlEbZoyie18wjsTul19AuLmrdUYnTVGplV+m1Q/aHka+a82jrkUnSs3m0IG8iTOj6rSD3fhjm2kCa13i99te82FVVWzvjYp+eGMzEe5St/J04IAO30w/6jkENiyKMSq/8NbEqGv7UUjoVhiKOxT0s7jBTaLWesEPdadkWBNg4HInDqYLn8g0ngoHDgWwc/Cbncu4MonZ1EnebD7vCVNuOcBZGuaB3lzPvUZmi0ReESmsiExvFDM9MbTs1gXI0uqrU6yoXhC28L47agaPw7cgrSNvonXUNFjbXSo7KcbJD8UIfO2khSjsdFtyDUZ/bVd01CwPflPBGlrQrP1AiphP71FYdi69yljAT+zxnKVXp7VbV21Tet6tztYwKSai1ZrnYbv0GMRD0nMoRotJbPxXZNLGMDDFFKd3HIfAT6WpOJ0nXNF94IrEs8j4+euPMmB8cQnEPqmbETZ4ezucZEnXx+rJ38ZozWiOUd46zhyvdkNI5qsddkLio5hhKanEUfasux4ozVxR+00LTk2tbJYNDOkNmRVEoYiqdDnOvBZueEN61fk+wiIdyqW9IDXXeLYaOv+gi1jWioNBxzy1TJ8BVM65R/TjEWBT4enkTl/Vtg4wF3vJ2ftMQQw7qRrOtek4eEh1jdTJJ4JRcexlXB8qF1EXraHfnZHMzyX6WN9LC1P1crrrMzzf5gjJspL0oK1dQ7c7NF/6pWOxP+9oppNrFI5sQ8RmKELRqYqstcZvN1/Rsia+Ham2XS24RIqwAzzIThan5ZcaV5kad0T5h2rLS2Q657XbXWrx0p1WDO467TkYrW6RW3uxVwb7QiUZydD0P5jdBH25eYopLgawqNfVj4MqB0YaMMOrc4xXDkJvNNkn1+TJZHhR3q2UCzB7jM32WEgY75sYojUKT76UdVde2URyzw2aFeoGYokwtn/f4oqja1aI4tSqJEakH+wl62iBCc4lVry7Eg0lT3GhWSYNJUebOGb51U21rI4f5LaRMI/IyU0vUsKGGnSgTeU2JejYTo6MoXfKDu+Y1uDocsUtrVxa6ZC0qkiqmpS+UL+n+oRj2orWJA+q0brKN6gLENffHXlGVYzYzR94YwiXFjuH2xiqYM25hScex4rQXzTGnK11eLBqFGJAUK3VaVRFePpenQGKNIGYyZ1jnKZ9YR/yo+W7HE7zsHlJjVu5DhZpVYDDB7VG4HUxpuw5n8Uq3F9TMGpxzMy62+2o10BYt8Kx6aM4qjBALUm60AGmP3LrI4jUVs0WPakq3yCTUsU7V6oao+spbpFhupOcEvzGS74+G580642ooRW46CbZG2tuGogNiZUsADReyfcDEDlxj8wUuGPC6NKXIrsV9XkSb62CZSwChVR4b3YGkL5vuMgs7dG4uU5mMQZZ57VH2Ct466dcuLUpZXXq2EGfznSKhgmY3iYly3qHF1r0VjUd84V6z1oqUFJcRHUAfck3aW3bqLcTFgVJX3MLjoOp286uWeTpyLiNuWAhCaLECmiylMLLHJVdF15BzLIU5qMp6u2MWsSOVNZrZyBUGyKmwS0fTfRW7wNa6rpFYWHq5XXDxJTqqEjWSF2Vb2xqHBPyMsmiagKNqlXfI5aY4M3PpoA6B0bZt1DF8zAMA8nJLH258fRNV1tplZxEULUqLuzYvZ3qn1y0CYi3FRysI4rC4ni6W4nfdjWRxRhOOVBpi9CmYFdw8Lgoa3V+XQTiDuWtCCIbbo7uO1CQ2YE7kKtlyaySgREGI0hw3xbrdKcuBQhfi/hTv3EuCLflGQpT+YgjXNq9qL6+4XDZX+irj1G5pzyuKC3fBemDQkJ1pShMratynLCYDnJIOHAHmj33SBrHqitzO8lUc4Sm6JVYmn8y1hMlKxQHdSCQwKmxcw7hVdbd2lcoceNItLV7dYIKwWkuRiIpVgu0O/lk+YKyzWPttfWmti4pU8lzeX1cI6L4isc9va7SsbmtJo5XtZquVUm3ssj3q9kN46iJfSI4V7dhYgV34Srj6h/XJQMpsyXOn9a2zKcMKyrkXI0tueeSsehQtsDGwaw7H+HWb+GqO1o7gK15nzk/sHs5Clq1XaeUh9fIsjPhqveZW6FIj5/zl5MYnlodLbZdmVw5erWXB5v04StPb4rw05jv3gGaCz+hESmUsyck6apxUSs8jfy8iuxZ0IkkKd0NuUEPTqVXJYiR8ZewgTdD2KDikfhb1gbWSDN1JXal6pEeLIYtw89xyTis5aRtjGGqE3q9Bx8zz2ugcEeEbZeFkgn2wEWlZLQlp7LvjuU7MXPY4FgdNqgd1AhOCGpzFk3vilUWAkdaeUZwb6+3UTZ1Lp1LeUSleZu3FRVYlD/fGdrnVdqv8kOxOrKKey/TqIGeyx2khyK+cwi226Ay50i0V4sfFQj0cExxzIrONvJ4Mi5Nin+tTXjs1mzf5qMlhaKIj0lFbY8lt1yMckSlzI/fdein6B/F2q2h3qPi0nw/8CfeLkm4XuFisSAdBnUEw7DJZrs4Cfxn6tuWOQ7Tn1WUL70133pUCZhytkASwoSfrNA7kNPOGG0xUxDW7caFlCGwK7tQm6xT8zF1BpxfAPH0ue04wvf1IGit+Rzs7dGcUHrXTynp1GEynscWhXOHMaq3Mk35mayuOONjevumUkh30oVmx2UjUSjzeWFpLF+1ySyXLk6Wn/mohTGOd6o76Qphbt4im5SBtUWY/4vheHegZnQqNifJJz464r216Qkgq9QDL11Wk+jNVOBr4eXXdaSmewkYfe/NAZtA6H5Ny7ajn1EcO42ZZBZpf+gNvpwqc7oo44zjaSXVpVWJk57nwFjF0ph0suM9tteM3pp5tjzXG0C2WD5JuHboMdbRFhOJWS8DLkr/W/qLReG7tk6Aem6rBKK+F0aaore2w2Nqc5t9muy6FcVMf+R25Imc6d+oMurtQ7T5cM+uZr6HiTdQSqdbKgmNgWon8SjifDoQ7gqvybKtpl1/r017Jbn7BbBQhC2hyuMBxKNaiK1t+QYBZ9XQ+J5q08pd+cTHa3kmjJb7raqaI2K69CAqnboUR5plUoln9ZIdGTQhWsrqN8VUlsuzgG2iVZ9V8frZ0LtWr24rcDd6Sqa+XhMFhX2pksSPBdLffrQLVB8PgSb05VpUwpD3Y85tKrYRFARNdk5UNvMNGEkT6hMOYdHSElClnu8yr9GN5YsT6mnO7zl0kF0OkBGyO05tUbKO9MXS3PYKzrUeGZiyUyo2J502RHa+zUR8MvOLnDbHtSDVUeF+kOHZfb27zNcfMbgOn1GgppKQSOtGZaVwaEG/X1irtpSRJCd8xrXKMtsvFmsGszTbaUQWzPCWXVs5afbd2hWup1TpmH0DFSo2wbthrxaBaAEb9WxG5wFqfthleHC+lqVnFePVDLobHeKmPwu4079fJ6Yjc2GChLXeBpmQI7e5odFihSkK7MtdmRBFqC10KtzuxZPOth9oEzHtz3Wt3MryJ5CTD2z3lHbL+GLABYaJznqSXvYxmhumiTu03sesguuyX3oZGZHpG9nvU2/DewTz4AFQtg257kUhKbcnm1cJNUMcbE9vn1abB8mSUL/Lh2JAa2e3zqgRWB72N1OiWulrwClRPnonaCTsnWEcZDeu1yl6TzGyF5DS1IevN7nDdRpbrcbPTYkFGJzrUMn/jJyd6FTaXci250dxC+JmNh7bT7M0LvM3pzPV9BYwNYaF4JKbiCYn6FgcHgebOEGI2xxhPq6nlDkPntDa/wWlXkSjo/QD4YJVwTHR1DPcYjzpCchDOlDlXSmdOlci+4ptmdil8BrdBj8118lqyy3PUsWIhiy4sYBG1Hfw1bPLivB4P5yIwRkd3Dz59Ez0WgR3N3ShwQNacbgyMxxVmQVUNmoG59CTU+Erf5usQ5uLwvKb69Z7Ro8FNxU0qU7d1T5BnUUgSetwbF3Vmmq6rU3GYurc9HJ9Va3eQ4d0qbBvSvYhrJTm6t9LNSqSWNo1sHodeL8NFimDFvNmggZjzPnxE4dUIMxriSYcBQw4xad8otMuF/gZ2++XSuq7cdu+MOSh1pOjw1qA1aZxhF7F1aYs82z0RXGfoyLoOSK+ljAYV3q3ZsBW67CpF0ilX/SNLlYN15oklujdBnq8U4XDbb0Z8jYpuGR8DNxuxJvUrBuwP7Bajaj6aqUR09tFhc4yKNpjhBWsGvn2lMe6qtFv3qCKCZ3bqeYNXJH0jaUnAzzS2qRW27OBggV5ci2oPCSPyh+XR2tXDSV5i5eqQIOvSkFGSPRo1qPfjTE5NWMvW/pVDcDdrLLOf9Qiz9ysJPyABzW/EW0kZyQY/dQ6u0HQt3mLJ68/z5SBdXRI7NU7nFdKtqa4FGSlYfPU51cUcFBE3ykyUzFMUXw/uxdtmvlTT+d5H+UE2LBqlma26X7b9oe8dzPS5JkN9nUxvJ9RHO6PbsNphlo/t/njViKjDxM3lfGG0zfGALoxIp00/Oa6WmTC/nuDaOBKIgs3kY3DdZujiJBNbhLfpbR9fhxUD78jgggCnUh2CoryMzEzap2TUTftB5ItoHl9u88DkzoZMiMY+DPhkTx6R4SKdSXhWej6q7G2azmf7vo1Jh89Dk6T5+cxAxIA9DwZ5lppaH8wzGwg9JWhXRgp2tUisSW4uexcudXU538G+uPDxhXkJPXQmcYq03B7YhRTyZyB8h53LhbjrrsRqf7PlJM9nkoR1ND2j+jlxXrLjVus8igvim0MpK3i9hLOE6RYne8TBGj9XmoVUcXttPScRbXBlpaENtlzHrHbpY3pXEP7BYmab82W2c5CBnc0U344IZqm3scwvSpa6xTcrqcMdF4DZQyTE6zI3TpGCaGQuq1G1CcaslIreAjm6kzeosciX8xu9gwlmnAFDAnyvhWIsNRm8UeeIZeDX7mJ08y3RzQX1LJwSIxuNWL32V3Jl6yG9inR5nsfeSOKINbtsr7NDyHjltvX2p4pUrPxYCa3CFC5RxRwF9huabW+xik4H7TrSJO7mBwbbogYJjzvToIJo3nUHLrHaimGYf7x8eplOnp/nx3/hxfF0nvf/7VjxcQL49i7pfnQcOP6Xu6wvf0Wpnz69NF4CVHocn7ZZHz2PGv/p8PTzv38HMa0fH+9jp9de1+7tsL1zoulPil6Swu/brhm/tWXW3w9wP724fTv9dUP77XlQ/XI3LK/up95vIp+H4t+68mlK8DL97cH0JifwE6d7u42ex8lg6QgilHjtN5TAvwVNNRn6fKcB7ENe4dfFy6//FzqzRNPKJQAA -->
