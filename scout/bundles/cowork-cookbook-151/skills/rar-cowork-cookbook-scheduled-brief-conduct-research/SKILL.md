---
name: "rar-cowork-cookbook-scheduled-brief-conduct-research"
description: "Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_research", "rar_sha256": "3789e0d755f8a80417eaaf867365c0db90f81a5a5bc47e9f0b59eae9e303243e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_research_agent.py` and in the RCI capsule.

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

Conduct research Scheduled Email Brief — Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-research
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_research_agent.py` and embedded as the fenced Python below (sha256 3789e0d755f8a804…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_research_agent.py` first:

```bash
python3 scheduled_brief_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_research_agent.py   # or on stdin
python3 scheduled_brief_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Scheduled Email Brief — Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_research',
    "version": '2.0.0',
    "display_name": 'Conduct research Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af99ca48f33971cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefConductResearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(ScheduledBriefConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObWLbnV9Hk+8Ouh52IHbmjIkZCEiAhsUqAyhU2q0Ds+1JT330ukjJd1dX9ujtiIkZ2Rgo49+znd8695G8vVlMHWfny5UX1rHTGWnEcBl45s1J3xmRdVkbgVxbZ4GfmZGldhnZTZ2X18unF9SqnDPM6zNJpuRN4bhNbduzNkqxMw/T62S5Dz595iRXGs6pJEqsMR3B/YuQ2Tj0rvcqzSieY+Vk5qwNvupFnaRVOTLIu9cq/zYCU8Jp67qzOZmWTzlzAbJgB+s7zonh4BYp4vZXksVe9fPnl108vIfj+8uW3Fye2quqHYp67mrRhHqKVp2SwOrbSKyDLB+CHFFznXgnUScAtFyj/vPpYebH/afbf/x11VnmtfvryNZ09P19fpn8KUG2yoM6sqgbaOlZu2WEc1sPrbBl31lAB4+qmTKuZNauAG9Pr62PlD05ZPvt5evbxIeT16tUfv75kQAVrcvLXl58mu7++ADeA768Tl/zjT69x1nnlx59+8Kka++YB9wJmQOvXb8/rJ1tA+IM09O9SfwZcH+G0va8vfzBu+jz0nuwEK19eb1mYfnwwzsus9VIrdbyPP/0ztsD7ThSHVf1v8f3lwTjwLBfY9FT8p093J/86g54GvfP852JzENb/xBJA/ibu0+zpqH/G++7/v2Mdh6lXvXv8H7L7Rwugn2e//FPb/qcFn2b+15e1F4ctyA5QLl9mv31TpQ3zywf3x80Pv/4OWP9LNmrWlM6dw7fESkPfq+pv3375UN1vf/j1lw9NDnLNs5JvTRn/I57/yK93OX/y4JPq45/XAvmnNEpBtc/eM332W5b/r/L319nZikP3x/3qy+yP9TJ9oNlkxJvQhwv+UDMV0PUPfvzp5XcAECmwBmDA9BhU+X/91+wQOmVWZX49U52sqSecqcPEm5TXgrCagf8PdAJ+fYDTgw7k/xThSePMn33/384dMD87T8CEqzfo+XZHwm9P3Pv2hnvfX2ca4JuV4TVMrXimLCXpa2pdvbSeZOYTXdkCNLGH2vsMcOjz9GUWprPv/4r1tzuX13z4fofy8IFOCsNPyFSBha+TdXrgpU9bHID+Xu85DRAQZw7Qxg8Bpn6aMDmLW4BskyeqKIzjmRuWwOysHO68gbe+TMy+f/9uW1XwNX1AKTZ7tIcKBgTv6sw+fwZm+XF4DeqvqecE2ezDb79/mP2f2f+06s58kiEBTH/GAmi4U8XjDNRWkwAyECYQWAAc91j89vvTuYAN6CMzELnQD73HYpCbkee+eVrllp9RgpzZHvAw8G6SZ2U9tamwfp3x/uxdXyB0ejQheJBVNWhNuZe6XuoMgKsFzHn3ZJrVswokYOUPn2ZN5d2lfrdL665iAorcqr/PDowE+kUWv7W2iQgsztIQuP89Dx73AZPyQzVbvbF4nR2nbJzlVmnlQWk9ZfjWIy6gT7wtB8ytWep1X9OpM3qTq+6l8XAPIAKecZ4h/TzFHLRn0KpTt3qTfaexpq6m3btb+TWtnmlvlVMoHNAGgNBrE7pTM/jbM6WqIGti9+4/79Hfn1Fwn1G55yDz98PAe8Oebe6Tw71vz7426BzBZ/+/xoxJ0yXLKht2qW3Ws81RU8yHB6epaPL0Y5ACDf8pBlTLjyHgDULekPRrGocgHcrhbw/Ku9+fNA90akqgjLJU7vxB0IEHJ773nJxyrCynbLa+pm+Q/QmE+Y5PICyggKOHLW8Cp6dvmgagSqfrH+37HsPSncoZ5N0sb+wY5ITvea5tORHQqpzq6hkCkKDeVGNdEAKf/tGqGeAO8gDwnwElQlApwLt31x0zYCYIiV9myQ/ycBqKgBYgSkBbMHZ6rzMdlMYUgQrUI5hsJhrghQ93VrPEAz4GKr57uAqs/KHMNKk+FbSmWGQJyNg/RuD58Ecy33WZ1AdcLdeqgS+7CVxdr39E9l3PZ6yAsslUfvdFfw7309bZH3vL376mdx3f8RxU9SNxfzhnBqopqe4wOoFSBYAl8d7z9NGBXx9N9NGl33X58pfx/ON/NsHf2+Lpz5H7MgvqOq++wPCjlb11slcACTDIkTD3qh9d7VF4n59l9vmtzP7E9+GmL7P/TLc/sXgm9ZcZ8jp/nU+PhNDxpqx9foArmM8r8zM+Pf2aKt6PGD8TYQJUUM728N5d3khAi7mW3nUifnSbampSHeiLd3gFUfiavufBs0oAeqfXqTVW2R+q995mQVQfQXvvAuBRWgPZ7jSUXb1pvxJP6lfey5e0ieNPL6mVeP/GPmVCepCpwBnT7gZUDZhx6tC7X73PO9PFn/dl93oCQOBmX6ay+jSbZtNPs/cx89PsbfC/b6XSBux8fplG3EkkIAW/3mnfN3229wJ2WvWQT4o/djPTZPWceP+qxFRNQGPHm7p39l6ek8S/MAFfrlev/CsT8f7Fip8YUdXW1IvD+q2y3/Ly0wyEDlQcKCKAjQ1Y8FcxQE7pFQ1oeu5k7g///TAre9jy+90N9WNL+NvLG1Y8Y/Ac/wA5KMrP1dT2YJCmQCC4fiQUePYfD4bP9QDdwGACGGAUvfDmLkUQPm3RcxyhPMvyaZLCSMKZu/Zi7tOIRViE7eCUt/DnNrHwLG/hYXMMxTEP8Huk5bept4eTTqhlObRDIbi7oCzSAZQ25ngIirgU5s2JBebTtIcD97wvjQA0Pg19GDZ58X1GnRzytPe3F5vEASWHV/zy8WHgxdmyTdjuAw4qY6i/aHBW5puMIE9tBHpvTLfb43lJdW5cb+wr0wyKMW/MTKgOsX82xRWkcMTKT2JYvaBnFIChMs4LPrNut57TIkocq3Ych/EUKNtoXmtEgunhNr/svLraI0SiEzoWOOUWOVGFnPaeRZ10CcY6E7ve5vP9DuSVYOhUsrcXZ4FNbexE6VBa0dtFbFJuecrqqPBi5jJPctVMCOGs0Xpj78gTKqz7LCSF00m8GNUKOjexneULaRc7EoeQvm/M8do4byGh6K22tFGhZ4qiU0hpr1Qhil5y64g1cGibYUScD+6Jk+hVW6OIhRYXw9HkwkVKwZMwi7G6OdUurxuT29kdIZQhWuvCeKougk6Gjj6usrxMj9e96Ka7UwGdbf3ChDevqOvilN3Wl5tWcyhPeatbg80TKl+QGWojcj7gAx1dInJLCYcddgNDriH22yKXdsZlrQ9MkPeuQWQqFRcCSqKsgPvpxl051DzBrkuWrDzl3IjDtvMjOeTOtVvOOy3OSoqHze5A1kV8AuM8eV77qRvG8pnIL5Ejdfm+56mVCycRTfZuWJUXPMntxXWu+jgmLpIsc/18PNkrzwg9cZB4qwi1Rh8jYnXxBExCkEgfKprmVnMzzOaZEVdSBwXHsJYrA2NxX1tc0UbdtA4sCzGpL5S5eiPzeaygokRX1r50k1wIk9ry6kOn10wryr44F3W8FrqTCh2bU9qnY0AVupynCS+sfajvyw2/skd97/YqikkZLILhaHcJ0VE9Gyqusyp8gIUMP1DV9hDtjCEkqv3maJjp0T9JR/m0EZExOgq0U1UsWnaM3Z042pLwyMXp3nP3p1yGO7dpdj0MVxi9oQbH2FdQdaPQJB6gLRR76H7Uz/rBkFVVSeZofQxVx+FXlSGiSo+FR81JqWigyDYohlLtsKHC5ThilXm6yRKG0ENue0mii9kymW3vkLI4Vtcg2C7tCx9l2qAp605x+wOpbGQIc+Jsb+2sc6074zm99kfu0KpwrDVcvVgfjBiLeG0FHQJeVCB2GfFKoJU0Q0WGQis8fhixY13MhSai1quxk1y7PA9aq1sw4nTcoe9Rx9Lh/Y5moMpu7K0JG9l+yV4VyEBCzeVU0jLHwwmxGXpAjtft/uKHRtpwnOEaskYel3PmWEVWUqhKsU6ODhY2Z5A/euNkKNBi0UY8AUXYIKni7bALYJgqvV1RtGCz2eiyQdzIGwp0YpIKRqlzsKd3JqJTy+2J2uM1rco8IhbUuRKJUC39ObM1DLkrV3ZXHkZZ8gJioYQJru6Nc2I1wsC3kJ6O7sJ0Tfh4wG6DZuz5NEnJ6xbZXFzEXjeVwBFkmh5q87ynnRyd82dVTALUPcNLlN1AASKOLBmw3Q4T6+N5qzXhBcFKtxcIspFW13ZfJXFXu44nEQWVnyuYdKP5Yk4FPXLacppJJdDxSqgkr0R670TQkuHXgbOFBxW11t6cSjHeS4Uegn26cVaLUztfimvcWS4dYStrW6SNkqvE7Baksi5hPVdFLWuu1zrQcStfsp51Lc4I2qM9wsrcxTPw9tiu1jaYgojDeEtH+JiUCRsr1gFz2sZLBOkiXFYtH9GbnXzWCu5URh694klJr5QbwHVsxasAfKxNsEIpA3TZOTUPtuZyEexyKNfx+VxgE6uQPNZ2qLxbsptdedyj47KOzaEcna25sceMx66XPZqr6yBnTmy3uIZ0s84YSu0KWRCbNhRouikRkm6Z/dncwKyV9wgMLfKdgh59tt5XY6s6zD4nj4zArxaw1W39BS4tuYxfX8zA8eE8391gooPL222EF7DpXshA2gp4Rg6ifrb7WmT0pQZvgu2abaCYP59Xuy3ZupeL3q2tuHJxPQrmSL7qGKu3wBh8LbhwtPpqb0V7fb1Qzvs1cTQDDB0zduHQO28FM5vFKa41VkyRVUUXFW0fYC9rg5I/yRUh2CZ/0S4cUiGjw4/MmRNHo5J0JzkYykLH8WKlbsPTCt77HL/m6vySL3rT0I6k3oRhe7H3ruA4+2KBHxhkG+KjS2VZwYzYaT4qh7LK637Tr1RP9VNQ4ysergUkrXqsOBryQMJtnu+JgwGGntNNPmL8PDctattjAW6tnZGW1/ubcoFirJeCeWntElLgtvousHfzc6GXjU4yTkpbBM7Iu41F70RX0ozrcSVU60ZR/H1conQ3XvbMjV5ASFHjmn3ollLBlbmKOWuBMDc3xawNbbHGFi1zwveEUaVe7iVOtgy9DsAuvC1Pm7bXVuogXOIkGqmonW+FIpVXY5sMlnGse2bfpbKRsfNlnrRpP/KQViO1Nl+Z6tmsji1jN4uTuoLgzXBWBFTdcXu2OPA7cwkfCBZZS7btGctj4TRoG24xOOHRBYC4Yhthy5Zqbe6UbEqISOddchLKqJaHOs1wSeRvckOXp5sfOlyMyREekyoZVWlQ741uOBt9tqS2Z9dcEFdNxWXY3MXBHCdYNlEtgbnt1slYxNebLN76qqOOI1ZfoOgQHk7Jsjoe4H6AKKB8xA1yuiEc+iZvIt4DvlpnlnBBBPtcn1cy1m33LAzDaRjbNGey2u7g12vMjFaodEzAxWq57uxRuOVcVMHNyBF+SlI4cwXCbQuCLxmztPo+CKwrLy5Ihj6sDptB45lhbmnigTqfhwZslfibc9le2QtfpYPTtOVA5Egeqdn+ujyhG/xC5gfpQK+I3thvaiI7bwwOsWMGPyIxE+VFJKDmEr0VMVqf51vNa7bCjWqz2FleRRnOG0KpjlZkqYxQJKy1Y4xcQlm1dkRkE4meLMwhq8KXPFLta/nGKYichRmk+sj2ZuRWXieevbs08uk0grbaYoxoGpuBPl+svISuyKisB3nexweTUHP7Sk0TUh4Em2xXarrqSJKcwVcRERFDXm4SjicXbnQs1OEUmo6wOVcyfLK0640T6NWWgBXT8ys1XYgnJZZvI+oal9upaLOjRQq9GtgiT+3H89i660V8oLdQfuBzGWIZd4ksLm62qfG16dlp4Gg7o2SEvS4uXMne1VBB7dlb5WYkpWn1yh0Czh/yYd+X2C2JeR3mux2OdJhyvHi7tjCOq11Wba7OFm8GsTCSq07ttSjXbEtGVlyjO+tFF8wPutEajntYZFVAHqzUXDokpLYbL05MIbVvyeXUFNG1XFB6U7ChfEQLodqmsghVS1ZdC4vdQK+0UzPyZ2S+4PbuhnY31lnhTXogU6n0PbrjmmiPI5quNEII89n5VGqEXLASOrIrIQ2aIXC7ZjM6hX2oUovzbKovJZ1otyxjHknjgni2z2xCQ9HZotV2wXqJsWG87k/reg+ddm13vm2wdRyHC4te3aQ9b0GpgC8zmSWMHj47Kph33bpUovnOjtRNTe0ys2VVAUHJwKb8wnZMR0WLcD1WzG2UNMJatqNTjbzZ4L3mhloedqtDAZ/KFbPXVhelcaU9dryp2XrPcUvnsJS7raIEy1q+0Gd8VC/ymDMS00moQjqLMoQVvpa3rbyUunVYwjzDVKioSsh1ee5yJszlPoWIjbg5uqZ6Mo1YCwqPxeu9JTLW6SA0m0uta4ZEtRRHUTjtumuEwJ20NcC84R/2fMFsan8LhgjYIVCXZpQDURx0VjpsUSdiJf3Gd6hJ+y5Dkp7iSn7ZZLzIgWlIpKGxW3ihaHPhegGXHaEXoIuuIFtQOpol6Vu5VTLlVnfWmV0QhLXfznX2SrTHNZit9itlj6MUGDhK2SiLvsgbC/RKebgO/M0VhmZ5mZ8xusWlJpFvy9FMygFsuwZyCblczzGrcOPRV/jQ+KttylSFR+8VooQwlejNQqI2I4Ue0YzAAJRwAc451HpoI5jfNruUgLerqGwdcT7qNB6nBOjX0FKCrgl+1tl0UcK04XdOTFlSI/r+UVDNVByCOit5rFtnBwX1lJg2qk2TDHi4SRzgLxiXcz6rWUlCj8K2YFayVo9MIvEGzsaec8LCK3kbEg9xU6LT9gs3bAxl2LBzALakS4jKlZYqtigvPLls0iMxdD578EnV9PAja4sinF0T/+A7kHTii62PmUrJw716XCAIZyrsbdFkXujAApU5LNhjnlwssko06+aDZ+KbBYGh2NU8BGwBGaahaijBp5mZapXo5n5MYiRF2xynivr2jAQpvRlPGwMyJY4iubESBwd2VscAQbmTdguFZLmmwrAZQ0qXwNRkFie8CQ7rMukGER9kaYSOKCSvbWWnXWOUQg5xsVvTWumq2oY7URvZ4qW9gO4RT3YHihZPw+GU7laB72fQNvU3edl7ki/S67pY0U4XjWlXHI7OtuYjaQX8ovqhJjTezu2xlF0H0nHfI4u13q8tuBg02FJwGoLCUDRhAFPm9nSgI1erNIeLlLmcJ3XHrFbzBXEB9vFBfcLP7g0yT+yWutkJj1CQa6jK3JhvfOzW9HW8orakENs3od1Bo2xGxKCHCBte4sWQChvfyw+kZvAm3HEYWd3qI+I0YB8KmtN82Pa8IxPeeFDptQ97nAM5tYlf15CP8p1eFpIAZ0eiLcGOIOBKqsuvxlqx3NqUhhplOq+nLU5okxb3qAUjrDci2G43bLZwuNAlF9KOS5YmEwKzm2WKmNiFNtnTGmG5RelyqQ4QG06pIT3xBNhzdBDSLmm0QboA65dW6/mnhrsqdCVK0M53q4blhuWiYQg6CBcs5LEeN9Cu3lPKZZToRO59O0CgFW63pyTIMJc9chh8xRsS4doj7vQ3jFzD9DEyaaR1zl11KclLZciFlYk0f7osRQ8AMJmMHCyZg6Yb+oFdIa6DuNRWF/xQou3kajHqKS0gaNf6qXTarNk0UBrpRHj2ltZrbNu226q6Hbf0Zp5ejfPuViQAQUVBuy37a+dFmbyFLF2UxKU8VsPWz2t+5wVYR5YxdaE2jdWf+Tmvoqs5PASLFExhy76DJDJpyC5t55hnifJSbzZHvKmXSHIU7c3ZIBLDHAslVZLLgRwcNkXTS0ee4iOFyvWOhoflwb0oCDx3iWpBL+lWWm6aonOQhllsBcc3iUOONLeCbVxjzSXaAvRq4mofenFnYjtrK8QUGPRjFS4iNoND0Dl9X6LAqCM6RxRfx0uhH2ovhVchnyRWv2Tctmg24m4bLJQ4asMrbTj1GJBQpiWSPMZggwBGLuMEQYqv+xd2uITRcrn8+eeXTy/TSfTzPPnffkM8nfD9PztofJwJvr1Xuh8le5b75S7ry7+v0q+fXkonBAo9DlOruLk+jx7/7ij18796GzGtHh4vXafXX339duxeW9fpL4ZeQkBf1eXwrcri5n6Y++nFbqrpzxeqb89D65e7UUk+nYD/nRHT+XgGTM3rb3X2LbHA9naiCtPpzY7nhlbtPS+vzyPmTy/uAGIUOtU34NVvXplP5j7fckwns9Nrjpff/y8mSko8myUAAA== -->
