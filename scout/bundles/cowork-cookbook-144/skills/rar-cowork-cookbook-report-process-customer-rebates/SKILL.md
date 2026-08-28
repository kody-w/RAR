---
name: "rar-cowork-cookbook-report-process-customer-rebates"
description: "Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_rebates", "rar_sha256": "7c998568f581a0da6f08874a35aa81905a8a7106f35393090b51924013e3e6e0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_customer_rebates`. The original RAPP
agent is preserved byte-for-byte in `report_process_customer_rebates_agent.py` and in the RCI capsule.

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

Process customer rebates Summary Report — Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-rebates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 7c998568f581a0da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_customer_rebates_agent.py` first:

```bash
python3 report_process_customer_rebates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_customer_rebates_agent.py   # or on stdin
python3 report_process_customer_rebates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer rebates Summary Report — Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-rebates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_customer_rebates',
    "version": '2.0.1',
    "display_name": 'Process customer rebates Summary Report',
    "description": 'Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-process-customer-rebates',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-customer-rebates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac3370e129780c93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-rebates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-process-customer-rebates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportProcessCustomerRebates(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessCustomerRebates'
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
    print(ReportProcessCustomerRebates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+ZOi2Lbuv+LL+0NVH7MSlEGoEyfiIZMgCiIK0tVRzTwPMsjQt//3u1Gzqvre7nvOiXjxrCFV9l7rW9O31ob87cVqm7CoXj6/HD0rn/FWmkahV82s3J3RRVdUCfhRJDb4N3OKvKkiu22Kqn55fXG92qmisomKHGxft1Hq1jNrVjdV6zRt5bmzus0yqxpmlVcWVTMr/FlZFY5X1zOnrZsiA3oqz7YaD+xzmugWNcOsi5pw1hSNldavs6bychf8nNDYlWclbtHl9RtQ7vVWVqZe/fL5519eXyLw/uXzby9OatXgqxf1rlB5KKOfutSHKrA5tfIArCoHYHoOPpde5RdVBr5yPYDx8elj7aX+6+xvf0s6qwrqnz5/yWfP15eX6Y/a5rMm9ABYq26AtY5VWnaUAiPeZlTaWUMNrAOOyJ9eifLg7bHzu6SinP1juvbxoeQt8JqPX14KAMGa/Prl5adZUQF9VTu9f5uklB9/ekuLzqs+/vRdTt3asec0kzCA+u3r8/NTLFj4fWnk37X+A0h9RND2vrz8YNz0euCe7AQ7X97iIso/PgSDAN683Mod7+NPfyXWCT0nSaO6+Zfk/vwQHHqWC2x6Av/p9e7kX2bzp0HfZP612hKE9d+xBCx/V/c6ezrqr2Tf/f/fRKdRDhL33eN/Ku7PNsz/Mfv5L2373za8zvwvL4yXRjeQHXbqfZ799vWosPTPH9zvX3745Xcg+p+KORZt5dwlfM2sPPK9uvn69ecP9f3rD7/8/KEtQa55Vva1rdI/k/lnfr3r+YMHn6s+/nEv0H/KkxyU8uxbps9+K8r/U/3+NjtbaeR+/77+PPuxXqbXfDYZ8a704YIfaqYGWH/w408vvwN+yB+sNF0GVf4f/zHbRU5V1IXfzI5O0TYzEOAmyrwJvBZG9Qz8nWq78oBf6wg49rkO5P8U4QkxoLNf/69z58hPzpMjoQfVfX3y3Nd3nvv65Llf32YaEFtUURDlVjpTKUX5kluBlzeTyrLyaq+6ATKxh8b7BGjo0/RmFuWzX/+J5K93IW/l8OudLaMHN6m0MPFS3abe22SbHnr50xIH0L3Xe04L5KeFA8D4ESDUV2BzXaQ3wGuTH+okStOZG1XA6AJQ+SQb+OrzJOzXX3+1rTr8kj+IFJk9+kENgQXf4Mw+fQJW+WkUhM2X3HPCYvbht98/zP5z9r/tugufdCiA0J+RAAjFo7yfgcpqM7AMBAmEFdDGPRK//f70LRCTg8YC4hb5kffYDDIz8dx3Rx831Kclhs9sDzgYODebHAvYeRY1bzNhalJPvM/GNfF3WNTNzPVK0I+83BmAVAuY882TedHMapB+tT+8ztrau2v91a6sO8QMlLjV/Drb0QroFkUK/ptg3heBzUUeAfd/S4PH90BI9aGerd9FvM32Uy7OSquyyrCynjp86xEX0CXetwPh1iz3ui/51Ba9yVX3wni4BywCnnGeIf00xRw0dtCnQaN9131fY009Tbv3tupLXj+T3qqmUDigCQClQRu5Uyv4+zOl6rBoU/fuP4B0kvSMgvuMyj0Hlb+aAY7PceHRvWdf2iW8QGf/PweLCR7F8yrLUxrLzNi9pl4ebptmn8m9j3Fpkgdy51Ei3/v+O2u8k+eXPI1ADlTD3x8r785+rvnBGpVS7/JBpAHwSe49EafEqqopha0v+TtLA8izOyWBWICqBVk9JdO7wunqO9IQlOb0+XvHvgeuciejQbLNytZOQSL4nufalpMAVNVUTE+3g6z0Jsd2YeSEf7BqBqQD3wP5MwAiAuUBfHd33b4AZoI68qsi+748muYggMJtHYAWDJfe20wH9TDlRA2KEAwz0xrghQ93UbPMAz4GEL95uA6t8gFmmkefAK1nLH70//PS9/y9I5nAA5mWazXAk91Ep67XP+L6DeUzUgBqNlXcfdMfg/20dPZjM/n7l/yO8BuDg0JOpz78g2tmoICy+p5qEw/VgEsy75k+IA/uLfft0TUfbfkbls//YwT/+O9N6fc+ePpj3D7PwqYp688Q9Ohd763rDbAAaF9OVHr1s419elbVp/eq+vSsqj+IfXjp8+zfg/YHEc+M/jxbvMFv8HRJihxvStnnC3iC/rS+fEKnq19y1fseYqC+yADBTZ4fQN/81k/el4CmElReMC1+9Jd6aksd6IR3QgVB+JJ/S4NniQC+zoOpGdbFD6V7b6wgqI+YfeN9cClvgG53GsICbzqepBP82nv5nLdp+vqSW5n3z48lE7WDPAW+mM4ywPdgpGki7/7Jat1ocsj0/o8HL/n+xkqnoiqmNjnx+Df2vIN3K4BsqsIgmtj8dQYAB4ANJ3u6qRKnWcAG9tWAWD13MqAZygnx49gyjVDf5qv/ieBezICF3OLzVNOvs2kWfp19G2tfZ+8HjfvJLW/BSevnaaSebAZLwY9va7+dK23v5Zc/gfGcsP8axJNoHtRu2VNbmkz8E5uAtMq7tqAPuhOe7wZ+11s8lP1+x9k8zoi/vbxzyTNKz3kQLAdF+6meOiEE8hgoBJ8fGQeu/buT4nM7oD4wqoD9K4ckCQwnfIxYWLBr4T5MECvUQjDLIhYkjFmEtVrAuI9gCInAJGxjC3KJwgvEQzzcm+A80vbr1O2jCZIH+x5CLpaOi+BLDEPJxWppka6FrizLnaTDK98F3eH71gQw59POh12TE78Nrfc8fZj724uNo2DlBq0F6vGiIfJsrQwpbkKDrHCXytT5wKI3K16ZZbNfyDcBQ9pREc3a9/blvt/TPXsIxShqD3TBI2cUSwhVRDuNFEcJprdFpt3KcgGLcSNLa4XqHYOUFdc5ceyJcXFrlxp6VB2XVdqVAjpYR8ur5S1pbJe5jib9uTQ2UYqRcy4ir7nu6keed6/nvcFjJ5HHL6aCL51oXswjTVzMk+uqsWMd9BkH19U2Rg/jtY47vbfMbJ2k0koZ2orpLxuGwBvDxK1b7OKuH7k7ZEXg85jQV6UqlroWnmWaq5qh2x/N1lCrKO0La0hi2YVHhcA0GquudJlcm3WVObwer0Z27uBnYnka040c1+Tltj9wDW31y9qImss+uIwH9yLRx9BEKxyn25aTeLwSDp6ZepfqVC3ni6LZc+PWWx6hwjxX6SGMFtp6k6XlLq46agdVuoVpu7NzzYgcZuNyfajtTKpLOjnxt3QsXbtcbA6MWDNNQtNZtDFIh9MUK+uVbBuake1UuhmLCi3j9g4PVVwqz2rth+3WhDtX33CabKR7B1kTF6c+bruTLdZ7vVZA5x4I8apj5v6c1BvIwG4qUegULjO3cVsyMktfRtzTAj6+3Ha5EUNueOUWHcOdne628bdNrjBzm7HkruEbguArMXUSATFJJGlNhKn6cEVvbXnYcB4mRXij04J1WGnUanluToFu08ZG3iwaTmy3CSbIXgpwMspcDJBdSkPsVl+Gl3gwliVGr2Jzda5ibckyElR7yzI6B/iZzEVPHIcuPtYRuR/2pwuBs5VZn+bhyYn8k7mDCoyCDCv3Dmulx3utOgaxKve8gsJ+L6A9UZ33HKzm8+5Q5EXv+zGEC53Dm8s40HXMqXBNNX16kVlLTiuGJu9BLqg0qqvRonBqaV4bPJdzZMSL7ZE4eA0B764l25jSWqU60XKZrREn9Jy8zpmoiCK3XgfXjWTL+92hQXeCsGNMIYkuSAIfCG7lMHKiJvBg0NvyKgy76MpXLH7BOlS+SXF47sqYwiGSR829gYq3JKIlTOI5OO96ja6ZxSVhT2TQE/6egEd7W/pVKW6g5BjbUup7V3YDQ/0e4fszEe437W1Y8dntLEtRrxvdoBILRqjWexuLddfaBElYKRYginC5pWDFUTZnzyiSLudZdseu0bEdogMX7wXGOK/1KzzG5g7xaVh1E7FtLgbvLlutzKH5acvt9iXMu5yyM8pzrgVaWem54S8wkZI2HOBOXk3xFu/EfRakm5u1XJ60s9qrnmc1V/x6Yd2ECQpWucznJRvYI66drwcI2rIjqUp9Y8FUDYWnrSqKpSqtVhwseFudulLz5TJauEKSec4hiQSB7zjd03g7YcdsHDnmulOLeE6GfFQ6AzmqJcfyYmIqhtsf15IsDfEtAcR+IxahsiHBGK/DvK+MLLbADks4HfM1YpQ7BrCouVvtlvJpQVD0dRX11UpkrBu30loKijB3vtw0UC+4e7S6HXYKIynuUcvDytd1y1wvxzEW4Y1Mjh1hbqPaOaKova/kdcIXQqJ7tes0NLuuc3EucWS3tR3qmpvORSUIpHJHVstxm3CKxEtP+jyPGD1ggjQIsVO/HQ6CQvAEoy3y3VnA+p0f4upB3XRLSo/tXTPoZkJUfHahoIbfChl1tXq6qdNC8yF2yfWoKuxOgSPU9blTlSKGK5/x6zmPrgVf3/n6Za1fWkqXZU0y57KJJBhP7s1+MYeUOCUdZGUJwuosyzf8hu23u3IgtpdmaI77UINHtXD8PaSEGxqicXwMl3xfFIdMw0k5z2NSi8UFSUClu8FVVzngNKueeam2x6HPOYES00CFy9BSdsdsSwiCciaqZoevV+u927BwOkS+5lApzBcRUtDsJVPPMiJeD2WJ9NxZUE6IprcHlzLSTSh1HmyneFaJsJvEXKBwBLYrVBTK4B3qX3sPPcnbgooELMnKyyJYb8w0KknVY+Fb7GjlvD9EVzoJfCQsuebcXdf2GeuqjJA0MUNTxNzyTWlgAqVSQaGrq60hO2O1X7mMwhvSOpDi4+hHh3L0yuGGYHzXeAiFps6iXYr14BS0mGwZT8Z7qZxXzHqFrlhqEMC4cZpDGL3bWoedfzgmBs1qNOEbaebYsuHui82Kltag26KcWs2HOVmrIszInQJxR34OAm5JEgxtkEYTK6Jl1WCrl+ZqZynqRTBgrrRJgz2PNmGs9yeMLk/q+ZBqFisf/Ivl01p0MdYMca6SOlodTZPeLGlMtemrG4xHrx0rrVQDZMGf6jHkDlJcbMfzuVhf54Z5wuwjf0j2QXRshUILSRgOx126Ufkh09RCdGIXdcaTcdUOCIpaMEaj7jrd2np9KxPbt8TSGsslBZ0b93apWENG+aDjQSEETbe0A7hfLAX/uKU9SvJydad1l213PmHEAbZu6RCKxiAudqkcnzZMJ4LkGS+SGCGDyRdtkhwZctDE4GxgGwqjSQ27Jn7Z7TB/DpvHi1msexiH3E61o3xJWJ2zodYoUVGa280ta7OSdB65grnnenWWGTTAGxdSENRo81Duuj7hZWnZbOchDO87W9JvKgZ7rm3zcETchmVHtiE+cr18S7psiehptDbLS0/Fl4XZ7NuBEJwrS4eKgdsyLlZn0VvfGsbk9a1phQNxpDAfafBDjWxP6/LQHCxFUfRM4405lvHqasSGq525JTbC7WlLY5jqFaXIB81ZP8LoVbqm0vq0EMcoGfjCPDEUFonHRlr0ess66Yg0x4r3oi0qhJlSmliZUvYB4hQHDkTrSIpr48SUuBrQbMfozDp1d0MQJkfTGiTOFbEN4cq5hufwVezwfVly5dhl/fXWsE3d1UrcqoyZXwi9kPuNcIK02/YWHrPjLeMqrO/8Nc8aN/FYWmerDkjeWZ3Cg0Pq9iEbD2yI0FiXj2dtU6RhJ5434GuY3hfKbX5aarIJmwvxuMs8WDFavevXuyzWhnar7ViLvur7tVhwuKRp8sAviiXmL0KczBSHskQMrS8yrbCaFuvxPjhUF1RcpHx3oZsTJiY3kwpiKTZ1CacvymBfsUE9yUyxO29zomMbkkXXmnnloGIkxgXLRGXFomVJs1YRIvuc03ctNxbHdnPErliGc/RcrW/uZc8Q2EYedGRuBnqf2/6avkFrd3FRC5jVlMVeOHZ0czidaNhUuGVDXrY+LerS4CXL7EafMJNy1bRmodZJ19WeL6BQRfewnus3hUc0I4SpvIgWnM1u0YM+gumLCuQemodeZJRpBS2MjcCikDTySM0zzLHmlEFM54YVgRFFvFzC5MxgdrbKnc0WJq1YXu/HqDQsOVSNLSPZ8ZJq2E1z3WsCHIw8FsAqfg3QcCPIblaOhrDLdlvNFg5LOak88eSnpJCzhev3MmI1sF+motEjwRxMUEerFAqf4E6RLbrQAd4qWVhzuSvElzXbezv75vZsZ7fwXtlc4tATdvL1wmBWq9z2hLAY2CTQMs/b94v6mPKFtGBP6wt06HB5eboFFi0b1qpSDYnfzmmytIf4ml4B74YBWe7D0TkTfdvApeug0ImOV9amxVzQ9W/XCF+ucZ9MzzVysJdcbm/mMjgNrLUBhG1ByjC+CK8r7piblSsdVhSMcglTQpXNcpHtM2ONQ9zpsOxdxjgm9pprYgR3mcDiTBnnVqtIEmhoCYVQEsCXHRSdz/zNTxfYcqsc1rV9O3uup+8JcLTBQbfaLk6EaRxxeD1vV20ljXbID3v84G2I80Wfy7HDtD5zONL4DRoJFllRhrLdZgIDEYjfw0SOoaJKGcP8Bl+0i9ai2nbVn6yh3K0X/CUaL5RkaBx0YpK2t+drduupMbL1BmPMcorR4lvXZfudgjLCAS/Kk3G4JOO8Cgi5MY2qPcPY0uC705Dkodp5ZLhogiY7BMzc2Wa5d7osD1nvd8JWkxUovZ7Q0iyx5KR0Vxdh7I0MhfaCxBab8SjxxDxxhXIwEON0pktnTy4S69DZKaalFoIgOtk3aCFJqrsXEA5erKB0gJXmutjIy1u0qMjmtup7NExV3yPWK2qniizpKaXr7iMkNyF/p+7Xw8o2yDCSttRoR7E8kobREblmXDeYh6JCYJMUFpdzzFdxaFj6F/EqUAoEjj8kd/LpS4uV7KEZA1VGc29xOKkwwZIDSSwZNWBXYs4QN9UFp0QxpiwsK6PNNQ1wQQzs+rI70HVvUjoSOZ5PyVQGkT6vtzKBtgSNlbi2L1Yuq162BTZCp7hHSU+VNrVPUhaDaKOAr8bjiUwjyRKIXgcsNOYubl82nBIuE+jMxZCdCIvechV9JxHRPEBL1/KQQVohFRO3Xd1ztlvWG8U6aiy0w0q5hTfmraguwsnJVCNsdijShRmN8zjO2ObNsa+w7V6TveCs1medpIsddZHnnXmdQ1SMO/PbxRhxXhvj8nqjIqvpR9DIsKPk1bW8Txd1izPaEpyYb8xmjyVlvUSL3QGDJUGw4ghfUHYHhqpNwhz2rHmzjzm38mx22NHbNRRv4MbdSCrNBMRmA0cn4yyTZXODDpJGMpUnrFFtiaWAjit8tJWmIcEguciRPdHSOJYvl/juvGmpytTdCpSDaPDKeA3audhUxK5r5+q5P+M7uyBQzAZ0xJJoZ5bLOaRCUMyFUnBbLVo0dv1j2tMClaJ9GVEWIWpW41vHrdGlF508rY4ifyR9QjonHDLe+hbnShDrU7llW/9WlVrCsQLqCubqVreDQ4xXKF0GFhiZ/Njdujx0JuLi2i+9E705IPWcUnCoOKi9kaKaOcc6i51nWV7Zya7NkNwa05W5QnK13pGnWKKW8RxnBc8rODdnUGc7R5vIJI57bI4F6wtKFSrOivZFMW9qqqUCdM5OjRzvkCZNig2SeghfbuoUcRqLLFcpdUHHeLWyDKZpA4lccV3aZRpadAYBWXtpI5bztpsn7cjCfhMx0ooMrhoTF8Fy3+sqjTdrtrLr25UBqPGSGBZknrUmAu+2rs0EwmbJDnIZNqvDJVuXeX2kchtHgpFQL/5JNQW2hFiDDVDvJqFYLDa1nbvY6qZcHYXyuZWPqPquoCjqHy+vL9Md4+d933/10e10o+3/2f2+x62592c/9zuunuV+vuv6/C8j+uX1pXIigOdxR7NO2+B5A/C/3c/89E8eGUybh8ez0OkBVd+83xtvrGD6LZ6XKHfBlmr4Whdpe7+h+vpit/X0OwX1O9CXu0lZOd0mfugDb4rKBcib4qtj1eHL9LB/euDiuaDUvefH4Hln9/XFHUBMIqf+iuDYV68qJwOfTx+AXcs3+G3x8vt/AWehVAUWJQAA -->
