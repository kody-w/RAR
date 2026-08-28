---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-receivable-strategy"
description: "Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy", "rar_sha256": "7d096c0c00412b456a04d7bb9fef8c8e64b2470d71543e838e38b46e8d0ee915", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

Define accounts receivable strategy Scheduled Email Brief — Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 7d096c0c00412b45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 scheduled_brief_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 scheduled_brief_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Scheduled Email Brief — Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy',
    "version": '2.0.0',
    "display_name": 'Define accounts receivable strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e2c3ca7a92fc9bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineAccountsReceivableStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineAccountsReceivableStrategy'
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
    print(ScheduledBriefDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81a6ZerRnb/V5TOB9vhvWYH6c3xOQEhgSQECBCS8PNpsxSLWMUmkOP/PYWk7mePZ5LMJB9Cd58WVNW9v7vfKvTri9M2UVG9fHkxgJNPRCdN4whUEyf3J/PiWlQJ/FckLvybeEXeVLHbNkVVv3x68UHtVXHZxEU+Lvci4Lep46ZgkhVVHufhZ7eKQTABmROnk7rNMqeKb/D5xAdBnIOJ43lFmzf1pAIeiLv70rqpnAaEwyQoqkkTAThWl0Vex+Ngcc1B9Re4vI7DHPiTpphUbT7xIf1hAudfAUjS4RViA72TlSmoX7789POnlxh+fvny64uXOnX9DSvw+RGgcEfDPcHoH1iMJxRILnXyEK4rB6irHN6XoIL4MvgIijJ53n1fgzT4NPm3f0uuThXWP3z5mk+e19eX8UeHWEeRmsKpGwjfc0rHjdO4GV4nXHp1hlETTVvl9cQZFQFV9fpY+Y1SUU5+HMe+fzB5DUHz/deXAkJwRkN8fflhVMTXF6gX+Pl1pFJ+/8NrWlxB9f0P3+jUrXsGXjMSg6hf3573T7Jw4repcXDn+iOk+jC5C76+/E648XrgHuWEK19ez0Wcf/8gXFZFB3In98D3P/w9stAcXpLGdfM/ovvTg3AEHB/K9AT+w6e7kn+eIE+BPmj+fbYlNOs/Igmc/s7u0+SpqL9H+67/vyKdQjerPzT+N8n9rQXIj5Of/q5s/9WCT5Pg64sA0riD3gEd+svk1zdDW8x/+s7/9vC7n3+DpP9bMkbRVt6dwlvm5HEA6ubt7afv6vvj737+6bu2hL4GnOytrdK/RfNv6fXO5w8afM76/o9rIf99nuQw/Ccfnj75tSj/pfrtdWI5aex/e15/mfw+XsYLmYxCvDN9qOB3MVNDrL/T4w8vv8GMkUNpWu8+DKP8X/91so29qqiLoJkYMFE0Y+Jp4gyM4M0orifw95GuoF4f2eoxD/r/aOERcRFMfvl3755UP3vPpIrW77no7Z4t3x658e09N759y41v77nxl9eJCVkVVRzGuZNOdE7TvuZOCPJmhFHClAmqDiYYd2jAZ5iaPo8fJnE++eWf4PZ2J/xaDr/ci0L8yGH6fDXmrxrSeh11cIhA/pTYg3UE9MBrIc+08CDAIIap+NOYyou0g/lv1FedxGk68WPIEdaT4U4b6vTLSOyXX35xnTr6mj8SLjl5FJoahRM+4Ew+f4aSBmkcRs3XHHhRMfnu19++m/zH5L9adSc+8tBgKXhaDCJcG6oygRHYZmAsSKP5YXq5W+zX3576hmRg+ZlA+8ZBDB6LoQcnwH9XviFxnwmambgAKh0qPCuLqhkLXty8TlbB5AMvZDoOjXk+KuoGVrQS5D7IvQFSdaA4H5rMi2ZSQzetg+HTpK3BnesvbuXcIWYwFTjNL5PtXINVpUjfK+I4CS4u8hiq/8M1Hs8hkeq7esK/k3idKKPPTkqncsqocp48AudhF1hN3pdD4s4kB9ev+VhQwaiqewA91AMnQc14T5N+Hm0OOwZY9HO/fud9n+OMtc+818Dqa14/g8OpRlN4sFhApmEb+2PJ+MvTpeqoaFP/rj/waAueVvCfVrn7oPA/aCs+Sv9kcW9L7h3A5GtLYDg1+X/Uw4zycKKoL0TOXAiThWLqp4eexy5stMejcYPNw5MNjKlvDcV7OnrPyl/zNIZOUw1/ecy8W+c555Hp2gqC0Tn9Th+6BtTzSPfuuaMnVtXo887X/D39f4LOcM910HgwzJOHLO8Mx9F3pBGM5fH+Wytwt3Tlj0EPvXNStm4KPScAwHcdL4GoqjH6nlaBbgzGSLxGsRf9QaoJpA69BdKfQBAxtALU7l11SgHFhFYKqiL7Nj0ezQRR+K0H0cI2F7xODjCARgvUMGphlzTOgVr47k5qkgGoYwjxQ8N15JQPMGNn/ATojLYoMmjz31vgOfjN5e9YRviQquM7DdTldczKPugflv3A+bQVBJuNQXpf9EdzP2Wd/L5O/eVrfsf4UQhg7D98+ZtyJjDmsvqebMfUVcP0k4EPP31U89dHQX5U/A8sX/60Hfj+H9sx3Evs/o+W+zKJmqasv6Dooyy+V8VXmDhQ6CNxCepvFfIRi58fkff5PfI+f4u8z++R9wdWD819mfxjcP9A4unnXyb4K/aKjUNy7IHRkZ8X1M78M3/6TI2jX3MdfDP70zfGTAwj3B0+ytL7FFibwgqE4+RHmarH6naFBfWel6FhvuYfrvEMHJj283CsqXXxu4C+12do6IcdP8oHHMobyNsfe74QjPujdIRfg5cveZumn15yJwP/zL5orBnQm6F2xu0VjCzYUzUxuN999FfjzR/3iveYg8nCL76MofdpMvbCnyYfbe2nyftG476Xy1u40/ppbKlHlnAq/Pcx92Mj6oIXuNVrhnKU5LF7Gju5Z4f9ZxBjxEHEHhj7gOIjhEeOfyICP4QhqP5MRL1/cNJnHqkbZ6zqcfMe/e+++2kCbQmjEgYazJ8tXPBnNpBPBS4tLJ/+KO43/X0Tq3jI8ttdDc1jC/rry3s+edrg2W7C6TBwP9djAUWh30KG8P7hYXDs/6IRfZKESRF2PZAm62MzxsM8DKNwwqVoxsEon3XdWQCCqTcFDOUSFIv5LE5TJJiSU0BOXYoBUx8DYIbTkN7Ddd/GxiEeYRKO4009Fqf8GeswHiAxl/QATuA+SwKMnpHBdAooqLGPpQnMqE/ZH7KOiv3oiUcdPVXw64vLUHCmRNUr7nHN0ZnloBTr9pGEHDGktwN2dzQa/dy02Nm6Hlvr2l5Okih4dBtPOYuYH+jkbEuenrSMqzDqnNMSI9gmqOESFgFzqC6zG5470X0jHX3Cz20kOCv75eJg3ma6k2LVShaUhrAi/YLdSvy2alKZV2S9xYlTfSQsN3Wd5eC5B7ON5gGeXpp+hwaBPjtkUp8z6eaYkfnmQhWl63buYFUoP50t0UhRD2XjKMt2qVitjWWlo8ggvZSzsJ0d3MV5hemN3myO8pW8djtyKPE9cjsPwIzjAWkrlqGAlOOZGzFoJzMMHk/5TbdNV9hFHCTXzpoLedKFhj/YlWhc5uRFJJEzbBlXhdFSWbSnqwNAAnW7waNoADynN3i1w9dyhrSiSyw6cMkcvD11Ys2BrWNU/NzMnQEXmzSjsx1VHS6V6aSbRU9QCKWfL5q1Uv0DEZOzY3PMGqNMM3tBbFMt35UuzW9Rt1Hm9mHeWuVtw4b7W5jIW9wItVlWHaC3lTUguYCDrpTnoTzfzKPgEFqbvGk9AT3ZKeEe90g9mCGlEdPbIKdWc6qWGguGlYu7iVPNSX6lVOdZqmebvFCaKRbnBzc7pmtBwoVTnRnBLOOHWmv2VCVejyl1zKHJ5uV1z2Z1KZoQ/Oym7F17mqpaNvXmXJJvaNwWarJyqbN/S/tdS2LDyc+TqDK3eIx4FHpyFifi4tOn/dnUNuLQEvbFY0rWyOCUZbXL+/A8I8L4tiyBWB2j8pYgm06V2sieZ8iVXzhIpqqnfjWADW5eNgeCRgR6himu7B0Ix7iwx/l1IMszHRyXmR82VLRh9kc/3GUGe6FjVqRjSaRzYnvbq1thPxuMtN34vUIMW4mdLddTUUA2EiGl1a00aVlDhJt+UwMUY9C8q4WYtiqi78ymqOs1KKUmqvHyeLawRZLorVIdnYUkzZVK6ZuTX536TEqSRZbvNYrbZkTdXAuVUlM+X8r4ILFqp/GsaJViJvaWcKLUZkS8tFeEKRj2ZhEvMGNqmZ4JQmPhpPSaUdNYLG3ruD3Y1MKFyMhjffGvbYUtCHABLm+5NLJg7S2FDCavJWmXD+bJRkoa1JhBTEFCoNwUZ08XWqDWNkuTXDs9bS4+E8zO6H5faItzQdpAAoMlCWhit7LkoFm8sRuer3M8MhvJjJh9v8VmbrxoTtkghTZ68XNEjiuxK7A65mbhpS3VLN0m8dLCroq/b+hd6znKFZm6R2UaJOos2tCkTcsARYdI903LB24yYOW8nJHG7WrTKpvNXOOQDI5rxsSgDT5BrNeUGFoNQohFqVha5sjV+WIui5LeYsOuF2N6tsghTdlaXvz2MN9oaiJRl7a91WZMstRq7aaiJBxRPeSiQr1c8Mz0Q0qOdy215gdzPtw0N9SDmGX4As/JPUWZtMRViltzTp+fphh+OqqHY9QpbrXuTlE/W2woC1upZ7TYhhvQMb0Lt59HSSJijwFFeJt7UqMuGT6jb9d808TMarpaJppy3c/W2qloyF3XBStsHtCoG540ZpvlQt8nKw6R5rtwHRfFgLf51RYCk7maAkseSmSwiqkrcN6Zw7C50m2G7CTlioIku8XxVkzT9RSpjtxKv90yL7drlp7OzutswTsct1KXrZHJqL5CYr1PFvzA6cFeDYNdsF5fOHkdK+5yyK7z4xr6gHS1lg1/DZlE5UKz5orrYuVf8FZJdSe84TprFJUq1Jt0sehKWSTlbskRZbbbsWHJmmFAkCt+nbErXz7KXn8BVA8OfK775clfLcnjsccJcLSms+DIL+WTYJ0VwDDBDWn7jaq7WF/6ieeZXWgfj4XOqEonr2UP9ebXaMgWmro7z8wz6xouuhJmSAdd3jxr3UaiTXxupWSXZSfb5/hiCzb+LroBMNQwnV8spvP908FYCTIF7WXwZkNJ3LpcXjb0VVgclAwX9ARfeYnEzi+Ly9wZ5ETTEkfK083Snzv8JVFMUZHsDX7Sbmh17b0py16uC2VpR+ck2avlcnNyMiqtBKQTxEGL5Bu12Yn0qWqN1XCIjGTQ6mmGlURFLD1fPbIZs9vQSc0c0h0igQ1GcBdqH7MnrJ1XVU+ahsB6fTvUe0mnw8ze76+3WGAMHNy2KWpbMKA69uIatZu53Pa0phYr9VTaV/yguZ1xzQCdU+HikMXmrOnCXoqba2ZeUM9azeM6y5p97w/k3iS1WmCh83VRGWYlNsMPHL5IOcNYWtMq69yboFGlWOddhlud4ae3cq7uKmt7IEJAyUZii5KFNZaCKr0Rxtm+YrMC2MWcX91q+cBr/bbjarCxN6Lu2mmnCf0y2m+Ly3EnhF12do5828+5qOR0Y6XwRyWQuoKY5W5l5MV8lVB9KAJYJRfXppkBur7Mj1liiHvFX3gwrc623BwRUI2/Vn0ZpwQ+WwEU63fn2sCIxG6wFSMjJn5KV60aIdsy4xhbJr1KxgkJ4Y4nE1iODX0vwJjVBpiK4ZrLg4Iomx10vhLVr0i+RC3FLly63W2xw+zkd8nGjRFD5xRr7WW25e0dPlwRmXSE8TzkpTlbLKLtsg01hiXjfnPtNQSziW0uqVgfJhs7nrLUUqocWMsORHW5cDyX5kVOIjRQ83yx7rtpZR9OEoi5wD+JU7rHVoLGn3GirYODSdDbrkQDuYk3sa2Ws6qYOfWK75uFuJzy7Q1t+cjhF4Iuca6wK6k1CzatRdUCvnDP63pHENv1NJMrhmovrugMUbHeiEaz5YfwIFpTRpHLpbcyCNgB6X5gtSc5Ik1OWpnH67HbqYp02Dn4cWdt+L7wXHyWa8nKCLds1VrVbR9Klsgc10Ce57RCisHWU/EVBYxQxgZ3S23lfjtvd2fBYDg3SsQOKRUqXKd4jQ0Dby/tlpulNxMsulzcnPKFMU39ayR6/ODUxyQ68zLV71KD4GcUaNY3MTEisVFWawqbzc/Iqrc4y5qTRumdKwvbEbQcGYc493QzWnh62c63++4qivlsmdLMaHWU5w+p5vdeBvc9xFlvnG2aUGcvUo8tTmnD7lYGs02kO+KNC8qjtrHsQ3DisupcFjF7Sw06jvmqPWp4L7ulMpQVI108V8dJJpoLZ5Rfo6m9mJ399ghriI3rKzK3BG5L08VlNmyppSNsfT6EPcZpKMBmzdTl3EyZ9CIkSo2WV4Wc+yZhOzM/ovfEQIiyfvPC3qwYB48ZcX9uzxcVSetTXCpH93D29stV5OJmTglKwm7o+RAafKnSnEylhB23as7RSSGFnB7Pdwa9TGFHyszoKw5WOF7kmuwclsNeZ2gjq+kjJpjxduVuBQ+d+1y2vGGxfeWOcLeHrXRUso/Twl0bZwVBhfpUqrk8Wy9Pp2jDYterx2jRNtptLZk28vCCXSVufmlug8UBbXrqa2arlVuEc68aie/1QaKWBFMT9j7d8OJBCqt4OB1k8jzHCBKb7ZnZ7tDUi/0hOelBCI7UwGs3rz5zrhieLlmdMKft3JcDfNOHcXg9Ji5pDs3thF1gxx6HiDi/nublKqyPnKJupreDvBNoQY3pbesuMQLRqEXIp+2FW1LcHLt6F1KWY7YKp+RufZhvk+NGtdFsow6RXHFGI6iX6SLqpWVpRpRumDEbiTAjWzeE3eqydp7dQsaTzz2oVblir44m1jILkCix9aUcM/WZreaXVTWz9XBX1OilSPoz4qtW2/ORTh9oJGNjs/W7DbEhe3KPCELNUIwjGYxG55oQgk11nR4toAb8SmQwz+UIsg7s/bD0WE+kymWbr5L2Zky36mJLqBvAbeKNK5qnrkXOO8R38JN/M2ne8G1k0bdpa563V3mByL7Mnrc6dCu2iSuXdGsrpLi1JJqhomDHyFBgHbkaPX1j2lxaMEeyGlYZrB9oQWzRi1eykq8XQCTV6xT2mQPvJnC32Ie+x5K3BsM7dd0jUzTQpn4QCqt5O2Bo4wf9dhr2FWlpxgVt91Zn70BvZgLJN8mO9RWbFnOd3BtMJZ+V2Lre+hLd2YSpz7cZmiaWDHZrUSW17YmeQ+fY05kJNrdMHWzSIoKKV6oZqdK2uE5OldvmRpXMJCFEDNzSN34rI8eUvIaS6BeLemgSQaiYxbTASLDNU0TZd/lF63YyYiPnqZtXG/EWj9vJCNFuTddGO4kdpmdbOTGJ6OfERuqQ/azBeDkkbUfeexeqW+VnyspPhKrsg5xh1xaKd2wrdov6IkcIn2Ac7iTC4KDnKSu1uYZxN0tnzxeMCNN0Ydnh8bhM/Apux1PK38yOOq8rVFBqvK/f4B6N9DYuym/1BY1sjm536g/UOYhxszCokCJPsabDbZN2Olv0gDrdLp2u+dgvsjUCBdr7lEFq1hReoULS0lkUswAs9VBZsYe1cPWOfUJSvd2ZvdK2Hn2lzN6o/WBnUbqkMW2GEgnQpDOiUrNoVgiXnVO4/JVm7IFSV+Z5fluaXBYqvcsNVzC4nNNeK1m7DsUeVgduezQ7quD0pWlN1WaGo5zqav6m2uo+3R08YS9v93unwn2ubFGP1Il5cWt5EN3O8w63bcntKnrJ5f41YMtEC3dRnrPaYXWVp81VqWhjmZ45lMZOgua0K6pFmKk6XelnwsrqfLC5Vowx1um70q2VEGGZvaoDJSASFp/L+eokegOu6nCNJOOupkrZardc4qjezPOSJJvpSUqEXpRgdpfyw9ZM0BztVwU/VEyUzeadBBtj/MqTCOegQdeRQl8QhHTE1ie/aUWWWQCSB8g+5kW0FYFETH2jZ3Wk76FdtHM1VTommGORXzmShy0QA3ap5HVG7dwCU1n9hg6IIdyy2Q2czkFg+Ji6MPklmS61UDhGl0otcxtl3FUMZsw5ghgFRQimF0Km9K6PT3zBr822qqjLDA2s3Q5z42XmxeUU+EvP6Ej80i29UlMKTL7Mrit535PnkBOhj4ecsD9pc1jiSdjqSxmkxNjzbkeG28Z0T4FpePuZoNHOZXHg1rFKB+VpZvbkfBdNZ1rdNpdrgfYqhXkJ71C7PKYw/nDCKE+H+7u1d1YL0RPt5Navr06w8VOhNPZ0pxtYzqIrrk9TKUeP5u3G9gIGYmPOVPwtoyoCa3o2X0egwXz7llnhrEq0RPPV/fpWu+vavZYbt8GkuGtN7VCJ0FklVt6BAPXkxKNtPFQ1zi1iR7GqYbra+gtsyUgLM535YUUWSVVuF9kUQyNXIsxO9bbseaGgfruf+eUa19CwG+Y162lDwXHcjz++fHoZT7Sf59L/m7fW48Hg/9n55OMo8f0t1v1QGjj+lzuvL/8rlD9/eqm8GGJ8nNTWaRs+DzH/6pz28z/xOmQkODxeF4+v5Prm/dy/ccLxK1Ivce63cPLwVhdpez88/vTitvX49Yz67XlI/nIXPSvHE/e/EhU+KSofVG9N8eY5dfQyfoFifNME/BgCeN6Gz+PsTy/+AA0be/UbydBvoCpH6Z+vWMYj3/Edy8tv/wkKdLeymyYAAA== -->
