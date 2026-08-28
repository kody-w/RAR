---
name: "rar-cowork-cookbook-report-request-travel"
description: "Builds a structured summary report of request travel activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_request_travel", "rar_sha256": "52ee2a87ae11381aad717c0560331f41a30a3acff274c07dcbb363b67bcac218", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_request_travel`. The original RAPP
agent is preserved byte-for-byte in `report_request_travel_agent.py` and in the RCI capsule.

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

Request travel Summary Report — Builds a structured summary report of request travel activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_request_travel_agent.py` and embedded as the fenced Python below (sha256 52ee2a87ae11381a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_request_travel_agent.py` first:

```bash
python3 report_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_request_travel_agent.py   # or on stdin
python3 report_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Summary Report — Builds a structured summary report of request travel activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_request_travel',
    "version": '2.0.1',
    "display_name": 'Request travel Summary Report',
    "description": 'Builds a structured summary report of request travel activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '588ed0b9f5b8fff5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRequestTravel(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRequestTravel'
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
    print(ReportRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6a7ObyJLtX9Hs+WD3yN7iJSF8oiMuIAQCCSQQkqDdYfN+v9/07f9+C0netme6z8yJmCu7WyCqsjJXZq7MKvzHi9HUfla+fHpRHCOdsUYcB75TzozUntFZl5UR+MoiE/w3s7K0LgOzqbOyevnwYjuVVQZ5HWQpmE41QWxXM2NW1WVj1U3p2LOqSRKjHGalk2dlPctccFU0TlXP6tJonXhmWHXQBvUw64Lan9VZbcTVB/DQSW3wPelglo4R2VmXVq9gSac3kjx2qpdPv/3+4SUA1y+f/nixYqMCP73I92XkxxLn+wpgTmykHniYD8DOFNznTulmZQJ+sh139rx7Xzmx+2H2H/8RdUbpVb98+pzOnp/PL9MfuUlnte8AHY2qBqZZRm6YQQx0f52RcWcMFbANWJ0+IQhS7/Ux87ukLJ/9Oj17/1jk1XPq959fMqCCMYH4+eWXWVaC9cpmun6dpOTvf3mNs84p3//yXU7VmKFj1ZMwoPXrl+f9UywY+H1o4N5X/RVIfbjLdD6//GDc9HnoPdkJZr68hlmQvn8IzsusdVIjtZz3v/ydWMt3rCgOqvp/JPe3h2DfMWxg01PxXz7cQf59Nn8a9Cbz75fNgVv/FUvA8G/LfZg9gfo72Xf8/5PoOEid6g3xvxT3VxPmv85++1vb/tmEDzP388vGiYMWRIcZO59mf3xRjgz92zv7+4/vfv8TiP5vxShZU1p3CV8SIw1ckB1fvvz2rrr//O733941OYg1x0i+NGX8VzL/Ctf7Oj8h+Bz1/ue5YH01jVKQwbO3SJ/9keX/Vv75OrsYcWB//736NPsxX6bPfDYZ8W3RBwQ/5EwFdP0Bx19e/gS0kD4oaHoMsvzf/312CKwyqzK3nilW1tQz4OA6SJxJ+bMfVDPwd8rt0gG4VgEA9jkOxP/k4UljwF1f/491J8SP1pMQFw9e+/IktS8PUvv6OjsDYVkZeEFqxDOZPB4/p4bnpPW0UF46lVO2gELMoXY+AvL5OF3MgnT29S/lfblPfc2Hr3dCDB48JNO7iYOqJnZeJzuuvpM+tbYAjzu9YzVAapxZQAU3AJz5AdhXZXELOGyyuYqCOJ7ZQQkMzABHT7IBLp8mYV+/fjWNyv+cPkgTnT2IvlqAAW/qzD5+BLa4ceD59efUsfxs9u6PP9/N/u/sn826C5/WOALOfqIONOQVSZyBLGoSMAw4BLgQUMQd9T/+fCIKxKSgMgEfBW7gPCaDKIwc+xu8Ckd+RJarmekAWAGkyQQnYOJZUL/Odu7sTd9nRZq42s9AObKdHJQcJ7UGINUA5rwhmWb1rAKhVrnDh1lTOfdVv5qlcVcxAels1F9nB/oIKkMWg/9Nat4HgclZGgD435z/+B0IKd9VM+qbiNeZOMXdLDdKI/dL47mGazz8AirCt+lAuDFLne5zOlU+Z4LqngQPeMAggIz1dOnHyeegYoMCDGrpt7XvY4ypfp3vdaz8nFbPADfKyRUWIHywqNcE9kT7/3iGVOVnTWzf8QOaTpKeXrCfXrnHoPxzcVee1f9RlmefGwSCsdn//z5hUoVkWZlhyTOzmTHiWdYeEE0NzATlo+eZ5IE4eaTD93r+jQ2+keLnNA6Av8vhH4+Rd2CfY36wQSblu3zgVQDRJPcedFMQleUUrsbn9Bv7ApVnd6oBuIMMBRE8Bc63Baen3zT1QRpO998r8d1JpT0ZDQJrljdmDJzuOo5tGlYEtCqnxHmCDSLQmeDs/MDyf7JqBqQDxIH8GVAiAKkAsLtDJ2bATJAzbpkl34cHU38DtLAbC2gLOkTndXYFsT/5vwIJB5qUaQxA4d1d1CxxAMZAxTeEK9/IH8pMTeVTQePpix/xfz76Hqt3TSblgUzDNmqAZDcRpu30D7++afn0FFA1mbLrPulnZz8tnf1YJP7xOb1r+MbRIGnjqb7+AM0MJEtS3UNt4pwK8EbiPMMHxMG9lL4+quGj3L7p8um/9NHv/7VW+17f1J/99mnm13VefVosHjXpW0l6BRkPypIV5E71LE8fn7n08ZFLPwl7YPNp9q8p9JOIZxx/msGv0Cs0PdoHljMF6vMD7Kc/UtpHbHo6kcR3x4LlswRQ2IT3AOrhW8X4NgSUDa90vGnwo4JUU+HpQK27UyaA/nP65vxnYgBGTr2p3FXZDwl7L53AlQ9PvTE7eJTWYG17aqk8Z9pjxJP6lfPyKW3i+MNLaiTO3+4tJs4GQQkgmPYhID1AX1IHzv3OaOxgwmG6/nmrJN0vjHjKoGyqfxNBvxHkXWe7BApNKecFE01/mAE9PUB9kxndlHZTkTeBWRXgTsee9K6HfFL0sfeY+qC3Jum/anDPXEA5dvZpSuAPs6mh/TB7600/zL7tFu67rrQB26Xfpr54shkMBV9vY992gqbz8vtfqPFsk/9eiSerPHjcMKd6M5n4FzYBaVMwgwJnT/p8N/D7utljsT/vetaPjd4fL9+I4+mlZ1MHhoMM/VhNJW4BwhcsCO4fgQae/c/aveckwG6g8wCzlojjIMYaNxwYRtewYdg4jFvQcgWhKOxisIFCBmpYrovgmAXhtmWa6Ao1V7hpGRYCr4G8R4x+mYp3MCniQK6DEjBi2egKWS4xAsYRg7ANDAfSofUah3DXBgXg+9QIkOPTuoc1E3Rvnec9Oh9G/vFirjAwksOqHfn40AviYuC3vdn7N2JcudouXGe8cs56Tk1zo5Z05oIc9QPGVXXNF2IHkdeO31g0eTrtFXYHJ1W8WZLpyG9QFG+Ec8QPUNQveoFit6gJ4wS6spz5ik4bW0SLyBWQi6DK5nANbkFWl7W+Z244rDhb44YtDcfttVrgcUZW82AoBGEQ4lMV8vUVYVOdzYmVlcjqKqltvLqK+9IJRqbQEypiL3IZ1lAfMrIu3Kqbfr6W68E5Q7BRo8sVIaFLYiFYuNtyCzRVFo65vO6qUlYNJY4u19XoFUpdQYJ6RWCG5w76KlMczFgr0aqy5kGyTIbTai9sTGus+1IWL+d5ZGEimku91tpGJmyLen/Du2Znell94Ht+bPRVeJUo7ratleIwxoKsi8zlktt61SMinOZNbqcKiibyzajVPGfpqyFUgZSSzDi0XSRzWgGr3KHM6DCnTlXPnktRjeS4rcPSICos3FHJ1U86irop/G208vNRS7pFqoQX74YYKzvkjzQPqddLz0GokNNzZ2+WSr9VjQvr0yVvJp4UhkR8ugqpJtYY5IdXk700opUIAqyLUlujpoofxa5IouGKaPJlp3fBuVLGeElqyBmYYSxQzZBsi+wv6GHfw0o9X+Jpr5k6tM2WbcoQ+sGsQhY/VlGkcBZS55tYKDVWW5WyYN/kZBjT214mSyK9yEyOMMOOXuCasN+peh+5BD3uy2i/5jGsiZlxKyCDr52Rq8T3NB4soSt/0TUN89dLgjgP6LYO+rGCu2oXY1pzu8xjCboGpGMLuAQ0F9HrWUKvtnTRLWTY7gkxNTBmi4v7tZEuem5ORwYB5bSXoOe5tbiOc6xsl+nI7Fg2tAMDGVOlg5Fb1HYl1KkGN0LBWAgaZ5lkAYPmjnLWN0w680SAbCslMFyRXqK0TNW6mcsKh5xtV1DC6ODU5IrWiAMkYDdK3ebBCvY3KGlI645So4HODuNu1+8SLCFI/0iJNaOOjpoG2/F4WBb4kQxMROfURXxOttA8u8B9OSJ+K5LYpjtdSeKAKnkqwSXGGiNquNAaDvTjcrPK8vNKSCso0E9oRh3xubPNW5OVdkTb1+pFaffzG6sdb/F2H1snuya0vRBlqXjQkZ1x8UzPUDuy2aVdssR9bMDa1eXon2k6ucJIlh16byUL7moXS8IFvpTUliLstUnx2pmTCP/mIzomxW7qXYtBsMocmjNzvakQUeKlpDLc27zihe1ZZcttDpk0bmTqeZ7x+vacaaRwudVH6pIhnOV7ynDionzuOttePgQwaXB2tCOIUQ3XZ5Oqe2J9nXMLhq0Ye4zbnrsEx12wX1F2OxTLIxdKV03Q7DWPRMxljm+NIovgLb6h3d2aDgUsuEolM5y6zCPLOQZJrWKjKSmczrF5WWqL0c6Dxm0DqBSRkMGPBN2Ll1MrrgxuPS9IDjuLw2EoFDYMdn2o3S5nkx8pvja2cLYmsabZb9gREuriMEhoeizExI4pas0mzZYNfa6PEvbWVH2ytrIQJQPpGhtjZwKKikIabAxUMmU6O9GdI2t3tGGVMHO1UHm9cAtinA9xWWwtfW7rSTPcArohFYAetVxndhSwi44yV8X+oCVyXvUDl++pzV40KT3PDaSWb0OHFmsPUyDNC7aHrKgEtUL7A1/p2lVsIT9X6VOesgG9qxkL1jFTLHuE1OkiJwldo45sZx8DXHL43vajTN1LTRsUhJ0ukXUzJjV2kPMUdYlWjWJWuM5HUaxshQp4flNCWY63C4QkL0fL7he679H7CBRYt1j4/Fx04WqxGYlbSYzkFUw9wd4hK02okmiDPOFMmNMJ7JANefGMrVOiF5U/0f1S2Q68L8RFt8LIbVb3ctUp2lgVuWCx+SbhbswSisZzTerxEtroksFW/pWg18VmV9X8gXYjvpXsWExdr3XyQ9Zk3cFzGsVj9TW8b2Gq80XI3ZGXjj9QzmazHfrdEA8e2Nzn67pZ3ejN8oynHJuUylLqGmVA8X0z33hEdKQ0AznI1ko5+agzTxh7OOGGbtHrk9p3+FKRHDSypfZghzF6OQ0ccgs7I6O6zZLllWS55GkhJFrUDTSHMbZ82c/Pm3WsnaxSlcIxwHxLm++j4bhvTitckAZsrjmaVMXshpLG41XNT8qSLK2zOaqU1qk73at8zZSDEPI7ssPU3CkqhnepfQHGamZtylt6XKM+OfCWpx4p1T7rjHRqTtxtzXnayKzW2yypoCQslzSrHghFvtGO51J2vHXqw57NwQ6XvDHuZpvgCTtsLp1IVFWmQBHjk6bExFa2S6jag+2Clfkt3aiU4y0au7GTS0HTx8J0rpDB+HZ9ky81frhCS6QWVVyEhetmIcdOuctZZb6OI7LY7m9A9Mr2O3/0du1VFAhs56S2cA5UvluCfoONYCOrN2xrDWTs2FvSLI9R0YWId9tTiR/Usk5lzDb3ms2uYE8itWK6sc+9Y4KnUDg3sPpwWLO3lX0Otd0x5xG8F/lQxwZvzMjcQV177qXmIREvV4cnTkOEOfOF5eYOYS8PEM5ke+skEvzQNNihs7eldHXsNtwDp0W3C5ysU2JdIbuGgo24q0M4O5KqcV6fdoEomXWk3vw9dSKtHdueObRStVzAjsTO2VVduFPF21q57TviuBKv2pDtqz1p+MFQ51EfG4lORdK6ZIpkSRmgPd7HtFc76i0Qbv5J9kfTsS7bnqq7wojyftQ3p0Mhe1bP4IlfYNoQZ9GIxmdcFTpmzcjj5VTWleIJXiG4y3yjRP4oK0V2Hb2YDDivqOa0YIgEFYLSFmdndHUbj0fWPaawEKtaDLMLeb8pY0Hf6qZpan7GbW1/NRx90KHlCHfiV8ESNqV4VWB6kPtJvzvUWKEJsDYM8E1E1nEn6xcD4sVcI3YMcxBskrOlzKjwg7SRslJjrmFY5wTRaYN6bhp3J/BxiOQYMSDMLoo6AzRJSn/qT/EVz0DgtZ1hnPCdlpy38SKhyzVpYd761i/JxMEajuPoLF1DbOFqFAzTpQ764WW9UHeadbYjgjQE0KEE12Bpa8Zxc+Jv1qYc1brDMN3pV4dFNspNFApNsVe7nC92Oqb3R451JRxqb6rFRETdA2xMJFZL0GZSi9yr+8SEDicEis7lkXRd1lIZOYAwYUtfPT6j4VO03hQ63kB11PHE+nArRT1F/IZWtyq5pOo0ojwDlotmJyiZCF1TpD0yqH3zITLN8gu9CLbqbq8PVuRpnOaip5tObaxLW7XSie/n3HXb6hBn9DtBis7CuoZpCJbOXb/hC25IhNoYjpd8hLmMNlHqGptXlqpiW21q+7Yo9Y7Gc5gMFWQTBiPPFAXnYftoiRjlziKhSyGdLzS7hgJ8KXhWnTNYvSnnFIJfmrDAvGHeQDek2SjnC7+1F14RjbrZXua+7F5t70DkW5PcBGUeHuqQO/cSrqqeHUii4akDgK4G/WZXo6nLOiubl6/Y1rq6zHocE5qrVgaZbPccKhfzCqZCdzP5GPJStbiUtnFWLTUBiSvEMNpa/BVdRNA6MQnMYuJzazsrc7doqKLBRTTaUDrSZ2bJ7jMVOrgQ28pJSmf723Ubgy1Na4feZu/JVdzq88xzSJs4SmO5vu1EIx5hne3Lju0rGyq2zDjmOrQeh5A7bBYsSruBXBpXsxcKAm6FTgvp8uotDHK1wfZYcDjjjDLH5itJwzHPILvRRi/xEsX0yndirkexds7CEFEdl47EZ7iyXiywk7vmT1GO5+1i0W8WnKyg53Qb2deSxU9Wnh+HnmRbmMcFiOfSZbaHsnEhJS6M15Hrn1cbNzpbHtgsDMXJa7D9KRSIkSNoaXcUNAFLU+7YRuNxLJu9LZYNyi8xdg+F8FVGao7HWObY4doBmS+tcytJVjZuct6zd9fbFa0Xylns+sLsLPJoFm1hymt7TmDmsixhnFntkZWMnceqbZpTgyWYst1rK588nGMqG+vENRuKUsqw1PWNRbBgP3qU51IIyqKyOActPF+UHFdJN+mCalzFDAxzQzApRdGWO9mpPu+hjtnfkDaUgz1NtmYQSuPavI3rpjwVnO7gp11qErtlmKP6EVvYS1msMJglU7CFUQAZHX32ZkDznbQcdqkqtxD4hh2FWl4Xpe1VtNwY3ZFD22BsgjRaNXy+8q1ck2jJQFbrYEuGonriW6zmRC/dnV1o6++PnGKd5qQlXOMSHyB5M7igkW2LQT8ej61IoCjm1SQGW/NtI0DJMXcp1ucji+eCOuus80gtsooqWLpp3bMRrOZkvwzyerHSYRY+hKMD4yZ909f2EF+xYDnYGbYSrnrqFPVFHALT7jIuFYIds10SecM289gBbW6ZI3OlqRHcyM8GIzHuzesSac3uK4elq+wkLo6uqu+3Pa7PYVNn8XWMoRwSaOaQJhtdteuRyKrVXuld/WJC+OmmcVB58Hq4TCstDJa4Z2OHMJOXG3XjSGhRnwMCJNkhJAPPXcjrIZUx+JStjnxP7GJGPLeGUbqW0+KnJQr2fYzd1hLlga2cqC84HK7i9Oamm2FVpji6J80eU7D5BmAvum62OCmLeE6ZmYvfRDew8WHJLaHLTbc7Dzk1/pLoJMJFm4VOuJxLc+tyRSGoV7sqQgoSCWtdEZDqPJeuTROLw42KjBCEZc+WeYKv5WG+x1S3Dwwq4/mTUxZYZblcLzMEO9/Ze3OPCKhn3HYhsTb03kSN3K8go60L5hLPB/Kw4sRyIN3NIvb3mHLTN+k+3WQKohdNXZ8VvHTqVrzVZZNLuHYKVW+/uYbzcQk712xrpxvM2cqW2h/mPDu3pBN5bZgd1tSkmhw5MRDKtVIiOkyO2Sj4h0NLaYixFCXAqidbG5xc56QDbsxxgdDZgWrRdqQ5Sj8qJeVmYipZpyRZ4WdY4Q6lvEJ3h7ZFDrkoUQWtocWFKTOIUdqmavsjdQovLaIE2MJYXk9Yl8OVxJF2xqNNCcfLk1bscydTyNTEQzJdyLubalCHZb44IHSGc/skkRbnBlixi8V8fuTdbmuHxrVf0RZJkr/++vLhZToGfh7m/vP3rNMx2v/aad7j4O3by5v7Kapj2J/ua336b/T4/cNLaQVAi8fZZBU33vNQ7z+dTH78y5P+acrweEk5vU3q629H2rXhTf+C5iVI7aaqy+FLlcXN/UD0w4vZVNOL/Wr6tx8W+H65q5/k0zHvYxVw4Qel86XOgOI1uHqZXrlPr0ccOzDqb7fe82j2w4s9ANgDq/qCrpZfnDKf7Hq+NQDmIK/QK/zy5/8DOz6R44kkAAA= -->
