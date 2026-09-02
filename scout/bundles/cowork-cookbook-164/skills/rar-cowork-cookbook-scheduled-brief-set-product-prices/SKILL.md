---
name: "rar-cowork-cookbook-scheduled-brief-set-product-prices"
description: "Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_set_product_prices", "rar_sha256": "55bf0fe9c1d44ff3c1ff30f967c49995c6f12148f6e08118c033ddf14bd152bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_set_product_prices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-set-product-prices:e912d4d3155499c3358e68852696e8003b5a0756b0dad7b4c948e59ddbb73b0e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_set_product_prices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_set_product_prices_agent.py` is
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

Set product prices Scheduled Email Brief — Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 55bf0fe9c1d44ff3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_set_product_prices_agent.py` first:

```bash
python3 scheduled_brief_set_product_prices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_set_product_prices_agent.py   # or on stdin
python3 scheduled_brief_set_product_prices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set product prices Scheduled Email Brief — Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_set_product_prices',
    "version": '2.0.0',
    "display_name": 'Set product prices Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-set-product-prices',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01f3e4448fe42ab9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/set-product-prices'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-set-product-prices', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefSetProductPrices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSetProductPrices'
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
    print(ScheduledBriefSetProductPrices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e5Oi2LbnV2Hy/tHd16riIQjWiY4YQAQVARFQ6erI4rF5yUseAvbt7z4bNbOqb5++5/TERIwVmSmw9nqv31p7U7+9OG0TFdXL55c9cHJEdNI0jkCFOLmP8EVXVGf4pzi78AfxirypYrdtiqp++fDig9qr4rKJi3xc7kXAb1PHTQGSFVUe5+FHt4pBgIDMiVOkbrPMqeIbvI/UoEHKqvBbb/wbe6BGgqJCmgggFajLIq/jkU3R5aD6BwLlxGEOfKQpkKrNER+yGxBI3wFwTodPUBXQO1mZgvrl8y+/fniJ4feXz7+9eKlT199UAz436rMHjfaQrd1Fw+Wpk4eQrhygK3J4XYIK6pPBWz7U/3n1Yw3S4APyn/957pwqrH/6/CVHnp8vL+M/Heo2mtAUTt1AdT2ndNw4jZvhE8KmnTPU0LqmrfIacZAaejIPPz1WfuNUlMjP47MfH0I+haD58ctLAVVwRj9/eflpNPzLC/QD/P5p5FL++NOntOhA9eNP3/jUrZsA6F3IDGr96fV5/WQLCb+RxsFd6s+Q6yOiLvjy8p1x4+eh92gnXPnyKSni/McHYxjGK8id3AM//vRXbKH7vXMa182/xfeXB+MIOD606an4Tx/uTv4VmTwNeuf512JLGNa/YwkkfxP3AXk66q943/3/31incQ4T+c3j/5TdP1sw+Rn55S9t+58WfECCLy8LkMZXmB2wXj4jv73uNYH/5Qf/280ffv0dsv6XbPZFW3l3Dq+Zk8cBqJvX119+qO+3f/j1lx/aEuYacLLXtkr/Gc9/5te7nD948En14x/XQvlmfs5huSPvmY78VpT/q/r9E2I5aex/u19/Rr6vl/EzQUYj3oQ+XPBdzdRQ1+/8+NPL7xAhcmgNRIDxMazy//gPZBt7VVEXQYPsvaJtRqBp4gyMyhtRXCPGs6i/7jcrWf6U+V8ReHcsdwgRTps2iFiNMAfrYYz4aEERIF//t3fH0I/eE0PR+g2LXu/g+Aqh8PUJha8PKPz6CTEiKLio4jDOnRTRWU1DnBDkzSjynhwQTD9eR6lQo/iBOjq/GhGnhrz/gXz912Je7xw/lcNoyJccRsaJ7yALsrKoIFJDjHVGpHKHBnyEAAvRpCrS1HW8MzL+astPo3cOEcifPvNgAwE98NoGIGnhQdWDGILyhxHUi/QKkXH0ZH2O0xTx4wq6qaiGe6eB3v48Mvv69avr1NGX/AHFU+TRYWoUErwrjHz8WFYgSOMwar7kwIsK5Ifffv8B+S/kf1p1Zz7K0GBTeLYaqOF6ryoIrM02g2Q1MiYGBJ577H77/RGKUTvYiBBYUXEQg/tiyO1bIowWPOLzFhxo86giqJ6S/ug3pIugX5C4gd6CVV5/+JKPLApIWnVxDd6c+Fj8cP1btB9yxpjUTx/COAVVkd1p7zk4BtMrKv8TsgqQd09Bc2FcmzGiUVE3MG1LkPsg9wa40mm+hTAvGqSGlVMHwwekraGpI+evLmQ9OieD8OQ0X5Etr8FOV6RvXXkkgquLPB4D/0zXx23IpPoB5hj3xuITogDoTaR0KqeMKqcGd7rAeWQE7HBv6yFzB8lBh4w9HYwxutf0PfP2f54i3js9ItyHjnvDR760BIaTyP+/CWXUlhVFXRBZQ1gggmLop0dqjSPVaOljCoOjwlPMWOjv48Mb0rxh8Jc8jWE4quEfD8rgnk0PmgeutRVURmf1O/+xrqs737iBOTEGuarGPHa+5G9g/wG6GUakHnELlu75YcubwPHpm6YRrM/x+lvjRx7pNpYBTGSkbN009pAAAP+e801UjRX1DAJMEDBWFywBL/qDVQjkDoMP+SNQiRhmKvTu3XUKrIwxKPc0fyePx3HqESOoLSwd8Ak5jJkMI1AjLoAz0UgDvfDDnRWSAehjqOK7h+vIKR/KjGPuU0FnjEWROQ34PgLPhzArx64C5b2XHOTq+E4DfdnBIMCK6h+RfdfzGSuobDam/33RH8P9tBX5viv9Yyw7qOM33IeT+T11vzkHYnWV1Xf4ga32XMPCzsB7nj5696dH+33093ddPv9ptv/x743/94Zq/jFyn5Goacr6M4o+mt5bz/vkFRkKcyQuQf2t/z1K7yMstI/PQvv4KLQ/cH446jPy97T7A4tnWn9G8E/YJ2x8JEMxY94+P9AZ/Efu9JEcn37JdfAtys9UGCENFrQ7vHeWNxLYXsIKhCPxo9PUY4PqYE+8A9y9U7xnwrNOIH7m4dgW6+K7+h1tGuP6CNs7EMNH+Qjx/jjQhWDc7KSj+jV4+Zy3afrhJXcy8O9sckawhckKvTHujaDP4YDUxOB+9T4sjRd/3NfdSwpigV98HisLNjY42H5A3mfUD8jbruG+EctbuG36ZZyPR5GQFP55p33fNLrgBe7TmqEcNX9shcax7Dku/1mJsaCgxtCQetTlrUJHiX9iAr+EIaj+zES9f3HSJ0zUjTO2Q9iFn8X9lpofEBg7WHSwjiA8tnDBn8VAORW4tLAB+6O53/z3zaziYcvvdzc0j/3kby9vcDF+f0wDj7wZef/7M9vo1Lde+zqydu4Mxsnq7uP7RPoK7YvHnvrdo3AcEF4fifjyGaIN+PAyerKK4Zh9u2+gXx76QEO+zbKQA8SNj/U4I6CwjiAn2LnL0YgzxLzvBIy3Y/9OP375/NcD8F8CwGcwxwmf9Kc4RZHzuTedUgyYMQxFzOYzwGDY1KUcjKZmLuY7Pu2S3pxkADX3fdelpy4GoBqjlMx5qoHiYxSgAe+u/r8Yy18eHGDPIKgZZEFRboAFYO7hPkkGwdTD4S8smM9oDyo9p7xZgBM4yQQzgDE4znjYdOr7AU66Pk4Rrjvye46FD7Ve30bwt7g8kOAVomcWj0oTjuMxHo2T/px2Zh6YYu7UA1CIT08BRs2nAcMAEq5/X/qMzRi6h+Vj3sKJEM5j11HOb89Yj7k4IyGlRNYr9vHh0bnlzEja7aPjpJqB0zaZnI29sfGbIU7dZqmULe4MHJEsienOZfWMF6hzbMveIVQdK7XlNS8NnJbtg4vfBmwGAHHerIqTUfVynqQ3Kh0mMKZ6GLOn4ynbLB1rMyONSXrKdzRf2bFsqPoWJlzaZ/S22cfRkZ4DP0C5GtjkurHsXA4WhHyzmmgtHaD56z1aGLnBMZfjJdtb+pXbXwQ5PTRrp9m1y4lppGHR4LeMqLhdNaOG1JT9/Kwwa8/Wmm4uFbSS3Qayye0Zc71mq6OMz4MgAgOO89ZF7vbAs8jjATc3TjsnMP2SXnm+v20SG42V+QWTj/aBhwloJ0ID6HJ+6uyDIJmkwCY8KWfSmvKz1PSYVF7oF1s/DFRvmuktvtn5gFFu6vEWrogH/6o7WTqkWXaOGnpRMf41sAi3SgCmot1t2erMrYvcYX8xuFzDehHgUyET6NN+VeCUF6puwQv4rZ5bixw0hEgmZ2x61djBGW7T0k441iovDF8CSBAGu0q44O7J6s+pfNpvF+oNxEteov16WzFVk9VeYiaZ3qHyUu/lE38941Jy0PAoCg5CegSisiUn1rwB+8PsePGmTifl5DG9JHu+Kk6z/KpuEskdQDnZ+MlBT/KuVhNBVynjVKMBPxOIDb7QA68qJ9tExBnDIgnMm9d5dQIn2ywaqvASYzqIDEY4ceuUyv4iR1uuui0J+0jVi2XWecRBBRfaNE43lFD1DbPu5l1/2qPJ1omGlcksZdET2tKYLW5HFD/Jfpxdwss82zJGfeP6GbMWXBCs+OV5pflgIoiEfrO4/Rb34U+zP3rHg95dCYK4VU7OlleR1bouiFj6Rol5s4urAvW2BkVvr1e7QHsv35VEE89mQjNMSnoJZo5hRo6V560eb9BjacWGJ+p8uVXiBLuJDtFv0IjBmWOAn8WevEb2LK45bCj36m4iYpi5MRm8twxVsY6ZVFmC7IupsGVFItloq6V4PtapQqgzjuXA8SiHnSnvU9LcEpoq8Z5aXu35rfJ4l/EDYptsAzFxPGGXSZzEC27a6YuTd5oFvGpvMI1fHyctKHHhKM4pKSAzjWvw87USVZ++MoEktQt3S0Mzh0OladWGpg8HCZtz0cKMNWaCxZdqdrwlG/0qNTuXcM44iGoRdlJJci1JN0ilw3il8tN9eeH2lsya8/Mts65mmJ5rFL2ebbVNpnvttIqEHp+jpYfqs1Xdn5v8EMpUs6+mvpyoWe1iys3M01V92Zy6hSknrlp7hozzG+Vm1dhaWk3nKzvFsB3fSaeh1zBBKkAgLCl1NaHS4twkNb8O6jVQDlhsLyakFG1SIbd09MTzu5Vo8ry7ufiM5rLn+XZ3EL1c2jQNvwRthV/lTXNquy5jxHzY4eZqTh1s/CbLvLkzzJa6nNfH3cWdneSu2dj1xjgdkwloh2WjEbl90Gyx8PF9WzGO6MnknOMiQq+27ZZTUQ5ryZimoPLowcFz7HRaMS2K8q1EoqF+CwpyGywWOXkqTl13sK4oWOwmTElhwxqmeoGZCz2JyoBXroa+s1ZDxDSr07RhLXubUGpwHVTSVoylkG8Si2ImMjWbs91amaTGHgQX4+bKFNeTS2Fz2aGqmVH6OmG4/fHmKkRJ2o7ARrO9oK/dmaLoSkOQs1Y1g/zMs5fF/uJH66uTsIMFujW1ubmZZ66MY2jh08zhdXx/CdrbKr8lxjU5mEtZWmeds5JtQlycUJq0cCnzLnmj2BTOoBo9J8HR4jZn8ZyuT+QMpafO3vSXx0nuVeYck9hzBZKdNzABegm50xH4nXbiwkQ+d55mURO5JxkfPZ5yKZkmjEJ5hZtKu2JD2ROHHDa7JRNGk/IsSopJUeXOYEtraG2cy0P3KK4ueirFqLleMuKFO9brpiimBH2JC8E+A9P3w93GXCtuSHc3Uh00ptEjzeMm1j61ZoY65dhrW5vJVqK3rSouDnqBr2+EmFJVzMwsVY+4PaWs+PS2CtEZiSmdKPt73CW73peJ4mIPPE41N1kUy7zbCmdeiy4olnjdoDZSowpLEpfsug09t+uJXnXiiIt11C0blUwro26vzmxe98r8diJYDdWJ8LRxS932i0MOpMle6RXCwC7rZT5bX9tdEh8wiL+XA18nyWkoGltoJ3CzKAbDOtut2WSouvMFmygtZ0pKp+JrYZ46h9YO8/2tkSmFNos5ubPMgVfdqd8vTLCQgSNweFG7qraY9ni0520PwwzjnO4W5kafFvyMAzs8HuzZLVF8qs6l2VnoNlcn3omwVVjWITcrkbJv6U1YeKFpcDhJnd311HNTXzhIm8NmYXcZNtmvWTlI7H1H0qpQU7ElCmbB+sQpdnZ5jd+0q5huju6yy91rnx6Unbx31hfLkMgrLVnZORGojMTEs1R2lw4HarUCK5/ZyufGWma9PMl10cDs+AjWG74idqnAn2YRcyn4y5I4rB1PKepiWSyHztkLFac7yiqM7CVm7mV3ZbIw6TSxC1HncCwXZCasWXFmXBnvmg0dSu/8teAlcPKw2JCMKBXbqlHYVGaDH/WdvQhYszigKAhcZ7rbnjTh3E8wzT/vpBNzMM86wbB5bmdTKdZKC/Uu0g4lGFxZQow1JykDbqwQ4lyy2OLsNZ0Ry87Z1lyY7ZQ0NBPv1uguP0sW/WmTbmoWRrLvl9aMaW9ZvheD7R6oSj+EaG5tWpFcZuRV4Owuaq2NGpPbyFxdZXy7M1O8jgImn9mTa7SyDXCwZONomCXDRxO2K9WJeKWOoc3v14XQOtKuOiuHLBALs9qQxTmaDtms2RWqsFVctjZXcANQcP3eOZJ7GueNprLLNAZuZOEsY/X6JGjKqDbWPTc9RlfAW3M4Bim+sB+qarOeLaqFdpSx1eLcc97+IEcUL+7kxXZuQ5zEWmnlEOCsJN62306mxKoouEll5r2oHklVMCZZt50oGx+jDhuNVzSb8C9WLDOXqa4vCc6en5KrvDwemumUMG/dEcY1xBfkaY0tjxQ5Db1pCHmvTha/Pdroee2jTnCRq4kAdEvaMSFtH1QMp7RzsDVaylxrjpIZNkW1sxWrUKmu3xT7sq6cVBW3+mwddpveLwJTU9g2sdWY0AxDKDbZYJ0DQlBDf5g7NF7MmiWF2bfdjDXyw5AyMZYeJa+q/ZtjYwa2BFP7MBSXNTs9FRBxfZYedgt7tT1j+WYnzPe0uTqUOWlLRZ6vIv6yXkgZMMu5S3sYT1Fipqyo1PUSlSkUc7AOxoZKZvU6jXr7QMXUipIWZGqjq/PFBSeKbyTLQjuREeAqnFIqq6zOKlmZ6yDdz2wBDhqr7FCIm2jeH5yhwiRDXA7U1vdqsOrzpaAcjXTCYaeFXnX0heCCa9eSeOmcBGWQeZGirJVbD9ZAK7smuPaL67aJSkvnZjBAs0zHruxUbzLnTBy9k9zqPNZvN9sSNSuO2RicHbW+xtNW4oXzzTpjyRM7CWUx5MUgHBg5bAyR8wqbyTcpU4EMi9Dj0il2s6IPQtaOkshuNrKUV/KJrcT9cuku+IA+r7dRU/Fxwvfxtu87Ylkme8yIQ4KciIF5zqaoK1KT2/qopU4EDieOtn3Yp0XiWmWeuAM8TixOE1e/hC7AhI1EZhJqsJgyaBKY7vIT7dGem0wYzE3m9LE8zGnNvwVVcriU6PQY9u1Ah9Nxh5R6VTz4NzgVKxGl4H2OLcVQko5X7aJQBkaYctha/JHtNFtnL0uhSd2p2h5wuGce8svBruKq5kygC5fIMTt8G1+1CGXnlEFdJLfc0KvZBIcOvgbMgKXbBQTm64xTA48ITUVxLYbENJ2eMHs9ATN1okR+eTlm3eXWMwv+lNvW1DXlg7CeeJGM1Q2dH425Y5yBll9RetiiM94TrdPFJ64BGaO5XRLmEdQTwpEIM5065XVFs9PdotX0tcQP2ZLkM93PEjava9GadNGgc6yaoaWdK0Dgw8Tph7O6grP/EG1XLsd7Ue+qp1zbHwbb8lsjXG0dnpBzjfYTnSRYFe602JLNKo3a366i6O0ydri5THyyAm7aqEu3I2dXDufnV0277bSLdpKT6+bKywsRthNqQdpN6uMDN4VbiokxUSz+QM3iKJ9kWtBwkSP6MuctFHx5uoC8WuV6AWCFU/mRzBlXmrbbM+dj4DamMr9BRUmgyY1RgEkdbH0lWk7nFw7vl7nAkUNjZCZRH+39McJmuJeQgtFMCq/vKsKYaFNg3lxO2YUl6uKnJhwMKsFnLVtbrTew+7V2WWOb0knmQ49SwBc3izA+oca6pRa+UM4H0B7NrdEUHHNy5WTZXw6Lk3yBmAg6T+S9Pp/qtkHfruoqYIGjR9VpfewXwLs02nUGBzApwTbdfDHZSViYFm7mZ36M9dTJE/a2XLPRzoedglhE3cpNt8vDFvUJnmnghkuIPVSyurThlUjLySk7w3I/8uvhQBv2EJyx2frgpWELuswOttzQSdRGV88WNZfaLTNPi6BU24qmZGfqNl0qFzvyTHsL9hhEydTLWcJTWDTpe9HpPO7gNT2qZH271XW1n1cntg8PC9tWCEskD/7Gza911jjzi3uVyeNi1+P0BdtKy+lUqHAK7A1F27HLFNUbLrh0bQKxplhctkGvD8fbfrM4U+IRlgZL+XO7m9yOnEC0VBdPe9apvMBUpZBjrjMJXV2z7OgbJN0egYd2BFig8kJbUJ4q79ACwuLNPA3UtC1RnnG9slmc2otJa+iWiumpDbKVmEu0F6LoMOmTyFSYKb9u7P18Mj8tenGqi9mKu3aWmMPBi6BcYuXdnBI+SYqsmnqbfkHHVzxyuGK1jg/ljGyDIK92wkIsJkarnebAteeZStPWeGKxaOTzptRy9YIvliuonycmMnfjwma9C2/KXlUlVdrh9UAFbbOmwGQ6daqUPtHzQDnJrCP0hjqjp8qxxO2II30tuYwnUxtpzuH5omCX2CDAXXfo3DRJiTclUyqEiLO34rYUfUrlEtdv6fkmzub05lAQgIomah1eUIdgsMNEbo55yB8pF3NoBcTLs1LXrTk7RjQ/1daTRV/NJYuhQg9OUZrq5gqfDlZEXMgCTfeciU4c21CuOUgkNhdJ2uOGcLmbHSp3HvZCstd2IadO8SOvifGOKZg4ve1uilevowlZ3M7rwMCmE+rmDElhozsfbK+47O7PLMv+/PPLh5f769uXzzg2w6gPL+Px//MQ/+8dAYe3uHx98prSBP7h5f/d6eTjpPDtFd/9SB84/ue79M9/R81fP7xUXgxVehwb12kbPo8k/9sZ7Md/fTI8rh8e76DHt5F98/YOpHHC+9F1nPtt3VTDa12k7f3gGjq7rcf/h1K/Pl8gvNwNy8rmeUz8nSGP9xNxmL82xXgcG1fjWXKcj+/ZgB87zdtl+Dzth/QDDF3s1a/TGfUKqnK09/nGaTyyHV85vfz+fwCw8B7zZicAAA== -->
