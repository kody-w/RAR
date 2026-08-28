---
name: "rar-cowork-cookbook-report-manage-project-knowledge-and-documentation"
description: "Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_knowledge_and_documentation", "rar_sha256": "30d01a53dbd56f64f3e3634d01b85fa192eb43915546a213c5538388778c6f2e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_project_knowledge_and_documentation`. The original RAPP
agent is preserved byte-for-byte in `report_manage_project_knowledge_and_documentation_agent.py` and in the RCI capsule.

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

Manage project knowledge and documentation Summary Report — Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_knowledge_and_documentation_agent.py` and embedded as the fenced Python below (sha256 30d01a53dbd56f64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_knowledge_and_documentation_agent.py` first:

```bash
python3 report_manage_project_knowledge_and_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_project_knowledge_and_documentation_agent.py   # or on stdin
python3 report_manage_project_knowledge_and_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project knowledge and documentation Summary Report — Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_project_knowledge_and_documentation',
    "version": '2.0.1',
    "display_name": 'Manage project knowledge and documentation Summary Report',
    "description": 'Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-project-knowledge-and-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a3545cf2d05ab65',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-knowledge-and-documentation'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-manage-project-knowledge-and-documentation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageProjectKnowledgeAndDocumentation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProjectKnowledgeAndDocumentation'
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
    print(ReportManageProjectKnowledgeAndDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOj1nf2VyGdP2xHMw1iZ37lqiC0AJIACYQkPK4x+77vcvzdc5HUPTOJncRv3qpolpbg3nOesz7nov79xWybIK9ePr2orplBGzNJwsCtIDNzIC7v8yoGP/LYAv8gO8+aKrTaJq/qlw8vjlvbVVg0YZ6B7Ys2TJwaMqG6qVq7aSvXgeo2Tc1qhCq3yKsGyj0oNTPTd6GiyiPXbqA4y/vEdcCVSZ+T223qZo05iYRMuwm7sBmhPmwCqMkbM6k/QE3lZg74Oa23KteMnbzP6lcAxx3MtEjc+uXTL79+eAnB+5dPv7/YiVmDSy/HO4T9Xb3y0L59U85mzvJb1UBYYmY+2FWMwDnT58KtvLxKwSXH9aDnpx9rN/E+QP/yL3FvVn7906fPGfR8fX6Z/hzbDGoCF4A36wb4wzYL0woTYNQrxCa9OdbANcBV2dNvYea/PnZ+lZQX0M/TvR8fSl59t/nx80sOINyxfn75CcoroK9qp/evk5Tix59ek7x3qx9/+iqnbq27y4EwgPr1y/PzUyxY+HVp6N21/gykPmJsuZ9fvjFuej1wT3aCnS+vUR5mPz4Eg9h2bmZmtvvjT38l1g5cO07Cuvkfyf3lIThwTQfY9AT+04e7k3+FZk+D3mX+tdoChPXvWAKWv6n7AD0d9Vey7/7/D6KTMHPrd4//qbg/2zD7GfrlL237rzZ8gLzPL0s3CTuQHVbifoJ+/6IqK+6XH5yvF3/49Q8g+r8Vo+ZtZd8lfAFFG3pu3Xz58ssP9f3yD7/+8kNbgFxzzfRLWyV/JvPP/HrX850Hn6t+/H4v0H/KpuaQQe+ZDv2eF/9U/fEK6WYSOl+v15+gb+tles2gyYg3pQ8XfFMzNcD6jR9/evkD9Ivs0bem26DK//mfoX1oV3mdew2k2nnbQCDATZi6E3gtCGsI/J1qu3KBX+sQOPa57tnbJsSg4f32r/a9i360n10UfjTDL49O+OW5+st7J/wCOtuX7zrhb6+QBhTlVeiHmZlAR1ZRPk+bs2YCUVRu7VYdaC/W2LgfQWP6OL2Bwgz67W/r+nIX+1qMv907bPjoX0dOmHpX3Sbu62T/OXCzp7U2IA13cO0WaExyG8DzQtCEPwC/1HnSgd43+aqOwySBnLAC6nNACJNs4M9Pk7DffvvNMuvgc/Zothj0YJUaBgve4UAfPwI7vST0g+Zz5tpBDv3w+x8/QP8G/Ve77sInHQoggWe0AEJRlSUIVN/dbBBIEHrQWu7R+v2Pp7eBmAzQIIht6IXuYzPI3th13lyv8uxHlCAhywUuB+5OJ1eDDg6FzSskeNA73if9TT0+yOsGctwCcJib2SOQagJz3j2Z5Q1UgzjU3vgBamv3rvU3qzLvEFPQBszmN2jPKYBR8gT8N8G8LwKb8ywE7n9PjMd1IKT6oYYWbyJeIWnKV6gwK7MIKvOpwzMfcQFM8rYdCDehzO0/ZxOVuu8Z8nAPWAQ8Yz9D+nGKORgPANsDcn7TfV9jTryn3fmv+pzVz8IwqykUNiAKoNRvQ2eii388U6oO8jZx7v4DSCdJzyg4z6jcc3D/P58k1OcY8pgBoM8tisxx6P92YJlMYDeb42rDaqsltJK04/Xh2mnKmkLwGMwmeSC/HmX0dX546z5vTfhzloQgT6rxH4+V94A813xj35E93uWDbACuneTek3VKvqqa0tz8nL11ewAZurc2YBqobJD5U8K9KZzuviENQPlOn78y/z24lTMZDRISKlorAcniua5jmXYMUFVTwT0DATLXnVzdB6EdfGcVBKSDaAD5EAARghICvru7TsqBmaDWvCpPvy4Pp3kKoHBaG6AFY6z7Cp1BzUx5U4NCBUPRtAZ44Ye7KCh1gY8BxHcP14FZPMBMk+8ToPmMxbf+f976muN3JBN4INN0zAZ4sp+asOMOj7i+o3xGCkBNp6q8b/o+2E9LoW9J6R+fszvC974Pij2Z+Pwb10CgyNL6nmpTr6pBv0ndZ/qAPLhT9+uDfR/0/o7l038a9n/8e+eBO5+evo/bJyhomqL+BMMPDnyjwFfQKQAN2mHh1k86/Pios4/POvv4XmcfgeKP39XZd4oefvsE/T2w34l45vgnaP6KvCLTrV1ou1MSP1/AN9zHxfUjPt39nB3dr0EH6vMUoJpiMQL+fWehtyWAivzK9afFD1aqJzLrAX/e2zAIy+fsPTGeRQO6fOZPFFrn3xTznY5BmB9RfGcLcCtrgG5nGu98dzoIJRP82n35lLVJ8uElM1P37x+AJoIAmQx8M52iQFjA8NSE7v2T2Trh5KDp/feHQPn+xkymsssnsp3Y4L3j3o1xKoB0qlM/nDjhAwQM8EG/nOzrp1qdJgoL2FuDZuw6k0HNWEwWPA5I07D2Psn9ZwT3cgd9ysk/TVX/AZqm7g/Q+wD9AXo70tzPjFkLznS/TMP7ZDNYCn68r30/41ruy69/AuM5y/81iGcrejR/05rIbTLxT2wC0iq3bAGbOhOerwZ+1Zs/lP1xx9k8TqO/v7x1m2eUnpMnWA7K+mM98SkM8hooBJ8fGQju/e9n0qdA0C7BCAQkYoiDzE0CcyyHID0S9zAXIzEcXLRowjPnDOpaOMbMCQInTXSO2QSB0RhNUxRtkx7qAnmPxP4yTRHhBNJFPBfsQG0HI1Gwj5lTqMk4Jk6ZpoOArQjlOYBRvm6NQbd9Wv6wdHLr+3h8z9yHA35/sUgcrOTxWmAfLw5mdJO67CwpsJiK9Ng6YuJmMHUxnsNbuXXkktRu51Ez2l3tRGUb5LqgrkQpPgws2hikIsk8uVBQ1bNsDl5odiPGBSXfNpZ75txliGek7Y5kLrDBZoeeUh3JT2LHrAfzjN+UXaVzOi5U0krkE9vSj+cx2WWpFnZS0BRNu5W2maiFDQPDJ4SuLqp55jbr3QnRE0I/htZilma8RpeXK6ysGGN9K7fzeTtYp3ZO7vYqkZnCfGUm6gXXvP3lWGc7cQfL1tI3M22A4daqZ3Zm1Si8Rs0WszB8PzjtfJVt3MRgc2N9bm1EUZMqPhJ6Ya3shttlx+0NXlxCO9FZB9UxYVA7bXmY4anVSmpRlg6y7LyUYNFdciu0oL6U++DQqb6PHsP2es01jSzPo+gcdJ0urnJimgPhXC+uJTnR0SSp9OwA3/fI4rItJKPacLS8tEX+Eq4I5hTOrfV1W5xqg+/FTGWD68GJXdMSBsmpeJOhiGFzWHIM2+Qs19ZqR/Z96hKXyJOS7W6FzkzViwqFu4zGvgwKojL0Q+4l0e5U+GWNbgOkG02iXeLX4RpLfolqJ1O6unNzHZMath5Hs9lZHdrc3IpQ9yJS1we0OiyLZboa4u3Ju9R8ei4XXTYgV4oayrwV+CDTFfLWXbIerbLdInKUIB0M32dQMWAy0hhZy0WZgEv2QbezjUtJSdutYxFHJal8hurH+rqTgmWURTgS7rGNSSNrhYaH0ffgVW+lanoJ5Z2m1sOw5U905BzDWbmPPHS13MGo55207W1XV9yN1LQ0sNbemrYIIy9wRDiPJ8I5rQjnCJx7jEczEpsAQ+o2pyJKNpbKAGYfVPQCPMvjru+9gMUHukClNe1WcK+SWUzasFZRHC6HkpmgUuXtpTUneNZeD7foUDtr3jQ1JInLVj+prcnveN5a++zCuV6H0oqjZKUtI5zAq8te98v+Cgrq1ojDuOtk97Igk/ac1Itoq6ajYwqB1Zvxot/Qp+PljB6LFb6u7EiOjz5+O3E7IxT7fRimO5Y8ET0u87sodfo8EkjYvpLmXKRGLE9tBwjPzGjQfM3JCwIbEhKMYLXoHaKdl8SwRh2aU5VKZIDAGxOxfDs3sBRGO/rSncP4kpCaMiB62lnkaYt3+hqV/CN+1ixOtgrifKsGv9v6bd8UFr1y95hiK7ym86o4U6Sehq+Xsy7vCdfkQZhWKyHZ5GsDppCxLkzHklcG73Q54riKgJ63tDNW640y20bgVnLMNFMZWyRXBVDWejb0hBKmY8fFWbo8geuWocr6xeENIkdAGfiqfHXCAz1bWmOwKQAix+1VEfQpZZC7FMvVsGCY+hqrkdEXHmKOAp/sr+bC6YYlyfAVN16dE10LaLw6t9TC4BH0ijtFsI+X3iCejrtMKw0Oz7u+6Vbk5mTMOi28Cdq4a+Y2t9SMaOZ0mnmW0WiFKcxW3M8PHWGbFD0r7M1Jk7Mi1dVzFrooh7VkiGqoppnxpVKCcscgFVUvtl6kzClm1rDLq4Q7c3FrbkiHOec2dpPkfXdUKVjS/TiXCUK6DbBe41vaPMwOlhJ7Szdg4YL0QvJKcynGlQOWcaBMR9DnDqFuOFQRq5oi1JiNHyKaK3khXpDpHlW3IsxSYgnXi9CQY5bN3dhenfZzZF2m1M47sWv+iuYpW1FayAnsONaHlrpdVwkzXgJWltXlWtiFN3F9Wl1JgdhSPUFlwW2h8rpfzXP2jFQRetMQgrwUeI1ckFtRSUp3KUa303K4JHjRLIb5DE1U9XQtLBhgnA0CupASRw4KRYPpQRVpKiplyt7zR5yhGSWsBpgfr97Or/WBhh2fDxP6JK2j/RZltks/9ddAhnkgmqxcoVtWPHb6rWxX+cKrJGdYIeD8sHfsxQZJ8+Qi7JArqh8SWTuFN60LuVIF4YolOZ6xt0DiDNwbdfYQxjM34XXlWC7k4sbZLjNzHVc/Wkw8s5aBMJzUZAhnGCIMInLLyLQXqjKMNq5zbVV+HLGF6RzOlGt6HBG3nrFkYWTGqrQ/p7chk2yz7RGjnOC2DL0kvS10IdpskIXeRRRnnEtNOlkuuUOpdYzXaBogdJiI/ooxu/gQ25m7YzAqp1YucsyRtnFm4cqwEd9oMU6c6dxxcFflSMnSRTTmOg9vdgfrqh9SsqN4yi0d1Q9TLhSKDG2CcRXuTxcT7qt863HaTPZX4tzXh5PJLheKpnDctkmrRAsJouhF/Ty7bXd708533G53EZbxYonLaRjYYaKfzhWF0OJqK5PJJV8rt3m37dXs2hS3q5viUb+RfZ3vOuUGzhNzOWYKDk3FENXdVbPn8kZqCKo41KHmNgS78Q4kgRIzwy3o66xpROuYq2uSYagzVQ+XW1WYZjGzhFPNz6JyLh9LaemYS5VDFmlnXG/z+Y5Y6rjm7vcMreaMTO4TQbDC7akaVhKRl8y2U+xw2aQan1/0ULURlbpKFqtvt2chz5FwfTjxeqjv2pWPCJto0VwVlMqQiDRXEqvEGUY1y8ia47uoOcV2tL4NyTIduZGpNw7DYXKhmGUYqG1Q+0sY6xlCxuC8XAjqdUHgJq5Y6NxC9kd+h7mzMtIO3Aw9K5VkGEQtMo7GpLvYWe7cJqqdJub46OgvLpdOx+KTANg/ZzebpdovWnQ7VzXfovzeh5NyFQelksPKxdh6unRFMxY+lyc7G919cRJzGxRjEYiFa1KLuhCTsY7dVVaIh6IQN8FYu2aMdyWlN9yJEPtjvRKOC99DBPyctIQ6ruvkdknO1sIKJVwIUr+wwZ2VcYDXCsg/0VQZcXE5LQta9Vd0b5yXi8TZh34QHw0z3RmOiPO4KfERGcjylcvOF227IncHtCSH5UHemVgSe5pxjta562uDFF80N6ELe39cD9iR25yRSy2qrbEmq3ZdB31R5za5T+v9Od5yMj/zmZYILqKwZKWW3xS7XLhcvK5nHKwei0PrZKJA5C5m1MO4yWUzju19YlxxVnfSrebv5pt0MGMJO2zUKlvO66YUw4O7wxM/kmhMCaLd1ScRtzxcF/NkuTO4mU7idH7t8cjak8HpZNPOCrAq0cYu76vleoOFqXUbwLBzwALvmPl1IRyX15OIIAoZjzax72UVYxas6J1spg20XVbJ/Hl5gOXjrU4aqsn52kDQ/gDmkotzXnmoiAAVBXdm5yUb+sfL1pLbFhk04TgG7m6fInNQchXLlZLplw2C5pJerTV+UYQr8kZcUbii5WjFsLf8kh+rYWHKyzrgDrcVXEq7Hd75TlPA47AR+pGuKBlhzmvpGnOJmoTMNo1NjxcM4dieb4Cot0waSSe3Frv9utCdq3kOD5i79gxsQ5I9RxVzNlIHvjJvxqos+QAXYwY1K8FmR+MWLcYAjMa6gyRHWUfAOT+YwwLhlITabmYctUFVRbtJ4trJsgpZmpWSjuGC0tdD3OYYtjqWSyYsk35zkyRKwB1H5TZ435OFv0vLHKWOGY/tSNpJvIK/mUe5bjVrl9OgelutujmLFe8riC1HRbbFUz9IUtjATsuB60rLPDM5WZiDNdRXL58luAMIpp2het9V25LJ8nJJ0+3WKy9l4zCsl/XEmeHIbNHX1NVeoMvsILqoQ6wPkSQ316CleRF1MQ6Re0leMNyZCshkQaQYTlOyN5ireX1R57q4GQ8WzsySA46O6m0WqHAejouO6cZ6cywFQNpzx2i8FKerNZ8frZSaX7JLE3kCvG6jwaMV3eOceSqxV6ulypE2ERntO3XZU9xlreLkbLamZUVczRTP8+qTkq7m5mot9R5MeDB/6Ptlt0aYbmfeDkWT79fDIu/mxnU7R3ifIEXpsGRce0cf2i25UfBNP9AbdpXAYsMJtu/s5UxhD0hP+3SxKLWAtYNWU/CW6xuk7zC7MqK8lQ5VJmJykNM7lrfSeuNmdFthCS+fjPZUj1K8BGm4ZYxdShpBgu8Fnpjpg9IRG3hhS0xy4piwE2FPsEUC1ecX4cLcbGOW7M/Hg5dTx007u3VNx7LGSSIqOWjPkUlb69zbHSvZKTyDuIDpHouigN/6IXleoqwRciJFKyqF84tcvrnwdTS5pKIuTBDutixlhZF8o60LRme3S7khXOogdBZzIKKiMxQctohDU6/mHJtRlV6jbNsF7GVEOOFMjEJ2OnSbChVmbugSJlwtfIRj6iFwvbxd75yVXs1tzR5Wa7V3VvtRQvOVsnBNxF9ag+F6rMymcM5vz61M4y3NEQV5aHwG7LPGHCdm5aKnXcW/LREe8Zs1kRs17BDF3gWFV6/O1x0im0nUMlLNc36P9ddtOcASyZd4tI/3PDU7Xlj1NOuUil44FBMN2PV8DZnuit6ythBDa2PfMsxc1FiG1TF30gQKHLn2MhwXURe0bW4RioVVxZAw+QEPBnupGniYj0OPb4bAp2icOWY1zxrZ7tqhSlpeJQOvNtgu1/v+zFsHp8okP6YidO4S0mlOGY6JCbV0IPCtgLthuJ5FEi7ifdWvcnelePJ2gd1kVFwdNqdotupaG5c34YYPyL0i7su21KlD2R+VTkLkBvf5gLcoyvd5bJ6dvfkJNgljjs3AEWSOMWSC7PFa8hK3r/lz7iJKffB8mGOQiLGoXb+dMZKvk9KucfHiIl7U1Qz33YpSPL/r5qfjstWZJeUN5y7fLHSe3dLX05GV3VPUXS6rHUHNlToyC2fYRHlaNevtbEmdupuHLA8HjS3Uy2DDMDZmwnY7HEj1dvEsRyDIeI6JVadn9AYrSZuUZvXCPK6pms73csAfaRZG6eJgROmcVg15uJmxmZJYY8V1SWKYOybUlaqiFA0WuZoY2QE2NELJbFZeBnC7drwTOD6IKE3bLNvYgjY4Jlvt4RoVym5YdEZ2WsrR/lIkMc7Pk/ZmFRcw7YBzHGNgsTLM4w1GWZc4xHpnRpesSt0YpOgvKGkuLR7MFg1gkeYGBnUrlnXMkk8Zz94We1PCTkaSC4llE7XuLdlI71C1jEFEMtA1inktK6yTi713myfE4VpqBTjKsZlFhSwGH4XL6XwEmQ2zqODjMxKL4j0J2rITzVH3csVn/kwQjxqqc+Bcw/7888uHl+lZ8/OJ8f/7l8fTI7n/b08GHw/x3r5Zuj+tdU3n013Xp/8Fxl8/vFR2CBA+no/WSes/Hx7+h6ejH//2VxSTuPHxje30FdnQvD2Lb0x/+v2klzBz2rqpxi91nrTPHVZbT78dUU9W2ODny93stJgeQz8QPK7cLWzyaZkXTtfCbPrax3VCs3GfH/3qDYczgmiGdv0FI4kvblVMZj+/8QDWoq/I6/zlj38H6XXfTAYmAAA= -->
