---
name: "rar-cowork-cookbook-adaptive-card-develop-frontline-team"
description: "Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_frontline_team", "rar_sha256": "3916005c1a01dc131cbb03bfedb935e25edfd7cef9cf01d3ba8561f0ee5376dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 3916005c1a01dc13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_frontline_team_agent.py` first:

```bash
python3 adaptive_card_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_frontline_team_agent.py   # or on stdin
python3 adaptive_card_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_frontline_team',
    "version": '2.0.0',
    "display_name": 'Develop frontline team Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58c3e36e74142fb2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopFrontlineTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFrontlineTeam'
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
    print(AdaptiveCardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bObyLLmv6I57we7H/aRAKHFN27EIAmQQIDEDu0ON0uxiX0V6un/fQpJ57j9uu+b2xMTMfIiIaqyMr/M/DKr0G8vdtuEefXy5UUGdjZh7CSJQlBN7MybbPM+ry7wLb848N/EzbOmipy2yav65dOLB2q3ioomyjM4/VTlXuuCemJPKtDWtpOACenZ8HYHJlu78iasLAqTOrOLOsybSe5PPNCBJC8mfgUFJ1EGJg2w00nd2E1bT/y8moDUAZ4XZcEkyiaeXYdODiXVn+ANO0rgOxyjwDn1K9QHXO20SED98uXnXz69RPDzy5ffXtzEruFXL2+6jKrsHgvTb+uOIqCAxM4COLIYICIZvC5ABZVI4Vce8CfPq481SPxPk//8z0tvV0H905ev2eT5+voy/pHabNKE0JbcrhvgTVy7sJ0oiZrhdUImvT3UEKCmrbIRqhoCmgWvj5nfJUFQ/jne+/hY5DUAzcevLzlUwR7h/vry02j515eqHT+/jlKKjz+9JnkPqo8/fZdTt04M3GYUBrV+/fa8foqFA78Pjfz7qv+EUh+OdcDXlz8YN74eeo92wpkvr3EeZR8fgosq70BmZy74+NO/EuuGwL0kUd38W3J/fggOge1Bm56K//TpDvIvE+Rp0LvMf71sAd36dyyBw9+W+zR5AvWvZN/x/y+ix4Cq3xH/S3F/NQH55+Tnf2nbfzfh08T/+rIDCYztasy6L5PfvsknavvzB+/7lx9++R2K/j+KkfO2cu8SvqV2Fvmgbr59+/lDff/6wy8/f2gLGGswW761VfJXMv8K1/s6PyD4HPXxx7lwfTW7ZHmfTd4jffJbXvyP6vfXiWYnkff9+/rL5I/5Mr6QyWjE26IPCP6QMzXU9Q84/vTyO+SIDFrTuvfbMMv/4z8mfORWeZ37zUR287aZQAc3UQpG5ZUwqifw75jbFSSQqo5GjnuMg/E/enjUGBLbr//TvVPnZ/dJnVP7yT7fXEg/357E9+2d+L6NxPfr60SBsvMqCqLMTiYSeTp9zewAZM24blGBGlQdZBRnaMBnyEWfxw8jM/7674j/dpf0Wgy/3sk9erCUtD2MDFW3CXgdrdRDkD1tcmE9AFfgtnCRJHehRn4E6fUTtL7OE8jqzYhIfYmSZOJFFTQ/r4a7bIjal1HYr7/+6kDS/po9KBWfPApGPYUD3tWZfP4MTfOTKAibrxlww3zy4bffP0z+1+S/m3UXPq5xgvT+9AnU8F5jYI61KRwG3QUdDAnk7pPffn8CDMVksMJBD0Z+BB6TIUoX4L2hLe/JzxixmDgAogwRTou8au5VqHmdHPzJu75w0fHWyORhXjewohUg80DmDlCqDc15RzKDJa+GgVj7w6dJW4P7qr86lX1XMYXJbje/TvjtCdaNPIH/jWreB8HJeRZB+N9j4fE9FFJ9qCebNxGvE2GMyklhV3YRVvZzDd9++AXWi7fpULg9yUD/NRuLJBihuqfIAx44CCLjPl36efQ5rPwp5AOvflv7PsYeq5tyr3LV16x+hr9dja5wYTmAiwZt5I1F4R/PkIKVv028O35Q01HS0wve0yv3GNz9dV8gP/qCH5uKry02Q+eT/8/dx6g1yTASxZAKtZtQgiKZDzTHnmlE/dFmwSbgLvmeOd8bgzdaeWPXr1kSwdCohn88Rt598BzzYKy2gpBJpHSXDwMAojnKvcfnGG9VNUa2/TV7o/FPEJk7Z0EXwWSGwT7G2NuC4903TUNo6Hj9vaTf/QkhhBEAY3BStE4C48MHwHNs9wK1qsYce3oCBisY4e3DyA1/sGoCpcOYgPInUIkIZg2k+jt0Qg7NhDBDV6Tfh0djo1Q8HOtNYFMKXic6TJMxVGqYm7DbGcdAFD7cRU1SADGGKr4jXId28VBm7GOfCtqjL/IURu8fPfC8+T2w77qM6kOpkF4biGU/kq0Hrg/Pvuv59BVUNh1T8T7pR3c/bZ38sd7842t21/Gd32GGJ/e4/Q4OjMgqre+UOhJUDUkmBc8AgpFwr8qvj8L6qNzvunz5U/P+8e/19/dSqf7ouS+TsGmK+st0+ihvb9XtFdLDFMZIVID6vdJ9HkvR52eSfX5Pss/NPb7/IPsB1ZfJ39PvBxHPwP4yQV9nr7Px1jFywRi5zxeEY/t5Y36ej3e/ZhL47udnMIwEmwywtL5Xm7chsOQEFQjGwY/qU49Fq4d18k630BNfs/dYeGYKZPMsGEtlnf8hg+9lF3r24bj3qgBvQWwGSLhQXgDGrUwyql+Dly9ZmySfXjI7Bf/eFmYkfxiwEI9x7wOTB7Y/TQTuV++t0Hjx4+btnlaQD7z8y5hdnyZj2/pp8t6Bfpq87QnuG62shZuin8fud1wSDoVv72Pfd4YOeIH7sGYoRt0fG52x6Xo2w39WYkwqqDFk8XrU5S1LxxX/JAR+CAJQ/VmIeP9gJ0+qgGw+lueoeUvwGurpwWYHkng3Jh7MJUiRLZzw52XgOhUoW1gHvdHc7/h9Nyt/2PL7HYbmsVv87eWNMp4+eHaGcDjMzc/1WAmnMFLhgvD6EVPw3v9Vz/iUAYkO9itQCL5GF7MZ4aL2DPVcFEddx5nhjg+peo0TACOA53tLF/hr14cjcMdeEQvUnwFA4MuF50J5j+j8Npb8aNQLs2135S7Rubde2gsX4DMHdwGKod4SBzNijfurFZhDiN6nXiBLPo19GDci+d6+jqA8bf7txVnM4cj9vD6Qj9d2utbsBbZ0pNBBqgUwLWN6cCK1lGVkqQr2sc0Xys1mWXLdLiVAcUuWdGVNUPYHa4c1lL3p8rPvHpDBILJjdWW94tDSec04EXqz6oUrWn7nMyA/kCFzW8noQCubpDS4cnZLg0TfOuuQuELf1Yio0oS+otuBSoZsubQ8H7MauTDUSBDFmj4aqSubTD0lrtMGrYpMAIujXqZ0OXinlY6li6u2VZUUjS6lezUU0awJI/e4WSxT/bVPAYUTyTWIz8Q+R3jjuCJE43r1sx0RF4tVd8vmB8zV7JqUI0mbX43EqzS3KG1E0u1FYvVBDYb5AOb2irsgzVYbDCpWDlayvLmnSlWSK5u5Gt/n6qJsw3Mh3mqERw6EsEUEnU7pJaPSva4Wg8TFO3eaqG1YkmXjRih7TByBZzXPNOwkFa8VCkriKp/KJSfo6LBPwZYNbqpC+rc1L2WNd2VDEaO3nACMA53Juw2INka93fGgEvXBKfB94LCEZV34IQi46bAYdGZA+yoL8H0YULMlI7uNpO+91OFQjjIOXTK9RYWGVsmFT9b4eb+5Th1SvsbmppmhdKwf8TT0NCrRPEZQl5h2bUBkLzVbPyfmrl8pi5lc7AxqZUmGvz/vSgT25Yy7xkCcZSSfUGeZ8NTO78CC0hnc2zinqhjEmEERKTFxvF71lK3XUkgjxEyX8iVL+7Zj6QyyjzYWYXjW5aAfsKs7Fa+qrohKcSYWeSJrtz1i9n4WtH69cexzzSKSyF63u2id7I6iioTkMF1nOGoNTbmozqv1pebPtdIMBI8yNhOxW3q2O7WrtOUiqs2OBZYqSiFwFrbIS0wj2lvciA3nUtC0+XQnIVQc7/uKmtGbRbfc0FtfcfCF6ef7zcxKYP/WrY6rrNavVpeqBKdr0oIoPco/quXVzFNpZbFiNGARo/Imehp6LmJJ1pUGq8q4nlJnXKmU+7PrljFKTweXmJNOLNOm5TYyxjVub642Z2auSgpB5/PAq71a2svH8yCVV9q9WuqJi9JNgVpxeOWP+1j0Vof4sJg21cICrTvb5dnhYNE3WTjP2S23j9nZ2ZqV8mou8wsLydTQtfCZhVzmK3J+salasNB5Nz3NxAGtG3q/zVB3espQWlsX1XHukleplPgDNotKuMIu3krdvjFtW7945LG4arObsMI3Z80HORGGRK5q89jjBK5XZ9b1fF4nSrIJqCDpm920U9lZG+Py0eoj6oqup41uXOTouHK5Ikl3iFxojphcM8U+LTAiV+YXXaN5k5RFVsiAyGbolmuWah2aBOVf0MzYyeBIngOeWp8VJCRWO40mtrdUj0xMOR/wtSSWPUdcQrHPtBkSaVt2VxbImblEWh1FoeFM9VaXFnZyECIgUo5MHpX2pnXLo2AhfZ/J7PEStQc2WzmpQTU1cSYFGU/qoPD44rIKTwes1ftcOKYicfWSo+w0KTvzB+9sl4UXzNcocbrMGMqRMitBU+FEbQxx1q46m/Vou7MFbB+IKCDB1F9jp94XV/pevhI4T8n8cIlDwdGlcOGs54OyO6YqchvkPNrtrkDZ1tZKUDZaHO36Wxn7s41GD27NIYhJhxRxMiO1EJbH6wJIlH1t5aops1oltAy7pdEOGk+dlgEvqkzps51GXk/kvDeN5DLvt1TBbZjiFEoopAEnSpdEtHXVw3YhlJuWvUg5r0iaE0REBRjo4lC4XA0dWDlLRjctC8+n/f4M2gMnizHgZwFzS1zmis2yU33kCRi+4u1WEWtgHBdIN6jSgTU5Gb2iLd5dZvnAdYRI6OXtgNEnU2BCCycQ5MgzsYCie6Heb83yfJwisr+dI9NZtULMbm/crtb1snbzY0ifTXFltfpyyM8UTxZYwciMUK+JItA2hda3lsZmwTEmjiWR7knD2KA9VQGnFrygkmILldSFIJ9EsSVZlmMSO1jRinnaqrwQRyeKRrRtoS0URtuSfjebFcLJ6TsxFItE6G8O4ii3YBp2B6XF1pc14gS9U6rzKOsthpyGZnMTS8emZWvAhFizjNOmVFRhmZzy3jqQ9c7rCo5IEu+4dNwzi5cubmqbMxbCvauLXMHa83VBWG6TpRc7UXSrFcelOBortiGf2ElQnJa7XZU6NelRMn3sHd9EmHNzYLz6IKt9E8s3nD8Kx668rg77dZQGfF8EZW1xJ3ytzLQNQu0yTDlZdlrZ5jGvh9vUkXHuqO6ZDb+LORRijCfHyDNISat454xTtx7dyLLlTlVlfSnOHMVJXc8ctnw/YIO2GGLBI+rMGahTzUG5Z8aONaDpmVoxFnvrb14xJy8Hjl2sCzfB05sWJg1E64rxG5bvdKDv947n2lttpVRmsojOAzNtbzAE1TboCGIxI7ZzS8Q4N+W78yIEslWWSajvplLjVWZFuYBg8itD3WrUJhetmBvefMuKzrlQNWRugr0nKhcjMiKOjaoVifBzGqyWl23LLnRWy8+H1QWWoVnvEGRBq7UuSQeeM3Ox4SPd3ezKKSdtVrWAHTss5uS9QB5AZizbnXK+zO2uO87cgFEWKinhGwJymiheiEpNZoakWuuTkeXIcuUby7giz3xpazMuEjqFXtYMVe+lxbzOMg8Wz/RYoKhb4irRWbV9vHh64R0db2HOLJCeqO0+NhdTEwQSdTn36oG5KX3RGLByB9Y1XNXaOdXzc8nkSLy6gQvbKOvYyI8qMOPhpHRJ2dILOhZOF8vupUjlxJLgN9K1W6LRWS3wvDJ4G8X7gk8rnSOasqgOyIZAyF7aIjY+b87uOmdhsU8pwgqcIF1IfOwyaXaog+sJFVA7OLuH3sU2Fic5iQybh8ssW52XBKdAhquusu6FNEFOE0JBbpuKUbau5iwDjN4EqrjgEU816uLIMfM4mYu4QB9u5z4yId2asnsk5VayDdGMz15cXjGFYW/nmbSazdsm2l8CZTqzTD/QkFNE7eIaLTIlsw7qFqaQjFkpV0oHU9bK1i0IK5puGANLktPifMuNeejvmu0yFzA6g5wcB1iwTvgA4+0rGptRvTk2DJLGYrCYJpcLLeGnnMM0BTrsdHF4pSVUQZwtZzg+3OiZRzq3Y1RGdqxKtRwzB6tjbDJwWbNTxdKIAjXMY8mhimKrpmm6FLGaBGSgrfAUF2V6NeTX2TpAkSouCF3k2PNMU2nM36bJRk/IIwvXolakZma6jtl6kotSfqzpMu8xjztLxJlLtR240IdOXRTlsECtOb/0WZ5DGBK3XGeuMMekPASnBobSTTsGA40ehhC/ZNauBOxJT2954KcO6q/kbrMVJI+PbctmCKrlZ0Q251tP3KkybHW4k1zovKZa2VlwaisYKp2wXTo+bcVTCyRi0+Zbppq6g1b6ZSbCPZDEqQxtT2/GqSy2Xoq2hlUyldMevDQphDXJ602bukVW7/BkBqy0oAWc2x4vzpo2Ff7GTi87aiU5zE0agCAbZuaeic2VIZf5Xgpgq0bCct/zYlhrHOMcrkXGaUQhtkQjVAe74q8FiarujoPNc1CJsYesmmB7seYqW1O7paN3m96W5FCRGOsw3++kTeHgIe9wp/2pJHeO3aaQrSjcu51m+FEg23RO2HxblAS9ofYB0aTXU5qzmXy7bCJmut/c1E5gvQsY4Ha3hxyPTOf+uRSlqa8RXgNQ3zacA97LxnruUrjeudFySa7aMGqWDSbuQgu7zpVyF/aHojRag3Fn80TFFjyqMINLX7zecWNzKJY0Dkmu4811wwhaqyx7tD5EhCzY7jwLd/TVXzktO+93azP1KQ04N5haGaY1g0KSDGxxb115IuNlSxxtuSLjhe/pYQz3qQC71k7Dyiu00fVTmCv8kkOmdsD11ykg+yWvE7GDIvVmIe63p+nS8/wVKXKJziReNkUOxnyhA2y1zGIMPWML1sNZp+Q6bUauBOq8D6z26Ef6GeiUnay2mIaYipi7F2a/u9nEUgvJa4/llLZPjwtSPYNL1u7mO/LiX819uEQTN02MW+a5u2PUDGu4AQnME8C3cIcz0GcEIzLR9Ihzz10wFgtZydpka5pz5qh/CgdSAEdxvdoU+9Ux7OqWXE4P5smPdjndJQ2K0gaHs51nMXALhYmBlHbaGq1cR9/Ecq8fEGHjCeKtiGJzjR1Vfzkse32KdlOMEamO21aLXjA35fGwT52FYZDzhsU8/EYppub7Nt7ykm9QGGwsrVaoCMSgq2TfnMTVlsWmqmguPExBTjhQb85GOAfs1ER9IegVIk5WLVlrrTsc56eD5FmU2Uknt/MRai6RncPz/vFiuGEbaTzRGscI22AXWOmE7Bb2uU6ax8VWOIG5y2zd63E51CyYL28R0S+jxBwQUnDP82zRxnukYeB2Yrrlj2e/JJfULNl5TujVQ8Af10GsbIzgMgjleiuZokcH/Hll5PhslhtrjEl4Rej6QaSW5Y4XpxKMTWflzRJ9uXOuwoVY2LKZSZeabrDAERbtUtj6/IWer42UAkh6xUjcUL1V2ixRdD4Q1wPM8nZD8O7OXzO72mWYLu/JVSbkIj0g24uvet0yuqWx69tIT+V0P+h7RxFcRwxmwxTXdEKYrZfe2kZzkwtvKmYEi+PBWPB4kMU7nNzI7sxz9QWLogBjKVLUYuQoyohKxcRp069ZgsIUQ5PxUpjb0QwHlL4yd2enWYtzQC6HadEhiC/UMIHy3jcQzSecDemvu6ydlfuUdLAjD9bB7aDpU6TuiQ7umxtXwH3OoocbdmzbwoY9sh9MkWFYpyElEPiKbqwIXW/N05XZJ/v0wOY9LSaSUTtEtZBrBZReyMS53mFiiUAlOixc0MWBDdSCm7d+VxXKhaZKxOlOvuXZGyIT8KHKtHRm24pASGsU0AuKyyzifPB2+m1Bbkox2TBM6uTBzbtFM1YTETwrhgVoGgFvinY4+fFKi850sMqn9dXDk3JjWD2y33YtZ6YdNQV+a5L6jtT6hqGLelfj8yEfAr901FgI+GWdqBcGTwDWqRkuV6XRgH499LwLm/qVjaxuOrLrjOywNTbmSa52fkzkp9pN0wUeXbe4eAwHNCf2Xk3IprvjqWu3yllYRA6WA0qE5tlzp3ZZnc58e5mRq1uRBKc96VVsb3MoTZxN2cnZg77Nqv62MXDpkKpAcomKiGtjA5B1sbuI/sxFRelm47uLPyXNdEDWMsmdSfLl08t4EP08Tv5bD43H073/Z4eMj/PAt8dL96NkYHtf7mt9+Xtq/fLppXIjqNTjQLVO2uB59PhfjlM//zsPJkYJw+N57Pg07Nq8ncA3djD+ruglyry2bqrhW50n7f1Q99OL09bjLxzqb8/D65e7cWkxnoT/YMwoHVRd5EIj8m/PX2e8jD9DGJ/zAC+yG/C8DJ4nzZ9evAG6K3Lrb/iC+AaqYrT4+bxjPJwdH3i8/P6/AWZIsRXHJQAA -->
