---
name: "rar-cowork-cookbook-configure-manage-loyalty-programs"
description: "Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_loyalty_programs", "rar_sha256": "9e5b93881d1d3e221de69d53c78f7c006cb1cf6df909f2bde460289d4a8ceff5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_loyalty_programs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-loyalty-programs:fac10165698ab458ef856401a71752c8827b618174a11486410e487f9cf8b3de", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_loyalty_programs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_loyalty_programs_agent.py` is
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

Manage loyalty programs Configuration Bulk Setup — Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 9e5b93881d1d3e22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_loyalty_programs_agent.py` first:

```bash
python3 configure_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_loyalty_programs_agent.py   # or on stdin
python3 configure_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Configuration Bulk Setup — Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_loyalty_programs',
    "version": '2.0.0',
    "display_name": 'Manage loyalty programs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b20f4a724994b1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureManageLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageLoyaltyPrograms'
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
    print(ConfigureManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V655LbSJbuq2Brf3T3QhLhCKOJibigA+hAECDhWhMlmIT3jgT79rvfBMkqSdvTO9MRG3GhqCqYzOPPd05m6rcXu2vDon75/KICO0cEO02jENSInXvIvLgUdQL/FIkDfxC3yNs6crq2qJuXDy8eaNw6KtuoyOF0vizTCDSIjThdeh/rR0FX2+NnxA3tPABIWyCZndvwLi0GO20HpKyLoLazBvHrIoNMkSgvuxZZXl2QIn6Ugg/IJWpDpLfTyHvQGiWrizR1bDdBmq4si7r9BMUBVzsrU9C8fP71Hx9eInj/8vm3Fze1G/jqZf6UB+zvAuwe/OUnezg9hRLCceUAzZHD5xLUflFn8JUHfOT59HMDUv8D8l//lVzsOmh++fwlR57Xl5fxn9LlSBuOmtpNCzzEtUvbidKoHT4hfHqxhwapQdvV+WioBlozDz49Zn6jVJTI38dvPz+YfApA+/OXlwKKcDfAl5dfkKKG/OpuvP80Uil//uVTWlxA/fMv3+g0nRMDtx2JQak/vT6fn2ThwG9DI//O9e+Q6sOrDvjy8p1y4/WQe9QTznz5FBdR/vODMHRiD3I7d8HPv/wZWTcEbpJGTftv0f31QTgEtgd1egr+y4e7kf+BoE+F3mn+OdsSuvWvaAKHv7H7gDwN9We07/b/b6TTKIc58Gbxf0run01A/478+qe6/U8TPiD+l5cFSKMeRoeTgs/Ib6+qvJz/+pP37eVP//gdkv6XZNSiq907hVeYpZEPmvb19defmvvrn/7x609dCWMN2NlrV6f/jOY/s+udzw8WfI76+ce5kP85T/LikiPvkY78VpT/Uf/+CdHG7P/2vvmMfJ8v44UioxJvTB8m+C5nGijrd3b85eV3iBA51KZz759hlv/nfyL7yK2LpvBbRHULiELQwW2UgVH4Uxg1yOmZ1F/V7Xq3+5R5XxH4dkx3CBF2l7aIUNtROoLa6PFRg8JHvv4f946jH90njk7esBG8PtDw9YmGr29o+PUTcgoh36KOgii3U0ThZRmBI/N25HiPjabLPvYjUyhQ9AAdZb4eAafpUvA35Ou/5PJ6J/ipHEY1vuTQLzZ0loe0IIOYatdROiD2HdCHFnyE8Aqx5B14x19d+Wm0jR6C/GkxFyI4uAK3a0eId+0HhjcfoNObIu0hLo52bJIoTREvqqGRinp4IHqXfx6Jff361bGb8Ev+AGISedSYZgIHvAuMfPxY1sBPoyBsv+TADQvkp99+/wn5v8j/NOtOfOQhw5JwNxgM5hTZqAcJgZnZZXBYg4xhAWHn7rnffn94YpQuh0UR5lPkj0WuHb3zXRiMGjzc8+YbqPMoIqifnH60G3IJoV2QqIXWgjnefPiSjyQKOLS+RA14M+Jj8sP0b85+8Bl90jxtCP10L5/j2HsEjs50i9r7hKx95N1SUN2xVo4eDYumhUFbgtwDuTvAmXb7zYV50SINzJvGHz4gXQNVHSl/dSDp0TgZBCe7/Yrs5zKsc0U6lvX6Wffg7CKPRsc/o/XxGhKpf4IxNnsj8QmRALQmUtq1XYa13YD7ON9+RASsb2/zIXEbycEFGSs6GH10z+h75O3/pJmY/9B8zMZ+RIWoUyJfOgLDKeT/b68ySs4LgrIU+NNygSylk2I+wmxssEatHz0ZbBoQ2HQ8cuZbI/GGOW9o/CVPI+iaevjbY6R/j6zHmAfCQQzwIIQod/pjjtd3ulEL42N0eF3fjfElf4P9D9Ay0DvNqAJM42QEheKd4fj1TdIQ5ur4/K0FQB6hN6oOgxopOyeNXMQHwLsboQ3rMbuejoDBAsZMg+nghj9ohUDqMBAgfQQKEcGohaXhbjoJZglsmx5eeB8ejY0VlMLrXCgtTCPwCdHHqIaR2SAOgN3ROAZa4ac7KSQD0MZQxHcLN6FdPoQZm96ngPboiyKzW/C9B54fYYSO9QXye08/SNWGvoe2vEAnwOy6Pjz7LufTV1DYbEyF+6Qf3f3UFfm+Pv1tTEEo47cSAPv0sbR/ZxyI2zUMzjHkYNFNGpjkGXgGEIyEexX/9CjEj0r/LsvnP3T6P/+1xcC9tJ5/9NxnJGzbsvk8mTzK31v1++QW2QTGSFSC5lsl/PjItY/PXPv4lms/EH7Y6TPy14T7gcQzqj8j+CfsEzZ+2kUuGMP2eUFbzD/OzI/U+PVLroBvTn5GwohuEHGd4b3IvA2BlSaoQTAOfhSdZqxVF1ge71h3LxrvgfBMkwfawGrRFN+l76jT6NaH194xGX7KR7T3xs4uAOOqJx3Fb8DL57xL0w8vuZ2Bf2e1M+IujFVojXGRBK0NO6U2Aven965pfPhxkXfPKAgFXvF5TCxY42CH+wF5b1Y/IG/Lh/uKLO/g+unXsVEeWcKh8M/72PcVpANe4IKtHcpR8seaaOzPnn3zH4UY8wlK7IKxihfvCTpy/AMReBMEoP4jkcP9xk6fKNG09lgZYUF+5nYD5fS6EdOh72DOwTSCIdrBCX9kA/nUoOpgLfZGdb/Z75taxUOX3+9maB8Ly99e3tBivH80Bo+4gRP+/e5ttOlb1X0dKdvj/HuPdTfxvTN9hepFY3X97lMwtgqvjzh8+QyxBnx4GQ1ZR7CA3e4L6ZeHOFCPbz0tpABR42MzdgsTmEaQEqzh5ahDAhHvOwbj68i7jx9vPv95I/xn6f8ZioxjOD2lOdZ2qCkLfHZKUxhuMzgzJVyWJRiHxlmcoWwcp1iawjFAsYzPuT7rkB6AUoyezOynFBN89AGU/93Qf707f3kQgPWCmNKQAgemDkeyLO7hHgkIAvcAzXlT0mVYn3ExjHYd3PVpz+cwziccD1A0RrCcR9msC3x/OtJ79ggPqV7fWvE3rzxg4BUiZxaNMhO27bIug1Mex9i0C0jMIV2AQ84MCbApR/osCyg4/33q0zOj4x6Kj0ELO0PYl/Ujn9+enh4DkabgSJFq1vzjmk84zXb0iaOEO7RO0euVpI8kKNIb0LtKLKa4aHhGwWcLa+euzHPdLNtho+OSqyWdffZy4RDJ9HzS7Jg0t3JvE6Vbt1z7i8JcOQN38wgj8y3K3hZZjGkza6jPSufF296jt81tV6n60B9OjqjStK22J3uFbnebmlV22gmk6IEwDFazdGDZurpaHYO+JNsptr60x3pNmn0hElW8cdbHLoyYbXl1jVo7aFFp7PHlCdBkEdYZ6PeYtVltouo0pdJ9TSnt0G7OnH7BDn1P03CSMUW5rg9VY3FlOLBjMiPCz64i1GZpD1sHZMs6vpZ6qexIRavUIV3nB1rJ0aoWplsd97ZO4k1PVWntDOYmYInUrHVHiNWuSs+blHZ7fTGcQ1CZ9ZbOiySXjqGx0ttoJoi42qY0X+FuxRYqyqSbmuTtKogNTK8Dd5DbsKcFo5pqa7M9R+cqLZtyzcwEIGFZd2ZW6jaTp/QFKyxh4C+hss02OkWAEGsGIPMHrVKY40qQeNxvsfNZSm78JNu2nsR110zVgpq0MGwrx6A6x/KVPDt6kRXb7XWrZdfe5ieieFqGzcpQnVirV0SBNaIKsi7b6ZtD7juC3qJplaeOPmd7nnWxyxEf+NzUi2lXiHqEDZxXWg3qywJvSU4l0ZbloayRbF2vs+dEh+dr1JT6wIWV1rgZc/PibF3lbDfbPInRFPTRUFQSodb9jpmztl2ej3o77w+qvFP3uxlv70DG7DVzN7nu091M81Eh9Qp6zZaLGhwvaucd54QmHw3JRxnHjpaEp5H21RgA24jnfNqlVtyJChqqME7X+5OGn08G/DlLZ0/PaVzFloeJqJfonEPnK1SMCVM2+S03KbSNIKL55HiZ5FiEonnM8BSoljRG1rHN7aan6MiYnrRNGd0LB+JqbNm6tR1pr/XrW1N44izfdZvTWSZqiWHlmaUcmUDD6fO5jpKF7jX6IiniOd6sgspOB8+2Zs6FCpSmvRRxIrHXekXthKm4WSoJdsHcLV6tq80mPegaMS15Kqtj/JhRmtYA/8BK+4A40zZ7Ogi1QCrh0Ox989zP6M2wlFVLjICt9RkEU1HgKHLheFgqwexA5Uk2DRZnluGizYR02dmlL6064g6GSavLWUVfIprcCExJyjMxLnciTE1brVOZLTOf6uZ4jbaKfY1RojzXdbdwrjeKKFF72W1lSyszg+S4qoxkZu/V880pI9kpM0E3mgXTeErX6a4xpm2lkDv8VivuhLuu1Vy71oqxi7vYkwIdhDyhoXWupA6M2mq66QWtvuDrkLuey93Slwt2shFQsGkXJb5WdtNaQddTgmizdeL7qrDZU2RRieiy0hd+Vd140qAVlhIxwXStoDFPBLWGOVH17ErzdoeDQCtHJUnpWSup02KaYIeGLRLC1oxqaXbYIoLrvtuunrsrRrnGHeirxJK6WCdlzrbOnALcNSZz1LkQTrGcWLiUerIArptqgi+OJ+J2szrcBOdOl42aZiyAuldzotaooSyYbqOIIF1JoE0oZq3ufV11bVDpMqFuFgvTug5GHDe7LtB5cbNir2SEx4GI+jlV9P1MZUJ7OZWuKXPj9lktmIfkvI2m2ZKTEsDq7MLjt0dZnBFD2QaR6tPSIdzXsiWcWjeYLzciWMYXM28FcuYUHRUM/Ox4mdft9lioSpLUrXo+sGv61PXzzdE7VmDOKpZZH2iJXzC7OegOgPPMAIuURjL7pvWdjU3SqMVp06Rsk1O9O/RkOvi92EyPujLbmIOWyDoJ0FiNlQr1irOVtzxlhkbiLW6NOCES7Dzv0MbyYpZL1h6bxFeY1kUikzlFS5IsDmdfRdliki7OZdqgqFNmKTYjgpAq470oabctGZXbxKhwjGhmtyvVL+JNuUulPHAXAqUXYc5vryZxMnHhdM5ujQ+WUyFbGoTt1cbGo+rkQBsJPV1TpZ9R+8omzKHYrW1ctm8SbhukRWC+Rk0iojui9Gq1njOpcVK7cxcSHGYDr583SapPLXd7pHBzdzG1WTUxOm4bl10n1trM2Jc0NXUFY4cvzgHvzRnD2k7JfCPdWmKfXKbxOrqmM+kSb243w6nmy4rrZ/ju2uiNOQ9QpSTX57VS1amzZH2M6Dbdmr9upEwRdHNYFzrKifxpxgjX5twbUR1Fjt56NboIYJUHQwFdf02W+a1jogub1ivukLbW1KVkw0RzZydfZ3ZHrmJguKkmnnc9j04D/jCt1lknSzrAZwt+xYSaT7u1jl1PVyqtlPzaaowab04WXx2n2kHIVTPYFavNaVuvqimgUCAkKdr5W1ysvfO5n88S5zIn1iklbENLVua0s25xChShHlw3Nh1eL6hueJZUrYE7S93JclCOlbSpaZzbkpebCwv0WsdiGWM3rpmFEs3gcag0mUNt1Q47A7UzMquqtd3Fob2ZdD52pBHwGKh2rsedTlovVaFz9NmuNqfihZDwQuJ3yszi4I2GL2Nyv5FV/bjNqSCkPcw6KMd8fm6NaOvFnmGvo8k+CsQVrq+0IikPZwmbXa1215BntVGvs7LaUddDzYbn/Wx5GWy9l20HGJNW0AWA8zUmTBah7xS9TtnURlyjLtuel/PQzZhJnh9XcactYUFvl6yOdpRv0RN2AauZaVosn2/ELIedqLuecmVNqjY7OZEmhfaZNhjOKbulzt4wWU2jydmFYI/8XhYvq8yXTOlwOWpLh+fNYl/yLLuoV9vDrG0X1txZ7b1TS6ghivq3KJcqrLEv/HEp6Qtzv7r22VLFCdBjM/MYdvg2Sd1cTUwyIObL1ZpjCGyr195QGlt7Kx07fBbsfP68nK2NmX/yBz2QtlhCmeKJ9iJlg568Y34SF2nb7DZbtAqy4rLJ50uhjfR5AivimVBtmc6NaJkYxE0V1xtaO2ALwliJ1Jx2TTKhGjKJd+6MbI9LhuM29QUOOG+OPSbs10YXZjlQKYAvhmNY8IfqFNW5WPrLgsa8xErmlHUoTrmoebfjoFnCVqQlMlvNL8nUSrXp4awUfKmQm11yjTTDkNLtFaxuG1Iol23PFWQ48S+nvV5p2xW+7g+zw9RjLW9pSwVcv83ymIud60ybDnv7VFnTPtlwynFZoLfalg61Tl6WDrNRMcPpuzOAvTDaF0ZieOflrsRyKt0NFzM94uiRms8WIkcN21lRMNshPXSHqUHso/Ta5fz8KB4bJcCSXl3zWTf2d1nOnSqY6nwOlwokSg1gq4fLY19yW2uunZX1Wig1mqNO0wOFKexaaCsjvqzUtZdpEJ8ofVJtMHpziqJdSCWpIBkdSQWSJwrXWPRFM7sVxUIZ0j09pIVmLK1gktklEdEw1/NyWVllQxDDMQ9ZD5en1llNDwrn7mxlsPYura8v1y00qhJN8ZyHUHaujCDTRK/hjWNVeM3+tI5vwp7ZBgva7AOHOUbby6GIoyXT7DzJFtTZwpj3YRPUm5QavEPEVfPe6wq8WaerxUYQDCPMCW/JszNZJrfXMt6GRda1QaCgjrqwhIC/HXAsHsrFxqiCoIyOmMCbMEWxs34LxNtK92qrWLFhrroZsWlVr17Qs7V02pAnPuX5LJuk2ZCv66rneHyeFotBcfeO7A20he7mW0yPIDrLmqnPJfE43R52+tLC1aPhn/f80KebtPYP85gh57KV0DSFFoWlaEJAFTVVzvGJqdTaQlkLK2MhFAwRc05qxJMOB+JlAlBZyYgaYzRqtaDkWdoriU8mFxI0sC5OyNXUXyRkf+v3IsyK+iIePCE05hjADqZX4tvtHpsulIbKwlsXbBNl5+jO0cMJ1aibrFkQdr1mSnxBKYKpT/f7U1D3lD/tYEO5Tpzc8gL51qK0QZ/lpbc+8Am5NViedLrdURDTXVW5y0XJ4fZmffU90ROu+WWWyQetlk4XzOomiQHAceHYfr5niF66TcmavuUFxR76SYvjkwvPRBpFn3B/QoV+XlwZm+z2vq8tTkVOUG0LnW4MogV7ZSrqr4BTWUhOrgM9ItFwTkXx0aRyvxXCBdh73XZ9YxbcbK7Ig3NVvEURg6mZl2QvcvvKM2aDKWwzojpW5CEsWHLZ6sJwvgnQ09NT3u9d18pm4W3LnvbbvnCGnm9NVN4d7RKQhdat5ZaRdldyZWqLfAcMj5yxcu4YFhvLvkQntnrVjltbvgJjyGTHm6mUROjRVNhWuzbG0d2qcES9OjCttyomNMnlq+gmKJv1xD3ZvJ2oM5SdqBQtgvrAALSMjJ3Rt/phu+4u/AEqxxzw1vEHNp2XTspeAtsl6SKPvY7ZUQQznUvecnpY5Ex/jPSikq+Hc7Xs1vqyFhT6oFcbZun2QKRYGMVBA410vsoktMIOLMsT7snybr3wgEJdw3VOhmeTUbd4ZHIMn+xVP8lzSV5m7hHiyFSYt2YFlhxzKWfMBFtcKVZehM7Cuol0cNhsytCp2Xjar4Mikpf23BKPB0LiT6bD7ni3C+obeUGLs0QIwf7U99TtcC5LkV23E5xlCEd0y7RbE5xRHsAgZl7i7CyPLQnGm8/Qea52K4De4nlPXy2xrmt7xeYt2efXnAyOYZ5PxepycdD8ItXlcZUueIZimlniGksjJ2GLBkT6as9J/XaseWNxpLx2jQ8dMTM6lL2R2zzL6ENLc6tTcuAqRc8LtuEUgjViJpyqy4Uyn1Rg5uA5M6jCDOfZW04NXRyWkTWAuKXU7RpUIFn35mk4erHvXsJJQLS4Ix1D1BVuE/qS7bg0nvge4KbszliwJ17mbrcLLS1uEQwkVukTMaJaf8KJFp2epY4uzcTvr9PBpUm524sW1BczSPpkLeyEG8j9NfNLfZDmmyJghghmYXzBtVw/7X3WSyoJeFZw1es4U/ImdVboTr5c9zzLJ5uJhrPuXl5cikiozxf2FhDk4rZz0NMB1JrpVJvpchlzhjoLh2TvYnv5uAjQ4AKC4KJeSIlSLXCN7cBOj87lQC1knRAZHCOBfIwHreJXwbzou5AVxWouOwN7SBU3wyUw6ziKDWa2uazDtbtzzOXUD9NZavhJhokSv6fc8pxs5dQmAqySz3kR23FSDTcMrpA0jnBhD8yefJEMok699SWYo9jubE4j06g7OTWt0iErbla2k1PqcZd9MhyumjYjbAPXxVU9xJzGr06TIpto3n7SmuXshnYGb1KzzmVODcefM6Wss/XmZNJ6e2hm7qYyG4pLnJihbBeuTwX3VuxY7wZYLlzhXV7IKNlw6fK2DXj+5cPL/fj35TOOsRj54WU8M3ju/P+lfePgFpWvT1IkQ08/vPzvbWo+NhjfTgXvxwDA9j7fuX/+C1L+48NL7UZQosdWc5N2wXMj879t3H78l7vJ4/ThcYA9Hl9e27dTk9YO7rvdUe51TVsPr02Rdve9bmjprhn/C0vz+jxyeLmrlZXj+cU7x8fLpgRu+9oWr1VXtOO7KB/P5IAX2e+PwfNo4MOLN0CXRW7zStLTV1CXo6bP46lxi3c8n3r5/f8B0mZk5aAnAAA= -->
