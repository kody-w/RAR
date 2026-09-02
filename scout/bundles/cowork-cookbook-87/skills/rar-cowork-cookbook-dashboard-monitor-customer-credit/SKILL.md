---
name: "rar-cowork-cookbook-dashboard-monitor-customer-credit"
description: "Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_customer_credit", "rar_sha256": "eb1a73a7ea4a970734099ff72f630f3c1be33c323121c88d5c1d9213a452cd23", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_monitor_customer_credit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-monitor-customer-credit:c9cee2245d0249164b087d5209312b116449d0ec75a492ffd810b72de480c1b8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_monitor_customer_credit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_monitor_customer_credit_agent.py` is
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

Monitor customer credit Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 eb1a73a7ea4a9707…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_customer_credit_agent.py` first:

```bash
python3 dashboard_monitor_customer_credit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_customer_credit_agent.py   # or on stdin
python3 dashboard_monitor_customer_credit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor customer credit Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_customer_credit',
    "version": '2.0.0',
    "display_name": 'Monitor customer credit Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-monitor-customer-credit',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a9f3cd4efdab12f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/monitor-customer-credit'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-monitor-customer-credit', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardMonitorCustomerCredit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorCustomerCredit'
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
    print(DashboardMonitorCustomerCredit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5OiWLruX+Hk/lDdY1bKTZCcmIiDKIiCIIioXR1ZXBYXucpV6N3/fS/UzKqant4zHXE+HCsqE2Gt9/K890X+9mTVVZAVT69POrBSRLDiOAxAgVipi3BZmxUR/JVFNvyPOFlaFaFdV1lRPj0/uaB0ijCvwiyF29Uic2sHlIiFlCD2Pg+LrTAFLhKmFSgspwobgCx3soS4VhnYmVW4iJcVSJKlIaSIOHVZZQlk7RTADSvkM5LlIC3hdihMh9hF1pageEbSDJkT1ASxHMitRFIAXMjE7pAqAEgTghYUL1A6cLWSPAbl0+svvz4/hfD66fW3Jye2Snjraf4ugnznzj2YczfecHtspT5cl3cQnRR+z0EBhU3gLRd4yOPbT4Omz8jf/ha1VuGXP79+SZHH58vT8E+r05tYVWaVFZTSsXLLDuOw6l4QNm6trkQKUNVFeoMNgpv6L/ed3yhlOfKP4dlPdyYvPqh++vIEsSmsAfovTz8jEL0vT0U9XL8MVPKffn6JMwjETz9/o1PW9hk41UAMSv3y9vj+IAsXflsaejeu/4BU70a2wZen75QbPne5Bz3hzqeXcxamP90J50XWgNRKHfDTz39G1gmAE8VhWf1HdH+5Ew6A5UKdHoL//HwD+Vdk9FDog+afs82hWf+KJnD5O7tn5AHUn9G+4f9PpGMYAOUH4v+S3L/aMPoH8suf6va/bXhGvC9PcxDDUCssOwavyG9vurrgfvnkfrv56dffIel/S0bP6sK5UXhLrDT0QFm9vf3yqbzd/vTrL5/qHPoasJK3uoj/Fc1/heuNzw8IPlb99ONeyN9IozRrU+TD05Hfsvz/FL+/IHsrDt1v98tX5Pt4GT4jZFDinekdgu9ipoSyfofjz0+/wwyRQm1q5/YYRvl//Rcih06RlZlXIbqT1RUCDVyFCRiE3wVhieweQf1VX4uS9JK4XxF4dwh3mCKsOq4QobDCGIHxMFh80CDzkK//17mlVZgg72l1/JEO3x6p8O09Fb7dU+HXF2QXQL5ZEfphasWIxqoqYvkgrQaON98o6+RzMzC9JdybFBonDgmnrGPwd+Trv+XydiP4kneDGl9SaJd7+q5AkmeFVYRxh1hDnrK7CnyG6RXmkiKLY9tyImT4UecvAzZmANIHYg6sKOAKnLoCSJw5UHIvhCn5GRq9zGJYDqoBxzIK4xhxwwKClBXdrfRArF8HYl+/frWh4F/SeyImkHvJKcdwwYfAyOfPeQG8OPSD6ksKnCBDPv32+yfkv5H/bdeN+MBDhSXhBhh05hhZ6coGgZFZJ3DZUH2gjS33Zrnffr9bYpAuhYUKxlPoheC2GVL75gaDBnfzvNsG6jyICIoHpx9xQ9oA4oLAogeuMMbL5y/pQCKDS4s2LME7iPfNd+jfjX3nM9ikfGAI7eQVWXJbe/PAwZhOVrgviOghH0hBdaFdq8GiQVZW0GlhuXVB6gyV1Kq+mTDNKqSEcVN63TNSl1DVgfJXG5IewElgcrKqr4jMqbDOZTH8MQB0Yw93Q2cbDP/w1vttSKT4BH1s9k7iBdkAiCaSW4WVB4VVgts6z7p7BKxv7/shcQvW/BYZKjoYbHSL6JvnyX/SSYj/3IB8VH/kS42jGIn8f9W8DKqwgqAtBHa3mCOLzU473v1uEGuA4d6zwS7iJsMtiL51Fu9J6D09f0njENqq6P5+X+ndXO2+5p7yaigzzCka8q52caMbVtBhBg8oisHJrS/pex14hjhBc5VDSoNxHQ1ZIvtgODx9lzSAaA3fv/UEyN0XhxiBXo7ktR2HDuJBIG4BUQXFEG4Pu0DvAUPowfhwgh+0QiB16BmQPgKFCKEbw1pxg24Dwwb2UfcY+FgeDp1Wfjezi8C4Ai+IObg5dNUSsQFsl4Y1EIVPN1JIAiDGUMQPhMvAyu/CDE3xQ0BrsEWWWBX43gKPh9Blh4ID+X3EI6RquVYFsWyhEWC4Xe+W/ZDzYSsobDLExm3Tj+Z+6Ip8X7D+PsQklPFbTYB9/FDrvwMHJvIiKW+5CVbhqIRRn4CHA0FPuJX1l3tlvpf+D1le/zAJ/PTXhoVbrTV+tNwrElRVXr6Ox/d6+F4OX5wsGUMfCXNQfiuNnx+B9vk90D7fA+0HwnecXpG/JtwPJB5e/YpgL+gLOjySQgcMbvv4QCy4z7PjZ3J4+iXVwDcjPzxhSHcwBcOYfq8670tg6fEL4A+L71WoHIpXC+vlLfndqsiHIzzCBObW1B9KZpl9F76DToNZ71b7SNLwUTqkf3do9XwwjEHxIH4Jnl7TOo6fn1IrAf/J+DMkYuirEI1haoJxA1unKgS3bx9t1PDlxyHwFlEwFbjZ6xBYsOjBlvcZ+ehen5H3eeI2oqU1HKh+GTrngSVcCn99rP2YMG3wBCe4qssHye9D0tCwPRrpPwoxxBOU+JZgh3LxCNCB4x+IwAvfB8UfiSi3Cyt+ZImysoZSCTP7I7ZLKKcLO6tnBNoOxtxQC6y0hhv+yAbyKcClhsXZHdT9ht83tbK7Lr/fYKjuk+ZvT+/ZYri+dwp3vxmm0P+4nRswfS/DbwNla9h/a7puEN9a1TeoXjiU2+8e+UPv8Hb3w6dXmGvA89MAZBHC/ru/TdZPd3GgHt+aXEgBZo3P5dA+jGEYQUqwqOeDDhHMeN8xGG6H7m39cPH6553xn4X/q8M4AOA4OXFRnGQwirTRKe1OcJQhMNzG4A2ScVHg0BOLZHDPc6cYatO4C8gp6mD2FEoxWDKxHlKMscEGUP4PoP96u/50JwDrBT6hIAVgYxZNWDSwSIuhUZogUYbxPBr3KAL1CCgGIAiHwKHEmDOduhMHcxkcIyxygjsuTgz0Hv3iXaq399783Sr3NPAGM2cSDjLjluVMHRojXYa2KAcQqE04AJJ3aQKgE4bwplNAwv0fWx+WGQx3V3xwWtgqwqalGfj89rD04IgUCVcuyVJk7x9uzOwtCqdtLbBHBQWOE4/aEkZuRDHF7neWVGfUbpac9VaOa8P2OaXTlmi1NYLRQqZNf8MSuKgmgneSpj0/WYcnzquOGV+R3LY7jWw5OaiTPgVCeFllDL/eo5fQOh1R3ArVNtOsyUa58pax28id0szUJqGdqsH3So1Raeg6k9FotD8wRW6Ck7zqd+ddFgeKjBmWFNWa3MdOIjlSzASpM3VHBnW8GGZWnujeKQvNxLDCWGDHC9PovUQzvipv6iTfc5ONHxG7dc/X13WYVNqVUrXOU9MJ7qk7hgKquU8L+Ht85frq6ie5oeWCMJbN6qDba1Q4hSjWEWfewNKtPL4KZZ6vE6xoeyvcWg5R0KZMOHokLayTv82V08y/9NPJpufLiWPSS/2qdLwPOCpO9AN6tA5OmKCJMxP2lGQauVkamyjeB83ejsB560wxaWGO97RJLUKjkaf8JdLj4zn3Jpw8sqsVezKnorB2pnWmyZGyHBmXQJMlN8XMxC5ST271NUWsVtWMNdOWIIxVRGO6wo8mR5gZbbtYKUJUrWvPSdcYL5kSPj5l9v7strswW7sG1jtqd+WdLc4W9kajsIA55YddsNkfsGKvbGLPtn3Ns5pdtyhYsAyB0u1FizyflZ07dVm8iOmYpPv+RNXAZTuDkCWs76gJPd4mV7yIpFMFVA07Ek0oFuZoepgZ4wCXyXDOCzRqahnN88AqToKr5qQP3L2BO9w+UcuzRxzX51WaTzPA7PW8u2pj3F3YrdHgS74ScZlZLxdkEDBOF+zjiwddcsz0GHbqqrOVot7clmhZkguy7KtTFIjJNmbW182FitWLGYsXK5Yu9sQ5UeJkROAXRj+Q3Irqg7EwH7G80OTmKWPPmIdzS3SUHlS0HV9H8+yw1GvGoQ4nVa5WFq1YcXRSt9VuUUwszFzx0VUtRA07mO22C4pFnhzGRl2N0i1tJxOjyDiv1ztMpOZpulO2lSJFVZzIp61lz7B5pF/2xCycbXx7ZaRi32nBjjlvQpbUKLPbtGKRSOt8AkGqlLPiKKsLOT2tmtnCXh76dLkTN6mSTCMiqFbThR028yW+KFpXd/xzmWhkGlUuf+jsYIaN1I4iokzvy804HreX3CfJehklDHEF2tEmgjVJ7Hl84882elGRsakZm+UyGh8VAUXnlwBjQ/Z8AP5JTcjLdjLu+mRWnoWQC8nrWj538Yw5ZsK1NaZaMDp0vNyAYMq13mrHOaSlSxer6FshMY8NJmFxSRsms7mM13QQLOtV5KyBQCz8GFujh0vD16htbkMQNuv1TtrnTVv5E9nH+OA0WR4wPurjdX0Ctr6C5MdozsMysklUIgrRi67j+nq0jXI/1/PLtVjT2nGaYrpqO9k1vJaRzW5OncS5YhwQ4Ii6ebyJdOK4QvetuUtsq+PEdC9jVyVQ6VySJpyyd6MiYq2lDHpmbJ5PAXrEJyMxiTN1EaJTj5pGc2Fez6O2pCIpSX21Vo+HmVdGdRKYlULNw2XVMkeHGJvBQu3C8azzVUDOwtXVXEAJTitq3vveIpopykgiJOPYh4d07iglKVyOfqdNMLuJC9RXo4mKu85YFq7hoo939RG34m4MrvmxDaxVxY0rI3b2+Dn158VeFD1ltmwMQRnPan+xD1neUTY6MXWiUtRk7cIZksfXHZGdM3Kh+kuAZjBagiDfbmZGpR8ASfXKkpuwekb4krfhqNW5U1ftnggaopEAF3EWdqhktsgPy8JN83Psppa11IUThjE1LqH05mBPJ+JqGe7RemfS2minn0XZo5h15SY7h+Mu1Ibr5fl4ZG6VsZ3WCnE0liZJk8TE8k5emh7ztGcU4Zxvp0bTBZfItWpPYEqd5dzjwl0f8XN/nrnWYmGvJ/tVsjMFnBxHo2x2dFY7Z3Fg15WllMszTTlqE4Sj2peSgs/n84jINBW98idxiyfp7MoBNtPTmSwqRJteIizLs6lrCGGH7kjcMpPAY5TTlnFDj83AnuV1z8KUxTLm0rWonyNJoZ10FRyM+hqLW0tekeola70N06xX0eQQMllZFMEJZbgahsiMW3HBUa+Y9bHm5qnRu7EqVNmJzebrXAVNkU9HzuIoniScFogVvbmYFekHay0bk0eTckVsXFfeuQoYMtzmG5MmI7mDWoUhzidrWJFJDxfOlbTvNtWWtPwDu0A7knNszzpvZK015m2nqycF21SyjIKTOLYrAeNrjuPEy3BCOD9kmBiJCxYr5IN9mPf9fqZ1/DQ39DgKdtRivZsd4yAKposG31bmdG3LWEyCY4wHLG92rMpPj5PcWZ+PUiDYApFs2Uw4h0m/8/Y81ewN3naEbbZpON0WjBSGCAYbdz+IA6dLSnSlaI2HH0PrmqIYs/GFYH0oDsTEBljMuRtJ36t79DwPrYg/5N1aS9xGs1g9cOjGbC/ndDInhBboiVHsgwOjnBdE1i3qaW9oKb6Iu34h+FXaJSy1j91slLRR3p5r/9DzWdyVprYSgyXQD6vFfGYo28j0KjlgCBmP1X4b50Hs097OGyesNDJGlJuKqFPyZ15hl1I9pVBDmFNGd0mo7HIR0XROEOPeiW3vWvkLXWssn7/OmNwnummoLG2LXCQNiuKEqRb73LkQ6Kg+MaYUuusLY3uudTyeTGG+4K6Nean7kz+T+S3riMLYLqpCMra7zMZm02ofJGYGmkUGPJWiV1srPQvN1p1yK9EwU1fal+dsGQmuuN1D4MSLsibk2ZUuC97SDIm42FF5xA7khQOpejZKzEQTz5/37LFNvU3R6aIg4wsURyUjFGrdKxZc3FGXbdD1HGNEWDlbTcPZ7riPcrY0cnbjn3tqxUyDVcw0BnpSlTZEfa8j8/Ep6s8rTFnHk96G01S31GYpgG4rBtegFmNuXvS8vsZ1MVnpaGokXbuwIzPeaTtDc6WgE7J0JVnolVPQ2g3XCWt3m1WrBfGouiyW3NHyzFilnIJf+8K+pBRMzsHFL9ZoKu0d2KNcl4AKa5dWK3RV6I2m+HS3JLZ9vWgkrFnyZ86mTa1MJv56f9XIfgdqT/GTsRZhZ3KSou5plXc1BGCDr4jpJWksl97tJ6Q5WvubESaaRSJCpzf8qyJI+WTGkhicG5pEyZbrC+x4c8mCg8Q5qwkzZQlH3HPVZIzWZ3Uby3ShOePznlE1tA0EPgzJtBPtQ7XTDbYMdPRo9zM+dPntLJMXPBwX2aaNhEtZpXoUmQaXxxqRz3SJEC/2ojmgatHDet6uF6ezG0v1bGtbUKCTpXRtYpmja0WOOw2WrdM8RxdbIqGO/jLZEbB8NTN9s2Wm6fF0WTPsaFFPUFEZVdzMILGFz88zg+bXF6fPZnEntyetADTgrkQgLBt1Nb1qxszWGFioMXF/SO3LdBXr3HHhTeBsJS1oEWdOeHQY1VlCVBuXddG2lcU69dTpUZ7T9XTFFcDndhXLXASZq5o6Okyjk6+bJA77ghz20LxgsqJStss5S8qzQ0Ru15HJB2gV5tt+xW04zKw3KwxXJ9WRxZzDRuQuZ+y0H22O8xMKDk0hs3miL2D3zo8EqWhlJTWOa1yb6YBh0Z0FumyHX4LVvDuzdXc5HeqeHI243ZkgFPpg0JRf5MWE0+IFNGkYqmYqpXoTzWajgNYmRrMJQBjg5ZUmKJwaMeS42QvkuL6UEaFcDfoAJ40sBHRLbujSozDCOdSksCad2gG2xLWb/uScaH4rzgisz/e8gpJxhJNifNi3m03isXvnbJIdXdppvl2mpXk54dbQVBn9QlvTCS/Lu6zwyIo8XLhtxdrG5hDLRMKgPH1ROYXlz1tan412E4wWD4wHmweeCXcMauXtca3abG/jDG5OGm1TSLsrekrGsa2B7dw6ekvHoQ0wCe3ePZ5RAM7eGKe6Mcna6KXkJfownhoqjTtMTBNLtemEHNfp2sAN15WyGW5llir2qNn4BTUuI0ya8FkxamN3ez1ugBrtpWvBzXbnqmMTVfZQUczGq2bPo8uVPL5Q6jk19x21txUGa+WLQFzQDFdmPkO0QlYpqzzxOqoBxnQSTrkItqrB6WRrBCYIdtcemiBgGSDipTqeLhm+JXDD4OPUOVRtOFXwDqcn3DizI9irny/scecdYa49zTFie1SCVEcTdrzRXAWoglCdx8dKGzdSGSzH5nhEHqf6NPObi4j5QlbCCafJK3feoemp8eTrJsAo+jAPQqkWOSx2CBmrPNCRFZPR+aTd7gFxCYjl3O2Z/lrH6Oi6M7Yzr87NnpLhlAezH6cKdsqGVKdREoh5aXEipOXUraOtqMznyy5XCNkuA7U+xF0Wp27OKmfJdcgyXPqJSftzGy+Xrp/K+ohI12YNu8zRdDbJBLbKGG+xobts1U/x+ZWcgmC3LL2KdXVuH9c2ruAzexkH6HYV1i3HzzBlIpfL0G9x8biO7bEXrXnqfIxWS3qkHXQd9fC5Zx5qvAKA7uijX2ERUU5O0vTg9EJ4pVg3HrWT+DzuDcFZFTHqkftrLY0PrEu7RXRKPLdeMA63FJTCP+7GawhIRi6vQUZNFWXVm/NAPhfVofTsEZlPKHpZ2/58rR03sYZhZ4KjM8a50GtYXChAV+4Fy45WQOj4IaAEMUU3zYzFF4DlfCrHpxk6ay50qYusXCxHggOr28bs1CWUU1mVyejCj3frNtjk1VTekLAjIWx83pZLIq7xEb4aEd04b4LRxOUx2ilRflorHq2TwNLGO3C1J015ck81w0zLg5Ni0qmmRFttouuVwULVPio9NfayZtwq2rkzmCvhnCpPZzr0uJvwRMAl4ux83Zvpljh6tM234GwF06tZFEnRiJfRhmrVFtuwUyES1T02PW1Uxs9Codi3E2KZyY0S1crJph0sPIwvdNjDH6QoQo/r/Rm1dNOWnRunJQdW3EHbpHTKZxp14potEcnVzvYaW3cjhlMn1po1F6uzQi/RGuQL5jwngTInq4s15fhJMInmR5k3ucX0gPurHsyVcB2M8qozMLbPe4M7nkb8/DQPj8xaiRUslVpJddtUOKCV1Ei0yI296WLl8KmznvIMb2ajK2cdilrl1bKtaFgUYnfUxyem3bC75bQQI1eIznGFZ1Q4xbiNOQbcsqeLBMx7Lj205HQ28uE03CiHGM5cSgQCkXObkF14zALmhSgikhRPrtpySYdn5TiZq4VHq0vh5O56an5VDeqMjdZbln16frq93316xVAKx5+fhncAj5P8v3QO7Pdh/vYgRdA48/z0/+6Q8n5g+P6W73asDyz39cb99S9I+evzU+GEUKL70XEZ1/7jYPKfDmI//9vT4WF7d39DPbyOvFbvb0Eqy7+dXoepC3cU3VuZxfXt7BoiXZfD36iUb49XCE83tZL89j7inSO8zgoXSl9lbw68+TT8/cjwfg2ytSrw+Oo/jvnhxg6aK3TKN4KavIEiH7R8vGoajmuHd01Pv/8PiO/K9IwnAAA= -->
