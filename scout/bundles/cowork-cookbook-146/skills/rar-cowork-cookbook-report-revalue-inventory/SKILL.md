---
name: "rar-cowork-cookbook-report-revalue-inventory"
description: "Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_revalue_inventory", "rar_sha256": "bfd85c13650630977616794fd974030ba01f250c9fd5b2873079108ebb527d9c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_revalue_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_revalue_inventory_agent.py` and in the RCI capsule.

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

Revalue inventory Summary Report — Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-revalue-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 bfd85c1365063097…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_revalue_inventory_agent.py` first:

```bash
python3 report_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_revalue_inventory_agent.py   # or on stdin
python3 report_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Summary Report — Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_revalue_inventory',
    "version": '2.0.1',
    "display_name": 'Revalue inventory Summary Report',
    "description": 'Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e070fe8201d890ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportRevalueInventory(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRevalueInventory'
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
    print(ReportRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+ZOjSJLuv8Lm/lDVS1YKIXHV2Jg9dCDQwSFAILraqrlB3PfRr//3F0iqrOqd7pkds7WnOlJAhIf75+6fewT524vZ1EFWvnx+kV0zhXZmHIeBW0Jm6kDrrMvKCPzIIgv8g+wsrcvQauqsrF5eXxy3ssswr8MsBdNXTRg7FWRCVV02dt2UrgNVTZKY5QCVbp6VNZR54Ftrxo0LhWnrpkDOAJl2HbZhPUBdWAdQndVmXL1CdemmDvg5qWGVrhk5WZdWb2BVtzeTPHarl88///L6EoLvL59/e7FjswK3Xs73lc6PVbhvi4BpsZn64Hk+AGtTcJ27pZeVCbjluB70vPpYubH3Cv3Xf0WdWfrVT5+/pNDz8+Vl+nNuUqgOXKCmWdXAQNvMTSuMgfpvEB135lABC4Ht6ROIMPXfHjO/S8py6O/Ts4+PRd58t/745SUDKpgTlF9efoKyEqxXNtP3t0lK/vGntzjr3PLjT9/lVI11c+16Ega0fvv6vH6KBQO/Dw29+6p/B1IfTrPcLy8/GDd9HnpPdoKZL2+3LEw/PgTnZQZwNFPb/fjTX4m1A9eO4rCq/0dyf34IDlzTATY9Ff/p9Q7yLxD8NOhd5l8vmwO3/juWgOHflnuFnkD9lew7/v9NdBymbvWO+J+K+7MJ8N+hn//Stn824RXyvrxs3DhsQXRYsfsZ+u2rLG7XP39wvt/88MvvQPS/FCNnTWnfJXxNzDT03Kr++vXnD9X99odffv7Q5CDWXDP52pTxn8n8M1zv6/wBweeoj3+cC9ZX0ygFSQy9Rzr0W5b/R/n7G3Qx49D5fr/6DP2YL9MHhiYjvi36gOCHnKmArj/g+NPL74AZ0gcRTY9Blv/nf0Kn0C6zKvNqSLazpoaAg+swcSfllSCsIPB3ym1AUW5ZhQDY5zgQ/5OHJ40Bg/36f+w7LX6yn7Q4e7Db1ye1fX2ntl/fIAXIy8rQD1Mzhs60KH5JTR88ndbKS7dyyxawiDXU7ifAP5+mL4AaoV//SuTX++y3fPj1zozhg43Oa25ioqqJ3bfJGi1w06fuNuB0t3ftBgiOMxto4YWAPF+BlVUWt4DJJsurKIxjyAlLYOadk4FsgM7nSdivv/5qmVXwJX1Q5wJ6kH41AwPe1YE+fQLmeHHoB/WX1LWDDPrw2+8foP8L/bNZd+HTGiIg7yf2QMO9LPAQyKUmAcOAW4AjAVHcsf/t9yeoQEwKqhTwVOiF7mMyiMXIdb4hLLP0JxTDIcsFyAJUkwlRwMdQWL9BnAe96/usThNjB1lVQ46bg9rjpvYApJrAnHck06yGKhBwlTe8Qk3l3lf91SrNu4oJSGqz/hU6rUVQH7IY/DepeR8EJmdpCOB/9//jPhBSfqig1TcRbxA/RR+Um6WZB6X5XMMzH34BdeHbdCDchFK3+5JOJdCdoLqnwgMeMAggYz9d+mnyOajeoBiDovpt7fsYc6piyr2alV/S6hnmZjm5wga0Dxb1m9CZyP9vz5CqgqyJnTt+QNNJ0tMLztMr9xg8/0Ohl5/NwKNEQ18aFJkvof8vbcOkEL3bnbc7WtluoC2vnK8PoKaWZgL00QVN8kC0PJLie23/xgzfCPJLGofA6+Xwt8fIO7zPMT+YcabPd/nAtwCoSe499KZQKsspaM0v6TcmBipDd9oB6IM8BXE8hc+3Baen3zQNQDJO19+r8t1VpTMZDcILyhsrBq73XNexTDsCWpVT+jzxBnHoToh2QWgHf7AKAtIBsEA+BJQIQUIA7O7Q8RkwE2SOV2bJ9+Hh1OsALZzGBtqCntF9gzSQAVMUVCDtQMMyjQEofLiLghIXYAxUfEe4Csz8oczUZj4VNJ+++BH/56PvEXvXZFIeyDQdswZIdlN0OG7/8Ou7lk9PAVWTKcfuk/7o7Kel0I8F429f0ruG72QNUjeeau0P0EAgZZLqHmoT81SAPRL3GT4gDu5l9e1RGR+l912Xz//QWX/895rve61T/+i3z1BQ13n1eTZ71Kdv5ekN5D0oUXaYu9WzVH16ptOn93T6g7wHPJ+hf0+nP4h4hvJnaP6GvCHTo2Nou1OsPj8AgvWn1fXTcno6scV334LlswRw2QT5AGrje+n4NgTUD790/Wnwo5RUUwXqQNG7cydA/0v67v9nbgBqTv2p7lXZDzl7r6HAmw9nvVM8eJTWYG1n6rB8d9p1xJP6lfvyOW3i+PUlNRP3n+02Jv4GoQlQmDYnIElAp1KH7v3KbJxwgmL6/sctlHD/YsZTHmVTLZzI+p0p72o7JdBpSjw/nCj7FQKq+oAAJ0u6Kfmmgm8ByypAoq4zqV4P+aTrYzcydUbvbdM/anDPX0A8TvZ5SuNXaGpxX6H3bvUV+rZ/uG/F0gZsoH6eOuXJZjAU/Hgf+75DtNyXX/5EjWfj/NdKPLnlweamNdWeycQ/sQlIK92iAcXOmfT5buD3dbPHYr/f9awfW7/fXr7Rx9NLzzYPDAd5+qmayt0MRDBYEFw/Yg08+x83gM95gOZAIwImWp5DYvZ8gWMIvkAogsDnOEEtPYcilsgCsUxk7qEYYlOeg1koSSwQgpojpGtZGEo4lA3kPSL161TLw0kXF/HcBTVHbWeBoxi2pOYEalKOuSRM00FIkkAIzwGV4PvUCLDk08CHQRN6773oPUAfdv72YuFLMJJdVhz9+Kxn1MUk9KPFBxZV4h5tpxRnhfpBtiynLI9u4Z5wU7NMfsWnNcX3vNxvpWBfhInEIUdLW2IRfN7DnUIcUz2jvayRo4WxaJQN3xzPIt3bOiWIjq1ut9KGxzMTizW5uVVaoqJHwgszwHB7Fp+p6sXVWvaojPDRwC7CdhCi09GsrnFzOQTsThlap2aHvbKYn0+lhWt1Uzc8gx61vjG0ctfl10KerSwji6/xNnf3Xswb1XG1FBUmHL30CGBLUzIYY5jyPN458HgTX2/juD240f7iYMNlr8Gg5djV9XndHRuHzkWb95hcKOkwK5pzErkxs25Np1nGh7TICVmwBQsZ7Upv8lMs9xo6X5P1amXHcRn0nMCP4lneSfW8t9TiZi/HyLV65mJZLZ8I56Si5tShwl04HHdbNrHVQ5yl46nYbjazNakVEs5ETRxl2qnEaWW/PlfYMIoMkw5GsbhRNoat1som29N1xq1RmNWUTpNbO+9abRnHiTYzB8XPF8wxkc+XzUioxUUOYV2tyiHMxmvByjPOSpZisGFCCV2XBr/K5sF4yTQlF8h2d7zkR2c2hy3EO1x8IUn6jVnTQiRclYN88fvmEKiKI9xIFE1TXTqp/EaA7aqpbW/EK6fC14i9UGitSi7o+UalqDn4uo3W+UZjLs3m5FyK8lRylIWd2zjzndlYZN3FWlvblU5VzD7ZV1gnurmVXrqW3CNXXU6scGVZUrXCjsSWDBzMwVWZlcYzE81SUVdHoa/La1fBEYJlWq/33g7WzIPLr5lTLOhCL3jC/pTYFiCZ3SVZlk4+3+t+t7gmbKazS4XZtfWhz8oNMltsyIpMRmIwZp286TJRzepquUCSbKAu16qujttcxqvEMRSujM1Yy5lo4NEbHR33YmV2VKiWGyxrBWzkGOJoHTRpJlttvr46ATZmHq14Rhw3gc1IRsnMs5BpVg7JSId+xfCX/U7VwzPf8fhqvQodl8tROvFjTuuvyiVxj9vOCXljcbidNiW5EOObemu3wsAOSuab+26kpISEtba6rtJeFREYOVwO2E0rVyxylI18PhitNMyG2VVrZrWfJehMWwSXA7ywE62D0wPXHnCf3FwH91Ke1atxO116dRWtCoVWstDbWWnD3nKAU+GdtWxLquuc5bOZaYxhgF1M7qyIuncg5SuDzaurdnUS+LbPMWpbhMPOxqnzTYxKlBOFOZMqpjg0UXa+RI52GLt5ixcXTVbmbpG6l2Ou7S+swe+xaqGHuS+b0n7waWoz4mm1z5qc3/XhTKeVGTq6POJ7cgCTO9WXb8p6IeI0vDXJGFH3mG4c4xPM5VjXhuyytWjewE5Bg8qllZ8kIeritWjha/MQK/sFv5LUM5cIK4RvJaOzoy12QXcNvcq2gSUuMPOyK52bleKRqd2uA3YMZmWHE2nd2+gquZhXhFRQGmXmKjrYg2lpoSPBAXZiGJYiSgleEequY1ergGkwXvZj8WYx2w1+ZfuCxinPrtJiH3R7Ky60E7mjD1nQdUWOEvTxfBKNRL+hqU0n6dHo03R98sTFYNnhNg/xUmfBdsAwGmPpN922EU60xxw2Hhey5MZwM3zUDpFjJ4I0P3acfCyjDc+72vxQFqcjYGm2RIPt9nyLGSlQ9WTYx2NwWy/tdcRw4eV4ii7SeZ/dojLdWJWwQxjO0dapptLq0IhqLYys5ggMmsAJvwdhBlPipp45OuNmy/GMnbyZEpb7SuTQcXbk00zadCCB09oau57kEaGAl1TgnA40p9rOTLzgxdgvPRHJYJhq+pJluWOXmbqgXWrM2NCxvxXmR1nK27RjYyY8hLrcz/XCQQRj1naJmqv9WPpcEjBzt12SpqssETK5jXCwM9pDlJ5uQsSwFreLkHGggrrbc6yzjoRWSjmaOrSinYTbC+074RarRXFviQIlZPpqAJVBFWkOELO8UEJ5HhuFfHNrkUr3A1FlzDVMyi1LYjh/VXeEZfnlLj0qubgOrHNZo4YYL12aPlS8spMbZ1/KkovvTtagWEvDPpwk6RLfOtjG2ium4RnloQ3RWU0jdEeNjdacw6u7axUPokzOFkkbwEdqeZNy3iWo7WnA8k1ozolToGwHm62ZAI2PS33uDFyY+BTQSDB5wTnPNDoyV/k1TZtWRrfJ6cTyJDxH4yGcB13vcyrmDuermqwrqclm3cJszMMuxZr1hpcxqQrX+SFJONu3u9OwbelOOKyWh8veMDzWHBBBwnB/DFRstQmpKnYDW9m17gmE1cmg053YNoPuEDxckbmMRGpwstxtbHdcUtb1wpOi+MjvukCeSQeMZWZGk3nXJmj35SWXmYGkYg2tzt6YFeRcsVH9UtHMzcSEs8tV1FJc0dt92u6tHpmJyabcSm4lIEQfUUKhpvRSXx6KcbkL5k5Rb0bRhldZ44AdgUnvlZit6TrZSFJshlEYMRlf3brhEC/WkgyqeGcON6rAKA5Ogo20Gfc5TEgkqrEz2UmLjS9VbtLxi6V4QGV3nHsVHuVhcYjFvCTr9ULHcJjSEHyJXNdrv+9Xs1xZkFkgsBaOLHbp+jKvKk8Zi3E0lARPiJPO4ZczjsLYvJD2ziHhtr2QX1CSPHYxntG7HXXOC0svBDUiWXi7jdxrnx50JeSOMe6lc0Y55VKsATvOS2yhEtzg6II/7G2rcBS7nPNmE3dBp9aH45zl1OwoMkktHAq8NrsLL9tLrArc3YXrxGt4Okoz+1wH1t6eY5ekuyxDeM0ZYaEJ0yKyzogkEuxNGeMCXT0anewPWceim1XMb4Nln8mGmew3FI/dqlOqYJi0uXC5o12REMEwOTnryaihslpgziofDZJPr6QGFAd6jUo2tLUcO87pFI+63zDaVhcZuTGZIomoC3YqbMJPK9KMDvJ6u+v0pgysg69sTw3L0sfrVtPbNuCpnhwMqTnr+wOWyahBUsOO228j5CrEcwlbxef4MGb7+a7pTJVBJVxI0g11qj3/PIab3uNPa2MWLknbMbdrNJzL20DAM8nidLllV/PNjt0SxvF8GG7JLUsLwa3UixnIDcemcH3d5EhPkogx24fh6szsN7aaBWtHlQh0DPc7LzEWi8XG8FSbagLlGJVHXQOYC+djFdREk20rA0E7qZx1urPbWpdVRWCSvK1o65qEq9M1rXCUiGLOZw7MspEVZRGs7crnsgFfBwth7c8T/3JaJDGnlHx88+Dcx0Ul2ogBX+xdTpe6OtrLGu1TAeWwq2hbUyK8XmI0y2LGVQOkahRgpxqeq7Q7Ip7iYJvV9hQWXmEXscXNNPaoud2qsUGbqyHrNdaZl8pGxIyuW7k47yLQO6hJyF9Uke2O+0U13wHMq/JUaeiWz/P9IrwwmC7v+wOrk0qNls5mDnKSdJZtRWpRUshHYra6cMmoez2/vsExsTIsWUTpUNVvLG9pQhI6aHDtqK2d96tgrtD68dLXfQnPGz5WjHxnndkhllWObsijewsaM5NLL16XphoThnyMwN5uczZ7pT5mjLkIrjnM+pm0R+u56OK3Jjw356VDBIslJVABUdqsMS4uMGHDnqQ5lYXj/Y1mNhuOOCr9qNwuDFEOQ51cOj2YrUBZJ49KwyQndtXAu9SYz47zsFrj6/K27EGR9j2kYHdjKHuIps+TDbeaoaTvhX3h77z+UFRoiyMRy6yzwF2ycz2SBp/i2s3MX+mzYyyueDUR6LasiAM8s6ID0nm6pBKVPAtJwrE3S9Nlj8RAkrOl5FR7Gc3gsprNenqWauNCaXcq5Wa729XLjQ3Sd3IzzzUOWbc96A5myNjpC5pjy4voKzLr29QubBoEoTiP9gR3G+QZ6ZPZrZBXtB24inhNZaRCunZhl0aa1cfgfAAFj1kR8Fa4HRCjFVGsFa4Odg55WdkupCqrfIJKGyu4mWlq+PAC81Q0iRbkdqajumSh3Env4Vt3Sw3PcQIQBR0iaH283kfpYX1rXYlykN2mCE6n/Ww+qrqiRNh2ifPUQLGwULQqAVees+wlJpVrYbmPOa6sOkdsfVyACWckb3nEaSnYdFer65lpr5d8MG4mTMWwR5xTfTQDZ+leRcF2xtPCE5a6Qux4f8vA+9gSpTZZJnzfSMO2OQl7dJsiXbU+JjTpaiKOW2XmL0+0HRdeKy0YdsUrx7ktoZcTK9M2a3vcnDxsVuLKkvdnDNksB4U8V46xLNgbQYupbxzQDbNUZt46VEq8vWWkJ3bEBmERv2awzKgUJ8g5F2zT7e3uelCFXXwLqFN1XKcd0XmHop/xOFssayE9pARs6LSpjq1YLg1HpG79wtSuIdFe0TFt8n1o7ewxXZiranEbK8TkhnN6q0/+YiYla5jF8Y1utDZhdpZTRDxnE1lz81bIHD+xnnaa655f4jbcXvXj8tBTpD3WM3zsNb4uJCLxa3RUnYLg/Wg5Nng9mFiJ7kBih36/SdXKCwrxmKqrduXDW1ea0925xrcI2RpOpXAdl7HkybMxlN+FDHtensT9qYCLCyHPLThFdzgrkNJGKmvKXgobYlhY3lWlTMyY6zhOOvMFVcYlsqx4z4O7mtAqFxGro5fMVqB9JBazje+QskW3iK4bQZ/AchMY2KASSknBq9nsaKzQvbfYOOPOhBNrpUqrso+VLT1fyuHctAk2alGnOx1KdGsKgQljSclt2tK7bRDQXCh0Luu9PYOTsOUOB0bC5VGXCGdj4Am/2Jctk5LyYo2fcVEoe/PMzCoyOwkBeyZpwAe5ZNwSnpQNoR/NyEzwRW1FVYEvFu4QEypR3BI0cDM5NlKwzxwxEewXhE1AOgxoXAN6thfIzqbp2uaU3jHp8rS0Ua5o+0NrpCol3E6SEUfLLR83o5VLaiRWubkxFpHYz6OdTpz1m7zoHJj0aJkYKSTv9FlhUBa7z926a31qJGeOFQmXhSWo6U0s/YSZx8Ea43uuIFoxUNbqcX7E0iJn541xW5xw47oZO9A32juyPrvqbhfinMz4OTzbdgyFyPs5E+m26c0onzqtL+OFuWKL7W1GnuM5z/oivJcToooONE2/vL5Mh8HPI91/+eZ1Okn7XzvQe5y9fXuRcz9LdU3n832tz/9alV9eX0o7BIo8DimruPGfR3v/7Yjy018d/E+zhsfLy+n9Ul9/O+GuTX/6FZuXMHWaqgaLVlnc3A9HX1+spppe+1fTb4bY4OfL3Ygkn458Hwvdv0wH71/r7Ov7rTCdXpm4TmjW7vPSfx7Uvr44A/BAaFdfAZpf3TKfjHu+RgA2oW/I2/zl9/8HHpMt+K8kAAA= -->
