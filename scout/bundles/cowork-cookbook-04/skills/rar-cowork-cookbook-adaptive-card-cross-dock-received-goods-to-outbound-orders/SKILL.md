---
name: "rar-cowork-cookbook-adaptive-card-cross-dock-received-goods-to-outbound-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "9134621f175ff36de5e4339f5c70540b40244d3a276317910803d3e369ff1e9f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-cross-dock-received-goods-to-outbound-orders:e7bb51e062290497988b2d29d4a7e6d9ae4cb570e72e4a670fc629c97f2223c9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` is
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

Cross dock received goods to outbound orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cross-dock-received-goods-to-outbound-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 9134621f175ff36d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` first:

```bash
python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py   # or on stdin
python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock received goods to outbound orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cross-dock-received-goods-to-outbound-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders',
    "version": '2.0.0',
    "display_name": 'Cross dock received goods to outbound orders Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-cross-dock-received-goods-to-outbound-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-cross-dock-received-goods-to-outbound-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c7ed5fc7a32e624',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/cross-dock-received-goods-to-outbound-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-cross-dock-received-goods-to-outbound-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCrossDockReceivedGoodsToOutboundOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCrossDockReceivedGoodsToOutboundOrders'
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
    print(AdaptiveCardCrossDockReceivedGoodsToOutboundOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816Z3PjxpruX8HVfvD4UCNEIuiUq5YJAMEAEokgPC4NciByJOD1f78NktJ41sd7r0/5w3JqJALofvuNz/M2Wr8+mU0dZOXT65PsminEmXEcBm4JmakDLbIuKy/gV3axwH/IztK6DK2mzsrq6fnJcSu7DPM6zFIw/VBmTmO7FWRCpdtUphW70MwxwePWhRZm6UCCLO6hKjXzKshqKPMgu8yqCnIy+wKm2C4Y6EB+ljkVVGdQ1tRW1gAtstJxywqqarNuKsjLSshNLNdxwtSHwhRyzCqwMiC/egYPzDAGv8EYxTWT6gVo6V7NJI/d6un151+en0Lw/en11yc7Nitw6+ldw1HBxajOEmgjPZThRl2UTHxoIt4UASJjM/XB3LwHnkvBde6WQK0E3HJcD3pcfarc2HuG/vGPS2eWfvXj65cUeny+PI3/pCaF6sAFtppVDSy3zdy0wjis+xdoFndmXwGv1E2Zji6tgONT/+U+85ukLId+Gp99ui/y4rv1py9PGVDBHMPy5enH0Rdfnspm/P4ySsk//fgSZ51bfvrxm5yqsSLXrkdhQOuXt8f1QywY+G1o6N1W/QlIvSeA5X55+p1x4+eu92gnmPn0EmVh+ukuOC+z1k3N1HY//fhnYu3AtS9xWNX/X3J/vgsOXBNE59ND8R+fb07+BZo8DPqQ+efL5iCsf8USMPx9uWfo4ag/k33z/38THYcpqJZ3j/9Lcf9qwuQn6Oc/te1/mvAMeV+elm4MMrscq/MV+vVNPqwWP//gfLv5wy+/AdH/TzFy1pT2TcJbYqah51b129vPP1S32z/88vMPTQ5yDZTgW1PG/0rmv/LrbZ3vPPgY9en7uWB9Nb2kWZdCH5kO/Zrl/6f87QXSzDh0vt2vXqHf18v4mUCjEe+L3l3wu5qpgK6/8+OPT78B1EiBNY19ewyq/D/+A9qFI3hlXg3JNkAqCAS4DhN3VF4JwgpSHkX9Vd6st9uXxPkKgbtjuQOIMJu4hrgSYBUE6mGM+GgBAMSv/2nfIPez/YBc2Hzg05sNAOrtBphvI2C+vQPm2w0w3+rs7R0w3+6A+fUFUgKgUFaGfpiaMSTNDgfI9N20HlW5JU3VJJ/bURugaXhHI2mxHpGoamL3n9DXf3/5t9tKL3k/Gv4lBZE0QXgdqHaTPCvNMox7yByRzepr9zMAaYA+ZRbHlgnYYPzR5C+jN0+Bmz58bAN+cq+u3dQuFGc2MMkLAbA/gzSpshiwTD16vrqEcQw5IdAQ8FR/IzIQnddR2NevXy1AF1/SO3Tj0J3AKhgM+FAY+vw5L10vDv2g/pK6dpBBP/z62w/Qf0H/06yb8HGNAyCWmydB+sd3zgO13CRgWAWNiQSA6hbrX3+7h2jULgWMCyow9EL3NhlI+5Y4owX3uL0HDdg8qjjS4m2l7/0GdQHwCxTWwFsAFarnL+koIgNDyy6s3Hcn3iffXf+eBfd1xphUDx+COHllltzG3nJ2DKYNgvwCrT3ow1PAXBDXeoxokFU1SPPcTR03tXsw06y/hTAF3F+BSqu8/hlqKmDqKPmrBUSPzkkAnJn1V2i3OABmzOKxFSgfTAlmZ2k4Bv6RxvfbQEj5A8ix+buIF2jvAm9CuVmaeVCalXsb55n3jACM+D4fCDeh1O2gsS9wxxjdMOCWeYu/0p3I9+7k+4bnS4MhKAH9r+yMRgtnHCetuJmyWkKrvSKd7+k4dnmjd+6NIWhHbpJvtfWtRXlHs3ec/5LGIQhh2f/zPtK7ZeB9zB07mxLYIM2km/wRC8qb3LAGeTQmRlmOuW9+Sd8J5Rn4C0SxGrERlPtlBI/sY8Hx6bumATB0vP7WXED3FB1LByQ/lDdWHNqQ57rOrU7qoByr8BEfkFTu6HRQNnbwnVUQkA4SBsiHgBIhyG5AOjfX7UE1jW6+lcbH8HBs2fJ7uB0IlJv7Ap3G7AcZXEGWC/qucQzwwg83UVDiAh8DFT88XAVmfldm7LwfCppjLLLErN3fR+DxEGTyyFxgvY8yBVIBcNfAlx0IAqjC6z2yH3o+YgWUTcaSuU36PtwPW6HfM98/x1IFOn7jELBZuGXzN+cAfC+T6gZZgM4vFQCDxH0kEMiEW3/wcqf4ew/xocvrH7Ybn/7ajuRG2ur3kXuFgrrOq1cYvhPrO6++2FkCgxwJc7f64NjPI8l9vpXe57H0Pr+X3udb6X2us8/vpff5XnrfrXh34Cv017T+TsQj3V8h9AV5QcZH29B2x3x+fICTFp/n58/E+PRLKrnfov9IkREeAWRb/QdLvQ8BVOWXrj8OvrNWNZJdB/j1BpY31vnIkEf9ACxO/ZFiq+x3dT3aNMb7Hs4PUAeP0pEunLGZ9N1x8xWP6lfu02vaxPHzU2om7r+76RrBHCT2eAH2b6DIQMNWh+7t6qN5Gy++35beyg/ghpO9jlUIiBM02s/QR8/8DL3vYm6bxbQB27ifx359XBIMBb8+xn7seS33Cewl6z4frblvzcY28dG+/1GJsfiAxoADbgD+Xs3jin8QAr74vlv+UYh4+2LGD0gBqD/SLWD5BxBUQE8HtG0A7NuxQEHNAShtwIQ/LgPWKd2iAQTvjOZ+8983s7K7Lb/d3FDf97e/Pr1Dy/j93m3ccwlM+Bt6xdHZ7xz/Ni5pjoJvHd3N97fO+Q3YHY5c/rtH/tiYvN2T9ukVIJb7/DR6uAzBdmC4bf6f7noCA7/13EACwJ7P1dibwKDmgCTQMeSjcReAm79bYLwdOrfx45fXP23U/zqIvLqUZU1RFyExjEEIhmJo2sIcjHEIk3JJhzFdwramFOJSmEuYJIV4NokxNkN5GIbhNgPUG2OfmA/1YHSMGjDsIzR/47bi6S4Z8BQ2JYFoBsUJEkM9lJp6Hk467tQlcJzxpjaFTAnEIhCMIBzcxCgSRykGRWgEd3AXJxnPQ13GG+U92te7um/vW4X3ON5R5g0gdhKOxmCmadM2hRIOQ5mk7eKIhdsuiqEOhbvIlME9mnYJMP9j6iOWY6jvHhnzH3SuoG9sx3V+feTGmNMkAUbyRLWe3T8LmNFMjKAsKRAYFPWQnT8xZV0S0nnjl3PXiBZwKZ3W/I4h9rOL5++r5ITOk41i7YWIOi1n3lqa2ALdG2RBFcZaDih+J1lnbkXQR9TQHcaL0U0iZ6FvpprHnXLOYFa5uol1MrbLFZZHu7DO1ggjC+Y53yWLXImlk16bnbWhif7kmEdWdPu+ktoW7oq2YHZooWwW/qWODE0ofUOGqYBmYuV8zA3sjOWBFgpMTGA1hgfxpuCw0M563ezZ7eWYUPL5inB06i5YNErpgEYHoTSwvZS4Bx6laY8fMFhcLWlvmdNE5RmT7VTKUpXdqoUZcpab7ArdZc4WhUtaIffxOhVJKZ4UPW/HW7PJOFIlSVlGXaIUqEhuNivdVxcKesHYBdrbujUni2OtVVruDLSscFlRyvmekeLaIIVTzxxlzM1OlKmJa561Zmbc0dbKabvhgjcLhdFjK4nl/HKRi55bdJEhcHt6exXsHNvEmmCsE150/d1+CCfsRjoaE7yIEARvD/7GLK54zkbhrGz5g3PklINyIniip4rqim2J3tKKHFEqaiXFWiGk1Llnc1U5sWyWCoOibAg497XQxBaWtZdMNKQupkqFZtJMuFCmuAlWxYZTMKJVn7dXenkdAnKuHKf4zligPErNyYuZ6kN+qCfWdbBX/uro8jYC6Lnt2ZOIe3PqYJYrg9mXVbqhDgg9ZZbOCVHUos7NXaRgmw1ZYUJY0+1qMUybRA5OlVAdY5jxXWPBi0sNRnEhLOeHiXBBqngBr84nLDpHgypKdhTE6tSPq8I9NjY8oaZmuEKdGD9fU9Kldwe9NIrUGIKV1MQStk3xkyKxV8yQFWuVC3sfFfaNekkYI+FyoSLzTdWQ3ICrGxqbJhSXXrMtfUwrgkn5yWFfD7nGbsvJsrsihxZPrpM4dZcJqfKNNyGj43TdOzJvLfJcbcyhOqxL1i77BhUa7qyfnHR6JKSo9s7xoevN5rCYIgl5sTVzJjUVaR5b/ezZ1LZbU1ebzXZpqGlsRHbDqaitzvLlM7/TrvK+I9jWY4ez36ycGPGJcMuGm8JgY3GiBAO+DIFol8UXBc3rcH1YnvfbpHVYQbTOqaEoHLnxp3XoxHs7GUJioxsNl7YaXi0usEQa4nI41At0aM7tEm3oPb1Bw6kyBHsYg4PDtdMCF3Z2VzycLLo2N8qQUdurv7DmJYeEJC5wVEm6iy0nn8Q5Bc/Oq/nqVB2OuwNGbZOUKhrj7JKzTbd0EYpOzATge8lMh5l0Us1Muk70/rCAZcpYhpRanBEYdrfDidVjV7wcYkSYLHUNaW3SZNpZyyHxmavBnvF4mS2ZJumEna9uEj0ySTXS9GuYkFNridqbbF5eTEFGvENmEmXhyptaibFC0ihkRpZEG0T765Zh8nM2RHJfwgSOHMtcM866woDyV+iwFVlM8ljKYMvSv8bTuPTMsz/HEhWTTNfXtSnPnxLlSA5dWFRI0ZJ5fJB305jfE3Exazg2hDuYT7Vil05SQzw47nmHqq1Mm6ydoArDLbMQ047ThUPOsT3Kdgp5HYwKLb022vFTlXLqAw0DCplEHG8oZL7ey1tBUiRrKabF6sTz8UFspQ0P7905WNFezPGI2CE7tt9n3maxZWR5s1LUiZUS04s7VySfU/P9NeVxfHpIdq7W+ssKhLSw1k5Xrzb8cr1m9Vm+yWqkyWB/c51Jcbgv5yhBCGu1W0fFagsYVZrVJb6oNvuZiWycE2rpXNKdacQ4UrOoTJcNe7xK25lgzZHSj0KJr/WG123QWJpyXqzw02XuYiBj28OQlm0qn0hZdFAUbjCFJpzD9jqR5XpGnYdThM5hWY7yYuJkqpE2PqGGBGLq6VGnsKrTL7h+trHOVsN81iIhozHtpYA1YeJeGMZ26YHvg4nqKOF+w9C6vl/PdowvITmdiqY0bJDwtD+VsUpaPL8gxJ3i65vtLCAWW9ssWHeWiZHiWXloptdU6aMykxdmLZQ7vdx4c1JOo7rw11q49fu8NCINndM7c7ZbVJqPSVyMtHuutxI9acpFLhEpAfcOkioCXlhdeNnF3JGWDKrXC92Op4w46ba6oNs5SRBXYrpR2lmvnDt6qzKXMhWlNDLyYdFgZ2qarONrOU+6yCpWAJhr5xxsMYq7pJeJ2DluiHKnXS3TSVZFuls3MIOK1zlS7Od4Z3gExqt1xlnNTC7j3ZWgzhV/jDX8tJ50EyLrWLRA2GndGucKNbY0yx91j11rlOnmfnBCpwVtsTK6JmRjtnEWqoqYjtAZqmwSQ1GwGxImXARfX/raS+KVuT+pIruPS3Ujr3Vitwt7O4wRTLLKbpKv8/lVrtFlZACQdo19snYBg9v6xujOg3ItTaONTBoXCrsW5mubw4O9sjita5GxpqoiJEVwWYcNorkS7mFe6PVTwk/itW6VV8YiUZYSUWqQhSRW6/MBxkqRXEsC00jkTooXU2Jrip3Vz0h25WXWKSlO6XUZ0VTWqyGjxJoRTpiZy4vsvL1Ic7ddFpcNfwXKrOEzwF/saJyymIjDpbcDuKPp04VPLAIjRDp+QsakCgvLdbSwjmdmBwc9ZYT4nsavpigtppQ52+I+nSLw4RQqqRrX6vQ8XcqH9XGAadjtpyl26epE2ufmspGXh7ZBiZVETowUV0jmJPO5xnjJqcNbgxxYbI/nVWkxxSJgsShbyaLvrmC865j5Yk1Ex33sk9VymJmNitD8JOOJRY/OEIM8EHTb8FNGdqKTyrZB6G+6ztywriFFxcw7h0iw1ArNEVDHtHx3aZ+PlxzNSpCkW0zbTHUl2LBYYZvsZM5n867n6D2+1q7lLuqVwNlJiHApV/tT4lW7jbZCTsfjQOCKfd4M+WyJXbeCzO38fCUmE9lDuSjN7bxNVqmUTCXzeEBdFa7WRlDpebj35F1ZcS49ySONUACNONlJnseXJYFFbJSsFV8ODrrQNfMkZmNnF+zjXixTgzf9NN6Su+TKSittyiXEuuvheX3yEO6Ugp4AVtCVWQlHB9ew83VTFuyp6d0YX+NsvKobT1NaxzF6S92iegbkMqKALHU0QaIKDfYN6TSss4831bq6CG3P6at9lR42BZ67WY8pUYOmPcu5CwfeXAXq6mPtcMDoxWTuoLZS6QspVIl87mwEdXZOkkY/HAoe7K3LjURkx6010+ZlgovzhpCLg7m1aoaf9uoAdgw6zbWOaDpKFPrIfnUJOHSqN8VZPQpmsc+7tBMzxKKCKG9Uf7cLGkMtxRjwdxYrWXzYcMtWvWRkgWGgD/NgGludKZZc9TZ7dOeq4WO7ei6co30yRNoB0Y9zGqHWzlLYJximrKZ42FoTRUOyY3GoL4CSpPlgyVNtWB8lmrS5ol7JM3USy9UqzIba57TVsIwD35m762s6XXLeYcbMTHtJap1jcKiAEp5pqrNL4Zpkd9EvzGpq0yyX6ZOmSPRi79WXI3zmOH2IY2wvLpnrcoeb1yza5GUStAk3tLFuX0x/sSAxUjQEw5yqK3mx5s/n7dy3kzDqbR/dlVJiT2aVusMUH786pWwdJ4OsSJ2jEq160CWub73GXTZNk7X+4sIS6naxEOCW5yNivy4l1IzsC70P1hniUMjlLFfrYVMtmpNvJVIl7yX0eOhmSHtYarSyG7pGTxPXXQ15pqYA5MsCO6uSyg2biazUvkwSF/K4Skv4KJ1sGmSbucYbVJSag0TCE9BkZIOnUXntGkdm6FKTkj0YPW8sPVVPE3LL2MvYw4LUXAYGinf4aZcc89zEmyE+nJlYO5vuNRMDLug3a+54ZC3NyiWk6ry2ctsdViD5IQjMldIYJ21RKYTPETBd5ytmNeOPoq2pCNi9l6CrE0TAjcS2a+dHj2+sHcJzpakR1VLRJ4gbDABOzHXkIf52sg/0Uxtkyo7aYDA+c+IZLEoImtU0i7fMeYk4rmNNMHICEwsmO7HApL3FTApATnQ8ULh+uJoTAOyg6ykJ5Wohi00h5GKW0Fu+MOW5He8HVzJpnhDwo24qik+RzAUP5qcOsKDSXnZE6BxdtWwic6twXjIclmm9dXZljQtXghNmdrzTqAbN6O2MP8+r2Feiid5Sl9TeXdX6MMfnFTksSnJDl+hSPyRst1/rDMltQ546DYrtXE+sdB7aHq1Wh3BCURK1XmJb1+ASuqjmZ4oUgwNmMDXBLddSVbPIfrg4EQMChiImH5s84+zFHCavDB4Zl8rUBZCT9Yx1kuX1NIkQkq9TfuCVteR4Jg2g1LjOy7NmYFZpTuB4arJSql0737FxMh542bNaAremi329YsVlarVqeMqKw3Vda8LuuLea4+SyWOmipG8RqTl51wnY3frEujqQjIju8PmypdMSvS5BUzfzuN3EJmiTn5Xz6ChEVK7PfZyw4Spd6C6ggyWxvMoVa0kMLW3bTUkdBtXz8AHskDrMHpgjr/oIMmGbnB7ioyrx8f4i63NxRWWIsA8a+6xcdqwyhfcku3CkRmYXMLyO8i3Yis7167yzThTv9PBKrfsLXk1zgT7ZxlaynUzsYX2Z+vO5trE35dAfaKMHOyiQZcwJ7RG0wqlgrR/zXtG63RyerOZ4jojRUkMIkU73mcgWk4CGJ+oyTarqlMG10fmEvpTOTim02b5iU4MkvYnMmJ41tBahceczifQ9l11d5sgxHu+nw2y1lOY64vnDFMMZ+rxSl1PxANhY3Fw0XSDFNN9mQW+Sfszsmq1QO20wb7kZsp/C4trc8v1QegQaIDJVelGOTqmys47HaziDcZhf5rR4lMDyS37SdsimhQ/SxK20OdWQmrDmmYSYGI6OryL04FCMQHmicNkzCrbEcL/2rHrVz6SpNA0X5m6unBltcm5M2MTXSOETUkZqpdVIete66GR/OO7n890iFsAGE6bpzczP0su2mrLRkZ4MMFs25dLdTk+mNScUle5ULY+Gy0xCRMrzZ1zWMYIRxdM8I2zCWYrDWiMTxI9J3nVKUa/LypuU7Gp5DLZn/giDmB9Sey0CC13N8U7B1stFmrBns9peK1fHnLU72sbWRTuI9iDmnLMwsqEUup23caJlrqpoO76HoPA1f0Vjdgmfh2HAO6dzg5ngxalU2ixFn47YtSeV3OWrrU0nxLZqSbG0hlkvzeyQbBbIBnT+PBv1JaOuWQUeW2ymgutzNpvi+tYX7bkrAtups7aMlspe8qMzqYH92Nxx1MC5UgLO6fCKmBzFId3vjf7AYhRcNRgy5eFOvc68eRD32Ww2++mnp+en21H10yuKMAj+/DQeTzwOGf6e19H+EOZvjzVwisKen/6+N5/3t5DvR5a3YwfXdF5vq7/+Her/8vxU2iFQ9f5qu4ob//Ea9L+9D/7877+9HuX293P78TT2Wr+f9dSmf3vtHqZOU9Vl/1ZlcXN76Q6C1lTj3/pUb49DkaebI5J8PGH5zvCn8W9vxtOMDAgApj7+Uul2ezxpdJ3QrN3Hpf84w3h+cnqQBKFdveHk9M0t89ETj7O18QXyeLj29Nv/BdEOCPH7KAAA -->
