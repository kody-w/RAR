---
name: "rar-cowork-cookbook-dashboard-correct-supplier-payments"
description: "Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_supplier_payments", "rar_sha256": "eaca80d1745b07b88a4c738b3ebff2a3157893b74f4c5cbfc4d5ca66794ee686", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_supplier_payments_agent.py` and in the RCI capsule.

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

Correct supplier payments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 eaca80d1745b07b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_supplier_payments_agent.py` first:

```bash
python3 dashboard_correct_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_supplier_payments_agent.py   # or on stdin
python3 dashboard_correct_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct supplier payments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_supplier_payments',
    "version": '2.0.0',
    "display_name": 'Correct supplier payments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f38a4c99ce6cf5f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/correct-supplier-payments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-correct-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardCorrectSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectSupplierPayments'
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
    print(DashboardCorrectSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZPi1rblX9HL96HKT1WJ5qFuOKKFBEIIEGgEXI6yZgmNaECD2/+9j4DMsq+v37vu6A9NRVYidLTnvdY+h/z1xW6bqKhevrxovp1Dop2mceRXkJ17EF90RZWAX0XigB/ILfKmip22Kar65dOL59duFZdNXOTg8X1VeK3r15AN1X4afJ4W23Hue1CcN35lu01886GVvt1Anl1HTmFXHhQUFZBaVb7bQHVblmkMVJf2kPl5U0OfoaL08xoIAOYMkFMVXe1Xn6C8gAScIiHbBfpqKPd9D6hxBqiJfOgW+51fvQL7/N7OytSvX7789POnlxi8f/ny64ub2jX46EV4M4J/6Nee6vdP7UBAauchWFkOIEI5uC79ChicgY88P4CeVx8nbz9B//VfSWdXYf3Dl6859Hx9fZn+qW1+N6wp7LoBdrp2aTtxGjfDK8SlnT3UUOU3bZXfQwcCnIevjye/SypK6Mfp3seHktfQbz5+fQHRqewp/F9ffoBAJL++VO30/nWSUn784TUtQCg+/vBdTt06lynWP95z9Prtef0UCxZ+XxoHd60/AqmPRDv+15ffOTe9HnZPfoInX14vRZx/fAguq+Lm53bu+h9/+CuxbuS7SRrXzb8l96eH4Mi3PeDT0/AfPt2D/DMEPx16l/nXakuQ1r/jCVj+pu4T9AzUX8m+x/+fRKegCer3iP9Lcf/qAfhH6Ke/9O2/e+ATFHx9EfwUtFtlO6n/Bfr1m7Zf8D998L5/+OHn34Do/1GMVrSVe5fwLbPzOPDr5tu3nz7U948//PzTh7YEtebb2be2Sv+VzH8V17ueP0TwuerjH58F+o08yYsuh94rHfq1KP+j+u0VMu009r5/Xn+Bft8v0wuGJifelD5C8LueqYGtv4vjDy+/AYzIgTete78Nuvw//xPaxm5V1EXQQJpbtA0EEtzEmT8Zr0cxgKb63tuVD+JaxyCwz3Wg/qcMTxYXAfTL/3LvUApA8QGls3cI/PaEv29v8PftDf5+eYV0ILqo4jDO7RRSuf3+a26H4N6ktqx8AIa3O/A1/mcARZ+nNxNY/vJvSP92F/RaDr/coT5+YJTKSxM+1W3qv04+WpGfPz1yATv4ve+2QEdauMCgIAbg+gn4XhcpgPZmikedxGkKefGktKiGu2wQsy+TsF9++cUBhn3NH4CKQw/6qGdgwbs50OfPwLMgjcOo+Zr7blRAH3797QP0v6H/7qm78EnHHoD7MyPAwrWm7CDQYe2DT6b0Avi4Z+TX357xBWJyQDogf3EQ+4+HQYUmvvcWbG3FfcZICnJ8EGQQ4KwsqgagNBQ3r5AUQO/2AqXTrQnHo6JuIM8H9OX5uTsxkw3ceY9kXgC+A2VYB8MnqK39u9ZfnMq+m5iBVrebX6AtvwesUaTgv8nM+yLwcJHHIPzvpfD4HAipPtTQ/E3EK7SbahKQaWWXUWU/dQT2Iy+ALd4eB8JtwKHd13yiSH8K1b1BHuEBi0Bk3GdKP085B4ydATTw6jfd9zX2xG36neOqr3n9LH67mlLhAjIASsM29iZK+MezpOqoaFPvHj9g6Z28H1nwnlm51yD/l/OB9M+DxTunQ19bDEEJ6P+zoWRyhxNFdSFy+kKAFjtdPT3CPBk2peMxjYHZ4G7FvaW+zwtvaPMGul/zNAY1Uw3/eKy8J+e55gFkbQVsUDkVenO8usu9F+5UiFU1lbz9NX9D908gUncoA7kDXQ66YCq+N4XT3TdLIxCv6fo7098TDeIHSgMUJ1S2TgoKJwCBcGw3AVZVU/M9MwOq2J8asYtiN/qDVxCQDooFyIeAETEIOWCAe+h2BXAT9F1QFdn35fE0P5WPRHsQmF39V8gC/TPVUA2aFgxB0xoQhQ93UVDmgxgDE98jXEd2+TBmGnefBtpTLooMlPXvM/C8+b3i77ZM5gOptmc3IJbdBMKe3z8y+27nM1fA2Gzq0ftDf0z301fo9zT0j6/53cZ33Aetn04M/rvgQKCUs/qOtRNy1QB9Mv9ZQKAS7mT9+uDbB6G/2/LlTzP+x7+3DbgzqPHHzH2BoqYp6y+z2YP13kjvFeDGDNRIXPr1dwL8/Gy1z2+t9vmt1f4g+hGpL9DfM+8PIp51/QVCX5FXZLq1iV1/KtznC0SD/zw/fSamu19z1f+e5mctTMCbDlNXv7HQ2xJARWHlh9PiByvVE5l1gD/vMAwS8TV/L4VnowCUz8OJQuvidw18p2OQ2Efe3tkC3MoboNubRrjQnzY46WR+7b98yds0/fSS25n/721sJlIA9QriMe2IQO+AoaiJ/fvV+4A0Xfxxi3fvKgAHXvFlaq5P0DTMfoLe59JP0NtO4b79yluwVfppmoknlWAp+PW+9n3/6PgvYHfWDOVk+2P7M41izxH5z0ZMPQUsvoPsRF3PJp00/kkIeBOGfvVnIcr9jZ0+kaJu7Im24+atv2tgpweGoE8QyB7oO9BKACFb8MCf1QA9lX9tAT96k7vf4/fdreLhy2/3MDSPPeSvL2+I8czBc14Ey0Frfq4nhpyBSgUKwfWjpsC9/5tJ8ikCwBwYY4AM33ZtBvFQmiAdhHYYxiZcGmcc3HeCALNxlKQZFndoIiBc0nUCl/BI16YomiV8n2IoIO9RnN+mSSCezMJs22VcGiU8lrYp18cRB3d9FEM9GvcRksUDhvEJEKH3RxOAkU9fH75NgXwfaqeYPF3+9cWhCLByRdQS93jxM9a06ePG2UUOW1EB5+YzyYkNSj/fWrPJa3RluTtht8sqccTgjBBjUjpE62uccRxS0BZBJrC6hjud3uREoSTyLl231XbEiEEfOLVzj4vZeEGO5lxdFr2SNm50PZfXq3zVD5UiO40WVR1KGY3HMVfYMk87GPaDxPOZaienpkvCA37EybSij3KGdKe+TNTeku2rs8nq6EAmjLL0naYrdH1DN30/pIdUC7fzy9p10qxEnZPm10u5L0l2Bp8uvbCvz2Z4VU9kg3Tw1TwtPe3I1d4FcVYjCQe5TsyCfE+lawz28z12Ykb/tL4YYS6IGX5NG7nDzcKj1gd8429N3fK4cbYA5VFXhnUT0OuaL8m8GrEF6g4LeSGfL4fzyroUrnBm1GRTsmerkvsLe5XFk4yklmUj5NV0+eVuf5KNqjihxlprDK/Izca64gUrhmR3xYqGqSqbXAxus90uo013tJlx4RH4VVuOu5DfJRHphZknbZdkudTSk1jNq9QdLAzzIkQc8HJez0Mj0WWs1chLnbobcohNx94c23WrJFaqKzc9dXgNjdlakVGkw90FceVzc+fiAlOrxwUaytho+M3JxWQTIfRSgxu7HOuKtZlljlUIE2ndKiJyIF4TW4kYsxsMkNyM2ZFxSbJujnul8+QqW1IkeW7YWaGfKnNcMn27KuDayfu1WTn+prv6XSV6qnqJvQyXkF18uQlqXXoO33c1U/VXjzfjXX3c07VpJn1CGXv/ujZKt5xVsuAyyw0b9Y62u+y1qFekk1dlrlRjUc+TFxgLdPNypa/tqIyFvNlutjTTjo1O8fNFJGOigtWaDV81O7r/6FcNP4ug/vcGRdw6N+guK8TaE2FwUg50dshkI2BW6SU+B7f9heXq7aUmFyQ63oIktXBUuGbJuLlezquTUfEpUjfp5UDWOjG4jjmXxe0pIyVBzRAOlnTJrHqXvyjzM16SGgDPYCzxzkXT64HDRL6snDUipMFBc4qOC67bhFcze61067bPVUmT9Uqd28ipX2ZpYKJyOUbz3WoxTu105Kh9VJFkWTILPL8wOi11OaxJ0qxPKbEZtLVvxJiwZUfbvvIOKXc9PJuTqG25SweDZ0MgHZ0DkhipHES9q+YWivdlvS9jQe6LBS86vRzHhaHs19jg7sLzasef5sV60bJcF6CouctnG+UsjrUU2+VSzzarNB6rhdEuzseIHSwePd2UHc5r42Lgk+HMm7BCosNFmMlHTRxL3UGwivFacTEj0p3Vr92e27jxckmNboNfzhpPKhJTlMoum7G8tc8HwTWWeOEHBt77Z3WQRuW4W4sBnLnXkSbhXumDWxUmraHB6J7li3jee7KRwke+MjYXw886XcDyJLKRiMczzDz0aMrip5NeLsdMOy62aEpYWnbR+uHQuG5JNZccraw+FfzyXGxCwRmZYNg5tZaIsy2c6AdkddUdf+X56Wg6rrPLz9ftJsvD/bA/HedBnZRZbDUKISSr4AbfvBvcr0633F+tqjmDhltLoZKwERzlEIo5S3S5pM3x2Vm87Or9nNzO+4xDmaWlSPuNYgOEE7fH9dBVNJlYCz1jhvOQ4cltNfbryklkVe0sWMuvcYdtmYMrr888w+0Edl6STMZwKsYtzHC4rQ56mMw1Ld5tD7F8akgR7T32kLhc02VLx2hcVeJoObuGaC+JHk5W3Ny4HPh2221O1kZmj3MLFmcuwzLaoawMuEa42/rktwSpNLeeSuen696Wx1WO40SrI2iQlPFBXxmJE1frW7AmzQTdD57cmJTKyH4rr4UVcSQZlxHFleO4cIepS36xEeiZPGNiGL5W+mo4b1SimbWS0GuwbFUaKrMzcxdrnLHhLqUuI7572khdmJOWFNWUXezg/XlzDa3V1sDny46v7DDe5xeCDPR5AeeCOqoX3NMTXFIVZL5zJNVKc5XifK4I80g6KCAf7QJGjCQ05JBpGdtHi1s3N3NvvEqbWi9WglYI16VgbnduiPnJqfeOKr6vqcYaMiVJOaGvdvM0WF1Y2x40b28WF1uQUepmi5GTdTOeQ8K+XmtkugCMShfnM+gXq2CbpbW8iLyCrnGcZdfJeNCFuHexk0VtAP2RZBjLatFtzCaV1eYWOLOVw9PRItLsFu+DJhn51TJl9lu0Hhfd3t2tbKtKKj/q0+WR26yNkFLq0aHEEgbDRMZr9Do3ypLMYsFc0SyDHdImX6TG2tQAsW4MVdSkw1bcZFSEwqDFCL5dVmvrapZbfiVxW78bJFpY0+tjxfM7zMKYm3SgDkV6XUtLXolI3Fe12t5x9ok+Ka58vcQ2fAz2DRmY8tI5LFWcjLlhtkZzJ+5QDOBw6S/I3aY1ztXhRmNn2l4IQXE5VmipLQeMCS2iOfupzjOpblqbLFqCABTU8pQruESKUhd7mGNYqoDgNL5Q1o1vIpcjHUWEh5CK6q/99TU73Trd3YSaM4qqVOxZwx5PvknOR3VzjlFlrW3mRq1ZRnFgwl18PXIH+3ZNeh8XnJhmCy3px8OcLmcsNkdvXMBKANgVlSdJmzuOIXMl8pWj2eP1ACPnASDABYMlbLakBSLRPfuwG/yoifBLGCvV6UwgbUMiHWYFOVYyNY7AdURtjwvKtmZObtunQkvFizQfb37RLubhfLvUuHqxyh0wyUqEpp8CfO6WZiRapb9fVMqRhH1D2Y5kVCw2xVyzd6fyqGE3dzYn4khb7KxSRY7LdNPOCY/O+FQplw6611plsTFM/nisGqPGj4johYIgOd0xWFT8ib9kR55yjO21F8x1jsZzfnTNw4kmI6scZJg7KQ7fJlKPpKc1MshHdr0jojWKtgbG7pWwxQE6ksVezcfLHFOuKTGesLSlBH1+tAoNluJG3xobZAWYkNnXhinry16SGjaRdK6SsyEuREoTEs9SBrsvbTBaefjSrA9jAojsIgiMmyTNIiToxnYQEtNMrs5PyC47a81yeTTTtRqTm+Ml3jDLc0BZelCOShRoJk8iqzbET0qA52elsjnM6m4n9LY0N3HcCWbQztZRdlNzdF5QeWI6axJpK0TeYmucuVoXm6WdgJSs2bZbwxR5lbJTs3AWYEoWVwUVLQhtzuceMqIcfVTFOF07Xm5kYlRllTJXOvXK2mMQkSJ8XpxwMGbN0AvC5sf5orDXG77aRM35hJYHfjA3erTnlta5MzjxMhzSuEEuK/5wzQasWR7U0lhngLISVGpdvrnxjaPDMxGJaemmZnPsqBDiXL2ki3la0I5orx0MvRXZYc0gtOTJXDg6RRlzx/PNnA0as5DQFTI0JViMyMQAOjMcSYTYqbaUcAUrp6fSVDOd22Z9Jsipg146a8tIxIwkV4lchxvt1lzWWMlft3RwjBbFYeSiWZVHag+PLl75CI+j6AKeFU0xb0VrHqUMSd4uQTiz0QggIrLUgkJtDj3nNTPkOksuW047iqM6mEqzSYyztA0pgXO3QtKBvUPIrdWTlduIvBR2CYHIpoYoOe4i2fxG5HxfcqjhjzKovtBRLjrL2txyO3TF0ZDyoXd9IUKGaG4MkqzPWjHWVQzlfdSYy75xWGKoI4Mt2wI/tL4/c3CMVOBQpnxYTc7qUtGI+oKWPElU5OEQFoHho5vxdCxmTeXGLN8Mt1u7x2U99HHTOjq0ffWqyLcJc98U7mqH6axMDxvaXZGucrQCLwpPFlu3WxrMYXNAyNgmxm13iB1vGVcVKcaD0u1btXYMuqGzMtxntdXa2BVfs/0JW6g+maULVycuMdEwVhW7IB3G7oguMIqABRYV0tUh67rdbT6TCIplNnB11dpF20twhZknlxUbvKlpcbZz83pE05KgtqM/NHUrzZvtfoy3Dbxxe4/E6jml7Pn9jPa8gOEU2bT4lHFmsHQkKcvHWDrPMVK3qLW33zhX+ZYiHLNbHFbJGd4EoeUFmOGkTIyas5OuFG4t5sIoowQScX2HFQt9le0pzjj4Sd5eQLKzAD2tIvS2IbdykysYIa4Eh9rJu0t42jfw/Lo+hkpEl6PvovSQJsa6Pro8n43xnhKNvL/AgbDkZDpvqIUw7BlfCDxPFUW192lyc9gEm+rWyLB+0xRq2EknBFNCfafkdKUwmCvMk+KW1jZP2Wx7WNs4hthjbh9JewfvZlTfIxcyMj2jn3HbaL5kK0F3qL1Q+Lg7W1NnftNiN8dZWdvDqpLR+lzZMJtSPt2DzdOhbpn9Wrz5CpF5t9x1GibOkJi/cXqDF9boZTktSur2aAsLNMkRo5E3mAS32Z6kWK481LyvmLZ/k/CzcFxcN6in7Det4Ik8Q6rb1T461ERnIbXLUnPmvKbluj0TGX2ptpt8VctovKb08yjEeDUYs33YucrKVQdaQA8rI8tKp2I2TWvN1WO7yA4Fs8j0ZgwBT47VNqKWMeszuSlH7QGpYhJlF32fewcvPFIytaSDvA1r/KyDDX6+N7Vxi23J2w42NuebkTvFhSEOx6ZmumoWZgosUtjFWV88h2LOLJHIkotzaKYIN1ZfYoogWIi0CPSsE/k+ULXAG/CGPI/L694LXMHgCXsjAFhrd9jBZgM8tcktguIe7TXqoRFu5/rKI+7RIla+0BJrpptziJqyR3Bt5m6uhuphX59mMpr4zUJSBCS4aWfVM2gsTHvb16racyJuTxwIEl6B3XJwrmZpRld7YPeORAnNgEVGW/k0RXtyRKoi69Pz+uhTIjrTkZOPs2Aebeib0d4MtvfQbO+Q4kjvg+J2IxeqAJusQAfnJtAbnjnr5ByN+Ks010lDxS3sNBtoEb9ebPU0WFWVVzfuCldsEkRXe35ayge4qohBc+m5KjZWdcGxlR/5Zu8yBN6fq8VtxuLpCjeJw0m7ennKXZAtvS84saC2C9cW21jf48rmcDGolT/PpTOVITMfy+g1tQg0xuJqDniE7kuGPaxpZdURJtk7Bkrk9MiOnNid+HZRdk0TetlMNEVTYHUnKYt57iVV0g1MhXWrBKZMj/cq7Nha/nhRpLyyccvDuh08IzmNGBXYJDbEaac2cYLcjsyxO5Ktg1usINNsLutjeAqzHWmpMtXMVxsn1dF1h/KswfrDpqed7CSMSnbkGGbe1rl622yP6Txat2ESnWT3xjPLwFtE53WR4tkNgXt3SdNYohCkoNIGuT+KhHe5EYIhmweclEqO4358+fQynUU/T5T/ztfJ0wHf/7NzxseR4Nv3S/fDZN/2vtx1fflbVv386QVwE7DpcaJap234PHz8p/PUz//GFxOTgOHxPe30ZVjfvJ3AN3Y4/bXRS5x7bd1Uw7e6SNv7oe6nF6etp797qL89D69f7q5l5f0k/E3n9+PRppi8eJn+JmH6dsf3Yrvxn5fh84AZPDiAFAG++4ZT5De/Kic/n19zTIey0/ccL7/9HytzjcfkJQAA -->
