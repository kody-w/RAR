---
name: "rar-cowork-cookbook-report-pay-taxes"
description: "Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pay_taxes", "rar_sha256": "a558ecc9fb748bbd99d67f066f291d1ea0dba1eb1624da65f8ac37009d7b5466", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_pay_taxes`. The original RAPP
agent is preserved byte-for-byte in `report_pay_taxes_agent.py` and in the RCI capsule.

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

Pay taxes Summary Report — Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-pay-taxes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 a558ecc9fb748bbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pay_taxes_agent.py` first:

```bash
python3 report_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_pay_taxes_agent.py   # or on stdin
python3 report_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Summary Report — Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_pay_taxes',
    "version": '2.0.0',
    "display_name": 'Pay taxes Summary Report',
    "description": 'Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36c45a0e8165da3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportPayTaxes(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPayTaxes'
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
    print(ReportPayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6a7ObRpfuX2H2fLAzsjd3EH4rVUcgJC5CQgiEUJxyuIO4ijvK5L9PI2lvO+8kM+etOkd2IgHdq591e9bqxr+/2G0TFdXLl5eDb+fQ2k7TOPIryM49iCv6okrAV5E44D/ILfKmip22Kar65dOL59duFZdNXORgOtvGqVdDNlQ3Ves2beV7UN1mmV2NUOWXRdVARQCV9gg19uCDgW4Td3EzQn3cRFBTNHZaf4Kays898D0t71S+nXhFn9evYDV/sLMy9euXL7/8+uklBr9fvvz+4qZ2DW69aPcVVHvUJ+FgeGrnIbhfjkC7HFyXfhUUVQZueT6A8bj6WPtp8An6j/9IersK65++fM2h5+fry/RHa3OoiXwAz64boJBrl7YTpwD2K7RIe3usgW5A1/ypeJyHr4+Z3yUVJfTz9OzjY5HX0G8+fn0pAAR7Mt3Xl5+gogLrVe30+3WSUn786TUter/6+NN3OXXrXHy3mYQB1K/fntdPsWDg96FxcF/1ZyD14STH//ryg3LT54F70hPMfHm9FHH+8SG4rIrOz+3c9T/+9Hdi3ch3kzSum/8rub88BEe+7QGdnsB/+nQ38q/Q7KnQu8y/X7YEbv1XNAHD35b7BD0N9Xey7/b/J9FpnINQfbP4X4r7qwmzn6Ff/la3/2nCJyj4+rL007gD0eGk/hfo928Hled++eB9v/nh1z+A6P9VzKFoK/cu4Vtm53Hg1823b798qO+3P/z6y4e2BLHm29m3tkr/SuZf2fW+zp8s+Bz18c9zwfpGnuQgeaH3SId+L8p/q/54hY52Gnvf79dfoB/zZfrMoEmJt0UfJvghZ2qA9Qc7/vTyB2CE/EE802OQ5f/+75ASu1VRF0EDHdyibSDg4CbO/Am8HsU1BP5OuV35wK51DAz7HAfif/LwhBgw1m//x73T4Gf3SYPwg82+ASr7dqey314hHcgpqjiMczuFtIWqfs3t0M+baY2y8mu/6gB7OGPjfwa883n6AcU59Ns/i/p2n/Vajr/dGTB+sI/GiRPz1G3qv07ozcjPn1hdwNn+4LstEJgWLlg9iAFJfgJa1UXaAeaaNK2TOE0hL66AWgXg40k2sMaXSdhvv/3m2HX0NX9QJQ49SL2GwYB3ONDnz0CNII3DqPma+25UQB9+/+MD9J/Q/zTrLnxaQwUk/bQ1QCgddlsI5E6bgWHADcBxgBjutv79j6cxgZgcVCHgmTiI/cdkEHuJ771Z9iAsPmMkBTk+sCiwZjZZEvAvFDevkBhA73if1Wdi6KioG8jzS1Bj/NwFlSiygTrvlsyLBqpBgNXB+Alqa/++6m9OZd8hZiCJ7eY3SOFUUA+KFPxvgnkfBCYXeQzM/+73x30gpPpQQ+ybiFdoO0UbKIOVXUaV/VwjsB9+AXXgbToQbkO533/Np1LnT6a6h/7DPGAQsIz7dOnnyeegOoNiC4rn29r3MfZUtfR79aq+5vUzrO1qcoULaB4sGraxN5H9P54hVUdFm3p3+wGkk6SnF7ynV14fLn0r5IdnkX+UYOhriyEoAf1/bQcmAIv1WuPXC51fQvxW16yHYaYWZTLgo6uZ5IHoeCTB99r9lvlvBPg1T2Pg5Wr8x2Pk3ZzPMT/A1xbaXT7wJTDMJPcealPoVNUUpPbX/I1pAWToTivA2iAvQdxO4fK24PT0DWkEkm+6/l51766pvElpEE5Q2TopcHXg+55juwlAVU3p8rQziDt/smQfxW70J60gIB0YG8iHAIgYJACw3d102wKoCTIlqIrs+/B46mUACq91AVrQA/qvkAkifvJ6DdIMNCTTGGCFD3dRUOYDGwOI7xauI7t8gJnaxidA++mLH+3/fPQ9Qu9IJvBApu3ZDbBkPzGk5w8Pv76jfHoKQM2mnLpP+rOzn5pCPxaEf3zN7wjfSRmkajrV0h9MA4EUyep7qE1MUwO2yPxn+IA4uJfN10fle5TWdyxf/lun/PFfa6bvtcz4s9++QFHTlPUXGH7Un7fy8wryHJQgNy79+lmKPoM0+nxPoz/JeZjlC/SvYfmTiGcIf4HQV+QVmR5tYtefYvT5Aapzn1nrMzE9/Zpr/nefguWLDHDWZOoR1L73EvE2BNSJsPLDafCjZNRTpelBcbtzJLD61/zd78+cABSch1N9q4sfcvVeK4EXH056p3LwKG/A2t7UOYX+tItIJ/i1//Ilb9P000tuZ/5f7R4mfgahCLSfNhkgKUDn0cT+/cpuvXgywfT7z1ug3f2HnU55U0y1biLjd0a8w/UqgGVKtDCeKPkTBCCGgPAmDfop2aaC7gCNakCWvjdBbsZywvjYXUydznsb9N8R3PMVEI1XfJnS9hM0tayfoPfu8xP0th+4b6nyFmyIfpk630lnMBR8vY993+E5/suvfwHj2Qj/PYgnlzzY23am2jKp+Bc6AWmVf21BMfMmPN8V/L5u8VjsjzvO5rGV+/3ljS6eXnq2bWA4yMvP9VTOYBC5YEFw/Ygx8Ox/beie4wGdgQYDTLBJcu67LhM4NDF3HI9hPIoOEIoKMAb1UN9GADOjvoNSGOHZFBnMbRenEYTxaIckKArIe0Tmt6lGxxMGzLbduUujhMfQNuX6OOLgro9iqEfjPkIyeDCf+wQwx/vUBLDhU7GHIpPV3nvLe2A+9Pv9xaEIMFIganHx+HAwc7Rpk3a0yGEqyrfIgNrjxtVIbjq7T5OOqqLdNuEctjrj8Vw8YixPJlc7O6ztdSMj6FLdR7NCY5ILjt86dplKI9LOYpXNyCa5bXG69UmSIFxWEcLOG0WjIUp5pK7M8Wpf9OikmaQ89zu1I6JTahC6TB36EpTK+iJeec/qFIw8dxG7EpHNunRojTQcl8rFdKxG46phEnIN6/7knyVTatPNsJs3nRIVKjuea5zEvE6PabWLpJwewXcPr0jjKu0URk7PR+7YGtftqDWJ1mhVtT/Wh1tykgNkuZkdzVV/NHhcYg7Lo9vv0FN1XXEkdvWTVGDgne4OVufZlhIzx1TeUia/HhUpVNY2mZeRI6Yoa+Aj2Mycx82WwLp606nZTigdis4OXmLCq9GGjXOuWOEpGDbAarsFm6fB7ah4cXHcjynMo54o85GKOeQ5iZcM1Xqbm10n3kIpewXbizLFbgLnsiPoFbKb0XJqStEcP1Drch8L41m5RiVRnY/7oks7ySjDa43JLdKNJlov5+K+Ptj9KZAKdV2frJSjPMm5kuetnzM4bJDqcX5tecrcieejKCGRztljKm6d2XLYoBK2saidt+xR46Sowya+OH1wwizH3azKoT31pKXQSSLgao2g+o73HFOgJOOcIWSFyt7p2A5jE8jnvovz1M2OHXfm2WBuUap4lG6Zs4vKPIXV+XlOtKvFyGNMH4kObq4lmLNODiWkR7K2/H1rw02soCu7HTe7AVGKlLRmNzw6rWd5vAg8WaiH7UlZL4wbWWzKOOf9zKqCEklPYQKfrqfwIBRHwVd36CUy0wKeCzUCCxVNBAGxPoW4etQiSSCx5mznm0Gre7yvz+sVZXooX8ftsQcMo6/4fcBHoSkH4um0kw5z1Yxj+qTApzqtr8clum1nhiSly/60G/bGeNtws9VgtwDbWoqqMLUia5Htz9qR9S4rMb24+jwUe9GpSFboj3se5OYq25rnfieF5JbM3Sveex1omOY7YlloeBDquTa7zQsPDnHjTOfl5kK1vtQkpjw4p8VAcqNpz1yMHmt12NPUbeshDTt0I9NQHZaeVlXdRdfYiQGjFGmdp+ekzxdJ1KnyIo6by37RKA6tK/BIbJKKGk+Xijq4sn/UMyNolDMKLpqVmHUVLp02UowQmCu3OyfQ6yHYipkpEvOhWpkbWLlZ55pqh3KrknswK75uDzJtOAjDy1UpkB0qevIaMy6ph+3PjpLtQmMen8TFbaveCL6R83nqmhFG5wt6jlQzmemxQzSThCW81YpS2JEWLFqzAyrvRwPDSFbttoGbIuFIY/3W1DRx0zSjo6+iQV1blIYEC1wzrt6OLMdDRC7a8HRMqeUuiHsHJEvZc97CkEoyyJLrFsu9NrD1EnXY09JVPe9k+gwsZbd5JZcbvReJ5Qk/6rRES2Vja0yg6W4LX/TzrV9f827lWdX8YAeif1zJyjrzaP24oPMkQO0Mo2YJL2hcVDALhWKMxfZi8qOwNWuM38QqXV5PF7RzF9FJPg95zu4CVcWU7MAZ1ZS3p4vK17iB7XWL0wSzUMZsaVyJJbNI6Kqro+jctvI6OWv1qCyowbzpm7I2qaaEcVdg+aHU2CVJsoZsrIYuXru01KcGU7Jxci7tJI5ZcbuxYlPZ7mrJ2hs1Qh5Yu2/UQ7Fd5h7XSkneOjfOS6hZUDWUl9ExrdhHe1xX5w7WD5W0Z6vEdGg/cRZgO3wpDg4yg5WEyzWCCj2kDerr/jzC8YakNyJs4tI48yVYOl/0ZmYwy1DezebyLUnDJd6Lg1E2QrI9rXw+FK4DIqyPadlFHuu2BpG1x9FzWRkrACUwgc7P/As5m5WDWcntIYxajdWwgbVKZQ6LtlX7C2y5Yit+2y26jUgKaRn1+nxZ6euzTmPYEq82sorVQnAclvPFeiFmjXETyvP6nFoUpXugWm1yLGRH2c72gZ63TIhSZkaAeDaRTvcTs05HUtVrilnUQTsOrnVl0KzcxMxcsRD3ctpjBG+FcUViNxU7YrWReVfanlUzaqXnOCKUiNVvEt6RndxLBCLwZvDyIAx8xNmMej0EyWW9XG1h3crIeWKYlnyTM+dkqJ6txFmI7YxiM1YtNpvZa6NYbUN7JqPbynIHJKwG0oWPSllzi2a9lw7U0UWqJc+HNpsfW/Soo7Tee0ZtJYcqmG/ZfrszCHabOomILU6EuokdN06PhlnR/VwSzJ2abooVp3fFtT/kViPdjDojYnGNhPuLCuOEDVqZ1PaQiN+XRLjoYq1GXJfE/LKuTE1msqReVslcY26WDhOzqBvwUxWvhrlb4oh7Dm5CO0OcPXIi95xoRoh3KA4SnljLhbXftSZzkXwfxm0xZNiqzHcdteUlVUsKcuVpcTbvE9uQFaarBDkiz2EvqkkzhmaI62wnHjyN0yRht+UvXXg8lYtwxVkDgfICblXXI9xwh2RlLkVmjeNnS22GGZZso5ggufRGLAYOD0my8/Jt62mmdhYOAd9rs5YKJNKb3da2e+DZRjRpNdilgnLQBTTvSSoctXmPYUGeeRLZDbR1AN7MvIsaNLdyXyprI9YQzsWr063luDraF3s0annfjNHDJTkLi5lGLtdY4WCrcHaJYS8pl5q3tN0lZ0fR2ElXObWz8wIBNZGPUzLPnLHZHLkw9Q0hY29sLXXptW7lmEgpwthyBnmmIn+3Ege1iNENdwO4DuhhRd+qtFL7o8Kfb5peuZoWKYU15oy9R0rRR5DrdVnz0t5CCZVWw2sW7+cWulJKjmfmqU/Q3Hk+8w2X0WQDtRrxWqscP15niDyM2npT3tbqZt07dm9dNILzrII14dSSc3VZKtJWOl08OZM7083mxvLYkDNSO+9p/Ly1ie3C5OfccmEwW3enc+sF4+5a7rTvsxqGJVuQy/xQGufdcL7t59pw1pPd/rzdiMRZHEWEPTaxBoKWWuondVz3Vk/6UnSFU5Vb2BJJ1gdWUfOL7lX65SB6hc/Tu3A2Z4/23LuhG2qvMUNbpehSyay03QFDGHZ0aFm/Y86IoJc5QVjDTPeWVCwd1kShHfhrEeFMvjq4pFLBmg5C9FBhaHB2S+9gJ/RaQbLTcWnhW0NwL02TRKdhPxtrMb4ui1PbGpK1MItdxopWXhMYbaRiyMsroh1B/Ylktw6lYqA4T1W4EMXCo4Jm6RHTt1EIz5qEUvVEUiOvkn3xZIQtxkvCYj8Q8zaIxwOG5fDKdMPLijF220aoZfsi8nay2c6zraog7H48XxQyl+ndvjKz7TUwOLXlEDmrQYkoHFxOa6eLXKv0ku1ZROozybmUJdsR5afnXZDFlcCRCukVuDFUS7Gk9CKXqf1ONSjX9cuVbVMSH9R0umC6uk88Uwu6XkrrmeisTqWBDz4Rd9Z5TQicTNmo4xJIqzcILa7ES64WCXu1qJvTNq3M4Kv+YOplkRFwJ/P8fsZe9j0q6Gv0dgpv1fa6TavlKARoOzSnEs1QEzV6sNEC+wdh3TjM8dJWNG7Zhq02KI042YxmEO+EjWgKk4zj6YBuSBSFhX5nLlrHqpz13DdgJpKpqxuSnrItvdBdsBu+wWWaX/lwsLzVKbxa3MylC6N7xKbY6oZTR/ZyPksqdZJITcpU+Obv1UhEC7B1SI+nCmdcjokvxr4zL9Sll/FTnajtKIXVHD10UXYVVguVGb18zzRjeraCfGE5gAvHOd14S8L1lxuaGucw0Xe1xGEFRjcBPGhBfqhw0LoaTFCYIeE0x2U9dFiLFv75xqsxWqhX69J3GSyuHV0N82RHENRWsNdkakbsXsQKXheyDbkw9r7RzMWw3u2JNHGFNdkgfYu7dKFbV3WvXDa417B0uzgGcn+uHDI4dbLiFuO8JBtqrxRdSKNJS5epfOqOod+d98ksSAREgHH+uHewjZJfkLDHc2ePulFAqn0mB8N45VbCWuVw32M8YrGUo04pcxTsmDcXixF4e+vdvA29k7uTMNT+mXevXJUlKsFmopjD/bwIAGRgJJq+SIVs0valcTVHW6nW8YhZuj3AKWaTOu4UFLui/WK925l02lxuXeoOvW6IctA2OOi5rNkK9Td7MaJNRWOLEFY68XImJKGhZ3XE9RusWq/IWQxsjeyJ7jhsaV48blhkf1NUE7S4K/JqLrbdOrFui5owmDjnXF/B3NNO9ZGGP/V5G69X+Gm+x48Io2rlWnRaFtlUrWmtcRYJKYc3eo2MmnCJnvwLgezFjX+rlNk152a5u7lmxCywqhhF5yvptt7SIACqsoN31ZrmL9tBwGt4IJGDO7ZLzB6dVEFyDuTVqGhihWEZcYCJM92Vu+aCjQFudtn6hEXLWNjekFUe2zHuC6oZoAv44lwNpiNGkXD0eUHmKxhLDrVgY9Fpu3RAHOzARnR96ziqOm2qrHNsm2k3S37nHQZqXVBto60Zn07y27rgOBeuknxJKs4BXbOAE6ILnO4uTRGxvb+8kJq8aVs/aU4zkrTbQW2TPSPSoElfs/GsxnBanHllTeF04YJ9O2MGitX4QXepLiXWBC6ynOUjp5JB2FLLpptfwhvunFjfatp4eandyFvQeCKaIU3XAjwDbaV1hP2mDx2aMmGWW8i+srPC7LYAZCZlRZ2Ahpr16e11dePttj23fVjxXaTB67JYh0kqUV0Xn0m42fIHxakjhKnbWTvndGZ1bivB38A3zqFrtCCuzYpUjHY5i3pbcYVeZZxDxGVgazOQISV42eFKVy7a2jfacTyKci4XP5Od60BGVy33lmTWGaPfh/Od4M8NVPVX+ryzbux8wXl9pK7IYl3D876Ir7BhAm7XEapG3Wx3igKMIr02DQ4FNaTViASEHm8IucPsil/BLcmIczZlUl6iCwYB+VaDrpvKdziH724XIdNJ4QiT7N5jXGVsFUQ+AUpbBUd6PljsHj622S7LAgxLVJeuml7YLbyc720YWUl723YSS8R2aWdqi05JpdzwD8shZ1R3y9HFJVEouGxIlqIPl8KFWXffqnnRce5isfj555dPL9Oh7/Po9m/foE4nZ//PDvAeZ21vL2juZ6a+7X25r/Xl7yH8+umlcmMA4HEIWadt+DzC+6cjyM//fJA/jR4fLx2n90RD83Zi3djh9E9gXmKwS62bavxWF2l7P/T89OK09fR6vp7+BYcLvl/uoLNyOsp9LHD/MR2kf2uKb++34nx69eF7sd34z8vweQD76cUbgaVjt/6GU+Q3vyonpZ6vBaZzzOm9wMsf/wWWwqJIRyQAAA== -->
