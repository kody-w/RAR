---
name: "rar-cowork-cookbook-adaptive-card-analyze-customer-risk"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_customer_risk", "rar_sha256": "7d287c89cc6869c261382dae7084f378d0e507026e842823ae2b6af09b611ce4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_analyze_customer_risk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-analyze-customer-risk:8993722f7a4111d545d7ad369368c2e9caa888e149844a78302b3da8127504c4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_analyze_customer_risk`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_analyze_customer_risk_agent.py` is
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

Analyze customer risk Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 7d287c89cc6869c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_customer_risk_agent.py` first:

```bash
python3 adaptive_card_analyze_customer_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_customer_risk_agent.py   # or on stdin
python3 adaptive_card_analyze_customer_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze customer risk Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_customer_risk',
    "version": '2.0.0',
    "display_name": 'Analyze customer risk Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-customer-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a12f1a1cee4c15f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-customer-risk'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-analyze-customer-risk', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAnalyzeCustomerRisk(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeCustomerRisk'
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
    print(AdaptiveCardAnalyzeCustomerRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPixrbnV9Gr94ftR3WjfekbN2KEEGIRkhAICdyOai2pfV9AwuPvPimgut3P9n3XExMxVFShJfPs53dOZtavL3bXhkX98ullD+wckew0jUJQI3buIUJxLeoEfhWJA38Rt8jbOnK6tqibl9cXDzRuHZVtVORwulYXXueCBrGRGnSN7aQA4T0bvr4ARLBrD1nvVQVpcrtswqJFCh/ysNPhBhC3a9oig0zrqEmQprXbrkH8okZA5gDPi/IAiXLEs5vQKSCh5hW+sKMUfsMxB2BnzUcoDujtrExB8/Lp519eXyJ4/fLp1xc3tRv46OVdlFES/sFXeLLVIVc4P7XzAA4sB2iPHN6XoIYyZPCRB3zkefdjA1L/Ffmv/0qudh00P336nCPPz+eX8UfvcqQNAdIWdtMCD3Ht0naiNGqHjwifXu2hgeZpuzofDdVAc+bBx8fMb5SKEvnn+O7HB5OPAWh//PxSQBHs0difX34aFf/8Unfj9ceRSvnjTx/T4grqH3/6RqfpnBi47UgMSv3x7Xn/JAsHfhsa+Xeu/4RUH251wOeX3yk3fh5yj3rCmS8f4yLKf3wQLuviAnI7d8GPP/0VWTcEbpJGTftv0f35QTgEtgd1egr+0+vdyL8gk6dCX2n+NdsSuvXvaAKHv7N7RZ6G+ivad/v/N9JplMMceLf4n5L7swmTfyI//6Vu/2rCK+J/fpmDFIZ2PebcJ+TXt70mCj//4H17+MMvv0HS/yOZfdHV7p3CW2bnkQ+a9u3t5x+a++Mffvn5h66EsQbz7a2r0z+j+Wd2vfP5zoLPUT9+PxfyN/IkL6458jXSkV+L8j/q3z4iRzuNvG/Pm0/I7/Nl/EyQUYl3pg8T/C5nGijr7+z408tvECJyqE3n3l/DLP/P/0S2kVsXTeG3yN4tuhaBDm6jDIzCH8KoQQ7PpP6y36xk+WPmfUHg0zHdIUTYXdoiUg2BCYH5MHp81ADC3Jf/5d6B9IP7BNKp/QSjNxei0dsTBt/eYfBthMEvH5FDCDkXdRREcACi85qG2AHI25HnPTqaLvtwGdlCkaIH7OjCaoScpkvBP5Av/waftzvJj+UwqvI5h76xocM8pAVZWdR2HaUDYo9Y5Qwt+AAxFuJJXaSpY7sJMv7pyo+jfcwQ5E+rubCOgB64XQuQtHCh7H4EcfkVOr4pUlgN2tGWTRKlKeJFNTRUUQ/3ggPt/Wkk9uXLFwei/ef8AcYE8ig0zRQO+Cow8uFDWQM/jYKw/ZwDNyyQH3797QfkfyP/atad+MhDg3XhbjIY0OmjNsHs7DI4rEHG0IDQc/fer789fDFKl8MiBXMq8iNwnwypfQuFUYOHg969A3UeRQT1k9P3dkOuIbQLErXQWjDPm9fP+UiigEPra9SAdyM+Jj9M/+7uB5/RJ83ThtBPfl1k97H3KByd6Ra19xFZ+chXS0F1oV/b0aNh0bQwcEuQeyB3BzjTbr+5MIc1uoG50/jDK9I1UNWR8hcHkh6Nk0GAstsvyFbQYK0rUvhnNNCdPZxd5NHo+Ge8Ph5DIvUPMMZm7yQ+IgqA1kRKu7bLsLYbcB/n24+IgDXufT4kbiM5uCJjWQejj+5ZfY88/k+7iP2ji/i+A/nc4ShGIv9/W5W7zJKkixJ/EOeIqBz00yPAxv5q1PfRksGW4U75ni3f2oh3xHnH4s95GkGn1MM/HiP9e0w9xjzwrathwOi8fqc/Znd9pxu1MDJGV9f1GM325/wd9F+hYaBfmhG/YAInIxwUXxmOb98lDaGi4/23BgB5BN2YDDCckbJz0shFfAC8e+S3YT3m1dMRMEzAaF2YCG74nVYIpA5DANJHoBARjFdYGO6mU2B+jGa+B/vX4dHYVpUPv3oITCDwETHHeIYx2SAOgL3ROAZa4Yc7KSQD0MZQxK8WbkK7fAgz9rxPAe3RF0Vmt+D3Hni+hLE5VhfI72viQaoQc1toyyt0Asyr/uHZr3I+fQWFzcYkuE/63t1PXZHfV6d/jMkHZfwG/7BNv4ftN+NAxK6z5g5CsOQmDUzvDDwDCEbCvYZ/fJThR53/KsunPzT6P/69tcC9sBrfe+4TErZt2XyaTh/F7732fXSLbApjJCpB87UOfhjr04dnjn14z7EPY459R/phqU/I3xPvOxLPuP6EYB/Rj+j4So5cMAbu8wOtIXyYnT6Q49vPuQ6+ufkZCyOyQbR1hq8F5n0IrDJBDYJx8KPgNGOdusLSeMe5e8H4GgrPRIEwmgdjdWyK3yXwqNPo2IffvuIxfJWPSO+NnV0AxmVPOorfgJdPeZemry+5nYF/a7kzgi4MV2iOcZkEUwe2Sm0E7ndf26bx5vtl3j2pIBp4xacxt2CBgy3uK/K1W31F3tcP9zVZ3sEF1M9jpzyyhEPh19exX9eQDniBS7Z2KEfRH4uisUF7Ns5/FGJMKSgxhPBmlOU9R0eOfyACL4IA1H8kot4v7PQJFBDLx7IIq/EzvRsopwf7KAjhlzHtYCZBgOzghD+ygXxqUHWwEHujut/s902t4qHLb3cztI+V5a8v74AxXj+6gkfgwAl/p3kbrfpedN9G2vZI4d5i3Y18b07foILRWFx/9yoYO4W3Ryi+fIKAA15fRlPWEey4b/fF9MtDIKjJt7YWUoDQ8aEZm4UpzCRICZbwctQigbD3Owbj48i7jx8vPv1lL/wvMOATy3EEg+M+Y5MYhnkUSXmM7RE0R9CsiwPOtW2WZQFGcixJ2gxLoLhDeDaL4QyFki4J5Ri9mdlPOabY6AeowVdj/9+06C8PErBw4BQNaTAezjIuy7kuzdKci9MYweKeDRiUJX2CYT0UUCiD4jRgSZzFCRvgDm37KOfQGOaCUcr3DvEh19t7N/7umQcavEEIzaJRaty2XdZlMNLjGJt2AYE6hAswHPMYAqAUR/jQKiSc/3Xq0zuj8x6qj6ELm0PYml1GPr8+vT2GI03CkUuyWfGPjzDljjZjyY4SOlxN+3wTc0nbb45n5dLFdX2uQEPj4IrarqM6lR/DENqFwsFYbMVdMSOOJJVM9PXkemDknCy20cY9rrtavaFk7wxX/epa4vQWo9Zxpi8KSt0vuM6fubA/83QJ2wzmpCg9SSLtm0ENVphSsheUNaHh+DCZNiXAhrLd2tvzWdZrBUVX2/OFuJFtYx3WgEWzNs0WxeDn/JKxzqeqrNaHfT1Y61O9TjoTWlFd7A6lsLNJWeMdFyPXl3bZ28vDwKk5hXvq4Yh7fsNsrZqlpzGX1Yqxr9Ei3m8V+tTaVYofK+ocodhAxAsDy3fbaZ9u5axsN0nopIdVqzoYFzSEu0/7xZxdiFS9VWRrhfv5utMt7bzLj3v7im6tNlvJUbfWYbuhSqnFl+06nm9gMGBHwaiPS3uBGTaGc4sCXarKjpP9o413upvLh61gZycZA+tMY+V+LVBZX+ozaqi3Nc3v1rdASjfB8cyZp7YhrIvGD3t6INbndMZLl4HemNKwuNZ5QEhW69XNulMTyNdVCBVf1OYKt7zaSWMvXVdpkfKEwvvLJdbOHEEJcOJmSKl9AcBADd88Hk/4YeqZksRJmFrgzWw1LCkmPQT1XlLX1O2KukSzrM7RzVcTGpsQcboTk8VOrX2UAK0WKZZqHQRmmq0TD2zrppYxP12eJAU7h7NUd267s5R3xpGqWvG8m1jdjMK8/TlQjFPH8L6JWhmzOJwLiqy8sxVpxBldWfE6h9YV/PYcuduS0mZ2Gc/k+sSGLMZxFkuc8TLc3HBwuwnMdioXpEE151WyNnfNhDzQbLmKaH+SDXYIf434jK0PTXzzsuXGA0dSUshbyEjzyWopaal0LtYRpk3ma4POLQKdTvX9vCDU3qUp4jLsawfL6POhqs+mhcpiv55I5THqj8qhGjRv0beiW5z6ykmChejwczJsYuNyvK6CYmHkh0lCUuI0l+uIknkRlxI1vXon6rYwL+T2tBLm3iYphXDvrkDDNfpyL+9xvQoXLnY+amqVpSV2jsNeWS7jtceu4hU99Tb0edZO0GkSr5ZkTui9zCZnHkYyLbXDfg2MPT7fcrfK7gSHUq/9tJu7QjtTlZamfc43eWrTeXzsH8hmsl3TV8y1q2G65Hm9OJrsoT5V0i2GfcZyaduScMWCdCeg/pHjr75CmeHhhl9QfivOmT5czJhCOeC7tWlOBsES5OnA7VKdZv3EJErhfLgw7MQE62pz6a9Zdzz51AY7NjTMU6WaWnUYaru1cdoAwkmY6lSye31bwfTV27Owpjds2W1bM+RMvgmtcxTE3PxGJ9G6T/NVu6VckJyntOgdPWtII67aXlZo0iV6nun0TjSqfWdnsSUT4iRy6OvmZIusu8IT3ppybgkubhszc8Fbxd2wIYPsiHVne6/K+ZJH64m17+f02tGoGTh7hgyr8HLr346EEa/rplduE707KIbMLKXJVBH8YBAodr4tI6ogY+yKp6jBrDW46s717uLz+EqrCYZoZ/ScvOooLWqbKz8scCORyHqNL/ho5UuCe3ajRJvsleXiZM+H0zLeztrVpjntgElizi2RT90BTZcEprnbTKm2t9S7rIDPNEezL40oPrZlrx2PaUORAbVblQK7Ukls1iRDMylEeombt6Wrzm78ap8kou2G4vLoNG0zMEm4Os0WwYbGC4nM9Fmtb4/HiyBLHkEFM0HE7PRwTqygFTatCRZT9uRNaTQoxawlbrudoxozZ+nY7KRp5OOOLhhNveQpDi5ORBa9GCRoKVtLkwGTwz5ebX1a2bRednAFoaMV4badTyf7nSYycaUyxlbU3dCfuMpyIH32tHfEksvnN+o0MbQhqlZHt5tulGYvzsLVytuczfCmK8AWF/zm7MkZLGe8RE9iuljoVKLwZ4+vbinDu9UmMbB42CRr2yP14yAu1gZWi1awma3JPR93/JruNbsyt8tUaRs5mChmWbkWoWeGlp6I6UZW9zZ1mU/amYwl0WpECiZfGTKNDps80vkpEaxEoHlLWW0duW72qeR0vUHYfWHT2nay5/lSqp39kVkV9EIgTjcvdNRmqQvVAa81vKp7nAsC8+JcPZft5No6hlywP64S97ytzyABMqFOZt21I/WVkc8w1mTOwjU4g2u0qtXjlhCTK0t3E28jXjVi5QV8oBcntuRZTCHtOVaIWBOBActse+UVbmpNvWhZyuJcnKGrHZ3eHFivNpFMCOoiVyzWn9123EwXFmxr2GgSHkiR1i+71A3UAFOHM30LDuesvRxuYpes9CrbzYT8GGbptVKCy/bcnLptMNspmtRmJps6nF0VAkpuw50DxAzvQo0gHNOsgCBNFpeNzexCaulNz906knx9ySzrQyKHDWO0V3uYyvmakrOqMsNmOaltStXNFerRmi6Icu5V+MJwp3OVHuaDgad2o06KxM05aZcQ2T7adlfKlE4huuAnxm5+aJhSKnAxVQ2/WTS9s97WiyQy17MZt0mibRtFhhtuiol9XjJgDqxpKxmZZPOVp16mrmiy4fSSNbE+8KZmnHi/W94s/8rY+8zbE0f9uHNRBoCI8amBZXOXXyTpwGnozqPnFHdEo6DSrKlI0lMTp3tvdamx/ST3mG09cw8lprWOc7H4+RaFpURvNqTVsY2gh/x2sZ816MZy/LSQSVM/+czMPR8jqQqBlhSddaZ9g1r11HxXWFchQalyX6dtQhXzfm42K1tPddRaJ7KqUF4pCKnaLp10vu8mx5WBrUUnxSs8icmZT85nokzVfoTN+izI8hV9uoU5jyWVb64WstIfZ/ElW9j5qib5HdVssl281NsgP6xKH02IiM8tkzosUZYWGMBP5SzhJF/dLk90ZcXzdm+yK2W38OxtfYo0STpV1knNt0eyPl2jXSZHlu4w8i6YxrfblBN62LJg88uedcNuPezJVtnFiuyfYjmQtrHpitXZDyxOo+XwYKP91EhPpbhC2/xMl8fVhcaTeu8G1s67OWHtOvvBoTSblbl9ccCD/rpi9BvL1mvM2S3n+MmR2iIq3bk5wyax4QhL/eBXh4G/erfJpoVWtY77xYYRmclxfmhNrs3ZRvZFXprYqJbctkakVEahLzjyYEvzxXJB99huYghmm5xlY9GKtogTMZXdgnkh0Rpg8RO9u2SepOSNeisrNRdJkjwud+nuYLOVbYZrUQBRbAdrdF7XUthM0Vq+GtKOQNdHJeXsrgij1UHbLBdyZRoU5jgZJkxvFI7tyMXG6NUhJ/hKMRxzH1xcJUsvVxtM2GRPhcSucmLTOzdZsTolHsGoDruPpblX4qoTTZ0sYLpGwPJid/VURV/Nds1Co/ZVuqu2TjMXJYNm2nhXALJPqdvG1zCab1cqI0McU4ZDCZc6eCEsTHzAprdrc2iuLd21fMv5unJBt3q1ioRrI14Kbc6eWI1WmwVfd3lw8DT27IRtcvJhi3Pd70lpIx9KxqSTyuBP++ZKzHlyOzOSlSuj0jpkvazazRdzJaKMzluj+AVrTgHmWh7P0zFpHzvJmVNX72KVF964rYWZt4+mywXWSMsDvRXjU1JovOiuW/m0PU+NXZKSemSdMPfCE6eInuy7wEDZ+Y0VhZhwMGzmrzerSpAWgFjjxMJlTJcVFJQg1QiujZhmtU27oyrA5CKmPMP1lUpgwHKs1lCPeNYyYjoFS97BarzrJldNLk41YLwgIE2vASIdkSdBsFPm2PutCt3chamBNZZ+XrJSvsLYLWAyKj8tB1yzlProJBO3tYVV5cZmvlmTu961piYjgIafH5U8XODmdTJX+nlqucl1K3fz7kBgcgKzxk0ZUPN5dfDN3lWdpU5ct86EiAbCw9U2PPkqsxlY/HpMgkm67AnxclsQDXfSMKDuzhNzMp0WK9/YXIUNY03Z67RH0bRiCEtraK5DBaI85KuD78CrSgzVomYtbVfTGlrjTCjWNT7kHE+dFYnPYIwU0SIIFFXNNf6EkmzAlrEroRZswbKbGtedfFbklthMKHzDO0fVcvIdCpRwXjFWYG+WXOfcsiUwmlmpRE6xN0zjPN0N0qS1bqQbzM2Iuex4oE9jEiJMpV4HQSbIgJ45lO95ujW0g35pbnvJrud6j8fmHMt9B8yCvQjkiTdzFZXoT5xD2wo3tDLbSFNpyp1YRm+udVcFkyAzgqjrw5LjFj2qOZ2feNt+gXMOhl8XsTirhtaRbPxyOQOruzqYi8ryZT7oJRF365xjmdDTGhEXdxZZHRsu7p1GJGwqnkVMf8rd6MoNia72koylE/ey2xgyHxxSM68HGd+j/SbirEM8EAGhBxfJOOg30pAVdtHK0jLfafFas7G01kScpG8wH5ZCexpAkm2vZEtPRe1GbqVYJ0S3u3LGDFuXkUkTAuOkgWEsQzXZyLO1wdjoehFwqMn38x7U/sEOd8TJ3vbbyTQWyaEr1KvMtp7AXXpiD/tM5bLFb3ldriNH2qMmYc8agraa5szSOyLGwEmf9s7yNOc8nRhs4mJZsZyLYT/P6GVyuyrT5qT25MmexDw3uHhAWjK9PBCrlgGm2zvxhOhmNPTNIsRbqVPxq+n5dXZhGxLtmI65hEY7Xx67Krq6ln8SLjrKiuppFmzWt0lGCpdzDnI90HdacprSegK83UY9kOCyV3QuIbB4QTlAcOCSO1xogoB6k0nkagJ39jFrclFw03c91CHqa9AyShFoHNFP6eP8Fik0hy/djks29ZRCLUBwQgwgEF3yRuiPRDo1F461pP1iOhlwzu9FhSLYdetFGIeScr9YpststS6uCzXtAYnfltMLmc0MZq9Iew4yPZILor/gIb0op6Ep1mTj+0xviYpUhsdO2/XAXrOGQuDlZZERjr28UPoVA+JGqnyd2ZGeoM7p+QxfSEK34Il+nTBLpdKr4+zCM8mWc2zn4hw8khO00lzzJr+JJ/QSBaAQvXxOTjYC2UY2u+eoEK4VTs3Mgh2eiV9nNxBv4g2YlO3exflbOBj73WlylO35fsdtQNTWqhWZ4Bar20tJe1RH8VOmW+x9/mxJlxnEpEpLdhk20HHoM1sZkAS5Nv3Gg7+yLs5uckXJu/KEnbyqqzTOCI7aNAvdnrhNj2wwzz2346mrRA2tEp8FtNquF7goyvPDgtQC+VYl8loTVRabFBO5sBwX7YnFil7acT/QWJz4U97nT3G4jjY7nn95fbmf5r58wlCKI19fxmOA52b+39wJDm5R+fYkRjA4/fry/26L8rFd+H7Yd9/aB7b36c7909+S85fXl9qNoEyP7eMm7YLnxuR/24r98G/sEI8Ehsep9Hgy2bfvxyGtHdz3sKPcg+Pr4a0p0u6+gw3t3TXj/6Y0b8+jhJe7alk5nkt8pwq8L2oPatAW8L4JX8b/HRmP24AX2S143gbPLf/XF2+Ajovc5o2gqTdQl6Ouz3OncdN2PHh6+e3/ALcYUWF6JwAA -->
