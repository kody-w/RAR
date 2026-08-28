---
name: "rar-cowork-cookbook-report-sell-an-asset"
description: "Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_an_asset", "rar_sha256": "174c5ecbf4f2df823b105010d5641147d4815e552d5e98d069d22f0776fce6d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_sell_an_asset`. The original RAPP
agent is preserved byte-for-byte in `report_sell_an_asset_agent.py` and in the RCI capsule.

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

Sell an asset Summary Report — Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 174c5ecbf4f2df82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_an_asset_agent.py` first:

```bash
python3 report_sell_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_sell_an_asset_agent.py   # or on stdin
python3 report_sell_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell an asset Summary Report — Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_sell_an_asset',
    "version": '2.0.0',
    "display_name": 'Sell an asset Summary Report',
    "description": 'Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-sell-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-sell-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0009834f5e59b884',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/sell-an-asset'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-sell-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportSellAnAsset(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSellAnAsset'
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
    print(ReportSellAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6a7OjRpPmX9Ge+WB71N3ijug3JmIFAgnETSCBhNvR5n6/gxB4/N+3kNSn7Rn73XkjdtXntISoysp8MvPJrOL89mb3XVQ2b5/fdN8uFjs7y+LIbxZ24S2YciibFLyVqQN+F25ZdE3s9F3ZtG8f3jy/dZu46uKyANPpPs68dmEv2q7p3a5vfG/R9nluN+Oi8auy6RZlsGj9LAOyF3bb+t3Cdrv4FnfjYoi7aNGVnZ21HxZd4xceeJ9VcBrfTr1yKNpPYEX/budV5rdvn3/+5cNbDD6/ff7tzc2ANKCB9lhFBytsis0sH8zI7CIEt6oRGFmA68pvgrLJwVeeHyxeVz8CrYIPi3//93Swm7D96fOXYvF6fXmb/2l9segiH2hotx2wy7Ur24kzoPmnxSYb7LEFJgKTi5f9cRF+es78LqmsFv8x3/vxucin0O9+/PJWAhXsGcEvbz8tygas1/Tz50+zlOrHnz5l5eA3P/70XU7bO4nvdrMwoPWnr6/rl1gw8PvQOHis+h9A6tNXjv/l7Q/Gza+n3rOdYObbp6SMix+fgqumvPmFXbj+jz/9nVg38t00i9vufyT356fgyLc9YNNL8Z8+PED+ZbF8GfQu8++XrYBb/xVLwPBvy31YvID6O9kP/P+L6Cwu/PYd8b8U91cTlv+x+PlvbftnEz4sgi9vWz+LbyA6nMz/vPjtq66yzM8/eN+//OGX34Ho/6sYvewb9yHha24XceC33devP//QPr7+4Zeff+grEGu+nX/tm+yvZP4Vro91/oTga9SPf54L1j8XaQHyd/Ee6Yvfyup/Nb9/Whh2Fnvfv28/L/6YL/NruZiN+LboE4I/5EwLdP0Djj+9/Q5IoXjyz3wbZPm//dtCit2mbMugW+hu2XcL4OAuzv1Z+VMUtwvwM+d24wNc2xgA+xoH4n/28KwxIK5f/7f7YMOP7osNV09S+zoz2le7+PpgtF8/LU5AVtnEYVzY2ULbqOqXwg79opvXqRq/9ZsbYBBn7PyPgHs+zh8WcbH49a/EfX3M/FSNvz7IMH6ykMbwMwO1feZ/mq0wI7946ewCavXvvtsDoVnpAg2CGPDlB2BdW2Y3wGCzxW0aAxb24gaYVwJ6nmUDVD7Pwn799VfHbqMvxZMy0cWT49sVGPCuzuLjR2BKkMVh1H0pfDcqFz/89vsPi/9c/LNZD+HzGiow7oU50FDQFXkBcqjPwTDgDuBAQBAPzH/7/QUoEFOAogQ8FAex/5wMYjD1vW/o6vvNRwQnFo4PUAWI5jOagIcXcfdpwQeLd31fxWhm6qhsu4XnV6Dc+IU7Aqk2MOcdyaLsFi0ItDYYPyz61n+s+qvT2A8Vc5DMdvfrQmJUUBfKDPw3q/kYBCaXRQzgf/f983sgpPmhXdDfRHxayHPULSq7sauosV9rBPbTL6AefJsOhNuLwh++FHPV82eoHinwhAcMAsi4L5d+nH0OijWovaCOflv7Mcaeq9fpUcWaL0X7Cm+7mV3hAroHi4Z97M2k/49XSLVR2WfeAz+g6Szp5QXv5ZVHDOp/quv6q+4/K/LiS49AMLb4/94hzIpsdjuN3W1O7HbByift+gRo7lxmIJ/NziwPRMkzGb7X8m9M8I0QvxRZDLzdjP94jnzA+hrzBxO0jfaQD3wKAJrlPkJuDqGmmYPV/lJ8Y16g8uJBMwB1kJ8gfuew+bbgfPebphFIwvn6exV+uKjxZqNBWC2q3smAywPf9xzbTYFWzZw2L6xB/PkzmkMUu9GfrFoA6QBwIH8BlIhBIgDsHtDJJTATZEzQlPn34fHc2wAtvN4F2oLW0P+0MEHkz95vQbqBBmUeA1D44SFqkfsAY6DiO8JtZFdPZeZu8qWg/fLFH/F/3foeqQ9NZuWBTNuzO4DkMLOl59+ffn3X8uUpoGo+59Zj0p+d/bJ08ccC8Y8vxUPDd4IGKZvNtfUP0CxAquTtI9RmxmkBa+T+K3xAHDzK6KdnJXyW2nddPv+3BvrHf63HftS285/99nkRdV3Vfl6tnvXoWzn6BPIdlCQ3rvz2VZo+zqn00S4+PlLpT7Ke0Hxe/Gv6/EnEK4w/L+BP0CdoviXGrj/H6esFzGc+0teP2Hz3S6H53/0Kli9zwF8z3COohe/l4tsQUDPCxg/nwc/y0c5VZwCF7sGXAPkvxbvvX3kB6LgI51rXln/I10fdBJ58Ouqd1sGtogNre3M3Ffrz5iKb1W/9t89Fn2Uf3go79/9mUzHTNYhIAMC8/QC5ARqSLvYfV3bvxTMK8+c/b5CUxwc7m9OnnEvfzM3v5PjQ2GuAOnO+hfHM0B8WQMsQ8N5sxDDn3FzfHX/mRlAtvVnrbqxmNZ+bjrkBeu+O/rsGj7QFfOOVn+fs/bCYO9kPi/em9MPi2zbhsdkqerBP+nluiGebwVDw9j72ff/n+G+//IUar/7475V4UcqTxG1nLjWziX9hE5DW+HUPaps36/PdwO/rls/Ffn/o2T13eL+9fWONl5de3RwYDtLzYztXtxUIXrAguH6GGbj3P+rzXnMAs4GeA0yCSczFfdcJsADxgjWCOjCEQzDk4QQGwxjpYWsY93Ec8XCfWnsQQXkIEkAkSQSuT3gEkPcM0K9z2Y5nPRDbdtcuCWMeRdqE66OQg7o+jMAeifoQTqHBeu1jAJL3qSkgxpdxT2Nm5N5bzkdwPm387c0hMDByj7X85vliVpRhkxfRkSOHaohg4xYr3onRw8mqlBq5I0RTKXIid3mzm5Blju1inD1GQh3nGx5qHBPD06UmLIcTKRaXkgnSCka8VZ3sHH9k/G2MFcCGkSj5TbTjxkqO3JHtONvAatF2dvqd891ahs5VcENxbsUZlQea/ThrTUO7m9q5Zj1LPVAD1N51RICcXeWQJm44LrHnOz1TDzBNCG1GW2G6tART0A773MiFmxTVqjba3QVH/NupI7xARxW0GcjVyJ5JyjrcmWtjHK3IcFKEPmdOnh7ONgJz4l7BISalBnidCZmLw5w8SlADlyVdTxTKVmfcUG0zWa0KQbn2FyWTuJgysgNHXFhuOJv9DioxVKI40WL7+mDDxtU5HbT8Fh5q6HZyWD/pLLyxvQDyYOJq4xdB5OzhhIyHaIOth5tcp351FQXjwCWHZZgSx1RkZAmXQOcvymYbNGiRsoKkHlMGCUOGvLuWSlu7tTRVfncX+SFHr+MprC8cY1fXPsaN8ny4B15jXut4rO/XWj65ED24wXpk7qxDd21eSvbdG6l7dS3LxkhhYol63amlLkxtnwTHirhzVDCCIojKpaQTR2WLS7OSoxKHoS13cofbXj6gZLEMuKQrNmaCLN0ETsd+lJx2OekGQ8Zwd3VLw9nd95xfTTXRmkIvrzuWueF9HdNGK7RHbkWVpRQpRRRShN1Oxua2FMKh5/g9wYknvb3fD/vzOvEiAz9XetHy5mnZLpdVbsQXy8QLCCkkBlFWYjnJVllhkJiPZ9xFWai2Y3fIi63mnV2sllZ7slOyw5phSRZfsnfwozWk1tqHI6VSAyWrgjFRktpeQoIbYbQ9mVYsiyfT8ePWMBExOfpmXlCWxjeZzZndPo0FOB7uo3Brr4Mcm2Jyr9XlKlbhSXAOpr6ULQSqFOW4weEVJrutRJjDTqoOjgCXMXejnYE72pHGeWdhl17CiEwtKJa2O3ut6RIt03wgr4e+klxfDEceLtxaGpQbqS9NsJdaSyTP8HttexCRDZfc1rGTdFeK91VjusvdGtb6Em7K6zqxGm6vBBzp7zEioxysD4XRvI0+S9zM7MLl7S0akmQE7IIhra63xP0W8QntG/SFtncDV1+LSZdWIzGeb0QTbEx2J1k3goJKW9S13XF9vZ8pWMuzGiqhY50sfezCr9vDSTyO7fXeUiv/blV8tVZVl7hb8UpqTfPUGRa0TNa36sCesl3FWWs36DSxsQTixjFtcoXPXgoX+eQux5wThY2/KXBsf4H54aQFOtFFnK8wxSoz146zoTh1hQz8cuKdRAxGpWZ9g7ukDB5k+9EPGLcdjncSMzqe71xEh8+a1R+QHTser9u9cd90YHuYinHMMmqrFwdMCjR8YFIOz+5uTwsldA9kVLNNBUlYVKV4SKbJ9F5E6CVC7yHAWCKl+lw1GLPREI66ILF5txsz8dRscvvldruchl136TivE5cpRNprQj8PskTsKH3oTXddp3IPL3nBjmVXZzAbJiXaQ0op9f3WbqWE3ZhFtTw0++GIYFcdZPThvvbRxhu5U0bWG7faeTkzeVNEGxva3K43tnXYOnykrjfmsj5MOyElPN6NCD08jiezNG3n2JVnA3IloisVutvxfBSOnB3roxOwR2GMIrdb6Ux6LLNcP4R8AlmDsY06dC/aTLpr6KThN7Vw2VfLrJrw/UkDUs9T01DC7VIh3k1s8ToQWdui0KUDC4IWZ7eTeUWUu4jQNO/5WaNu0eV4PBRkkqskz240t7ivV9KlOE0UwE5Vb1m0Xt3yQs2267KmaYPDcRMV+A0vhxpUmbYq6cxhzTOBMda+VItOkCA63lbRAW43BMZwlXY7Vct1V6RLuUjHk2K3dnZwc5wVljE/WVyb18HlvG1pmMV4O0IUltD20WmX7Q1JWDPh8uAiqXbjcGs8GHEY5KcALe7M3cO6rFKHVUGyxKEgoh212rUmtF9fxUJWQNXgOyV1dFKUj2iHXOAVkStdZOzb7Iyfzrd7v5ekwErUPI23O0X1mQmVkR1xO+8dE0GUi2du+cbyb3RDs4MKcfTBKYZUsNXdKlnq2yE+VrJPAsoarWgb11QvWcFmlESN05BcvDSo56YxE5L+ueQVZzku0fpwLrksdP1DJuYDHmvcNUn7VQPrd+F0xDa1c9bMTivPLOO6bYkRiN0HB664d0xsnHCoDPRyLA68m/jhPmTVzagIMCEanGXdVGdk5euO0y+Xg5sEmpFmSBlVk7HLsZjfwaG2vyXqWHiTjNQ6FJ2P4zWUbvG5hV1vh7RwW5qa6JltyARHGkeFpeWX0nXZdYKjlTpHUJRqou1dm0oTgk+Tw59ddpfUsKIhUkHZW52B6PxmuSfoJkZb/nryJREl44jwIEHRjsWUVUFookZdQ9KSkqWt3BL8Zm16whTtuzBLt0qZ2XGc6PnxaqkpjYlLNsyUOKHro4qQBZQQNitvVCk/4Qh976CA4hDXVjQGJ/XNrgjXzZXeqxo81Toy3pSznwcjpAYrZV8UJrrdxUftzC1FhBKI5eksD9S+UUuI2PZeFBOWdxG6THFqp727SWXsE4cs9HATQeU1PJ6JFHXqoWNMItxcr1Kea51d4/ppCLBjfM3v282537Pni7OmlNpPr+MgrJvNNbmTbGVaeapo2zTGurPdk9xBh72m2oaCbV7G3TkajGmSddcwKAUO62uKD5PFQFJ9D/176uRZj9kj12YTmukObcUHjI9yqDpjabYxaPe8mnQ2q0Qo5rxjV9CH7X672V6l3RnS98kuEjJQQHCoyJWB8NQCFo2znsGXRBdPRcZ0nOPIjiUwTQbtCmk/IF5yt0OZdaOTLK8OS5g3YGhoLrzPYMZV89fGIc8mgxYwyYB1a5gQS9YteaPvXbbYXLqAhunBcRWFMY+b/rYKQtJphFSPXD+qeLz0Uau9j7tS6tPUlTJDG+i64Y3ieKplL4Z4sY94Q1X2pGWvNlqR7uOldmWnQJ6w64jwjLyvU2HjwccaOSac3zP1TlJEc1RKg9ure0003WUg7CKMrXutw2pzTblSw8pIA1kYz+jiEeIY9wywk9culp/C+3TzBBRGaUF1XG+sdLLJDqiyPQbEVXTxGudYuatYYhr26L3gLNaSFUmMnCML0ddS72lM6nqCGK8cE+0OMNSO5BGlD3q/KcMpHm1IskvYlDzZ2NXiydkXCblsBmJzgk6HyL8zPcu1uKJv+G0brMpzG8a9gCIXVGKx21Zkio7cUjbLyTqfKYYT1fZKKN0ozfa4w51b69JDeJ3AtEyGHVM1Wx3Rd8uxcnbk6rJjLt6uZG2Tp2Lf4jnjuFaZdaFMhpWUbOyuBru8Ikh68YTzKfP4Yl96oHhf9BvkYTlNIoSmnki5Us7ixnTzSkJsB/Q0Z8Cl2Fa0NWRg2Xp5RcTrHVqfekRk93xSKOVOqq8H0u7lVuy7FBvPBC/eEYhy3UsGDL3RtxIzuNM+m6IQsmR0ykuW4QJcGcEGAiZg0MRjdxi+18p+7CyvIRJDnpZyd1CXa2XTV2hPenIaFBvqQuU4RIcteV3L8JZrD+NOJp1LOZ0ykxMbXlKmDYZUEE0N7KijnggdlVWPcgU+rQ9bpR9xoowx0FNjQQfVNDtJJ4UIEiJeSsFqh2xWbGK2LRobhnULjCFBDvKRoUq1VjdJ6I8nn1ztmBtkHJYHu5Tc7RG1EINCUN6ooqVLJ8ixozhrWrpbyPehG0mM6xW2OXuCSzQ42a5X9/O6gBz4pHI7qk935PXUCqfVdNNzpKJpiA1ijFdXTVoI2QpTy9MqRM/KgO1w1bKryKRp645gvL7P99gmvXpn9SqGEqOt8NDf30yDIAxH8UATdaB1ZeIRhQ4pkhGtfFSdYl1VaLaTJKG9uAyTT1uVMHeX/T5ShXEjO9MSrxgBXavRre1DtNT4VbDeR3tlXBIkc0ud6Oq2ic0ykX/klt2dAh2yoxyYcbgMiEx7sr/iGHlL2p02dQ0pH1bOfum6Lm+dyUsX+sOW1TX1khDBZYN1AuKgE3s6nm+BjfaSZuqc45oWEiS2j+ZLGz6iDWrT2RTUeymQSQFsKAL+3oVpObArj8jSgbsvxRE5h3caVu4sERtI5d/3EzSoB9SzW25zueXt9k7tsZIsK9hvYlspLwdzGyaAZG+baDhMZ4hxlgdtugoji1ISpk93qODQEOVUPWs50NDBPsy3Qb1UEwFaMdJeX7FceZNVNXSiTkiIM0+F8aQck+HcuqqQhRi0Y5db+mLe8O7oBazVRsfVauKx2M4FHPepJry1SwXXJ8nwSAVyPViUpuOUrxH8KOegQkaRxoIdxzKdtpdVonog1mExEC7myuvZrmP2rNKE7kmVCw5R9mCDIO1XhVNLcIxtWdIx1oVLSWs7Ic+yXB1Fum0VpCBg06Ora9DWHWFVIrkiDFB4iWyCJfruUeGB2nnDCU/OG9oPIAfg1TnXQgu1o1peVzsL8mSWV7aQG+gC2OORSA42pGrTQYqHhSBMHNIKr3sULsxgTCkbt+ALsVn3Nb7cjNBu7bM39WKb2+SsEluIu+GrcEfsl97kYJO/zjXK42Dk5O7FQiyVwGVuF2p/GwP0vuYjUJZCqsPEC3wJmSSUTelQhpxan7imqdS1PASI1p37a6JBk4fs8YCmDgEGyRuITTHxDK9NVe3KKlYSn1WyNkMhNIyDKvHutnN3VnHV9RORVDVkXgPB3XvbGMIGNVyNUMZw8nTER3wgWC+3m8Y5Qz2BNs5kkDYJiLTV0XMobs+JQu4nxa9YKqExV6GwqrbXDIcv8XR75dkmOrji6bq3bvdMy7xlKeOKvbFQ64BL0u1AtfDoeIdlRsONiIo8NRS7y+BdbjSyEVYUddWwrbAyeJHctVQbs1B/cYPpYsWOiuB01i3vmUUN0ua0J5ky8XZpbHSjtWLWICHNlXWoT1STe9sTU5gDtqaRsKBXqnnJ6LhSsjHiGe/Wp0xAsZGnWRyaF+vV9bBFr709kLSCnR2IwT0pItTVJiTO62SqhGGzefvwNp8Fv050/+mD1vk07f/Zod7z/O3b85vHWapve58fa33+52r88uGtceNZiccBZZv14eto778cT378q7P+ecb4fEY5P066d98OtTs7nP945i0uvL7tmvFrW2b941D0w5vTt/NT/Xb+ww8XvL89lM+rx2HnYxHwwXYfB7Ffu/KrF7dV2fpv8zP3+RmJ78V29+0yfB3RfnjzRoB77LZfUQL/6jfVbNrr2cF8yjk/PHj7/f8ALtbFP4ckAAA= -->
