---
name: "rar-cowork-cookbook-teams-update-plan-demand-consensus"
description: "Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_demand_consensus", "rar_sha256": "6b04fff997ca4cd30e48cfbf9753e25bad6b972b2c8b0e8a006b70497b657882", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_plan_demand_consensus_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-plan-demand-consensus:ce0b1f64fe9fa4bae0410836a215a16b2cf5805c2e52abea94bd37681c342a41", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_plan_demand_consensus`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_plan_demand_consensus_agent.py` is
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

Plan demand consensus Teams Channel Update — Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 6b04fff997ca4cd3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_demand_consensus_agent.py` first:

```bash
python3 teams_update_plan_demand_consensus_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_demand_consensus_agent.py   # or on stdin
python3 teams_update_plan_demand_consensus_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan demand consensus Teams Channel Update — Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_demand_consensus',
    "version": '2.0.0',
    "display_name": 'Plan demand consensus Teams Channel Update',
    "description": 'Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-plan-demand-consensus',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16e8075e38c33d49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-demand-consensus'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-plan-demand-consensus', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdatePlanDemandConsensus(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanDemandConsensus'
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
    print(TeamsUpdatePlanDemandConsensus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZPiSJbnV9HG/FFVQ2ToRlK0tdkCAoRO0AWisi1KhwsJnehASDX13dcFEZFZU9XdU2trS1iCDvd3v9977p6/PrltExXV0+uTAdwcWbtpGkegQtw8QBZFV1QJ/CkSD/5D/CJvqthrm6Kqn56fAlD7VVw2cZHD6Xzlhk2NuIgJ3KxG/MjNc5AiZVE3SJEjZQqpByAb6UI6Ncjrtkbqxm3gTxc3EeSIxHkDKtdv4itAZoFb3i8WbhUgYVEhlzb2EwRK4J7AC+QPbm5WpqB+ev35H89PMbx+ev31yU/dGj56uothlYHbgC3kzd9ZLz44w+nw4QmOK3uofw7vS1BBLhl8FIAQeb/7sQZp+Iz8538mnVud6p9ev+bI++fr0/intznSRABpCrduANTNLV0vTuOmf0Fmaef2NVKBpq3y0TQ1FD4/vTxmfqNUlMjfx3c/Ppi8nEDz49enAorgjsb9+vQTAtX/+lS14/XLSKX88aeXtOhA9eNP3+jUrXcGfjMSg1K/vL3fv5OFA78NjcM7179Dqg83euDr03fKjZ+H3KOecObTy7mI8x8fhMuquILczX3w40//jKwfAT9J47r5H9H9+UE4Am4AdXoX/Kfnu5H/gUzeFfqk+c/ZjnH2VzSBwz/YPSPvhvpntO/2/2+k0zgH9afF/5Tcn02Y/B35+Z/q9q8mPCPh1ycepDAzKtdLwSvy65uxXS5+/iH49vCHf/wGSf9bMkbRVv6dwhtMjjgEdfP29vMP9f3xD//4+Ye2hLEG8+itrdI/o/lndr3z+Z0F30f9+Pu5kL+VJ3nR5chnpCO/FuX/qn57QWw3jYNvz+tX5Pt8GT8TZFTig+nDBN/lTA1l/c6OPz39BhEih9q0/v01zPL/+A9Eif2qqIuwQQy/aBsEOriJMzAKb0ZxjZjvSf2LIW1k+SULfkHg0zHdIUS4bdog68qNIchVxejxUYMiRH753/4dOL/478CJNiMWvbV3MLrHyNsDCd8+kfCXF8SMIOOiik9x7qaIPttuEQh0eTOyvAdH3WZfriNXKFH8QB19sRkRp25T8Dfkl3/P5u1O8aXsR0W+5tAzLnRXgDQgK4vKreK0R9wRqby+AV8gwEI0qYo09VyIvONXW76M1tlHIH+3mQ9xG9yA3zYASQsfih7GEJSfodvrIoX43YyWrJM4TZEgrqCZiqq/lxdo7deR2C+//OK5dfQ1f0AxiTzKSo3CAZ8CI1++lBUI0/gUNV9z4EcF8sOvv/2A/Bfyr2bdiY88trAo3C0GwzlFRENTEZibbQaH1cgYGBB47r779beHK0bpclgHYUbFYQzukyG1b4EwavDwz4dzoM6jiKB65/R7uyFdBO2CxA20Fszy+vlrPpIo4NCqi2vwYcTH5IfpP7z94DP6pH63IfRTWBXZfew9Bkdn+kUVvCCbEPm0FFQX+vVelqOxEAegBHkAcr+HM93mmwvzokFqmDl12D8jbQ1VHSn/4kHSo3EyCE9u8wuiLLaw0hUp/BoNdGcPZxd5PDr+PVwfjyGR6gcYY/MPEi+ICqA1kdKt3DKq3Brcx4XuIyJghfuYD4m7SA46ZKzpYPTRPafvkbf90z7i0XMs3nuOR9VHvrYEhlPI/+fGZBRytl7ry/XMXPLIUjV15xFRY/s0KvjouGCHcJ98T49vXcMHwHxA79c8jaEXqv5vj5HhPYgeYx5w1lYwQvSZfqc/pnN1pxs3MBRG31bVGL7u1/wD45+hLaAj6hGuYMYmY/4XnwzHtx+SRjAtx/tv9R55RNkY/TB+kbL10thHQgCCe6g3UTUm0rvlYVyAMalg5PvR77RCIHXoc0h/dEEM3QPrwN10KkwI2CM9ovtzeDx2UVCKoPWhtDBjwAuyHwMYBmGNeAC2QuMYaIUf7qSQDEAbQxE/LVxHbvkQZmxp3wV0R18U2Rgs33ng/SUMxrGYQH6fmQapujC0oC076ASYSLeHZz/lfPcVFDYbo/4+6ffuftcV+b4Y/W3MNijjN7iHXfhYx78zDoToCkbvGKWwwiY1zOcMvAcQjIR7yX55VN1HWf+U5fUPffyPf63Vv9dR6/eee0WipinrVxR91LqPUvfiFxkKYyQuQf0oe18e9ejLmGdfHnn25TPPfkf5YahX5K9J9zsS72H9iuAv2As2vpJjH4xx+/6Bxlh8mTtfqPHt11wH37z8HgojkkF09frPgvIxBFaVUwVO4+BHganHutTBUnjHtXuB+IyE9zwZ0eY0VsO6+C5/R51Gvz7c9om/8FU+Insw9nGPNU46il+Dp9e8TdPnp9zNwP9kbTNiLAxWaI1xSQQTB/ZFTQzud5890njz+zXcPaUgFgTF65hZz3dwfEY+W9Nn5GOxcF9/5S1cLf08tsUjSzgU/nyO/VwgeuAJLs+avhwlf6yAxm7svUv+oxBjQkGJfTBW7OIzQ0eOfyACL04nUP2RiHa/cNN3mIBwPlZBWHzfk7uGcgawa3pGoO9g0sE8gjZs4YQ/soF8KgAxHuLsqO43+31Tq3jo8tvdDM1jGfnr0wdcjNePJuARN3DCX2jVRqN+lNi3kbQ7Erg3VHcb3xvRN6hfPJbS716dxr7g7RGIT68QbcDz02hJWKfSeLivm58e8kBFvrWwkALEjS/12BqgMI8gJViwy1GJBGLedwzGx3FwHz9evP553/svAeDVB5iHh1MqBFzoUp4LMArHWHLqEjjt4lOP8EOaxWifADThesDlKC8gmSmL+yRFuBQOxRh9mbnvYqD46AWowKep/y+68acHBVgzCHoKSUw9jArDkOMY36X8gMQAxfqhF3IMTQKC9txg6nEMAYVlPQywLoZNPQajOMab0gzLEiO9927wIdbbR+f94ZcHEkAJsiwehSZc12d9BqcCjnGnPiAxj/QBTuABQwKM5siQZQEF539OfffN6LqH5mPcwkYQtmHXkc+v774eY3FKwZECVW9mj88C5WzX26OeHsmTKp3cbuR0R1qlRVQGB7Fpggt7/7CZZfxxwOJ6YxOLPZ1AiGln/aGRlIHf6gI3D4mU64aarQ+WczG5fCaowvyUmTWjTdHtsOjsuSIUunEcEveiDitNz9T+QqrH/XUl9g57OO5bl+5rndSNohIPDEPb4e0imnJ/qkpJF7eWHnmLoyZT8Yzcs4l0JWis0Y8OTmapUabWJL2IGL7bo9pKSS+pk6USW+V2L7ql0dOWpE+3poix7VBO/Ou5REVlGl6ZitroxhUvSsruL9dI6qvGSPEG7BvcLnlxlW/26xDjBc7eSJS8p61dQJtlK5oplzRCqxpHN4lm1iKwD25pHcQbUIS29HGr3+PEisqS1S3bl6vDLtyZBGfLrtvNmMOl2rlZ5metL7d9ZQrYvjjTeOWqIR6k2tGlTXGbLiLbucx6mT8s2KHSgoW0Ny77m7g9HChx0d8OmikR6z0F8zpB99r2JPl9T97ERq1a5eDTPH/0uy3HlraTZp65tLam1Qpss6RONH6xpcgMK8JK+/OF3KTusTWW7oXnMj2Tzo7aYPi82lfZIRJ5IV05ddaHdLZjBL0eLk01N5RoAsolJSXzcysqonRe4yfO5CyPZtP9tmX9hZzNp0fcCxqyUn29pfupQx4o2mmSncTMejCg8nE2CEHk6DHvLqXCTsqrUkncMSvInu22WiZHiqQuVoCtg30iJ5QyHS6ZuToo4VQuaF+iwnqpE2fnPCSa4Z+j0qGjtNmA0yQgW2bqxqRtrw7OJOv3rBIKTFfr9bE4bQ7Gibn0MV6erZw87nq3LXq3KTNbnNxqbuWjPHOcRDd2oaCr22TNs7PV/tqsxSLicZRYbOpJfthiHXoDcrHL9xMuYA7HrdHEcrgQL1YrnZvKWEj0vrQvur/TWzZe33RXP68t37g6YRMy5MSCdFKRmNUhhpWmtTn4U48VZLCnLo63tuzhNJ07kjWf+/PlGrN0i1jo0OJLzz9bsdT1ernnNSeW1rZurjJ/be40MaO49Nau8HB1GM5b83Y+aMJxNeiY2cZixxSNEzgsuljT0HRLKfPEaU5kcqhmFw0IqOKZSXHEqy0aTpSuwCy50TcnlT14CjkxLlQdpBMtCVmclKdqBbPMygp2CTSqKea+22szeyOH3KwLVcxe5WgJCpmNymWRHFbdMTgVnENbhNTsQXSlwWbHcDOQ7PlmIZ51eoKmWdJnEssKm7RYTY6wZrqwLmB+NWlFY+XZ63xFxOpRJfea2OHzy35xtZp0QwcgoSQR30+Xs+CQLdpE2J6mbMFl7q3hy9tCX1HYCV3GjINF2iY/DCC2F8rhUk5282Us1XCxTO5plSXyQTR826p3A0HNDn4W50NpB3QrLae6SSerft4ExpG65QctqcuwEQ15et2VHZ4LG510gRkXCn7ZQqzAs8qozHxqSKFm8W2pqtPcxcV4yVOCpNX9hhUZVtbQi7faHmV1qodXwLuF0DAog28DgXEUgeP5M3WjM2W1WmvrPgj1Yrmt5tp2qxsCKq7jy0bmaJm5nTA8WWlqF0qL+Z7zVktzQxxzanIC8x2l8+fSPNNNbtr9itQtPKXbglMPGZEb2/i0aDa6U0/KoDuZ4VRtm4UFMucsUT5viZvFMhXcSFo1Eql7jU1uMXOnukvatU+6VybO4VgUjWqGGqNs5nM5thYqyw7HnSoFlncA64nvc5w0LEqHdD0Yy812w6tD7vlaUQ9LltvgXEKaLKrlsFKK9LHIi8HGhANzY059rCSkeAbedkcJXXGx8vMBo3x2vxS8gz/p2p3AY6E0nYAtfxg4k5dpSeA5dYtOHP62Z6V9fU7zPXvhT/lpOV0WywhqLLpHe2eYoMot44jNydZjMrHQ6bMzX2HrS3uINT6yqowp4hJzEuBwwWlnWrrqxczNpLT+wAa7+XY/n9i3VCdMeR/NwmN5NGP1pG6Ctb3fnfBdt9F15XLJ7HizLOkjVqZKcCvrEySz5YGXnjh8w+oWVq5n7Mnhet1W2wU7BZW5x/oVI7oYJ4FAY3m+nZ8dk2ZKT1NSuQtEdOEQTk8Xm9NNnhsDk4EWXehqosvnPKwabp2rYZ4wadNVdXc9Zd15JS736aWKk8SUSTBJ201LR4WVJziXMWAxzI5gWNzqJGgP7vLiZp7rysyMpiRH2kh6Mzi7Tt2KgVAVR8s6k5a47v2NEYTgOqXt1rD8bLdQs3Tj4PTZxXgyi+b2frBx/aawKmW1WbhcrXaBZgnEPPE43pzLvaKnCrs6ZjVLmM3EWEa8VlqFqWLFYlJpjb0exIo49kcgJjB2NFlQTQ6Ql5uqJ8Gm5JcaK/bUzF2s23lNOv2erqgmjYP1clMLlcnjx9k1odMmwW4L+jjpq4Aort6FAK6hEP2ymqPStDaT4wW03KqYS8eBrBtnSl+HQ6bEnOR0R2M/KROQc2sjIWPjclF2w1lcHLuSp4nZ/DawtYF1weAXTKHWN69dVraVGLpe1xCng/3RqqnFxkaxWmZ8K5BR6pSIswvGoHoVMutm0YeBwyduCxYlv9ps5ZbLsHpdTK3bZTqVN640y3mSRAeYqWg6ndWG2xidTcy7Y7wdklgTnDWVpFe6IEhiW9mplZEYXUNXrnqlPIAmb/jan+/O82juoC7bYrNdpCq7md+tk+G6JVZOeaO23MaWTGfezOTotpLxiZ9zQqLQTtpW3boWyyg/SHY2sEIJgo2Bx2frtC8v3UqJDuuDhMXl4WruNRf3Wnt3NEFmG4PVNhSqH5X5aaFO8KvqFTh1MswkUMpu0w1qlw8CXxpzISkUTslNibcm5qxMZj2WWtLOyzNzUqh+I6dqTRKirPZrNg4NrESp3cDTCzM+e6a/nG7zIYuWB1uQrXPK93qvXrcLXFwbzlxbGRYVaKu82IWJgJuEhZml2B9l23TKZgg4WWmHs2Ta6+Z85tnFiZxGohHUccbl5VnENk1tHGBXcrlK7uSYcMblkHnaxtMO9vkacApMZler3bZDDS2c48pt5knO9gg0OarN1b6K5c0y2W8WFDQFzdlWuZqeZVfTcByoprAQyayJtZuXn0csnigzlU71kPBibOcbZ1jf9XO1NKPNchGQhmLxwVFTV4p9L0x+s+rVfC4VErPVJu3UzhKcYblrOVse8WYVdqpqm6RICppsYDK22of7DJ9b6TwU981uOZkdinxtzDze0Bt9oi3CFcio7a0EWGfxNL4Ty+XJxLWLz9aNh872rr09W6qxps5muKAP0C3rRawvBN8PfDYgrCETuoWemmKScRdTvRTouT6iorRwRDqn6ca7yngs6EdibUAnuVQbbDZrq1hLKXtb6bRXUJapaHu3wsluraCbaJgGwmWN7zyAksr1LOZ5zlw6cWXsnaVOg37aSTernZyyhJzkl5zM+BbW5F2nbNou2GLOrKIAayqVFvVmswwu3iQv5LWNxnquLgk+Hjxju2DU1C88ay0JO19Yn7xlzBNhUeqHs+o0M8VSiCHpJ/XFbMJ8Kq4vjObOVtxsffRpw99PN8wtzHzeXCQbaS+v0fVQUcoutwu91LP9xND7DG8ifHde8waqKUYlVTnZpxRBo1ORKZYhEI8Y4QHVsG2cHU79vGjlU7/NErlYXJv54qxe+WlxMoQwvRE1JhMSKaFrCr2u4BewL/Y1IErK5677umRq+cS1w7YgQQmYmLpGQ0l4dS2syabshKl23p0rN/daLSgJSVphYJ0fO0XN8pPU6vJxz0yrvHGEqhYvJOFuN7DyRvHmbA9xuxQPXKrqsytYcquZSoG2b68q022ZsnWZtJhH7WzLbQ9CK+9kJpcv01oJyzPnirAFDARvcbsScFFpSk0T8rvMI4IAx2d4PEO1E00WzbAis2knFBwbooxXMehp3uGHqCT3KJrlEy1Pmy2YMszl6p1nDGHTrTWozNwzeSDsLLAqFZkStMWNPs/OQc0aobK0km6qGtej7ZhyPS91iqYX28255ruM67y5b50n8maqBYxXlkFNk6RyK2Sn9Rl/uj4P/sxt8SRO/OnV7BOottPtsi7opIWnKGhB9aFyDVhgzS5RQA5mv0NjxcmrWskSQiGompnz9LWd1DK94PZkdixl8VCYFtsN80l/PV9n3XGmrq5a1Drnml4a2La5kIJIXFm84jyUPOOzKN2ZoaczM2UvLrls27XanHGHRiCHpek0oMVnrBsfinlzO+bHSVMywFtd7WV4aBV+WKMHyz8azKSKzG29uc12ByoLao6/efGGXNP8xqAiy6tFoUyndlLrGXpEL9JxzQqn2YwcMBJErWRDYbf2kkOPJ7Pu8rwVNzdWIjVsQdSmsHX20cJDab88UtlQMZ2QnZwFwa84/QpWTr7lnK2QD72hx2vmtLVPdjRkXBvGXsLG2mym4O0pwowz1zjLRef3sNpF3VUml9NL6dXa+qaq4fzii6R17qbkjsS2Rzbokz119m5BQk8l4BQndh8LtNn0NODoS6AsV1MmdHRUZGSH50K9SvA2QF11QmHyxmd0zuFn126YEVdhtl8qwjXnzgoXU7wyndqozZ6G1XUbeMEqWVCOzDeXeWsTHcFND+mBViiMtEhQRdYxyivSPt2EdGjnZEyBxVZZnzYbeXJ1FldvaNWls7T46Xp7a2ETbyvnghMYLLZCW+FK0w+u5YoQuS4WIt4l/bqS5CnphSBFmSHA80kVaJMJXRKTtWIIgJmigRHRO4mrJrylHgi0CeN27eFq4ankLtcn6Ilcknsc7U/ytuImCxQV6LWmmaQcDGswyZj1Ul73/HWxWu74PLpUbVXfUJZQTvgaP9+ipp04LddVEDVENIOrft5wVhd3IgvklLJvs9uFt0mhAK2KTYY1k+Fk3O8jIp4sLiZdZasovmKwWgd8S1KzGeYdloVxbN01aAP4jHAvFy9QfS63CJIhsHyZD2a3v2Cwcc91bDtxJuaN5IUTFQqEecALnWTNq6/tZvt2KVPBZdkoG39b4F66BYeszLzdEA2JsXMmtux4yY1JONVtaXfWcuiO6idzPWCux9kBRftoe6qr+HBCWxcX+o1p0MGNarhsdfU9TMhIRrPF4eSeMnWS6tq0mS8rLyFv6W2j4h6XlM22bY/YVpGCkM+7LTZfCjFLg+VaSqb6dHkSiYnW6Why3EzPvXxVt5R0a5YMk8Va17shQaraYe0EZ5TiN/yFOua7cjab/f3p+el+kvv0imNTnHh+Go8E3jf2/9q28GmIy7d3WiRDMs9P/+92LB+7hx/HfvdtfuAGr3fur39FzH88P1V+DEV6bCXXaXt636b8b/uyX/79bvE4v38cR48nlLfm41ykcU/37ew4D9q6qfq3ukjb+2Y2NHZbj/8lpX57P1R4uiuWleMJxfeKwNuwqIDv1s1bU7y9n2fcT34zEMSPEePt6X37//kp6KHfYr9+I6f0G6jKUdn3I6hxD3c8g3r67f8As5YJsmMnAAA= -->
