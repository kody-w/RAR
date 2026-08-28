---
name: "rar-cowork-cookbook-adaptive-card-report-on-compliance"
description: "Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_on_compliance", "rar_sha256": "5b0b5f4666f684c0daaa78bd7558b295a3263fa7b739c49ed211769811f3372f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_report_on_compliance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_report_on_compliance_agent.py` and in the RCI capsule.

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

Report on compliance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 5b0b5f4666f684c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_on_compliance_agent.py` first:

```bash
python3 adaptive_card_report_on_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_report_on_compliance_agent.py   # or on stdin
python3 adaptive_card_report_on_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on compliance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_report_on_compliance',
    "version": '2.0.0',
    "display_name": 'Report on compliance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of report on compliance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-report-on-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74a15870069b7c8b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/report-on-compliance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-report-on-compliance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardReportOnCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReportOnCompliance'
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
    print(AdaptiveCardReportOnCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abPiRpPuX2HOfGh76D7a0NZvOOKiBSQBAqEV3I62dgmtaBce//cpAee0e+x33vGNG3Hp5SCpKivzycwns0rntxe7baKievn8ovp2PlvbaRpHfjWzc2/GFn1RJeBHkTjg38wt8qaKnbYpqvrl44vn124Vl01c5GD6oSq81vXrmT2r/La2ndSfLT0bPO78GWtX3kxS9/Kszu2yjopmVgRgXFlU4FsOJGdlGtu568/qxm7aehYU1czPHN/z4jycxfnMs+vIKYCc+iN4YMcp+AnGaL6d1a9AG3+wgQy/fvn88y8fX2Lw/eXzby9uatfg1subJpMix/uy+5x9XxRMT+08BOPKEaCRg+vSr4AKGbjl+cHsefVD7afBx9l//EfS21VY//j5Sz57fr68TH+ObT5rIn/WFHbd+N7MtUvbidO4GV9ny7S3xxoY3bRVPsFUAzDz8PUx85ukopz9ND374bHIa+g3P3x5KYAK9gT1l5cfJ7u/vFTt9P11klL+8ONrWvR+9cOP3+TUrXPx3WYSBrR+/fq8fooFA78NjYP7qj8BqQ+nOv6Xlz8YN30eek92gpkvr5cizn94CC6rovPzCccffvxnYt3Id5M0rpv/ldyfH4Ij3/aATU/Ff/x4B/mX2fxp0LvMf75sCdz6dywBw9+W+zh7AvXPZN/x/2+i0zgHGfCG+F+K+6sJ859mP/9T2/6nCR9nwZcXzk9BZFdTxn2e/fZVPfDszx+8bzc//PI7EP0vxahFW7l3CV8zO48Dv26+fv35Q32//eGXnz+0JYg1kG5f2yr9K5l/het9ne8QfI764fu5YH09T/Kiz2fvkT77rSj/rfr9dWbYaex9u19/nv0xX6bPfDYZ8bboA4I/5EwNdP0Djj++/A4YIgfWtO79Mcjyf//32S52q6IugmamukXbzICDmzjzJ+W1KK5n4O+U25UPcK3jid8e40D8Tx6eNAak9uv/ce+0+cl90iZkP7nnqwvI5+uD9L4W+ddvpPfr60wDkosqDuPcTmfH5eHwJbdDP2+mVcvKr/2qA3zijI3/CTDRp+nLxIq//mvhX+9yXsvx1zupxw+GOrLixE51m/qvk4Vm5OdPe1xQB/zBd1uwRFq4QJ8gBsT6EVheFylg82ZCo07iNJ15cQVML6rxLhsg9nkS9uuvvzqArr/kDzrFZo9CUUNgwLs6s0+fgGFBGodR8yX33aiYffjt9w+z/5z9T7Puwqc1DoDYn/4AGt5rC8ivNgPDgKuAcwF53P3x2+9PeIGYHFQ24L04iP3HZBCfie+9Ya0Ky08oTswcH2AM8M0mNO/1p3mdicHsXd9n6ZpYPCrqZub5pZ97fu6OQKoNzHlHMgelrgZBWAfjx1lb+/dVf3Uq+65iBhLdbn6d7dgDqBlFCv6b1LwPApOLPAbwv0fC4z4QUn2oZ8ybiNeZPEXkrLQru4wq+7lGYD/8AmrF23Qg3J7lfv8ln8qjP0F1T48HPGAQQMZ9uvTT5POpLgMu8Oq3te9j7KmyafcKV33J62fo29XkCheUArBo2MbeFHv/eIYUqPht6t3xA5pOkp5e8J5eucfg8a/6AfXRD3zfSnxpURhZzP6/9hyTxsv1+sivlxrPzXhZO54eSE590oT4o7UCxf8u+Z413xqCNzp5Y9UveRqDsKjGfzxG3vF/jnkwVVsBuI7L410+cD5AcpJ7j80p1qpqimr7S/5G3x8BLneuAtaCRAaBPsXX24LT0zdNI2DodP2tlN99CQAE3gfxNytbJwWxEfi+59huArSqpvx6+gEEqj+B20exG31n1QxIB/EA5E+QxyBjAMXfoZMLYCaAOaiK7NvweGqQyodbvRloRP3XmQlSZAqTGuQl6HKmMQCFD3dRs8wHGAMV3xGuI7t8KDP1rk8F7ckXRQYi948eeD78FtR3XSb1gVRArA3Asp9o1vOHh2ff9Xz6CiibTWl4n/S9u5+2zv5YZ/7xJb/r+M7sILvTe9R+A2cGsiqr73Q6kVMNCCbznwEEIuFejV8fBfVRsd91+fynhv2Hv9fT30uk/r3nPs+ipinrzxD0KGtvVe0VpA8EYiQu/fq9wn2aitCnR4p9KvJP31LsO8kPoD7P/p5234l4hvXnGfIKv8LTo23s+lPcPj8ADPYTc/q0mJ5O1PLNy89QmKg1HUFJfa8zb0NAsQkrP5wGP+pOPZWrHlTIO9ECP3zJ3yPhmSeAx/NwKpJ18Yf8vRdc4NeH297rAXiUN2Btb2rRQn/avqST+rX/8jlv0/TjS25n/v9m2zKRPghWgMa02wGJA1qeJvbvV+/tz3Tx/WbtnlKAC7zi85RZH2dTq/px9t51fpy97QPuW6u8BRuhn6eOd1oSDAU/3se+7wQd/wXsvJqxnDR/bG6mRuvZAP9ZiSmhgMaAv+tJl7cMnVb8kxDwJQz96s9C9vcvdvqkCcDkU1mOm7fkroGeHmhyAIF3U9KBPAL02IIJf14GrFP51xbUP28y9xt+38wqHrb8foeheewQf3t5o4unD57dIBgO8vJTPVVACMQpWBBcPyIKPPu/6BOfEgDFgS4FiMAd2MGDBUEQAUEtXNizbZukHI/EccpBadzGUAILbNIhMdpd0L6HIghJ0BSCBBhGogGQ94jMaY0snrRCbdulXBJZeDRpE66PwQ7m+giKeCTmwziNBRTlLwBA71MTwI9PUx+mTTi+t6wTJE+Lf3txiAUYKSxqcfn4sBBt2AS2dYbImt+I4FRcqEJSlaRdZN4u1fM43pBkrVq1N2S7sBAshdm68U5h0R0z2sN6h2XiYb32S5nCWzJUyrWe5/oiF2IzrtfBgSzJrUcStxOz5Avav+7WeqqxC7UeF+M2kPn41GyMSjdKIqk3OdoMUlLrkLDVbvOtQRgSAR/Pom6WdtxdtCWaQDk5UIXZt+qtHhOuWeYSuaqYNjzpZWRUwiZBkC5SiBWRwVc6Wl5wJFT2xa4bhduxzhBO9y8w4R0snIIOFnKDCngRQEJGB37kb2UVlhprc53z1aY1NpaJnBzMUNP2OPLb9f4q5/NNy7or7HQtVEK3nYsOitkWx0Kl3SVWqLCesTVKvVoR9MGqVuTVkszaSIHs1ZlxjfRa13Kxtfa0vrXtnnWsa6XYEoXs3MI6p2ZmFfQqy8faTbpFq+b7xq3OwvUocgsqoQR/hQumS/BKm8JpmBl0qMnchcTHs3WWVSfVcdOcu0d4NbQq55/NNFh45wN3ZqndLQwu2+R6I4vjoHeX1V7bGRvEvOrCiCWlXhD0uDHXVhZlxx7i+IrP6hVK2BekYlBJaTEekX3KOyWoN6/PtkUYV/9YnrYDxQ1IRjCegiO7s2oIMskQ+bXEbuWhgarhVvMJr/ikW7eIH8DbndcSLOqjlkgTjiVtDDRozkMs2KZ+1K/p4Owumjlu5rUpZQjV8ewNbwmNUWupVlYB2mO7SM6jgibO9WBcDhDfn0y1teKNpGn1MFwFsdV6vXZ7FU0ORbALUJKwY8MwVtYZ9SStH3bagcX54rgIRUuNSElAUO24GghPSWFaS+CROM+Lq3cxnRiZo01FrQWK7ylWhLjTYqCug7wS/Qrqj0wOE3Mox4i1cmIEHOm6QEfW2CJaiOigEtfNeFwgoiQFWz1GpP1atFCHO4mSOFx4S4KuBxO6LYKktHZpX5xOPNxpfrLAeTLfWiF+63lklch4ZBuauWncvqiZxRoGKKHsseQXvONe9skxTAY93uCxVEjH1c63GmEv8L2ryji2aXZcNR/zNEOrOPN0jyeL2N2PG+2Iw+SQEit5PJa+HmeORORoZJ8xXpP5iJL7Dczi6q1KAzoQnfycLGoSrYkuJocsiE1rVe26oWe59WXdx/ZNsi+g8WW3a9dEmY4+rxV2dBFZvAWr3lpZmO0WKVnLNt7UF/jKbY4b7ULYPJenB/iKOCiUDhcAu+LMeSWXu0orKOpiHJ1L69HessvSjebBXUO4Xud1Ngj8FWLYtYKBcoQp1844XT3SbFMF1bsEya2t71eSstxSlKKaEU6trJWICLWjEK6aqL7MQ3prIYMq6hC0MSS+QOrrgVjRImsboilpNmb5BiXmmGSf7IRyKxNe6piTmvO6btKKYz0x2asbIswu5GHfyuezmqy1RX40CGYvuQPreIs8Da+C7N4GSKfPV7iA8bl+0WAhVqy97LXqWWIua/hIiu1u2FAMIpDJUJFHzq7Sm9b1N5b0oKtgQMhCkOeksqRXQndUIlEflcypSFkOqZIcrstcsMx5stnJ/ZZMO4wPOZU2Ty5IU6wUzePucs6CC+EvVqv9BtYSbOseBAiVMtVH5OMVdMULs7LPor9Zbno74uZntSr5FILt1BYL6IqvjWW/c5NQVHXvyhcmUnlpJwhKU9pLrVCv3fWY7RMmpm7DyV6OeOrtJbVnVtGQ2/5ZrEOVNPKoy4VDoNfF1ZTRrDd3Ww3dCGekaQO9uCUDdVy79LxzzmiQbWNMVtUjgayzwIM4uyk3e5WEhxa51DZdKIYQXItEoaGGZ/sWxy9Nv2ZBzg9naMvgCEUdLvic3gcLN5BW5PKw0vrSxvbmmRyLPesvNZKPpYsMU8k5NSJJImqPkXLDdCizt/TLXlKamheWxWXUeiroosIvxoAZ1WHaVjiJkhObpEnE2B6O9SkPN+uy1ziuhaX55qBmu+v+ajCwyM2b21Zh5lZ6SLNqM4etqGd6ZU/qDrcZSNuKYfkW5OR6s7naccm0u8gRezIzS81lJBDdlUzwkrm5eQhGLOZMbIe33WZJJ2W+PmO9V96WHnqi8UaMh4o53pZBUISCubbdgZpbjclJ1bk8cKthvVHFYmNYfFpAWEDiJhk7kRDZJ7mr4Xm53u23Du5K6aCJsMcNHXz1m0BX1sWxl+CrK6kI5gW0wWx5jhzUg7xOK/skFc1qgBwf2VxcXjzulrqxWy2GorH4wmVQYrRb5ypaeMuuihE369IuswwRl7Hfy3seWvbmxltIF+mMU/mGgHftWlILJfND8+gZuVlcLlFFuKPS8iGj7w5rOptTiIOcsmLUk10Ubn0eceeLxPNIJK/Wx5XAzk3JCe3WI4JMiZywwxzb3Nk62BoF4qolXQsmqiTTnX3BrG4K2RhN4l/2mBnCYSOeb6h5ovWRHuCMty4yDUmFn3sbLbGu1nUjqjdqxe8W5p5aJKAYEpZkFEekVVxYR0+NHhvXwhTFWGGJQ8YYXsJyyVbOSU0MmosEXyiV1RPWknCQyAQq+euEuEmCOLhUqvBU7xteeKuKPY5IjgGH6Fm7wYIH7THssu2Tk+ltCGPFYuWtQx1VZU9ETeadYi+EmLsatJdZyq3T0ngLn1uNMDFSJ4StvIxE2FmOBg43fcaKTOmEW4lZU5TcINaGMBkolpUkE+3rWiTiGAnyM62sL6YuhU2wNOQ9rpPFSGKHpX9a6BGnXw2PGTwb7JWEQAtL7Xo05x5MxgaLG8cRIXBjL2/mvUYtwzM335BJo5wNEU4Wgrb22Gzp2/i87wtdO54Z7nCRkTEs99ZpHrNMXwgGwItWSHyjbR2zgm0X2mgqA23jCx1pu11M70yHOKb7cCRyYw21sYrql5Qbj71udZcNr4GONWej+Dxq0YnkjgvK16GVtrZMy+PGER2T8lZmtryHu1W8a0HRbLQw17aUsJcwzd0cOy1HFJ1JjgmoEpZU2ddufZaNmL5lWuaMgiOgbTZ3aJeHjGHdcm4EAgHjilWKVQUaztcLdM6ju+6E6Pi5wMnYREHt1VXdEE4QaJCyvCX6TM3DNBgL1acy+roDUXUUlW4zit02PQ0bUY9MUNLGFE5YqcXGlcHLx62cirp7SxrRvXi5s2f2vXadb27B1VvNx9PQ0pxOmZCFEmflwoUw0pgalyGSlS41Uaf1Nb08FrmpIDKZwJjNQpEo7/ogV+Ek0VkcUfCGzfKroaPRyclb7oARDtvFoTyY2ZwfYtxWd9ztSJknTALbElO/ZYLPntO9lGR0dZFjtbqhLpalzG5NaJSLriDQLG+vtU1ulagnXDNLeHapQ6ndntgCbXrvxGvbPN6D+B8uhzHj54EDM6BH7609ljvSvttVmhmJqdYbLrM5p3qx7S7z8owVBN4Q0eBYfOgzkYGw5Tz3w4NvxVJ6hmvULcJOxZOSPUN9vrcPEasSKLE/DraN61ixBEv0gsP0pw0k9UxzrdcSjbODcjvvDzucb7YljclSKnDIMZGLPXEBdWG+d4Uz7KaddlqWjL9ib0wcOEdAs5y6gbdxcVsdmJO6kYUgk9b61T4jKms5SE0w7SBj3pbmRMjG8lAxvH1wgnfhFYRnXaEliyyqUtECTm3mNpdF1nBuKjemx7LvoOuepCHfP6jzaz6ShrN3ruTZpM0j6QuMh1TQvqV7P1/SudOgGqc66FA4t/WyNuBm1VpmCy8QBSZ8R6nFPTfaC94SQZvjjc0tg4UxO1hgm7JNaOq8i3jtek6PHD8XF/sttDWOh+PyoAvb4lrRPsQ1V2fdUsVSlFsG4kmUTCwqdxHPMMIjDbo1pQT7r8o5oTJU4s7YGWm1sPmbfzt0bcHWoA706zW+ak8tTZpLWhCSOVR3h8OcFxi247R9B0ErjKKFre3T6I3c1A7NX9GUbnjrOl96WSxwodjF6CKFhZxx9C7M4m4ebRcRqzg7aFVmss+zueCEqegqhwW3UTCp45lxje+geCEwVZYSi8zZeatevgLuBYF0YPoR7c04O/dXobUEQKkuPCybwxpbRs05EijGtBZpk/e4wl5xzJUhGILW4c2yFE2Wdk4zP8JsTgQerQUJiYDNFprsUp+NpfnFpJE82PpMOC6dG+oxriScRzEtAtK47pHGw6uAwKBcENi1waR0KNTLQU805ASxC9DvVfsxCHZHOUZIR6eHWGz7rRPf1gNNOjCF3cxrgjbu4mDKPtiUJ02Xu3ZDxZnOst3yJmO1eduZ+SIXj6yw3vJkiolzJS5Rce7XEGzAaMAuDfK8ioMu7FbbgC8rxDsctnvOy5aUu0g4oa92XrhqFonQ9VwoddB5TPNL4Fo248IQY4ZqF6/phaG6ELILBG6Yr09+ONcZVJS9gxuE0A7Xed7HtfMy6tXjHqXZ42lPX5ZBFFZdh9OKZukOH4ldMGSulCtcr85Ha3lwKBpNM7FzBrnGCds8Jf0tozBcaVr67NXRIVNZqskzPoDgAesxC3bOslMF2SXo+OjI5QuhCBd7iN5Zp8VOdhQQpAdnedJW1OpM4yAjxiGrXJ9A+1W9jaLdfh7ZC+zMVkjnY7mUZy2ZOU274fg97Y/XdUG1jbKmBHpxxJcwx9hQdV1WKE4mxI7dMBQnUPD+QhfpsfcvF0LZbNvMT06drI1HL+5cMVooaIOQm2igznSFriH6vAfuX7a577vwNtDWIgd5lDcve5ApdObz2C4fvSZAjfV2QRfOGdEsj4K21Qozj/SoYPummXMQtN2u/ZWCwe3i4gfq6rbmL9IKi9hMZC49YuQGdgrwam21FztyB7Oqsm2328y3C7UbWpspJEnxq2oR+wHJHHl5Xcm5688J6gZ65HNbcf4WV227goiiQxs9W28sBlIWzX7H2dySUCMmw4vTwl3Q3P62NRC5XVucgzTlnG7kQYIX0MpOmNM6cTBlTt4QNq8XARdZudFoQax0HbZbOtxy5W61yHGW5Gq+u+5KgSwb6Xbi9qRsSEyDW03UamRjwVZjj/R4w1xpWFE8gqV0wgTQnOXny7FDfG6+AM21GMnbFBMoBD1lNN0pnhPUuG7tmZg9YYTBk1eYV5tWC9YCX2jX/LbV7CBwb6F9gkdKyEMZ7us1VQ8uuvMkmIO3Sy2l3LCCioS7HsSWgqHKWfVK0NpLkpNKyPF03D1H6B4KZZJVm2UQJ8vl8qefXj6+TAfQz2Pkv/GSeDrX+392vPg4CXx7pXQ/QvZt7/N9rc9/R6lfPr6A4gRUehyj1mkbPo8c/9sh6qd//Spimj8+3r1Ob7+G5u3MvbHD6beHXuLca+umGr/WRdreD3I/vjhtPf0mQ/31eWD9cjcsK6fT7+8MuV9ncR5Pb0e/NsXXxynytGqcT692fC/+dhk+D5g/vngj8FXs1l8xAv/qV+Vk8vMlx3QqO73lePn9vwDvcvXNriUAAA== -->
