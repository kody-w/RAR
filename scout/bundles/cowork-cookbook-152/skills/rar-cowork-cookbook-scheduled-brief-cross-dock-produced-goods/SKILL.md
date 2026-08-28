---
name: "rar-cowork-cookbook-scheduled-brief-cross-dock-produced-goods"
description: "Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_cross_dock_produced_goods", "rar_sha256": "d4404811302058a61c14031f21f418a4ca56118b792978fffb5d6a94b587948c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_cross_dock_produced_goods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_cross_dock_produced_goods_agent.py` and in the RCI capsule.

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

Cross dock produced goods Scheduled Email Brief — Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 d4404811302058a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_cross_dock_produced_goods_agent.py` first:

```bash
python3 scheduled_brief_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_cross_dock_produced_goods_agent.py   # or on stdin
python3 scheduled_brief_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Scheduled Email Brief — Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_cross_dock_produced_goods',
    "version": '2.0.0',
    "display_name": 'Cross dock produced goods Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddff51b800003739',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefCrossDockProducedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCrossDockProducedGoods'
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
    print(ScheduledBriefCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e7Oa2LbvV+Gu80fSh2QBykOya1ddFERRQEAU6HQlvOX9RqFPf/c7UddK9+7d5+596lZdk1QExhzv8RtjTvz1xe7aS1G/fHnRfDuHeDtNo4tfQ3buQaviWtQJ+K9IHPAPcou8rSOna4u6efn04vmNW0dlGxX5tNy9+F6X2k7qQ1lR51EefnbqyA8gP7OjFGq6LLPraAT3IbcumgbyCjeByrrwOtf3oLAovAYKihpqLz5U+01Z5E00cSuuuV//DQLiojAHlG0B1V0OeYDrAAH6q+8n6fAKNPJvdlamfvPy5edfPr1E4PvLl19f3NRumh8a+t5yUms16cACFQ5PDfhJAcAktfMQUJcD8EsOrku/Blpl4JYHjHlefWz8NPgE/ed/Jle7DpufvnzNoefn68v0RwUaToa0hd20QGnXLm0nSqN2eIWY9GoPDbCx7eq8gWyoAW7Nw9fHyh+cihL6+/Ts40PIa+i3H7++FEAFe3L615efJvO/vgBvgO+vE5fy40+vaXH1648//eDTdE7su+3EDGj9+u15/WQLCH+QRsFd6t8B10d4Hf/ry++Mmz4PvSc7wcqX17iI8o8PxiCYvZ/buet//Omv2IIguEkaNe2/xPfnB+OLb3vApqfiP326O/kXCH4a9M7zr8WWIKz/jiWA/E3cJ+jpqL/ifff/P7BOo9xv3j3+T9n9swXw36Gf/9K2/27BJyj4+sL6adSD7ABV8wX69Zt24FY/f/B+3Pzwy2+A9f+VjVZ0tXvn8C2z8yjwm/bbt58/NPfbH375+UNXglzz7exbV6f/jOc/8+tdzh88+KT6+Me1QL6eJzkoeug906Ffi/J/1b+9Qic7jbwf95sv0O/rZfrA0GTEm9CHC35XMw3Q9Xd+/OnlN4ATObCmc++PQZX/x39AYjQhVBG0kOYWXTvBTRtl/qT88RI1EPj7ACng1wdGPehA/k8RnjQuAuj7/3bvAPrZfQIo0rwh0Lc7Mn674+C3CQe/veHgtzsOfn+FjkBAUUdhlNsppDKHw9fcDv28nYSXAB79ugew4gyt/xkA0ufpCxTl0Pd/Wca3O7vXcvh+B/vogVfqajthVQM4vE72ni9+/rTOBf3Bv/luBySlhQvUCiIAtp8msC7SHmDd5JsmidIU8qIaOKKohztv4L8vE7Pv3787dnP5mj/AdQ49GkiDAIJ3daDPn4F9QRqFl/Zr7ruXAvrw628foP+C/rtVd+aTjAMA+2d0gIaCJksQqLYuA2QgcCDUAEru0fn1t6eXARvQYCAQyyiI/MdikK2J7725XNswn2cECTk+cDVwc1YWdTs1sqh9hbYB9K4vEDo9mjD9UjQt6Fmln3t+7g6Aqw3MefdkXrRQA1KyCYZPUNf4d6nfndq+q5iBsrfb75C4OoAOUqRvPW8iAouLPALuf0+Ix33ApP7QQMs3Fq+QNOUnVNq1XV5q+ykjsB9xAZ3jbTlgbkO5f/2aTy3Tn1x1L5aHewAR8Iz7DOnnKeZgEgDNPPeaN9l3Gnvqc8d7v6u/5s2zEOx6CoULGgMQGnaRN7WHvz1TqrkUXerd/ec/Gv8zCt4zKvccXP3luPDe0iHuPmTcOzv0tZuhGA79f59IJt0Znlc5njlyLMRJR9V8+HSapCbfP4YvMBQ8xYD6+TEovMHMG9p+zdMIJEg9/O1BeY/Ek+aBYF0NlFEZ9c4fpAHw6cT3nqVT1tX1lN/21/wN1j+BwN8xDAQKlHTysOVN4PT0TdMLqNvp+keLv0e19qYCB5kIlZ2TgiwJfN9zbODG9lJPlfaMBUhZf6q66yVyL3+wCgLcQWYA/hBQIgK1A7x7d51UADNBbIK6yH6QR9Pg9B4jMKr6r9AZFMsUgQZUKJh+JhrghQ93VlDmAx8DFd893Fzs8qHMNN0+FbSnWBQZyOHfR+D58Ed633WZ1Adcbc9ugS+vE+56/u0R2Xc9n7ECymZTQd4X/THcT1uh3/efv33N7zq+Qz2o80cG/3AOBOora+7AOsFUA6Am89/z9NGlXx+N9tHJ33X58qeR/uO/N/XfW6f+x8h9gS5tWzZfEOTR7t663SsACQTkSFT6zY/O96jAz/d6+zzV2+e3WH6+19sfBDz89QX695T8A4tndn+BsFf0FZ0e7SPXn9L3+QE+WX1emp/x6enXXPV/BPuZERPWgrp2hvfG80YCuk9Y++FE/GhEzdS/rqBl3pEXhONr/p4Qz3IBwJ6HU9dsit+V8b0Dg/A+ovfeIMCjvAWyvWmCC/1pj5NO6jf+y5e8S9NPL7md+f/63mbqBSBzgU+mjRHwPJiL2si/X73PSNPFH/d29/oCwOAVX6Yy+wRN8+wn6H00/QS9bRbuu7C8A7uln6exeBIJSMF/77TvG0fHfwGbtHYoJ/0fO6BpGntOyX9WYqouoLHrT/29eC/XSeKfmIAvYejXf2Yi37/Y6RMzmtaeunXUvlX6W55+gkAEQQWCogJY2YEFfxYD5NR+1YG26E3m/vDfD7OKhy2/3d3QPraRv768YcczBs+REZCDIv3cTI0RAdkKBILrR16BZ//zYfLJCMAemGGmbSyOo/gCw+boDCUWNom5GI7OsWCGBTi2sHHXJkgMWzgUPaOpRRAEDuGRNo07xIKi8YUL+D3S9Ns0BkSTcjPbdhcuheEeTdmk689RZ+762AzzqLmPEvQ8WCx8HPjpfWkCMPNp8cPCyZ3vc+3kmafhv744JA4oN3izZR6fFUKfbOeMOOplD9cpfLvNSWWulzqaUr16TAIyvsj7ZHVcJlQXNduTz7WDcMYkV006Xncx9qBu6GUwS+nr2CwaQ3d2Dr1hcIkLnYwYvNyaGRZBWDslWqGntKyX51KzCU63KvSYKtWpsZNTfZOxqGpF5Ab3JUdyOL2vLdA3CBp2Wmorr6XIXJQuQbblyC9OGl2SDcGnyGVzUI1djlR6qTqnc5FqM3Gfn0oRA7TlQlgLKa1VG4s/cWeAnheQKeFhwPQ0sKTLIB3LBd2NF8Tr6wzZJniA5Blet0q/5aubrJ2GqLmQs7LVUqxFNMeOEuUstqZ1cKW+5Wlvtit1Nz7svPW4c/t+u9JwjDowEbeLjlVEXAbXKJd2Z/AXezinszWeJ+ubdpadQneds9ali/LMDZu1jIEYGDsV99luI2Izem/f3GHeZjm5sWiyNGRT8DXxZmkl2M1R136Lj7kZpXqWNLi7rlgFLW8DM5e9AVtLXp3bt/kYyWHnDZoTcqzHG0I1Zy0NP4xbbb9HsytpWgN64rEEq0q9CC6zvdYP3e18G5orNvgsbmJmIoUVfNT91oQxe93gmo6RN9vaL5zRHvR81qNEdwr7w/WwOfGJdFIETLIGj8N6gczJera3+C5gr6So8nW6jwYKD/T8xhfGvo69w6W6OYawNjqnsAbCk3F4q5W6o+EUv+mz0/rcjfoZ086pbETm3rhsYulA2fwoni3cln3eEE/4SN/odS0Y7MiuLzVs4hjLKSVenWW8dI4b9JAf5qdYujlVtYq7YFQFPztcMPO8nYkzjduXmjezTd+wMalzdkBofhRy4lhXAxx0AI+CEOeQxg5WzuHmHq5KEDIORZ0jWxBpAwlj6lDiMJwFi+MeNY1K6YajIhz6dtj7q7LTuypu6iUvEHx5qi66oN6uJX+zHIFVfRMTd1fyIjHY4jyc6mw30/OIg/tzl+DrtW5IjEKNKJru11S6dixZ8rSWE6+Mz/q7orLkAo3cSGjUjbYNiRmRiEtvuTPbaOgc0ZWFEG+p3K0OV68fTit6hUYnxkjNKObytb4tyh3GKSleRWKvOf0R289kI0N9i6jOM3XgR50KNOXazirdpQ4B3i9kzMS8/WVjlVt6dztbtHByz9WAbJhtYmsOL9ViWsmdhW8b6+aYm73LXsUjwvQHVz5k5C7Kr+atSFxyCS9XyGhXR0Gr4vWeO2ieqe9S/hTbSE2smqCk0QhhixtnBYic7zXBWPvyRtKGFXB4QZo8LdkI5Zwv251ans4Uo+h05cgLW1F3kuGcGxlJ3DpAj4nhHK/75SkWOUQx/QuxUJWEjEjjFNmdfd228DYlMUdTdAQxaSEpsFXlkNJQrNOTeBbs0aEMGG4vxI2webnfbyVvt1G8vIxmlj73youMe0GyqgrVJd2xzs9nrgGbvhNxLuxFu08ak5rVUqlLDpzHcFmNp3LT58RK9uQkaDGpxQ0SbzMJbeRoaaW3RJgXMoboZykYdg6mtTa94Jhgze7rGQKj+hJxhYXfx2ODK83eUo4elmc146MshWYboyvZRs/V+rJuVp2NJ4pjAgfrRs3Seydd9uXgRW4QrM7jyrJIM90filsgzreBXJaVN84J2D5IvZwYdGgo9prZWkcnZdDDVXD4cs/Y2TG9MvymPKjcGFuC7fX+vLeoG2baXbi2UbIisfxyDCnYMpO+IABMbfjSVOoVPraSOLOYXT8moEXHnWpwa8EwRNSRmdY6bVrQJY65mrtnJ+ItDKN7Y2wQ2agXtCCcI6OxihvJeqWgzk4BTw8NnR/d1YoipdWoxtTiquwVJ++Wc1PfDyWDGhqJBMsYIZQNHBw2+R6hKm6h9yuwLyNKo9+huFAsjYXG65JNULtxVayODuaS1VFmNs4YmEdJYMtbMmfUWqj2Kbya+Xu53F3LShWcObbUCxXFor1aHkLXOiqZvIFbhSnanTkUhHdFlsqBnIvtdkOqOqyfm85LYrGX9HN3Y0wL18veyz11H0ezlLup6M3gYTi8UZVWOe4GQ8dz05bh/mzPPPRKmPSFwxlLP+e1ashNX9RsEC9FbszG9ZyPeb6ZCTPmKO6SmB5Zrb4551H1kDEdT+Ewwma4ZQs1S7rdmJ5uEXmI50s4n+EZruJ6ptF01pNWzGhYnI6xPDRhZMzqPVqd3FOCwcFie1y6l9NSJcfG9PlSr1bbrYBElU+2ko4qpx2J+su2dot26yacL2norY74HuUIF93uK9juNH/fS9paLPOBVc3D8bRaK9aOXnqKALOGWYH5XAS5PNB9qXChRVc0Y9lyX1cJiXGOzK/dOUMTS+rqagc/x9H+RDrx3lZ2vNrgrH7basx5bs6qxtpdVbw008ul3jGbRWbmemeppcEdqqQ2+lk1Q7LNmUZXapWWZwbBWic3Uy7MiE1x4/UxT9oCZDHNzqJtr2Uir6ebVo71eTHo3eJ4Oh2ji80tbgVLpqu66VfXW1Mz2Rq/dFfnuq6Xii4VBbpbK/rmlJ32Khdy27WwQthNro301uIVQWQJ0kLodIblspzxaLvZCjqdhuvt1j8GB7axdAITnDXozumV04sz2AwGNT8fkuulUrHKZrsry7bw8ayZM9/M+2NGGNG+PNFeZihUbxG39UrKdTgFs42nhPgyBvMQg62JWXqFV8myyBQpDckuIOarOvU2zMJeHhkxPm7cpUYH+QlWu4MGAJDJFXvIEj6wS0MomIPmEkrar/kyLMhaxw2mwxsrXSu9P3I9ysxWxq4ShX7cpWoxn+8CZnsMRdLpztR4xHk0iUihzGJFII5ekdcbtlSFTZKItJg7u5VOH5kyYW5orItDtDkhgkTGRIm2+nzOZNrohk0BNuhVMCJ0w0aWv0Jbd6Ze3WVFEttyq8G6Kxii4sNrShXD68rlU6Gx5E24XRdXquCERlYxnBIcnVgQUqaJ1lnlLkq5QC08CE+rQ8excZuekHKMmh0Tn8eSEvfcCeDFeSlL5lEYNyXf9l5d9g2dhT29kgJxd1GQsxysTr7amyxPxSszzgcsIuJoue+MDX2TnBs7VCW5icQ2wamjeZLifikjqZLQIXqojvuRRlGGorbRsnMHNPBn0YnVYTOSZadl7QtV5PKQ7GTnfE52SkaMY3hsuK6vFgsSjzWyJQKCjDliGefBdb1N59h+Eziodtunt3mC+a12whS9WvcnoQ85UsCSkL8p2rqQyUIgQSmFcJZaQlltwNCqDQKb74IzmNhNw9/CKCiewkalW9bBqZZRtiHyXCTOTBHzFjV5GuXNbTWCSOoZUsXbUKcQbGVE6VKUkX1DYlKfymodVk7VH4ULuzT4KGVvOtvuYNsJl0VybFYnmyLr61lcFLeYdPNi5YYy3NNDjZMWTszIfnXU027JqUbTNavmVPe1V66REi5pImZru9j2u+sOAb3qFIIhAR/EoSNnawnt4WrLmPCNXjXrYuCkfQv60mZd1unRD5fbDct4DXMJwRaU4aUKNWs64YZLPoA+NKS2caRa36iWG9BGSWY5Y7OTQWRXL7lR3aIJAc+tbogZR88FYrjUNRONrFgtRvV2XpfxDVejZRlkvANQdESc1SDDO383jZxhZC8WSLyI4zzWpVMeyKYY2huNsEDCz8hlvWCUelQVhNwqF4PSPUqS6b4d+8EXD6KxXXRVG8/hEV3ANlm3WNj0LelKwbm/7RbzzYzgd5TbnXBnLw80TxJxuVaKo9OOLL2DS9zatTjMhzdMpCNd8VJVJmxy6cT1dlN3REXPbLdglusgU7M4Txf4cQv6Z8D0KSexrGzb4+D30u0qIWiAugde2FHLepmPNSqZJ/qIDYeZdJif83wdFqBSD71tuKs0aPe6vwntsUV2M20RggEl2OA62XX06Bw9J078oOqRccEh5CrgT6YdzPoe75DerWd64IqIXNgucWxPx1CdgSa1Qe20WLB7s9wK3pq6aksZv5otck0GdckczkhCZJLNsWHuJOnWVQ74fmdey55bgg2XiETk5pJnJ5JMA5nmGGlGjsLcQX32MnZKezIHVWe9zhnTgy+asZtcadwWz4qFKGgHm7a1kE22vZ3RkSdVhMUdal9IGXc+4PjFFsZF28FXh7AJmzpsMUMw4mrlO4RCE3N+DM2mWUeHXDEia+ZGrMXDoH4R4+RXCN0G0vWmpLlSB656YKQTwSzO/XUmXyhiXMTonDOcVu1mTIOHRrODcbEF27MBoFE5rwihUPzNLJ7nvEvIBMB3MjCtjuH6UawtfLNCeKtbX3mlHUN1eU3gLj5WWCRSaQxXZXIp/BXDyv2xJXl8e6ZS2q8Ea54rYBrPjXyT6Dhv7cmldJCvHr8KLvGCdAUYJ8eYuG6yiznAzMlV4J7sjhTc8Ow4Lg5XmqWVDRpiyY2AEfHWXl11s15mK2QpJHuTWg1Xd7ZnzDKsnfkAF2XdSLaZGf31JnNU5eFbJJ0brBPRs/S8jZzboQH982wm1+s5mhNae0FEas2HYrImqWC7Rea5YMa0p1IN3HmpJcH4cY3u3GLuskyAqIyEeyxxxVh5teGIfnnNTlcsnycj5VqL0YrmLrqMmYYfcJJsnNRDhS7x0HlnSAeP7DAyOfOFhwdrF9RrAsftcJXKebhUXG4ThNXy0FPNcXuVi00jBrFIHsD4urmRUrCzVPo0zvIRlG1umNR8xQSJVHtLrMFhiRzm2uIwSm2KmLBNAYuDVcqwhz178OhArpVFwdA9zIlO39U2YpjSnByV1b67wCMCq6LjufE8Ms/unGrWCHycHdxd3PO4JmG0MJcLTdQNn9u5IX9gT2cv8BLk0vhLSqo249ruOrODw5rrLzuEJwo+TFKB7PuoJJBO0jXRXszpG8nXY3tozhnZenifhlbVL8/5zsY00ywXG5qNUPwqmiJb7jjeybL4MsaoSImtgc5wy5X62cygZuhcT8Z4caqUdWirvUdTXa/v/PGyOKyX3hk7wOyJvhAJa2456rJz944pgiilaqrAaIbmUijiLsYl8qHVZjzh+thGye0xxdO8wcdYwNEWQ72GDXoE57rV2GH+CnZiPTBLscaQdbSBzTM97xQ68BaEcpYv3co04DO3z+Z8dGmPyI7jiqAyxs3RPjjByPgO0H+TMwJ2beR4sdQkPssIdiXF5YD62/UN0whsk4QLKxjHmCwOYPNFrUoyt+cc5gU38oAwAq+Q/sHaKQzz8ullOqV+njX/+2+Yp2O//2enj4+Dwre3UPeDZt/2vtxlffkf6PbLp5fajYBmjzPXJu3C58HkP5y4fv6XX2JMbIbHa9zp9dmtfTutb+1w+nHSS5R7XdPWw7emSLv74e+nF6drpp9INN+eh9wvdzOzcjox/wezXqYfLUzn0wVg0Rbfnj/xuN+eXg75XmS3/vMyfJ5Kf3rxBhDByG2+zUnim1+Xk+nP9yPTGe70guTlt/8D80zXBBImAAA= -->
