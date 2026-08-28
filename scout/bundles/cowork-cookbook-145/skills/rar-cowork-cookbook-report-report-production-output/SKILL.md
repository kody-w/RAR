---
name: "rar-cowork-cookbook-report-report-production-output"
description: "Builds a structured summary report of report production output activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_production_output", "rar_sha256": "62bc3cfd8fd80558e3b4af74740d4054da7a7dc2b7b99c6bf1df24a0eca3f11f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `report_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Summary Report — Builds a structured summary report of report production output activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_production_output_agent.py` and embedded as the fenced Python below (sha256 62bc3cfd8fd80558…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_production_output_agent.py` first:

```bash
python3 report_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_production_output_agent.py   # or on stdin
python3 report_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Summary Report — Builds a structured summary report of report production output activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_production_output',
    "version": '2.0.1',
    "display_name": 'Report production output Summary Report',
    "description": 'Builds a structured summary report of report production output activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '745bfebdd5536d9a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportReportProductionOutput(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportProductionOutput'
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
    print(ReportReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716a5ObyJL2X2F7P9izsps7knziRCwSCCEBAsRF0njCwx3EVdxh3vnvbyGp257dmT3nRGys7G4JUZWV+WTmk1lF//ZiNXWYly9fXo6elUGclSRR6JWQlbnQOu/yMgZveWyDH8jJs7qM7KbOy+rl04vrVU4ZFXWUZ2D6qokSt4IsqKrLxqmb0nOhqklTqxyg0ivysoZy/+1TUeYuGARmQnlTF00NWeCqjeoB6qI6hOq8tpLqE1SXXuaC90kbu/Ss2M27rHoFi3u9lRaJV718+fmXTy8R+Pzy5bcXJ7Eq8NWLel/m8Vt+X+twXwpMTqwsAKOKAZiegevCK/28TMFXrudDz6uPlZf4n6D/+I+4s8qg+unL1wx6vr6+TP/UJoPq0APKWlUNrHWswrKjBBjxCtFJZw0VMBcAkT1RibLg9THzu6S8gP4+3fv4WOQ18OqPX19yoII1afz15ScoL8F6ZTN9fp2kFB9/ek3yzis//vRdTtXYV8+pJ2FA69dvz+unWDDw+9DIv6/6dyD14UHb+/ryg3HT66H3ZCeY+fJ6zaPs40Mw8FzrZVbmeB9/+iuxTug5cRJV9T8l9+eH4NCzXGDTU/GfPt1B/gWaPQ16l/nXyxbArf+KJWD423KfoCdQfyX7jv9/EZ1EmVe9I/6n4v5swuzv0M9/adv/NOET5H99YbwkakF02In3Bfrt21Fm1z9/cL9/+eGX34HofyjmmDelc5fwLbWyyPeq+tu3nz9U968//PLzh6YAseZZ6bemTP5M5p/hel/nDwg+R33841ywvp7FGUhl6D3Sod/y4t/K318hw0oi9/v31Rfox3yZXjNoMuJt0QcEP+RMBXT9AcefXn4H/JA9WGm6DbL83/8dEiOnzKvcr6GjAygIAg6uo9SblNfCqILA/ym3Sw/gWkUA2Oc4EP+Th+/M5UO//qdz58jPzpMj4QfBfXu+fee5bw+e+/UV0oDYvIyCKLMSSKVl+WtmBV5WT0sWpVd5ZQvIxB5q7zOgoc/TByjKoF//geRvdyGvxfDrnS2jBzepa37ipapJvNfJNjP0sqclDqB7r/ecBshPcgco40eAUD8Bm6s8aQGvTThUcZQkkBuVwOgcUPkkG2D1ZRL266+/2lYVfs0eRIpDj3pQwWDAuzrQ58/AKj+JgrD+mnlOmEMffvv9A/T/oP9p1l34tIYMCP3pCaDh7niQIJBZTQqGAScBtwLauHvit9+f2AIxGShgwG+RH3mPySAyY899A/q4pT9jJAXZHgAYgJtOiAJ2hqL6FeJ96F3fZ7ma+DvMqxpyvQLUIy9zBiDVAua8I5nlNVSB8Kv84RPUVN591V/t0rqrmIIUt+pfIXEtg2qRJ+DXpOZ9EJicZxGA/z0MHt8DIeWHClq9iXiFpCkWocIqrSIsrecavvXwC6gSb9OBcAvKvO5rNpVFb4LqnhgPeMAggIzzdOnnyeegsIM6DQrt29r3MdZU07R7bSu/ZtUz6K1ycoUDigBYNGgidyoFf3uGVBXmTeLe8QOaTpKeXnCfXrnHoPpXPcDx2S48B3xtMAQloP/LxmJSj+Y4leVojWUgVtLU8wO2qfeZ4H20S5M8EDuPFPle999Y4408v2ZJBGKgHP72GHkH+znmB2tUWr3LB54GsE1y74E4BVZZTiFsfc3eWBqoDN0pCVgIshZE9RRMbwtOd980DUFqTtffK/bdcaU7GQ2CDSoaOwGB4Huea1tODLQqp2R6wg6i0puA7cLICf9gFQSkA+yBfAgoEYH0ANjdoZNyYCbII7/M0+/Do6kPejgGaAuaS+8VMkE+TDFRgSQEzcw0BqDw4S4KSj2AMVDxHeEqtIqHMlM/+lTQevriR/yft77H712TSXkg03KtGiDZTXTqev3Dr+9aPj0FVE2njLtP+qOzn5ZCPxaTv33N7hq+MzhI5GSqwz9AA4EESqt7qE08VAEuSb1n+IA4uJfc10fVfJTld12+/LcW/OO/1qXf66D+R799gcK6LqovMPyoXW+l6xWwAChfTlR41bOMfX6+fc+qz4+s+oPYB0pfoH9NtT+IeEb0Fwh9RV6R6ZYQOd4Uss8XQGL9eXX+TEx3Jwr57mKwfJ4CgpuQH0DdfK8nb0NAUQlKL5gGP+pLNZWlDlTCO6ECJ3zN3sPgmSKAr7NgKoZV/kPq3gsrcOrDZ++8D25lNVjbnZqwwJu2J8mkfuW9fMmaJPn0klmp94+3JRO1gzgFWEx7GQA6aGnqyLtfWY0bTYBMn/+48TrcP1jJlFT5VCYnHn9nz7vybgk0m7IwiCY2/wQBhQPAhpM93ZSJUy9gA/sqQKyeOxlQD8Wk8WPbMrVQ7/3Vf9fgnsyAhdz8y5TTn6CpF/4Evbe1n6C3jcZ955Y1YKf189RSTzaDoeDtfez7vtL2Xn75EzWeHfZfK/Ekmge1W/ZUliYT/8QmIK30bg2og+6kz3cDv6+bPxb7/a5n/dgj/vbyxiVPLz37QTAcJO3naqqEMIhjsCC4fkQcuPevdorP6YD6QKsC5lOY7eCO7y7Af4QkFx5uE5Y/J+YE4hIISbjW3Jq7DmbP7eXSoWwfdX2MsBDPsXAfRX0g7xG236ZqH00qeYjv4UsUc1ycwkiSWKJzzFq6FjG3LBdZLObI3HdBdfg+NQbM+bTzYdcE4nvTeo/Th7m/vdgUAUZuiYqnH681vDSsuTm31dBelpR3vpyWvB3pN/uSN0YSt1QZHqR4ba+2Gyxa8EbDSsOORaVYGbb1HkEZWQlnubqMrzg+tiutKuQmDyrkuN7bIi5nY4sQy+UQyuLCbg2DNAolEuZ7IopvbnHcl0PZ3fpTiuJOEe2WA3vC4ZmqDaW74m3+rBdrZGjWoS4Q1Nlwkxt2y2ArGa49RuqNO9tZSV+rl5shjpujHurF1RdzZJNyIcmZzsnyuS2BHk5lT3iwHZESfpFmQoXaDS7D1wjXrd2erYVE350NkxqC27Gu4r3OYSi724oXKj96hO0cY6py0uhGbo86JeyZRB/rvlAlQ5vFDunhO7M/t66V7ze3WjjNu4q3g7wWhZWKNheq0IedqxgGlXeukMfRQPVNNQDMIwTNxOt4vszCMW2MdakdxQ2tGzbrHmg1S9wwjw69HuWHy0nZZUc6vGSHzLRKPpcce2uiFNlzCrOrmTqn102lbV3lprVO0bWZUhuxidlH/1rI9K7pJMpOjqEvb5dqYUW3DX9VCiNGR2Xb97ORFzZGxSELK+hL6brH01Tb7KwqzXxsLt38zOpO2qAKdkXfYpHQdubuMrg0ZhdzjqpOZFVvD01wLmxOIqjCWzruSFV1Ra0RB9dYs0pRTL0uM+w4rFaN7SHhMTEqxnGNvJYEfrQvRpnkgTsbb3mg22ubPfjweS/wStHH/pLRBCGWFywpjTtD7umkzk1+kTA3T2m6yjVSw0zXMg+zvq93Tb93Wkc42GO0cjm7QPyLW5FEvM2Gqq+JanRUsoJF8HOyMlOh2x7rtfKYMWrTr/0ZAS/U/koasbfPa3kZqMbhsljO0i22U84rlkLDKjPR5OZkwDPbJuTjfXZx01O82JHbwr0xhsTUAdxXM3XRV+IZFQf4FvZt3GystazVCs+n+0HLT4qzuBnoxhicIokLhrePbNJuuUYwnT275VbVRrlgtnJcH3oP45mGu1j8oVuE9nqPHb0RjdyDPq80DyX2pbPPZ4e2NOq0NmaO0Ak44udRJRDnBj4dokiL1strv4ALsmQxb9igygAv+YTDzD1W6zu4hEHxR9dXe23Jvr9JZXSW7BvGuPjX3Xbc+Jq3Ol6EfbIr5dXpWjE8bZoyX4XsjFKTGX44J7ChEOfZ6sLXh2DcdcyGwY97z0Sjq74uZXJ5tcMxbkTX3hNXdhxnVJyCjfawcOlikwrwIQoR92YfUt0Plzsl44KEL+XreXBQsEPe7OS9pM1B9O5X69syL8Saw/ykWqvDajDXWVb7OjVKCpYgl5VMO6gIs+bM2jdrwZ/HR9ZRrMqAZ2uEk3fr60DXJTqQrhBTnqOywW6HdYLpabwdxyUWjxumFC/EdUaFXFSwQzUWmyBK+E5oj8UyGSznbDCgNiBSsLaEhd+7upUUB8zOVuMNC5tbMmYhfCqQTTAPSFEQb2xREvQmxDbLE7bW+2NpZu6qZxBCymUbTtXZtle8wAk4LprH/W594sRax+Q6OHHH3PCpeLWM0M2ZSMIOL1OH4ZfmmT97iJ0F/LmREYMZ54pJa1rD59GYRG3WkmPq3/TeDYR6Pwosiq0XiiWuXQbhD+JmU8WDsFjJJ2NzGbmh3qeygvI5f52XNKNKvEntq0E3Jc2haSxhWU1bXSX6hvccU2nn0yYUg0JngiLjovV+xTqoTdj12ONqsb4Vq+UlWFkW4YK0OXjazA3j3BgPTbvASC+7UPBhxEpRVIsMlD9cjxNub84GSWqboxYoOq7lnob78CKm2wNBXRuUoZETn82XC/ZG6pzoytl1nO1bSnD5bbTJYmlohX1K7hi6CtgDyu8VErDfFt3Q++S071FjfV7V1XmWRrqyKhWxCTZnYaGAGrGW7Vt0zFY3lVTR4YBKIlLqW4+7rHC1CkEU4IF8jIaSUa/7wGMpQRzSpcm3zSjmRdFbEu+ognmy58lAMBgs9elpvhH3+W3FwS0XmWjpnIVMOBi4RdVybEdzgVEWUu3HChOvucA6iYVOHA+Avg/8bqwa7HwjzueuD8IMlqtdst9J+qbu89auTLWwN8L5EK8u0WYzHiPyUBxwxihndhS4rCUJpe/zIafXPOdWXSRdj8F5i+8Xh3E9j28Udl2GYrwQNse1ycFSfqSShFsVPMCwOZLi4Vwp58IyWmqpV0fJSemdS91400gjtJPr45Bh101pLQhvgRK6GZ24hLVcXp/3q7iMN4K8IjhVVVoV1HNJyglPuXbMSs/QLiUIPLn0Wq4tyHI1iga52rukvnSvzWXeeYWY1LzBminP7IgEYLW91LEjJsdhlxDmoLDuap5dsiIirkFLpkbRcD2r2wa2sD2QqrN4rqFcb6zrCEZc83aUtcS+KpbiRWt03GGHpHRzNVzbZLaULWm7g9W4WK0c75jOFDxI1wUeLrqO95KzTq3qc5wZbIMxasfOKiPieUkMZZYdxGNy6Vi2JGp+W+Y4oFWLLeQKoReWJcMOy5EEbPsZjVTVRrtUtNMIfb1THDe/msXN5xcAb0eWtSWOwF5jWl53FLkdYRE0ilUWHChbAWncuigMR3STjFymjjnHfNNp1fCcKUWGzVHPuK1P6nmgzyV6a3By1dCVwXOjYmdSae+Og1gHPl8RkcAeigXir2aXZtRnxaUvefpEVeqg7bohUVJHBQ2Hksfx5Tb3qmKXDlXssadid9pdjhvG9kVp158MNKfoYtASRq0OypCdtyYZ202p5xbJLkjURBlncwHZj8Rz4Yzk5m2/vs4shSh4B0lu1qohdgov8RxJ0016lc8XdEfnewQXU3E+Dlt4MWO2xpYEhQOxRgqQvrptUMyk7VVo24V4pex9d5aOmT7u15KxoE63MoyCdDvfdAMeFaFglHzNph2R7NZUboZiGqzWDecHblQjvRJw+KbUk5gWChgnpJN7FW9cGRPD8WDZNWaLTnhjtGK33ewMQ6SNU5HGxBo0R9W6ShpKGvTl2Su6Ag6YlSAvx00X5pXtUoOyX3H1MshM3d4Fe1JLkN15CFcsrsVWm1+C5S4u867WiUPQ64OH0w6OX4ONzJU5dj1hkq4c93l7jcKYV2/R1sGcS9dTQ+06HXVCt7KdG9olGpZogMhj7Mx3tm+tVzbnSiK7hxcbXA25Wjku/P1NSQLhQquKYMez7HBKuiKmC7/dDKplLXZaEq8M7qLoHInqXINEIImQcO1eKsduqTmT97KypjYUay0U8xrMeSUWe5m6UoPJEIJt+QtRjcRDu2/GWt6Emk7SsV6c2/2l4LLVwB1ZOxFRs48bXE1vssniEYNQt0rSVN5u10VVJtua37jILVYLYdO7u/xqGEzv0IM7l9T4oFh7FDSvIWNbx5pIFM9EIucYojA7d2+4Ai/0i7/1mPl2U+xucdTAnXHcVdJpqSk5fIs600KiZUC7G6LvTfRa5JlbWTpoy9YVSD294wa0ch1n2S5w5rShRrsvkOIcGehiMeKil599rUiEMxdckzS8oPq6X7QhT5liThVWbYOiIVva2cMNX7SzJilL8mAFqjxbHBiT2jaJa2x8nCZPUjpnV3k15zsJHbnz3lurlHbCR+1qAKe7wzKq8UyFV0W359d4jetnmU3hbXZBYYGIqoji6uQ8rBmb9pHblkO00EbkE5YI/Boe3U7udRQTJCIxbBtHzx4DmqqujZZU3QlU58R4iHdBWc+jNpndtC2NSJibnNx62Fhn+ZoNHpoE+Vz0QTBdVVyFYc/IYNoYj6ddRLf2SV5ovlYR82K8Ul6WSrtKRZxieSask6WbnOVxRIMFDIJoGbB2XpttkLGywHMo4+3JRA9XdYdVyh7kyBK0c1tjIy7miyDzZ5aWL4mhtflyg1eNEGr7o1lsVeKwlTXGFnfruTNm0mGR92IhRW5+1M1TAmua1A+jNp4DJhzmjWWKLrwg7HlZ9hTryeQiINSxapsmuJEc4c8FHgvp5gQaCbzlvdZmjr3CmTOS292EIkT8aHHZzkjrCp8M6+bCJxk+n1vQ1lWZsx4QWsfOhwzHk62ybC8zFRlZW0Pak02brAqaNstJz1ibXbzTDLHQBZafDtv0OmbbapRJcr6m/LPayHQ76mVCEkeYuzSbkFTqMVIPXeylp0xd99vl0MP66AbsdhUwVau5c4rYaQIwoIi2UZFR51VgV0oqhMdz1QlWf/BceibGsCxszWY/I2YdQxLcsW4Fj10ZfZ6TcLkilrOGF3DYrxlCM3PzguEc0lA2q+PBJtwFTn1qshwPtHE15lVIbdezzNFuETFTFkJEJkti13Posu0GzLe4rbt0o71JXMHWLkeoPXbJPKcG/VVzWfYrgtxHe9Ygl0UjOewAo93WN2qnrm1pRh45ZO8MrhEEN5kGXaLFcW3e8bNMzg+b/WyG+MZJMjpO6FOpxjo8aUVuOLrtRgoq6mqiPumekfnFOONELiokIvC8dY1QKpAIcduVHccfFnVrN9ly7teRyq4SHp5pZHLYEZiSU7K66ncJjiotpZo0vyywEG1ZGtnP/cuMCWaLmprDyOmqCU2ztLZJf2qXZzOAw84YNvMj4VkeDFrw5dJfMKgKj1UIMwWZUuIpX1SjXWTVxt1odsFQfuvP+tkim7ESWc5Y7BS3vnqk955onoP0CoKpPKVxlS4XGBugHHrtA+lkH/ALkyxORA4zLMJ0lhK4p1OPIDC+jnjroCsUNjspMtjoOBGK90W2aY9cdhhPNxjLVdOey/SYO1jLrxbyzGTbcOfGmNM4h1C4pKC3QyWhqSlsgXpYQxHzOlxLR7qSLHkungzSCgzMka95LkTpLut5PN2m9OYarJttriRSwKRLzjjo16V5OYoUPa4w8xgoMwOQcLwaTu6A5oes0VfXUh7aNG23RhvMl+SGTkChQG7dqZcsRtjuiqYmGmU5DoRTDzI/rzNe28VSp60BYRcgjSqjTtpZQe+3VIH0CM4QeNRtU1dsVkTH1BcOvmBBvb8ymhv36w5ZuhmxXlAFSzEdk0otqXeez1BkFbUVaApJ95qi7jaX51g+7je3PU3TL59ephPh57nuP/todjpI+187z3scvb0927mfqHqW++W+1pd/WqNfPr2UTgT0eZxYgpYkeB7w/Zfzys//4JHANHl4POucHkD19dvZd20F01/pvESZ21R1OXyr8qS5H5h+erGbavqbgWrS0AHvL3eT0uJ++nlf6HlE/K3On1Z4L9Pj/OmRiudGVv12GTzPbj+9uAPwSuRU33CK/OaVxWTi8/kCsAx7RV7Rl9//P3v2Dh34JAAA -->
