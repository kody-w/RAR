---
name: "rar-cowork-cookbook-report-define-environment-strategy"
description: "Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_environment_strategy", "rar_sha256": "7431b271b1d4fdf23e42c6d9a3c5575991a78b9b1c9582eb41685a710317653e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_define_environment_strategy_agent.py` and in the RCI capsule.

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

Define environment strategy Summary Report — Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 7431b271b1d4fdf2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_environment_strategy_agent.py` first:

```bash
python3 report_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_environment_strategy_agent.py   # or on stdin
python3 report_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Summary Report — Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_environment_strategy',
    "version": '2.0.0',
    "display_name": 'Define environment strategy Summary Report',
    "description": 'Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '799c1948dd607dd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineEnvironmentStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineEnvironmentStrategy'
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
    print(ReportDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aabOiyJr+K86ZD9U9VB12kLpxIwYVEVRUVqGro5odZJVV6On/Pol6TlXPdN87PTEx1qJI5pvv+jxvJv76YrdNVFQvn18U385nvJ2mceRXMzv3ZsuiL6oEvBWJA/7N3CJvqthpm6KqXz6+eH7tVnHZxEUOpi/aOPXqmT2rm6p1m7byvVndZpldDbPKL4uqmRXBzPODOPdnft7FVZFnft5M4+3GD4eZ7TZxFzfDrI+baNYUjZ3WH2dN5eceeJ8UcirfTryiz+tXsL5/s7My9euXzz/9/PElBp9fPv/64qZ2Db56ke9rru7rcd+WU56rgfmpnYdgYDkAB+TguvSroKgy8BXQcva8+qH20+Dj7N/+LentKqx//Pwlnz1fX16mP3Kbz5rIB/radQNsdu3SduIU2PE6Y9PeHmpgPnBH/vRNnIevj5nfJBXl7O/TvR8ei7yGfvPDl5cCqGBP3v3y8uOsqMB6VTt9fp2klD/8+JoWvV/98OM3OXXrXHy3mYQBrV+/Pq+fYsHAb0Pj4L7q34HURxwd/8vLd8ZNr4fek51g5svrpYjzHx6Cy6ro/NzOXf+HH/9MrBv5bpLGdfM/kvvTQ3Dk2x6w6an4jx/vTv55Bj0Nepf558uWIKx/xRIw/G25j7Ono/5M9t3//0V0CvKrfvf4H4r7ownQ32c//alt/2jCx1nw5WXlp3EHssNJ/c+zX78qR2750wfv25cffv4NiP6nYpSirdy7hK+ZnceBXzdfv/70ob5//eHnnz60Jcg1386+tlX6RzL/yK/3dX7nweeoH34/F6yv5UkOqnn2numzX4vyX6rfXme6ncbet+/rz7Pv62V6QbPJiLdFHy74rmZqoOt3fvzx5TcAEfkDm6bboMr/9V9n+9itiroImpniFm0zAwFu4syflFejuJ6Bv1NtVz7wax0Dxz7HgfyfIjxpDEDtl39370j5yX0iJfwAvK8PtPv6Hdp9fUO7X15nKpBcVHEY53Y6k9nj8UtuhxMiglXLyq/9qgN44gyN/wkg0afpwyzOZ7/8c+Ff73Jey+GXO2zGD4SSl8KETnWb+q+ThUbk5097XAD9/s13W7BEWrhAnyAGyPoRWF4XaQfQbfJGncRpOvPiCpheAFifZAOPfZ6E/fLLL45dR1/yB5ziswc31DAY8K7O7NMnYFiQxmHUfMl9NypmH3797cPsP2b/aNZd+LTGESD7Mx5AQ1E5SDNQX+1kOggVCC4Aj3s8fv3t6V4gJgdkBqIXB7H/mAzyM/G9N18rG/YTRlIzxwc+Bv7NJt8CjJ7FzetMCGbv+j5JbELxqKgbwGQlICY/dwcg1QbmvHsyLwCpgSSsg+HjrK39+6q/OJV9VzEDhW43v8z2yyPgjCIF/01q3geByUUeA/e/Z8LjeyCk+lDPFm8iXmfSlJGz0q7sMqrs5xqB/YgL4Iq36UC4Pcv9/ks+8aM/uepeHg/3gEHAM+4zpJ+mmAOSB5wNGPdt7fsYe2I29c5w1Ze8fqa+XU2hcAEVgEXDNvYmQvjbM6XqqGhT7+4/oOkk6RkF7xmVew6u/kE/oDy7hweTz760GIISs//nPmNSkuV5meNZlVvNOEmVzYfzpm5okvtooCZ5IIMehfKtB3hDkDcg/ZKnMciEavjbY+Td5c8x3xkks/JdPog3cN4k956OU3pV1ZTI9pf8DbGByrM7PIGIgNoFuT2l1NuC0903TSNQoNP1N/a+h6/yJqNBys3K1klBOgS+7zm2mwCtqqmknp4HuelPvu2j2I1+ZxXwcwPcD+TPgBIxKBLgu7vrpAKYCaopqIrs2/B46omAFl7rAm1Bu+m/zgxQFVNm1KAUQWMzjQFe+HAXNct84GOg4ruH68guH8pMHepTQfsZi+/9/7z1LYvvmkzKA5m2ZzfAk/2Eq55/e8T1XctnpICq2VR390m/D/bT0tn3xPK3L/ldw3coB+WcTpz8nWtmoIyy+p5qExrVAFEy/5k+IA/u9Pv6YNAHRb/r8vm/NeU//LW+/c6J2u/j9nkWNU1Zf4bhB4+90dgrwAJAZW5c+vWT0j49CuvTd4X16a2wfif54ajPs7+m3e9EPJP68wx9RV6R6dYudv0pa58v4Izlp4X5iZjufsll/1uUwfJFBpBucv4AOPSdWN6GAHYJKz+cBj+Ipp74qQeUeEdWEIcv+XsmPKsEAHceTqxYF99V751hQVwfYXsnAHArb8Da3tSThf60YUkn9Wv/5XPepunHl9zO/P/RRmWCeZCtwB3TBgfUDWhymti/X9mtF08+mT7/fkN2uH+w06m0iokyJ0x/h9G7/l4FlJtqMYwnZP84AzqHABMnk/qpHqe+wAEm1gBhfW+yoRnKSenHRmZqqt47rv+uwb2kARZ5xeepsj/Opu744+y90f04e9t63LdzeQv2Xj9NTfZkMxgK3t7Hvu83Hf/l5z9Q49lz/7kST7h5ALztTBQ1mfgHNgFplX9tASd6kz7fDPy2bvFY7Le7ns1j1/jryxuiPKP07BDBcFC6n+qJFWGQymBBcP1IOnDvf9E7PiUADASdCxBBEzjqYDTqoB4ReAGG+wTmUh5j4y5J0iTDoDY9dxgHdRlyjvkOgVJz0qZRBEdpisR9IO+RvF8n8o8nrTDbducujRIeQ9uU6+OIg7s+iqEejfsIyeDBfO4TwEHvUxMAoU9TH6ZNfnxvY++p+rD41xeHIsDIDVEL7OO1hBndpvCdI0UOVFEBW1+YpLlt9VJC/fSoHzZuIFpXS9rjFna4oeceERJxy2cKa4aOUTOgoFYMm9PisfVYmI2V3FFwPz9Ih6OxDzl3I447jyZW2zBe9ucDioiJsq06RaxhYxu3652J1OhZuIzXDjXKq3RYS2snqW7YAMFgP6Cr0b4SOexKVMKwjTaGOkqtURGn4SQtLX28blG0ve20Vqd2e4XM7USJpSHazdM0icnEEYdBgcesJ/jFAAebFIO6HUH76egGFUV7ybE4x7QW7w41uU2Ga+mSpp3sgD5DaWBCaa/zQ6vlLd9x5aFiy7pqZSrxMyqk1nvctdeqrsFlfnBqSBjXCjmy9TryolbUl+6GtwVjXDHmgPRNqlBhVZXK7VAzXFb7Z2ONZ+PZRIy2JZPcWgc3N+vQrTXywtqeG6TiX1h2HDrymh1u2ra0lvRFgUJueUqd476JFO+C+NfzBfUs0pTmilV4NXvSkViHz7w2Yoc6IOurbmab0VNrSySUpSqi2v6oB9vrejHvyG26X+vZTR9SSD1LfcBvdlxcr43BWS2qFVZqdb60ydZQ9XLnwSjkIME2DQ95SLvK9TRGbMah+bZX9TqPz9dbl90Ql6IX8bU1z5c85fEc6qSoOe+NC08FqzQcW+UEHAWr+p6O0Mb0i1TOHDVrtRL1jGqzReflZgkPvj5YRi0mJxIebppxuqq5AFFc5p/n9C0fQ0IfBXVH8+uo000zn29bryt8/ZzdInJJXiD8qGr6lRZqenMa4nMa0ZK/dh3KFxYkUvgjZ3kbs/SWRILsLofCoMISk8p2h1OerROsRGwjanOZixv+mPI3oliiR2glaDQ/4oQZEM6it9JrYLbNnNZqSU4ZATId0zhcYkY8UHEmn5eUZDS7JF6jSd+LZTcXeik+06tbBUPYIOij6GzbJTuqjajUbuSNZde7jZWGkrwXFR1bVTK387l1fwwxZbmlOmUv5FzihB4S71f8FpGN/cJYJJp2s3ItO2y43m0P1nnZ7lcVg+VRfq66TRuLPV0UBF00hXca4CUPcvy4XKtoPVcds9Gcq0jFPbPBOXvpXh0U6eAjv75VhLaV1seI6XW720FnxezOa+6YBidLl6zjASmSvSRjAlENo9ao5lLenwnVhXtXxzRmnxI+EUeqZFLIzbI2lk6mC9e1VSXcz0sk9S8HHKn3fpeLi8451yYCwcHQJepu7R4cPa6TpPXyU6+WFV+dA93asjvlihL1/qIznh7FAbrYHn3dKwplvl6QJICPuAlV6qTEocmsaCpDxG5fesZtIAJWhVGh4/PrKY6geaJdlIusFEEvHsyluxeMhdfU69EIJG1OlJYQnpvCrN3MxwcxwVxns/KFGxIv55HRVtpg3VRtsW7FxOyGZpGvFNdNN6AA99tQMYp5gNVXCSQyfrwJ4pw8GWSC4CJ6tpBT53fOvuJuW+4GsSNExdiFklW7TqtzDZct6cEd6R1vA8Jg9Ck0x83GvYSKki/qzRm7ntbEOF5EhG2Z8VaLdgxKECIctNovcr4QEgNg/V46cksuF6Gdteq3jsvtNr4r3uYQVjXDWi2qondhzifRjMqUXcwuE/IUzZObPchiN+e5xtDz+iwgNceukmQRK3HTMyy2cIoSK8geFfvFuD3JsrrUdWoR+g4XWe1xv4t66CSUC4i3xCtoZuSNZLQ8bLreXDldC7KdI8teNP1uMHMDo7xRkubHKz+qFUl65x0FdQNyi6DK9RwpAKVvieoAuGFgTIo7Gut1RNLafH4IdsoKgO8RFNoyXB7z+ErB8Q1lGCYzlOBIF/Ggkijrb8+3E6iRunKQ4rD0WZXmYnHFo37BCkWYZIxxiAklXHcIiu5VxbjaEdpzjmLHgN7LW2Tpg0ZKyk46QMJW3C4z+4RDlwIYNBcDkEEcY23EOSMcrqqCUCuineO8RFfHw3lbxAwCedTGkLelR3TVxRw0yToYx1y7yGtP4Uy16tBbCBkZsRvLGBVVWTjX6SgjG2p9DE+WsB+XXmcp5ZB4dG6aPYqTfn3RZfYW5ZcsgIJTpl+TUcZwM2bayFrt9nLhoAI2aMXC1s87WaDNgHFXrrIiLqdS8mlmgwxWyQ6ewMkunHAHUkytc4YlZjtcGuiYHe3VijRCgm/pipyXohu67VYkChNpbiO/HLsN7pHawCPbLRcss13ujMsEsSh+zdv8SkdFjYHXvRpe1W2KDNqOQyyW22D89ZQSPNcrwXpb7nZbojTOEbk6amayzU0xzktPL/L97RrkkiyOm367DsldfcNH1K/grdaUC0Hnx1A886I4dxyvlEZRq2Mnl0pk055aGLOuMiQWztxDKTNyA8Af0IY/10PQNRoi6ZDGdlbnbbQrd8VIvu95blWljTlkeY7iV8Fji2ghB5x9vLS5eFryRJyK87gnbrofRmdIZdG1dEHWFAALX/BqHmGVE9cQYbxYzQuGWOvUSTicsiSQTgsI21NpMJ7ScpGHJCxXHr1YwNcD5t76/fm41A46K+wyyBlToqO02/VKicJVn+crHIcv0AHvWjQXuJTN4nWr0nBlIHvuhtrwASqQJthLaU4ymeI788DgOjkkc3PAaY0+b5kVKiQW2+kUzvSHZbIIAVzE3d53MyyuUmvHwrK42xiCE697Kp6Pfi4yqr3aaosL1UZDsB6H9JR5PZFCjpCkVkUHIA3SoU58blOKp7IUl1FX+9uESK601iw1UuzjAlsLN58N0WrbeztGRmORHNvmejz5O04eZYD/ijywV3O4QPaJKAUfSa/2oiXEk3kTNhZ7arMLS1ioyBZLBNtnLj1uN+NA+p6W6PIWlnGpSPc+d8MNr9AbwPbucjhWNb2O0b0gkHy6XVmrsVTFs7pKXY84Rnq0pkElUD3vZCphjrpvsSpmS4ouscujq+ACLAUGv2Q999Ao51Of1TAs0I5k5YqoNYfBGk9Me7NWyfHkSDuBsIRBQBZ6c1XU0w7hM8hKJFrGhi5f6d0hIE69Mo4u7gr2kceh+mBxiREhSrWVMM1bi2BzUtmn8OJc2/qcCDcP1AdCJR2gN/O63hKhHFA30FGpm0GV8Xm2FTzO0KSbulxbrg6LYkIOZMGnNLSJkrxsD+Sp9BAjc/JFcWwEsnVR76YsMVDhJqHCxBgX8SG7kGRflkubRa/cJQzGndMu63ZhFXKcurt9i6C9klThQpC0umg4/irpl7VqyNcYwW4EAcHX+SHkmLVSVGZ0Xi4xNwcVvch2MKIZmnxmadpixsVh18d9Sfs9bFgLA4ktNW2JIdMGfyNYogwZt3RdCYyRHzU/FDt3vdUb0zSGE8brqolfYgo4r0DDi3LLs8VYssV1U1JjQmL2bu+zgzzichZfcF/2tFQ+pEjo+hEGm4y7BTFUetzFhwUVWKVwrWsmCB3Zmp+Rw9EuOyG98RARS6cjqycMgVllZW7U6npiRwAQsrBwbzqPu0ciI/dq2rXegSoRZO1czoO4NHfsgdD8S1nGhFuEDN9SKEoxgHMGm5+jFKp0TqvZXeKThL+Ektym9WB1bSmPZ7KIbjegV97hQduAPddRPzsN4jCyhd26quIlQdP2adsENNjnaG6bVDsMBNPeuPyZrYmdh0u3m9njIUEfYEY+rbOzvHZv/Kl2fAnKTwSWKSqVUjArkycHwokVpEjKaYREXb+i8JncmAXK7sjOv7oDRNDkmmjm7g7OzCvhtfktXDAe7hl4pUUGtqF6gyfSU9geqmAFnVch5ZNdB1PLDbw8N0sWIo70XINvCNIQ9M06mgPWIkJlq3B9knaMwQ+NtCAOfsxrC/h8Xpy53cWPVGiR1t7iAkf+4JxiSlipq3LsOWl/FI7b0zapTxvBSUZoF7p8a52rWEduyJknjDipcvnkw9G6pBp+TzOtM2YbXzNzJLlJyG67E7aw5WSE5YgkcjoOmI5KFXmAFzDKrBGeiddrxitcgcR0/Gye56orM2ltn04WR57Cw3wEnRbbe5pURhIE2bGteZui28hVqxcBiepUAaOXseG3bEstLxRrgd6b3m9UmtituhZ3YYGylusr1jnOxuDkBFvbbmZiXWd5eYtY6Bwrzv4mW435xh0P+NiuEahXzcUiiEVjRCSrFVTX4YRod1nHXiQyQnWMyVCi0xwqM3ol8KvjRrRzGhFvCqlqA3Pmjqi6QMLNAhcID1ovQjIsC46Y04u5JUIcJtdzmbkxyXq8IKkj83NB28WyjDPGCiTtQRZ5wWlZaoOeV9KGrmyTWcdbU5j3BsG6O1yeO8R2fZTRDNYXEezUoi77wTELbvMBWhJkaAcbmqRXFXdp5+2NG91bQx9cQOr4/hZKbc1bwQEzCzfI5EvUuAgCcy2HGRSxqqzGrVrUaeJUKk7EAvWZpUUIJjT0FjVMTbALdSdjV2xVptGwcx/teQJCR9XXlni1WzWl36T5yTYgXDdICUGpvaO3smlH48qVAedwOrXHw/yy7FglJAo8YJjdFuz9uDg8Cjd4lZ8xjbuQx0U/F0kOU8/6Fi9QYpdhGMQZc3N1choYIw4sPdBWkCSQY3n4ec9C7ZWBFjFKziG2lXNbZ8aTRHXzTScFMWYfa1o8jm3rkJpXYGo7RNSQ4UrTQCsY3tArfh3gudfzFJTSA3FaOLdY5TiEWCao46J6As+znqEKLDH20ZUiW1pYdjG8zgk7C42FkhyvFHTcbA69JndyH+c+NtC00x92mMGDDTVg6QSZI3ZjLtF4N5rkifNWLU6wxwhW+nwp7ebZ2IwRIpB7NDAwsfTQzkezHYbi+sarXUa77FbGBRo3o+8XnJevCHcLEWVsz1WGhMhwYRJsFVGaqJpHq5NTNWVhPQP0eNnjTZoUGzz1cbvc1CnuNjZT0ilrUuNSpPCUmDfzjdeJLNfWvZu227muBp1JSiJ6kNo12Net1plKbvSOXJ48xt337R7ZnsVst3Z0en4zFydYa7NDlgUYlhxdukr7zYH1cqG3IWQtnmy7SgoBO2S01LHnjS7mmq94t4axDptLILpkZCw9pGZ4WaHwVX+esw68PcDUvmBZ9u8vH1+mc+Pn6e9feJg7nbX9nx35PU7n3p4D3c9dfdv7fF/r819R6uePL5UbA5UeR5t12obPY8D/crD56Z8/QZjmD49npNMjq1vzdlTe2OH0M5+XOPdaMHj4WheAwOL7z3actp5+cVBPP0pxwfvL3bCsnI6MH0uCD7aXxfn9kPtrU3x9HOlO555xPj2K8b3422X4PO39+OINIEixW3/FKfKrX5WTrc+HEtMR6fRU4uW3/wTWX4fzQiUAAA== -->
