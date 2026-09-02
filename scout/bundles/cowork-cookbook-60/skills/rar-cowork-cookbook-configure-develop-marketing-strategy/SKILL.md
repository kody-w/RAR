---
name: "rar-cowork-cookbook-configure-develop-marketing-strategy"
description: "Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_marketing_strategy", "rar_sha256": "297d66c6ee383af3e816e1df62d4804d0da1009980b4fd68390256d25b4e3f4e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_marketing_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-marketing-strategy:4ff6002cf89e381ecc3acb959286f90931b2424db9c7c08c172b2ae8c972de0c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_marketing_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_marketing_strategy_agent.py` is
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

Develop marketing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-marketing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 297d66c6ee383af3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_marketing_strategy_agent.py` first:

```bash
python3 configure_develop_marketing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_marketing_strategy_agent.py   # or on stdin
python3 configure_develop_marketing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop marketing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-marketing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_marketing_strategy',
    "version": '2.0.0',
    "display_name": 'Develop marketing strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-marketing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-marketing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90d014260935b4b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-marketing-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-develop-marketing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopMarketingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopMarketingStrategy'
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
    print(ConfigureDevelopMarketingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6a5Oi2Jb2X2FyPlT3mJVyR/LEiRgQlIsICirS1ZHFZSMIckfEfvu/vxs1s6qmT585PTERY0d1cVl73dez1mbXb09u20R59fT6ZAI3Q+ZumsYRqBA3C5Bp3uVVAv/KEw/+Qfw8a6rYa5u8qp+enwJQ+1VcNHGeweVcUaQxqBEX8dr0RhvGh7Zyh9eIH7nZASBNjgTgDNK8QE5ulYAmzg5I3UAicOiRsMpPUC4SZ0XbIOLFBykSxil4Rrq4iZCzm8bBnd2gXJWnqef6CVK3RZFXzQvUCFzcU5GC+un1l1+fn2J4/fT625OfujV89DR9qASEuw7auwrmQwPIIYV6QtKih07J4H0BqjCvTvBRAELkcfdTDdLwGfmP/0g6tzrUP79+yZDH78vT8N+6zZAmGux16wYEiO8WrhencdO/IFzauX2NVKBpq2xwF7Qf6vByX/mNE/TR34d3P92FvBxA89OXpxyqcPPBl6efkbyC8qp2uH4ZuBQ//fyS5h2ofvr5G5+69Y7AbwZmUOuXt8f9gy0k/EYahzepf4dc77H1wJen74wbfne9BzvhyqeXYx5nP90ZF1V+Bpmb+eCnn/+MrR8BP0njuvmX+P5yZxwBN4A2PRT/+fnm5F+R0cOgD55/LraAYf0rlkDyd3HPyMNRf8b75v//wjqNM1gJ7x7/h+z+0YLR35Ff/tS2f7bgGQm/PAkgjc8wO7wUvCK/vZmGOP3lU/Dt4adff4es/1s2Zt5W/o3D28nN4hDUzdvbL5/q2+NPv/7yqS1grgH39NZW6T/i+Y/8epPzgwcfVD/9uBbK32RJlncZ8pHpyG958W/V7y/IdgCAb8/rV+T7ehl+I2Qw4l3o3QXf1UwNdf3Ojz8//Q5BIoPWtP7tNazyf/93RIv9Kq/zsEFMP4dABAPcxCcwKG9FcY1Yj6L+aqryYvFyCr4i8OlQ7hAi3DZtkHnlxikC62GI+GBBHiJf/9O/oeln/4Gm43eEBG8PTHz7wMS3d0z8+oJYERSdV/EhztwUWXOGgbgHkDWD0Ft61O3p83mQC3WK77iznsoD5tRtCv6GfP1XBL3deL4U/WDMlwxGx4UhC5AGnCC4ulWc9oh7A/e+AZ8hzkJE+UDg4X9t8TJ4aBeB7OE3H0I5uAC/bQCS5r57B/P6GYa+ztMzRMfBm3USpykSxBV0VV71d2hvs9eB2devXz23jr5kdzgmkHu/qceQ4ENh5PPnogJhGh+i5ksG/ChHPv32+yfk/yH/bNWN+SDDgL3h5jOY0imimPoSgfXZniBZjQzJAcHnFr/ffr8HY9Augw0SVlUcDg2vGQL0XTIMFtwj9B4eaPOgIqgekn70G9JF0C9I3EBvwUqvn79kA4scklZdXIN3J94X313/Hu+7nCEm9cOH6aOPDrS3PByC6edV8ILIIfLhKWju0DSHiEZ53cDULUAWgMzv4Uq3+RbCLG+QGlZPHfbPSFtDUwfOXz3IenDOCUKU23xFtKkBu12eDi2+enQ/uDrP4iHwj4S9P4ZMqk8wx/h3Fi/IEuZlhRRu5RZR5dbgRhe694yAXe59PWTuIhnokKG1gyFGt7q+ZZ7w54PF9IdZhB/GExPCT4F8aXEUI5H/89Fl0J+bz9finLNEARGX1np/T7Zh5Bpsv09pcIBA4AByr5xvQ8U7/rwj85csjWGAqv5vd8rwll93mjvaQTAIIJasb/yHSq9ufOMGZskQ9qq6+eNL9t4CnqFzYIzqwQRYzMkADfmHwOHtu6YRrNjh/ts4gNwTcDAdpjZStF4a+0gIQHBzQhNVQ409YgFTBgz1BovCj36wCoHcYTpA/ghUIoa5C9vEzXVLWCtDOG5R+CCPhyELahG0PtQWFhN4QXZDbsP8rBEPhrIbaKAXPt1YIScAfQxV/PBwHbnFXZlhDH4o6A6xyE8w7t9H4PES5unQa6C8jyKEXF0Ye+jLDgYB1tjlHtkPPR+xgsqehoK4Lfox3A9bke971d+GQoQ6fusFcHIf2vx3zoHoXZ3qW8rBBpzUsNRP4JFAMBNuHf3l3pTvXf9Dl9c/zP4//bXtwa3Nbn6M3CsSNU1Rv47H91b43glf/Pw0hjkSF6D+1hU/P8rt80e5fX4vtx943131ivw1/X5g8UjsVwR7QV/Q4dUi9sGQuY8fdMf0M7//TA5vv2Rr8C3Oj2QYYA5Cr9d/dJt3EthyDhU4DMT37lMPTauDffIGerfu8ZELj0q5Yw5sG3X+XQUPNg2RvQfuA5zhq2yA/WAY9A5g2Aelg/o1eHrN2jR9fsrcE/gX9z8DBsOMhQ4Zdk6weuDs1MTgdvcxRw03P27+bnU1QGT+OpQX7Hdw5n1GPsbXZ+R9Q3HbpmUt3FH9MozOg0hICv/6oP3YWXrgCe7imr4YlL/vkoaJ7TFJ/1GJoaqgxj4YOnr+UaaDxD8wgReHA6j+yES/XbjpAyvqxh26JGzOjwqvoZ5BOyA7dCKsPFhMECNbuOCPYqCcCpQt7MvBYO43/30zK7/b8vvNDc19q/nb0ztmDNf3IeGeOnDBXxrmBre+N+G3gbk7sLiNXDcv38bVN2hhPDTb714dhsnh7Z6NT68QdMDz0+DLKoad7HrbYD/dNYKmfBt0IQcIH5/rYXgYw2KCnGBLLwYzEgh93wkYHsfBjX64eP3z6fif4MArGYY0iuJ+OGEBMcGA7xOu77EUi0/okEVZAvNwEicDj/UZH534GIN7uAsmPsvgAUB9qMgQz5P7UGSMDZGAJny4+380tT/decD2gVM0ZIKzTEDTPg2gkoQbEmCC0QALQhoPyAlKBmjgYijKshPUI8OAnhAsChcGOOWRgAhJMPB7jAx3xd7e5/P32Nwh4Q0C6Ske1MZd15/4DEYGLOPSPiBQj/ABhmMBQwCUYolwMgEkXP+x9BGfIXx324fsheMiHNbOg5zfHvEeMpImIaVE1jJ3/03H7NalScZbRt6IocNDeZxM0HFpFjw4XE/emt6ZphBMk25zwWNcKUtlLeKjq5zHhaqNRZ1vI4HlMkYx2mCFqTtnF5rOYrb3FA5vkgOQCmYRMJSgkmXcbZdYZStWXO3qKjWbmN51gbmtmqCXN5hWs4sFv8RRdbLDLZtMFlsLpCNdJ4jJVtkBx92Zs9nqYBTX5oIq+zYVq80a986zRV9eZ5W8auPY2xU9a2037exY2DIxP9LUjkyrTM+EyHFUuQcOI7NitS/iy3K7mcwPlJFdJ2MjK0YT3a7La0qzeshe5IauZ/PULGl5V5epXTQytjyq23IWwvoyd1ojUoavE/NC98Q2z9s1k+hlmjR2ViuF7O5X+Wk5z4LtNLeoPswWM6ZcpZt62/jWxFXnpFrE++66qxtu4YB6LUh6oybnkupdtjsVexm/SDkqGam3qkYptaPSfAsrEMpfl2Xe64YvXJU6xdTIUR37OgKHjTIP24Mmb0wnnrXbYxEwzkVaSSomB8l02h7cMdtttGVSHcYGP91dmeCo6Ds4mWTXTcHO+sJMCFHoGyem86ISj4eOb93DSDN2Dr9X2QM+Z8x5YzaOnmBa4O9K01PHO9+wbPds9bMFD6QY6OZWdsnY8hcbn9CEcu16QE9G+CjLspWWYJY+9mu4JQpRtQ5aeooD4siB+pTi65TNaNB3pk5sCxFTC3dH0mebD+xtedV255Q8gGC5oTfqNjLiw3GEx3W/mhPXzQbXW/HcZceY3KzOCdU0005Cz7XVz6XtteR3ZsEISjbGDXtrqdeyrcwrbVlp5KbhEs2WIC9lVN31KMWf3Lazhghgx0OyTQFas4oWKhFur5JRPA9jElg8xc3m50Yv8ljAQnyqouM5YZD0uNOFgz3HWXqMn3vQecmuFy2zCbBsD3f06751r5sk9iRmumJUC8jO6nLcjBdcLqNcdhH17aiTqzZJ1AiXJL2a8NbEjtzT7LLl1/tRo63YzgzzjgtIjRTixL2MVKXliZVsql4V8R66uYipeV1obn297E/HZF2fqVkRBUa8hFVN6vOwSpYHRpmTgQhLU1igKw8tzQkZa3OHyvDCpQhtHSXkiKNm7sZPPRwfX42VVeUUUFdbo+xM7lq5zAndSdBbQodu5qS1ozSi0dlOkR1lT0oyVntczVtj9Lic2IqPhbsiWM9GK7wvt75ENfsoDtJRO92LfDpPYBFRoW4aKwyfcBe9si8UxrJzty0ljWY38cnpZytPT53Mcs9oRaIJJjdVFR5zU19jmxGvnGbTwr40gbpuK7Io9CU+YnfTitsr0jQYryaj3I39opBLTLfVYh6O8pQkHHcZh0cHo1YkOonN0SkgpxHd9rB/MsGeybCpoQf4ypgx+3mlrmyrxupldVpK+/2REgt6vRVNCmVOm9NxQl64JdSNy2xHWVuZXKyJKXCnuYYRhsRay12JSrZx3VMotRqhCW7zYxvWst12/mmZbvQNPuGxlolJhd0XNWHSoTrqJCKXBYIZ19FJorq4o4GhXw/TzVidurumxiSO6oyjImpndjo3nOlR9YU55fPRicPCrThdGLtwt+tiXrWS8ay5TlRPk4vMKbX9KISjgG85CR752RKTqDomJt0q2HMORPXZkc52prId57tcVGs+dnSc42SQ5KKZROkU9Vbbc8lUR0WebQ6LHs0PcSEsuWoJdvNOQx37GIsHZaXK20vSerJlnoNue4w6mNUHMVHdiMcybjdbHHHBQi+EZBWGr8w0mh6bzIwOsqpndHNqyaknug6LTbKZaW78liiOQmWsEonLa91YEVeFYffdMgouzJyRRXGdZAQrS+duIjeSfSXI0Vk7J/3ElPpotAnW8aJkJztiKXOqJpuOpKG661xVNC6X5iLa0J7EcwQ+CbeZxBH8rNOqnRfP1od63ThLa0MvzVCPjuia0yVlhdLd7lADjhRmfM0tye5cklrp4is6X3LBWWrWybWpJwxKx1NJ6TBhm9glLP5guWQmmaR75YaME82ZaxTd+K6BUa2Z4I6XBLm2OO3YvBTZLCR9JZmaUWDXqU9d9ebaaPLueJUqudmstL1zEq+TC4ZTyRE3rD6IY0dhluw+9PcXUxEUt6QcRdJZ5nzwYgtfC+t0XZt65PJ46BzE+VwM5pg5AiquKo2L7bKRyKlNeUyXq2R9rAsjyRduP9keZyxoxq6+3Rv2Js5s48KPTlawU6ig32wCrZ1YzOl4wKlKxBNjuYsJfpPMpxdrGcjrtVnAerVsqtkuNtGRr3l1oxdWVKCZPmV5MN9vraXdGBIRVdx5yzCHfMSXfYrK9dE/2LxoHHp1MetV23Lm7VnokhIVg4W90Znssl5SCb6PShLfrv1CFFauvvasYOIS9EWz0kbuIX6ZuDpdpesR3ueZ2Xja6rSbwZ3kFHNGDizNzahpLhqHKyYGAFyN71uG2DTLTU0fZsxyXNLpKtlke2LOdYdAcyrJnmHeZifp3IlVTnJ5LreSMl4nucL5DmSSn4nlbF0lTudtSbUvUQFcFB3IzF5xpjQckfIDiZU86tuXZOvR3AHltfWJKPSAgY6ZoM5GvqLScWWMW8HzMbo+4Srfabax2PCrWkhxgqaxfs8klwXmNIohnauI6YPzWEHnHC7OTXlOchN8whD5WhLOy7F6tKre9xYGcepPpjfx8c15fWAyszjjDD63y2m0JntOXzCunZFyGc9WnK/QTUdNDHy69Y+LvdTLV9XZ82zvCiN9geFmhnni0jnsN3ObQ23Bv2Kx09GZwAq7WnYbsypaoYBzQM/MRUUNXJVQd0e/z22V3rtRUGbzrc45U57TojMf9Lt6aSTJlbQtMZg66kXYKhIjcZHTqrIWTghh5UyvES+Ul4UyNYgd7clLiTU9am4tqrCwcwXdnkh+ZC952hz5e/tAl/bhuLCXOMutqGUQLPJUxzRqVaPzg2yPDifBWPoGHQsy1/LSTGm2xwTrshVZN7kSm/he3291adtcNn3oaZNFZ15XK/la1SeRKK59qnIUjeaetkiwaGt7WlJSYHZVsJmjtmf2QMSGVVi1WWxpZSyHgaDDCaxCg0jW/etcWqdEu0/72Qbb+S1eZjhu2tjaRcfi3nMwlM544Wjw+jhdoYzdtOnObhmm5oh0uySWykw+uumc7xRszolCtBBpC4/yXOqviauKNDOZmU5f2iLuyz5HO0esTVJ6LZ+wXkOXNMqeAs8wSADonAk9YTYr6AU986TCys08hlmKlQfiLHocc11JewgCKIQ8FXcprQ8yq05HG6HATKkQd4urWqL7erkYC7jLG8eNdtEv4uky6+OZa2qzsZnj+54KJzTuLk5CKzqpWZxOVy+TY7C4EiZxSnl5PrEmJK6NU3fN5L4gZMWqS/XquJlGqcrHKcwI38dlxZ8WKXEJ1iIgLymFTkNrM+aG/rc4m51eWs0VkHiuaHNtorMqdd6KtiFsN955tb2eMdgERTkP5S6m2Xp0OXAQFtFlV9PbYo0CvM07e0QnZq91SuovZnMFnZQ+vVM5Mas1voPjHb+mdBG+mlx2labOhGVCwpnaRNuM8Cct6gtbfYVzvMsJW4a2uybFGq/misgUxS45hhV12esLS01cmLALwzFaZWmvJup8lk/9US4vzuUc0E26GHsgyvaMvMlqNPRGbblwovUMVkBF0rAZ586iBPhsVU5k6xyXDD5VmMJKvGMCzmkokIAP0rDAC5KW2omyG50iopVCD+6hjfOyCzIjsJn02rJrB7+cq2o+FbdJs2gJDaAktpZpUFm10h7RkNR0vqM2zLkql3Wz5dhAYaPWCqhMVreLtaUfTZ5c07493nVcGK+EUNKmh1FbG9z4smIvaLOfHgF3HgH97O8OGabgbNkpo/ToTnb8EZA6voxC/uRMyCBwW32sXeuS8TYcDmce1FgmSsAHTDuZ0YbB+eP9OAwnyzBRSV+lifEoG18aytgRbQvAdhzk0qjPwtVpldWzq6gvAt6iWhAd5IpRC6gVCRSDntpmqYW71m5EUC9h4BmSX+qGbKh7gm9ml4vRO0SKnhdLbcFeVdyhF5wXLbfecb0C40hIYXy062Ej+W1FpJLuO9Gm7peJoC5odZJfqlBLpixzEPDx9IrxbAXbwWgST/N6D3fjxFS6gKAJtv1sPIHjiTlXK86iRrBPJRHN1EuJuzquwFQnsj0ZcEjcReNmRzI4hu6O4+o88n2w7xWlJUj2MN8fYjAW0HYUk961Js64dupKKqguaDc7itMm2mZO21TMyKbOqRScdW66wMcrfU97rV2DZtJk+NSNOYHFSjxc21J3WkRgLS58UrRaBe5aMbl1haC/jCW7kKbCoYtGdtGSJ1LZeikFyjVFgJWQX7J1JiUrUqQWNL809M6fT8OIGOG+ElBYJhEHYzbtZs2s2kcYwBQ9PB18QzrirjX1Wo7d8WvBcCAUzWyeEgNxul/4YrIKQnDaTa3swFzDMu7GDQ6N2jVXNJuMtXOuqFtvapNBJ+wwKWCDGHrN8vAARWm1dbJ1uCSX/Xkv5UdiBPeNcoWhgLRHxAmMJBoXbKXyGZp0AjJRZZ+wgtOIH1easPd9OEKtwhHYLawdE8tWBc7zM9dcyiuGG96c04rZebeVcMKl7EAocinYEkVxAlRLuOhunvtMMPONNbWhDw2pSd2x4zbSWvew8coajT2x16YqP8nOlyiQFtvpMZ9IDHrahFudzWdsbCgBDrdTsRQJLn4Z731jyjpefV74V9cJiPAMqGDGUrK4IEhfGxPpeI8dR8dMMUgndkdk0IxLcl1v3ZSxA30snS9zCqcJidC9enQkaIGdnE+hlYarETHZFnSKWjIvpdJJVvJutjxioTO6LljHP05LNpofi925PZQjkcHPlxA1rJXAFaaEBWPDss57VbZjwg/5niaPV8UbWXNQLfdeaVN6wbvnqTBNjXqSa3okrVnuwMxTXjF8guczJuPzNe1Mzysi0RrL886eGSTs1KDcXDqJylGns64FhcgeeRLoAtmU7kSgqIhKhL0sVpHqL7y9SJ35dJ1ao2JJ6a5UoJSqaFqoRjVPaSA11jqWLbqFEXSZaKOBdBbalT1iqk3WzbejqrOIUwPqI4q29j68hk7sETjLp83okjpsh3GhRJb5IZgnx23Tu5N4sp0uN2M6xF3G1hgan+nN5UIK1TSQNJxgc9nkUMyWV1bN6ntrLO4kTNz4gA4vbg9HGmZU6A4tpnOaAK1q0sSx8y6bS8kHpnrguKfnp9uZ8NMrhk4I8vlpOD94nAL81Q/Ih2tcvD24EQxNPT/9733XvH9jfD8nvB0JADd4vUl//WuK/vr8VPkxVOr+2blO28Pjc+Z/+YL7+V/5sjxw6O/H28Ox5qV5P0pp3MPt43ecBS0k7t/qPG1vn76hy9t6+Gcu9dvjEOLpZtypGE40PoTC6zCvgO/WzVuTvz0OP+JsOKoDQQylP24Pj7OC56egh6GL/fqNoKk3UBWDrY8jqyEIw5nV0+//HwlFrO/JJwAA -->
