---
name: "rar-cowork-cookbook-demo-data-develop-sales-strategy"
description: "Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_sales_strategy", "rar_sha256": "e2d5f866300915fe8878d4de1ebf96539f841ddc9e0f0253751784cb50bc078f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_sales_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_sales_strategy_agent.py` and in the RCI capsule.

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

Develop sales strategy Demo Data Generator — Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 e2d5f866300915fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_sales_strategy_agent.py` first:

```bash
python3 demo_data_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_sales_strategy_agent.py   # or on stdin
python3 demo_data_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Demo Data Generator — Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_sales_strategy',
    "version": '2.0.1',
    "display_name": 'Develop sales strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3a8d9b521b60094d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopSalesStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSalesStrategy'
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
    print(DemoDataDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOj1nb/KkrnjxlHM82+zStXBZCQEEIgIdDicY3ZQez74vi75yKpe+zYL++9qlRFs7SAc8/yO+u99K8vZlMHWfny5UVzzXS2MuM4DNxyZqbOjM+6rIzAjyyywL+ZnaV1GVpNnZXVy6cXx63sMszrMEvB8pWbuqVZu9V9qV269+/gRxxWdWjPHDfJwKWdlU4187IS3GjdOMtnlRkDwqqeFvvDLExnJriXOlbWz2o3NdP6Tg6eh2mY+nf2eRhn9ayyweMyzKpXoI3bm0kOOL18+ennTy8h+P7y5dcXOzYrcOtlAaQvzNpcPIRqk0ztKRIsjs3UB1T5ALBIwXXulkBmAm45rjd7Xn2s3Nj7NPuP/4g6s/SrH758TWfPz9eX6c+hSWd14M7qzKxqF4Bg5qYVxmE9vM7YuDOHCY+6KdNqMhFAmfqvj5XfOQFAfpyefXwIefXd+uPXlyyfsAVAf335YQbA+PpSNtP314lL/vGH1zjr3PLjD9/5VI11c+16Yga0fv32vH6yBYTfSUPvLvVHwPXhUsv9+vI746bPQ+/JTrDy5fWWhenHB+O8zNrJS7b78Ye/x9YOXDua4uCf4vvTg3Hgmg6w6an4D5/uIP88mz8Neuf598XmwK3/iiWA/E3cp9kTqL/H+47//2AdhymI5DfE/5LdXy2Y/zj76e/a9r8t+DTzvoLIjsMWRIcVu19mv37T1CX/0wfn+80PP/8GWP9DNlrWlPadw7fETEPPrepv3376UN1vf/j5pw9NDmLNNZNvTRn/Fc+/wvUu5w8IPqk+/nEtkK+nUZp16ew90me/Zvm/lb+9zgxQQZzv96svs9/ny/SZzyYj3oQ+IPhdzlRA19/h+MPLb6A+pMCaxr4/Bln+7/8+k0O7zKrMq2eanTX1DDi4DhN3Uv4YhNUM/J1yuwQFpKxCAOyTDsT/5OFJ48yb/fKf9r1ofrafRROa6t43B5Seb8+C9+1e8L69FbxfXmdHwDcrQz9MzXh2YFX1a2r6Lqh7QGZeupVbtqCaWEPtfgZ16PP0ZSqTv/wj1t/uXF7z4Zd70Qwf1enAi1NlqprYfZ2sOwVu+rTFBh3A7V27AQLizAbaeCFg+AlYXWVxCyrbhEQVhXE8c0JQzEEnGO68AVpfJma//PKLZVbB1/RRSrHZo0VUECB4V2f2+TMwy4tDP6i/pq4dZLMPv/72YfZfs/9t1Z35JEMFJf3pC6DhRlN2M5BbTQLIgJuAY0HhuPvi19+e4AI2oDnNgOdCL3Qfi0FsRq7zhrS2Zj+jBDmzXIAwQDfJs7Keuk1Yv85Eb/auLxA6PZoqeJBVNehiuZs6bmoPgKsJzHlHMp06FAjAyhs+zZrKvUv9xZraGFAxAUlu1r/MZF4F/SKLwX+TmncisDhLQwD/exw87gMm5Ydqxr2xeJ3tpmic5WZp5kFpPmV45sMvoE+8LQfMzVnqdl/TqTG6E1T31HjA40+te2rRd5d+nnwOen0C6oBTvcn2n+3dmR3v3a38mlbPsDdL997YgSrDzG9CZ2oGf3uGVBVkTezc8QOaTpyeXnCeXrnH4OKvZ4Gpa8+mtj17ThdT62tQGMFn/6/jxqQyu1odliv2uFzMlrvj4fKAchqRJsgfUxXo/A9mU9p8nwbeaslbSf2axiGIi3L424Py7oAnzaNMNSXA68Ae7vyBYgDKie89OKdgK8sprM2v6Vvt/gSsuhcq4B+QySDSpwB7Ezg9fdM0AOk6XX/v40/YJstBAM7yxooBoJ7rOpZpR0Crckqwpx9ApLpTsnVBaAd/sGoGuIOAAPxnQIkQpAyo73fodhkwE0DrlVnynTyc3Ae0cBobaAtmUPd1dgI5MsVJBRITjDgTDUDhw53VLHEBxkDFd4SrwMwfykxj61NBc/JFlgBv/94Dz4ffo/quy6Q+4GpONfVr2k1V1nH7h2ff9Xz6CiibTHl4X/RHdz9tnf2+yfzta3rX8b2wg/SOp/78O3BA/JXJI6Cn6lSBCpO4zwACkXBvxa+Pbvpo1++6fPnTrP7xXxvn7/1R/6PnvsyCus6rLxD06GlvLe0V1AYIxEiYu9W9vX2e8Pr8TLDP9wT7/JZgf+D7gOnL7F/T7Q8snkH9ZYa8wq/w9GgbgrwEWDw/AAr+M3f5jE9Pv6YH97uPn4EwVdZ4AP30vc28kYBe45euPxE/2k41dasONMh7nQVe+Jq+x8EzS0AZT/2pR1bZ77L33m+BVx9Oe28H4FFaA9nONJ357rRviSf1K/flS9rE8aeX1Ezcf7xfmSo+CFSAxbTJAUkDZp06dO9X73PPdPHHPdo9nUAdcLIvU1Z9mk0z6qfZ+7j5afa2AbjvqNIG7IB+mkbdSSQgBT/ead83gJb7AjZc9ZBPej92NdOE9Zx8/6zElExAY9udunj2np2TxD8xAV983y3/zES5fzHjZ4moanPqyWH9ltgV0NMBE86nGQAQJBzIIVAaG7Dgz2KAnNItGtD8nMnc7/h9Nyt72PLbHYb6sTX89eWtVDx98BwDATnIyc/V1P4gEKVAILh+xBN49i8PiM/1oLiBAQUwcFGH8GiSxGCYQQjPpWmKdnDHRVzLY0gCYzwaRxzHZlzYg1ECowiEonHbImDLhinaA/weUflt6vHhpBOgdDEGQW0HI1GCwBmEQk3GMXHKNB0YCIApzwH1//vSCFTGp6EPwyYU32fVCZCnvb++WCQOKNd4JbKPDw8xhkmdt9YusJiS9NjqxkR1Lxk5Nx8N50I5BzhNiCgZ7eOVOh/s277QIlEzxTjka0lFXOmiwppXRfOBEDpO0C/F0UmcNO8TLPZTH28283RdNQUfSlwE6bWd7yRzlOPDCS0TrY6Dtj9I6M7lN6V0JfN9swoK+9C2UGdC1UY/nfZheThAfcHYKFKkYrFDYj3fxUbSd9K2qta9w4txerial5rcnAKtL9KM6M9uEA7uZpteaxPljov4eEHXfq+kI0J5HlUxMkYssfWcrrCSQtX+WhhL0y/EQjQqMj/lzhbps9gyw1g7yfWSUO2dt9Mu2OZ62Ns3THSM7cZs1cvRGLOzqOfJjo8cQ8mP227u2ViYXU/FSRqaC7Sig4Yv4ERbdUZ2cguhUm1pU8ZGXGvx0qrFspSIXdOjO+6GnOGCyihKHBDsCBvr5Aib0drd4ZFyGgidz7fXdSakGhtcoOqcxwt+Kx93WuGWqSeLmoSjG6FmWQO7ITDMRRQMKxwtN8VNdm/1NWKUzmPMCF4rsRScthRiDkJsHE+bNXs92jBH214V8r1RcvUu8Xcm4g7OpriQWW5E6AGq8CvUIGYambqaVF2+N/JFKnf7cyZbpy0mIkKbDsYFovouay5Wnho1irm1Gu7OyvnIU96x9zFX00p5dEdMuXZbwQqHxaUoweq4OxuIWY1CSbjiOj0aSszHlyOeiVCd5XJ/TYOMwK82cfZVTICz0z5Ik+V24TV9r+K6nYbxkgjjqnL3c5txzjAmFAWxVQhE1mPyMk+N3qwvx4O4b+Irsj9k2MZYKZ6W7JT8LIi5SVyu5Cqfr1HT0c44uyGlAFot5qywamtBVJkbB+HydayunjdC84WoLBC0LE8uQx01ywtX2qKWEPjk1JtkIZ0H9BTHtwMx+uRgWzG3XsmXhNgiHIlh3tGMJCSq4gPGba9wlLvKXibQFleUUNwcWV0QbiTcLzBOnN9ErvGhiM4Vh95G1JK6sMrSieHACqU8lIqrkCinK7w5BsMOW/sB0hW3jpzbZ9riZHeQlWN8o3K4v6Ke7I/K6pyxmEjHOLeU5wuZHi27tq3mGvgds8YQk7czC4HbeetyPWwnwppsh3nHtqVJJfBpDRMcJ8L6Khrr4dqS4m0RHfzktj/jp1u1Pktn/GhDnW1gJ0ZKEV6FuZuhF7jbmuNKSM8Fvh3S0DAPHQxtsWVhYbDF7jxyd1RUCAtpKimGZi1LxEm76AOSnXYIUh4kiOlFtgyI8qB762NCWX5G8we5YM7KTeq0tVRQIF/Vk0/qPB7o+eDbzI0iAZZdBDelftWtKMfw6FzqhggyZ96K/ThqWtbiB/SyqAo5k9AGPe0aqOuJ3hk4vbVY5KpJpmPHTq33PnWTHfGm7qWsOCtggxnB53g138SGG6/XakrjjMnTw2CfuRVC4lBiFfHqRl1DS2Xcq8wclKOPYQR+rkj5rPjXeBc76tJFebgZbpcrSo3XKC2xzK253oU8mlYDl1zgt3bfHW52et0fV0KdJt1iwdHXTRBT2Z6gRH3tBad068hyt/KkLDhsiaQ2mpPf+LjS7zwPuC7U5XOEreV2fZtvkmsoiNkoQHwvedudsFuu9OXSPMW8YWawPj+60p68oduldVr4XKex+eqghANnCft81/LUKVjjLOZvSDRb4eiBi45yzFW8tHJg/MpyelgsrXzNYYtV7B79Ml14lbKiN6KO8cdSYcvCWJdVer3FcqqdSI2/Igiov2MFKWdhbkfLdtycRHS0WvJibDaHgXITWakYfu/yoY8zvKfe0gFkFEndUAHpMvZGGCqOzMctAe3WC0Ks1guKoreqwuGBI2wdaxhKGwk6rQsPrK7t+zqtSlvKNmJr3LJajjjL2TGqDG8sWGVHc20Y226p2WexKdJNsScdT9vzTS5QYAeOwItqxYj4xg3QbklbKmhbhUJq5nLBMedN1V+gopJxuOhp4RoRXJ+dC1g7OgQwREElXd9DMgvZcnNgBwyHTgkhHq9GsURduL6W6C3zF1TbdRux0vdxmWouTApNMET2dXddlAES8mIVeTtrrMlUSg8Jv9WYNiDEXJZqGZIPB9bR3FOx4xtzS1hV640u3nXnqCeO2VoL1bJvt5UWUsVy1XmyDq2jU2bbJ1itNR7hVJpvDzvV2evbXPT3B5iZW7GGZNbeZQ89b+iZyQjL6/LAX2CyyAsYwhtTgEfi1FqmXyeVaPhNt2uW52U3gFJZpuLVUCJpoFX6FO/loD83Zmgduarnj4dIDAnNX15g2kd1CwoaIzTTraYNfFDjmjFsQ/PQrGh2eaiM64EXyx3bRtKZSfAoy5mtd7twmRaTBN2dxro/HtPANPNrvNyiWwi0kViElF0jcwFLbo5nuT0QXT0G/FJqNUQ18KQmnWWucn7e644VcteCPEvr2kUz1lccI7iQ7OYYry3OkU/QUUSWW5kYOPIix2uj0bcK6yPuDiDpCei2RW/Scb1jpVNyhprFVh88S2iYzmaFI4ruVyAs66itdmdIybeXfCB601K3eweicc+VKcemmMUOJnoOyfQz3AbzxcU0hHWq4TB6WuQGYico3rebZhQaR8np0nJMRBbQ+LjkFzdtQJHttvPRbC8tmXOeU2lR6xG+msO7aFPpgyHluLxlcOdMrDA72BshZ7M6wc/hgRhuo7x3KgIOtqdCMDY9o7NRLeFkR0YG75AJvl2VxpClapmghW4a1Dwt1KhbyRtsY9JIwam7YCcfYHSBhKtGUxOJ40fb2F8oojlFg5Dy0loIz9rSJLElS143GVRYnqhdPQtZocexympxTTeSigpy16ub3mjzlUHybWHpTINv2OtBgdUNm/emuxrUlbvsbHO12W4UoRPdC+16Ol6vg2EFknV79auAI/VVL1AsR6wqXOwGiIt1B6i3suCcOcaspV+Wu1QYzL4o80QzLi1PRFRIB6fzHIkw0h7xs5bvi5qlsh26SHtHoTerrLHknQbpI3+WfCupiF3GtSiqpcjBhKHlxboicBPhkmyL1NxQD/VqToiERrS0zrmCjcBadA6dUL+kbKSvs72y9Pc5ZtOtohR9ZJobZOykaIzsRqhwluSUW1vvdAoOuU0ZXSsLySGZTEwoyKHyVhONDGtxdq2WVRPv8lMt8SetNqsdxSm9YncsinJdzeE1W4f10W5NOGDn8Z509QN5FGi8K7DVdsFTHYNWe1zYgkU8hrKF3lmm5u/sXXIUmLINW42zO0aMVWm3wk5HnbSD1pmL5lwXNwtscOJkEzMXbeMuRM1hJHm9qXWLBTPqntaLjNr5K29ZsjXfzHlZuKm8rM6TA8nWGUeW2GWYS2AQUzAED6Rl1YkQSUTnygv9kBHQ7DRHiwQzl2xtZ35F7URq6PDE30LngUY1MPXrmBGRp2rBiBCyGf1Q72zdTI9DPm70gg21vsMWLC5zy+jijEuhFUwZLnR52N/Ou+OWRx3nNqcO7O5MjHtWyLhEh1KUPTnrlEJHVrroASdvRAwMUqdFCKOFgkTbOK0WyBJtM1dY8DAnubouoMh111ybIOxjCDR/ft1ArE4lgXVKUeYmidmwZmNvtz+piHfi9Z5HmaH0xrV37tFqzJECk7BlBzX6qqNc48q0DpljjVoX3IVBA6zCTjuMqu3W6YwYImxqZ5yY4EoO0C0VDuLhXI+ZsVBgKo5IalgsKmzVYKq/aQ6SdaIsKnXY9rivj2ONNIcxiKDlHjUTYUvfsrLEva61xF5gE3p3EmyMZGiBLlRTWSxY1poL8yPYreJnxoPLS0gtUzLrz2G3vGIcOlYWVQ1gLi62To9dEy/Gjhd/BXeQkhHYpR4FLCG7tU/TMgTVCAJ1LFkYF/KMeBCee7fsSllYM/csY2FlCUrHVVYK5zBhktsgQgIGb+etqa2Im1gbKZj1kOWq1fF5eZZXsCgoCibyF7qH9n54oxNGP+/taIS22VxxrucyMCIKO7PDxTJL/rYnyAXm+mZhRFzmkjaW7hQ66+f5JrQyTT/pB2jfJfOrQdDoRc1RA8u4rQQdIIQREOHSb3ymgVWfpiSqjLbzoNk5cXXdc8aV9G8WFalnh/PJlbXQLKZCBBgmlIPS3Dy7PUBlniEqdFLn+KXSxtxtIzHOllnlO2qLN8qcuo70WCdiM4IdfsZd+qV6Eer+WppzJiZd6tAa475qaFVcpa6CJ1ab2lZN+wkc8i071lhmjvY+xVPxwJ9X2yW1OpLqKRDGpdWuVKJg2H5f8Zyi9SpGn8O4DMFWqF6ntQFqDO+6tnZYdEbSZCwKtgvjZTMsMVgmNGosFbVlXZPzt+bm3C9OdLGRvcS31fUNlXAmYLJFsTclE8dO5GXAFXHhh+PG82/aLqOWw9iQRzCydGWJwWim7zDSkY/A5l7RqWKLC55V5ud6rhDaKB9qskFtJ97K46VPKpTY1wnDMkWgxppEO2CT543LHu2gc2cSOyv1TgurXQaHRUpuM6xzIOkyH3CQE3N2nNuouj9tC2mkTvXYls2lDkCkBTsWzB4YtbpZm629VVJsLKvcgtGxpddmDRJHbywhVLalzXsHlF7yF67jpXMtY7wbGHRrLUN2IfWQn2Z4czOqW0+7LBNam7ZoPHio1kdz6y22rsiB7RPj49qCGjDL2y8h6+og5zllNwNJXw4uM18vVIbw0N0Fytp9Am3nq23pIG2hsgxfniqTKmucsAMqokr5aGMNRqpQ1bZadWBcB+Itazi1gR1cRYkW4Z7bKXxenXJKmpvQBoxeRXs5ZKRRUnHRBgpT0qYbmBp/ESRtvk0pmjYI7rCpTtStUs6nwSVuznChkCvYSO89NhYxA95f7JxZ14sAFnE1k9cXPRPx3egtk2Nlo/kq11f0otmPSJ03TL1DNqRsa4gmg7BeMzpIFWcvUsq6p3Wht5YMnlIjN7J83wUeB2ca3AWjfStaiXNvSk46q6s/bjed6EnObZHv9bS98vB6xES1R+LlEbgviVufQgiUjfuEgfPujCQmU643uVt3tc+A/UNVD6pI1a14vLWlfxI6I+CJuhdzS4fImC3WZEz3SJ0iTT5iMnm9LMZuhUakekViYn8pFrmQaWxqURsWgw7iWe9TrElpz/ZvDcmkY6LsRxNriAFvF5kLsS5yNhttwUcsy/7448unl+mg+Xlc/E+/CZ5O8P7PDhIfZ35vr43uR8Wu6Xy5y/ryz6v086eX0g6BQo/D0ipu/OfR4v84Kv38j142TKuHx8vV6e1WX7+dqtemP/1i0EuYOg0gHr5VWdzcD2s/vVhNNf2aQvXteSj9cjcqyR8n3E8jJriz0rXNqv5WZ9+eh+FhOr2xcZ0QSH9e+s+zY7B2AM4J7eobRhLf3DKf7Hy+vQDmoa/wK/Ly238D0Zzl34AlAAA= -->
