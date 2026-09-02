---
name: "rar-cowork-cookbook-adaptive-card-develop-support-transition-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_support_transition_strategy", "rar_sha256": "f966005e8bf01fcfe0faf77c5e005b612e4453b6ba47b89ff766179401a39ee8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_support_transition_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-support-transition-strategy:c4bc4b92590a78be5ee0388efd8b535a66e4425ddec92f5cdbc4318c3c413348", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_support_transition_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_support_transition_strategy_agent.py` is
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

Develop support transition strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 f966005e8bf01fcf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_support_transition_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_support_transition_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_support_transition_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_support_transition_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop support transition strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_support_transition_strategy',
    "version": '2.0.0',
    "display_name": 'Develop support transition strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-develop-support-transition-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '328ad66101ba6cdc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/develop-support-transition-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-develop-support-transition-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDevelopSupportTransitionStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSupportTransitionStrategy'
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
    print(AdaptiveCardDevelopSupportTransitionStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81665eiyLbnv8Lk/dDdl6xS3lJnnbUGEUQRUEERus7K5hE85CkPBXr6f59Azayu26fvnJ4zH8aqTIGI2LGfv703kb++OG0TFdXLlxcdODmydNI0jkCFOLmP8MWtqBL4VSQu/EG8Im+q2G2boqpfXl98UHtVXDZxkcPl26rwWw/UiINUoK0dNwUI5ztw+AoQ3ql8ZK1rKlLnTllHRYMUAeKDK0iLEqnbsiyqBmkqJ6/jkR5Sw+sGhD28cJq2RoKiQkDmAt+P8xCJc8R36sgtINn6FQ44cQq/4RwDOFn9GTIHOicrU1C/fPn5H68vMbx++fLri5c6NXz08s7YyNfiwYX+YML44EF/sgCJpU4ewlVlD1WVw/sSVJChDD7yQYA8736sQRq8Iv/5n8nNqcL6py9fc+T5+foy/tu3OdJEAGkKp26Aj3hO6bhxGjf9Z4RLb05fQ801bZWPOoQKgJJ+fqz8Rglq6+/j2I+PTT6HoPnx60sBWXBGnr++/DRq4etL1Y7Xn0cq5Y8/fU6LG6h+/Okbnbp1z8BrRmKQ689vz/snWTjx29Q4uO/6d0j1YXEXfH35nXDj58H3KCdc+fL5XMT5jw/CZVVcQe7kHvjxpz8j60XAS9K4bv4luj8/CEfA8aFMT8Z/er0r+R8I+hTog+afb1tCs/4VSeD09+1ekaei/oz2Xf//hXQa5zA83jX+T8n9swXo35Gf/1S2/27BKxJ8fVmAFPp5NYbjF+TXN30r8D//4H97+MM/foOk/49k9KKtvDuFt8zJ4wDUzdvbzz/U98c//OPnH9oS+hoMvre2Sv8ZzX+m1/s+32nwOevH79fC/Q95khe3HPnwdOTXovwf1W+fkaOTxv635/UX5PfxMn5QZBTifdOHCn4XMzXk9Xd6/OnlN4gXOZSm9e7DMMr/4z8QJfaqoi6CBtG9om0QaOAmzsDIvBHFNWI8g/oXXV5tNp8z/xcEPh3DHUKE06YNsqwgSiEwHkaLjxJABPzlf3p3jP3kPTF24jyR6c2D0PT2RMi3J0K+fUPIt3eE/OUzYkSQj6KKwzh3UmTPbbeIE4K8GTm4+0rdZp+uIxOQwfgBQnt+NQJQ3abgb8gvf3nXt/sGn8t+FPNrDu3mQGP6SAMyuMSp4rRHnBHH3L4BnyAYQ6ypijR1HS9Bxl9t+XnUnRmB/KlRD6Yf0AGvbQCSFh6UJIghgL9Cp6iLFCaRZtRzncRpivhxBZVYVP09T0FbfBmJ/fLLLy5MC1/zB1ATyCM/1RM44YNh5NOnsgJBGodR8zUHXlQgP/z62w/I/0L+u1V34uMeW5hA7gqEzp4+UhqM3DaD02pkdBsIS3fL/vrbwzIjdzlMqDDe4iAG98WQ2jc3GSV4mOvdVlDmkUVQPXf6Xm/ILYJ6QeIGagtiQP36NR9JFHBqdYtr8K7Ex+KH6t+N/9hntEn91CG0U1AV2X3u3UNHY3pF5X9GVgHyoSko7ugKo0Wjom6gU5cg90Hu9XCl03wzYQ5Tew3jqg76V6Stoagj5V9cSHpUTgbBy2l+QRR+C/NgkcJfo4Lu28PVRR6Phn967+MxJFL9AH1s/k7iM6JCB62Q0qmcMqqcGtznBc7DI2D+e18PiTtIDm7ImP/BaKN7xN89b/EvFB/6o/j4voz52uJTjET+f6p3Rnm45XIvLDlDWCCCauyth/ONJduoi0eVB0uNO+V7JH0rP96R6h3Dv+ZpDA1W9X97zAzu/vaY88DFtoLOtOf2d/pj5Fd3unEDvWZ0g6oaPd35mr8ni1eoJmizepQVBncyQkXxseE4+s5pBAUd778VDsjDIcdAga6OlK2bxh4SAODfo6KJqjHmnmaBLgRGXcMg8aLvpEIgdegekD4CmYihL8OEcledCmNnVPM9ED6mx2M5Vj6s7CMwuMBnxBx9HfprjbjQkrdxDtTCD3dSSAagjiGLHxquI6d8MDOW0U8GndEWRQat/XsLPAeh345ZCe73EZSQKkTnBuryBo0AY657WPaDz6etILPZGCD3Rd+b+ykr8vus9rcxMCGP3xIFrPzvTvxNORDNq6y+AxRM1UkNQz8DTweCnnDP/Z8f6ftRH3zw8uUPvcOPf629uCfkw/eW+4JETVPWXyaTR9J8z5mfvSKbQB+JS1B/5M9PYyb79Iy4T8+I+/Qt4j69R9x3Gz309gX5a8x+R+Lp5V8Q7PP083Qc2sQeGN34+YG64T/NrU/kOPo134NvRn96xoiBEJfd/iMVvU+B+SisQDhOfqSmesxoN5hE74h4Ty0fjvEMGwi4eTjm0br4XTiPMo1mfljxA7nhUD7mBH+sD0MwdlLpyH4NXr7kbZq+vuROBv56BzViNfRkqJuxDYNRBauvJgb3u49KbLz5vqm8xxsECr/4MoYdzIuwan5FPgrgV+S9Jbn3fHkLe7Kfx+J73BJOhV8fcz86Vhe8wJaw6ctRjkefNdZ8z1r8j0yM0QY5hlhfj7y8h++44x+IwIswBNUfiWj3Cyd9YgiE+TGbwiT+jPwa8unDYgyi+3WMSBhkEDtbuOCP28B9KnBpYf72R3G/6e+bWMVDlt/uamgezeqvL+9YMl4/iomHF8EF//cV4Kjj98z9Nu7kjPTuddpd5ffq9w2KG48Z+ndD4VhuvD289OULRCbw+jIqtophST/cW/eXB3tQrm91M6QAMeZTPVYcExhkkBKsA8pRpgTi4+82GB/H/n3+ePHlT4vtfxksvnikC/+zOMVOHWbmAgqAKTGbgcCfuRRBOTQNSBKnfB94LB5Qng+nE9jMIzwSIwhyBrkaLZ05T64m2GgjKM+HIf79juDlQRBmH5yiIcWApenplAIzN5higReAaeAEDONRAD51aQyHLFOES7sOybgzNggYmsYYlpxiDsECMPL8XoI+uHx7L/ffrfYAkTeIw1k8yoA7jjfzGIz0WcahPUBMXcIDGI75DAGmFEsEUGUkXP+x9Gm50bAPRYxODqtPWPtdx31+fXrC6Lg0CWdKZL3iHh9+wh4dGifdrjuhAw0sN2d3OoQyxt0vd0dfFMUUP3m6tnISlStO1qCRWm9lpoa2/snL6hXPbRM9UJLJjvHYxJWDVBeXobJ21rhd055mB9dgCczdnlcgSlaJk/E0tM1RzLpLq1NpeTxo/pY8rfJjWmKnq1xg2pSiDl5a3Q4UmbmbILhmx6uOHc3Y55UZJR/MGtj46kZ3k5xgsEhrgXi6tPJFP262+GriBr57KeW1oQ/6UbOqda6ZXoVromdc+J1DDlvO9XpSINDopi5KFA02Naudug6kg3+tMrLtpUTE6/mhOZyKbGZVfYtdLgfMd1eVb+s1uTtt15a99dRA1N3T3Na5VhQykpJPOO7jZLqJrSUpr5v9+mh7sW0Gkj21ZimTFOdjZEegO849MZVhx1LciC113BROuDJOVqNPh2RIj13kO6bDmOcDzeTLFcivRWqcVq1PrbKFu1eW5lZgJSAyUnYYrEMRTqk6OfqrlUCTlEdZ6zrYaGbvloQUumvKthOlD0N50tO9uezVW5WHxPJU+pdpQkj6ITLMpk/dGJMFZltjFRbZFFWJM3WmDp7UdVNrh9/OlhpNsag5Vqc0Uo9Smh41NQkYcx4wjVlSy2O4lW7bzVFOVGvXYSqY+YJaremcrAjMlrXAu9GH/XyRYDHGskxhWNURE2d9m5O44uadeDy7YBhWRu1gosmf5LNuLyxyMtMrDcPD8LSZ8LNL3Qi35UXJ7XZ71teDf9kohwN6aIuqk4aaFIcu3zBLMdriSqcJBy8PS4uKU2wFdqiHohVq16ejKeY1m8XHzGqlY1ScrWG/2tXRmupSvDP24o323QQbf9yTWtG5VrXkDMPtjs0upc/rdEyhXYfy0Sxai1dbXxVWM53g2jFB6+l2OrCRJ+0yMwWMtV4kYY9vkmC9lq1GHib9IZZZszye95QSkcYqEMViqVpmJzNRiJFgoa+wfAj4A8cfS6wuHW3H0thQbI1Z13HlYnk4siEdBZIs2jeH4xrpAIxBtSpLcGt/qgt87tz2jrL05vrhGl/SvU1axrxTmPyqqTftTDpoW1wC/0BS+Oo6VyhmamgaJlW5FzE2ekugtPqU9xMTQk3qVit04fYaQbZgEfTRxmRw9DrhPZqNz/ZKd5stj2mTa7uqzr55sm7z9cI28eRo28buoq3xm4d1lVWdDkKjbOeqQSy6KbafOgBM0H5x9vp0npRCapUH6yAf59le63lRx4OUiQ5LwnAvYofrcUGjYHJOdNsQgaZN9brkLg2ho0NZLlHCw9Y0r8hxpiz2nOXFqUjO5vpVblL5tEtmWU1TzrpzeYHLpYyXE2Mb0rPSX3odNsgdutfJywlNVi0pG16Eeumh0OOjfgmKtWbpnlzUen89VKXS0nZv5Ykpajjn9KRiA0wf3E7xtGmf67Kb8c5WJpN9flKSeh2lmleFpY+VmRAFK5zHpzdV5jmq89MNVFy2ngb6vnAWw7q7Lq7bkuXC6OoqldIq6zPNdQ0mEmd6P7TFsQqaJFbJivFUGaLJGt80wZwUgN8tVoZSrKiNieVFQGyBtl+wtn+iD8VM4lDtFNT2TTO7fRgPsxu1PF8EdJFQlj+Z3Tb8Wg9KodSdy6lCaZ6bLmb9wCkrs+yrbSNthRUmiquFxMdeoXjoGcjni3fch/11IxphMtfbeCkE5aaMuBu2qLfDUuh2u+LgHs7efrWAtU0cE/PseuDrLo55j4m1ZDbsrMUyq7Z8hmqainm7Qx0s464IG2JlqcO1BKfEtPsLmB5TiO8krZ2wIUiKeOfvDhJXKKjRl2t5GzOY2arnWmeTnS2dqowivYkDnfXkgS4I4pDf5pf+yJLo1SjJKdhaE3Kq75WTvKT2U5nvzSBDlViYs6uVL3t4NOxa4BwESy79Tebv7WZPbP2bQJD02d62XOwIZjpjl0bJqhIqpYoy2Njeo1Wa2/n17qQf11UpXfSc05IydPVmftyZRSqXeoGW580utcRLedFn83hGeZfzmTBg1WOoe/e8HKbMUun9peAZtnBEraKTks2mXWOGu2sNPZumzkSmSfXkbBo8hzkmnOP7yhSPQa/3Z4tFNWGIDq7nZMtK6BZzz3Um+iraWOaMcSbXOTbsWBkyzYe8dMj3x2VlbJdnchjqS1WvwZQX1twpsPeoXlvc4YgLBpOHtmL7XTNZANRdr6VdvjK5o1OzEpNdcDnEYr5hVqe6MY6qsFzhjRufdELeAEmea+eEx32vwFUl3rtzB6sUd5eLw42IDN320MOJSqjdVZD3191K4ZVbZ/YY3Z1Vn6pzt094Tj46+G5pnR1wNPNDtbTt6W3wS5JrLHntdEffIdrhGKXNzZZMXJmvlVyf41Lg0rXDH2c73cLoeKNvTu2gGN20Da8URU8pnrQ17AIy5XqbRUCnLpc0Mhd8V/oQoYREo5ZFtxSGGnNCBm8F9Lxb8hYR5T66I1GN9tLVVWCFgyudyI1s71ZbZhcu58as1iuL3ttzYr8pQ2K2NuW1VccUdyompGDi+5XGJbilSvMJrtBpMOzScp4XIjifmGxurEnGKXNrWteiIZuceVIZ/EYqOEZdDnWMnvub0U+3/mTLUDe/Wy3dRqbFOU+UXUqc9JYvWKAYQ8X61SBOL+j1uLn4RN0rYq9VBzStW1bbKYORxHNp1y6ChtodzjDUZGHhkKqxYK97l+/PC9SSU7nm+lSJOpHC2a1Bn9XlVdFzlT+n1awopB12VJcxrad6IhXrgz/vbB22ulLbhZRx2S9Rf8qcM52S9ouDmB5m+IHovFAyOOuWB2rVnyzJw4VpJxnyThGWbWKsiHlZ9puVYrCGbxaCxCuSGpp6EhRuKagXrSM66ZyWHnVtxUOUW3uw21LgMKlvTpfcctFESTW8OYsFfg7ySBRlp4/aFWUu2IHSd1N9la31aTrL45uwS1zssDQOLbuJ+mUlrRcW4SoHAmNjmebyHlvP9lGKzodkUtSietZzXzvG0S3pcR+2n1Y82Ti6uu7TYKuYxY5Ak6JC+6XPB5FqGJK62CRbPM1n1Ck/41yXKSi+dw7q+Ti1qThgtsf52u8GdFPKm/PS1bFpm8eDAla4l/nxxWZtorTzKmfkdk6Y+2VQU8uVoSfLqYmBA8qFO2cAK/+wFQX2XPIhDLmTsFcVzYyu1o7mpwPTNhJIN3aln+3JvMJ8yeAT7yBXhb7aw95nI8eiwJtx7Hjr2eKylhv1OB024r7UNSE8rtPaiYoUzt3KS2xzOR4uogtrIB6qMpsalkgrkTajCC5WT4aph+Zsn0Uxe6IiW6HOi2skDFJCGwCDSXzNbAmHINPlaknrMysTZoTKw76JIra7aEd7ZpII/OqAik5r9UXf7gBnGZsEV4eSPC+DRLG92TATs9vWPGlYXh2IY8tS5Y7XK4Xwlo6NnVZDTTRGtd0djQD6CN6tQ4vn2WZqNBrLAbbdLDSsyBpu54JuElILu4Ule2HnvOHgtLbvLg4lMLEEg/MmsRytzE8JyVGKOS9xlY92g62pCqU3askS6jp1F9g+UQvtcp50ZnuawZI+qAix5g9niYvUMA6gScl2octTpV0NW4m3dFndBCashwzSxnTOdU9TaoWTGdNMNdifzeRVFAGgCR09Lf3Tse85iC+de4t9deaqae4tBH/iLNAIODGTsZibGme3PYLtrewLSmLZU4VjJMZS/mw4OMbkugjtC8Ukp7MtYTflOHFbkrM2Gr5d+Dsrnx/XRxaFLUQuXEpin1+sYQhnebtY7ebKJeuPU53YmPzW3U1MF0apBbjDzJYvmnciIjm8TpoJh672lLDwo02wpmd4dmPodrLeectEvMJmXcpvJ/km01kjLFp9W/kxo+aFW6AqAZtJKES0DOtt7qc28L2lvSLKOQlpoXbDbGHEnhZJti2v1wnNSxh/XfAthk5UYuZv157mYx2DXt1mLtIHOhNonOUiOT4YxYoQh6liSQrPbnfzjdso5WR30I15uFGDGX3L0tXCWFyGm6Aq29VW3hHzWoh6iaqHkGR43NCZpr+2anyT5j6V21NVOlsh7ONJGDxOPUlVbVbYLG+LG+VcKrce5RuZlYmot73FUpx4qEeGk2N9IyTPRoXDctr5BC/1AyPTVbJp+tab6Eu+mh+Kya5D0eHaENyt5DTxqkWteXame7EKNvtK88uAqk4kMakkKd4mcx9fSTOuF4QTrqjba1hrEQOG2bmEpeqkBDiu1GSYL4+xNSyxGbPpWfxsVjnYeyRwtpoHBmWS5/UmZeOMhL2+ord56G3Y2GROnKMQYC2wyWHTerFsrobWhM2cT3G7egk02NNfd7m9OSnXdbrfSmjM+cslS3aFsJl7msCZRO2BgNNWKUWaVuP5bOcX4mDMRGeeoet4iPb7YWKeO5IFe3lZBBjn67wZhWuixVVDSuPbngrbG8/OyZZSa4kPbzhMSok7cZMNRZ+dZI0zqH3ivamKC8BJrybbakzP2GEzzYaaWq9np3pY8h3N2bAuW2fR7XLkPbka+q3XUoboVrGGnh2KcaauTyablcfMWZPnwRTnak+b15alTaQoVrCYXAiMs7n1Vkt2FMlIOBEu5LmlpnOcMAh+KFhVZNPj1Wgknw702llqlWfNE7JtbzCNa+R6dmM57piz86kMsgDkUbjfbRNrcumSoOFWmnHzAn2+9xMCixt6roll4zORuOX5KU75QNuetfpKnRaoq9YtU5W34IQ6M70WxBmuAUaHFp1PdnHHwPp87/sTMMkyqT46WUL42yYnasbSaCovr3mJDgS5YWapEDJpsANEBnHnvF8sLXTnW7tLzB3Qo9hOmyxo0F6lCzwxlejC2A5D8tfLxGJIJwvNuZ5sLjSqHE7a7bB37XayYFNieso8IuAbP3P3ZS3gKbk5MKdkf2nOKbefam6QcMuiN4VCt9tY0ghN2qXJQIH2ui4dlCBAnzIWNdt2zoYzpe6sMRKhmaXon+ekp7FkeXFmvEihVLKwFPHAC94pC+UhGLRYjtCy6QWMGy7DsbdsIE5sNnZ9GU0BVm2IDcfe8uXpdt0QubtaQhUla09MZrIioqZZox3vuFW7FTf1rZEqJ0x8tEvt5qZwhjThi9xfJnHa4BcynKW8ak4A7xpslYHFwOfmjfTmeJjPyat5SufxWkvNaMX712olBKwQ2XtKHLI8u3S1lBP7idedaWZJ4Vt3TfnnM72gnWmFcoMcctzL68v9GPnlCzadTYnXl/FU4Xk28G+9Sw6HuHx7koaNE/n68v/uRebjpeL7ueL9qAA4/pf77l/+Da7/8fpSeTHk8PE6uk7b8Pky87+8zP30l984j+T6x8H5eEDaNe/nMI0T3t+Qx7nfwsn9W12k7f39OLRMW49/WlO/PY8tXu5iZ+V4BvKdmPf7LM5juEP11hRvj7ME8DL+Ccx4+gf8+Ntt+DxmeH3xe2jq2KvfCJp6A1U5auB58DW+/h1Pvl5++99XeaouXCgAAA== -->
