---
name: "rar-cowork-cookbook-adaptive-card-plan-service-contractor-work"
description: "Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_service_contractor_work", "rar_sha256": "c240693418d5f59edd7b0b40a3a6a94d4e6c46b010258f6633e8822856f1d99e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_service_contractor_work`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_service_contractor_work_agent.py` and in the RCI capsule.

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

Plan service contractor work Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 c240693418d5f59e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_service_contractor_work_agent.py` first:

```bash
python3 adaptive_card_plan_service_contractor_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_service_contractor_work_agent.py   # or on stdin
python3 adaptive_card_plan_service_contractor_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service contractor work Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_service_contractor_work',
    "version": '2.0.1',
    "display_name": 'Plan service contractor work Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-service-contractor-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b14d8887c3d5e81d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-contractor-work'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-plan-service-contractor-work', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardPlanServiceContractorWork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanServiceContractorWork'
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
    print(AdaptiveCardPlanServiceContractorWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81665eiWJbvv+LEfMisITMEeWn26rUuorwUUEAQK2tl8QZ5v4W69b/fgxqRlVPdPd0z8+EamREi5+z3/u29D/72YrVNmFcvX15Uz8pmrJUkUehVMytzZ3Te51UM/uSxDf7PnDxrqshum7yqXz69uF7tVFHRRHkGth+q3G0dr55Zs8pra8tOvBnlWuB2581oq3JngipLszqzijrMm1nuz4oEcKy9qosc70HccgDt2Z1r3VhNW898cO2ltue6URbMomzmWnVo54Be/QncsKIE/AVrNM9K61cglXez0iLx6pcvP//y6SUC71++/PbiJFYNPnp5k2gS6ADYqw/u9DtzA/AGVMCtACwvBmCcDFwXXgUkScFHrgcEf1x9rL3E/zT7j/+Ie6sK6p++fM1mz9fXl+lHabNZE3qzJrfqxnNnjlVYdpREzfA6o5LeGmpgq6atsslqNbBtFrw+dn6nlBezv073Pj6YvAZe8/HrSw5EsCbLf335aVL/60vVTu9fJyrFx59ek7z3qo8/fadTt/bVc5qJGJD69dvz+kkWLPy+NPLvXP8KqD58bHtfX/6g3PR6yD3pCXa+vF7zKPv4IFxUeedlVuZ4H3/6e2Sd0HPiJKqbf4ruzw/CoWe5QKen4D99uhv5lxn0VOid5t9nOwXcv6IJWP7G7tPsaai/R/tu//9EOokykBBvFv+b5P7WBuivs5//rm7/aMOnmf/1ZeMlIMCrKQG/zH77ph629M8f3O8ffvjld0D6vySj5m3l3Cl8S60s8r26+fbt5w/1/eMPv/z8oS1ArIGs+9ZWyd+i+bfseufzgwWfqz7+uBfwP2VxlvfZ7D3SZ7/lxb9Vv7/OdCuJ3O+f119mf8yX6QXNJiXemD5M8IecqYGsf7DjTy+/A6DIgDatc78Nsvzf/30mRk6V17nfzFQnb5sZcHATpd4kvBZG9Qz8m3K78oBd62iCu8c6EP+ThyeJAcb9+n+cO4p+dp4oOreeEPTNARh0D4pvTwz89h0Dv017fn2daYBDXkVBlFnJTKEOh6+ZFXhZM3EvKm/aCHDFHhrvM0Ckz9ObCSR//eeZfLvTey2GX++YHz0QS6H5Ca3qNvFeJ42N0Mue+jkAtL2b57SAVZI7QC4/Anj7CViizhMA9s1knTqOkmTmRpU3cRrutIEFv0zEfv31Vxug+NfsAa/o7FFH6jlY8C7O7PNnoKCfREHYfM08J8xnH377/cPs/87+0a478YnHAeD90z9AwnvpAfnWpmAZcB1wNgCTu39++/1pZkAmA4UPeDPyI++xGcRr7LlvNlc56vMCJ2a2B2wN7JwWedXcy1LzOuP92bu8gOl0a0L1MK+bmesVXuZ6mTMAqhZQ592SGaiENQjK2h8+zdrau3P91a6su4gpSHyr+XUm0gdQQ/IE/JrEvC8Cm/MsAuZ/j4jH54BI9aGerd9IvM6kKUJnhVVZRVhZTx6+9fALqB1v2wFxa5Z5/ddsqpreZKp7ujzMAxYByzhPl36efA5qdgqwwa3feN/XWFOl0+4Vr/qa1c9UsKrJFQ4oDYBp0EbuVCD+8gwp0BC0iXu3H5B0ovT0gvv0yj0GD/+oXVAf7cKPHcfXdgEj2Oz/i9Zk0oBiWWXLUtp2M9tKmmI+LDuRnzzw6MRAc3CnfM+i7w3DG9y8oe7XLIlAmFTDXx4r7/54rnkgWVsB8ymUcqcPggFYdqJ7j9Up9qpqinLra/YG75+Afe5YBtwFEhsE/hRvbwynu2+ShkDR6fp7qb/7FhgSRAOIx1nR2gmIFd/zXNtyYiBVNeXb0x8gcL3JyH0YOeEPWs0AdRAfgP4MCBGBDAIl4G46KQdqAjP7VZ5+Xx5NDVTxcK87A32r9zozQMpMYVODPAVd0LQGWOHDndQs9YCNgYjvFq5Dq3gIM3n2KaA1+SJPQST/0QPPm9+D/C7LJD6gCgC3AbbsJ/h1vdvDs+9yPn0FhE2ntLxv+tHdT11nf6xDf/ma3WV8R3yQ7ck9er8bZwayLK3v8DqBVQ0AJ/WeAQQi4V6tXx8F91HR32X58qf+/uO/NgLcS+jpR899mYVNU9Rf5vNH2Xureq8AKuYgRqLCq98r4OepOH2eUu3zM9U+f0+1z9P2Hzg8DPZl9q9J+QOJZ3h/mSGv8Cs83doDrlP8Pl/AKPTntfkZm+5+zRTvu7efITFBbjKAkvtef96WgCIUVF4wLX7Uo3oqYz2onHcABv74mr1HxDNfAL5nwVQ86/wPeXwvxMC/D/e91wlwK2sAb3dq5QJvmnaSSfzae/mStUny6SWzUu9fmHKmmgBiFxhlmpFAHoEOqYm8+9V7tzRd/Djq3TMMQIObf5kS7dMdLT/N3pvUT7O3seE+kGUtmJt+nhrkiSVYCv68r32fI23vBcxrzVBMCjxmoakve/bLfxZiyi8gMYD1epLlLWEnjn8iAt4EgVf9mYh8f2MlT9QAwD5V7ah5y/UayOmCHgjgeTflIEgrgJYt2PBnNoBP5ZUtKI/upO53+31XK3/o8vvdDM1joPzt5Q09nj54No9gOUjTz/VUIOcgXAFDcP0ILHDvf9BWPikB5APNDCDlLDCYWKEYsnRxH1+BekbasI3BFmoR1gpzMY9wMMKGEXiBL32CQFFvuVwsljjhI+5q5QF6j0D9NvUD0SSdB/seukIWjosSCxzHVgi5sFauhZGW5cLLJQmTvguKw/etMYDNp8oPFSd7vne4k2memv/2YhMYWMlhNU89XvR8pVvEgrSV0IYqwjMv5zlvR6eS0PQjkrdEVRykPI43Mtkw2LGq4/VNOCGiE8aSBSs5C4XrVX8lBT912m6b3OIIMxaUKe85KR2LHk+g1fJCBAG9NTsRx8a9k9vpMTLKfV96+q6IU0T3HLjdIaSeFou0213jq7HOuu14Ick5dEsIY1fCWq4kWWEFyHUUb+nBOAzQyhcFdDyWK/3mqirju00hI6w67xupYvgTnnapeLsM3YnQCzoTbtdArKVu5OIE2lpcvuIKmHDOOLw6nHFkPixxv9tXmGioHZJY2EB3LLEoGzXJmqt0K/eavvdE5pq623HO6KGToHmZq9hJta9x4ZE3FFitFbZ2kKfINtGTQUgYQF+5DudWjSSDSRmSiZneOBWDQlw3zjw5tWFJNZ0TMcI+sSVRcF3zbCWpfKsQr8Rv6qEkd5IhDVwsQ/gxOmlUNK5EJWvcmxDKC4beSd6ZlzJ1s4YiBvDZXO3GGQzfl/uBxlGBqdeBHof63OboC5mfKYjl3EsZwySrOo1isG5a7ZDd9sz7yXWMCh2pkrgWKyORtSu0oMKI7Tm7KA9szVUSTdRCe5FO2EKZNx6rE0zpKolJ3+rDiNDF2ohFR0MzRkEa83CaMyzUCcp1nnF0JPBi1Bhg3nBVf2u1dZsy8JwLMxfiy9reD/5FvZwMrO3V4mhrps1yXYpc0hbZqriHccCeWEohSkRK66WteHatCek1ixKE88S5TOYn+kBni+2e9mM7cvhS8MJss9+doLC+zVcZjFygttx1ylKKO7Gv1Ya+yUiqbqMLzcHXfV2nwz6CozhB3GOC2IpURnFDLvDA1vSMIy5XHeP3uJaQ7AbjucUmlhc3IfcqqFfXGbxYQWCR3LssY3Fonce0ujw7NXpl3WS/y1fi7RD5Yambua6ZhFiiikmuNworWinOu8q2d9o9ziMj4tDGbq0LCFrIsmIQo47Jy+X6oBQbzzSaExI1Z5G1KWPdMdsTdLJkPrM39laBI1iMra1ii4a+GfIisFzDxByNvmFj5tP8IHek6aVZfpYMQhhoWGlVfbBzAKWwCl/a21Y2ZbXZrkI49yFPzZGkXUbd6sRR6PGqMuG+hVFoP2xsYgHi3dWImr/CxNBCcBKupOPFRPhIOluKrjeScruJi2taS75kElS5D29C6WGenJZyqI3IGe43bXlKtqWY56oXFWMQWIoaqOkcbRmP08liU2MqbRJQO+73g6AwrcycBnQ9F06li6rYWBTsynUQYVDFXZSK1GXjpGPFbUcoZHaryjjmbuQP7FiF+ZyJ+SMre7lIHpfQGjSNzGXc66It81u7LThdWLm7Y3YZCVJWdsl2TI5zHkmPB1ZXjlUDbc5asXKDmEP2Au02FFOMZok1SQpxpqkVDBpp5+0WhaTr/mqkZkEZiDWkJ73tjkN6zBLbri4nNhq45cpPbMNsWGnhR4pmEaE35CiKz9MTe9KOwSVBUpfbenN60S6vtrASLp0lIGQ/p9dLY+nNnYMybzcseupv9XrhIgIL7RZNp90G7hZk7JkvNmicKS7LtsvUNcelHQEM23JJuGnWR26riQslI/HYY7XToApDjji+tlxY3bGmC39xQpGMyJeLJawEJ+oS6kdqHGJUFZp5DspQmW62S7GgqR4XKLPMVwZbpH3l6xy6N7SxoPZJobBwoqRlLzPnmhatGrpkzGaL9ozr4mkQ06JkOYyBOe5qwIKCIqSW1Ki9ofekdjEcaFWPobY0R1nuunbhZni0bMZtkA2FrW2NszvX6EooD4GdWJ2U5ccNdjK4rMtwTF1aMWefHaP3RTqksdzzC2zpHfy8hNRxdbzeCIJtReN2hHfszejKRFQpujO37s5mr2PIutaWHXe4zqfu0cJSaHW1xYtyzVBKcdflmBAUZgjxCfFjhA9gEguqWKDVAqDCgTp5Wp8e9p6pzbdecipO3onM+kGXi9L0CcVwouRioKPQIXG+rOWqRjnFZ8ubwsbWkscGZrhKNY5YWO+5slGqlkAjRGN5EaWFS3qD07l5Wq/2tixuspjUWmpslNTe1gCTGaYeG+y6divrhnc4kdnixnYWQu50fKhqjGCUYmRIm4yd6xCWkmtMiUNlmdnI/hYI6u16EbeJ5PBww47yoO6H2h8V6LIPhEV5WmtSVxwDRLk5W+GodZdtUpWWEITrRU8sq9jA+dVgUhyy3Jm3yuXiAlZ6DExK+N6sQInYeReR1/X1EVb9mDqe870RyqaprNVVfks6kdCai8ytGTo/YWex3wdtOZZ6VMNLCi9vQ6/mzPbmeJBvwR5iXewjo6yKiBp8YUuBOpgiJBs03tZdANMnRtiN7RgPzt7kIK8tpCO0UxurU682LPZo3lpgGNWDcWGjKrIL90WrtJISghhc1FJzzVV02KYai+103a5ZtIDVeMViMRxFeb5aD5m0FipV6HPeQwiDYHaiILe8W7NLgLSnPROfVJ1Od5tK5ZOOPqrXZdzb8nXV4iseSsPNcSMJKwgg0ML16Ng+KRx/q5fJkU97T282Y5NrFiK4OnxidZiKeReCDl2xQ72DKVBJdarXztGxLMkt+GtIbHw1hocDJw/jCkrKpIWSxaXqTeOC7C6rdiUUZRidLDEQopVFLx1W3g46T/dHywWtON+Egh7ORUZNDOqiplssinA/K1ZKOGqpoEfeeqh8lJFbthOywBcd65hU+m4XYMvi1B+4hRiYBWJmnly6t/HiRDlBQHWZpENbazGVmxuZJfGro/oASPs25YnLUY/YVj1ct3SCmmUQjqOIGJlSU4WTrjV+nRVEcC7ibTWq9m2tNZVTVDUFJ5m59rSDYJ3mNWbeYDhj9q7HbjFpvKy0XZVHkS5djgfKUy4EPoSUmYrnbRFZrBYqxPaMkjijn5bRSocP+70NcF7eKPNbpm0XfL+jtYORhXJyzuVAk1vyxEqym6xPO5KVuGLhlELZo3GlOLg2jFLLSrdmv+viVdV3CA1RBMNR12Z/GIeOY5p1LV+y2oWTPdtLJnsm5FDkXQaZ8w2/u5Zer9dVZhGkL6hm5g6FJVVoEaFJajcJlQ1nBsjEYp2Z7Pjj3BOl8IirNzl3T11C3TSFjVJBO20bUaIWXmNuV2u5wjqp7WIbj5VrQ1DOyuC0ReOIaph3tVi37ALoklC+cJKo7YrS88wwUOLM5LKZ75dMmfeQK4D25bhP9U0aM/vDqSyqAUcumEj6hbgLdxR6sWzszO6Tkg9El9+Y43UfDC7iDCGoNZdN6QkHIx3zIE3thb9cdGtaurjy1cKtHS61Ikxk2Kl15c1JjQRqd4iKs6ifLO4oRfUlGCoDv9bM9UDLh9bXcCY8sjZH4AnpQIbnLqo+1nNn76zLG67n5xpORkmiGtdXpA6W3ZKP6L7eorm0gc2lTHiiLlZt1Wsu75f2oMeXDosvaKSarLzXQuJMJFXM5SrAgzVFLtdmzDujw+rhUkpBNWE2AIZPXSPAiw6pzavuZO6WIq44YbRbYlv0Lnm+ddRpFOi1GwVz7jLWO04lRB41K55bx47Q7E2xmJtHPpkr0dlE4u6AmhEBgzGgMIzNpYcvc4rTcStqyhI/rWMuCN2sBGFYZiWah/QO0hQIyLB2ihtcjwJCo+AHm/uqA2qYgS0gUtd7f/DP5GZTbPp5C5MV6if+qnf0/uItadumexEk5QVfK/wmQUjCurKWo6qJJw5VQKbyeAhAcynjxorYJw1/LmqIKFILy2mKoPmY0aSdxWd4c2n7sAqyK3VYDNZR0fHuEIy57xhoKK4ph+owD6pAyd0sBPuEmKe5yhGwsh4tQl6sr+5yYaRlC99qYXNBQQGsTmvDOBDwmTNp1LS9ORIcFAx3O5K0yXm0Ro9VD1fNvLtpc05RF2jmOh5Z7bU8Q0/JLa/2536DwQrsrVOs84TLGjcvpdnvLxYeykREH83l4WhnzWm7QTdWrJw8s8sVZU1oHgZUphXQCvpcZ+iDpfvyCulFbIfuUZ6Q18GKTPcn48DrG9JOHTxEkw3YZ2bWNmFi1od1pbueHYjNKZSvSbRfxH7fstCAbbplFEAyLwcGZKDnk+40YMAlRTiM8x6+iTCZe7U9er24Uze38y3fFwBZat7iIMS+dtbZU1GomRO3Wx/iR9+3FJISFWG7Gg8qiXFhLo/t3BxsuqrI8yaM9inP3hInE2+NLw9Ys8pXBY4GuoyW4cht2tG/EeQw+KZQUtSBlCt8ydK+s2uTgLk2Y6T4ekLvKz5iShndc/OihU1e3my4QZBQ3q4Ttz3HQ55dvQslXze+iNUREwBVg429qDkpyER1yZGy4UnNbZVz41FkrHUECT5AXGGc65sbvoTS2Aw7c4OYjMk2e5s0Q8kzNmvKYAlqJ27tc1MF+WnDKfYG/Cbc22Gnk064R7mxwkCqyhgY8xt0scQXPuczTNsvnPNFlqMkvfTWXtEcMGQ7nXcbcm299nyFDNE8qFe1hCB7X7CNudtuG4fmWNkOTA2VTvNbjnG3MCeWh4UwGptQvIbVGRpsCGtwjOQWVbDZrU0pURaLK0qPYGbDV4neac3BxXy1tlgZxHoYY22bM95VwnixX1HU6bxiYM6rz24WBsrxEJvzUoj95sjLGuZ1qqSsYhS5Snglb/DGJUPmQNPwAnHP8uHq1R1+Xsu2VLcEWXDdGdL8ub2m/FWXQXDJpZS9AHC+SkZZN+ZjDeMRwaRNIKF+dJEGcnFu25t19gk/mEPDYjWGWwlHl1JziZCVgx1uLJdwKS/kPSMnyrke8YrkwExYrkL2mhvdwiohihy6RUEwBS8Ep2KHtX433s4xs+2gS3ekcNcu8NQgSW2MRquRtBRMGdaBXtGMXy9zUQ73yooKVowaXNeaAe1F7og3w0XtGhx3oKyyR520yFpDTXJrbtf2geDI3fmCW4ECO4crlldlLJC4gKabmGLigXE4NdxpNCcNcrkscIJF+DHfiNzlsltvcL2xV7sNmMx3RkB4uELIdT9AtgHABtp058yhz2vQ4VVrvyzyQ+2kKYFGtw0q76EByXHOrXHVdDbO9tYtMeF8KfmL7ZXQthaO3anL6hT2LTKjlmORBAeOciuht3YIgx9N1c5l3qAz+3Zdn1GFT08eaAwqnKptBVqhJsc7UHXpGi0daM6cQxSYSrr9md0dKerl08t0Nv08Yf5vPF+ezvr+144cH6eDb0+f7sfLnuV+ufP68t8R7pdPL5UTAdEeR6110gbP48j/dND6+Z9/ejHRGR6PcacHZ7fm7Zi+sYLp+0kvUea2dVMN3+o8ae+Hvp9e7LaeviRRf3sebr/cFU2L6aT8B8Um6k+tmvzb8wseL9M3GaZHQp4bWY33vAyeJ9GfXtwBODBy6m8ogX/zqmLS+/lQBKi7eIVfkZff/x8g+H+fFSYAAA== -->
