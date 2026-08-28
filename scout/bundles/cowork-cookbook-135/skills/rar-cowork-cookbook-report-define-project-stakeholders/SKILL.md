---
name: "rar-cowork-cookbook-report-define-project-stakeholders"
description: "Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_project_stakeholders", "rar_sha256": "eaf2cb39ecab4500eeb2a8c4f58d349ff2d63877050889c3253f541a1ac8b749", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `report_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Summary Report — Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 eaf2cb39ecab4500…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_project_stakeholders_agent.py` first:

```bash
python3 report_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_project_stakeholders_agent.py   # or on stdin
python3 report_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Summary Report — Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_project_stakeholders',
    "version": '2.0.1',
    "display_name": 'Define project stakeholders Summary Report',
    "description": 'Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6e0e31b02135889',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineProjectStakeholders(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineProjectStakeholders'
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
    print(ReportDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOb2JLvV9HU/GH3YBcIxCLf6IiHEIsEAgkEkmh32OwgVrFDT3/3OUhy2T3Tfe/0ixdPXkpAntzzl3kO9duL1dRhXr58etE8K5vxVpJEoVfOrMydMXmXlzH4kcc2+Ddz8qwuI7up87J6+fDiepVTRkUd5RlYvmqixK1m1qyqy8apm9JzZ1WTplY5zEqvyMt6lvsz1/OjzJsVZX71nBrQWrEX5onrlWCpU0dtVA+zLqrDWZ3XVlJ9mNWll7ng56SQXXpW7OZdVr0C+V5vpUXiVS+ffvn1w0sEvr98+u3FSawK3HpR7zLXd3n7hzjtB2lgfWJlASAsBuCADFwXXunnZQpuAS1nz6v3lZf4H2b/8R9xZ5VB9dOnz9ns+fn8Mv1Rm2xWhx7Q16pqYLNjFZYdJcCO1xmddNZQAfOBO7Knb6IseH2s/M4pL2Y/T8/eP4S8Bl79/vNLDlSwJu9+fvlplpdAXtlM318nLsX7n16TvPPK9z9951M19t2tgBnQ+vXL8/rJFhB+J438u9SfAddHHG3v88sPxk2fh96TnWDly+s1j7L3D8Ygfq2XWZnjvf/pr9g6oefESVTV/yu+vzwYh54FovP+qfhPH+5O/nUGPQ164/nXYgsQ1r9jCSD/Ju7D7Omov+J99/9/Y52A/KrePP6n7P5sAfTz7Je/tO2fLfgw8z+/rL0kakF22In3afbbF23PMr+8c7/ffPfr74D1v2Sj5U3p3Dl8Sa0s8r2q/vLll3fV/fa7X3951xQg1zwr/dKUyZ/x/DO/3uX8wYNPqvd/XAvk61mcgWqevWX67Le8+Lfy99eZYSWR+/1+9Wn2Y71MH2g2GfFN6MMFP9RMBXT9wY8/vfwOICJ7YNP0GFT5v//7bBc5ZV7lfj3TnLypZyDAdZR6k/LHMKpm4O9U26UH/FpFwLFPuid+TRoDUPv6f5w7Un50nkgJPwDvywPtvjypv/yIdl9fZ0fAOS+jIMqsZKbS+/3nzAq8rJ6kFqVXeWUL8MQeau8jQKKP05dZlM2+/mvmX+58Xovh6x02owdCqcxmQqeqSbzXycJT6GVPexwA/V7vOQ0QkeQO0MePALJ+AJZXedICdJu8UcVRkszcqATycgDrE2/gsU8Ts69fv9pWFX7OHnCKzR69oYIBwZs6s48fgWF+EgVh/TnznDCfvfvt93ez/5z9s1V35pOMPUD2ZzyAhltNkWegvpoUkIFQgeAC8LjH47ffn+4FbDLQzED0Ij/yHotBfsae+83XmkB/RHFiZnvAx8C/6eRbgNGzqH6dbfzZm77PJjaheJhXNehkBWhMXuYMgKsFzHnzZJaDxgaSsPKHD7Om8u5Sv9qldVcxBYVu1V9nO2YPekaegP8mNe9EYHGeRcD9b5nwuA+YlO+q2eobi9eZPGXkrLBKqwhL6ynDtx5xAb3i23LA3JplXvc5m/qjN7nqXh4P9wAi4BnnGdKPU8xBkwc9G3Tcb7LvNNbU2Y73Dld+zqpn6lvlFAoHtAIgNGgid2oI/3imVBXmTeLe/Qc0nTg9o+A+o3LPwfU/mQe05/Tw6OSzzw2KzBez/89zxqQkzfMqy9NHdj1j5aN6eThvmoYmJz8GqIkfyKBHoXyfAb4hyDcg/ZwlEciEcvjHg/Lu8ifNDwaptHrnD+INnDfxvafjlF5lOSWy9Tn7hthA5dkdnkBEQO2C3J5S6pvA6ek3TUNQoNP19+59D1/pTkaDlJsVjZ2AdPA9z7UtJwZalVNJPT0PctObfNuFkRP+waoZ4A7cD/jPgBIRKBLgu7vr5ByYCarJL/P0O3k0zURAC7dxgLZg3PReZydQFVNmVKAUwWAz0QAvvLuzmqUe8DFQ8c3DVWgVD2WmCfWpoPWMxY/+fz76nsV3TSblAU/LtWrgyW7CVdfrH3F90/IZKaBqOtXdfdEfg/20dPZjY/nH5+yu4RuUg3JOpp78g2tmoIzS6p5qExpVAFFS75k+IA/u7ff10UEfLfpNl0//Yyh///fm9ntP1P8Yt0+zsK6L6hMMP/rYtzb2CrAAtDInKrzq2dI+Pgrr47OwPv5YWH/g/HDUp9nf0+4PLJ5J/Wk2f0VekemRFDnelLXPD3AG83F1+biYnn7OVO97lIH4PAVINzl/AD30rbF8IwHdJSi9YCJ+NJpq6k8daIl3ZAVx+Jy9ZcKzSgBwZ8HUFav8h+q9d1gQ10fY3hoAeJTVQLY7zWSBN21Ykkn9ynv5lDVJ8uEls1Lvf7VRmWAeZOt0ATY4wPVgyKkj735lNW40+WT6/scNmXL/YiVTaeVTy5ww/Q1G7/q7JVBuqsUgmpD9wwzoHABMnEzqpnqc5gIbmFgBhPXcyYZ6KCalHxuZaah6m7j+pwb3kgZY5Oafpsr+MJum4w+zt0H3w+zb1uO+ncsasPf6ZRqyJ5sBKfjxRvu237S9l1//RI3nzP3XSjzh5gHwlj21qMnEP7EJcCu9WwN6ojvp893A73Lzh7Df73rWj13jby/fEOUZpeeECMhB6X6spq4Ig1QGAsH1I+nAs/+L2fHJAWAgmFwAC8/yUcfGlp5j2QscQTzPRi3KWfg45WKLpe+jLoFRJIngCEUtHQzFMR9fzK255VA2uVgCfo/k/TI1/2jSykN8D1vOUcfFCBTHF8s5iVpL11qQluUCLiRC+i5oE9+XxgBCn6Y+TJv8+DbG3lP1YfFvLzaxAJTCotrQjw8DLw2LPJG2GtrLkvAu5hne2Cly02yXM+ZxS1xDRY4Ze5WZaERtjIaVhy07l2On21lGXfJKuF7SGbkV2ibzeEGUE8VdshxfRvNxm+IO5EIZeKaz7OHKEbfGIQyRxfoYyW8XrcZvpsklUXHtz+nyFKcjl3o3ie0Sv8VwDuajeZLcQkdl9cE1bONwK7fLFJPUSKo3Qri7xUjiEae8Ls/anDOMw1B1XrSLij1ltOntEslx4RaOidnO+kAAngS5P84pvz0mkAQc2YwCIvX+LWH1RjOGqAoJtDD57QaVFkOe1DdR3V6GeRgvuzllbGsnSThjkJ0CscV17oxuX173xlFJXbwZF9edIWU7pjtxKLeIEa5zzDw8KDvjKp0dVC9vTNM4jOnizKaM46YCcIIqfVEvuV5sCA2+mGyZOBWl26uTXkT6+joy1FgqLiOl2u3UHxkiZActtvc8FTBGiEBNciwuNt7zh7Ukr+ucZppKbIm+S715G/j7hBlZtCci+1oIzEF0N0Rg4pJpHPI2gUWtCIh62J5OZ052sDW1O1Sa2J3t4rY/VcKl0Ah3e9FwUwbZg5EOvjeoPGXxE7oxjc0WCY+iNcQ3uUTX/X5+wcYL0bhuN9fPO6Ebo9Qe23PWoWUmra7uPoR6M9uu5NT2TTzdLVxbEW5bzUx1vLyK7nl+6yXOFtWupc71IdVtxmQVn6oMIxbjhbhvwq1ujDzEwlWmNWa09C+HSiYkgV2Ebl+7XH8ObYGM9+n+qC/l3hZv2rVxj6utl+7D+cUQq20eCGctJx0jQQhOyhHRP1yOEAflonsFY0sNZacEotcec/PCGGa2/RVXI0+k6yMcDJyyTmDK2YfZekMqhuLaNodWpnjeEnyllgtDvjKLUkHTVBXEfscXq3iQ0fgwl4o9onXLSCfXyxvsQePGyERf5GmatPOtFrvhcixaWm9xLF4ZO+5wToXSYPcOnSx2Ae9dRb7UdouSje3ARTSWSYdOPTmcvmKtE67x5Y7it0G3w7KqMbrmurAgz+yoyxwLUdVB/BhThTl2FNBN2YVgizCm+21BjaNRV2OspDcUEq6srem5Oc9b2Id23QU5SbW6CVzqZO8wQosWlZFAu9in5ga3FOoqvCn1cXHYjFc03roWlbHMmTzusN5JVGO5qxcevOmW+kpHHILEc2dRDPPTjT21MtY1bL713DLlyMy95tQAwdH2UPSj0uq5hEeUWBEGs5QtTBTQYpuvTOPUCqvY8kql8o5mvlXB/TrZzHU/NrKU1D0R5aRixYqrK7Jvb1aXUkeNqI7JoWEyP5K8+qiH3B4eVposyq4YQKEfCXASaMG+lvPGHPFrlrHwZh0tq5WRxUNGrHZzTLvkPkANlXGCTNVTVzHjbqWakclf0fZQUH3G9wcsPR2YBYvmvkC1VmYcjn6Kxw7hXmxrEKV+WXYp31lqhYLMBwUD0StkGTrzZZ5URrTMMU9eNNkeX5A1tOfXLSbSArcYKFiPzYO9mi/TjHZBRxnc1dg6lS16eY2xbcOP3kibxW295bJSuEpHlQ63gx/1B4pJMXrYImfR8fd1CjshQvCpKOzDfTQO9nrO9TSnMfkBYjaFudExaK2qt9t1kGLztKZXgwY4qWiuhfalHk8k7aKn64JOwq24yIPbLVy1IJxHa+RTA1nYG1oP4LWMIJ2qbzK0FNZ+o3jQ6nLUd3Yr02V3Esoq3fZ1kzmqyepwXm7lFisGp70isG2vBavo57C73G7V1GiZbLiUenLR3Qtisdnoj922qzYNVOFuuAtEVooT6LaF2r6AlaOJUBAMKbeyhUOaujQMl85xXMe4zYGjghApYkuQRYKBN8VVp8hEIYKxk2uMn7NDlF8vKw7hy9s5kKz8phoGqurDXmsZr1Hp7S2t7YgchG6Jr7s5xC66cx9HN3G4DLl09Ey9tzhhmSStkJz2mLsPqtVwQNOLN+9xXVnXuMgYGcnFYmFFBd3IRbtcL7pT4Tr1Fqmtq7zgtidtpBBECa8bmmekTZ9K2OmEOEnTdxlliCN/Zm2WF6wt5DCZvMjEjEGsaE4610gfL9KlGVd4mPcqd1O2N1XLYXLDkDTM0ww7J3wn8OKRXycSL0WbY7mt+ehWXiiUCvH54dhsqXF+uGxulEIYmHtmjdVmtw5UtZUlvsu9jRz71n55FEs6jtYBjRzNk2RharTYHPDusjL0ud9SgiwjW7Y4D7V6GzVuHxxNa2SMYOOuBNDJYicmjrjpCam4PNDxzT2YnmeQxk0j2QIoyWK8R28Yhl5CDGTaPV8QsaQdBm5VLzRjtCPPRKWTVpmsUUnmhV8fPBzFITMtaBaq23V/PcRSkhF0PVoRkh3BRJFyrSx2e6IuY5xbXGUsX7Kbw82jklTQdWjh4f2K6L2xWx0Rooica+jRNxFma7Ta7vIzRxmH1e64mK+OFK9ljEKs3N0pUtfOJs8RlKN10kiN0WOD+V5bc2WGNWSGXAmLlWklzgS8XpPWwV9q84hQVAYnbvR+pHEDzZRTEGR6Up/Ny9RT49yDYb8dvSV8222i9LKrjrUlbJf7xTVA+XBYYzfXlkYeuVFthKlLbz0PJcRUtpBcN8vzjSk1IlGQ0JGkYzzQFzFeX/JVm411fMNPWrdHVGvLRfwt9JQcQG8x+Pq4GBL6wpWXXao6VaGbma5s2pTfbhUrxUhRM51yK4QKoRmipWkLu8ziQtlozfx4SBTN2dzkUNudgw1nDbWgFfpRjzyHtL3QGAWUt7hrMR9FFg0b0ccLWkMSQmOanD/GGQ261Kni1yKxXa3Wl3iYI5pBHPt9l7q+r6eJxp/1ucxWSqP31GlVJ8uID5zzXLI3OD/UvH+p6Sy19eUx9MVsz513ylxeXRtO4s8lD0Ast4cY4nbZsT3EWFIiQXfoYoSVUb534mBHEwvHipsgdF0IXmGYtRavKX5i4muakG46Chs7mBOa2g1Gsg5WBnTZKnRrWPam3NrNNUv2ilCelJsQaV6JtsF6RWGgjfSVJluCKlY5iquInl5RWR/DFXvmieqs7zqXJQ2ECCpXOFi3hCeDxCb7jkmO2DJTsyERN2fB0Ff9UWM3837d2AqDXmjOgpyLK6Vl5uoi6bRmRHSWgGuKH8uZDwf1FYwaDAdDNHlbXMN8B+05d6Md+PoQ62vKlHB0Oc9FmNnoNmTGaNow+vxC42pSJULlz1e3mm2sTma17OTveWw8h8ihzW8GbbMWdThdA3JziHf9nriigyctBNtqocOmV4RM9m1USPuL2Aaa6FRnnp+TxwBfb8X9gLrlzjx7yPJ2lVcyGRTiwlprqMYvtZt1o8zzaXV2+RxMLvmygswNZxyoPRdnCmmY14A/KktRRljLH2yQxNuuiY9XxMtIobzqVldqNIkSh/2RlLecEWckxVj2Ptb6nphzHdxsRpRVmxWq1Wkzx3a1xJJura34zWIktoGYihVKttL6bCqUM81crOcuy+KGs/WOpY+e6B+7nEFOZdAzLWnWgqtJMQ/t3MQaz+35ZhBkv6Fusgp7Ri03clC7jiKdhvVoCSvc5WG9qSMKW6HnddKnZ/XCc60tRcpGR1aJ1/PjElJ06hRCpMJkauXYO4i2Oj5L7HZA6TWPYlyLLylJ3DYaweTpBWUlkqwRS6YRyTKRFYbTzUWAa2IFb1blxoTZWzn34FK/VroYrCmsNRrVd1wkolCI5fzhZFClcbQWTNhgVUmSt0N55Jb2CDsafThnZhu2a3hw9/75jJH8Gg4lI9z4jgBDmzNOWB7kLuKswo+Gxbq15EMin6CFjJ9igPt7dS0yvVTGJcONbVcs6QGXg4MwtCZ3Obq7VeEh+CJSEpKVkn2i6ZtlvB9MMsVaktuNS0wkTEu66lt1cLHc2q86moJOa8WHzhw5Zpm4Gwntwg9cglecTyGSs6tTiqfXOCkS4RzK/KDhIYpYmT0Y6RpEYSlSJNtYgphmA2nofpPvAic/CJ55RrHgsLvx1JAesL1ai7sr4hc5iolIS+Hl0gdbph65JszZpT14tQtX3LJZFy4lQIhgNn613K0Y1D7XdSgxm8FmWmWU7TNWNaNtKWDXjEit1KvkGDZ4Y+IYQ/gXs6HpdmRLc8HvYN5stoFwqMdIVbrYu8GZ6vT8cujhOamGLNggrav26BL8Ygu2ifipjASiiInLKrArH/WZoHO6ExJZ3pIGYzgslJuTJ0ILtFvjC0KTA9hjNaHPcxwqtxTl+Zdqze6xwKWJeTWo0ICke/MSoYywS6K14OCYk6Lr8LDxzR2nXmAMZ2THyAYuo+BNGygiy2dLatF0RI+TlbRTFSyy3RGJq14elcvoFyvUJlJU2QrbmFvYx40Mw2ZQh2gDOqSNAeDjYa9Ya4KC1UYQRD7Dy5XP823ebaBsnyscBTGxh8My10nHeSq7VIclQcUPrUWcbdVH0LqWkyPwycq9pnMz5pXCpUfWOZ861rs2iw3V2TRdKgStw60n1EfAORe6nT8USFs7IupS/t7c5ChhEgeIYveyiyrLLhLCtYWdKk8Q+hL1LJs6pWS5hyHc4ebjpW53l2DvD6DbgI2ip9Ot3EZgFAH7oDPehxy1KJECMQWN63P02AwhMaaYVtTQGoY5aa1wByxzO56AEmnoDiu7j44siyyYeG57cyOGYaKriByNrV1yI/CG3GjtDWaFhZUGp5UW728EpKTZqdPVVu2izEMHgrQ7RWpOFtTKixryEAqx6gsjR6Lk4AG7XDfYgt6HsNplTCkF6ViPV2SD72R/2qa7cuvNMwmdY3NBrSo1PyS5rcLmldwLOuONEdXOZefU77yY9GzlQJ8adrtoavqUyqjNGmdck1BzTo/5yBKmqaxc0656Qse3S1I8ZScXD5T9LsB9Fz/tBHiP2NplLZEsuyXLmkUGFm3OB3ckzdBurW4FNpHj3IS6enEQ9nspk5nkaoT9CVfhXbTSYVwzj2ULtoUlnQkLnFoNQdqPOyWrV2DXld76DeO2N2bt91y4VHFOSDPKdIxlCIBZBjv/hdrIYzHcbB2GAmg9b9FbygQ0Tf/888uHl+nM+Hny+zde5E7nbP/PjvseJ3Pf3gHdz1w9y/10l/Xp7yj164eX0omASo9jzSppgucR4H871Pz4r98eTOuHx/vR6XVVX387Jq+tYPoVn5coc5uqLocvVZ4094PVDy92U02/bVBNejrg58vdsLSYjosfIh937jbU+UTmR9O9KJtewXhuZNXe8zJ4nvJ+eHEHEKDIqb5gBP7FK4vJzufLCGAe+oq8zl9+/y/9Rc0EOiUAAA== -->
