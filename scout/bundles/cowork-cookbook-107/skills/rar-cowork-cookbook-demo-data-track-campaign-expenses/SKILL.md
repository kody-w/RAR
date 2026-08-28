---
name: "rar-cowork-cookbook-demo-data-track-campaign-expenses"
description: "Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_campaign_expenses", "rar_sha256": "d703e6102687d31fefa5c588c9398170532767bc4417c3a37e7f6aa6516a41fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_campaign_expenses`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_campaign_expenses_agent.py` and in the RCI capsule.

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

Track campaign expenses Demo Data Generator — Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 d703e6102687d31f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_campaign_expenses_agent.py` first:

```bash
python3 demo_data_track_campaign_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_campaign_expenses_agent.py   # or on stdin
python3 demo_data_track_campaign_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track campaign expenses Demo Data Generator — Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_campaign_expenses',
    "version": '2.0.0',
    "display_name": 'Track campaign expenses Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-campaign-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e1c70144438bac5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/track-campaign-expenses'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-track-campaign-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTrackCampaignExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCampaignExpenses'
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
    print(DemoDataTrackCampaignExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjSJLtX9Hc+VBVo8xkFaBsa7MHAoQAgSQWISrbsthB7JsA1av//gJJN7Nqunu6y2zMntJuXgERHu7H3Y97BPfXN6fv4rJ5+/ymBU6x2DpZlsRBs3AKf7Eph7JJwa8ydcHPwiuLrkncviub9u3Dmx+0XpNUXVIWYPo2KILG6YL2MdVrgsd38CtL2i7xFn6Ql+DSKxu/XYRls+gaxwMynbxykqhYBGMVFC2YkhQLZ9ECIW45LrqgcIrufXxSJEX0kF8lWdktWg88bpKy/QTUCUYgKgvat88//+3DWwK+v33+9c3LnBbcemPB8qzTOfq86ua1KPdaE8zOnCICw6oJoFGA6ypowKI5uOUH4eJ19WMbZOGHxX/9Vzo4TdT+9PlLsXh9vrzN/059sejiYNGVTtsFAAanctwkS7rp04LOBmeaEen6pmhnGwGYRfTpOfO7pLJa/HV+9uNzkU9R0P345a2sZnQB1F/efloANL68Nf38/dMspfrxp09ZOQTNjz99l9P27jXwulkY0PrT19f1SywY+H1oEj5W/SuQ+nSqG3x5+51x8+ep92wnmPn26VomxY9PwVVT3mY3ecGPP/0zsV4ceOkcCf+W3J+fguPA8YFNL8V/+vAA+W+L5cugbzL/+bIVcOufsQQMf1/uw+IF1D+T/cD/v4nOkgJE8Dvi/1DcP5qw/Ovi539q2/804cMi/AJCO0tuIDrcLPi8+PWrduA2P//gf7/5w99+A6L/pRit7BvvIeFr7hRJGLTd168//9A+bv/wt59/6CsQa4GTf+2b7B/J/Ee4Ptb5A4KvUT/+cS5Y3yjSohyKxbdIX/xaVv/R/PZpYQIO8b/fbz8vfp8v82e5mI14X/QJwe9ypgW6/g7Hn95+AwRRAGt67/EYZPl//udin3hN2ZZht9C8su8WwMFdkgez8nqcAGJqH7ndBADXNgHAvsaB+J89PGtchotf/o/3oM2P3os2oZn5vvqAe74+KO/rO+V9fae8Xz4tdCC4bJIoKZxscaIPhy+FEwWA+cCiVRO0QXMDdOJOXfARENHH+ctMlL/8S9lfH2I+VdMvD95Mnvx02uxmbmr7LPg023eOg+JljefMXBx4PVghKz2gTpgAVv0A7G7L7Aa4bcaiTZMsW/gJIHRQDaaHbIDX51nYL7/84jpt/KV4kim2eJaJFgIDvqmz+PgR2BVmSRR3X4rAi8vFD7/+9sPi/y7+p1kP4fMaB8DqL28ADUVNVRYgu/ocDJsrCCBfx39449ffXugCMaBALYDvkjAJnpNBdKaB/w61JtAf0RWxcAMAMYA3r8qmmwtO0n1a7MLFN33BovOjmcPjsu1AaQNY+0HhTUCqA8z5hmQxFykQgm04fVj0bfBY9Rd3rmRAxRykudP9sthvDqBilBn4b1bzMQhMLosEwP8tEJ73gZDmh3bBvIv4tFDmeFxUTuNUceO81gidp19ApXifDoQ7iyIYvhRzbQxmqB7J8YQnmsv3XKYfLv04+xzU+xwwgd++rx29Sry/0B/1rfkCIuwZ+E4TPIo7UGVaRH3iz+XgL6+QauOyz/wHfkDTWdLLC/7LK48Y1P9JPzBX7sVcuhevFmOufj0KI/ji/2/PMStNb7cnbkvrHLvgFP10eYI5N0oz6M/eClT/p7A5cb53BO988k6rX4osAZHRTH95jny44DXmSVV9AxA70aeHfKAYAHOW+wjPOdyaZg5s50vxzt8fgFUPsgIeArkMYn0OsfcF56fvmsYgYefr77X8hdtsOQjBRdW7GUA0DALfnTHs4mZOsZcjQKwGc7oNceLFf7BqAaSDkADyF0CJBCQN4PgHdEoJzATQhk2Zfx+ezP4DWvi9B7QFnWjwaXEGWTJHSgtSE7Q58xiAwg8PUYs8ABgDFb8h3MZO9VRmbl5fCjqzL8ocxMfvPfB6+D2uH7rM6gOpzkyrX4phJlo/GJ+e/abny1dA2XzOxMekP7r7Zevi94XmL1+Kh47fuB0keDbX6N+BA+KvyZ8RPfNTCzgmD14BBCLhUY4/PSvqs2R/0+Xz33XsP/65pv5RI40/eu7zIu66qv0MQc+69l7WPgF2gECMJFXQPkrcxxmvj48M+/ieYR/fM+wPgp84fV78OeX+IOIV1Z8XyCf4Ezw/khOQmACM1wdgsfnIXD7i89MvxSn47uRXJMzkmk2gpn6rNO9DQLmJmiCaBz8rTzsXrAHUyAfVAjd8Kb4FwitNAJMX0Vwm2/J36fsoucCtT699qwjgUdGBtf25RYuCefeSzeq3wdvnos+yD2+Fkwf/xq5lZn0QqgCMea8D0gZ0PF0SPK6+dT/zxR/3ao+EAkzgl5/nvPqwmDvVD4tvTeeHxfs24LGxKnqwD/p5bnjnJcFQ8Ovb2G8bQTd4A/uubqpmxZ97m7nPevW/f6/EnE5AYy+YK3n5LT/nFf9OCPgSRUHz90LUxxcne5FE2zlzXU6699RugZ4+6HI+LIDrQMqBLALk2IMJf78MWKcJ6h4UQH829zt+380qn7b89oChe24Qf317J4uXD17NIBgOsvJjO5dACIQpWBBcPwMKPPvzbeJLAOA30KXMG1MSxgICgVGCIn0MCYPQWXkrivLW2JpCSHiFoSRBuh6OI6SHORgZkCHhOMQKIRwcCX0g7xmXX+dCn8xKoY7jUR6J4P6adAgvwGAX8wIERXwSC+DVGgspKsCD301NATm+LH1aNsP4rWOdEXkZ/OubS+BgpIC3O/r52UBr0yEw2VVid9kQId1e12k3SmanZkG2R1TLC0W7tsU9vELVEbGGpcGnGaMzXH9sXSO4Q8d4WZ7W6Q1TaYPRMnVIMb+wHc/p5OMOV9nEIrFBMBmaK0nfLHhCUhTCaM3SPGaE1V5ZLZH8qaQsvd+RvIcUO6leIaJFrpenENroh2QXK5UYZjdoX5u1adT7rLIm82TlJ16WpeaGcrS5iy/bYyyu5XNlj5zVrYhuw2v92SIqD6GkdCsRhtLzpX+QqWVY2NRKxWwY4lGnx1brpYD3iJNkR4vjt3IvFVafyQhSVo6Eq/50j0+qjrHVWOv5WjYMIbpPmamNvoW2NoqbcgEb902sBX2eVil+uGcF5TOSmYxnxOFxw1AGU8unAY10Hi0rXceYxCfFKYn9hJ+KDIl9AruQ25tJNLl6r9p1VvnQCTYPlcs5hdDzq3R5HFaZLMkb4Y6cu92kREysESnMdWNnulXQexRdSY3spWeDY82lYJrDVrspe1yIJhxEQppL0M5Zt0uHF+re1kyW8mGiSS2T5y7pvvMthQ4FgdxHrb0dXN2u2fPt7J1TBPaNrB4dHQqNLedvMbVEW0s5pWZUaNteTtgDh/SlbCbwGJzhJbq8FsVxnyr6FvJbsInxYantemKDetiVC9pzQ10l8gBT13GPd81+F9WYgx5YxbT4auSrW7VrrYDHMVOrYkUTAkpcdrtCGetbXlZIFYq3+CDI6MnTtsFlaPklKXD46TQFkqHlkjGNK3Z1RZDw7p2Bfe29oBDNqhLCP29r5a5w8abOcpOXdC8zDIrIam/5+LllY1M2Ba4qFsFlA3enLJbiBJzeHEJJPYasKiyHI1HAxBIq7uQGV2PPB7F6z/yUIpBd115drTojeZhWhjs6piXy6XRAU7qQQS7Ywzox7uy6xgJI25mYMBq1swnv2oTsCLYodDXqVDmqN5vjYCquq/J7rcP3R5pmA2lXLUND04JEbE+CthuIU83w3sgbezNTzyZiX+NxLwvXkzudtgwC2Sf4vrZXsQvr6fWSrDkru50U3L1MIYPaWy7kiPN6T91tr6Sw1F7G+JrGeYfrJBvBb0soVyezrXhhWYweeSgQ3x2mswCPTFzCyU7sbEEPYKYQuDuvbqM9rSSXjS1ZuO5Bw4pwWsKBzlJ4ZIZMsZFs2+FhURu33d40WWeC74xyI++b1L7jzb7DJF7jMGwcJ+p6tq1r7O/rMZzMprHhpiMcs+/DvIqPcl2bK3l/9XRfiTR/eUxMyMmOma5pso9p1Cno2C2LsJd6u4UPh0gaGu582rmZ37Qb5W7olN506cTh2bKPU80+5rIBweJ2x6l1W4poD1lKHw6jPV6n8Vi4R+aiOXWYmybsXPCw4vf5yUpFuBF2zR7NjCLe7uzKdJBakHcGDknb9X1KbSZfijjU2PVKOrottL9mZsaSgW4GwjLQVwxDMdMFNY8r3R0EDerlmwAn6d1rzjc/iFgUX95QN7xuaGGlhwO+FA7hPdL0jGkb4UydGeoijmktGcRq1+5Xp1AVg0CBzhNdMyO7YosGs3fmuA+rOrwSAc4r8l4ur9IhX116bBfurxahrq7pGknPUJGwwSDtMJpB1UpJEy0kFG4pyYdLLzuXiFa1YLvb8ihyVO3GN3tIDm/Dmubg6mQilc5q0Q6qvLS92A7cy2xMa6UVya7ocZkkruv7gDXX4nY6cwqdkffjZm1GBGXXHmlVcNYbq9xXXFuZ1uodIdaqpp5KXnAkcUSW6z5Ny4G4dQ6P9aOoMozpq4ldjNDSoZmou2MC2e7YkxeHq/0B1gcqOBQNTOxAEwkjS+Io8/Kxcvo5Oe5ngVFo0a+PcHx1D3g37ug0Ryyphqcj31MYwt3PinFm1gPnak6ChFEdX22FNVbIUYITWIsUUjzAznAOJY/GppxpKBONAB/BTYleplJmO7BhtXHizEPwKhMQlR0UKKnpaonru1pXDneVlEbKInlHKqnIigQulPauH8hwp55z4tKdco8pLALiPYFnK3qkGe9Gk/vKq+/LLFWWe8PtJHfve8f9xfa5KzmgllF7aCu7662cY8I+FBNTrFeJduRrQ0KO9fmO3JTbssM7V5c3S10ugtPx0rv0/dD0YkYah56b3A5n90iwl7eCWglEHHssfzoceNWsHa/C26OW2ZRzPsNVrwX0hl/6aWQrpmHvGfqCeDnZ8ALRS2p2J86l55RTUu6MyBvOGhfSQyIx+C6UcMmXkBT3SkSL/KzRqNru9o4u3MPtMcdqjb7mbNInhQWZaOcbK3fcR52r0qlnwPnQVUg05PukUXeiRIJQ3BSYmIuKZB0xeFo7Ruz1hcO3pGFRK9RKare2NSSCENuqJ3lMldvJobXYQ0iZVq87D6eajWxUvnmWm2Vx2uiwPZ1bSb1xmmDiPXzcL2GcZVqi2vjURms2KsGE+/PxLq14nuPGKNyG21N6KzXW2LWFHFwCHztUAgyLztEtlRBzBPTOLNPCWuPIVinimg029ET2Z8+nxXOlOlUy3okmFI9raA0FWgcKs02zEkzEDFbya+R6QjcXwg+L8OTAuSZX5ton8oG82fXIT2pjLM22Xwf3zU1rE4YfKtP3w4naHSRuE9Ow46AEc7VPZ+bWsTbb8PuaOam7JrixOFl5q1TgvciKV8dwAymZ6OL5/oztiWMGnCmnJdFEGy3rCi/UpCxYsxf+ane4ZCl1mfeukw1sQQign6F3GGZReslvYGPABZ1TgnKJi32q800CG6OQ5iLUiPmeEamE0S9ZWomtWnFqvtysV1d7gnsD7ZRl2pJHeVqtZM1CriwlnDRKK1GdV5gIU+qdGXI7tGpqOaK78aLinLJVudGTElmxN9thV7tL1TVJn00mNMpF2Y4m0NEZ55EXjiJJ7Cl5kDA235wQdKpteDVqGZMKF7jLeb2cWqzhUhpNVA/tTz3oQs5+gRHAHstown3FkqUI8xgZl4LRdXmPJLWEyBVt3ftdifG3WEmhoYRXtTqicVP5Bz8tqRPW5n5S2+uJROJCBsx9YTDzpFZttd3pWroVB7FThp2wOcsI2waYpYQXjRc2ogNtThvcQiIX5TYJSsEce7pQZWs7q1surydnRNfXgrIOIdxVbSzVadum6E3KTF1LmMY+3QIOZbA8UochyErVjbg2w+q0UYvKgktBq7PDZteB5tnAbdu1eraFNXdb2pEyGjmIrYR3kz0vnwCvjaJLUeeTlLP9xk4nvVNyeKlzrnC9ZdA242l9kq+Fe1d1OVlf83K/Fnm4GrwaZJB4lEx50KRrn9NOq+1V1JFha9juoV00EXZRini0o29rUr5US9Ijr+c4jY73oYEaVVqz1OVy05Sab7rKnkrO20U3d70npmgoIvmWTTcHcCGcWrl4OXvMWhSo1C6u8uUsqbq4Oi+z3VkQhcuF7SM/566TR68Iacy78/EsbV0RNHq9CTYDvb3yS1ytPaalN7BwkhBYj0g1wfzRpbOdOOxy0OKQ3lnnR+d0jgZbxUuM3YxjdRHE49BBcWrafLsmLsS2ya8424dG6kb3cblV+66pN/nlyPAEyLyt3t0au09XJX67FccjtweE3FyEAuyNlaV0IsN6DXZ9fMDfurzCIDxvRINCT3BgbUPEXbe9H3nWsDLIDknY2EVHXK+2pxLUBrazWMBYvLkhUOXQYvlmOgyqeqpJY927WVUeyvaMrNEaE4lhisCGan+f8o0In1AqpM79JtwM94vQJJNz9zzm5kBYFuEDIwT0jQjV29GMLLAj46AL2CNfHO+8uaLDHvVBv7L11113ugRqo2JUc5En2tWvOMkW2gZrXc9t9t51pBAICswC2jHtyowrbB+Go0HdKhuzhEBd3jg5tIW60g0d5bJEQPqo9ITDqXcYSCZzfnOerqO1jGM4YWmjg/ilpwxHyfNzjY9X8ZIRBWGl4JFKk2KxtE6Uh0+de2xWWNszHY2aZ1444aqgIgmSFdw2Xld3FRSD6SosAUGhsXiymWLNc+4qtothpNWGbwKKbxuKHzDUikyIq2UUPwXsHWxklseeyPFpJV+IaCNj6OZ064/rAN7ypb1vxehwNyy9uA6n5gKhshGSNSGdIOQGoYC1PCO17kYwsJx2OlhXwrVoqhNRH7vv9Ysf9MiAX5JVRKN4eW+hM0JBYoIRMVoUAZPew1rwQhVj0QMWGHeXUY6RCDlIqEQ7Hdd5qqMTpvcSEeHcUfWTvVVe+/Mt9KgdfQzzlh2RLV66l0xRm6rErSisBiHOudTrefHa0F3DDWuC8U7iUkKNzvP9cV0K9+Oed5h6Kbp6fNKxVSlc7zh02A+sCocm7WmjpmHYsL4HJ5ahz9uc2e053W3vgycxbNnFtcwuoYs+IWdsd1rfqWRJp5Xf7sJO6fJ1HpATyR27Kb23q0qmrPa+3YwE7WfLaZVeoc6QPLHJ4AA3R02GLNon/Sa189DvubW3EbYqFsF5r3SrKwMfrqwJ4ztPzylhY1usczOsAsW7FUEKfRWxEnNRMlAGXGxDlr5HkFIR5MSZHP0a2+0VjWzRHd53kbgW3OEoxiRNNypxafn1Vlqpdy6JDrsR4rcNXkemV4CmM10mpHirGRchPPbukMWGDTim9JdLzTts1rZ7u+HLsGtvK7cobtYyDLtLTIfrW7GEayGnXRjCQy8P5TOyxA3zluZxVZjsGsMoo9UD54oBiFyLpHho6Z9Fb3O9nclEQdayJXKat1OpnTHSSiDVCqmSPCZ6OZu65iGXYB+0daRoDaGGLJX7UWFEdYMoFq/fIV/CryUMTcoIaOtuHyipwx17dFlZP4U0IpIr2Cq9ihLWbAKvjkq5ZyuJU10iucb3K6y4+95qGi2wbh2JtqsADZYy2RpHFZSWwmcpQ06X3cCApBspA1k73JpKyTsz0BtkiAUeKTfUPb5fkjqU2EDflltfdSKdlYfSlTvdqo5wNYtlbLLn8GnJVD55sGkLgvr4ELVNbEU3eAtj007XbX/Eu3XO3zwX3p4xUjVzjIaZfZiAxgh2NOWMqdeJHY0dokNXa2v53n0fXjgCEthIhTlY5St0Xe5PO1g3drTerZshXJapWu/K2oOhyOWMEMPWtBffCR9F0QDdHwnhBgtXFsqYE17RNP3Xtw9v83Hz69D4338nPB/j/a+dJj4P/t5fHz0OjAPH//xY6/Of0OlvH94aLwEaPc9M26yPXgeM/+3E9OO/fOswT5+eL1rn91xj93683jnR/HdCb0nh923XTF/bMusfh7Yf3ty+nf9oof36Opx+e5iVV8+T7pcZ8wl4Ccysuq9d+TV3mjSYnyfF/PIm8BOnC16X0esQGUyegIMSr/2KEauvQVPNlr7eY8xHr/OLjLff/h/1m+HEkSUAAA== -->
