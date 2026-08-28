---
name: "rar-cowork-cookbook-report-define-queues-and-teams"
description: "Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_queues_and_teams", "rar_sha256": "b5c1f43f594518cff7d260b0df2ffe7e96028f4055616fec13762391c7b558a5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `report_define_queues_and_teams_agent.py` and in the RCI capsule.

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

Define queues and teams Summary Report — Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 b5c1f43f594518cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_queues_and_teams_agent.py` first:

```bash
python3 report_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_queues_and_teams_agent.py   # or on stdin
python3 report_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Summary Report — Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_queues_and_teams',
    "version": '2.0.1',
    "display_name": 'Define queues and teams Summary Report',
    "description": 'Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '48207bc4931ad76e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineQueuesAndTeams(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineQueuesAndTeams'
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
    print(ReportDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZObWJbvV9HL+cOuVjrFvrijIx5i1wICIUAqV7jYQaxiEYKa+u5zkeS0a6aqpzvixZOdKSHOPfv5nXMv+duL07VxWb98ftkHTjETnSxL4qCeOYU/Y8u+rFPwVqYu+Jl5ZdHWidu1Zd28vL74QePVSdUmZQGWL7sk85uZM2vauvParg78WdPluVMPszqoyrqdleHMD8KkCGaXLuiC5i6kDZwcfPLa5Jq0w6xP2njWlq2TNa+ztg4KH7xPdG4dOKlf9kXzBmQHNyevsqB5+fzzL68vCfj88vm3Fy9zGvDVi36Xx91laXdRTOEbkyCwNHOKCNBUA7C7ANdVUIdlnYOvgHKz59XHJsjC19nf/pb2Th01P33+Usyery8v0z+9K2ZtHABVnaYFpnpO5bhJBkx4mzFZ7wwNsBp4oXi6JCmit8fK75zKavaP6d7Hh5C3KGg/fnkpgQrO5NQvLz/NyhrIq7vp89vEpfr401tW9kH98afvfJrOPQdeOzEDWr99fV4/2QLC76RJeJf6D8D1ET43+PLyg3HT66H3ZCdY+fJ2LpPi44NxVZfXoHAKL/j401+x9eLAS7Okaf8lvj8/GMeB4wObnor/9Hp38i+z+dOgd55/LbYCYf13LAHk38S9zp6O+ived///N9YZSK3m3eN/yu7PFsz/Mfv5L237ZwteZ+GXFy7IkivIDjcLPs9++7rf8ezPH/zvX3745XfA+n9lsy+72rtz+Jo7RRIGTfv1688fmvvXH375+UNXgVwD5fK1q7M/4/lnfr3L+YMHn1Qf/7gWyD8UaQEKefae6bPfyur/1L+/zUwnS/zv3zefZz/Wy/SazyYjvgl9uOCHmmmArj/48aeX3wE6FA9Imm6DKv+P/5htE68umzJsZ3uv7NoZCHCb5MGkvBEnzQz8n2q7DoBfmwQ49kkH8n+K8KQxwLJf/693B8hP3hMgFw+c+/oAua8PkPsKwOvrHeR+fZsZgGtZJ1FSONlMZ3a7L4UTBUU7SazqoAnqK8ASd2iDTwCFPk0fZkkx+/WfM/565/FWDb/ekTJ5IJPOyhMqNV0WvE2WWXFQPO3wANIHt8DrAPus9IAuYQLA9BVY3JTZFaDa5IUmTbJs5ic1MLkEKD7xBp76PDH79ddfXaeJvxQPGEVnj1bQLADBuzqzT5+AUWGWRHH7pQi8uJx9+O33D7P/nP2zVXfmk4wdAPNnHICGq72qzEBddTkgAyECQQWgcY/Db78/XQvYFKB3gaglYRI8FoO8TAP/m5/3EvMJwYmZGwD/At/mk18BNs+S9m0mh7N3fZ89a0LvuGxa0Lgq0IuCwhsAVweY8+7JomxnDUi+JhxeZ10T3KX+6tbOXcUcFLjT/jrbsjvQK8oM/JrUvBOBxWWRAPe/Z8Hje8Ck/tDMlt9YvM2UKRNnlVM7VVw7Txmh84gL6BHflgPmzqwI+i/F1BKDyVX3sni4BxABz3jPkH6aYg56OmjRoMl+k32ncaaOZtw7W/2laJ4p79RTKDzQAoDQqEv8qRH8/ZlSTVx2mX/3H9B04vSMgv+Myj0Hub9o//vnoPBo3LMvHQLB2Oz/40gxKceIos6LjMFzM14x9OPDadPQMzn3MSdN/EDmPArke8//hhjfgPNLkSUgA+rh7w/Ku6ufND8YozP6nT+IM3DaxPeehlNa1fWUwM6X4htCA5VndzgCkQA1C3J6SqVvAqe73zSNQWFO19+79T1stT8ZDVJtVnVuBtIgDALfdbwUaFVPpfT0OsjJYPJrHyde/AerZoA7cD3gPwNKJKA4gO/urlNKYCaoorAu8+/kyTQDAS38zgPagqkyeJtZoBqmjGhACYJBZqIBXvhwZzXLA+BjoOK7h5vYqR7KTIPoU0HnGYsf/f+89T1775pMygOeju+0wJP9hKV+cHvE9V3LZ6SAqvlUb/dFfwz209LZj43k71+Ku4bv8A3KOJt68A+uAYlY54+UnFCoAUiSB8/0AXlwb7dvj475aMnvunz+H7P3x39vPL/3wMMf4/Z5Frdt1XxeLB5961vbegMYAFqXl1RB82xhnx5F9elRVJ+AtE/3ovoD14eTPs/+Pc3+wOKZ0J9n8Bv0Bk23NokXTBn7fAFHsJ+Wx0/YdPdLoQffIwzElzlAt8nxA+iZ783kGwnoKFEdRBPxo7k0U0/qQRu8oymIwZfiPQueFQLAuoimTtiUP1TuvauCmD5C9g764FbRAtn+NH9FwbQvySb1m+Dlc9Fl2etL4eTB/7YfmVAdJCnwxLSFAeUCZpk2Ce5XTucnkzumz3/cbqn3D042VVQ5dcgJwt+R8666XwO9phKMkgnIX2dA3QhA4WRNP5XhNAa4wLoGgGrgT+q3QzXp+9ivTLPT+2D1PzW4VzKAIL/8PBX062wagl9n7/Ps6+zbDuO+YSs6sMX6eZqlJ5sBKXh7p33fTbrByy9/osZztP5rJZ4o88B1x5060mTin9gEuNXBpQMt0J/0+W7gd7nlQ9jvdz3bx+bwt5dvQPKM0nMQBOSgYj81UxNcgCwGAsH1I9/AvX9zRHyuBrAHhhSw3MU9OMTQEKcxHKa8MCR9hIBcyA+RMAzIgCYghAoxCMcJmAgDD0ZJAkFp2CNdHKccHPB75OzXqc8nk0YBFAaAAvF8lEBwHKNhEnFo38FIx/EhiiIhMvRBZ/i+NAWo+TTzYdbkw/dp9Z6mD2t/e3EJDFBKWCMzjxe7oE2HtDeuErt0TYRMc6bT9rY2KwVBLsQNJc6xqpyVNq+tEZnnmBgfE1lLYd2QGce81tShD4Hbjis6GzcUszu4a4NMcbSKczSLigjrVvNCaroLy8jLZmFqub++rttD5QyatV+tV75vFUJYt4bmeo6zRldGAuP0gveoS7F3jjJyqy510pz5C0/76jbHj1ddWu+0ZW7P04stomI74IeSgte5n+jrkpT5K1IEKBvjeWDYuQZJ0Vy1NxSt2jdisbOhzsjmi13YzAWRtveNjpuXSyNs5ItJprFzvHqJtM7qY5zJgUdUVohdKCO9lGyCSJ1G1PkyTRf+TTZV00AyD1+P2Li1NoRIH12R4LZWzZdrBbL3h96s8uAiNKxtC5mxsnA8k6lFtL9QHYUccdEZYRu6kCVJbVJzuBiWc4suRoSyOoxFamjuFOtmsYk5iibFnqBItoT6NOYNKwG4QPcUcr7sInF/lDayIChMFmZwsVWKWlLDTZavYqo4kOI+EDxoCExOgmw2P2tXyd9XLmuuUtPD7RweNel2mw/yRrAaERoc5lab5KrPOyNPM8tAr7if07uxOm6qk5y1FmPvRW+VymmDd7KrNJDhqxyFIEVha9sDzKlzr+lgLxyJxm8IFgpQg7GaPEP0M10gznAuPKQtuYMVWpsrvi9M2AGAYQ+pt1mscHuVOX2uc8ViI+gntlK9M1nuT3g4XsVQ5WJ7G2+vzdESaTNOwv6CI/MYNwNXlNJNviM9WtEt0LLGxufWq8CSGhgzb9cKi6RiH5NbPYOUJBtp8HNL3LOR0V269kMwpbTzwswClvOHMoixBavfzrjVBOuo3S2im6DemvlcQudi74kn54qs61CFN9zhFLK7XESEc4ld90ZXVqnZd2ez3uPy2T9SW3btLtgtd8yQnnLQRbtNBG+whiqKthDJHmpJNj3CoCTOOjl2n8vlmhTgMhE6VqPEfrNcCopViQc72Su9SizZ5dkM5EvOXJhE3Ryb8WJIXHJUDXFLZpa4hOe42w91iya2zuMmZKiCzh+SNjI1cuGJOJ/uZP4k0eGOR5CNKRKJdR0k2RpG65wbQVMsdGpoFZuL9dN10UZsDeP+4LgScSxjqiY4ZFWvcKsVl3GyvRWCZ12y0mVOq2SxPhXzTdTtr1V6ZVF+uzpZunUIRN/0a0NZO7hZLoUzTd9WNxwLDO44dMdbS8+veSgj1hrzxloQd/Pt2XPVzCwMZzd2ULlPUgtc3YaV6hDDlU2LnDt0UMVlUJyZ6B6zArVjmhNPXpYstNtFa+wCD+bNkdyGZ3fj4Uzt3SpKeCz1Q9lZ8fLC3Ug3CdozK0MUE9R2YSo/j9mKX60DUagHdhX6Sec4xtZUsVFKdguMv6wzo0K36uFgRJae0Gt5G56qPk4FPBuP3bIqm9tVRatsffabUTmjRsJtLFNtdn5gHxyaXxUjNa4rzrgxzthsLnXL0zlktWsi7gWIpDcouYhjYnOzA8YLRdEhU3jDWvNrc0h2bVGI+1L3ieLm7QXBwTK/R2rR42T/oMkNfSSODi9zK9Vo9iPZHxBsP6gUZpzxU2u70C7f2TaMayU91gq0hayUsZUh5oZjIqTnXYgpxLrYqMdOr7yWllYyy/vCKcbp9lIsjVxH6oucLgneOyc1U9UUO1L5iqO31gmkiRYt91yzRfbmUmCTAJSygvQYWWaxoI9+lQpOAtEOD6tt1hO5E+Ih8EVhjzTRGRAdZsAllYURg7uAsMuwP2fGicyIG7QKoPWaOyMVjnkL68DZthfcEGrJ8OHmlEFUEBribre4biqMzqjGLoYoWNs3Ddpum9qFSpUNmD3JRytOhANmdzR7Rwk2ku5VRxYm9oRVxZus6QmMFSrlZrX9QR6aC772xErKJZsX+HRhtMwJvVGcvw3EjkFtlqbOaWDlkslQMtT42a7DmfmlH9OgFnfhNt91dCItNWgsuPxiWzoed9ktc05ryBBUdn6IF/YqtFPiiPpGyJvwXo/VDrElDnfc6KxW9eGmWHEw2IqkSQkaLm9r7ZgLYkAURibjhIpqklislvxBOToNZqkbZGUGl+2BvmJYcSzzcBiugSizqyZd814GD+ieRkQblVGeGWSICA9deJpvRUfb2seRd9Vals/aZSBVxV7p8Fpa8MqSoi6MkdltSy8OTaUFHMNRh41r9fg5Fhbn+soACORKjmdpxYDdjIhZbZuNTHSsVxcCwGfo9GvD3OWXxLlkaz2NBoHgWkajuN2xtMvsYGY5RV1lbWHk64MjGNC2Hpu0gjbJEb7iuUzdEk2QbxQ9t8hb0JpFK1v8Od9wbp/W1w3vtdfOc/B07+jtJoIJzl6ju3EHS6MEtfOdo7BaZ1+zPaokm7m/RfOLmyfwhlmUSGekZqIUAddrS7YiByvyDyMZkSQv1cpqx592xiVf9aqAsdWa0iCiz/bxCR10BsZ354Ow6U9rT6ZLAeodl1eiJDnr2EHXfGt16DB2eaBhkcOPYWvvKukArR3mgKtX9Cjlw6qHJWcdYfymOMuSvJUy97Q7ETfE31uwKbAFjM9Bj1rg84XioHOtr1ktGm8AVlwUqhOVOxI5DdrYCbk20r4eyPEEmm1RM7ZMBAbluj5hy0KXjTyrnG1icZxrS6bUQGYTo52gnO5Wp35Ll75MxefNgQk5zTbm+HXPI1UeK+vloOyPeNhgXh4mfg8Nc4nPM7wgQq/dZGyUBQfpstLicgVnXaOuc4xYYweFPeAVFZciCJgqAy+zo3/C9/B+RY5dVu80K+L10RhbT78lXnlMirmjQZUcQOnlsmywleZIx/WGiRIwm/RHeLWtWB7Jc2rs1wU64qp+KDJztdPJXZltQz7ZmP5Rb0ShDdlhVzX1MoG3zArPs82IocPq0HBNjx5QUcTM5hQ0J6HJEInNh3gsB6e/OVopY7bDBqSIe2m0ZQjMd9Iuin1/PmcR1Dmvsz1ueek5j0k/HyX5FCGXvd4PZqaX7MXl0yKyS0Vp0JWbn+tsp0p1cFz0egp6E33BmD5UFvjRm682LVemFh/qZbk2dEmxx+VStMWhsVP55kP9ASbyq1dox4uwxiI9JG6RWhjSYOgolV/kHW+nys1g+RWsc1dXldMTVB3nNeZvLkXRpurJy/yEiBwJT1Q/pa8erLWJiiCsEBIcSfTJWG6RkCC0LFo6EVby6yQZz+51f8gZr7QTWFaUgMeHgbmclcuG9JaOZDnLw3ghDrHaIKKyIBCupFWNnwtIWWGxz7GIlq2OLIdIMERZ2h6FFhiuD4x6JZK+XfjRaF6XJR+frjVddoU+iKx8yjzaOiWSW46mVO/Dfpn4pmW1Zer3kYWYYz+P2I4AOwooMggyRXTiAvYNUqXSeTXY8jbfjrona4iaksHqYGe+XPClH4LScFpoWeZgsEej+Xhz9k4lX6+UcEhcwV/E0HpHCM0qa+XFkRVu4Tak2yPhrFBHPHON3he8KJnbpdfaAiqrRI4vF1uQ1SPOgk1HqSL8rrjw0X5J9x4tcSbcZyZzUVyoruE9H658yMdZOMk81JHhqzC/YgE71wqHBPPoxSJOIinGZCf5LrxBV10L9mA703Zb6EDrJ+R2rWtxGx2abdzR4aioyuHUnY0N4tggDJ4ogdLd+Ih5ux09NMJIdUEHlBDZWuYVosa7B2VeaBgS7w0i288p/aQZcxTi6L2iM+N8ZZoXeGEhoCnAzAYLg4s3zFMSF7CWAnN2Wl4wqytu0ZL2Ud9C60NsIRLRWyKWadtOrUNubnPRPiCu18WwlUjWalnGwnYkpS1u0LbFyJu5swekgeSNY8w9Td7Qlpi0qyWmBsnywIKGzVz5TaLGxnx53vrL8xwPBlcDSccZXDX2vLLdybu1RqSpJsluOoLh0RO7k10nJnSDbFC++7QudC1YxEK1b8WtQXfumEvB4Zgd0psCbdYbeb041Tl2OlY4dNxdERNWLpW6WIYwLUAinWwEyi89GUdM1D7alOnpdNY4mmaluNZ25LioOqb3D0oVK/O5kzgHXyqvkl53ZhnisElcQ/g8tuKa6QhmJJjTnl2TW8kgsQ137VBvIRMnVrggV9eVLF4PEcHx8iNyvZ78ooNOMIWUdiDl3FhI3qiiYydA8944LpdhsrJGSDl1suG5vBxvzkLixyua3ewSPFLIrJhXOTGXRW4nrZyChFa3PWQcBtrm1cxYQpG0RGXNnwvL6BpVJY9R5JI6reYrRGsonb7RqTCeoczVRUrW60TXUfrAwQSt6itRdjuGkGCb247k2bFoIVkfZaq3MGa/QXXKxdbCTofzhbmMF26zMvUg3GVgDBrmLIafnaAgBXJXs+eO6m786N1aUvX2oYBub5HSNeIpVJ1j6Tm5fo5bD4IWSschFoFx9an16g522yRTSg1bwgHNnsj5sRv6EzHMQdJ686tmbQBW0tEBsXtlK2JzeGMEBxatN1xbghmy0BzrgpoWrkAwIblmpx+dGKxUen/Dm8QWjYoze2X2AO3GkKCFC7oz+CTaybcFW9jIgT/ju2VPrXAeMWxzjZYoJuYIMuct6shpbrYYMZUhB/IUxoe5e/JhdMvMuwtNIwmMU3OxA+Vt0qOmEL3HX5Vrojq7zpWvgxWYSMQR6maLEDa6s7UDQqjtFQoW8iK0ojMJNk8CgkZteFCXa5Uxj/0lYQ7zyrSaLt+NqBCeRHiPJ4pkKOiJMSkJqhZnBuK0vRG1hn07Ugs0yWVH3WqENdihHfC3eQ6jQnwVrotLoZLGZdfVemAIm2hReuJZWlLcwoJKrbqmsBcc1Rg9gaZLoIqbNwQCoQGSkyVZnXOiCY5OekK1+WmEt0Uj77gYvQqKYcdhuEG2fcgwmScbt8BhamWxJeSLRERoipdB4ad12g9UjYz2qoVqwiSt5uo1HMp6eshSV3vVRC5Ncn3W5wZU9mAr4ii1tKqCrqfTbtxCQQt2SyR9XhvjuYwQBcl1kVCWfO1ed4nROzyRUQN8KEiUx8lc2bZLHOPalcpZQNKakzSfb9meJ8NLKS6IFUMkw+aq7Iihb3jOHAPpeEI3o45Lm0ujLhfUktihCov2JcMw/3h5fZmOkJ8Hwf/ic9zp7O3/2RHg47Tu26Og+xls4Pif77I+/6sK/fL6UnsJUOdxxNlkXfQ8EvxvB5yf/vkDhGnt8HgsOj2turXfTspbJ5r+mOclKfyuaevha1Nm3f2A9fXF7Zrpjwua6e9PPPD+cjcor6Zj44e46SzZaYKvbfn1/gj728qkmB7BBH7itMHzMnoe976++AOISuI1X1EC/xrU1WTk84EEsA15g97gl9//CyBqIlchJQAA -->
