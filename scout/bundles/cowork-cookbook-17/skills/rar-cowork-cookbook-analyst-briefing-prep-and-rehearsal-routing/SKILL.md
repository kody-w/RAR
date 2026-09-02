---
name: "rar-cowork-cookbook-analyst-briefing-prep-and-rehearsal-routing"
description: "Prep the [Analyst Firm] briefing package and get the team rehearsed before the room."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing", "rar_sha256": "8413801950006c8334bc6c08e142f18cac6ff0402eb0858fc3d65ab1ec33d313", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "analyst_briefing_prep_and_rehearsal_routing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/analyst-briefing-prep-and-rehearsal-routing:0e88817d9b8474947a61e5abe1f9b7b2b3e1d45de269404eef24aeaa07427380", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "advanced", "read_only", "automation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `analyst_briefing_prep_and_rehearsal_routing_agent.py` is
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

Analyst briefing prep and rehearsal routing — Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyst_briefing_prep_and_rehearsal_routing_agent.py` and embedded as the fenced Python below (sha256 8413801950006c83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyst_briefing_prep_and_rehearsal_routing_agent.py` first:

```bash
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 analyst_briefing_prep_and_rehearsal_routing_agent.py   # or on stdin
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyst briefing prep and rehearsal routing — Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing',
    "version": '2.0.0',
    "display_name": 'Analyst briefing prep and rehearsal routing',
    "description": 'Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'advanced', 'read_only', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'analyst-briefing-prep-and-rehearsal-routing',
        "upstream_url": 'https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '033e08f333f9f0e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/analyst-briefing-prep-and-rehearsal-routing', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AnalystBriefingPrepAndRehearsalRouting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnalystBriefingPrepAndRehearsalRouting'
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
    print(AnalystBriefingPrepAndRehearsalRouting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6eZejxpbnV6Gz/7DdqiqxL/nOO2eQkFi0ISSEwOWTZgkQ+y4EHn/3CSRlVrn9Xnf7zYzyZIol4u73d29E5G8vdttc8url9eUA7AwR7SQJL6BC7MxD5nmXVzH8ymMH/iJunjVV6LRNXtUvn148ULtVWDRhnsHpagUKpLkA5Gc+s5O+bpBlWKW/IE4VAj/MAqSw3dgOwJ1yAJr72AbYKVKBC7CrGniIA/y8Avc3VZ6nXyATcLPTIgH1y+vPv3x6CeH1y+tvL25i1/DRy5PV7MljlIHPPO1B0E60vG3gY0gmseHX60vRQ2UzeF+ACrJK4SMP+Mjz7scaJP4n5D/+I+7sKqh/ev2aIc/P15fxR2uzh9i5XTdQXtcubCdMwqb/gvBJZ/c1VKZpq6xGbKSGtsqCL4+Z3yjlBfL38d2PDyZfoCl+/PqSQxHs0ZJfX35C8gryq9rx+stIpfjxpy9J3oHqx5++0albJwJuMxKDUn95e94/ycKB34aG/p3r3yHVh88c8PXlO+XGz0PuUU848+VLlIfZjw/CRZVfQWZnLvjxp39G1r0AN07Cuvkf0f35QRg6yYM6PQX/6dPdyL8gk6dCHzT/OdsCuvWvaAKHv7P7hDwN9c9o3+3/n0gnYQbqD4v/Q3L/aMLk78jP/1S3/2rCJ8T/+iKAJLzC6HAS8Ir89nZQF/Off/C+Pfzhl98h6f+WzCFvK/dO4S21s9AHdfP29vMP9f3xD7/8/ENbwFiD+fjWVsk/ovmP7Hrn8wcLPkf9+Me5kL+exVneZchHpCO/5cW/Vb9/QU52EnrfntevyPf5Mn4myKjEO9OHCb7LmRrK+p0df3r5HSJFBrVp3ftrmOX//u/IJnSrvM79Bjm4EBcQ6OAmTMEo/PES1sjxmdS/Hlbyev0l9X5F4NMx3SFE2G3SIGJlhwkC82H0+KhB7iO//i/3jpKf3SdKTu0HJr29Ax9MIFC8QdR7q95x6a16ANOvX5DjBUqQV2EQwmmIxqsqAkEya0be9yip2/TzdWQPRQsf8KPN5RF66jYBf0N+/Qv83u6kvxT9qNrXDPrKhg70IAynRV7ZVZj0iD1il9M34DOEXogvVZ4kDoRuZPzTFl9GexkXkD2t6MKiAW7AbRuAJLkLdfBDCNefYCDUeXIdwRxqUsdhkiBeWEHD5VV/rwHQ/q8jsV9//dWx68vX7AHOBPKoKvUUDvgQGPn8GarlJ2Fwab5mwL3kyA+//f4D8r+R/2rWnfjIQ4Xl4lFWAJRQOey2CMzWNoXDamQMFQhFd2/+9vvDJ6N0GSyDMMdCPwT3yZDat9AYNXg46t1LUOdRRFA9Of3Rbkh3gXZBwgZaC+Z9/elrNpLI4dCqC2vwbsTH5Ifp393+4DP6pH7aEPrJr/L0PvYelaMz3bzyviCyj3xYCqoL/dqMHr3ksCJ7oACZBzK3hzPt5psLs7xBaphLtd9/QtoaqjpS/tWBpEfjpBCw7OZXZDNXYe3LE/hnNNCdPZydZ+Ho+GfcPh5DItUPMMZm7yS+IFsArQnbgMouLpVdP+q8bz8iAta89/mQuI1koEPGag9GH92z/B55773Ft65ibDvu4fQe7Mgz2JGvLY5iJPL/ozG5iyKK2kLkjwsBWWyPmvmIm7FHGtV4tFWwM0DgzEcSfOsW3oHlHXK/ZkkIbV31f3uM9O+h8hjzgLG2glJovHanPyZtdacbNtDhoweragxS+2v2ju2foA2huesRpmBexmOW5x8Mx7fvkl5g8o333+o88oil0SAwSpGidZLQRXwAvHtAN5dqTJeneaH3wZg6ML7dyx+0QiB16FlIH4FChDAMIf7fTbeFYT9a/h7DH8PDsXuCUnitC6WFeQG+IMYYpjDUaugC2AKNY6AVfriTQlIAbQxF/LBwfbGLhzBj3/oU0B59kad2A773wPMlDLmxiEB+H/kEqdqe3UBbdtAJMF1uD89+yPn0FRQ2HWP7PumP7n7qinxfhP425hSU8Ru6w1Z7rN/fGQeGXZXW90CElTWuYdam4BlAMBLupfrLo9o+yvmHLK9/atZ//Gv9/L1+6n/03CtyaZqifp1OHzXuvcR9cfN0CmMkLED9Xu4+v6fTiNPFZ8ju80dGfn5m5B9YPCz2ivw1Mf9A4hnfrwj2Bf2Cjq/WoQvGAH5+oFXmn2fmZ3J8+zXTwDd3P2NiBC4Ipk7/UT/eh8AiElQgGAc/6kk9lqEOVr47jN3rwUdIPBMGomQWjMWvzr9L5FGn0cEP/33ALXyVjUDujY1cAMbFTjKKX4OX16xNkk8vmZ2Cv7LIGaEVRi+0yrhGgpkEG6QmBPe7j2ZpvPnjyu2eYxAcvPx1TDVYxmBj+wn56FE/Ie+rhvuCLGvhsunnsT8eWcKh8Otj7Mey0AEvcL3W9MWowWMpNLZlz3b5z0KMGQYldsFYqPOPlB05/okIvAgCUP2ZyO5+YSdP3Kgbeyx+sOY+s72Gcnqwa/qEQB/CLISJBfGyhRP+zAbyqUDZwnLrjep+s983tfKHLr/fzdA81pO/vbzjx3j9qP2P+IET/pVWbbTue4l9G3nYI6V7Q3U39r01fYOKhmMp/e5VMPYFb4/IfHmFOAQ+vYwmrULYbw/3FfXLQzCo0bemFlKAiPK5HluDKUwsSAkW7GLUJoZo+B2D8XHo3cePF6//rBP+n0DDKwpYlsUYj3NYkiE5krFpDFC2AzCfcxgHdwiAeSTlAZzmSJQEwMdJG9g2ypA4Q7CjmKN3U/spzxQb/QI1+TD+/02j/vIgBesLTtGQFktikCfGUSiK0i5LEKTj0i7KAozEfYx1bZf2fZREceCgLMX6LuHRUBkMuAThERgx0nv2hw/53t578XdPPcDiDSJtGo7S47btsi6DkR4HTeMCAnUIF2A45jEEQCmO8FkWkHD+x9Snt0ZnPkwwhjRUETZm15HPb0/vj2FKk3CkRNYy//jMp9zJZs5rZ3txuIr2+Tri4ua28pSqZlq2oAuSqSxBPRazOGspfFfiy9miUPZ6p61jyUaleorKfrnwLZnjulWwgi/jCYNqw7Zdayp/c8/cTvVcfbnQI5daGcatljnFLkm9TehVeTqc4tSE+Wsd6upwWzheKV4yhqIN/xbmsGxqytkEp+PZnmZXX+9bylrfDiujbEUqstaVvJgmcqKv9b4GpYlZN1rVcGebJTdfHRrK9edxe65oaiqYhjPMzdRRNOuwjXH6tqmsdtsJeY1iVlwXq2LdBtY0VBTHMBzx2m7mBWHUDcl6l825TWaXeWijhqca+k7qGWW9PGB4mdbnUrk4qtiFravJFSUGzYHB9k0RyyuD0h1HLzRD7G361h7XrhftTe7ErVp6Nym3ESgT0RBZOttgQmyZ5DFzTlV+nPd6n2zNObT6vqbStY4Xl2Uq49R5d4qu2cKauQ4a4gG/ojt76ixCi7HP/ASXGi2dnvBNTK5mnJ46g5q3pxUW1jqx4lK5DdFGWE5MgyoFkuSseBlUuGD6nmljKyymjvqNG+xCqSvO6lEHq3QyOnTniDzDMjWfN7LOpHUhRgYWcsP25FBsslMnrLtapyJtYY7XENWRjE5DgnYtgbJmg+5PFd8Dhs0tvpKcEJ+Lq+s5KXctujOw5aEdThEFSCk7YkU6x0yNHDSW0QwnJNSZNpA4dbyK/k4qG2ueAnNfbyeMtCA1rQcr7JiuDPxGCRSDYf7gHkr7kDO7IVOAKKUYa1iGxQZydkgYOUHp42YbHnfJTWnCBk/PYLnzgYp62XqZku1OZxbXrj52x4x1VTJwzYleZGG6Pk3J7XIoPfVaEBPR3EUH5oTVASscPccPpX3kLJ2qrBaZqedhwjb22kj6rqJ71znNDuLGTCk50hI0mGyO8qlS3FXUzi5ERR0giF2Hkug8LLG14rI57XFcqM6LNVjs+g2Pzy/KvjTT8BicvH5Da+JhWOpyneZpnlzO9aEtXXJz1G4yfnZLtNtdmXlrBLY/O7JxcJgqu8N5NsuT7MQeGArckoneHFoZxDEhsNjglMXcUXYDtjhFTngSdv2SYRlSnJiH+mw4x/WNPRnGdioX7rksB6m/5sZ5S8aYprd21HthtjYNXaybQYz76crKJuuwFa/Fgqgrh88kQaGXEj5Xjidrg86udFPdzmo8jbedUeyyLmYW2MYQb0xXm9mWSmhfkERyqxrisd2HDR+W0+ay4isxRs1cjdY3t+kNcOFTbFJJp8ZZKat0mh9VdSdZ+rwsdOsQ7LmIoQNaKJTCM6z5NJOPU3SRHBU9OF1YBm0WcdoswHTHySIo2jLH4nR/ZhIsVHc2utcU0jSu8r5w6mSt0Sl1Nc1juRScbRUqEIiF9fF0cSnT0ACN6scJewwyed2vE9GlIVLe/A3h2XWKDwtC5URqw2m7Oh8IijyZEnrcBFbSnD1hwaGzxMfE7oiv1l6cVWogTwW2ojiATXlM9olVLAnUlCDlRbY0DxyWxHW+o2eutbosp+XeJxT9LISuJOS7mhQNO+i1hOjnUcEGVs2oN2t7nR2dS7OhNkMhoeQ1ddJ5oq02jduWAM5VF7IcHBeb3bzYapWyoab8YXUZqo2JH4Oumy8KbSYS8nHWnCiaiVtU1nB+Y85tr1y221gz9WG5d7pIyfzJcs8nSjmTDtaSrcRElS6VKkTtzpcU84Cu/KvK17Yh1SeYlj4LKNlQIvxSUxTL+QNLQmSek26eOAvb4gh2W8ZxTi2vRyMzwE3e3WauNwmPm4iYdN2KYbJ0S8jmJqQ2YqRNqhlxs1UpwuypRNz2AoEGQD5rGtGydUkIprtY8A1ebA/iNuYSUzP0QT2FubPD+Z2w9WIRi+cXTvZCvrpcpnOjXMXnsxMvNke0yrMylmm7yHElqCrdQnkpPh+2krWZuUth4uxvejdNWI5ky0srFRQRkzy+LP3eT6SclFiJnsVbWTsaXKwbVazMRRX4QXa7KbG1W8xjwfa0U4onuqnSV+ukdDWOQzYGmaTciVQCKucS0eTl2Egq9dyGUV5KfiTIZE8Py/MyEsX8tMI7Xg/rUqCom6IrFMCALG6TtNzuVoK0vmlOd6yYmdv4A5jeCmJr3yK9q/3Z6YC1WxbL2/QyO2cDb816r9jzksElcx/Vg2514wn5YpJn0ubd1UDfMOckslUwP/NBsjLQm5/NML1a6WWTVrFwoSizb7H5pF2JpC0Xm/l6ReSzvSaQqhECEMYiblVOxyaLnZAmElzUDFfPU1M8D4+dQO1uu3qj5Gh6ja/92SOa/nJAL/p+bu4319Csb6jLNQnllvMzHh/m51wYrkJGpfSFH2gcjzvBzNanigq9qwV/t3MUOwz25hBdp3SCckZx2A6RH+3tPQg32LBegUPlyl0yr/rmuJ3IinosI6VXsSRUNleB14td1GSXIiD0kxdM2kHZAZkxFWt2O8ozZRGL131yMOl6dbG6hVx1Ba8a5ARzJ7F3NIt8VkNI5AKX0QTY5ma7KN634BbwF1JVmtUQ5axyU5xTc5r5Z41aLa/T7IzfKj/K1D1lZHN5x82lSW5uO0c6XlCKrgyb7jz5WsX4JPVoUM/cY4GpjeNcz2FXoXkeaPHqcMYZylsslPlsHzjbzeDiSZWI6sqeHpZ9jC8sPWSBYnP+2bods0E0tkc+yRd+Hlspvbgsh1SyZ428x8Rmhh/ym9v5UnsMNgVmXkFTarfVDZT5zibhMkW8ALLY8AtxPw1bSkZFj15ZwpXq9YPYHmA/ODsw7onfUxRs1YdTxotnJTgfFha9NwXa4gedr7BllBVu0dh2o1jt/hwPnZFciblIgjQmSxwdFtOZ3zXlXPEWy6Q/Bhq5KZYFqcuslR9nt9yMm5g88T6sSKW8srdD7hoA30DrbuaMucnymGejg7swLT8Ibyq9nh23pT4t6GBjbObiAJHETk5cR63qc7DyMv0UFzSH180k26DLm2YsRa9jajWNJMXG9xbwTT41HRYT863ennh8a/XMWfCaNlXpsM7B5oZHVeGJrm7mGsGWILRP3OD37trHdIFdkY4Zk+0iIy5pEOj7br9b1MdCMqfX1gxvsQVTCuu3oXezd1pL7mmBHzKHlrtBCFOmW6RUA9KcxveX+SpL6q5p7C21nx2W65Pmbxa6gp460e+2y3KH59P4VDqhtUtzaV4uh/DSHFY+jK6TuB7sdnU+S8x0HehyJJLl4Ibk9eDJ4myRZ9tUCXBfnUQH7ELsC/toeHaLk7I5n0y5fUJWeytqXWa51tYUFc+ZZB/AhkdeqiKKNuDU9JVejpv1eGShmty3E9SdRep8J028gVqU+3khlbeE2V903GurLjnJSqAxyaDkeba0GcajZ3CdUjogb0X0MEv7enNNVYE1mSndVtEMtumzo8dPC4MXiHC6z3aHTTebebanrtBtA0qBjxZCvZkF3faoaWS7X8anYNhVe2EpbENy0/Kh50UTS+Ob83I48Hk+TfVrJvKif+YAOU+X8n692m/YzVk0TV+F6bUN+pxVtWuKepGWFQdNEfpo0rarwmEhxMmF2OBeppwpC8yyhKSBZGBVGU50XdsvbZvCj0xZUpOcyvVLnvJguZ6YVWluk/YExEl/Iqfisoxi/7pqlsSu09mzeMMg0uKXziP0K7Gu6avX+UlHudQJE2cXB+/JqFxq8pFohvIkbFHylOyYQhBqNm0HVZbKayxfV54Te1rOeQG3bY5niZ/Ludm7+MbMYAM486cMNWPkQGndPqzqBJtK25UUtFOSF9VueZUITEquMy88N3N0BShlYlMLst5KHK9dGZGeuA6j0/Nu4uGnhrp2hLxsdipsADxbArfm1ta3fqsO2ZSaHHw2ENGTIWZcRkzkDKNaQHNMn2FcyDoKl63cdNdhKD/h0JMUU7SC7S0PuHv22Or0WqVFpV/JsyPwd8s23hY3lCKPYiqhUrxxYiLMqYhNPcxb98NxPnX7JgVhJ3LOCadRTwrIPZXz50u/2x68Hr8CnSS1VNMGGS4M5GsOG1zZ0ye7ij8fVQbdDLHKDmJLM+FGDm9XiVL3Kz/hCGLprwkRTPqtbJWL7fa43aykasfirjCL82lS23Pa9rK83F2mjUEyOIYblZ9Mp62oLuoSrg/DrTkr17IUDZwa5QCvmS1DpUotXs92Bzaa1/OOa1i4n9mASCcOtifWTMT3tysWtduUKRiJ8WWryeO820w9OonRJTVRSlSPbzNsd1vQIUZq4CYNaNQa132zkfm9n9bCjYPrfoZMPFAVFFkEftFJUbqM3clSiTi+qRYUgwpkD9cPdWKRCSHhe3/Hd6dqAReb03a5zM7MWc2ijhUX7m1CCpi51DcTotmymivFGrpXwqabJzNiS1umuuQv07g7LaOpH6+WdGTGSsZMTueDgZ71xZVVcMIYVOixcN2SvTMBdYIrrRUdfI7c9aBre41cl8JOxPpeZXsyo/wq3Hkp1jfMtiXmbnsRLtKW3CjTgAQm6wpmh3qTnbSwqlm3sLDrmZwOnGvULBfhZSCsNJhvGldP2tN1b1MYcfJo28rabYM3y0spgUI7C6h32uUSEGaszPLLGXrwWLgC8Rf4bRPxYeCTt8lmnbO07PpSjnFKImFH1XbPgkLt2xvRLnhWZgDmKLMb63BZG04tq6GH6akFHM2uK3cQZWHqsf4k2bNkBOKr4CzGfa8rCtv0SaLPmjXHnFvMBAyWVRvBnbQErU7ZodbYkwAwgncq+nxVu9CSW1bWuZtjiuqJS9cb/wbbpeWxkVFLwuAK/RycfdjfqHtuy2/mieyfCJbb7rggD8W118+kdeWo86alXIuusUsLEQPEasnKG0WfDH1woxeehM6F2tYXrrFsw6NK7Nb7SKcliHKyRafoFOApg3JztTAK3uBX0YRmUADyBZcJ5GQ1J6vQYdNqEAZe7LrZeY6SRtvNBhCtotVsUm0L0eKtjlkp/MZfNddZwbvJ1dphkjCswRDt5GvRA8agZj4z8Q8+b/kUmAO6Ojiby7ZKUMmdEqYB3wVtP1XoZiofIvkYGlhvXA43cCNrSvfpYlaqZDSnsGvGXS1eUmnKnQ3BjojtNY0tqb1pO7kqG/OsmmT8mdDk88FWvFsxXU7WOYSkGmLaHuOwSdEzAsTpKT9phgQMxorn+ZdPL/cz25dXDCUp8tPLeBrw3NP/F3eCgyEs3p5ECQZlP738v9uSfGwPvp8B3rf4ge293rm//kvy/vLppXJDKNtjG7lO2uC5IfmftmI//4Wd4pFQ/ziTHg8wb837aUljB/c97TDz2rqp+rc6T9r7jjb0Q1uP/6lSvz2PGF7uqqZF89w2Hg8FvIdy4357Dg1QNG9N/pbaVQzGUbZ3Hc0y7q+OZnnLs2R0yPsx0uNc4HkgNW7XjidSL7//H6u/EVVfJwAA -->
