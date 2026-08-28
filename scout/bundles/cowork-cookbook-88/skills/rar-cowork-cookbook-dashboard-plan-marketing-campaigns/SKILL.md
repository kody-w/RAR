---
name: "rar-cowork-cookbook-dashboard-plan-marketing-campaigns"
description: "Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_marketing_campaigns", "rar_sha256": "5f439a93f9f2c0771c94410af3706c0026d4db1083cd34fa06d38277a1e61b27", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_marketing_campaigns_agent.py` and in the RCI capsule.

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

Plan marketing campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 5f439a93f9f2c077…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_marketing_campaigns_agent.py` first:

```bash
python3 dashboard_plan_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_marketing_campaigns_agent.py   # or on stdin
python3 dashboard_plan_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan marketing campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_marketing_campaigns',
    "version": '2.0.1',
    "display_name": 'Plan marketing campaigns Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fcb8c9de4b3bbaf9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-marketing-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-marketing-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPlanMarketingCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanMarketingCampaigns'
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
    print(DashboardPlanMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOj1rbmX6HzPlT5qirFjKgTjmgECCRGCZAQLkeZGcQoRkm+/u+9kZRZ9vHxPdcd/dCqqEwBa695fWvtTf764vZdUjUvX16M0C0hwc3zNAkbyC0DiK3GqsnAryrzwH/Ir8quSb2+q5r25dNLELZ+k9ZdWpVgud5UQe+HLeRCbZhHnydiNy3DAErLLmxcv0uHEBJNRYYCt028ym0CKKoaqM6B3MJtsrBLyxjy3aJ207hsoc9QVYfgd1oCba6Q11RjGzafoLKCOIwkINcH4lqoDMMASPGuUJeE0JCGY9i8AvXCC+CUh+3Ll59+/vSSgu8vX3598XO3BbdeuDcddCBeeZPOvgkH68H9GBDWV+CfElzXYQPULcCtIIyg59XHydZP0H/+Zza6Tdz+8OVrCT0/X1+mf7u+vOvVVW7bATV9t3a9NE+76yvE5KN7baEm7PqmvDsOuLeMXx8rv3OqaujH6dnHh5DXOOw+fn0BzmncyflfX36AgB+/vjT99P114lJ//OE1r4AnPv7wnU/be6fQ7yZmQOvXb8/rJ1tA+J00je5SfwRcH2H2wq8vvzNu+jz0nuwEK19eT1VafnwwrptqCEu39MOPP/wVWz8J/SxP2+5/xPenB+MkdANg01PxHz7dnfwzNHsa9M7zr8VO2fZ3LAHkb+I+QU9H/RXvu///iXUOSqB99/i/ZPevFsx+hH76S9v+uwWfoOjrCxfmoNga18vDL9Cv3wydZ3/6EHy/+eHn3wDrf8vGqPrGv3P4VrhlGoVt9+3bTx/a++0PP//0oa9BroVu8a1v8n/F81/59S7nDx58Un3841og3yqzshpL6D3ToV+r+n81v71CezdPg+/32y/Q7+tl+sygyYg3oQ8X/K5mWqDr7/z4w8tvACJKYE3v3x+DKv+P/4CU1G+qtoo6yPCrvoNAgLu0CCflzSQFyNTea7sJgV/bFDj2SQfyf4rwpHEVQb/8b/8OpAASH0A6fwfAe0J8ewe/b+/g98srZALOVZPGaenm0I7R9a+lG4dlN0mtmxBA4XCHvS78DJDo8/Rlgspf/j3zb3c+r/X1lzvMpw+E2rHrCZ3aPg9fJwsPSVg+7fEBQoeX0O+BiLzygT5RCpD1E7C8rXIA693kjTZL8xwK0gaYXjXXO2/gsS8Ts19++cUDen0tH3CKQY/W0c4Bwbs60OfPwLAoT+Ok+1qGflJBH3797QP0X9B/t+rOfJKhA2R/xgNouDE0FQL11ReAbGoiAH7d4B6PX397uhewKUGvA9FLozR8LAb5mYXBm68NkfmMEiTkhcDHwL9FXTX3NpV2r9A6gt71BUKnRxOKJ1XbQUEIelcQlv7Ullxgzrsny6qDWpCEbXT9BPVteJf6i9e4dxULUOhu9wuksDroGVUOfkxq3onA4qpMgfvfM+FxHzBpPrTQ8o3FK6ROGQnVbuPWSeM+ZUTuIy6gV7wtB8xd0EDHr+XUH8PJVffyeLgHEAHP+M+Qfp5iDmaAAmBB0L7JvtO4U2cz7x2u+Vq2z9R3mykUPmgFQGjcp8HUEP7xTKk2qfo8uPsPaHrv3I8oBM+o3HNQ/6vZYP3PM8V7P4e+9iiM4ND/X/PIZAwjCDteYEyeg3jV3B0fTp70moLxmMPAXHBX4l5Q32eFN6R5A9yvZZ6CjGmu/3hQ3kPzpHmAWN8AHXbMDnqzu7nzvaftlIZNMyW8+7V8Q/ZPwFF3GAORAzUOamBKvTeB09M3TRPgrun6e5e/hxm4DyQGSE2o7r0cpE0EHOG5fga0aqbSewYG5HA4leGYpH7yB6sgwB2kCuAPASVSUEwA/e+uUytgJghG1FTFd/J0mp3qR5wDCEyt4St0ANUzZVALShYMQBMN8MKHOyuoCIGPgYrvHm4Tt34oMw26TwXdKRZVAZL69xF4Pvye73ddJvUBVzdwO+DLcULgILw8Ivuu5zNWQNliqtD7oj+G+2kr9PsW9I+v5V3Hd9AHhZ9P3ft3zoFAJhftHWkn3GoB9hThM4FAJtwb9euj1z6a+bsuX/403X/8exuAe/e0/hi5L1DSdXX7ZT5/dLy3hvcKUGMOciStw/Z78/s8Vdrn90r7/F5pf+D8cNQX6O9p9wcWz7T+AiGv8Cs8PZJTP5zy9vkBzmA/L4+f8enp13IXfo/yMxUm1M2vU1G/taA3EtCH4iaMJ+JHS2qnTjaC5nnHYBCHr+V7JjzrBEB8GU/9s61+V7/3Xgzi+gjbe6sAj8oOyA6m6S0Op61NPqnfhi9fyj7PP72UbhH+j7Y0U0MA2QrcMW2FQOWAcahLw/vV+2g0Xfxxa3evKQAGQfVlKq1Pd4j8BL1PpJ+gtz3Cfd9V9mCT9NM0DU8iASn49U77vm/0whewLeuu9aT6Y+MzDWHP4fjPSkwVBTS+Q+zUtp4lOkn8ExPwJY7D5s9MtPsXN3/iRNu5U8tOu7fqboGeARiAPkEgeKDqQCEBfOzBgj+LAXKa8NyD3hhM5n7333ezqoctv93d0D12j7++vOHFMwbPSRGQg8L83E7dcQ4SFQgE14+UAs/+L2bIJweAcWCCASyICMdol8YiOkJ9mKIQn8ZxBHYjjIJJH4ZRMsADD4EXmB9geOTCZIAtUIpykZBEPJQC/B6p+W0aAtJJqxCOQoxGULCARAkCpxEKdenAxSnXDeDFgoKpKABt4PvSDADk09SHaZMf38fZySVPi3998UgcUIp4u2YeH3ZO710Spbxd4s0aMjw69nztpdZ5OFywMznawQ4uuYDNYkcPqpJZUTXjG3vVFAVX6CQF4fRtMqt2dDZgms2nUlajaDoe0Hiry+UmuzkLKtfohSNV5xR2ezZHbxztHCoH9DMhoC1bIqSRIO0uYBbn2QE5rmbzMOLVcCGrWr73idnVLjGiaChTKuDxeKmz3cWW3LMnF22yJbKFtgq9bjybRkN13XjNt/li1R9Om8DLixo54kbYrqTLhqBn8yISFPRSHticP+WYIbuDHeeI7BsqrC/PgV52qB9RLa1gBI95s0WLrejbiopR0TDqLYLDKL3Pm8OB7NjBOQoC4i/yrUWPyCI7k7nSbO3oxJwd90xiJxrja+PCF+v1xtwfMSGu/XJFjr6QdBe/Ip2WbljVcbNiBfhQUm1yyJJ3yVVXr/fehnX2wdF2O1S7VGp4JhJpOFNwX7u5fFOWqpJaNyaQ58quPAX12tTQhEGMMkeWGzgZuTTfSw7o+XWP3NQjRaDCtpH9rID55SHUbXNbmMN+i4vIdUSExjR9ZwMGGpBxGrrKG56SW6Qh8h7fXKyVdhaInsOP137tbXdtgdPuSFTg+VgYOe0g5smxUQSXo/pQE8I+1sVRFwMpU4/bCwbCSPNqs6IKvMZujtRHwUhamMLBtxSUwWCVF6Ep5foU6EvCwaJUaoQrbV+2i+SgUOmN5Snf3VbeSgwP9vFQoPzpEuD2ySJ5inGP5Ly7IO5OMzuTPielkaP5TJlpdjzwM05t1wd+LmE8nuyuvbM931xRUYpofqSDg9+EPakMuiPLiqxQi/7W7YqkSre5yd7U86zIV7qpnsPCsyhkabbeLcgHmISH8RiNpQj7Ol5Fx3DrFdtMsqKFnpxSLxpsmuYU5ZQSPIEMQ2TlAobIRZHd5PPJvSmsnZwJ6yARZ/+wDJ1erdLsJCimX84q2pvryeyqGrQ9Zre4WJEuXIrr0ie8hbhxznXlcBsL6VpyadjVSoYdZsgFI2F2Kl96rJcFcKokmQvvDqoQ7ogc0IaN4mubCm8deUj4o2jPa51TVNBG/MxhqKw7BkbYa+0uSjgrN/SKr/WR0n20GINNz8s2LqpNmCaydsFm3pwlUS5L8czw5tGq3iWRj9jLcztcFuxm2QsX8ziehVNzCxVZcA/quC0UI16W9badj/5e39NsOciKJ2hSudY0Kd53DkEro+uk6jV1YyUiF9tmRZBDdbAd4WiI3HHXJ9UwrNYOcZ5ZWCddwqJz62CBlhoznN3DuIMDwSMqw1yseTnAUSvuzVSXXLMJKnt75gg4xlfLgBRLZMOYtdw7gnMlmrU5R5lzow3iTaTy66I3DHKn6Id5xpZrcYXUrhx4M/HS657rJLfbdTy528QyPenokgY6b5UNnLreukk19+pzsrlLjkR16HvCk7ToQDnd2rzKXeDzslGfZsEQsEqBOalXLk6+cAAb74VHLWA55AS5HJWLsLqZF8bhOnlsUMO67RrhFMwIEcN1GaPmTVNFWLw8IXG7OwUlst0ell1Zjpy5XDibJL9JW5paW06Z2KUcacooDOvqslsRx8u+DeMxJjRUjSJ/NqYWVpqahXo5voguqkcmptRdsYuFWAf0lqVcvJXP29PREs+cqmdYxeojY/QCMuK8z8eSwe9qltfNfBDQjutSvo5XAj82ZOakNbPaW/ThcFRQpzRzOF4a6oLFbts6PVon1F+FuEfTVyyumaI74LdYmu135NxBj4TnoEUCJ0UQRJ66oPRbTs51w9ge89PacGhspp+zrJp5w17K0PCy1pKlFYSJV1xuC3erJsGNEiiG53dtezMG1IkITbrRqgITfjtEEofv9oLcYV7e02dhqbMba2lsOAENF+16HWcFYSvnVtouhwWGKPI2uW0XTA4LjWZXsnAsTBPRTCvhzCF1+228kYouiqklkMLai6BP9O0GOddoda0VZheXtAfgd7Pt604gQj2WN/F2ubidz6Gwjo2M9fA6JTDRv6XxTvVUysLURLfGJD/uzsoG140Kjxoq3N+cWa/I9sbWV6RpqRQ6wK6/ZnxmrjkSklmBcvL8rauffey4SrZoUu2NcO7YJoGT1WjKdkdqfWgrZn9wN2Rsa8d657ntgYz6cT3DC+CwXdbsyAN10S/xxrik+FUpBuzCMrFQqKVLke12XM6PcssJkiSUpldYmmr6GDOz+AbdC+ejYumW5jTzLlmRBrJcduze6qndkobdRapxTCoXTThPifU2rhNp5pxXhWHFLMtxsZrOxpFlA+oGpv0ciLvCuiIRRmokTlyd582mDqXbVqILT7SFI1MVQ4revNBR0W4PL49+cazUgd15OJ4dAxQppTJRa5bKhRSWtKCPCi/xlgPS9avGzOSkpbbdxb3ScokQ6+J8PqiGXqzKHSKB7trvenWXMGSHtl0png2sV0JTwM/1YUBXJkzWhn9aGLi595EwFqsD02KFNe63euC79jHdE8vbTnZSLN0Y8sZqDXbvWhs+4A8aHyO6s0lnnIjtb+QOUdMi5l2TmqNLZKj0WebeVHG9tGZdtkLGMAg9Lq81B5HN/Wq/PJkIQcr9YNJzfDby8gYrTkt/G7jrC73EyxgVCmVDYaFKIynpBLbU0ZqHeocUL03DHjzqZIucAl+OsemT6B7LfGadnnk2YWAyVDvQbgWf01o9P7fKdWS8hZEQ87BZnLhzrAR+7MeCue1UrT80RGnpsk9u82YlyGmFN/4oij3cHurVdgjr3rjESJRWEkkH57w4o5W54E9HDvRwoo4MhLkWcVGiOM4bQp+b5I2pnV5aK9FiezoQK5uVRDWxDDADWakA54NrhuvQD+Rc1U2qltWRXfShAdcLYqRPda2tVZXw0Dg/2ogE9gwb27rl7GK5Csohv/Gr9HjxjWKTbLSV2B6iaI7bUimlleIapyxAtau9rF0rriJ95bRgjgTJk3Mc7WaWyuM41fkevEEPe6YXj3BfOEa3Mu19t1k2J41FfRMrqrYMr2LHuqOH93ZgsLA/5xohQZo6loQWRVVq15n4oWIR7HY6V0ENJ/Rq3+kXWcVJ0jbUlSvzVL/Td4E263y4lOe3jg+XYL8AQsdeUgtvWNbSuBO9XKanlD5eq0haUweDz88k6Qm71WCUDOav9+yCmKOHk77NFarZsRgYrvqyTlhFWwWInTHI0EljzTpsWcUA0gOGlEZuh68NWFyN/MxALCfS8voIV6uTdLqxQl72gYUQbj9GdukhemJtTIGSTZ8dr/DN4K+wtksUuGddrC03Vn8MYKnYInrgbc5ssRGD2XiY89UlxtzgVOADeqgMqmE6h+QV0TzDOVMZbLmo90ZlC6qwzDnJ8dFZe9CV421RJ3p5DWLpyo1XCl1wfgb2TZ16Zk7Lk86VRRIgYCz3zkSAVi494AkWiAG7Z663lj81Oje6i+G2aJF11RNbMziZVXrkut2s1nzeStn0CnLfbfa5EXPsqhDxI7eM3SzmLmF8WchpixyWx8ppbSm5OmEKz+iSF5qUrBjRijyjG09+onEtSdfwSmGtk83H3SUJvOVlMTvt1rAkyeMgzI6GoIvRai1vQt7JD0tbpvtGbCrQtwQcQ4o4yoJAj/YrBeyN1oq3p6zcW+zHbjMf13qUxqRio1V/iY2Q3OMiRYgeLQ5zsRqaetEjGjLeEE/C+qt2u+LSbIiIPdZzKSlIWAhWHeUQ1blgd1SXO9mgVpe401RL7UvXWmX2jtBpwWbQxXmP0rcQE42rbkeD5YH22pHs5qyc9qW0wY/FPN2cR7BzyWRLQLk9YapEEy5D8nQ9xbsjqiFMlM2CJbya28jGBt0CbKRJ0hfYUz8qKN0EZe/BCQD3RSA4A7GHQT6ihXjBRA0V+2OxwA5rWixrcb4YVH3GiCup4YwZN5/z3IyudSekbzeKjL0g67NcpUVbmjGBcJZOV4VeDRd50zaSasxMV5q3m9JSDpx3IlRj4TLxEaf8eHO6iTTLSvrVQ3bB8mrqZH/CCST3+/xwGwIwvi27QMuFHa4BnVJkdbqKWxolBu1IE8YoZOimTzY7Z1fS3NojkUhProzqyj3NLAlxpidD21cUt14PUcpVqyGnMWQVSdgmChwhU1xP3/JiVCUk1aoic3Vcjo+Kqi9KB+y/sojKzzrtBMV6TiJzjFuldrdC6B3fMsgq424DLZ+qEG0plSKKTSsMtjuGyu5wY9C2Lpy+a6iZDYSKwaAxrIzOLQ0nvd5uw27RiSjrpgxH386zCAwmGC/X/u5I+XhmW8bg3uB14p5Cwp2zNZwul9fjcWZveuIU8Gf96vc279+6NZgxPbUUs+1CvNoW482oBDtubvwwqNe8OQ2aPjChu4xlV7UvXLo4b5SoyEJdH7LsVOhYHNaMlGI7yo6W3ek6kmtmtPDVKj43QYFyl+06Wikro50PKM92++7KnxZzZahUSaFYvU0x7zDqAR208YG6edegRUipd8rdseP16+Cq14Si4F3JukQgzpZ+kM6RUQwxlxCdEvMS3WaSy+mMi/x8VPWFqy0XR1cbOJsnhuVY7GGkQbMO8w8L2jlhEczk61a4AogmmiSANYDtiN2bqh5gIeLC/mZLkZ40dmJunlksHiNWZ5bbAET4QHI20qEbfitYp7mgG7UjNg53wukVxRd2tFfmNX3cl3BBiofFlts2HbXGDxx1xbwogOceESH2xaJ7llzcDiE3EzmdJnxNPc4r8XihaXQ9dKI751B9MMnkggVMV2LoBe9J0Ijag0NHA2zPidvxgksa7fUK2tcHOgEzZUqNickzCH6ubpXX6ovgttZ2nTU7Njv4tsfKfbSkbxE+qgzMZ7hsIQtL1+kR7G9O1njGxGo7qPBMEjwcxtI5HMbysKjG45CuuL0ezyv/cBKX9DIONttY7raqHx7DBHMyqTO9LUtwQ4iUMopg/HC+7JlxbaBLWCe2M5PAGDHGI/Fi2khlYldzUESGkbtsg/cdcygUzeP3NpHbtWedtFgZgzyreD0PkRiuNIMqrG65mF8ZJXB22YxEF6M20zu7ZFj7clQMbBlmRKa2fp+Rdn/jMG2TsEhD6PuBYK2A89nrYGSSrRay07jNrOaFat5mMgiXfrOvjBYhV5zLGfWWu4HusnyqblZXnqd0o1tHqcylpbzRV1pLzxpNbCLZRy7iUiKx8MTXgXchuRnSzhkxv2YMw/z448unl+lk+nm+/DdeLE/nff/Pjh0fJ4Rv75ruR8uhG3y5y/ryd5T6+dNL46dApcfxapv38fMo8p8OVz//+3cU0/rr433t9Frs0r0dxnduPP3J0UtaBn3bNddvbZX39wPeTy9e305//dB+ex5kv9wNK+r7qfibyMnpVRP6btt966pvzwP0+0vLIgxStwufl/HzvBmsvYIQpX77DSOJb2FTT5Y+X3oAA9FX+BV5+e3/AMXa/rDrJQAA -->
