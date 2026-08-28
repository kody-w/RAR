---
name: "rar-cowork-cookbook-report-track-project-fees"
description: "Builds a structured summary report of track project fees activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_project_fees", "rar_sha256": "87a45da68fcdda92b033d81e689f55846d19127beb81245f9f0edfc987d4993a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `report_track_project_fees_agent.py` and in the RCI capsule.

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

Track project fees Summary Report — Builds a structured summary report of track project fees activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 87a45da68fcdda92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_project_fees_agent.py` first:

```bash
python3 report_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_project_fees_agent.py   # or on stdin
python3 report_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Summary Report — Builds a structured summary report of track project fees activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_project_fees',
    "version": '2.0.1',
    "display_name": 'Track project fees Summary Report',
    "description": 'Builds a structured summary report of track project fees activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bbafbdd5773904f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTrackProjectFees(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackProjectFees'
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
    print(ReportTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+bOiyLbuv8Ld94eqvu7aIgJCnTgRT0EFBFFm7OqoZkgmmQcR+/X//hK1dlXf033uORE3njVsgcw1fGutb2Um+7cXp2ujon75/KICJ0e2TprGEagRJ/cRpuiL+gx/FGcX/kO8Im/r2O3aom5eXl980Hh1XLZxkcPpqy5O/QZxkKatO6/tauAjTZdlTj0gNSiLukWKAGlrxzsjZV0kwGuRAAA4w2vjS9wOSB+3EdIWrZM2r3AgyH34c7TDrYFz9os+b96gWnB1sjIFzcvnn395fYnh95fPv714qdPAWy/KXZU2qjk8tGygEjgtdfIQPi8H6G4Or0tQB0WdwVs+CJDn1ccGpMEr8l//de6dOmx++vwlR56fLy/jH6XLkTYC0EynaaGHnlM6bpxC89+QZdo7QwOdhc7nTyTiPHx7zPwuqSiRv4/PPj6UvIWg/fjlpYAmOCOWX15+Qooa6qu78fvbKKX8+NNbWvSg/vjTdzlN595RhMKg1W9fn9dPsXDg96FxcNf6dyj1ETUXfHn5wbnx87B79BPOfHlLijj/+BAMw3UBuZN74ONPfyXWi4B3TuOm/Zfk/vwQHAHHhz49Df/p9Q7yL8jk6dC7zL9WW8Kw/juewOHf1L0iT6D+SvYd//8mOo1zmLLfEP9TcX82YfJ35Oe/9O2fTXhFgi8vLEjjC8wONwWfkd++qoc18/MH//vND7/8DkX/j2LUoqu9u4SvmZPHAWjar19//tDcb3/45ecPXQlzDTjZ165O/0zmn+F61/MHBJ+jPv5xLtSv5+ccFjHynunIb0X5H/Xvb4jhpLH//X7zGfmxXsbPBBmd+Kb0AcEPNdNAW3/A8aeX3yEz5A8mGh/DKv/P/0Sk2KuLpghaRPWKrkVggNs4A6PxWhQ3CPw71nYNIK5NDIF9jnvS1WgxpLBf/49358VP3pMXpw96+3rntq/PwV9Hbvv1DdGgwKKOwzh3UkRZHg5fcicEeTsqK2vQgPoCacQdWvAJEtCn8QsS58ivfynz6336Wzn8eufG+MFHCsOPXNR0KXgb/TEjkD+t9yCtgyvwOig5LTxoRhBD+nyFfjZFeoFcNvrenOM0Rfy4hnoKSNmjbIjP51HYr7/+6jpN9CV/kOccefB+M4UD3s1BPn2C/gRpHEbtlxx4UYF8+O33D8j/Rf7ZrLvwUccB0vcTfWihoMp7BFZTl8FhMDAwlJAq7uj/9vsTVSgmh40KxioOYvCYDLPxDPxvEKvc8hNGkIgLILQQ1myEFDIyErdvCB8g7/Y+G9TI2VHRtIgPSth9QO4NUKoD3XlHMi9apIEp1wTDK9I14K71V7d27iZmsKyd9ldEYg6wQxQp/G808z4ITi7yGML/ngCP+1BI/aFBVt9EvCH7Mf+Q0qmdMqqdp47AecQFdoZv06FwB8lB/yUfmyAYoboXwwMeOAgi4z1D+mmMOWzgsB/DtvpN932MM/Yx7d7P6i9580x0px5D4UHih0rDLvZH+v/bM6WaqOhS/44ftHSU9IyC/4zKPQe1f+z16nNB8OjSyJcOQ2c48v9n6TCatNxulfV2qa1ZZL3XFPsB1biuGSF9LIVGeTBfHmXxvb9/Y4dvJPklT2MY93r422PkHeDnmB/8UJbKXT6MLoRqlHtPvjGZ6npMW+dL/o2NocnInXog/rBSYSaPCfRN4fj0m6URLMfx+ntnvger9kenYYIhZeemMPgQJd8dYWujeiygJ+AwE8EIaR/FXvQHrxAoHaIO5SPQiBiWBMTuDt2+gG7C2gnqIvs+PB7XO9AKv/OgtXDhCN4QE9bAmAcNLDy4aBnHQBQ+3EUhGYAYQxPfEW4ip3wYM641nwY6z1j8iP/z0fecvVsyGg9lOr7TQiT7kTx9cH3E9d3KZ6SgqdlYZfdJfwz201Pkx6bxty/53cJ3vobFm4799gdoEFg0WXNPtZF7GsgfGXimD8yDe2t9e3THR/t9t+XzPyyvP/57K/B7v9P/GLfPSNS2ZfN5On30qG8t6g1WPmxTXlyC5tmuPt3r6dOznj6N9fQHgQ98PiP/nlF/EPHM5c/I7A19Q8dHYuyBMVmfH4gB82llf8LHp19yBXwPLlRfZJDORswH2B/fu8e3IbCFhDUIx8GPbtKMTaiHfe9OnxD+L/l7AjyLA7JzHo6tryl+KNp7G4XhfETrneXho7yFuv1xmRWCceuRjuY34OVz3qXp60vuZOCfbTlGCoe5CVEYdygQabhcaWNwv3I6Px6hGL//cSMl37846VhIxdgOR75+58q72X4NbRorL4xH1n5FoKkhZMDRk36svrHnu9CzBtIo8EfT26EcbX1sScbl0fva6R8tuBcwZB6/+DzW8SsyrnNfkfcl6yvybRNx34/lHdxF/Twul0ef4VD4433s+z7RBS+//IkZz9XzXxvxJJcHnTvu2H5GF//EJyitBlUH+50/2vPdwe96i4ey3+92to/9328v3/jjGaXnWg8Oh4X6qRk73hRmMFQIrx+5Bp/966vA50RIdHAxAmdSCwcnfIekAs/3HRpz0fncp2aApOiAICic9Gf0DFu4wKVmGE4EdIACP/BoauHjND13oLxHqn4d+3k8GgPQAMzhJM+fkxhB4PRsgTm07+ALx/FRilqgi8CHveD71DPkyaeHD49G+N4XpPcMfTj624tL4nAkhzf88vFhprThLMxFso9cekEGYZVMvFZcUwtXcestuDmMu9eWflHie9h8m3hvKLsiQ7GmOiqVqgF+vQwgYrZApzeRPB8GlMzmum6RzKrlhC11EXuIBCHKx5hB/XYnpCCu+SowtuLmGJ8TsatnZmq7nrPYFbUYzwh6uvboOneMrbrdNIYKsDo9VolAm52Zb45t5Jva7jpJazdxE8WPjcY2jSxJVgqhppPh1hueY50No/YIxvYSnQCXpJ+CeT7Q3VX0ApdcBPm8sOKFHvOlV7XDDlNaAzU2aHTaCOC62xIcrzc2WWABPmDCYOkCJ/gg0STPoLlLJsQEWpZFedFlLyeGG9ilN8Pd2K5+uA5noTfMM9lvw9ZbzI7Xs+B7DloVeOud1sYArcccESSo7h5S7VhPos7sNg5xW0kbfjA2qb9bKfMIXIlUHtarUls5tx0a8Zi/Is5qMxDebCeQXUv1ER/VemSiy5UbcLVQBIIVebi1wPWYLG2f2F/1S5zuWp4MT3gN92XHQASqkSozFwpqOuhmx+L21T7PwgrTdNDaUHZ6JrWiLuOZo84DeprR3FDabFk2R6w+siWbrQfYOSUXY6+HmTO/2WTn+/1Mt6RDf4tz93ax8h6rc3GV+IdVdz3lgrDP3OBEZBLuuzLX7ConQ/E62fnWNbvuWnen9BfKahWjyJY3Xl3gNnnhNaE3gz0LbYl31InCu81y2AyTa2S7M1MWeqbOFmi+aWOq8I6dPW1v6Gw9tLV6k10t2oPsEM1sY9eUeMhZanHzvfMN94bTRBpOuuyihJZrN0m76OT50ntBq3G9dwizwJaVOlfjnTqlDsRt4h8O9ISKz1tlAipvyDCxdVWnFmdKc3Ttk7BL6ZOUDZliMXjdOpqwti7biDGHwDYid11m3MLoaDQ71lt1YqyjqT5VhjNOsFauyGF+uF1ElrGZeI6xtbEWwZrqd8tZHO+yapD4fN0szic0lpbnXa/o0mq/Erx26LtS8oAYDvw89yq0ly8LRjY1FUjKgjf5i7LHxbWVRouNT05oLtYwdpUQl7zSTqmQ+AoPw+rsi86QyKPVJdPVbOLeDJRCXXIqkjuHNuyONU5BUnKw+DWg7FzeSWpxso4lnC6WGo9Gx8HFNW/ae8bMmaQKIU2Xt7aWWkc+MRQq+3rv1AYjh1k9sWJWusj0fIkmxRX15WkA14lVdDtc9EIg4ononGWOrGalYRGW2u+aYVtvVqgn113jaUQhpFZpkWh1UmXL8sUTQZKh2p7VrlglR2qyFGM4V+RnsiUtuaArOPyMiTTJ4agC2N3e5P2gScLourII3Wj3TWeweJvnnMovTaphjfNZvSyuzqWSImmhMQ5PT467orLkXBpsvEh6aTdH+8KeiFqcFOJVXF89xvXdeOJ3lXEO/ExoAtI/npy4Na715Za1YaBIJMgs00A9hbPF7bQSN4eTKJAqpOWrVNEVTU4xq7mC3dTjomOfHez8ZKvVNc2S3pdofFBYcXqcYCQocm6ZyebFuy1tuUo267yWJ6LXLg/CAOIuCBjsxlSnRt/pgbAnpyA6X5vsIu4gIajEPs2iS8hcoyPvb5i9U2DnCQvCssotcX1y0ukSF3g9sGtekFvZxFwXldv6aHCLPp7Z+tIQlBANDcJ28diVMW8dLneKyex16qa4yzNWHxhnIoMZYR/1JmjEo1yYeXXOSqIDluScUJ0q3b18mRMzcIH9p7quttX+OmtmU4EwziaXuoRkkAq1A85OYDXiQuA6tYVVG3iTHuM2zPoqbrzrNicxAILDdO6eUcrS5lg4WRurmMQoqj0N6pLZ22t/Z2LJbZnGF2alzexqq8mhbN8sW9kLUnE+z5eKv6qElGRPW+FsGe3gnFWHplRDZf09OqvQ/LhqBVyF5agLs51c7Xb9Sb9uCgl2mTU+TSgap6rIWpTUJpKPDHpzI/1kaMmeluhYi/Jgxi+V41xNsIC2O55bOO7ZkMfS6+ale6wPN+2IExx1nRcsQ5zrHKZIIrbXZeXp5G1jMex2uzb5ydxP2yIR5pR0otK5nwyeamjHs6sM4WoHKpHQhXWWEN0C5jZlh7xmVfRA47nd46U9CSbRuo1PMjvDLmyjxkSzJvVAWutcttiGA9bd6ino12EvrdYTChXM67lXI8JNsO5aTvhbjy+rAl2pQ4fqzAqdmDokh73F5Oytn0fK7kRt9eMJjbR8vVW645pnuNCl1yS9FrqGMq2UYOSemTmWvrWSKHJmmmVHZT8DGR7zKyxUuEt+GHJ/sa+aqGDwFL0uT2Bd+m1RpT5x9WrHTqdXV2BylO3oDGTzeLuaZq6a8e5aUNvAnLULSZmSSnvQ7Wy9WeynFZkez1XOT7cFGvrSqd5qEn0CC4VxOOt2AAAlJQ0kgsrsFmqcTY83U99NfVJcNhFhpFbBGLHqoerc3ruMVhUmXxRovMZ1TokNESzDVO6STWUfukWOJqSz3i/lc5YvWrZ28aC9zoAjK8yVcJfbS0hVxIo7KPStUjOx6SSQXQaU8wPYIWeiVrJKWHfMfLMA6SG4QiVtXmvFDGe32aSn+a7m25nkVm5z9ZLS4HJ3kavFMkIrO1RQMresob8wJhkubVvKsqgFBaFqfYAfndMm3OqlJ/MFTLjB1xNqSCMTN+39NslorUyEyJsn/ObanWb7odZRkrQYbsWgxUX3yl3YOOYOxau68uqVPhNu0XklKErkrVa1qVRkvGD2qrC4demCw5mK4SE/m3JZHNOZsTlQaESoR6IodV30ezUUyH41LFfGfhv110oV1I0QnSRiflYP+ZxM5UpeYoOjOB7F21V9O9auJMJsOB+xE3bYVIyuDBsJJah6oaeWpTFXr8XFSIs2t6temKVZ24dV1lW5xMG4XrRTsTrW4RQX7coIScH2mNkRQ4X2wDrJYprW5zbzmY2qs7u8ZWeLtJGOM+GMwq3KuYr3S8Mlz2eUoTdw49JEDbmXLcoGlV2FjkDMGlOWDlyi0aa2UXmj8NbkEFnNytp54LbbSjs+xueKOiRZUuSMHBxmyRFnDb2YU2sxAB2jV+bUISVK35wY3lEjeceo0bbb+dqpN28Hp3EXEO3s1O2JY+0TWOrmm+LQ8pvOm/nZwGDN7WTj2hS/xXEsTRLNxk0ULgnMah2FQBODTm6KlcYrceqJUofue/Vch7tCIpu0Zc1qb4RnzYiqGMWuOI5NXEoON/R6KGo7shgG8/LTcr3KxCnqmMrRWi4W7vTMSCPaFkZHRLNjcn6t5uLmump7FJWPg5pQZUaaTdI58kzJ+ozqzbTd9uj+HDXUUDvzcCB78YQ6x1PhaKRE6KFusNRUGnSiTTM5HKI5q2RxEgHFl1JFTtHQAwk2tWnPuRiE03NgPqzI4FTyVdPQQegqJ0rVpYNZdJvNdTvB4/1RlgydbrpTW9ucdqmOyxu3tRRp5V2N7Rz4PdyduddrCkJu68Mw8wZ9CmO2v1QMp2DY3tvrB6c29+RuJUXcTWkWgKft0rxgzJ6eNCiXzPReJrEhbW8HX90d9gXg2tuM3k1CsfY4gpINk/DoEDfpBqzJVbLcsKzg3qxmoV3MjVs3Oz8z+pZt2CRUcDP3583RZP3JAdxyShdZe4PuDU6pcZgHQYluV7nZ3IriUvFSyE3dgZuoLPRqIhiQ5qcWmtvFbMnNj5OKGhh9QWzwC+WJ0wwviaBLZuGK9ae+CVeHkYkdyN7c4puA6uQ6YCcWex4AdrlMB4lbMEa906rFdEHp0xvatOjiahzM6gp9rhyL9o7rmla3cbtZ4TJgJtU+F+szx2yGvC/pZV/uwyMnX06GrdnNqlyhBB7LZ27NpbyvHnkWbgdP87TvREMS6dsOs0lxh+swKy8KCthoUwztVrzRnXvLDkC3E/183aPiTuR3UwI3cRsrCdlm24k1Y8t2P11Je3qDbm8xu6GCguIJzJoHtkUtPIFNm9MxOglDwp3m+dTyVyFZaCwTsN5sg+LkQQFdYnkXZZpUl5kyrbk5kHThhGZWsxzQpY7Zcj7vAXekO2Kiobe1qzQAww6NHWMNJERp1gZgmB58fF4Rid5RB2F7ATKe+Zfcc1sq2qIMc1lp7bwwb5LB4TmvMNyWWy+2Gimb7ua2Dg4uS2lwmXH0GCCr18McD+IkjIuU7ATXidXyKDNdcCapHbc8rKyjkCw6Tglz/OQRt4g/cKZnyRCodm31URdzm7lFHafz86CCINpyxSFaOVeiOHnuJColX11x3TpTBB3sttrqKjWcHPYcbu9Imj5UOxdnd9kun1OnnNH022Vf2753oPPrfAfcWLxsMC0vSiKzt9T8PN3tL3NW69BqXRyttpX6BbXN5MmWxBJXyH2XpE40XMfz3nxJZ/KqFClbXlG2I1+YuU5MV/3ZgNvCGUpcTtNZXjXOwowsdmX77WpWdxhjJfKitoQ863DH3Xc7di3T6nWyLaiuPW4pjsYVYomyK9nFNuUUXOf2WVme1AOuTza3kHZ4G3DF1DsPFVla7WZ2IQPbLbzFdblnunkbhPjhIu7bSaDN6nRqBRU7kHWe7sWje8UdauqXtrw/Tov8aE6rCbMowOziT9kat0xhWjTdTYz2Xuszt0VYYpfTgmLpCTosveHSmG4nQy5AmaJgrYTJ+FUypJsKo82DGEh+6Bpux6M+P/Nve7O/+OZ0mxbbMMxWTnaJr/Sk20hH1OMjtD13kwm+1Ra822kcEA+Ldk9jiQ4CK2aSnaUsjjjNyCzOTn3iGN74wsWbnma7OW9s9pftXIQ9vZ3QrYBd0Tm3qZqVbZ5tyBPEbSblDR+w0fyyaTUrCgIRk/pguUw9XrsGzrLeTyWSh8WxuQiJzsr13hKiFLfotNPE0kILuTkB+gRTCo8nrLioqutyuphM1cPyFJDF6gA2OX0+ZrOBTDqwkCADzXm+uWBefZhsQoZfEIa+KNCz03TMZXeZHUPjMFEznVwQmI31wnUiB0uvEBrvxraLo50pZdSoy9wl5fBGKXagA0Uhyul2zoY46ESeYIWGcjs96PCe5A4ox5xY0h34Yrlc/v3l9WU8EX6e6/7Pr2DH47T/tVO9xwHct/c59xNV4Pif77o+/wu2/PL6UnsxtORxVtmkXfg84PtvJ5Wf/vIFwDhteLzHHF80XdtvJ92tE46/b/MS537XtPXwtSnS7n5I+vrids34OwDNaJYHf77c3cjK8ej3oelx525yW4zDgni8F+fjyxPgx04Lnpfh88T29cUfYBRir/k6J4mvoC5H957vE6BX2Bv6Nnv5/f8B6wWJiL4kAAA= -->
