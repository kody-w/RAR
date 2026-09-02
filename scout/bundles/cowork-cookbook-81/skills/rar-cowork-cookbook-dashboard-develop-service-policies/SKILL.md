---
name: "rar-cowork-cookbook-dashboard-develop-service-policies"
description: "Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_service_policies", "rar_sha256": "ecfc750ef31aac30fff2fe352eda8d833e3745292f5539797cf454b66e30d557", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_service_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-service-policies:80fb8e0b13ba670d025c336e94b573dc9e69ffab25394fc8e10bd22d9eb334b9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_service_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_service_policies_agent.py` is
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

Develop service policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 ecfc750ef31aac30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_service_policies_agent.py` first:

```bash
python3 dashboard_develop_service_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_service_policies_agent.py   # or on stdin
python3 dashboard_develop_service_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_service_policies',
    "version": '2.0.0',
    "display_name": 'Develop service policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-service-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-service-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55ec86ed89e4face',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-service-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopServicePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopServicePolicies'
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
    print(DashboardDevelopServicePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81aaZOi2Jr+K0zOh+oeslL2JW90xCggiooKCkJXRxbLQXaQVe3p/z4HNbOqb9+ee3tiPowVlalyzrs87/K8B/LXJ6dtwqJ6en3SgZMjspOmUQgqxMl9RCj6okrgryJx4X/EK/Kmity2Kar66fnJB7VXRWUTFTncvqkKv/VAjThIDdLg87DYiXLgI1HegMrxmqgDyGy3WiK+U4du4VQ+EhQV4oMOpEUJd1Vd5AGkLNLIi6Cgz0hRgryG+6E1F8Stih6ueUbyAhFJhkYcD6qrkRwAH2pxL0gTAqSLQA+qF2geODtZmYL66fXnX56fIvj+6fXXJy91avjVk/hug3hXr9+1bx7K4f7UyY9wYXmB+OTwcwkqaG4Gv/JBgDw+/TD4+oz8x38kvVMd6x9fv+TI4/XlafintfnNrqZw6gaa6Tml40Zp1FxekHHaO5caqUDTVvkNOAhvfny57/wmCYLz03Dth7uSlyNofvjyBMGpnAH8L08/IhDHL09VO7x/GaSUP/z4khYQiR9+/Canbt0YeM0gDFr98vb4/BALF35bGgU3rT9Bqfcwu+DL03fODa+73YOfcOfTS1xE+Q93wWVVdCB3cg/88OOfifVC4CVpVDf/ktyf74JD4PjQp4fhPz7fQP4FQR8Ofcj8c7UlDOtf8QQuf1f3jDyA+jPZN/z/TnQKS6D+QPwfivtHG9CfkJ//1Lf/acMzEnx5EkEKi61y3BS8Ir++6RtJ+PmT/+3LT7/8BkX/UzF60VbeTcJb5uRRAOrm7e3nT/Xt60+//PypLWGuASd7a6v0H8n8R7je9PwOwceqH36/F+rf50le9DnykenIr0X5b9VvL4jhpJH/7fv6Ffm+XoYXigxOvCu9Q/BdzdTQ1u9w/PHpN9gicuhN690uwyr/939HVpFXFXURNIjuFW2DwAA3UQYG43dhVCO7R1F/1Rfz5fIl878i8Nuh3GGLcNq0QeTKiVIE1sMQ8cGDIkC+/qd3a6ywRd4b6+ijIb49muHboxm+vTfDry/ILoSKiyo6RrmTItp4s0GcI8ibQeUtOeo2+9wNWm8992aGJsyHjlO3Kfgb8vWfq3m7SXwpL4MjX3IYmXsLb0BWFpVTRekFcYZO5V4a8Bl2WNhNqiJNXcdLkOFHW74M6JghyB+YeZBVwBl4bQOQtPCg6UEEu/IzDHtdpJASmgHJOonSFPGjCsJUVJcb/UC0XwdhX79+daHlX/J7KyaRO+3UI7jgw2Dk8+eyAkEaHcPmSw68sEA+/frbJ+S/kP9p1034oGMDWeGGGEznFFH0tYrA2mwzuGwgIBhlx7/F7tff7qEYrMshT8KKioKBrZohPN8lwuDBPT7vwYE+DyaC6qHp97ghfQhxQaIGogWrvH7+kg8iCri06qMavIN433yH/j3adz1DTOoHhjBOQVVkt7W3HByC6RWV/4LMA+QDKegujGszRDQs6gamLWRcH+TeQKZO8y2EedEgNaycOrg8I20NXR0kf3Wh6AGcDLYnp/mKrIQNZLoihT8GgG7q4e4ij4bAP9L1/jUUUn2COTZ5F/GCqDArK6R0KqcMK6cGt3WBc88IyHDv+6FwB9J+jwykDoYY3Wr6lnnin00T87+fQj4mAORLS2A4hfz/mmAGZ8ayrEnyeCeJiKTuNOueeYNdAxD3yQ1OEjcjbmX0bbp4b0TvLfpLnkYwWtXlb/eVwS3Z7mvuba+toA3aWEPe/a5ucqMGpsyQA1U1uOR8yd+54BkCBQNWD20NVnYy9IniQ+Fw9d3SEMI1fP42FyD3bByqBOY5UrYuhAwJIBC3kmjCaii4R2Bg/oCh+GCFeOHvvEKgdJgbUD4CjYhgIkO+uEGnwsKBs9S9Cj6WR8O0Vd7j7COwssALYg6JDpO1RlwYxX5YA1H4dBOFZABiDE38QLgOnfJuzDAaPwx0hlgUmdOA7yPwuAiTdiAdqO+jIqFUx3caiGUPgwAL7nyP7Iedj1hBY7OhOm6bfh/uh6/I96T1t6EqoY3faAFO8wPffwcObOVVVt+6E2TipIZ1n4FHAsFMuFH7y52d7/T/YcvrH84DP/y1I8ONb/e/j9wrEjZNWb+ORndOfKfEF6/IRjBHohLU3+jx86PSPj8q7fN7pf1O8h2oV+SvWfc7EY+0fkXwF+wFGy4tobohbx8vCIbweWJ9poarX3INfIvyIxWGjge7MCzqd+J5XwLZ51iB47D4TkT1wF89pMxb/7sRyUcmPOoEttf8OLBmXXxXv4NPQ1zvYfvo0/BSPjCAP8x7RzAchtLB/Bo8veZtmj4/5U4G/qVD0NCMYbZCOIbDE6wcOEA1wyX46WOYGj78/jB4qynYDPzidSgtSHxw8H1GPmbYZ+T9VHE7qeUtPFb9PMzPg0q4FP76WPtx0nTBEzzINZdyMP1+VBrGtsc4/UcjhoqCFt9a7EAZjxIdNP5BCHxzPILqj0LWtzdO+ugTdeMMdAlZ+lHdNbTTh+PVMwIhhFUHCwn2xxZu+KMaqKcCpxYStD+4+w2/b24Vd19+u8HQ3M+bvz6994vh/X1auCfOcBb912e6AdR3Ln4bRDuDgNvkdcP4NrG+Qf+igXO/u3QcBoi3eyY+vcJ2A56fBiSrCI7h19sJ++luD3Tk26wLJcDG8bkeZogRLCQoCTJ7OTiRwKb3nYLh68i/rR/evP75gPynHeCVwwKXA5iLk67DsJiPEbRHkgzgKZdmSd/jAcMHgeMSNMlTgccBHHN9gvB54JIk5fLQjCGWmfMwY4QPUYAOfED9vxjbn+4SIGkQNANFAC/wWBoDAYk7jkdiQRAQASBpAvgO53MkCUiWogmeCGhoJsuzXkDRlMswgMR8mmYHeY+x8W7W2/uI/h6Xeyt4g+0ziwajCaiH81ic8nnWYTwoxyU9gBO4z5IAo3ky4DhAwf0fWx+xGUJ393zIWzgxDr4Nen59xHrIRYaCK2dUPR/fX8KINxzWZF0tdPmKAZZ9GM3dyDyxrj01+KRm4nItnybK+NqyGpAWrDL2dEPdzWRHbhYrXNxsQ7TQ+CTGyU0SLZKSwKLeJI72Zp4rCeuj7KwF3nq6P2jMPKOmhXnKJjPGzBzBcE7bTNPljc5XxSE1L0Q36fKcp9KOCJUGP1XxmjDR0WhVAsfekzKwz0uBMDHsYqg2SC9K4i3rqxvu29Q8sEGYrrNFKjmVDDhyqexP526VuRO91v3RCCjXc6zWNn4stTntYxFR4ZTi66QU+2Lv5Lsz6+cswa53OKGpBN8tcXTLnQGFh1hy2qtAVTvDdvC0rbYVYYaZyVEniM8kRed4qtpm0aCyvb9MtWt3IBMlotO5N9/v5OjSNtMttbkm+dwQnUtj4vGUPSTrHs+3YNNU/T5ipifd67HqsNVOJ32qn9i+LZ3G7zRHnVxFY6OxtGHizDJRwCXWHPu4Ttlsfj13+zRaLk1ZTGX/gI0TPZfUhbE9ZWl7zpbuBr/miaWs6+Zi2tut6lIs40gXgzrlC96rHcPMCOqyO5VT2r24NXvYzjM3qMhc9cebvNyIvuiRE87zTUmt54RoBY1l4Q5O0TtbR+tTea6rkcNNK6zaU/Gin8XUARKWIDRzi827tRPLeMRfV4ZLc6m5QTlvscwmjI27fkNWOyo2rinWt2SC1VV1nhq5DSquAONq5od2KKitOt+rcTxaLurlwREmXMctzydfsI+qZ7XsyjeTXcIagVOUWOmXQbyMI0pa8snVFabh5tKc1/O9V2X7RU2EV1HJR+TmYOQLsmrj5ZXQL1fhuh4ta3ZvF848UfZ9fXW6Mmby2/9IztFi4cfArXk0N1N0IoIVhUY7dL3h3HnDR8ttsxsd9em6xGGabrDVkVGvWJCbAEd1zAX7Vnd39alSl9JZQeVTeraKTOHtqXJiiEjerix8fRkxMd5x6Mxdkct0N96tF86hzLeedwqu0+rspacymyRqGjv41VIU0Fu1lsjoXhGmk4Ta8nblxetES+p4Hy3o01XfrGEClLgdh2d1NosVn5vHc2bklYw9aXyMTSJufV52caRTFnqeAmmtp9JISddTepngBidjetMdRUK9LKSalYOyGy3Z7VqvTltlg6MHXJD5nRHIzgWdjVe5XOxmaiyfnHW8ovrELSlyIli4MpadRLiS4hnDDYwBXH0+uhMsMISKqhZSXJx2B1Vrt7qnpejhMvW64MwJ15FyFbaUGymYatBUs1uuDpeML60NjlfaqSMSamxOdJ2QNjF9BapggnCcOp2cJdPI0uid6bu8xEx1d5MclH4sEpvuNN/mzsG7rK7pDuh5kIg4YYBttiGTC9bqOqOtRpp6mbgZzGGy8ZM2uDL0TO3AVjdYa1Ittk7cpfuZp8Qhke0ZTfWPB+0wsdd2U83nkc9dXcPDq9lmWbbWXqXTrG9FtcvPo6XRnhdb1xutdtmuEVlz54EZDy7KecJPLhYBIkGJqXE9wqf9jlEWdmFUh5rkQ9obtbRPnkeeSLDbI21vQDOJlPNewjnXVnoRPx5kfW4Hl0T0L7jsUCnfk2K1mtTyfAUPdyZnu8pcUtY7Pj9srpPaClfMns3U7BxsDhwwN/O94BYdZyiHqV8w8zFn6MKMPEYqddwFlMqNo1U/r8LGWk1mylyQYG/tGwEL3b5hC8aZyNREbNaLtpQsZy+axnKfiu1udQ17dDsvZVSx6fn+vDpp7FrogApQ2t3uo51ZefZYjRcUH9T+CjQ1q20Z67pedx2Bgty+UPVVOmbr0rpKpuuPdkKlnDapaziVmhdb0dqbs7w40JzHydLMPXho326nghRsGPqyZLltqwWjBOeaVre5+SyaYvuGak6GS9SuVI9zQpF02S842tprE0W9tLZm73sR0F1rmflkT54nveDqTk17xzqMbVXc06o+g/bPT8pCSBydRHeFPNpzShCinMRbqXmK7XhxxODcUOCiL6CMRCRSvtx0atJzhwnYdm7DqszqMI1n+2ibFttoRVOqQ3FB5ZqHXXlq5u6WPnRTdocJskEeV8Z8lY/d1l5Mj6bPHhyvN4zTinWMcI6HWbMFqG/uSo4ye0c/NITaMq6ya1tLERJzvUh3rpfsnQ16mbR9ym7n26TyqT1LL85HRT8LVL6a1qw0n8wdi/Cr7nQW6Rl9lPtVX4blyjZXa37X4xMeEzNC25Q7F1elNbW23FEZThn9HE5iwdy3rjahMGcfzcRxtEwqsInoOeiLUEDNxdTRrRAVxPVxFaF93wo2e4UnqVTNnQu27he8ftRD61hoPp5g3dQuZvZVDaeTo75QKjrmzmR2NQqjGRuzKJuLSy4xfXQpHTxgCym1y7GW1nJfuHZ2rjQnc3vgrqJjhZ6fOwYqmofSojt7jBn60Dm2DbMu94qkXNXzSZ3PtBbHC48PLpx2PVnkVFvg6LkCuSbsMDeC4T9lFTZmLr2E1pdcyEKmjPeOJHTK2lHclYyGi4m/TKOt7guhEhdR1SdSwZQrsy1Qtg30WVlvsXF/AaOmDlxxNvJ8340TqwVyMR3NZ8uWtTFMxpiEPmWnYwkPf3rIshwNAByEosuCnmOmNANHZeSqc0qJywsAvAoPI/M2PeBEGYgtnxlJpyRUzpoEi5+9K78y55IttCmP+bB8V+Gx2KoZZDC7acLZ+FKJvFXF83rLZ0uNy6cnVt05OSsf5pvJxNguRrsqPUUGIUa7TaI4vRZhp/WJXU3gWMOmYLuvyMLdF45K9qWQVXuH9k9NuUUnljzuNQF1SKrpPaNQynOb0dLC25O6grtHLMGniayiBSQrIQ4nYtafFGHjl9HY97JkFLnBXLcDmGTM7lrPm/mMaxcBYa+oi78b7pDKG3rZhdjWIE9RG87Z7XWq0xOMPjWSK0u6RAOdEH1bWOsLp2xFe1d4JiAg6zomsHRzitcavhdAGG8EblEb/r6gWFV3sHK04w3bXcfNbgFkJjV3yanVp3UfdrxtrPlkxUi8dph3W0CLdEFzwiFl8FigY9WH46kFJ75TH3ocRVQzx1aCs23DDn911m2CjXAjmshscuWMXdCt/ZLgONWXxzLvS1f/mlihuthaubjZL4/WSvIO1cwQz9vZgtCSZmfuLAKm9ZiW2VAs5OUGpTGL2TeZv9jknNz5GL9StPP21J6OR5mnC9NYLeZSM5U5amfNDHO8mEwmZkIvxtHFZOKFnXTLaSqd9rKuQZj3HH05EY2CNx3LufrcixrZym2NPVpTdL3fyiBuartKO1dHY3ucX3d1iDELx90Zq+3cVdgOnRyOoVyghFav+BkISQGSrDQLQDw+uYZ0nIrFnp0uTt7FmmT6qre1CnCocCZDedZtFK7X6ol75lsb4HPjkLsnTkl1wZIC2uOYBQTX5D0iOaBtkZHNIh37GN6v5m0ebDhrJbIRpwoVOBK7RkhPi9WkOcrpgUts2D4oYrHYlXjpRztlnMz2lhgevWxcXbzx1FwKPWOe94Vdx3Kol4cwYdgcI+qjUy/lRDQ0Fk5ea3RSM6pG4sl4f10Kob+NguUUp9az3UKaBvNjtUEpR1FnDqewxlYqaW18cI26ImPO94UpxdJdsJRYJqrKipa0VNqfl9FpY+ZV7nRJOEFDXmP2nRqDZILVlyUmkAKKUmRQqPAoYtBG5xMl0cqTyt7zRNiDg73Bl92q82F99bTH+IQ8CV3iQl1Pi3ArLZz80C798rJQGuywaLvIWc5HY46Wu2bXEq1DHFHzzNDwnOjl12m81aZu5uzP2iZaixF5dmrlch43Wxzsd45L9kFbeBYrZJOw6Tf05rAHkw3O6wbmE8oG09BOOFpkKzaxdaCrlM8WdROI28wlDB/Hx2oZov7k2oXLbNn5+HGj0fSmY92KHR0nvV71UhUHI3w32sBRLu/8Gr1U8khblGXgaVOmO878IqSoaHMOfCGtRpfKahKzbVkhwEQjway1e+jk41xeC9j84nHnbhtHYp/xmKt5+ytazZm1T7tKadQ0Sa7O/dLVSq32RY1tC9VwuEm/9kFwyTqwr8/hKqoSbZ9Z9kgjpqjqXCivnpjCqB13o83oLKk8jsuWPZ2y9d4fN1zbonVFC7zCVissjHWKkTcYTYGavdr9Staj8+FcLMuKQMVpFbjaUPxBWpAUOapmM32TTX1cn3HSRZIORK1uuqJdh6x/5fIymbekw/v1xDqPnboyz1lTscQhZWuZP6jChe25xOEpNrJb1D+35EWCtbvgpmsShFRDSEHthcnZL+qdqQeaiRWdFcuMPYJsJvhCP5doo2S4iE+alV50BkZxDaVi1vKcSpiHToVrMHH1844sZuckry8XOo+Cdl33qDfpK3OVl9N4tV6C7hxzo9ksJynnzM7Y7Wx/TG234PPmaJ5py5cE6+SNo61/aHfuhCpWaiQLpTkiaSEEBWELGjrKDCxpJDWcESIbVlbeci1hLX27YdemPprCsBU1OM7soI5sa8Qz42vYeHU82rTq+cBQcW43XtVe3abPl8WW0nggCgEdzYjNbEys1FkQo2fZ6b1J5vvZKGchy3cbw/Kv9Zh2lpP6tG5Vkzrwyyo92HsWI7ekzzZmI4r7lgEXb6bTEho31FzqxX68z304vrUh7x/8SBuLqTW6XJPW0BbojgIbfa2pCYkfVMZBZbtRu3DayWNsTQNtPTsCriHI0WZDEAdexbab6th2nJ8cN831OnIM8aqrDG8qQevHVaViXd/ErkSUnkruZjY8fLZKW2usOyUCg+WnPKroK3Dp6rVbqRUD6kO8COZrbr7XxmuwiNZMexVHtnUR9665kQXc92ifnh7OQX3l1N12MykFEfeDmSiOvMU8PuHeujkzYnUtl3FoohvVqrgxtWDR00pazlMdv/YqM1Or83i3tWa6ORdIQ8yX+azQYCi7PZGsmq076mydr3mxw63F0ZGUncDMsDYoMfooQoREqqwcbsHSEzwTC9iILxJ3MI/L63qmRosTV/KMiY+vxVWSbXs9gRzeWjyctwGeL3t3xfUz2cRsGPxqJY46ylC4Sco5Y4nniALVBPewPK2no7pvyNiCyYhecRvtG2k7W7VVAjkiNkLixJxGzkQ4BaOpQDf4dXXmj7uK88CY3e4sysxd4niWYl3bHidrEveFDRNtueKiu9cdq3pl3NC4Tq68kNJalazqfdtQ/ISfUluCTYRkPB7/9NPT89Pt0e7TK44xFPb8NNz7f9zB/2u3f4/XqHx7yCJZnHt++r+7M3m/S/j+fO92Ox84/utN++tfMfOX56fKi6BJ91vGddoeH7cj/+7+6+d/fld42H+5P58eHkWem/cHII1zvN22jnK/rZvq8lYXaXu7aQ3Bbuvhb1Tqt8fDg6ebY1l5exLxrnKQ/HChKd4ef1vzNPwRyfCADfiR04DHx+PjLj/cfYFhi7z6jWToN1CVg6+PR03DrdrhWdPTb/8NdJDQ7ZMnAAA= -->
