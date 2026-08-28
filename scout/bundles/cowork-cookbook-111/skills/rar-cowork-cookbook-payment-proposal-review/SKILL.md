---
name: "rar-cowork-cookbook-payment-proposal-review"
description: "Reviews the current payment proposal for accuracy and flags lines that need attention before release."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/payment_proposal_review", "rar_sha256": "e9cc5729e109397f4e71f2f18090c5739ba26b722a431fba428a2c191ab632b3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/payment_proposal_review`. The original RAPP
agent is preserved byte-for-byte in `payment_proposal_review_agent.py` and in the RCI capsule.

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

Payment Proposal Review — Reviews the current payment proposal for accuracy and flags lines that need attention before release.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/payment-proposal-review
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `payment_proposal_review_agent.py` and embedded as the fenced Python below (sha256 e9cc5729e109397f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `payment_proposal_review_agent.py` first:

```bash
python3 payment_proposal_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 payment_proposal_review_agent.py   # or on stdin
python3 payment_proposal_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Payment Proposal Review — Reviews the current payment proposal for accuracy and flags lines that need attention before release.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/payment-proposal-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/payment_proposal_review',
    "version": '2.0.1',
    "display_name": 'Payment Proposal Review',
    "description": 'Reviews the current payment proposal for accuracy and flags lines that need attention before release.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'payment-proposal-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/payment-proposal-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd7b114adb7d66ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/payment-proposal-review', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PaymentProposalReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PaymentProposalReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PaymentProposalReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716a5ObSJruX9HWfrB7sUuAEAhPTMQRCCFxkQAJAerqsLnf7yAuffq/n0RS2d073TM7ERtHjnIJyHzv7/NkJvXri9k2QV69fHk5uWY2Y80kCQO3mpmZM6PzLq9i8CuPLfAzs/OsqUKrbfKqfvn04ri1XYVFE+YZmK64t9Dt6lkTuDO7rSo3a2aFOaT331Ve5LWZzLwcSLbBY9Me7iq8xPTrWRJm7jTTbGaZ6zozs2nANCB3Zrlgijur3MQ1a/cVaHV7My0St3758vMvn15C8P3ly68vdmLW4NaL9NAoPRU+jAKzEjPzweNiAM5m4LpwKyA4Bbcc15s9rz7WbuJ9mv3Xf8WdWfn1T1/estnz8/Yy/VPa7O5fk5t1A+y0zcK0wiRshtfZOunMoQaWNm2V1TNzVoNYZf7rY+YPSXkx+/v07ONDyavvNh/fXnJggjl5/Pby0wwE6e2laqfvr5OU4uNPr0neudXHn37IqVsrcu1mEgasfv36vH6KBQN/DA29u9a/A6mPnFnu28vvnJs+D7snP8HMl9coD7OPD8EgeTc3MzPb/fjTX4m1A9eOk7Bu/kdyf34IDlzTAT49Df/p0z3Iv8ygp0PfZf612gKk9d/xBAx/V/dp9gzUX8m+x/+/iX7U6XvE/1Tcn02A/j77+S99+2cTPs28t5eNm4Q3UB1W4n6Z/fr1JDH0zx+cHzc//PIbEP0vxZzytrLvEr6mZhZ6bt18/frzh/p++8MvP39oC1Brrpl+bavkz2T+WVzvev4Qweeoj3+cC/SrWZzlXTb7XumzX/PiP6rfXmcXMwmdH/frL7Pf98v0gWaTE+9KHyH4Xc/UwNbfxfGnl98AMGTAm9a+PwZd/p//ORNDu8rr3GtmJztvmxlIcBOm7mT8OQjrWfjArsoFca1DENjnOFD/U4Yni3Nv9u3/2HdU/Gw/UXH+BLmv7yD3tbqDzrfX2RmIy6vQDzMAfcpakt4y05/wEKgqKrd2qxsAEWto3M8Afj5PX2ZhNvv2FxK/3ie/FsO3O3SGDyxS6P2EQ3WbuK+TL1rgZk/LbQDobu/aLZCb5PaEvyFAzk/AxzpPbgDHJr/rOEySmRNWwMm8esAyiM2XSdi3b98ssw7esgdwLmYPxK/nYMB3c2afPwNvvCT0g+Ytc+0gn3349bcPs/87+2ez7sInHRJA7mfkgYXc6XiYgU5qpwiApIA0Api4R/7X354xBWIyQFEgT6EXuo/JoBJj13kP8Gm3/owu8Xf6ACyRVw1A41nYvM723uy7vUDp9GjC6yCvm5njFm7muBmgp4mO3rLvkczyZlaDcqu94dOsrd271m9WZd5NTEFLm823mUhLgB3yBPw3mflgQzPLsxCE/3v6H/eBkOpDPaPeRbzODlPtAdaszCKozKcOz3zkZaLO53Qg3ARM2b1lE/+5U6jujfAIDxgEImM/U/p5yjmg7hR0vVO/676PMScOO9+5rHrL6meRm3e+tQHoA6V+GzoT9P/tWVJ1kLeJc48fsHSS9MyC88zK6yOlD95/p+HZg4dnby0KI9js/8tSYbJjzbIKw67PzGbGHM6K8YjPtIyZVD1WPoC877ruvfCD0N/h4B0V37IkBMmuhr89Rt6j+hzzQJq2AuYoa+UuH6QUxGeSe6+4qYKqaqpV8y17h99PIIl3rAHGg/YE5TtVzbvC6em7pQHowen6BxXfM1Q5U2BAVc2K1kpAxj0QEcu0Y2BVNXXNM96g/Nypg7ogtIM/eDUD0kGWgfwZMCIEfQAg+h66Qw7cBA3jVXn6Y3g4LXCAFU5rA2vBOtF9nWlTLkDya5ABsEqZxoAofLiLmqUuiDEw8XuE68AsHsZMS8ungebsgXC/j//z0Y9CvVsyGQ9kmo7ZgEh2E146bv/I63crn5kCQtOpte6T/pjsp6ez37PE396yu4XfIRp0bDIR7O9CMwOdktb3cpwApwagkbrP8gF1cOfS1wcdPvj2uy1f/mE1/fHfW3DfCU79Y96+zIKmKeov8/mDlN456RW0+xxUSFi49Ts/fX7vrM+PWP9B3CM6X2b/nkl/EPGs5C8z5BV+hadHQmi7U6k+PyAC9GfK+IxNT98yxf2RWqA+TwGCTREfACF+J4z3IYA1/Mr1p8EPAqkn3ukA1d0REwT/Lfue/mdrAEDO/Int6vx3LXtnTpDMR66+Azt4lDVAtzOtqvz7RiOZzK/dly9ZmySfXjIzdf/JBmMCbVCYIAjTdmSKtQsYx71fAWfAg9Ccvv9x03S8fzGTRwHXDbDOrO4w8GwI07+Tw6dpZZoBCJl2ARP6PVAc7F3MNmkma5uhmMx7bDqmBdD31dE/ar13LNDh5F+mxv00m1ayn2bfF6WfZu/bhPuGK2vBPunnaUE8+QmGgl/fx37fB1ruyy9/YsZzffwXRoQTaEww83DXdX4gwj1bhdkA4FMVAZiU2/c1wcSD9XDny390Gyis3LIFxOdMJv+IwQ/T8oc9v91daR6bwF9f3jHlmbzngg8MB837uZ6obw7qGigE148KBM/+p0vB5zQAfWBNAua5pG0vCZR0EZhckISHuQTioR6ygkkYPFiQloniFoGiJrZAPMvE0JWJ2giJmBa+QK0FkPco368TrYeTKS7suQsSQW1ngaPLJUYiBGqSjokRpunAqxUBE54D2OHH1Bgg59O/hz9T8L6vSqc4PN389cXCMTByh9X79eNDz8mLiS8Eqw90aMQ9I4/IPXdS8iMWjyBnxytz6aWriO2apODKQxevtY472PRa93VGRMoDd9wNlJSevNK5uRQ7xLjZRBLCU+x2cUaIqoGWPsPI0ZYY5hcr3uptEVaCLLFHHYtNfufdkCUyt5UVWkYaxVXKueHJBQS3pLc1qp4S6xV6ProFOlxW1iVN7W6bufJlwC571lyVO+6wHVOe2mP7IpbTVjn7Zgb0OlnWE8cR6a9ejdV6NfQkTRZ5K+z2eKcHjiXnSUmgy9Ip9qPCuaskSEmmN4m2OF3gqiNO4bl2uXK+UlpdTESIXhgq7VwqeyMsnTTZ23MqH7n4qmjDslf3/KBTh4Bs3NNSlxPn3DfpQeVyY8SqmC3dClTn8RKhHotjC3Jjq/ZwGMBSMjYSPk84eehuIj6mZ/qSUOzIHarVWuZLZzvq7YnenloUXQUxvDzufEswGRRmqfS01Yna5rNGkYXlaryYJSqY1t6MT+0Gapg5vWTUkiF27eDzxbixkKw3CFSWhn5vn9B1VRwUDAlJw9ST4kDryk070r7pQVGecfiNupx3PNJHGk27sjFktyMf7fSTW0C802jSJjuLB5rFA5dt1VvGOt4maCJZS/DBjro+8WIMPxDWUexHqio7UqMt/dLfPN9xXNMyysY+YHTbu8ipjg4sKC4pMkXhECwNWSYFrKpYCeqH042y54Z4gYN8RNa2FW5Hvs/0i7mDaS2AEMJT/RQty+YkQOeup/rDQogHnlBGaM+0wXLA2WsEfhJrp2uFJso3FOqjUs0ot0XXUtd5wRrvV4JyoPQ2g2SvGlFH9K4FGdq6XGi5FOKpIPBwai6qAzYuTuF1mxWtszqtvIsZni9NlPeOs41azOqNvtRicruNHMqmB8PKTJzNasbIxDi265JBGHWwlrC+PXDWQAOaYtqzJm7hdUYV29iYczzLZ8Tuysi+jKM27fi+KmzpuZBq22yTp5vyspCgy9V3vGF7sD0RXUnWXtqjId8d+ha34R5zPPlMSt5ZUvFMiI6r6Dy3XYgdUBqvVwpUzNdlBAHOp53j4mYP3PxW881xByNKtNHFow3B8UWDsUXEK7ddczLZAx13nUbiQT636pKTbgyeQBp1YJHLltpkhW93hRarJXYmIGLUVkOxPZAkXZ93Z3hwJWlf7viVw/Uxupm3CUXEpTMW7Q61bJjLeI6nQ3Hc0IGulgqkG+miuSi0MvDzvZlqkXHh19aGZ6A1JMkQyKlr9sgo9LtigQkWlBpjnW+QWBozO0L2XI8vIT/2Nh2iFd22m3NEbLjsPqQkog1ZhKK7nTIgx3KjSrbI3aj2eqjiozHU4znSUqOQLyseNyu5NzaKeA0XosYeFpicZxWpNdcQNVdYGhcW6xO+sQPeVhHRpSeRMJe60t9s35BcGYGhuF4UhyWEU715yKRsvFCrDcofLkeEuqkES/D0BkcQQ96NoVTFuruSCTQ7ceuOowAk7ezNSjwb+/WhR3v5vNrroz23YAq7CmdxnSpavlpyt6yCD+fb3K/NSGgqMRznMg8Fp3yn8pSimn6DtazXrVMv8eGrvzc4uwu4ynfm5BrPUnQ0r9vA2nk+syH74nQEWU8r9QRry2IUGLyortDavlCqd4DhMY9ZwRy60orONaphh/1OaSxT3qhouzvPhT4bFqm99Vj7yiHzuTeusFqr6IHnxNKTmUpo5yNaKrwUEli5QqmlfDxyAiedbaKbeya7uei223knv1OvF2gXkSuITiRsNT/3GKnzkJ0TyUbe8/kSMrFB8JnYD7DiKu4Ol3E8+zdKrhJjKK1DKSGY7aceG8so2cG6HzbCxYdd6dqtoHRc4MHuWuNYKbJLhtlZ+0QGXEUoy+7abWxWZtteZ2mS8S+Kqe+SNVf7IlQasdHdWlBnp75v1yo7dKwrQqc+9w0fjqSB1yXVjW8xc0UxU+K3Gn5DCzkVDqUIi5dqMOODMPdubaTzNsJRnr6q6z18vfVdourouON8txPVk7jxVjrR84rmsCu7XLY92au5elVgds3EzCo6Va1qGtGOhG6DVVeuDO9POgqNG3Jr+HkhXLGMc68se9bqU1EjgzMud6qdHujyQp+szaVflFxYHlO5zthbwfEXQmSkVKmWhIuo4nWvrujdiHB9ZBj7y6U4duZi27VGNT92e2YjBHaADNHptKNClpQxWElZVXWO3XJYhKC7m92mX9r7vaaK8TEh8ZJG5RolIX2fCSjdImcK2V3oKpMsgP1i1dL7IzL6PJfZ5/0lQ1fZ1s9FD/D40a4DYwH4lruo9Lxld+fowghNilGHKh+WMrGAI1Mru5IKRPi2zbVSGZYshrB7IQd5hLE25DF1FLv2BAsXi83IYyhmecfM+bZGN14+Rjw1b+GKYq54rpxKj5E4ttyTNRt1nKJW21gdEjxYcUgR872/P+qZiUlbrl16EHw1ZaekxCKBdmGHyhlxdVA0iDPTLtdge+U6tw6owEqEcxJUTQNLl8nFau5CYL2XiwLvFHW8uZ1MokQ3IqHgo5ZlhjEsWinfks62LebNsjb52L1wRwd2Ha4TdydnRW30c0gYi2t3qo31jqFitDc1GmE4k61lRwi78y4Wb7TqnculrS4dJYiqhF67p6AEbQyqyIKFAFwPFanG5SY05VVYmFd+Q8zh1LKzfbLw17S5K6K8uMpGxkuYuqTZC3NWAJOssktXhL0ZbyHuuAx9jLfRa8rLZORDjLf3MUD7ErOllAux4JW1sFDGIEeESsVj+ECNu4Ng+KTNOE1d7o8oF2CKHPjqTb4u9pBJHeTjsNF9ADHbAxvRhwNEGId54IRH/MQiluzjIk5YxtCzPBU1PQQDuFJh3O0pCGr9WyIqjFKi9kleC23dFeO+qxjaFKpiSNTN8aZuhXhB10fIGfljMucc5GAT23PuaGZSGOy2utbKAcm2kR5seX0g5O317GhLKoHcg6TGSeEz/e7S1CKic1sHwqs9a9nnOoE9dlGUuyiVYRGlSak985v92a4xrS1HMy/ioWH2LLe6zouQ50IxzKIUFoTgfPB6dhkeSq7gIlNeRie0qLjM2YpXmObOeNEOxIBD2ZIHRaPUyjnLJbDZ2AyR1W1a/9ioVA2HVTEulFQrCapaqi6r35TltmZ0ouiqGD75iFDoVDP0zobv44WUcRvtSvqCH7ijSnPRfjyAJY4b2rd+XHdkAUNHAgagcETYcF8INGAYh1rT6EnHVuvWSoXkzI4EUqF7VilbmSd94qrI2JZh951hCLIaaVuzQ/MrJ57GaJscc5E4+1vTvMQ+pPZNiTQxN57406YIWuYCQBWVxGTjuHuRSvZa6NUDQ3vY+rSVypqzMXnuqIedesgWjr8XWTjU8Sga9uyoNHtPPI5ozSs7gLfIXpNKdaj9ZX/WinVF8bxE7iIvWjA0FY3WdgMKokRNhmZlXlMk3e2iy3y9COz9LXSsNSMYZxplsnQfn7bmxdCQ+pQNl4OSwsa5RIvxQIcqRbdmEnnseUhW5gULOnogPTzZwJS0IRtOIyyxpne3tc9QeHqls9QxYIjboZG4qUvJjgNNsxyKMbdHhndQ8gLR5pZ2zHJv8VjGjC6VnPHqukRqpJkfIraK5yZxBCuvYM0kIx5TeiqNGIYSq6N9vq7IE0cH7CV3zg7kOAfkgLjHSNojOxLVWxRZuuTy2AYtD9/GztB3WmZePLJ39e7KQuzhHBma0gL+WnMNwuOHZZEjYdrDLd2KoiEWuU2UXLBbHTLuvIZoa+U66Xy+iY/d+VbCuw2fo5ArGYhsLuzL1hTYSJZKfWDn5K32qzXaqqqMYOtmsfS2UUWrXI1GlTQqpLCPldstCqLdxlFO4qhU280Z9muCa0nzbKKDl+1PZClQR3TuDfGSqchsTi41b5XvKsHe8oQ0X928KDew/ZieblG1U/J+YTN0mQ+3/rrEKzXzgQCGRhU3LbC85lALMmQmlU+bulmFqzAlca4wsJBFz/BmCMTOomg7QK2jnUmn414hxMHWqPDKnM1CtxBn5xvy3D7k+41TIHZ0A6vjzkzDM0vINai5ap5SVo0UnnVZi5DuEPjyJK20zZF0KA+Xfc9KdidhvRNuldieWf7mFGxc873bFS2SuzCBk92R1zeFKeRWAQIbFybaw+UmxXXIRKDj3OyxXMkbjnbOR+oa0zzJsuiiUzNAKte5AiOMd4Yr/cponkmuF0qyr459Y0nDKqELp1gtfFNc4HkQOXMrqS1nFbEt3UnKbnmTQ03gJdRRS+PYaUwQR+pFik90vyP7fo5fG5nZhNOW+ewMLFHogg5fL/L6hg3IDimOOtsafBHKVEOgFGswfkpWFW+2DGTL0HoVt4nWqXV5CoYC7ucV1a1cSa428A73lxQfbQGEodLJqKH1vjaN9DbM153PSGC7BvZ9OLF2tTNM0Gvba29+dWT64JY2ltdEY4u2KCcAGsWkk+swgkj4kDbgy/PhtDQ3RhwnNk9Ca1dwvVMnLXRdRVZJQ5ADps0ZGYv7lgoa+4bxSIyxQ+BbK0LRFey4Lo8s6ZVF0w8832ubBl/vJAo7hDFh8dZ6uWDbFTmUywIVDpGe52wwBhuxO2wvI8la/enQEj6Tt2DTxDpra4lcQ3e92Rpzn705brzXuUG8FeucGko8Ssnlgt42xCLY3gi/XxFu5Hs7qJxn2xXaE3kbk0tiFCABLEvn9Wp1jOQVtnGTJNIb3tAu2Rwd2vTo4Fpqrs1RwKlaOw4cbpSEU5PQXvKKdbgjBXyL2v0VagwGG3dhFK23i5zOECpH/dFa7Iwy0jNtzzLoEli7LVoynY9OwvqFaCe8vh3nOE6vAzUmDW2lOulSc6/n2kwvKQIzI2hqrdjN5Ti88YCXIhUWDFcGNxJfCZSJgEawIb+epYbAMVJKUZZA4IWZ3Jbsvue3wUrxnIhoBZVpR38lJoodI0eIoklsqW4McRvTW7s9rLMUYi9qeevZW4wo4hBkUbOPKQAoKIInypA5GqHaiauSBxsrIWHvhIS1XizRyzoZNAK/+DeShlmWP28cr18FmzRp53rO7zz4qlsildLGAncYIod3ddOGc06iff0iLfwUnoNdnd91xbI+6uuFbPm4VlnEumei02J/WmcW0a0XrRJveGmf2vAK0YTB21Lj9G6c8AMPzTd4eoYFhI+N1Rzl1+v1y6eX6Sz0ef78r94NTwd8/2vnjI8jwfd3TvdDYNd0vtx1ffmXlvzy6aWyQ2DH4+S0Tlr/eeD4385NP//FK4pp0vB4uTq9COub97P4xvSnv/95CTOnrZtq+FrnSXs/sP30YrX19Iqwnuyywe+XuwtpMZ1Um60TNj+OQJv8K9D8Mv2xwPRex3VCs3Gfl/7z4PjTizOA0Id2/XWBL7+6VTH59XzZAdxBX+FX5OW3/wdKDEH5SCUAAA== -->
