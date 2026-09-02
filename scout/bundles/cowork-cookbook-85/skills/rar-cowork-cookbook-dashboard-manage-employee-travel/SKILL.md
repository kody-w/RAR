---
name: "rar-cowork-cookbook-dashboard-manage-employee-travel"
description: "Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_employee_travel", "rar_sha256": "5798a7a93adce56aec1fdf1a432dac86e8d143e07847e0bb7213dea75f1e4066", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_employee_travel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-employee-travel:6906ca29a796b7340f4ab74be79f5cc5bd4e49f56bb29044be0c51a1692d90da", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_employee_travel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_employee_travel_agent.py` is
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

Manage employee travel Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-employee-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 5798a7a93adce56a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_employee_travel_agent.py` first:

```bash
python3 dashboard_manage_employee_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_employee_travel_agent.py   # or on stdin
python3 dashboard_manage_employee_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage employee travel Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-employee-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_employee_travel',
    "version": '2.0.0',
    "display_name": 'Manage employee travel Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-employee-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-employee-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7507fb0f7d51f09c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-employee-travel'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-employee-travel', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageEmployeeTravel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageEmployeeTravel'
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
    print(DashboardManageEmployeeTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOj1rbmX6HzPti+ZKWYEXniRDRIQhNCEoMYXI4qZhDzLHD7v/dGyswqH9v3HEf0Q6uiMhGsveb1rbU3+euT1TZhXj29PsmelUFrK0mi0KsgK3OhRd7nVQx+5bEN/kNOnjVVZLdNXtVPz0+uVztVVDRRnoHlpyp3W8erIQuqvcT/NBFbUea5UJQ1XmU5TdR50EY5CJBr1aGdW5UL+XkFpVZmBR7kpUWSD54HNZXVeQn0CcoLL6vBaqDLANlV3tde9QxlObTEKRKyHCCshjLPc4EMe4Ca0IO6yOu96gUo590swNCrn15//uX5KQLXT6+/PjmJVYNbT8t3DQ534as32cpdNFidWFkAyIoB+CYD3wuvAqqm4Jbr+dDbtx8nO5+h//7vuLeqoP7p9XMGvX0+P03/pDa7a9XkVt0AJR2rsOwoiZrhBWKT3hpqqPKatsruTgOuzYKXx8pvnPIC+uf07MeHkJfAa378/ARcU1mT4z8//QQBH35+qtrp+mXiUvz400uSAz/8+NM3PnVrXz2nmZgBrV++vH1/YwsIv5FG/l3qPwHXR4ht7/PTd8ZNn4fek51g5dPLNY+yHx+MiyrvvMzKHO/Hn/6KrRN6TpxEdfMf8f35wTj0LBfY9Kb4T893J/8CwW8GffD8a7EFCOvfsQSQv4t7ht4c9Ve87/7/F9YJSP/6w+N/yu7PFsD/hH7+S9v+pwXPkP/5aekloNAqy068V+jXL/Jptfj5B/fbzR9++Q2w/rds5LytnDuHL6BAI9+rmy9ffv6hvt/+4Zeff2gLkGuelX5pq+TPeP6ZX+9yfufBN6off78WyFezOMv7DPrIdOjXvPhf1W8v0MVKIvfb/foV+r5epg8MTUa8C3244LuaqYGu3/nxp6ffAEBkwJrWuT8GVf5f/wUdIqfK69xvINnJ2wYCAW6i1JuUV8KohpS3ov4q77eC8JK6XyFwdyp3ABFWmzTQurKiBAL1MEV8siD3oa//27mDKoDHB6jOPsDwywMIv7wD4ZcHEH59gZQQiM2rKIgyK4Ek9nSCAGHWTALvqVG36aduknlH27sS0mI74U3dJt4/oK//TsiXO7+XYpiM+JyBqDyguwF0eWVVUTJA1oRS9tB4nwC2AiSp8iSxLSeGph9t8TJ5Rgu97M1fDugm3s1z2saDktwBivsRwONnEPI6T0AraCYv1nGUJJAbVcBFeTXc2w7w9OvE7OvXrzbQ+3P2gGEcerSbegYIPhSGPn0qKs9PoiBsPmeeE+bQD7/+9gP0f6D/adWd+STjBPrB3V8glRNoJx9FCNRlmwKyqfWACFvuPW6//vYIxKRdBvojqKbIj7z7YsDtWxJMFjyi8x4aYPOkole9Sfq936A+BH6BogZ4C1R4/fw5m1jkgLTqo9p7d+Jj8cP177F+yJliUr/5EMTJr/L0TnvPvymYTl65L9DWhz48BcwFcW2miIZ53YCUBb3W9TJnaqNW8y2EWd5ANaia2h+eobYGpk6cv9qA9eScFECT1XyFDosT6HJ5An5MDrqLB6vzLJoC/5asj9uASfUDyDHuncULJHrAm1BhVVYRVlbt3el865ERoLu9rwfMLdDwe2hq594Uo3s93zPv8OdTxPZfZ4+Pzg99bjEEJaD/n+aWyRB2vZZWa1ZZLaGVqEjGI+smrSYnPKY1MEHcVbiX0Lep4h2A3qH5c5ZEIFLV8I8HpX9PtAfNA+7aCuggsRL0bnV15xs1IF2m+FfVlOLW5+y9BzwDN4Fg1ROcgaqOJ4zIPwROT981DYGzpu/f5gHokYlThYAch4rWTiIH8oEj7uXQhNVUbG9hAbnjTYUHqsMJf2cVBLiDvAD8IaBEBJIY9Im760RQNGCGelTAB3k0TVnFI8ouBKrKe4G0KclBotaQ7YFRaaIBXvjhzgpKPeBjoOKHh+vQKh7KTOPwm4LWFIs8tRrv+wi8PQQJOzUbIO+jGgFXy7Ua4MseBAEU2+0R2Q8932IFlE2nyrgv+n2432yFvm9W/5gqEuj4rSGACX7q8985B8B4ldZ3ZAIdOK5BzafeWwKBTLi39JdHV360/Q9dXv+wB/jx720T7n1W/X3kXqGwaYr6dTZ79ML3Vvji5OkM5EhUePW3tvjpUWef3uvs06POfsf34aZX6O/p9jsWb0n9CqEvyAsyPRIix5uy9u0DXLH4xBmfiOnp50zyvsX4LREmrAP4C0r6veW8k4C+E1ReMBE/WlA9da4eNMs78t1byEcevFUJANYsmPplnX9XvZNNU1QfQftAaPAom7Dfnaa8wJs2QMmkfu09vWZtkjw/ZVbq/QcbnwmEQaYCZ0zbJVA1YGhqIu/+7WOAmr78fvN3rycABG7+OpUVaHhg2H2GPubWZ+h9J3Hfm2Ut2Er9PM3Mk0hACn590H7sLG3vCWzdmqGYFH9sj6ZR7W2E/qMSUzUBje/wOrWKt/KcJP6BCbgIAq/6I5Pj/cJK3jCibqypTYLu/FbZNdDTBUPVMwRCByru0QhasOCPYoCcyitb0Jjdydxv/vtmVv6w5be7G5rHHvPXp3esmK4fU8Ijbab95386yU0ufe/AXybG1rT8Pm/dPXyfUb8A66Kp0373KJjGhi+PLHx6BUDjPT9NfqwiMHiP9x3100MbYMa36RZwAJDxqZ4mhxkoIsAJ9PNiMiEGcPedgOl25N7pp4vXvx6J/6L2XykGoRwLYyyaoWwaJxCfsGyasD2a8UnHIW2X8AhwSdk2xiAEeIA4JGqhFIO5DOJaQIkpjqn1psQMnSIA1P9w898e058e60GrwEgKMCBpZm7RFoNbruORlOU5qO/6qEXgmGs5c8qbuyiBewg9J2gPsW0aQ3HXs2jSRz0CoaiJ39ug+FDqy/tQ/h6TBwR8AaCZRpPKmAX4OjRKuAxtUY6HIzbueCiGujSQQzK4P597BFj/sfQtLlPYHnZPGQtmRDCvdJOcX9/iPGUhRQDKDVFv2cdnMWMuFq3RthTaTEV5hqnPtnaklpRG4dpGY8pjTVgGmy6lseNztapX4rBboaJjBiaS09pBXGwo7oTJvu3AMlvI2doSQtvgYiJyMLvFhdgnSYK+cBKf37w5uei4294oUd7YXtIG3vYV1u0Hnkzixu4VGu4EXoT7nQg3qmNio47P4NDG5X06HwwpzKRQESzL3qd1I5Or/sjDdtOXumxvRKIdEiWRA/FyFT07SUvUQiSv3u1vJj2HLdg/mGR4mIv7rS7UsUaanWTXUl7YuXeSqJNi1kQ3mpSnk8jMgJ1OiGDm6uZJiMSpKnqi2F1MC03a6ixgWphqc6KMa4pL4C2aiKaWN/DaVAceOMrHF8pl3J/zc5GKXOxax7A/6AV3bjZoYtXV+oR1WzOoZM00DXk5lGrPnM9pG24smdeGc6rrGo9V7rW2lnrZGvKV6lyhlAp5PrKKsk0O/WYxG1cmgVvyamzys6gWpHse3K1zJPKLnBpaJdiNM2pH2A3j/YDvdg3HXrJrx9TyDnQpRyCHm2latl3tjvtYS3yxGRtzEZEh08AGivSYExPFAgcsNxum5uy1GKzxUdUao4atC4IohUXV1m7WVkuL4XE4R+pw228KOlOCTF63O2JMa7jN9cuADnPXJGvGPx0Dc2unIkWarsfMcsmg3Z6vybqTEgO/cVhtC6jPLwfeGFvhwCrNrViEteoCLAgt25BPPB56opIrNVdcKxjfXIoVeURPWLl297rlEwNBeguUGkwmXPQZqREZuz9eRoFf2xIZBsOMzqpyTGwUvyRkJZpm6KZ+gjmlgxxW8qoyNLO5xKgrxehSmn53On8MOhEz3AIt/IDFr8dN7Z2I2DFg1UyDQFBnxMocS9P3lRmz6M0NTwljdfKY3U7s9hojFunlkqKpEXfLi5zXF0Wl6gC5Oba02awPVmqeUInCMX/pplYCtru7jBMEJCuOR+lADh3RLm6X8Tysh7CwyTl77YztaYstvf0qWXiRsTtiPL4di5UpbFEiKq0auY5lUViuZhCOIt2IQfcX2+HY4RKcnu2NeyC32fIoE9txddRONacHY5zfToO5DD2ZFC8+16yuNmGsbi13TjKdnu1mN3HP3S7uYbfDNjfraOi4eOnBzmJus2FvcbWKHfZhTs316+KWJldnSV5XOWtQqnCab3gF9c8FDY/8LW0LQoIvFr+5rkbsJjXpVl9srR6eV9w+1TNtFm7I1ORWrhju6fWCYuSwi6vCdpFSpKxLq+JL2T/LWF7Qh7V0I9v0tjv0Z6PGl/q5jwA1tR4EtEB6lyBXZyQNSWat87toTLjWbLVhNxPlU7kQ6DJcjxsc3cn6fiftk5m0NQIDl5PcRdvWP5CMoYvHI8g52uKEhWKAvFb1S3EN4VgdzJ17HmU9NI+mWAnbxUUcBdNF6c1pX0RH1R2z9FxyoqcMM3QLsmcttn60A/gSuSeu68a+Ng8AItnxYOvucsVRC7QbrsZu5Pma2qH0/GQHROd3sNuF/nFJZE0/r4LNDjfl85lrsjWyELm5sbslw/7MkNvYacK027neoV+TbHkLOdJwL216biMCHg6+rzL9YGCxcrxgZEjO/X5o0nPBr282uvdKQTBHiavzRBUMdpwhXJQNNsGtDZbTlnvGhdvjmd8OW4RbLIoId2yFxy8LqV/oC+3SyM1tFSyd0ioFfeWZuJI6LC+Lqz0+sk1oxNXo8AZhM7cRD4pF2pyp8bwgLiGFm6lDKwWWhGqRuaJtivPZaUxg+BR5EsEre3l3Q+FZG8f5YHWolmDtbXfkONU9hmbKzWYmy/nMiG/ofLuUnGuWjTjl72JYyyjPn5kE7IVdep6r3RCWAIhbn+/smGWxHmTmTVymexk+bLeROlD6IQ2Es9jMNgixv+K5xcrU8pIJyMpx9G1RZrvynBR4KOpbP44Vrb25fVVnkoAdkz6LVjCiVqqpInEg72aa1eah7wLQWevXfjeYCu1adn1Wt4rLDyw/LFQzo+fXVairuXRh5WAzn2+Ys3ZCyW5P1q1+vpQO7UeMW1LOxXMZ+MCaXGgMySjkJavgBjIeV25zq8y2Xq4PsVsuu6waUD4O1qdNadd9s9XtEr3eOM0JJQcr7Gx11UMMhU/Y6hTtFjFqdpGvbLV4ucPO5tI8FLEBC8TNrex0GKsVFXsanB90VGPjNX7MSyom9xxibPG6bKw0W5+Fg+MH+NXl7HOgR7tynRdn1DpQWzg5JeuRR8l+Pm9yVQ39dbKyzK1KS1x85m+GufW5HZOMl26RjqLpbeod6MM7tQ6Wks8jeHuRav56PVwF/BgsM+l2cuMu9+a61S6altvK6Rjs3ERWqgGnQN/vtS6y5UynlrMt5tMH6TAfqDWc9so5FpKO9prOGvB9zJP7tEx1MdoRvG5ie4mftRJ1kMID3Wh562T5Cd+zlpIiVZFmKH9F6GJQo/moSpf65gYJcWF3s0RlldmpUS3FkFVSws8CGeEEuRZ2cSwvZgtlt9J5+cgGoK3uF4y+wpMZfU52YRrsdcWftUvBKX1XxK/WUV4UqMluhGhujf1mZp3HUkvLsly0mTIiYJrMEpomGyaScni9aVnRrbD5aSX1tO7BMcpEqTaMzDypEgzOmnGT3xylKGymZcbCC+eIdgjWe4ZeE7v1ftVetov+rDftGkuWyx0aaxu419cXI4y3+pUU9GpOn8rDynR6DOY7NnePslqS9vqoBXMJrRbrSsspIRi4mZG7xHGRHAveRk9ye+QF9cJWetWo9Vwf93KwXG7tXvcP9sIz+QPMIxguqdG6lU/VapFgRBmE4wicE19qtnCCxXnXB+aeQwdLgXfNPNwlTKf2u9Oxj5DAH4hiZsbjdYce9w05GEzcYBuRy7xov1hdm+XhIqgbIbUQsTakrZKQe0JM4q27LctUjnKLUpaxeznK2q1oVTO36NUlPnexpQTXpcBYqgqveoRq9j5CapbOAjxE3NKUmxWCX4q9VJJbfYz2c/TiUNh5Vig850cuV8SnNsjOoq9X1lHQWAyjO+N2XaKiyVddtkb7USmUYV9ReqDZJoq05Wp/0Hb4vPQiy51ZdLHVZ+l2S+zRykgP7apaFTdvscr1ZkMIobbKqs1leTvzJSbFjaQpW2zXxPwoZovNeYeBIapukcI/UCujI0SPKihHuUah6nIJJ1bjpS4N9byz9mLRZ/2xrNnVYjkT+SFmybhBF5fRtLQNtVOH7QjGC4nKEvGi0bmHFvBMMaTlQSpBEm67g8ia4TxgK4dLkxbXmKrYJddlF66GTVdlpshepK3Q4QucEsmwDejieAM1Q5Nz3h1z1WH2q2XBGDKr7kNlrpaFsruuG7bjkmNLX5D9pj2YntNn4+3U88slSl5oLUxkt6WR9LLdBVIHksWoKbOcNZ1a0gjv4HPTajk4PLKSiVHmmHH9ydN7RLNiHbeNfXuSQDIckXSmVscFp3A3yXJPol5qxZkLynHpHJZBz8vnsO96Y72RMKtgD+oBExKZPGSKNdNu0fJycxF2UZ6yQiHsWpTmBcbXC/W6YcPmHPo2hxLwUtoj23TbX4+wIe/FDRj9BFNemajM6valpnHBIR2YJHFMTzrDdW1d5edBHuXb84U+ZLZ9GV1zPG9pxQyIrY6NbR/AGnHBabrQ/Xm+sa+IXZfzBj12Z0K39ng8eHRPcGXtIwneKC2x3tNO6zuWcBzEpeuaO07aSpU4npn1UZ2vYxjhElxqRCb1WcSJLliCn/GNdj5tDAbs6lDPRRa7aBtd8OOeYFNJm40222krzoywQO72ZieGPUeX7dDN+GxLByKjkMiGxUlfRQ2WkW0Y34WjQZ0o9urjqLamup7PhSWJmxqe+ZwmLynV38xV6twyV3vp2tfY86NuRg8HnGSroKzFE62f5tJJoDQGHfFlV5F8hklUqeIrRiqMELXz/Wk3IlYaIBZTD7c9easL+FzDZ+ksan59FMKU5ZRrM/SpeDgRwtbAdx3P4RvyMCupTZill4FK/APD92K+RjEKcTcBcSa16qyfiAuHCyVDKmMqdJRsrAc+SZqNrxpKJ3BHeB0sUeJK9rNZ7yP60jels6a5kocvTj1tC3QXC7DcSm5SWyDB5qCbM/BwKlq2d5e7pDqEsBVZspNVJ13q2kvuozFGZLNqg3uHlHeRDY6sBoRVMUc8dgR8DGlznONgQG5Hi3FzzritlFqwhtTNKCxryFpjVHGAif5Q24xBX82W8m4wPixsa7c/LE/4sSCb9cKv901yEwNXSWVXOs6DzrjyFDBVJ1Rvdd4eR2EzkBv8QOfhtHEeiCx2C/Z0FcCEOi/5oJWp4Krg7UYKslqGx2yhe655YwiAS6BtS3tsa+uNslvOsatEMvC6BmogHLrdaRp5smkdrT1tI7HpPmO3q42CF0kwVxebm8Kp1YlmQra62E64mZ2GilrKV6z3ab/p0WrEfd1e8e28nWe26EVVaiKaIC3nFZY4sccwK7NPW12aBfja6BiHwxuslVqTwQgF7beOQbZceJqLCr2+Bv56fa365na0e2eXuKLFeLSH8/5JMxhcZHeywNXtsa0sAszjVbJxL3Q8KrhbNVqzWahH+DjUgoSqVNAQh01/7Vl1I3E64gUMs3EjacUl29lNQUpNAh2CgE+Sd9slOKqcKAnjSYZvw7Fbscie9mBtFcDzBsMx4YTBOuPO12Dab0GVZcEs7MeZpy+v2olaaYLv8FFF77AONiMboXLLxc8zk2Q8eNfWNtXTDtbi1Gk2D2p9fll6Db4A6NL4VcrOJZeQioi15vwZNDNsCVuMtdkOpe9IOQBSeth3AUxWjKEF1mJh8KUFCxscnl9uS6kgVAA6op5aPi+4c8u+2XTcgH0AytM8IudWAcbVZYQQoI4Oy2K/4vwyuYbjFTnQh1AvbXmh5y6N1aSHHfuM0Rb5OlyofRsy+4xyjwYLb649vLewbgHDZ9cMKJa71OGJR/PFfARIEpWzlcUIVmwiu3R5qDM2BNh7OCac7DGxcPZP82C50VTz1BbdYdldaZSs2WSuLVfNiGetubQ3QnFM6Lpnxsg4NxasoDZ8TjZnnK0rpFkkIwA3EytnpcSVJ5pfkAk+zlHANmOcliXPS4fUMgULwu1Vdp2AO46IKy+JqCeKYVBuSiX62TKk4K2dHlm6wNfkSIRC5Z3O/vGS6UgaFCzL/vPp+en+cvfpFUUoBHl+mt4BvJ3k/52D4GCMii9vnHAaR5+f/t+dUz7ODN/f8d2P9T3Lfb1Lf/3Plfzl+alyIqDQ4+i4Ttrg7WjyX05iP/270+Fp9fB4Nz29irw1769AGiu4H15HmdvWTTV8AZvW9n50Ddzc1tPfptRf3l4gPN2NSov724h3geA6jCqgez4dxoKrp+kPR6aXa54bWc371+DtlB+sHECwIqf+glPkF68qJivfXjRNB7bTm6an3/4v1rxLW4MnAAA= -->
