---
name: "rar-cowork-cookbook-dashboard-build-a-quality-plan-for-a-product"
description: "Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product", "rar_sha256": "84872fd2a5ca2fe8c17a05e3592cb7a470540aaec55fa9f8980b4b1d85b798b5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product`. The original RAPP
agent is preserved byte-for-byte in `dashboard_build_a_quality_plan_for_a_product_agent.py` and in the RCI capsule.

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

Build a quality plan for a product Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 84872fd2a5ca2fe8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_build_a_quality_plan_for_a_product_agent.py` first:

```bash
python3 dashboard_build_a_quality_plan_for_a_product_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_build_a_quality_plan_for_a_product_agent.py   # or on stdin
python3 dashboard_build_a_quality_plan_for_a_product_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a quality plan for a product Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product',
    "version": '2.0.0',
    "display_name": 'Build a quality plan for a product Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-build-a-quality-plan-for-a-product',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13d2c876382ffa10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/build-a-quality-plan-for-a-product'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-build-a-quality-plan-for-a-product', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardBuildAQualityPlanForAProduct(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBuildAQualityPlanForAProduct'
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
    print(DashboardBuildAQualityPlanForAProduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a7ejxnL2XyE7H2xHe7YAAUJzlteKEIiLJO6SAI/XmDtI3O/I8X9PI2nvsc/xSeK874do1swI6K6qfqrqqepGv77YbRPl1cvnF823M4i1kySO/AqyMw/a5H1eXcF/+dUBfyE3z5oqdtomr+qX1xfPr90qLpo4z8B0ucq91vVryIZqPwk+TYPtOPM9KM4av7LdJu58iNMPe8iz68jJ7cqDgryCnDZOPDCrbO0kbkaoSIAd0wMbKu4yG+gTlBd+VgNJwK4Rcqq8r/3qFcpyiF4QOGS7QHENZb7vAX3OCDWRD3Wx3/vVGzDUH+y0SPz65fNPP7++xOD7y+dfX9zErsGtF/rdGmoyZK08zJCBFdu8Wj+W1QAp4EYIhhcjwCsD14VfAStTcMvzA+h59f209lfo3/7t2ttVWP/w+UsGPT9fXqY/apvdrWtyu26Asa5d2E48aXyD1klvjzVU+U1bZXcgAdxZ+PaY+U1SXkA/Ts++fyh5C/3m+y8vAKLKnpzx5eUHCMD35aVqp+9vk5Ti+x/ekhzg8f0P3+TUrXPxAbw/3j329vV5/RQLBn4bGgd3rT8CqQ+3O/6Xl98tbvo87J7WCWa+vF3yOPv+IRj4sfMzO3P973/4Z2LdyHevSVw3/yO5Pz0ER77tgTU9Df/h9Q7yz9DsuaAPmf9c7RRtf2UlYPi7ulfoCdQ/k33H/+9EJyAl6g/E/1Tcn02Y/Qj99E/X9l9NeIWCLy+0n4Dkq2wn8T9Dv37VZGbz03fet5vf/fwbEP3fitHytnLvEr6mdhYHft18/frTd/X99nc///RdW4BY8+30a1slfybzz3C96/kDgs9R3/9xLtB/zK5Z3mfQR6RDv+bFv1S/vUEnkLPet/v1Z+j3+TJ9ZtC0iHelDwh+lzM1sPV3OP7w8hsgigysBuT+9Bhk+b/+K3SI3Sqv86CBNDdvGwg4uIlTfzJej2LAT/U9tysf4FrHANjnOBD/k4cni/MA+uXf3TuxAop8EOv8gxC/3snwq/31SYb3APkKiAXcepLhL2+QDnTkVRzGmZ1A6lqWv2R26GfNpL+ofECN3Z0GG/8TmPpp+jJR5y9/Rc3Xu8S3YvzlXgriB2upG35irLpN/Ldp1efIz55rdAFr+4PvtkBZkrvAsiAGnPsK0KjzBFB/MyFUX+Mkgby4AnDk1XiXDVD8PAn75ZdfHGDhl+xBsQvoUV7qORjwYQ706RNYYpDEYdR8yXw3yqHvfv3tO+g/oP9q1l34pEMGnP/0EbBQ0CQRAjnXpmDYVF4AJdve3Ue//vYEGojJQD0EHo2D2H9MBjF79b131DVu/QnFCcjxAYIA6bTIqwbwNhQ3bxAfQB/2AqXTo4nZo7xuIM8HVc3zM3cqWDZYzgeSWd5ANQjMOhhfobb271p/cSr7bmIKkt9ufoEOGxnUkTwB/0xm3geByXkWA/g/YuJxHwipvqsh6l3EGyROUQoVdmUXUWU/dQT2wy9T+X1OB8JtUFr7L9lUOf0JqnvKPOABgwAy7tOlnyafgz4hBfzg1e+672Psqdrp96pXfcnqZzrY1eQKF5QHoDRsY28qEn97hlQd5S1oDSb8gKX3mv7wgvf0yj0Gqf++f+D/vgP5qPnQlxaFEQz6v9q9TAtcs6zKsGudoSFG1FXzAfxk4eSgR/82qZ603pPsW0/xzkjvxPwlS2IQRdX4t8fIu7ueYx5k11bABnWtQu8IVHe591CeQrOqpiSwv2TvFeAVrPROd8CbIO9BXkzh+K5wevpuaQSAe33g8uwG7q4HQIJgAeEKFa2TgFAKABCO7V6BVdWUjk8Xgbj2p9Tso9iN/rAqCEgH4QPkQ8CIGCQYqBJ36MQcLBNkYlDl6bfh8dRjPbwDrAXdrv8GnUFGTVFVgzQGjdI0BqDw3V0UlPoAY2DiB8J1ZBcPY6YG+WmgPfkiT0Gg/94Dz4ffcuBuy2Q+kGp7dgOw7Cd+9vzh4dkPO5++AsamU9beJ/3R3c+1Qr8vVX/7kt1t/CgJgAySqcr/DhwIxHRa39l34rIa8FHqPwMIRMK9oL89avKj6H/Y8vkfdgXf/7WNw73KHv/ouc9Q1DRF/Xk+f1TG98L4BphkDmIkLvz6W5H8dM+5T/anZ859mnLuXunsT8+c+4OOB2Sfob9m5x9EPAP8M4S8wW/w9Ggfu/4Uwc8PgGXziTI/YdPTL5nqf/P3MygmTk7GKb3fC9T7EFClwsoPp8GPglVPda4HpfXO0MAjX7KPmHhmDCgAWThV1zr/XSbfKzXw8MOBH4UEPMoaoNub+r3Qn7ZEyWR+7b98ztokeX3J7NT/C1uhqWiA6AWgTBspgDloo5rYv199tFTTxR+3iPccA+Tg5Z+nVHu9k+Ur9NHJvkLve4v7ri1rwebqp6mLnlSCoeC/j7Ef+0/HfwGbumYspgU8NkxT8/Zsqv/RiCnDgMV3yp1K2zNlJ43/IAR8CUO/+kch0v2LnTx5o27sqazHzXu218BODzRJrxBwIchCkFiALwGcf6IG6Kn8sgX105uW+w2/b8vKH2v57Q5D89h1/vryzh9PHzw7TDAcJOqneqqgcxCuQCG4fgQWePb/1Hs+ZQH2A/0OEEZi5BINPNTGXRsNfNJFljaM+wt8hbrO0saWMI7Btu27OB7Yq4BckbCDOYhH4s5yRTo4kPcI1a9TyxBP9qG27ZLuEsG81dImXH8BOwvXR1DEWy58GF8tApL0MQDVx9QroM7noh+LnBD9aIMncJ5r//XFITAwksNqfv34bOark02gS0eNnFlF+KZlzHknPpaaEehKcu2ISyGxJSXUMI7GJH9CNwx+Le1UWo9cs+MRWlaiWa6urt1CMrhYx2Kl2TYhuzkLN6sm3Nk8k3jzELIc4o3jkGR7tPA1u+K0eswqKdl1bL7bnmxhOC2TxI9x5ppUvbHEO+PmrJJL1fgDlhq7oOuS09zRHOpgC0udTxqRwdWz0R5ji6PwQ4qJsDK/zUrCO2y1vZEfVKxLxaF0LDuhpPNu7mAk5s3N240arCpRSg3br4jBjhdmo6rO0bQvsJ/pxRBkOrwKstsqxceVb8x7pW48U+hwxrhs/RPanOD6BFvL8zmNzyS2Z+CbtF7kydFo43y7wPqRtXxyQaMji7sjs8D2Yk6f2lCht4Rr3PgmYKvduGnS2ybX98dit1Oj1h8JQ0EUVTPyRtPw803fnAxpixb4pbBXxtjmjiYgboqMXOpvtvYONESCzKw4f7vk0uPNZC4l7xv8NrvSVBpbRnumytGxqtQeluSFUvaZx6QYQ519du4oxKk7bZQ9Mhss+4ouzxZ/DouKmW/wbXnkQURXRsWOUbaNr/a1WZocZsIS7ygqnGKYPfg5sh/7rKz6seI4rVtVvZZpiB7X1do3Iv9cWvwOpy6lT2LloWkEIsNKFLEOUnDoCXPB0AgSDyvylguuV9obtDIusM2KSyzeq11lDalsetGZ73upE9mrLY6qgaboKeqi+fp8Pi3O1oaNxfoUpANmq5Le6Gqj3Aobj+esyAFryNmYtldxE+T6xVVCs7OUEUnk3BTl+alZnd3KbktYlq09zXDMwm11UU2pfKZE3uYm1LtUqMo0kMrYhitVVIzMl7S4XLRbxLPdQB0NQ6mk1A/qIAu7jvdPDnqMx23mccTl6sgVQq+kuZltYf6UV9JtphQy5g0OJWlJcvRbe6FyI7KrzzvxGrBnOq+9jir2kqjVtZaTimKwbmrjYxsJN0oVUErg6F3dqF0NmuTSjIq9b56r40wr3PC0pOp4n4+XMVeL7ZLXvQsT88rGq2bbsLdgTohRoUSFhMJSKkYW0ow5hV6AnhpRPrF2COusKzIyt2NjN+wZZaRVEutNODiUlp7L2iaZtX6B0DEcz4ckGGNOhLUt4rRLUiaRctGglXvQimGe1R1ODifQ+o1zbty4SMa6hm0ZJ0FGsL62hkpjKyRVVCw/+5jriUdvK9t2vYw6mR/LDRmP+anQ+Iuw3Ms7w+dPB6Gb+2TV7qUl7y0o/7JXGUWT1G162GLEQMmNwTN+7LkYfOHaRWkrPRbLhLg4S8ICp3fe8lhHCsF0V0Rzopxej0nRR8J2IxBcNmz3l3HfWrZwsbu1E6CMXZWVqHHLUT3HO+HIl36eDZQQl+Owc0W3u8ZLgisyU90puBl1ihJf0E0aWEJIuwcBjiuBr66SOdY3rWFHRi+Ik3sq2b0cSZgp4my+ODPCJQtnfjtuCxG9+YRssfkJMTueDLAZB5P0/Jb29Yjd0CzilBbzya4UvK3dEeKNs6SUjkR8Pp+RxWbtd0SsRTMcvlq0lSTSDkGsRF6GwTk2LXe8Hs5awlmmwY+Ed+nUhD+b+IY8bHhYWoMmYuGwXUdQmMrreJ7sLhq5CuYmIYr0PlmQNGOb5W1h3fwNs06vPMbv2yMLX2YcoRwvo3tgT0sLX6+j8ZhFrYchnnKg2TQKQxPhhCu1pu20GZhcLHf+jtOY3O6ptO7t/Mg6Bxi+5dfDPhj7gr5cWhbQFs+pNW2XGpK4TVkvJT88e0PR8taoV8tVk1kzszFwWNE2DFLY+l5dEsJO3FSzU3sqaziIQl5SYVqay/PB4omF54U3Rx8q1r/hMjeqQdBxPTmSwV4IyC5zj94Y5WS1xmeOOe5z1qV0RHN5yRFuNz1MdpmxwZNj6vF+IK9koRlO7K1zKRZLq4MRHrYm6iknVj/Gt0t33YRaUrCIqBdYLMBkIazaWu+P4a44lysxPNNC0Bf42Z7l2pxgxwTu9lKmU84lVZaO57nyAZvxNGYM9e16wpmOmcl4ThH46lwY6YYqS8TUYeXcIYl1o1aXZcv1VBnlNnJyxxG+pOmC2fBEJaKi4omgUJiltEuwWXCmENw6zUHapBR2stcx2FfsxqQ8pecdu9jOGxRphVkvMcUO8wtpdSHNzengnM+qoFvxQeSIFEFPi9HyT6tZJOsus95uda2HTY8ozZyW1zunjv0REY9wqMn2rd2Kezf3LGW1kfZYPlyOthIKerJh4VTsxni/csa4tNzd8VQcEe3EbxSqG6LwdAV0Z8jng1PJ2+vSD0M6MovTuB6VVXI6FchuSI/e5jA3S+WM7YQS0z1hUXklDAojf/E5lspRLVxvuLopJJGySX7j2qQqevSQmSND4Pt+P/P95qi0Z70hsvNlj0lwdu3ssjBPPE5nvnOsmW7EORNheTpfWDDKeud4vkZYc0FpgBguxkqKj1l+Y1BYOW6NWkrInpk1brbJMrTb3NRbFO2QiG5CI9WL7W6wtsx1bRExwUfKHlDrhqaKa1cMLR7MYMFWvHId5PIc3eJN6Yp7tNpJqmfhO16XKZxFl9IsiqtjgRiqYt2Uilea1dydV/ZFHQ7eNauOOT3RvyPap/6SEJ3spzA8ZyR1OSOObdK2BWztYPtcrPaFV84Dq40XmCat7c3cRhXtslz3Z4Xt+y1NN+3gbOALjZq7ZOeu++1BHbYVQvgZwlSibyaksJSPHCYp+21p7igxa11eQ+MLE56FHXKg+lWL08ddiS0RRG9bew+f2DVG76IiL+orud7b676VZrYB16G4yoUcr9EipwJmfhZAwwmfZ9wVFWaFdDkyesTQab+ntO3BjphDeTvO4/15rw0XW6TNKDOVmSJb7nFeLY3cXzBYYVUhRlDdRS79k8ucNmW1E7BLfxMM+bjThWo77JS0umJOGylkEFy3yI2wciafw961ZFxM3AXrVhz7mOW3u1WypVf29bzauprHpkdCOwFiY7aoQCP6wSs7GxaFETGkA1Hri2xd73102e6sq9FfghJfU72FiN1t6HShoVzbWR5cJN2zg4htjACVyoiYR1no8mNDFDDCXke8WjALSbvm6SJITeJkoVgYBap3ynWn2szjY7ffbFTxSIQxc3ZAXYtI0G5awvE8ljafikXD3qSK2uSCI7c47JDHpmx2tVGztxPmHbRoIEs2GxW68pNqE/LMzge731Cos7PGH4+00AhDT8lMg2y2seWymi2YI6/EER4RSSJ451Xho4csiA58tO8XFlhSxkpx3539cEuqCRV5hlX3iUtEC6Us6DmCdER+W1+rbCk5pHYRd8SGdNNtjZCR1+YkwuXG2mMrTXEjYQzG5HSIjo6xZvNDmYxOq8A+NgCy4w3ZRNeGKVeJ0dwIU1g47Wgdox3Fopws1mNxrcj+UNyynCgaTEMPbJqI6/4Gupq5FvbLVrV21lmUXF1kCUQ5rOFKVirWlWhKahyBS9wybtXZqF7ptUl1yvaiqI4UCvF2dGcsFfAWnLEpWRxTO/AvsXfsvaO5L+Uud3Kj0sb1EhRRf23H2vFE8Lq5lL2LtWrpzQ7eS/xtx61NbSPug52ga9VwI0IGXVRgXcHBlTI4G0zQmii9jHBJacHS6eg1J+OcHMJwo5PDeQkn+godtsV4i9m5RRFKJy4kJDR97IilmMplpJLMZLVFK1i3Z5vZbOu5pHTtbr3ZLo5cJASrwTV6i52h4uVintXWP+CJytMR4swctdoehOKUXg+tKQldDdr8C6OnJ06+eE0cLZ1lWeJpdVsLWwrTdlWKi4x+WJZOvbEGHY9klLRV9YR3crxUZ1jRrc2t0J8XmwUqZ7dw1+tE2mzADi1IZ6LE0epSYbwW2zp2bpUX0+aGdnQ7Fvbq2kHzmdTjs9t5Na8k/zKMhDwujMWcMshNQ298ZDY/yaTj6mi9LOlMDByPwYkjwTO4tlIA9bgL5djuF7mh7KwtYQub81hZBr7Z4gyzxofZzZFsOJQOXqoJ0SqaUcKes0QslNZLIasN1fVnpiGWOnmDdX7Ona0zbqiYxHXWiGwv41axEffSHSR3NAMGFdHIiiwqW3FHBxtQORqv+9BolpijyaRKSyuP6ghl9Hf78y2eSYbjWG4oHldEYmvjSdmZGSGasu2tfFOUFDpybrlT5Ch5FWx0hKtbShgzG5mJc3vAcpXMeVDiA4VmYlWubyg6o7CSbpcdcUjHBFmVA6JsY4bOx1pPTRR0S0djBpfIbNkL3B5R1WFc1uNM7vzjzaAkJcTnFjwXw17HLwnZrmu14S1+YJYw78WukXOuF8xKTKXWy/oQ6FfHjdrNFsbbbB+7FJHzpOtYHHc1DtvQIBTUq8jLYaMM+9WuFhosuWXLWN5u+qTe7pVoJiGHVF45yJIeCMY8R/OczhWtF4l2QAEvk7XEUIctvDmG7KKj91TfH8SY2JTsHMXXMz9Hh82pnaOnPm3WZF+NWTND6mFhG85h2zJlkBWUGHup3585zauzq1BjPjWGeou4rrpsFrzZrDx1gXoLWZcuTreO9L0EB6cwXNRUuDcuobNjQR/Sm/QBa9c3CU3J9U0e4kUS15l6XoO9dL/cRU0i1HTmEfhtAZIhsyVk5YPEl7zSOgkq7q5UlDzTyxjXYZqiDPis+PPNGcuitarJmLva4VdXvPryBTZABp1Wp9vs0kS1rK9y05mtRbddoALlcotLd54LRbgYllWXSBiJ30jVXMvz+jBfXHoMp2fh6WJcEROznLm7am6bcZs2oagHt4M/uEtkUVzRAp0tzMN8Jm05aacvOHdIb43AcfmNi+luBwoeK29PdiMcwEY84xR7bt+GUDT20qVTdmi1igOqNClT2OltVWGE7S0plVulxWzNUUWbpZbTNaK09y16fan5gnbkK0Jv5XCZm2y8p1ZU2Ajr8CZq5wN34BSk7nG/bSjcny0yG7Qr2JIMEHO/tteDJhHc4mAUuBUKPRlwo24gvL6A9fbACeuzzp96d8cUB97teOIyhkbvHGlpfei94przcnJGOziXjos8sem6GCnSsqh87oxn25ntu4sea8ZgwUfAzgaJbtu6ZQijHUELY3jsRYelZTGyGOjMdXY+xulSpJZ7J9GHZNitiYYkr2i2NA4kJ9meQ0c9a9MuFyNWYLL81VaHTWzBM9XcrTQmtlScuaXd9YjNLrRwcbhcmVd4lessSnP5nAQ1mjpe1XW5Xq9/fHl9mU6tn2fP/6uX09Mp4P+3w8jHueH7u6n70bNve5/vuj7/78z7+fWlcmNg3OMgtk7a8HlU+XfHsJ/+ytuNSdL4eA88vVobmvdj/MYOpx85vcSZ19ZNNX6t86S9Hwq/vjhtPf3Sov76PPx+uS82Le4n6e/KX6ZfPUwn1jmY3ORfn78Rud+eXhn5Xmw3/vMyfJ5Tg/kjcGLs1l8XBP7Vr4pp3c9XJtOR7vTO5OW3/wTnUzRCayYAAA== -->
