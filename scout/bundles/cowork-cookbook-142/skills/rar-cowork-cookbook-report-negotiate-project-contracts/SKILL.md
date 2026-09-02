---
name: "rar-cowork-cookbook-report-negotiate-project-contracts"
description: "Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_negotiate_project_contracts", "rar_sha256": "4b30e64d9e5f438927734e07f9d75ee3740b9f23c3a8adf0a34ad8cf4584abbd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_negotiate_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-negotiate-project-contracts:487c0d748d117f0cbfdc77b71e866bd7ad16d19fec30d087f767cdf613f33deb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_negotiate_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_negotiate_project_contracts_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Negotiate project contracts Summary Report — Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-negotiate-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 4b30e64d9e5f4389…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_negotiate_project_contracts_agent.py` first:

```bash
python3 report_negotiate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_negotiate_project_contracts_agent.py   # or on stdin
python3 report_negotiate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate project contracts Summary Report — Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-negotiate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_negotiate_project_contracts',
    "version": '2.0.0',
    "display_name": 'Negotiate project contracts Summary Report',
    "description": 'Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-negotiate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-negotiate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f93199aaa6a1405a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/negotiate-project-contracts'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-negotiate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportNegotiateProjectContracts(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportNegotiateProjectContracts'
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
    print(ReportNegotiateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOb2JLvV2Fq/nD3UC72rW50xEMSkhBaACEh1O4os4PYd1BPf/c5SKqyPdN97/SLF08OWwjy5J6/zHPw709mUwdZ+fT6tHfNFFqYcRwGbgmZqQNNsy4rI/CVRRb4C9lZWpeh1dRZWT09PzluZZdhXodZCpZPmjB2KsiEqrps7LopXQeqmiQxywEq3TwrayjzoNT1szo0axfKy+zi2vWdqWnXYKldh21YD1AX1gFUZ7UZV89QXbqpA75HhazSNSMn69LqBch3ezPJY7d6ev31t+enEFw/vf7+ZMdmBW49qTeZ23d58l3c9F0aWB+bqQ8I8wE4IAW/c7f0sjIBtxzXgx6/fqrc2HuG/uM/os4s/ern1y8p9Ph8eRr/qE0K1YEL9DWrGthsm7lphTGw4wXi484cKmA+cEf68E2Y+i/3ld84ZTn0y/jsp7uQF9+tf/rylAEVzNG7X55+hrISyCub8fpl5JL/9PNLnHVu+dPP3/hUjXXzKWAGtH55e/x+sAWE30hD7yb1F8D1HkfL/fL0nXHj5673aCdY+fRyycL0pztjELzWTc3Udn/6+a/Y2oFrR3FY1f8rvr/eGQeu6QCbHor//Hxz8m8Q/DDog+dfi81BWP+OJYD8Xdwz9HDUX/G++f+/sY7D1K0+PP6n7P5sAfwL9Otf2vbPFjxD3penmRuHLcgOK3Zfod/f9rIw/fWT8+3mp9/+AKz/JZt91pT2jcNbYqah51b129uvn6rb7U+//fqpyUGuuWby1pTxn/H8M7/e5PzgwQfVTz+uBfIPaZSCaoY+Mh36Pcv/rfzjBTqaceh8u1+9Qt/Xy/iBodGId6F3F3xXMxXQ9Ts//vz0B4CI9I5N42NQ5f/+79AmtMusyrwa2ttZU0MgwHWYuKPyWhBWkPYo6q97SVyvXxLnKwTujuUOIMJs4hpalGYYv4PZaAEAua//x74h52f7gZzIHQDfPtDv7bHg7QP9vr5AWgAEZ2Xoh6kZQyovy5Dpu2k9irwlB4DTz+0oFWgU3lFHnYoj4lRN7P4D+vqvxbzdOL7kw2jIlxRExgThcqDaTcBSswzjATJHpLKG2v0MEBagSZnFsWXaETT+0+Qvo3f0wE0fPrNB23B7124AqMeZDVT3QoDKzyDsVRa3ABlHT1ZRGMeQE5ZAnQy0hBHOgbdfR2Zfv361zCr4kt6hmIDufaVCAMGHwtDnz3npenHoB/WX1LWDDPr0+x+foP+E/tmqG/NRhgy6ws1jIJ1jaLXfbSFQm00CyCpoTAwAPLfY/f7HPRSjdilohKCiQi90b4sBt2+JMFpwj897cIDNo4pu+ZD0o9+gLgB+gcIaeAtUefX8JR1ZZIC07MLKfXfiffHd9e/RvssZY1I9fAji5JVZcqO95eAYTDsrnRdI9KAPTz1a7xjRIKtqkLY5aKduag9gpVl/C2Ga1VAFKqfyhmeoqYCpI+evFmA9OicB8GTWX6HNVAadLovBP6ODbuLB6iwNx8A/0vV+GzApP4Ecm7yzeIG2LvAmlJulmQelWbk3Os+8ZwTocO/rAXMTjAodNDZ1d4zRraZvmbf9JxPE/jFv3Hs/9KXBUYyE/j9PJqOS/GKhCgteE2aQsNVU455RI8PRwPvINfIDE8a9PL5NDe8A8w69X9I4BFEoh3/cKb1bEt1pvjNI5dUb/7GcyxvfsAapMMa2LMf0Nb+k7xgPVB7TuhrhClRsNNZ/9iFwfPquaQDKcvz9rd9D9ywbjQb5C+WNFYc25Lmuc0v1OijHQnp4HuSFO/oWZL4d/GAVBLgD9wP+EFAiBD4GvrvHFxQEmJHu2f1BHo5TFNDCaWygLagY9wXSxwQGSVhBlgtGoZEGeOHTjRWUuMDHQMUPD1eBmd+VGWfah4LmIxbf+//xCKTi2EqAtI86AzxNx6yBJzsQAlBG/T2uH1o+IgVUTcacvy36MdgPS6HvW9E/xloDGn4DezCEj138O9cAgC6T6pZqoL9GFajmxH2kD8iDW8N+uffce1P/0OX1f4zxP/29Sf/WRQ8/xu0VCuo6r14R5N7p3hvdi50loNnZYe5Wj6b3+aOwPj8K6/NHYf3A+e6oV+jvafcDi0dSv0LYC/qCjo/Woe2OWfv4AGdMP0+Mz+T49Euqut+iDMRnCYCZ0fkDgNqPdvJOAnqKX7r+SHxvL9XYlTrQCG+odmsPH5nwqBIAmqk/9sIq+656R5vGuN7D9oG+4FE64rozTnG+O25x4lH9yn16TZs4fn5KzcT9X21tRogF2QrcMW6JgN/BWFSH7u2X2Tjh6JPx+sct3O52YcZjaWVjowSoGX7A6E1/pwTKjbXogxbmls8Q0NkHmDia1I31OE4DFjCxAgjrOqMN9ZCPSt+3PuMY9jGj/U8NbiUNsMjJXsfKBv0UzNPP0Mdo/Ay9b1ZuG8C0Abu1X8exfLQZkIKvD9qPHarlPv32J2o8pvS/VuIBN3eAN62xUY4m/olNgFvpFg1ozM6ozzcDv8nN7sL+uOlZ3/eZvz+9I8p4fZ8S7qkFFvyNWW60+r0Hv42szZHBbeK6OeE2qb6ZIAPGXvvdI38cHN7uufr0CgDJfX4Ci8HEA8bv621n/XTXBxjybcYdtTPLz9U4OyCg1AAn0NHz0YgIwOJ3AsbboXOjHy9e/2Iw/mcY8UqyjI06DMk6GMZ4qG15js0wFoO5LE1bDmM6GO1gnOfaBOqgLOMxNGM7Ho0RHkE4rgXUqEBSJOZDDQQbowAM+HD1/8W4/nTnAJoKTtGABWkRqEuTDudSHkmwHM4wBOmijMc5DOW6BEOiFufhhE2YrOl4qEmQpsPaHkmxpGlZzsjvMS7e1Xp7H83f43IHC6BBkoSj0rhp2qzNYEAmY9K2S6AWYbsYjjkM4aIUR3gs65LuyPmx9BGbMXR3y8e8BZMimNPaUc7vj1iPuUiTgHJJViJ//0wR7mjSOGltewsuac/XUkS0GqxHS2VeFN3JOaLpgp5s+WvDqK4gHfBiAcpQDoLt0JeWvtlOl/RExveewQTUsFZLSWMKcW3tZuQmVOQZi8Q7DgkksQhRvcE2K12PVSneWnBWT6Rc2mclyharkCiwKDXqa3zMrekRRpADwZ70mmW7lXTsY5rZF6VdCFNuV6W4lWRpIEhrJjcxvO4NvIkLcYjtq+ObYSVd1mwsHJJzbK0K9mrPp6R7OVBue+kQl0gHruks27Noxkvk6hQyx2m/m591xbEOaFxo24t6Oh4ujTrE650jMDI7d+fD6bA6n4/25SRyFTZDmzNLYkxc5K26swlquDZSvM7VuLIKqd9XtnIsyrlCdnoVT6+UXmYSTR7rc34gL3Y+d4zTOcZ3fV5z816q6T1iGFR5tP3waE10M+kXk54JXI1YO/sy2SeHa3KkJiv0IuI7aS6p2plbmDkKnxauokQdPChrc8oHCRZsqEtV20sqzHRDZ+Ri1ewie8Vj+hmbXml9kAIDWS8OsTVHyc1xRzWmQO1k2pgYydFP8OtBr42a2scYqxkSdt5O2pawDow874rER+xr2a3z2UIYIupgE/YsUc1z06qcxRirMtuJUtA6O/ykNrsJp7u4N6F3DBXOdG3KiD18ZWRK6RvG7QIpOZ4uzabAWP0ooM31EM5NculoOKZNztHKZiW4FoNtb7ahn7Nn++pNPGaOAqvCEy6sZ27Y9ztRv5w2SDHEITGjUgSXtYM6Hcoi3WsZvTvM6XNwOg8mpi5D5exJSy+qdkmv0bNphC4WlpISEyIyNNZ2UBoFNaF1qgZvUlbdbTyp1lRFMJFKUHLS8RDiQi6U85Kiy+vaMnAJi/NNm5vXrTXNj+Yp1uoiD9WhsiaFct5oTr5Y72mNEyrZiHcdYraoV4VzZ0ikwOflHbeSDpdIbrgtPY3JdnrcrIJCCjvHNALLF1q1ml4PZxGlz1FExhf74vpKdGhOodRnYiiWAyIpmJZOQ3MzkzFGjO11Bk/bNrHlxdYWnL3b7FZr/2I6aD8Lpal4SKUc1yQqTZLTOV07zqpi3YWIo7lClOoEblnD76vak0KVT9kKX5VYfOzIck3aIsKVxZrapZu43NUaqYh9Wiuyv4s8XPMWWtosT8djqlpXy/ApuIf39WwDu+YSLqZV3MfO9pow3XG62Vx2WDnltJgYGLGVBfy0ZrV9Fi/WcFf72NIsiDw+Uac9usJWK0m6kiSbqsc5cdlr61lxMvHazqKibOIK5c6XlT6stsJ6ku089diruHqVc2eXX0Ul1+R+1eJ5poQUN+sO/nABcrzIYsWeq0xz6Zwvwnrh7Wy2S8+Csa9FsbbxPdfVUW0yywkZzlXg5IlJ19d1Op/zgn5OjhVc7hbKZtU3B65PIwXgojnrEaAWhooEBRvprpUEvEpCVjaRVRAtI2YVnHGqS2RfcpCDvvVU6YR1tckRJEtYKYtYNbxbzFpC4pdzlGPszUKzsxVwI6H5O3hnn6WAIorT9ro+6Ex4ImZOc/Y3KKb64RVL+zivQGJQcu/YyDS5TgeQ75ednDSY0xr0eaYdl0mXYlmYdpxiKxPP76fLTpuXOZ8gnShtj7rb2xdJ6fjdXlmspAUxRdenebMnjDTpUI9fVPnkOBcWx0IpuEEzr4sEw0hL5A8hwtdV3KkHMcXL5cxrdi48MbTDhjAtnvBrPjWcVKdJTg/1hIvU1DtlOOamZ5ptr0FZ2WqenjwuPUTxYqVzW+N4toTUFOYqQReryENgkTc8m+txcjoRTiKyqVONQdhDVFLB6UrjZ1k+K+GhmgYFej6fiNiwhYpP8ZWwXzgFy8tZ6UcRl8INevXnbYRjm+v+UJjBtptaezMEo3YeBGdMPVDb/XLrwitpJU0Tc0/AS3+FzLoYkQ1Su049fTFVxNg4JNY+vy5WEw7P6yWmy8R2Fla8pDY5R6gGQMWzze2l6XE7VwMZzg7JbG6VUb5LCvRYT3J30DMz8A+Gx/uRQi141KFP11Sg8C3KBCtmY9p9pBpcEPe+DbTGjkxCqLqsDVY4nHlrixmeAYp7NRPMgtTzpXS5tj4S8awYSdqpQQaOTQylKg0V1SRH2/ZTUTNZvSsp7KA1E7bHOntVVFPmiFMnAduuNjNfUeX5VO9sRnQy1jxxJ4kBGTzzeXSmHq3YvAjdJl3z/iJdlaSbue2ClHYn8WiGxyKWPCUYtjhfHBR2JmfZKYttLNLpmSwqdGfExVah3N1xftQ9M5R2C2wyrMJe4ecTXJiHA3qZOeuI2+hCkEgzQ4zKBhNsptLtwogOe7KPemM7YSImXSVmNNHohgX4NlWak2FMiW2x3jtbIilM090ffQQ7n8ph3Sdeq5r8PhAwZr2ZZJlDctfpGgud1sdkrQhWw25OTrOSVQmzi4fAPvUBL51TrJBSQ0hdwcGne6MWknOxXm3nvoImA4UpcEBuFbTjTGrLtFQtIkmw1maryQCXAgd6Emw7dnOJDNidZjNYXK4blLqiwoSOmIJeL7cFWsUzGbly1ILIODWeby6TONy2KiWeYWGz6FFXcblZecbVfN0y2YB7ZUdlIZcsQ8daz+pjUZXoLgtBb6BOqXviM9FfTHMel3iLYpmz5B7jasYJ51isFE5fq2w6T5itRifeAs3W/NaaRXstjqVyQ8+oOatQq/X1gCKUqckA7tgcUfa5pexPa8e241UfHtHCFPLhms/UjaSG9oQvda2gMck3I+2aOhZu+hYpXpIgMc9xOit1bC6zaEDtFSbLD4e10+39ctGt9/zkuF30XV/sV3tqVeQbioj2MtHiF6FQhyLJMyxGh0AGDTCrKwWdhTBnnZcb/Jhd6XkmsOrZbf0QPra62ZDHypwtXamZ1jqa74vM66PdvDotWzVCzxk6IdVOYOdbXOiplWhMjj2NrRw+NGcInKYVmjjyNizm0TUJGC4clqLnY6ar9nsnmilzvc9WWx5kkHVOFIJbyhLMysfNkDmrFd2a8HQjzLxAn21DlVHoVRwsCUOqD9I8bXMyuKwvxm6N80ZLG4Wka4fdJdvMpzHHb1pugfJansyvGQNf57wUmqCUMnUqFFlA1KmQ6MJUF0+L5Z7KqfQ8C7w1YTSZHsDG5XSeWYiMro1L3fr9CfZh2BYzcyancBKtDF7PGmmyE9OQ0REMW/tzZk5u955GBFO78sXsik8vhNz4WBIeN5kbi1q5TS4e3PqJfIomcrAtRFc8KaABrvY673MB4siXSKg5D16QFL9cUq4BI35nmDGIg1qlwwS1rJSaTYRNWHgFjNlO5JQXLt+QPLaj6VJFpwtKMfGCy8GAQZznOWoq55DsTJI6KDYYf5b6cKBa0P6n8xWHipa3P7dCsxuaSAsPu5YivEovNsGV71mHbKupHiXFXloik6OYDEePrKcXqi0nZ2Iv4ry2OV2WFqNLycXB+7xjBHvdT3pM4731qY97pN7akXWlsN0CLlAM0y+HhRRKfL7LDHtpWcvurM7oWifKbM4I3mKHVlSJFbGL2BnhZVxPcvPJquGqzN3g88PQMsZyS9qL9NBye5qYDPYsdprTxNjOW2sRNJWBBqoy6ASK7FDyqA60fJUrYhf4bne2p9ewRlan5eQycy+nikGwmMfPqnC6CucpVpMEfZz5tHlOHN6B+WU8KWkiW7L+ogpS1iyyIwFX+12vFLx8nXBHStj2xH599Ujj2K3Op74+bktfWjDu0LYNNa03J6yVOUqcTGAngRes3OUoh3ieVx1OsFC7QoB0HkJ5nnzayxc/jrZhuWCUsMw9uOfxFluVEoqRB6oQz8pi69ixrcAOPfe6Ta3Rmwlr4bp7IBTe9GrXFfq84SbUjDrG4cW8sIlHOQzcX0SOG6pUH2h8GukxK+0unb3ZyvNqSEXnOrExZrgIcISv4GC1P6sEW1/WwaVKI4qX17kHcqJiuHlHEOnB2omHE0Zfukt69hwusMVjL+z0Pp/MIy1e8Mx1DafkbIYpTRLRC6pY5T3rhpyzwCk9QE6OVlwRXZZRo9oz2YzItrEollXnyG2G4AHjXdk0j8AOw+TqamuoC8045sO5NOFZTHuW2p6ui8AWXFN2be+6uXoyedKYyTYQ5rAUe7KRJCTYv+wMWGg2uxUupOgphMVEJF1dphPT3vjGBsBs4bUGMV/GM03EbAU5btI9by/tSwNybDFLpomvaUS17KOU5M5TohfkJa5Yu+X+WC9LNFCClbD0uIMM9rW06fRLufamEpYml3hoWT3qsZWwI/eU0KhkWW+WwtC59Ix3Ar8sCRTO8tbf7A6N4fWJk281n+3rlBiWuLe087wRm9npvHOHNDmjlmZqbIZz9kFHrmLuh61mGioRUJua3WL1ItEaEgyGVxoTbe3c9NRmKiiGgVQzo0MdeLc8nJlJt8wxnBm3gcls7xZ92RZzezsPcQzRB7CHdF2mye3ENZlkVaFktlEYrBRF8zKQGG91DhEsAUZvBap1p+mWuTqhKkxiEenXqHFyaVxBPEJ1+1WMY/uWXmE8uc3h4NoKPCoxLovPfJytcaK7ymAbxDkwIq+LxvWEetIK6jra47FPYhf4Mp+UiEJum/CqwDuWb9OjkewuEqM0y+UwR09ycyBMbtmiJ4IWRZWR4J5qSOaE+ooe+lt3Ixn+Qpb0pLSwYhpwHj6Jjzh5UdHLETli1pSjTmRLz3Nx5R9ySWi89tofo7mwJh3xzLRVE6LsoCMR7uvXYO2lznq7WOv8pcs1S5Zmy0wDo7mMgO3Gwk76NrzO0B1jx4cDzlp2nR5wgsHR1Fpqto0fOnmKXqZ0ShZKjlH+jPQIh8xLk10z1A5LZhk/L4PpZF0q83PrJOr8AB8WbLJVNnSFbZLFKTjhOrVpYnnv031MYZFLapcrvWobthRmSEuDQXISw4UvIKDBDOrU8tbFLueqbksQth8OyJmuOkNnxUt1PCruZa8WA7mBj96avxxlXG8qmKaSrutyjN3xvpeB8V+7xpRiFFpeZHs+1SifJxBVPOnqajPPkcVi3nqOQzbXpXaQiEVPMNg28xC1bti1mydTn+f5X355en66vV59esVQgsOfn8aT+sd5+987ivWvYf724EXQBPb89P/ulPB+Yvf+Lu529u2azutN+uvfUfO356fSDoFK9+PbKm78x9HgfzsL/fyvT2jH9cP9HfH42rCv319X1KZ/O0IOU6ep6nJ4q7K4uR0gA2c31fj/RKpRSRt8P90MS/Lx2P4u8unjyPmtzkYyLxzvhen4Ksx1Rl0eP/3HafvzkzOAkIV29UbQ1Jtb5qOdj5dC45Hp+Fbo6Y//AlK/1UT0JgAA -->
