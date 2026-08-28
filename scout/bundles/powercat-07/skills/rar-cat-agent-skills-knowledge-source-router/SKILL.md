---
name: "rar-cat-agent-skills-knowledge-source-router"
description: "Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_source_router", "rar_sha256": "a6d2ac6a36c781505665b517953328f2dd809e91140dd40f56588569f87edeb6", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["knowledge", "routing", "localization", "location", "grounding"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/knowledge_source_router`. The original RAPP
agent is preserved byte-for-byte in `knowledge_source_router_agent.py` and in the RCI capsule.

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

Knowledge Source Router — Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_source_router_agent.py` and embedded as the fenced Python below (sha256 a6d2ac6a36c78150…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_source_router_agent.py` first:

```bash
python3 knowledge_source_router_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_source_router_agent.py   # or on stdin
python3 knowledge_source_router_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Knowledge Source Router — Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/knowledge_source_router',
    "version": '2.0.0',
    "display_name": 'Knowledge Source Router',
    "description": 'Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate.',
    "author": 'Adi Leibowitz',
    "tags": ['knowledge', 'routing', 'localization', 'location', 'grounding'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'knowledge-source-router',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#knowledge-source-router',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bcc9646e4cda8666',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class KnowledgeSourceRouter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'KnowledgeSourceRouter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(KnowledgeSourceRouter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9VZW5eiWJb+K0z0Q2a1kYGi3KJXrTXIXUVQQNGKWplcDnIHuYhQU/99DmpEVnZ3dc+sNS9jPqTIPvt8+/btfU789mQ3dZCXT69PjBciKxA6eRvW/dPzkwcqtwyLOswz+HabNzVA2LwIk7xG9LrxwhyJs7xNgHcCSAXs0g1AhdQ5UgcAKcNTUCMlOMHVX6oCuKEfukiVN6ULkM9MCsrQtatnhFd45hlhNIZ9RvISEZPcsZOfEMeugIfkGdIGoAQ3jU0FSiSES6ocsbOqBWWFVLXdIUnu2knSIbbrNqVdgxeIHVzttEhA9fT6y6/PTyH8/vT625Ob2BX86Wn5Dlu/4bmZVsJViZ2d4Ouigx7J4HMBSj8vU/iTB3zk8fS5Aon/jPz1r3Frl6fqp9e3DHl83p6Gf9smuwGuc7uqoRWuXdhOmIR194IwSWt3FfRL3ZRZhdjQgjLMTi/3ld815QXy8/Du832TlxOoP7895RCCPcTj7emnwVtvT2UzfH8ZtBSff3pJcuiWzz9911M1TgTcelAGUb98fTw/1ELB76Khf9v1Z6j1HnkHvD39wbjhc8c92AlXPr1EeZh9visuyvwCMjtzweef/kwtzA83TsKq/h/p/eWuOAC2B216AP/p+ebkX5HRw6APnX++bQHD+r+xBIq/b/eMPBz1Z7pv/v871UmYwTp49/g/VffPFox+Rn75U9v+1YJnxH974kASXmB2OAl4RX77qms8+8sn7/uPn379Har+t2ruBTFo+JraWeiDqv769ZdP97r99Osvn5oC5hqw069Nmfwznf/Mr7d9fvDgQ+rzj2vh/mY2UEqGfGQ68lte/Ef5+wuys5PQ+/579Yr8sV6GzwgZjHjf9O6CP9RMBbH+wY8/Pf0OiSGD1jTu7TWs8r/8BVFCt8yr3IcU50JaQGCA6zAFA3gjCCtIQHd6A9CvVQgd+5CD+T9EeECc+8i3/3Tt+ot9Aln9pYrDJKnQD6r8enfm1/LGOt9eEAPqyyFfhpmdIFtG096y28phr6IEkPYukEWcrgZfIP98Gb4gYYZ8+xONX2+LX4ruG6RJb5AcAG9ZeSCiqknAy2DMPgDZA7prZwi4Anfg9xuXIn4IqfMZGlnlyWVgX4jkZgbihSW0Mi+7m27onNdB2bdv3yBhB2/ZnTmnyL1xVCgU+ICDfPkCrfGToTG8ZcANcuTTb79/Qv4L+VerbsqHPTRI3Q/XQ4QLXV0jsJSaFIrBqMA4Qp64uf633x8+hWoy2DJgoGDvAffFMBVj4L07WJeYLxhOIA6AjoVOTYu8rCEdI2H9gsg+8oEXbjq8Ggg7yKsa8UABMg9kbge12tCcD09msDlWMN8qv3seWtZt129Oad8gprCm7foborAabA95MnTL8tEu4OI8g00x+Qh/9tH3PlXI/F3FC7Iekg8p7NIugtJ+7OHb97jAtvC+HCq3kQy0b9nQAMHgqlsl3N0DhYYm/AjplyHmiJunsOy96n3vm4w9NDHj1szKt6x6ZLldDqFwIevDTU9N6A3c/7dHSlVB3iTezX8Q6aDpEQXvEZVbDn60YeROO8i9ESNvDTaezJD/RxPHYA0jilteZAyeQ/i1sT3cvezmWT1E4z5lwRkAgal2r6jvc8E7q7yT61uWhDBlyu5vd8lbbB4yd8JqSgh2y2xv+mFiQKCD3lveDnlYlkPG22/ZO4s/w1S4URa0EMKHRTD47X3D4e070gBW8vD8vaPf4lx6Q8nD3ESKxkmgZ30APMd2Y4iqHGrvETWYxGCowzYI3eAHqxCoHeYK1D+4OYTVBJn+5rp1Ds2EZeeXefpdPBzmJIjCa1yIdojKC7KH5TOkUAVrFg47gwz0wqebKiQF0McQ4oeHq8Au7mDyMn4HaD+yOvljAB7vvuf7DcqAHiq1PbuGrmwH2vXA9R7YD5iPUEGs6VCht0U/RvthKvLHbvO3t+wG8YPph4waGvUffIPAYkirG9MOvFVB7knBI3/AI7Nf7m31UUDvWF4RljEQ5k5yt/6DfE7fO9utCZo/BuUVCeq6qF5R9EPs5RTWQeO8hDn6D83sLx9l+OUO48u99/yg+e6EV+SHc8UPEo+EfEUmL+OX8fBqFbpgyLjH5xVpsg/m+PyH74943eIBvGfIcgMlwnQZcrMKgHcbN7bge0AhmjyF9HevXKf76DbvIrDlnCB7DML37lMNTQuywV03dPlb9hH0R0VANs9O4M4Q3yv11nZhCB/c894V4Kushnt7w0x2uh1TksHcCjy9Zk2SPD9ldgr+xfFkYHyYjtBpw2EGVgYcbeoQ3J4+xpzh4ceT261mYLF7+etQOs/IMJI+Ix/T5TPyPu/fTk5ZAw88vwyT7bAlFIX/fch+HAsd8AQPVnVXDIDvh5hhoHoMun8Owi6KpPsH/qvzYeu/0wbVleDcwPbkDYC+W/h94/y+2+83oPX9rPbb03vJPrz0mMugOKyNL9XQoFCYcHBD+HwPNXz3P57YHusgt8DRAS60CQ+zXcKeEi5JTfAxThC4g09IGp9OMcrHPI8a04CeTGZjz5uNfZzAKQonaJ8igQccAup76B+6bzhgcSGxEtPJ2Ld9wsVsm5xO/Cnp4ZTrAwrQ2ARuNh5T4+9LY1gJDwPvBg3e+xgeB0c87PztySFmUFKaVTJz/7AovTuS+1lUXy1aG6NzI8NlvTGuTsBU+3TilWo5cXIlJdxVuQ5P7sYW0qWcXW3uFKh2veOYNR5y1yA7G1lcXLXu2MRbC+UV8VoAKcGBgaoaMHh329OXHUda4sZpPeKsnwFr2ZclW01G6IXPUFzwzskq7crltK7O8SHz13NWnRmlzyrL5jDdnFN8fyzT7cE5H/LenBVmmVrLSHDJrBnxSRhPzakzwb0d1TXHC154RhFtycyudn3nVdfDVE7Z8uCHzdid5yUzruIiiAQgStgmqNMVN2qtpUn17UgpsDRptruFoEz8C0mMQIShjVUuypIgGh+ftilxknd7QTjskstq4RS2SVfcfl8LdbFXitWlkHHNVab15FqU8yMljHZd4cQjTQOsjaer/WnD7vZ5yZnNBac9VTu6Qsnqk3HoVG57EfZxMwtMl7SqcKJIzlKVKmk24g/KZaxWI7EHUQwnsKnrlmpCErs9OTbm7DRQw4lRcNpFk6PusotStwkO4R6Vxlx0nG9GdrizA1ZZ7cURphMkwKSNo4xiEe9K0pjVHXqqzpRJJ16FCefS0hsl25/ntKOcg+PYDGdb+gL2siOYhzpY4lihKHVEd7BPqO3KO064aO9IWbHaSURfZCJmOoxu9Be1GIuoqEKJdn3k9DF1uDpSMw1oVjbI6fgkomvWEbmIK8ipCRJpjbWbaoqNZ5LVa9IypTZjHNuYaI/GS3c/9tqCw9TxenQNSiHbC069VQLL3MqHPlxPDjtd7BdRgirOOgP2lCYXGudVl4Va7GK7JjdGh4466eDa2KQ4pl5GAp01Hdvxd8tCOmuqhfVCgh+LrqFmI/sUXfp1cS12hOBdLRJVekdbaDXbLSxbR2tu1zHxdNbSxnEWGz3XBWYrLHb+LHXE84lpl8KZP3g9bsRCa265YxK4814/4ctNqewwXV+Wsels8DDw6uvSwpuS6dUiOZsTnLTkOKWwlnF1qyzW6XlDmasJ2fvzfqJs8ELCCNzdiYAJ8jMusluRX80Wqy4/zVlx0+6EuM74JsdC4aAEcrPvyFxNxjXWglmEZULFCGNSquhDKSVHUIz8tp9eJzJl+azbqllxFRZ8KvMNiq5lCWZOOk9QY8qjCwy1emORd/jMS0r/tMXFKR/4HjA1k2ybBTHvZ2XnB8CqHS5JKWWe0lKv46LZH0KrXRrEcm2sJPSEyysCoBOcIeNQpgTBlN1rBfNmo1ZCvUysUUmGAReslu3+yLfrkr24eCRerr6+nyh8vb2w6kqIx7KeS+5qsjypBqZZE/acKQquXCxcbP1tRIfOvGQMOp0wFGamsVNi+9GmcpPQ2oeraERFVYV2+LkVYk9gsRO0qqk92hPqfA8LjlsLKkmwdkf3pSWYnddLK3NVYewua+QTGfmeQzbcVghVd9oEK8MLr3G91IOxwfVbCrCeIWuyz/L2ctfHl+t6tvZ2JlpXtr84b/AcMK5tuCjhXA2UWG3q8RkyVjE6eyaPn2y88/fpiZYdtrp2HB42IBXxYKQX4nl3LEeEl2Q9tc1s10FHan+sCK7NXVwmipyR5EqtIzUbyVzS8gGjSFVSOwKUJdbOFPV3Y9k/cxVLJXsvJuqlOVY3c4s3ZOwwUlGRXGDEJsS545xLxVpqlMOKd+Yx2/eTTD13K2+eYfncsPhqqlDu0giy1WQ9A/VMrAPlIKBk6RYFuyc2eNnKadJvzgtx7Ihtoqp90HLiKWnrDOPUidueadg/vM2o1B09tK4JpaZauec9mdoKPDxFKRmpBytbVDxDnHeQQWtshxax3Sz01VXb7rNjMpqbzYYrQWydPNucgNIxcGHqG8Vp4roon4aYVRVcbu2ViIp27KlYOutoW4yrUudmcbyQBXELPTgfNQteDPNdYODeSlyKWBmvzMqJWfSyFdTd0ZwpCbbqaA9N1zM+l3uBEU1RzcGM37RXl22yzWEWGdypdiWDm1yP0yWX+qR7BdPC8RZzmgJjcyOmeVgx7HE0MRZnc5VNt5p6cvh5Itn8tS3BODtUUjfRl/aByxfCeeRb64m+vQb4+lxox204UcdZy+usZaghzXKazCdGnicmG1veahayI2GZynGRY3V3sBtgq56sH5t+vkskbT+vlYzZNpaKHZalV3E42SShsKx1UbdxDD+sTs7+MOdhQmo8sYlKQRL2yVKSI3WuZqEZHvsDR0yUoqK3glPp+CZJFnvzuC8ZVDqyextMVoHo2kThVSmXu+5aJw7kKd6moryyGmdnJkHeSRmHtxrBJuezeKLmRzzfUrPzIVLKmd02DTiQaaagSm2dVVywq1r3lAOzsFdSO0VZ+ZiYHQjnI3k9VzZb2prj54g3aG6UT92W01Quyefibk3kNG4vBLu3sFZSsSY8XljJiMfsnqnQHQj9VTqT8G4nVwf1PBVstOVm1LjhF0ayumiMNzEwLjeCglsQ6W4jk8byKJSHSGiI+KJ1SquuGNhcWoLNMzbbaNc+W+bn83rKdIQDfTnTMUHKrrTOdddwFuOeOtNNHLbJyipWZtPrY5Jq54DTmlKxglqfN7s+yUq63YruVeBzW6fTi9bg02paZjzpOatZ1CZYoI598iCldDnzmH5rqYt8YS2X0chKo2Ib9t2F8POxKW/6yWnttgd+xGg+5dU9c6iYcSxdFGocz5xIW+X6jC7XkcqcXX2L4soJO0nrVcqqRpCPw4DkerQCTX3IgtiJao6iZhrqmVRS+1Pmmq1jkj21qVfZIjXpvNxfToitxByL/hT5Yesm4qqgXL3lSbPRLIomZzUQAJzD9iR9bApxN94ZckLNRIpjJuv9acatlIlgNjQlir1pA3KO2WuOvRJaqjGzbDHZjDJtPlfnk5g8GRsgcjmpkErQH4NlHmqLcXwZWdeGXqwL/mQ2FLrWtJFslXp+IQ5cckFnjR81iXCW9ZFSelLUGx5/VilVUc/M4aweCG61CMBKvuimQx74iTZlN20VbVwXv061ZVdYc3FaJbq7kcZaEihE6xrXxXJBJmC9dBa1N8KbNr8K+WaplVtbY9ugE5kZ085pv1omGVBcci4Fl3irpAcPJZMNuSav8Iw418IZsEN7h+omKMtGJcaxql5dTZf4KWkLZcxVu4uEmuNrpBOMadnyObuolEVx82BW7SqCnekNGZyMQ6dqpl92hKyjNDobieP4LG7GXc9TzMSKuc4f8fxIvMD0lQx3W1/0yKsWR9UKBQrflz3r7GX3vDoQHtEYOb/ZoSZ2ICxSRaUSlRdJHhct1EwKKXVYjFpsaikYN8FwecFPcHp+1RfEUTs7aSZw7SY+FmNqtFA7wArSZgl39iXNPrmiCg40t4wiMBeDyOgr5xqTLnksp1dRc9SNo/LtJJGcUXANaNOyIBFZWUfY3iK+nLQomcvbviOLNpVmYTvK7Q7HpHPVLpZzDk6k5ygim3a3gwelwGijrkZ5qnBUt8Gz6XEGe7lIHk81lrUuXRSUTh1X14MHQTYGT8zCDbG1yslo2s06IXYL7GLSVEI7NJHrXSu7rnOZn5bzKF1USsbtFZlFs+ykLM5k1JFO35SaX8rJAVAE6/rCCStP9LTfGGoMwKVKa5sunIicWdLmOukvJzVKcTL0ZkoWR72Ys3LkyUd77RwVY8kQkYQbVRJO2fBoLBf+crGNdtNp49CVd0HNcsoqfrwu62BbYX6k1yi+CCZxX07zOe0KJM3l/JqqFFTDZ0TNdSmNSaPdgcfz5NJcCkLNjYZYWYJFo+Rm5LXe/lJcIxSVvH66MNcUynOHaUKTpbLCdTTqOEeZG4G99l2i2kwvS7dfFtFVjPK0pPbLrUB209l0zYz5GJfHtLLXtB4/h6rkHrcjXFyUGYADcguPNtj20JggOuzseoMbvEZI87xvvZYRT8XmuCw1S4Jtw8fg16bu93ip1XU9LYrmcCEuq43OUAtdIYtLmLCZlfJS0LnZxDDp2dEfZ/uDemIsS94sPHteKoS7l8+X67K5YoXosUfonkVr+7bXTPUYzl5HfZzRqDyPSlW1yKNlhtPWG40KhiVWHFa2OOxo/KKmmsNsf+3Z6WjFSJlPqOVsxQAmVNGYENfbbEUmFj5vJyytj0BHXGknPXC9mmInipnvGwGe9/PVNtb1MnRlTM3ohboQUtwQ3CBl8RpysUn7SdzpTd469BaMctbZ+i1TuoJFTTseHs9//hke84d7pcft0L/7s89wKfB/djdxv0Z4vwi+3QsB23u97fX6b5H8+vxUuiHEcb9uqZLm9Lik+PvLli9/cqE4rOrufzgZrqev9ftVWW2fhj/uf/fGcC0Dlww3R89Ptwv6sL9fF90fH19PUCjzBikI7nH/CDFhwwXk0+//DdYJjagOIQAA -->
