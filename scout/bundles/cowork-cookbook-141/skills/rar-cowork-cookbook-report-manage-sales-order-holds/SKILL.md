---
name: "rar-cowork-cookbook-report-manage-sales-order-holds"
description: "Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_sales_order_holds", "rar_sha256": "9cc3b71330a539be9cc1787c9785e12004011d4c6451f2597599899d4ef5fd3b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_sales_order_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_sales_order_holds_agent.py` and in the RCI capsule.

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

Manage sales order holds Summary Report — Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-sales-order-holds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 9cc3b71330a539be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_sales_order_holds_agent.py` first:

```bash
python3 report_manage_sales_order_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_sales_order_holds_agent.py   # or on stdin
python3 report_manage_sales_order_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order holds Summary Report — Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-sales-order-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_sales_order_holds',
    "version": '2.0.0',
    "display_name": 'Manage sales order holds Summary Report',
    "description": 'Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-sales-order-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-sales-order-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e5f564bb9f7b3db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-sales-order-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageSalesOrderHolds(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageSalesOrderHolds'
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
    print(ReportManageSalesOrderHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOiWLbvV+Gd+0dmNScPs0B2dMQTZVIUAUWhsiKLGWSUQcC69d3vRs2TWfdW3e6OePHMQZG117x+a+2Nv704XRuX9cvnFyNwCkh0siyJgxpyCh9alH1Zp+CtTF3wD/LKoq0Tt2vLunl5ffGDxquTqk3KAiznuiTzG8iBmrbuvLarAx9qujx36hGqg6qsW6gModwpnCiAGicLGqisfSApLu/rvDa5Ju0I9UkbQ23ZOlnzCrV1UPjgfdLGrQMn9cu+aN6A8GBw8gowefn88y+vLwn4/PL5txcvcxrw1Yt+F7i5CzMmWeokSpokgbWZU0SAqBqB5QW4roI6LOscfOUHIfS8+tgEWfgK/e1vae/UUfPT5y8F9Hx9eZn+6F0BtXEAdHWaFhjrOZXjJhmw4Q2aZ70zNsBu4Ifi6ZSkiN4eK79zKivoH9O9jw8hb1HQfvzyUgIVnMmtX15+Ak4C8upu+vw2cak+/vSWlX1Qf/zpO5+mc8+B107MgNZvX5/XT7aA8DtpEt6l/gNwfQTQDb68/GDc9HroPdkJVr68ncuk+PhgXNXlNSicwgs+/vRXbL048NIsadp/ie/PD8Zx4IAIfXwq/tPr3cm/QPDToHeefy22AmH9dywB5N/EvUJPR/0V77v//xvrLClADn/z+J+y+7MF8D+gn//Stv9twSsUfnlZBllyBdnhZsFn6Levxo5f/PzB//7lh19+B6z/KRuj7GrvzuErqMgkDJr269efPzT3rz/88vOHrgK5Fjj5167O/oznn/n1LucPHnxSffzjWiD/UKQFqGToPdOh38rq/9S/v0GmkyX+9++bz9CP9TK9YGgy4pvQhwt+qJkG6PqDH396+R3AQ/EApek2qPL/+A9ok3h12ZRhCxle2bUQCHCb5MGk/D5OGgj8nWq7DoBfmwQ49kkH8n+K8KQxQLNf/693h8hP3hMikQfSfX3A3Nc7zH29w9zXO8z9+gbtAduyTqKkcDJIn+92XybSop1EVnXQBPUVgIk7tsEnAEOfpg9QUkC//hPOX+9M3qrx1ztYJg9s0hfyhEtNlwVvk23HOCielngA7YMh8DrAPys9oEyYAJ6vwOamzK4A1yY/NGmSZZCf1MDoEiD5xBv46vPE7Ndff3WdJv5SPICUgB7toEEAwbs60KdPwKowS6K4/VIEXlxCH377/QP0n9D/turOfJKxA3j+jATQcGWoWwhUVpcDMhAkEFYAG/dI/Pb707eATQG6CohbEibBYzHIzDTwvznakOafcGoGuQFwMHBuPjkWoDOUtG+QHELv+j771oTfcdm0kB9UoB0FhTcCrg4w592TRdmCntYmTTi+Ql0T3KX+6tbOXcUclLjT/gptFjvQLcoM/DepeScCi8siAe5/T4PH94BJ/aGBuG8s3qDtlItQ5dROFdfOU0boPOICusS35YC5AxVB/6WYumIwuepeGA/3ACLgGe8Z0k9TzEFfB20a9Nlvsu80ztTT9vfeVn8pmmfSO/UUCg80ASA06hJ/agV/f6ZUE5dd5t/9BzSdOD2j4D+jcs/BzV+NAMZzWng0b+hLh6MYCf3/nCsm9eaiqPPifM8vIX67162H26bRZ3LvY1qa+IHceZTI977/DTW+geeXIktADtTj3x+Ud2c/aX6wRp/rd/4g0kDtie89EafEqusphZ0vxTeUBipDd0gCsQBVC7J6SqZvAqe73zSNQWlO19879j1wtT8ZDZINqjo3A4kQBoHvOl4KtKqnYnq6HWRlMDm2jxMv/oNVEOAOfA/4Q0CJBJQH8N3dddsSmAnqKKzL/Dt5Ms1BQAu/84C2YLYM3qAjqIcpJxpQhGCYmWiAFz7cWUF5AHwMVHz3cBM71UOZaRx9Kug8Y/Gj/5+3vufvXZNJecDT8Z0WeLKf4NQPhkdc37V8Rgqomk8Vd1/0x2A/LYV+bCZ//1LcNXxHcFDI2dSHf3ANBAoob+6pNuFQAxIzD57pA/Lg3nLfHl3z0Zbfdfn8Pybwj//ekH7vg4c/xu0zFLdt1XxGkEfv+ta63gAKgPblJVXQPNvYp0dVfbpX1ad7VX26V9Uf2D689Bn691T7A4tnRn+GsDf0DZ1uKYkXTCn7fAFPLD5x1idyuvul0IPvIQbiyxwA3OT5EfTN937yjQQ0lagOoon40V+aqS31oBPeARUE4UvxngbPEgF4XURTM2zKH0r33lhBUB8xe8d9cKtogWx/GsKiYNqdZJP6TfDyueiy7PWlcPLgn+5KJmQHaQpcMe1kQMGAiaZNgvuV0/nJ5I/p8x+3Xer9g5NNNVVOXXKC8XfwvOvu10CxqQijZALzVwjoGwEwnMzpp0KcRgEXmNcAXA38Sf92rCaFH7uWaYJ6H6/+pwb3WgYg5Jefp5J+haZR+BV6n2pfoW/7jPu+rejARuvnaaKebAak4O2d9n1X6QYvv/yJGs8B+6+VeOLMA9kdd+pKk4l/YhPgVgeXDrRBf9Lnu4Hf5ZYPYb/f9WwfW8TfXr5ByTNKz3EQkIOa/dRMjRABaQwEgutHwoF7/+6g+FwOkA9MKmA963mES2MEgToUwboBuMZohvZYmqECDEdREsUwn/RmJIWFOMXSFMsyLOuTQUiFPuECfo+s/To1+2RSCXccj/FojPRZ2pl5AYG6hAd4YT5NBCjFEiHDBCTwzvvSFADn086HXZMT32fWe54+zP3txZ2RgFIiG3n+eC0Q1nRmOH3exi5Mz8Locoa9VuEZ2tX9WvQLdL/f7udheVotN24mpnFardoNJgrnY5JtNJdT4yU7L+jVrvM1uEpwL9v4LC+oaeTqo7ZbMkimsnAszffcbH3aUKa8Wt+2WWxke9O6mKMp17fuih0ry/Uca33A3KTFWFgwkVOeOmkjmPYKM/1Lplu7GYaizLCoVXi/Xm3XJzi7yDMKa/W1eTnq+RnVzcv5JrhUXsjJzLzyt61/pJdocCbhUL2hcCi5KIzwTnAlKprl5QuxHg9GinmXmjSaC3WoDL9eZOuV4xiNcfRiy0a0TYgdrRMXauamwNbb7bAw8LCTUwXUd250TGkzfqEI9EVaXvZHARfI9CD0x2Pl6RHVtwWqtel6Vpa1aVatV4k2xa3rNbvt9Jm6LZK2MhGdONhlnXkNc9hz5rzeadHBJ09NYO8bfXHZG8fRMNGoNA43G3dPK4GrMW92POK+js5Hd07b86guFzXcedS5yTyJYi6mlYmuv/fsFWkTRiUdFjszuJhriQyTQ33wHUpwpfVtedr2oSQpfNIIx9E9Z/USrw5NsXDyq7g3K8VHCNhFw3UWqVkWi5jD+bLV5161Pl+omLkN5paZ7eqTG2xNblh6G7rCexqjmN2Fwm+WtKftjeHIPhdZiM1mTWq5HdHIRmXWCSGZjnszyKY8LZpQCRf0xWv5/mgvit1OMoGv1KXAoNz2rOQ7ZtXTaubdBA8fY2uPH9XVsKATCjsJQd7KgQZ7bLtnCP5yKdcq1ao8NrNgyYyt1t4P8qbLVvhMWF1IZJX1SNqT4eh4OwKvbun8xoTNYYZee3Tf7AvS2fWpZ8EHskguyh4hN+Y+sUPktqQkWT1v2AMlZJ3bOj16PPVnssR7w8mVMZ25a1vwlLTDqk2qw0wgcqcVHB+FxmissPVo4mIvGluhDvO5UAdxth5GIVSzkBtOWbfO+SETQkttD1pLasqcWVpr+eIQcp8w5t47dxHIC+y4WLfRqlwZQnPkMbtIho2oi6DOjrmAIivzNs72Q4L4AiX1emMwCZue+Gt8pll/tl6p8q3Jd7fd9oiPqpY7nY7Imws+UofbJQ5ZhNn7enQ4We6epslusAs0ywanVhhXhvVq5o6ruqkqdbskDZJO8LmQ1TLDGVGLoEsOOemHY2jkzGZzsvIaHQ9z3q0ij6wu2PHCm/SWQFu+sAPXzbmh8M8lY/uhvi6boVCv+1KhDGzbzfgFu3XwGY1XK5mzzeNVjFM7rNUm2NvpuiLa40znjBKRa3V7ZH3TW6gj1x8WUhmE/FHflniGWamCMNwOOSSMc2zna4keOWO13hprBI7S+DxoZTIojqt712LUd6p81HiBtsRakc8hvjALm0piNOdRHfGiQj/kvmqno65ziZ0VlR7vqZWqwNGVbxwKIfEYkRjXzOsSpzc3i0Vn0Yhl+/OZOGXbZTQmdoNsumYoyWir4SZywBfBeHTx1A8Q7kZjNUEjGTdTbqcuZYNdgnI9w6wNlWk9clz6Sicanh1cJAI2BMG2zPN4ks722dIOJRoz5Yi5WSpb3S7VpRsbMfO82KxXxj5LTjVFijdlcMDmMIOT1ejutkuFF4clLwfZQvdKlIf3wbyaFYXC20flKgzGvBIG0dtHitX2OFb5tZFYmhtJM7ScJ/Y+whPbSnfM4GeeymvRht9FVJI2UrY2tngg0IzFEiMaVzJt24OjtaEhb/eEzXQpekt7pnK36pVoB+9aXxBF56R1O2ANhqwoMzV3ikiJDivjwm6/FeOKIRhG9BRGqWsVZKWYxAvpkl6FjGXgU+ohODFgSDyI13bOWN1CyLcUdSAEWRPSKEar2JG2G3wBy+XykJCmOotu823bCig6JuHS4gRUrPNTJPDlRfdNXD+MO+O6CDpNraq8tRK638vqKKW+FaskNzOHTMf3m9N8dRiyVXkrGJb0LnFAH2YOPTs6BTtzo2KJrUp9gwVLGEwE3Uqa9Thn+CuTkJzzAktbZx27BhHkSKdZIu8Hs/x2lqlBRemIVzYBQPa5KuyEUKn3OapndLfYzgyqG6jVSrEbnS0xbZEph9wqFb4rZs36dD032lI+7yvWoOiC7KlKHv3ZsOnOtigM+FVp0I66rEoZsc6VysZbzriw7fU6S9PLIiMlPDkGs3Z7SDUzoqTrrDO7o9iocznZyoemjkWvP+YZpsLHm3lbaSiCkZqeh0rGq6Z8IIdlqqAir2WkuNa1K7ew6902pYJDfJnjl/2avzWb0+2SzjDeV8UGvQmBtk4XFsWY8JHuxSuZuo5m8GZDLswBNtwRLwBo2rK5cQUru3AOJVKI3ZU138XXFYlVhjCOzPmIt7p/A0OiU1WVsDouERNM0XImHjtWKDkg99S05MzK0DNmydejm7O3A6terEImT9E6qQe+woKqnSu783Z+89VRX4fztOoB1B5vQrEyWp3TK14gy+48v+Q9x82ERqIPWuift9WJQVeOZpfbGnWIoB9CpzhpHinWRXTRhp5L6Gve+NwejjdO1yXj+nxdRSyLwMRwZGF4gxupteG1duZfWQMNolyt3Rtx2TrhwKUd0oF42oXM2gYr7i+hgRNOEQyn8pQAMYB7NfqxYhrzhheXNw/vTa9eWRIsYwvdiq/y8XxRbtuZB4aW48bWchXrFjrJjofL4eZJHD1WBy/fhiFI5E1nouc+aleKoKwPpbITkkpdO3C21kzV8MjLJk54M+o3s3ijGLvDyUxUjarhClsKkSlthc0grCQ+uIzVLilUx+DbVZBG9YU7DCttPqMRZRWNaq5r2kxutooQqw18ZnbSecD0m8k7rdjgyWEg9xgowviIWkdhcOWquzVH5ZBF53StVwR1wqsxaXLBoc79aVEkCpauDngsZvYuTq41IYvBTej2djnXaFCuPZgvNVy2PBXTjr3cXnfuGWMHZLT6zuj7zENrt8E9asmLsWGokjErmXm2z4xbucLEblgbDl2a/v4Ww/i5gMUNGgE0Ws7FPdUhipCUqYiqiW7pjLiozcXawkKZ523PXQ+BdhaIPbdXc4ftfS4pD3XC2Ugtzmf+Jgy2YjhzyuigrzVC2MhaYfIq25Ct1qOzllH72WkrqUD2SF1GCovQ3S316JUbUGvOFf3W49cIIxBmLJpa6AXrmZZFis3rmrJMkUI8mYeKlzPtKiSa4zCrfZZymHjS9jl1PYgdalRJg8YL32427hWnF+UQapuZiMsZGbcSh2uxbCU7TBLQ8tgHOIqQ1pmX/RDbnt2AXsTlyInVYggN2mi3t3STWre1Dbej7Hbn9uC3q+tcXBEn0xETnVA5zTy1t9l8TZfZ5mwIu3q916XLZQngOKVwp9h60XjojrvTQsTRtB6UuKkrvsyWNewTtHA5U2izDaVgSe+EanVJExjpTWPVmCeG0ErYvoBZGz2zkSwI5FAHWFKVhN84G3WQFp7m+YdeGDFP91z6Sp8LAJIOvNoSw6pVu+iSGsxV0zkyZpfLkra1jpNlwr90vjCvtZpc4tl1FVTH+kSfxOUY4VKLncZ8Riwy7Bb6+/XOLwOp7ResA5dKbYHBWzWPgz+PyCPbBPwsPsvCVlm59Kmn99VRdJvNRr0dSLxCuaxfiWsicBvtKLfwLgDd5KAtnQwVzPXQzI/YNazQNVc6uY0WJ4xXLQlpcQ5ZcZfSRvhLzQZIfTs3BydaMqer2enhgUUTBoc3Qsh2B6bEDIdcxGDcrmn6otV7iSWXS8+I5FPhX+NweR63u4A4EQi3JACUxPOdJyHw+kTN1gHsk01RU3vT4betEgZrPsOrpQ3KmpF2OrfmbkoduQvhtusrdj5Q20iTkqstWHt3w1UcSpGJmkq8lMmCcZCX6W60CaHvFHOjsLc1bs0UgzSTtL7qaLCMhQpgwMZlO/eW74IDQOx02KLKWpHXCIW63qbJGXG+JJH1LMaCFIk6EU5mnD2IEXxFVbBhXdPXVIHPHQ8buFrqkkAljU0UyAnsPGalu1yESw8TgFqw4OA7P8EkGO4Ys4CbkO0HLSs0NiA5Zb7V7TkchLHnLXOioK7hRt8uRto9sEMiL3raTW7iwNIuyhC34yUHi/pN47IWfbbzWTjAxLhwrdV6w+0ItbI3XBAmcivIG60Fezm1zHz01OiMv0HGLUrQnCbQVD1nQj1YH2fr5HQhc+LCg90WKVNnt+llb7HB7HmOJKiPL7xYQHCVv3o+NfjkdtijscuJo5yc2v1eglvpfKNpZT4sWVLS1NbdnMOuXYG9ktxG5xtnRYPW+cSqjUgwLcN77nDcsbB2Pgk2E5+Q3aiQyyQeKiqU6qvaqKDab/ypBSp57ErZ7L1bvkFozc/hyD/Hen5cMNsqF6+00Es9ceJDd1sX/hEIPQztopDVutf0XbQUcHW5PKIyH+4LVATQwRmhf8kTZmFfCKm7WO4YHZe25vtLtulmyhHDx4qourQDI3o7LpeHDqFiFRTY4qrjHg9b235+KLYiHRRViFOoxR+WlLijGl+itcU5ZSQFLQ4ne8tacofsiZ1/vnpyTGp4i7oSNzA2W+AGTNnd7Ib43YnzPax2l6K8JBi9qbfoRcrm7kiTZ+0U8jmGcKQeSjNG8cUV6nvWNqWbKGgUwM0NIwQZ4P4cH7ZU3cnECS28XTJfBRvHisTr4pDXJzxpMoTHhaupoomeXk8EB4LqsycyZZcoOu/Xh5g9hTeSpPBFsiTV1KNw/OQrwWrwR5LA7KtwHdRMPPsXRC+1yi+y+Rnd0MC5MIGJi81ydxpWGS1tL/rFAXvxzhgvbsjS61NbnC3/OOvFeG3G/hLJdyns9xypSjBpYqzDs0zh3oZ+vsD6eCdg5YK5wTcruYTrZbAXS9EXnet+qfTXWvFzybhWUmuP7Oy223CD0PAE4ZhnDrmxOZrMR2TgFgFVa+4m3tYZKnksYR1puJmbdtiwx7BROJ673UbqplUWZnnHbn2ltMjcwUZ+mNEUYeH9aoDVcO6Vq8a7LVtas3K9yhtjXrizLroxuhUeAl2nKkQi+DkZdHVPLVdt6p59atYqF2+nhXgp0amQlvP5/B8vry/TQfHzuPdffWI7HbD9PzvnexzJfXvkcz9pDRz/813W539Zo19eX2ovAfo8TjKbrIueB3//7Rzz0z95UjAtHh+PQKfnUkP77Ui8daLptzsvSeF3TVuPX5sy6+4Hqa8vbtdMPyVopl+beOD95W5SXk3Hww954MND77b86jlN/DI945+eswR+4rTB8zJ6nui+vvgjiEniNV+JGfU1qKvJwOdDh+kkdHrq8PL7fwE5TiTtDCUAAA== -->
