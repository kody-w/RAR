---
name: "rar-cowork-cookbook-report-furlough-workers"
description: "Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_furlough_workers", "rar_sha256": "fd01a35c56dc7fd97167a392b244f108ff3b546266da8c4e82c7ae50d443fade", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_furlough_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-furlough-workers:c533ad04e89b3c143aa386d3799ab8d9353d3945ad3ffaac316295f34ae30960", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_furlough_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_furlough_workers_agent.py` is
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

Furlough workers Summary Report — Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-furlough-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 fd01a35c56dc7fd9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_furlough_workers_agent.py` first:

```bash
python3 report_furlough_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_furlough_workers_agent.py   # or on stdin
python3 report_furlough_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Furlough workers Summary Report — Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-furlough-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_furlough_workers',
    "version": '2.0.0',
    "display_name": 'Furlough workers Summary Report',
    "description": 'Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-furlough-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-furlough-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4ba22e8f5dcd0f3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/furlough-workers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-furlough-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportFurloughWorkers(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportFurloughWorkers'
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
    print(ReportFurloughWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOi2LbvV+Hl/aO6r1kJyJwnOuI5oKIMAgpKV0cWM8g8CvTt7343amZVndN9hogXz4pKYbP3mtdvrb3x9yezqYOsfHp9Ul0zhdZmHIeBW0Jm6kCL7JqVEfjKIgv8h+wsrcvQauqsrJ6enxy3ssswr8MsBcvnTRg7FWRCVV02dt2UrgNVTZKYZQ+Vbp6VNZR5kNeUcdb4ATRSdksw367DNqx76BrWAVRntRlXz1BduqkDvkcprNI1Iye7ptULYOp2ZpLHbvX0+utvz08huH56/f3Jjs0KDD0pN0arBxP9zgOsis3UB4/zHuiagvvcLb2sTMCQ43rQ4+6nyo29Z+i//zu6mqVf/fz6JYUeny9P4z+lSaE6cIGUZlUD9WwzN60wBtK/QLP4avYV0BRonj7MEKb+y33lN0pZDv0yPvvpzuTFd+ufvjxlQARzNOSXp5+hrAT8yma8fhmp5D/9/BJnV7f86edvdKrGurh2PRIDUr+8Pe4fZMHEb1ND78b1F0D17jLL/fL0nXLj5y73qCdY+fRyycL0pzvhvMxaNzVT2/3p578iaweuHcVhVf9bdH+9Ew5c0wE6PQT/+flm5N+gyUOhD5p/zTYHbv1PNAHT39k9Qw9D/RXtm/3/jnQcpm71YfE/JfdnCya/QL/+pW7/bMEz5H15Wrpx2ILosGL3Ffr9Td2zi18/Od8GP/32ByD9L8moWVPaNwpviZmGnlvVb2+/fqpuw59++/VTk4NYc83kDSTPn9H8M7ve+Pxgwcesn35cC/gf0ygFOQx9RDr0e5b/n/KPF0gz49D5Nl69Qt/ny/iZQKMS70zvJvguZyog63d2/PnpDwAM6R2Gxscgy//rvyAhtMusyrwaUu2sqSHg4DpM3FH4QxBW0OGR1F/VHcfzL4nzFQKjY7oDiDCbuIbWpRnGEMiH0eOjBgDPvv5f+waSn+0HSMJ3rHt7B7q3B9B9fYEOAeCWlaEfpmYMKbP9HjJ9N61HPreIAHD5uR1ZATHCO9QoC26EmaqJ3b9BX/+C9tuNzEvejyJ/SYEPTOAYB6rdBMw3yzDuIXPEJKuv3c8AQQFulFkcW6YdQeOfJn8Z7aAHbvqwjg1qgdu5dlO7UJzZQF4vBKj7DBxcZXELMHC0WRWFcQw5YQkMkgGcH+Ea2PV1JPb161fLrIIv6R10MeheLCoYTPgQGPr8OS9dLw79oP6SunaQQZ9+/+MT9D/QP1t1Iz7y2APUv5kJBG4MbVVJhEAWNgmYVkFjCACIuXnp9z/u9h+lS0F1A7kTeqF7WwyofXP5qMHdKe8eATqPIo616sbpR7tB1wDYBQprYC2Qz9Xzl3QkkYGp5TWs3Hcj3hffTf/u4juf0SfVw4bAT16ZJbe5t2gbnWlnpfMCcR70YalHPR09GmRVDQI0B+XSTe0erDTrby5MsxqqQI5UXv8MNRVQdaT81QKkR+MkAIjM+iskLPagpmUx+DMa6MYerM7ScHT8I0bvw4BI+QnE2PydxAskusCaUG6WZh6UZuXe5nnmPSJALXtfD4ibUOpeobFou6OPbtl7i7zV37cF6qNzuBd06EszRVAc+v/RY4zizNZrhV3PDuwSYsWDcr7Hztj+jKrcO6aRHuga7onwrRN4B413OP2SxiGwd9n/7T7Tu4XLfc53Wigz5UZ/TNzyRjesgdNHL5blGKjml/Qdt4HIYwBXIwSB3IzGTM8+GI5P3yUNQAKO999qOHSPp1FpEKlQ3lhxaEOe6zq3oK6DckyZh7lBBLijQUGM28EPWkGAOrA5oA8BIUIQisB2N9OJIPRB33OP44/p4dgZASmcxgbSgtxwXyB9DFUQbhVkuaC9GecAK3y6kYISF9gYiPhh4Sow87swY0v6ENB8+OJ7+z8egaAbywPg9pFRgKbpmDWw5BW4ACRMd/frh5QPTwFRkzG6b4t+dPZDU+j78vK3MauAhN+wHPTQY2X+zjQAisukuoUaqJlRBfI2cR/hA+LgVoRf7nX0Xqg/ZHn9hy78p/+sUb9VxuOPfnuFgrrOq1cYvlev9+L1YmcJKGB2mLvVo5B9fs+mz49s+oHc3Tqv0H8m0g8kHpH8CqEvyAsyPuJD2x1D9fEBFlh8np8/4+PTL6nifnMtYJ8lAEVGi/cAST+qxfsUUDL80vXHyffqUY1F5wrq3A20buj/4f5HagBMTP2x1FXZdyk76jQ68+6rD3AFj9IRtp2xHfPdcYcSj+JX7tNr2sTx81NqJu4/2ZmMuAkCc7wB+xiQIqCrqUP3dmc2TjhaYrz+cbMl3S7MeMyibKx+ABXDD5i8Se2UQKQx7XxQl9zyGQKS+gD+RkWuY+qNJd4CilUAQV1nlLzu81HU+85l7KI+Wqx/lOCWvQB2nOx1TGJQJEE7/Ax9dLbP0Pte47ZrSxuw2fp17KpHncFU8PUx92MvablPv/2JGI8m+6+FeCDLHctNa6x+o4p/ohOgVrpFA6qtM8rzTcFvfLM7sz9uctb3beLvT+/gMV7fS/89oMCCf9WVjaq+V9O3kZ45rrr1TjfNb93lmwncPlbN7x75Ywvwdg/Lp1cAOO7zE1gMehfQMg+3PfDTXQgg/be+dBTJLD9XYxcAg6wClEBtzkfJIwB73zEYh0PnNn+8eP2LZvYfMODVJjDMdBDcpRkLs1EcM02MJh2MYhjToh0GIzAHY3DCdDDPM00bQ8kpQ3gYbroYwpCjSBVwf2I+eMPoaG8g9YdR/92++um+DJSHKUGCdZ6DoCZG2ATp2JTnMBRKUibGTK0pjnsoQnseZhE4OSVJx6RtoMDUpkyXQBwcxzywIR3pPVq8uyxv7+30uwfuCPAGoDIJR0mnQD/aplAcMDNJGygITOKiU9ShMBchGMyjaRcH6z+WPrwwOumu7hiWoLsDvVU78vn94dUx1EgczNzgFTe7fxYwo5mUjltiZzEl6fmHFOasAu2SUuUDa+uiG92xuNl06Q7VKjuWh11kqAnHrCOKWzu1eUVmHjDnecvEAz9E3rqKtw1eNRW3snpk39PtdpJuqkZB2eNFo47ixUPtUGsuFqqjWcq75VR3QqHR1nG1PVHMRPE6w8SGYRblp/WprHdF3Wcyj5C9ZwRGKBhyhCClR66zi5XqKJvruSGRkrLWtMhdY/yS62okd42JObX3q8zZlz1hn4iekTACnWxpxml5itx3TqOxRZTvYu0o15bWx6FaX+a6tmhrZZHzkmMTe1v0Vqp12h6Uo33BdozTLZqJM8EjPi3yVJVofkXKOh9TuRxXp2IXmO3OD6daWNlnXtUDDc80ZOXYZ2EwNYnDdoeTvpoazqUyLU+xVcsNW6QurVgOQvQwV3ZJt1ZQPJA8dC+6ub4ItUHXyKWB+JwuDCvSkA3hYsVH4qRPbCWadZZMmbNZWS5Kplps07q2eSLcKZZe8u1WWiT0OUL1nJkPudnvupNd6nJsrRBK0HSiMWVS2k+N+blA/el0OK5BC21IEeqrjiEqaYVRwAYaXSQsoU85Q+O2SHBYm31UiNaUHzh0i2FnsnbsGXo8CfsrFqbW4GPpdVq2/Pzi7JVJZ6TbrZhYHkEl9pWcOvujGlNi3p0knWw2Rmg450KZtbSVFNauDoSQbSfTRdavdHe9xPJk2B9tGE+Wan/kaWVrmatwv5XJNOKbGnSlWuXistBOOspMcn2laaRpbbo+ag8CCIrlqTzT6pLPjxRTRIPpbRO23SU8jVhGmE9SZMss1FWRT/jDhE3p+UL0SFRRNM6ApT1mEELbbgkmsDdqIGVOaFKSHqsGb9EKzaFd4WgJgU+NHZc7fEGcEUlfww0fsGVBXy8stiV3e51U2RWSH6vYL7cUcm2FSYQT7L7lynC6Y6/xhjN3i7hO181Ot1cI28wzwEI6qOpW6vZTbhmsCYfTrmFxDquSq7bkIAlH3N54aScXuKZUjuduHGGd0uymV8Ulwfs+tjqvyG6jEhMVNso0ORkxf3G2HGwvd2LWHBmSk90DPItdqzwhEWKSME+YJmNotlT0k3UopeYkpFRj2JpDuZ2woUBQx2W4LE6zjaHCOyOd8H6zg/PI7zasu9NrNSwO+uoUsAOmzE297i+HsNjHVOjNdn4piIddd4iHgaIn7rZqNHzVKlvhxOQUZ0joqj2QbdPEmaKq5lFLu2Jbkzi/X0eJvtebwMebo30UN/qgT4qQ5Qw2LGZLZL8vFnKT43yOSp7Rbc5uvsEjhKfLDS5o6mwrChwNxrqlEWLGWZ8m6CknZuIwxCd2H8+n86LvOZgJE50KBFmKruliz0/X5g5gGSZK3FH2k1XCFNJOXhoddxSJNIAdOCE7HK4tnSx8i4aFQ3qKl5Z+4oAfXBZWl5UYDSyx4llmsgw8dHU5IWrMOLze2pwsEQ49Wdd7f0G55GlKt/Dh1FJDvu1n6CbmxfmCNIguIrmTa8C2kCs7acu6YsIks/1FX/ezVq+LoxZy+iDAm5i57ixbIJNtI3AT19KmRGgcVuK+cUEQbVdtnvm1zNXziAM5uzyqeMzMkp0xq7rAmByHDaemCMsx4pVPpmVpomgrsXmtLo+8Gi64WFi6RtT7iMImTImr7OwYXhe1HfTKyY+m5X4xm0juQJzlYwUb2hU/1/JVdk79lLDbi6tTSYcddJxkvNSYwu2laznByNPNaUiRKF4bOi3gmkEhlzOL1AgpiYnX9ocZ6jPMvKeW8vEIUlEkHCklwwk/UALiUls8zrTZ4tyEq1ghCA1bcTIb+QGSG+ZGXOALmouWxxDXJLLrZmKNrga0D/nLeR4ji7I4+aKWJYqjTZVjt1fbhdsouzxP6nNIyQon9euIUeaSuSXO5z7Dtq2czrbM0Qi4mSealjLXwoHoLhV6AUh8MOYbfdcDqMUr7Ox18lU97wt8msBmdpibsdibqbrKbexwjM+lU6dTNJskUn4m14LokMM1zV14s3O7Fk2EZr7eCTRNEaD4YIVdMoJS8ydnut8aogq20kIiL3OBUJWwqcSdF0+uA26DLTyHgLrSwN1SSEyAhaZ7KNN+K+NSGWD7Ot0qorwhWEdsq+1xp20uNdMetVhW4VmKHHhKQVFVWa02kQubhO5EUu5d5ZnplseWNYa5YOjHTUaJ3lFbDBNsPkuIRX2U0KNxUFlJbq4nJdz4Z4IlaRZsSkNM1ojFer0851xxkq5t1RRDKSvdFUklxTztzrNY8nPn6F5CK7aTvEciwaetORvb6TlhnRhzTkKyW4uGrbfyjJCIq9Fk/LG5tNsMzdVVTy5CHakVZ0gTGjkcdF6tlpPSJFxFB54n98qC3aXt1goEZRlukkp2q6lARTXpsPle8cu5plnhGlOK5si1DM3NtsKknrtiqjq4gp23eTgsDD3zI8SdDeqJ9zWenPnoQrugObtvhgS5TEy2FoTj2iLrQ3uW23iL0mtRuRD4zhfPvt1QRALLCJYcmjKr7Elh9ce9B3ugmdNDeK3O+mrVcFNGxILgLF6tjeZ0FJpULTGPGrhZWgaom9SwAhWIxafTjZlOukO2D1iQKNO2GQiH5ZXFXPYtUbjYw7KI29kwDWhQPxM9M1o2a07d4EWW08WBeeRn63DZp3nUxafGUi49XdtFQixJ12b4eOEH7hF0L0ct29VxWEu7kHR2V01UbZwQgmKtza7SOUR5BeCRpkoqQfUNionNbDocUN10WeegH9vhsFltF01Sq7KDzXdqcp5tHWoVXY3NQco4jdWTym9A57uFpcEQ+qzbFa4eTi1ld5xse73ArpezwPNUHQmYoS9XhXQ99Ctuii1K4shkZyKQGE4QrzleEIaqSUVQqgdc7xxXXBwUvVU38+XCkmfYoRVle72c1UenBgPcNJvAhEXsiPRgnNXQEJjC3dt1sOAMUDdj+9ieuePqWJGqIpe0nkhOJO6NSw+nSxRe2LhPH4alXNisyyWbdS2VnKN310NZrNTrSi1bbGVfgzl7WpPu6ShcPXaqARTJrI1sFvGG8gML56+LZEC2FyXtkt0G28j6tlNVFnQRy8aSlqJA7UpZq4R4cLqmWC0nRVQ6uDOnc7buE4pWZX1ILWu58OCFc6QVG+FO+5XDqfK6VqLjMjP4TachyK5dsHrZGdE0bhZH9DybK1EVUdUJnRf1sTETkVXTqbdcY4MVIHKbFdrcYk1a1i8+xcmR0O3Jy6Jfb/C9ZXr0UQkFgCjN1dmL4RV0DP4xN9sVU+hJ0K9VFmQwpTm9RGSUtrYW1gAaaARdX7JI7IMD2LLQE3vRkKLMIdV11VW9sisCfD7fSk5SDJuZNKXXspmdUSk6edvjIWa4dJMxXi+d9AZxtsmcmpDyXt2I29Upinh6YVr7cNcZJLq6GhPuKrFGM6vUOqk0TKh5lmJqdb7mcIzc+rtkR0/hahc2oIMcAinxSXwd2JyqaKvr/IDQZtSwPEbJRYJgc/QYEnFjtwe90qg9yegFrZGnjuQ3vWMxGrYtyhS1QsSzrvjCTD0KReoDgq9Jym6qq8FLvbh07M5bRH4ktgUi1l0REkg0PZ0jZ6NQfo+zztyYyM0OpC69gZ0pXIhA9hjUxaynSk1uo8lmfokGgTyW5GK/m8E9PPf8C2LPqBB1Vq1HMHN9vZcD9LonSylDFhNlwi834YRdkKrA47E5uw4OprUEwmnVxY02AbzSJ/s2w2ZUekXXfl3CE/oiTq6rUx8lBQzDexgv3BMlsLlvzV2M5MEeYhptOwIvD8Yx9MlQmHvshka7XkFnxL46wr68S6PzMkqrC01ksxmCU7SwvRyWk1nPSgUXr5D1VoB7fL8swf4F1xzJQXuBL3fTQKGdpUI0oJ3eZYfG3k0v7hEnu2R+GDjyIHBtXp5tmWHpppzpl/0myIrUQ+p1Q1LhNl9dpMUwR2Scx9ps16kNq5CDyJ2rRZVtkxpl0Na23N28R/QrKc4dURoipTwzU/7oUSS51T2yg+HlKtSdnUjJbDVDV9GSoCbsHJEs10sZumMRnq/rA7bman5RN7xgbRCnXQ6WaBYeSvl+P2/RSyOmVg5vKJjb1lmUXQWYJpMIYYkJVyDHqFuiUseSITrN5916QPo9hx3sajU7tUm1HBiWq6kMbMzK0GyyY6Ev/UuCNpUfzHaDxi6sCT+Wop49MQquDt00XWGgrd+rq5q1uICZo0K0ZwwhPRDw2navMLsq96K3D7xLvb2QOsf4wbA9X64ygLpt7NPImp0u5ye9JRj54LGGkB+vcJ+RBzMB7aY7aYO2mrjEbhAUZt30NhPzwoB3SYURch3SmhOHykFZuVPkesH2p71TiWi9nh4mJIriA4lytkw081hY7OTTGbeX5yviTMQmH6bLgLuU5Sl0Bnpg6r1zRqfxrFmHV7ALL0G/sW5jB9Wbgyg612RqHfV15pDakt4rqGb6NS5S1/I6z6RwgRXwoWGspuN8UEA9fEtKvI9aHO5ushme9CaZn5wd7a15y8MVqvPFZXOqSh9ftnwdM8KBqWNYsVMKxU4tx+k+7HNxR1Mq7poKrPR+zOxoAZOZ1p5OxFPbRAdMcUBHsjgQKrlJsfm2ngwgQyhmyc7g2JMbjNZKsvXnynXerlesvEzj3RKN8TLQ6T3FTYuTrWSkUcCrvg0mSEljzAxh2esOiWenPUzgeb8IfUSKKhSbYnLvEqXT4/jWuNZ13UT6pSto5WznzqZeXpAtvvf3DBYvltKgoh0RkBsmUYvCssVGHwrrwFCm1RzyRLKK6yowlYuzRE7csZ9cA1rauLSOiu5qSbfnYU7PFhoezFZMtqgwesjCAj7qdCLKAlmhdrI+Bd5UJ4Qm9tSM7GIKTd0rxuqI5jmKLmzgPWYp+JKneESFVw6RR2JFNxGZNtgCkwZmlRyIvdasFrKztBd9s0B2JzHhV62awga7zuAwHtLTaY+d1JnkoT27DMDGLDEdz1ywoSiuepml9gCp4ZBfFgm/BW0jTtL6RurhapkIyaA0nQHjwTKzYaWu+oM6ZXp7Npv98svT89PtNejTK4pMMfT5aTxyfxyc/xunq/4Q5m8PAhg5nT4//b87Drwfzb2/PrudYbum83rj/vovZfvt+am0QyDH/Ri2ihv/cfD3d8ebn//ipHVc1N9f1Y7v9Lr6/bVCbfq3898wdZqqLvu3Koub2+kvsGVTjT/MqMbf7tjg++mmQpKPB+13PuAiCEv3rc7G401w9TT+ZGJ8SeU6oVm/3/qPw/HnJ6cH7gjt6g0jiTe3zEfNHm9uxiPQ8dXN0x//CwjdYdtNJgAA -->
