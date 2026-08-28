---
name: "rar-cowork-cookbook-report-govern-projects"
description: "Builds a structured summary report of govern projects activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_govern_projects", "rar_sha256": "03b2e989e58dad79edde2418682422b929c1b9f1ee96f53b6b33fdfd29e3ec49", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_govern_projects`. The original RAPP
agent is preserved byte-for-byte in `report_govern_projects_agent.py` and in the RCI capsule.

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

Govern projects Summary Report — Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_govern_projects_agent.py` and embedded as the fenced Python below (sha256 03b2e989e58dad79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_govern_projects_agent.py` first:

```bash
python3 report_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_govern_projects_agent.py   # or on stdin
python3 report_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Summary Report — Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_govern_projects',
    "version": '2.0.1',
    "display_name": 'Govern projects Summary Report',
    "description": 'Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57acd2619178a5de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportGovernProjects(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportGovernProjects'
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
    print(ReportGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abPbRpLtX8Hc+SB5KF3smzo6YgAS3AliJwjLIWMHiJVYiMXP//0VSN4ruceeno6YGFoyCaAqK/Nk5smsgn57sdsmKqqXLy+qb+fQyk7TOPIryM49aF50RZWAryJxwF/ILfKmip22Kar65dOL59duFZdNXORgOt/GqVdDNlQ3Ves2beV7UN1mmV0NUOWXRdVARQCFxc2vcqisiovvNmC428S3uBmgLm4iqCkaO60/QU3l5x74npRwKt9OvKLL61ewpt/bWZn69cuXn3/59BKD3y9ffntxU7sGt16U+zqr+xrScwkwKbXzEDwtB2BpDq5LvwqKKgO3PD+Anlcfaz8NPkH/8R9JZ1dh/dOXrzn0/Hx9mf5T2hxqIh8oadcNMM61S9uJU6D8K8SlnT3UwE5gd/4EIc7D18fM75KKEvr79OzjY5HX0G8+fn0pgAr2BOPXl5+gogLrVe30+3WSUn786TUtOr/6+NN3OXXrTMZNwoDWr9+e10+xYOD3oXFwX/XvQOrDYY7/9eUH46bPQ+/JTjDz5fVSxPnHh2DgqJuf27nrf/zpr8S6ke8maVw3/yO5Pz8ER77tAZueiv/06Q7yL9DsadC7zL9etgRu/VcsAcPflvsEPYH6K9l3/P9BdBrnfv2O+J+K+7MJs79DP/+lbf/dhE9Q8PVl4acxiGbbSf0v0G/fVEmY//zB+37zwy+/A9H/VIxatJV7l/Ats/M48Ovm27efP9T32x9++flDW4JY8+3sW1ulfybzz3C9r/MHBJ+jPv5xLlhfz5McpDD0HunQb0X5b9Xvr5Bhp7H3/X79BfoxX6bPDJqMeFv0AcEPOVMDXX/A8aeX3wEv5A8Smh6DLP/3f4cOsVsVdRE0kOoWbQMBBzdx5k/Ka1FcQ+DPlNuVD3CtYwDsc9yTqCaNAXv9+p/unRI/u09KhB/M9u1Ba9/eaO3XV0gD0ooqDuPcTiGFk6SvuR36eTOtVFZ+7Vc3wCHO0PifAft8nn5AcQ79+ucCv93nvpbDr3dOjB9MpMw3EwvVbeq/TpacIj9/6u0CLvd7322B2LRwgQ5BDGjzE7CwLtIbYLHJ6jqJ0xTy4gqsUQCenmQDZL5Mwn799VfHrqOv+YM2cehB9jUMBryrA33+DIwJ0jiMmq+570YF9OG33z9A/w/672bdhU9rSIC2n7gDDbfqUYRAHrUZGAZcApwISOKO+2+/PyEFYnJQnQA4cRD7j8kgDhPfe8NXXXOfMZKCHB/gCjDNJjwBF0Nx8wptAuhd32dVmtg6KuoG8vwSVB0/dwcg1QbmvCOZFw1Ug2Crg+ET1Nb+fdVfncq+q5iBhLabX6HDXAK1oUjB/yY174PA5CKPAfzv3n/cB0KqDzXEv4l4hcQp8qDSruwyquznGoH98AuoCW/TgXAbyv3uaz4VP3+C6p4GD3jAIICM+3Tp58nnoGqDIgzK6dva9zH2VMG0eyWrvub1M8TtanKFO8XeAIVt7E3E/7dnSNVR0abeHT+g6STp6QXv6ZV7DK7+ocCrzxbgUZqhry2GoAT0f9AsTMpwq5UirDhNWECCqCnnB0hTGzOB+eh8JnkgUh4J8b2mvzHCGzF+zdMYeLwa/vYYeYf2OeYHIxROucsHfgUgTXLvYTeFUVVNAWt/zd8YGKgM3ekGIA9yFMTwFDpvC05P3zSNQCJO19+r8d1NlTcZDUILKlsnBW4PfN9zbDcBWlVT6jzRBjHoT3h2UexGf7AKAtIB5EA+BJSIAcYAuzt0YgHMBFkTVEX2fXg89ThAC691gbagT/RfoROI/ikCapByoFGZxgAUPtxFQZkPMAYqviNcR3b5UGZqLZ8K2k9f/Ij/89H3aL1rMikPZNqe3QAku4kzPb9/+PVdy6engKrZlF/3SX909tNS6MdC8bev+V3Dd5oGaZtONfYHaCCQLll9D7WJdWrAHJn/DB8QB/dy+vqoiI+S+67Ll//STX/81xrue43T/+i3L1DUNGX9BYYfdemtLL2CnAelyY1Lv36WqM+PZPr8lkx/kPYA5wv0r2n0BxHPQP4Coa/IKzI92seuP0Xq8wMAmH/mz5+J6enXXPG/exYsX2SAxSbAB1AT34vG2xBQOcLKD6fBjyJST7WnA+XuzpoA+6/5u/efmQFIOQ+nilcXP2TsvXoCXz5c9U7u4FHegLW9qa8K/WmnkU7q1/7Ll7xN008vuZ35f73DmHgbhCXAYNqOAIxBd9LE/v3Kbr14AmL6/cct0/H+w06nHCqmGjiR9DtH3pX2KqDRlHRhPFH1JwgoGgLym+zopsSbCr0D7KoBffrepHgzlJOmjx3I1A29t0r/VYN77gLS8YovUwp/gqa29hP03qF+gt72DPfNV96CTdPPU3c82QyGgq/3se87Qsd/+eVP1Hg2y3+txJNXHkxuO1PNmUz8E5uAtMq/tqDIeZM+3w38vm7xWOz3u57NY7v328sbdTy99GztwHCQo5/rqczBIH7BguD6EWng2f+w6XvOAgQH2g8wDcEdzGcZ1icZz/Zo1vc8HyNQhmIwAsMcFmNd1GED1PdZKiBxh3JwPPACD2N93HcJFsh7ROm3qYLHkyY+Evg4i2Kuh1MYSRIsSmM269kEbdsewjA0QgceqAHfpyaAH5/mPcyZsHvvP+/h+bDytxeHIsDINVFvuMdnDrOGTeF7p4/M2UgF582FKbbqvlDJI+KJ2LY6xK3V79cbOhctXj7WoXoihXO4rM9zEBKiddvIvrthVIcdvVyI5od0e5ylB0kgas5p8hHWaRxNhvlmr+zwYxonYxIFqdLbukGyRrYh2ua4PJI7veoHhIHj3je06FCVez7VXSM17Eg47We1e7gd9GtPhZniUnHjOfUJ3Td+LO6MA20JxZzU09nSy2Ij1NWUyMjLdSROEQIfKwPzs4rA/dwkKk2cwcdbeFu2tK7WbrpLLWNutKa9nCuNLZdKVelG7Y6pfA2QxX5mnJZjqi8X21G9GHG330nmYZ+OpcFauyN/CtbW0PtU0hn7pW0WZuTJOa/YnL5Qotai7NOw9WTjcCCvCZHr/TY4m1aVHdelQ9HZyUswuOsac1eKVnWcRxgvb1faOGewq0KlYZ3qxelQUYJWzuV6647JkA8EbNj9rPb8Tk469iTv7TkXZXB0oC/15bxkMb2o57RYLhlR5Xd6pyrGYqT1qzGPZ6bbqMulkfX6LiXL6tRJXT/vNw7vMVnB2L0Xo2NJJOU+TVAqwANWS1hzyAitPBNRqoe5ujxsq51eYDdCEm765dxcChKRFobmdpLQ7vY3ng2sqOnqU76igosRjq26CdzZqBlzQkabc1Ck2rLPt36pXelmtW3Euszns217jbcnZpvIJNxfCiY65HyIsQf1PHTmTOiCXM2ceHmmZYYn9/R8Frm8R+nWKas3vjxzYU894EIb9+ORbI5nljjPcDRyFpZGbqRjamHUUGYEWEq3vINB3rpBoFkxpwghp+WR0SJmuaDnGcUi1TwsYYU5B+MW5DSejHhIHlOxkdYrBHMjNaGO+LkSDDEmEbMpy5uqqlf0FBmVTBDV4nwQQO8EC3ZE7iUFwQ+BbAo2mTXLVRVkCRkll0SXIzdSFs5emye1menpJSGQfofIrcyfxfM1bmP1oi46sxkOw6Za9Ksm0UdBkYfFENSLUjvxndsGvoXPY2ZtwlFxWZXdbLkQ9omsrPVNn1OO19NNwO1xyaaCLVtlVw+I8eK14GhWaXX7m6vBHOWctnSNFIkIn4a9MUNasm4i9qCfWQPl8RWaaUambWZCfFiS+jJclnu6uPX7EV9cyJYpt8yO7sSZcrGE0l4ZKoNInm4Z134nSrsSNocVezv2ybyHK0ywJAmuET3RZ3neGudrH2Sn7V7JTUycX+FqUHljqVz7s32hL5YRxQEaJju2wtXI2anDjt42eCKX0cAqmyzk2MVIhOn22pb8qR9oiaNhZAOvsC6IZPjIOfJWKcr1heTwjdMadMI7muPo1GxVkn2lLsabw4nWUijaDqtsrla3SJepkkQI112qlfiBV3XlfOJVaqVbs6wK5WI/VJfSnV+0ZdwGtzgpvMaH3VkS5mMq0Ett75uolwcqO/KpdVL0Yr8mFnP66tgSuRSvvdmsGGfdqUggtWmE8IiOxSms1HBblEqILgoY5TiK2ZIJtdN9Jr/OpSLp9PKyYk8Fl/flguSTCsO5nXXYb2Pz0ucuF5l7tVe1EL7lNLvPZFsfPc2pQi2hTGelbfbIaicTMXfqZSdlVkyoiZh3One1aecLVSgYa3X0nMoqrwl28VQ1om9iKBBIEcZbLdRsKxCaut+n9pEbuJTblll8KjcJp15sZIM5oVZHJ8Hg6mMqG5tK61eazmLyJfXK1bnfGm1u0sjsaKJjkJaXi3jqvOAWqKpulU7XZ15eq0q02Wpb6nRlpIBWuWsF8nft8+FinyAMm+aLkaSlZbDG4dkSTssiH+KZgPIhdWUYyklSjjt2Z1avxUW2NXhfUMYraezXhlycsxl6sYZKWfqtEFOApfYdX7qqoxmGqs8l9TY/tAq1LE+NE9KcTByHleuZkejyhNFfeW4ukWyj97sDLGykdlYXA9HfuI4furnnOYYolEAOyx5nqE6QGK+yiYx2GzbHFTo2ScfJj23iaKKI+PZgSo0pqWZ7xfu6uc3Fm6eUaui4l+wodNi4wnlTWB3PN2xHaxkap2Or2a7i42cmEVIL2dCIzcGyzJa+lslYMaOPPg3inZsLKHXTGXi7Ohx3p4M5216c80pWaKYaqGTTDmMBS9jmumhJNYysGy3OD7p+lfcmRzLGBlDYKKjzan31WDPmw6hT1l25Iu24uy6ENnQOvVpZV5IlfAbd6Oo1ODYLil3phAKCEREYLifEMvb8GFVOJ2fEmHKh8hGSokNSEOvU2nrXje2iStluGL4mBAUn50wkeax3TbyNImz8DbcnUkfU1qpXb52dkBzUuE9CM+O6Fm3KKImiG4npVbvqD0aFI4wTjMJ6llaaXh1qPhgD6ljq23U5iP1V3Ky1ld8njaTdWp2LIxEZAZHOL2e8GPQkbm+8Epyxcr/0bSrt7LNvFHohMfUgn2Jc4ytu7ilqv1yuWjmLQ6pWS3cjLCtElyU5mqH2LBH3clrwcDLC9J6tEwkljwwmKjEJAD7qsntxZIfD8TEzsbiSdPIa7fR9ALcSkSvwcqV2arLENisy4mEnXpFibMlnhgpnVhxTaGBuy+RIZ74byZcSlaLAqfFYLg9FHSr6LsRpt2vnqyziCg2NMt13dihIf2ctD3LWX85Ig3N67jCsZK8VUDz3zF6w42hcl0mZJq0tJ3Om068pub2CrcjeANXO0814Z0aygo6e5xpiv0W7q52UvRYmYdG1XChedrh39GQ03pKj1Vzrjt8L1qhooE1U+vm1uC6Ycjwl0V41y82Okg0+FjiphePhvLuUiS4co/1C7016n+vBBaEM6XrkqKutGJavD4jR1OglW4bu6bipVuilP4UHUEG1xXG969GNYSBdiW/UOUohMVvuDHGfXVdaR1bXcOCBX210sLlkS2xbjrSvgivUR35FBLaQXaJGYeEOO560Yx53KNdvcZlRSEcT1qolrndEuSku8vKEbZI2NAtRnMMbR7nsQQe5qnhTPwj1DN/J8WrsmxtabDfCETnOPUe5zrhKPO6WFLbcbECzb1xnYbY4aHtTyrK+tjjUGNjZLr3d1txOOcBXcXWbe0Wge1t5vRR38sUEfq6JgzuC1pK9bAYNxW6WUTYDmjpXHjmN6vFsiuaZCRv2kJ0UAe4PxHVz2ZwHxd1ZchbuvbnSHdmkyU1TCwtkE6m3dKbZNrHVjJBrVraqKX2OrK5oXF4rJL6OFlOvA/SYK6ofW/qitiqSt+stJvMcHc/EdZoIxnCcYTDJDQLj1jsLrjdoJuvNJtZJp11Z9S4L5ysNCdLaUPvURsuLXWHcYozLIS0X8WyzCoerc0LmJjY3rIuqiNU8kPNdNs+KICePal7WVQ/i2W0Q63rGxkRHt4iWepscsFB7lPT5TfTO0Zxeoaq0H8Xt2svNCllYlZTNIoU2xC5uixxfKfGii5O0yUZRpAvC89T5iug7qgydrC0w+obP8RXGsOZYFidycdshgjwTLnJHHTOZvvg8dbIRRzK3wm6GKGl9trATekJNYlgBKpHorAkaLWsrhxDsUPfpCm/xY4M5ZXHzUliajSXm5B69GqvbTArPNz4Y+iMjUgxJUnMUva5k8uLuVZhLBMHdOm2VbdZcBq9zS4T3SFxnJFxdzj21sDiJMhYXK9tmHp+yyvLEwWPQBbFydVdBv7vW2I1CvMX8onc3m6Wabk90B5Xu7Jg4zlShIm52NMoL3MtJFHNATT6t+2F1ZPNbnR/wXGbXeXOZMTdRmnFtlrSOPvOwW0DEcA4oVQ6WCBtsbJkIGnQx9J3QoqVuIYIUo4WEndO1lMHEytFvYS5IHEEt1+6OTE8R726wQtDW2Z7kdNnXQ2Yb1keZKJNgfSRrBGlxlz6bRLKLgpPW0vYFd7lAQMPRxWPq5usuqWRbddwjkWU5PD5uLk6ZnsybHPo4aQqzPKGRNYyvDNnB9kzeMFGH545puFFAeV1OBf014Wj/TCoec6HpkFsbC/s8wlVbZKaUE3Wm3Fq/gEXUuOaBONLHy3KReeuU5g4st5SyRcoyywhsyluQmWK/QmjBarplKpy8yDS3qVitMZ2Em6Pn367COiILggBpcGoln9I1nD/IXDojckcKq5xQll3NDcv2rAjrWCNDZthnBd5Ovlvvw/B8OkgDu0QKp0gZv8rsbOPsTloRZpx/A9V4Ny4F3vG3fY/x566EraMAuxZDzFyOQpqV2aXXeL2ETWY2q5Ri8KTuwiNSz9v7UR0Jn+jU8yydc7aAKR3i7/KL39U1fUw6mnJ3FMs0131FsptsZ+KMsj64yHAT1zeMONEHrZXrcen4I7tee7txhxzIm9jqFzvYzwaliLcrv0WGhQk3EstKKLtqNYzEWZBj6OYsk7P5tWF4zaw6ml5k1ZrhAw1HqRUZ8Gpw4w8FPKsHK6atUCTPe78pRMzOEMzjHMu0DAelFfMMNvMWf7maUtitl3i9XVejGy9Eu+N2Yxtr3q06N45+XukLdCWRhbd25PkiYdZrLNQly2Otop0Bh3hx4G6imYy1eH4YecZhb63CqqOV3nCZlNcsewqUovFBB19daKwJXGQxu6pziVqHPrX2HHzRlczcWe8Ppmk5fXxU22hL9/JedtgZD8MLi8e2Ab5w9yt/ljkcIvNVH2kJhxJqK1oulSc3xO2ypUnH4loWTbdKYwkrg8sCWciyJpQq3rswnMe3zWnHyZQ9moTT8mdYs+kMxWN8VmAUJVNHsuqtiMkRHzmu5Us442Da1zcCIDtznS0KD7N2VduMJ7KSmqbBq7I9Bmi/t2TJ3aoHurod0FmuZdw66ph1DxpzQpeGqEwW541ARzt3r50PllQMxXCF9QxJxQtDHIZYXi9os8Gup0XSkun+fMSkA9+n9cqkNeMyh0evRXxugHt+7oNNrnOYiVU6rF0YP5/oWc15VlB7ZlAvecBB40CMcummZ/d0G6ReDw1ppl512iZx59SRfXuEObdYIu64bGD5nCnlrVa43KHQ8BYrunPdb0qwq4wcPvQX6Hhanw18eQm0vCqJowIz/FlBwjVorTiO+/vLp5fpAPh5jPtP3rJO52f/a8d4jxO3txc39/NT0F59ua/15Z8p8sunl8qNgRqPY8k6bcPncd4/HEp+/vNj/mnO8HhJOb1L6pu38+zGDqd/RPMS515bN9XwrS7S9n4Y+unFaevp1X496eOC75e7AVk5HfE+lnncmVb41hTTsCCe7sX59H7E92K78Z+X4fNk9tOLNwDwY7f+hlPkN78qJ9uebw2ASdgr8oq+/P7/ATG61CqQJAAA -->
