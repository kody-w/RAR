---
name: "rar-cowork-cookbook-scheduled-brief-finalize-work-orders"
description: "Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_finalize_work_orders", "rar_sha256": "a3c02bb4e9a724add8613c3dc9cf5524e187a2ed35136a8f929f18d127d3926d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_finalize_work_orders`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_finalize_work_orders_agent.py` and in the RCI capsule.

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

Finalize work orders Scheduled Email Brief — Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 a3c02bb4e9a724ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_finalize_work_orders_agent.py` first:

```bash
python3 scheduled_brief_finalize_work_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_finalize_work_orders_agent.py   # or on stdin
python3 scheduled_brief_finalize_work_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize work orders Scheduled Email Brief — Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_finalize_work_orders',
    "version": '2.0.0',
    "display_name": 'Finalize work orders Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-finalize-work-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '857b73424625a6b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/finalize-work-orders'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-finalize-work-orders', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefFinalizeWorkOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefFinalizeWorkOrders'
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
    print(ScheduledBriefFinalizeWorkOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOb1pb2X6FPf7DT2EfMg2/dqkZICCGBBgRCxCmHYTNPYhBCefPf342kc5zc5HbfdHVVy3ZZwN5rXs9aa6NfXpyujcr65cuLDpwCWThZFkegRpzCR8SyL+sU/lemLvyHeGXR1rHbtWXdvHx68UHj1XHVxmUxbvci4HeZ42YAycu6iIvws1vHIEBA7sQZ0nR57tTxDd5HgrhwsvgGkDv9svZB3SBBWSNtBJAaNFVZNPFIqOwLUP8NgZzisAA+0pZI3RWIDwkOcB/SA5BmwysUBlydvMpA8/Llx58+vcTw+8uXX168zGma78IBfzpKJD3ZHyH3zZ05JJA5RQhXVgM0RwGvK1BDiXJ4y4c6PK8+NiALPiH/8R9p79Rh88OXrwXy/Hx9Gf/soXSjEm3pNC0U2HMqx42zuB1eESHrnaGB+rVdXTSIgzTQmkX4+tj5nVJZIX8fn318MHkNQfvx60sJRXBGW399+WFU/esLtAT8/jpSqT7+8JqVPag//vCdTtO5CfDakRiU+vXb8/pJFi78vjQO7lz/Dqk+vOqCry+/UW78POQe9YQ7X16TMi4+PghXdXkBhVN44OMP/4wsdICXZnHT/kt0f3wQjoADvfPxKfgPn+5G/glBnwq90/znbCvo1r+iCVz+xu4T8jTUP6N9t/8/kM7iAjTvFv9Tcn+2Af078uM/1e2/2vAJCb6+zEAWX2B0wIz5gvzyTd/OxR8/+N9vfvjpV0j6vyWjl13t3Sl8y50iDkDTfvv244fmfvvDTz9+6CoYa8DJv3V19mc0/8yudz6/s+Bz1cff74X8jSItYMIj75GO/FJW/1b/+oqYMF397/ebL8hv82X8oMioxBvThwl+kzMNlPU3dvzh5VeIEQXUpvPuj2GW//u/I2rs1WVTBi2ie2XXjlDTxjkYhT9EcYPAvw+AgnZ94NNjHYz/0cOjxGWA/Pyf3h03P3tP3Jw0b+jz7Q6I397g79u47NsD/n5+RQ6QdlnH4fgU2Qvb7dfCCUHRjnwriIqgvkBEcYcWfIZY9Hn8gsQF8vO/Qv7bndJrNfx8R/b4gVJ7cTkiVAM3v45aHiNQPHXyYDEAV+B1kElWelCiIIbw+mmE5zK7QIQbLdKkcZYhflxD9ct6uNOGVvsyEvv5559dp4m+Fg9IJZFHtWgmcMG7OMjnz1C1IIvDqP1aAC8qkQ+//PoB+X/If7XrTnzksYXw/vQJlFDRNxoCc6zL4TLoLuhgCCB3n/zy69PAkAwsKQj0YBzE4LEZxmgK/Ddr67LwmaAZxAXQytDCeVXW7Vi14vYVWQbIu7yQ6fhoRPKobFpYpSpQ+KDwBkjVgeq8W7IoW6SBgdgEwyeka8Cd689u7dxFzGGyO+3PiCpuYd0os7cqNy6Cm8sihuZ/j4XHfUik/tAg0zcSr4g2RiVSObVTRbXz5BE4D7/AevG2HRJ3kAL0X4uxSILRVPcUeZgHLoKW8Z4u/Tz6HJZ9WLkLv3njfV/jjNXtcK9y9deieYa/U4+u8GA5gEzDLvbHovC3Z0g1Udll/t1+4FHqn17wn165x6D0Z73Be/1G5vdm4l7Gka8dgeEU8n/ZeYwSC4vFfr4QDvMZMtcO+9PDkmOzNFr80V/BBuDJBmbN96bgDVLekPVrkcUwLOrhb4+Vd/s/1zzQqquhMHthf6cPnQ8tOdK9x+YYa3U9RrXztXiD8E/Q3Xe8gu6BiZw+dHljOD59kzSC2Tpefy/nd1/W/pjWMP6QqnMzGBsBAL7reCmUqh7z6+kGGKhgzLU+ir3od1ohkDqMB0gfgULEMGOgde+m00qo5uiWusy/L4/HJglK4XcelBZ2o+AVOcIUGT3QwLyEnc64Blrhw50UkgNoYyjiu4WbyKkewoxufgrojL4ocxi5v/XA8+H3oL7LMooPqTq+00Jb9iPQ+uD68Oy7nE9fQWHzMQ3vm37v7qeuyG9rzd++FncZ37EdZvcjeL8bB4FZlTd3OB3BqYEAk4P3OH1U5NdHUX1U7XdZvvyha//41xr7e5k0fu+5L0jUtlXzZTJ5lLa3yvYKoWECYySuQPO9yj2S7/Nbqn2+F8NHqv2O9sNUX5C/Jt/vSDwD+wuCv2Kv2PhoHXtgjNznB5pD/Dw9fabGp1+LPfju52cwjOAKU9od3ivN2xJYbsIahOPiR+VpxoLVwxp5h1roia/Feyw8MwUieRGOZbIpf5PB95ILPftw3HtFgI+KFvL2x0YtBOMYk43iN+DlS9Fl2aeXwsnBvza+jMAPA3a8gHMPTB7Y+rQxuF+9t0Hjxe+ntntaQTzwyy9jdn1Cxpb1E/LefX5C3uaB+5BVdHAg+nHsfEeWcCn8733t+0joghc4g7VDNcr+GHLGhuvZCP9RiDGpoMQeGIt5+Z6lI8c/EIFfwhDUfySyuX9xsidUNK0zlua4fUvwt/D8hEDvwcSDuQQhsoMb/sgG8qnBuYM10B/V/W6/72qVD11+vZuhfUyKv7y8QcbTB8+uEC6Hufm5GavgBEYqZAivHzEFn/2P+sUnDQh0sFeBRBzSwwjXpQDvsATl+D7H4KRH+h7vBTRNUADnWIcAPknjJONwAU/wAc75OMH6JE8wPqT3iM5vY7mPR7kIx/E4j8Upn2cdxgMk5pIewAncZ0mA0TwZcBygwG+2phAln8o+lBst+d66jkZ56vzLi8tQcKVMNUvh8REnvOmwJ9bVIpdnmSA8JxyH8dWQk1RbqEScomm6YKZKiGVETChnR8yVts33inE0qDqeCUG5C7wlOtg0qxvngZ0P+jpy1tN2s9kPu8sancgd8PVZqYT8PCnUdjNZreftOW/35io/J3K8ryXLscXSlK5dpU4WPZaXVXCZ4NqNiylsUA6mnG0yXjtdaXOrqVhOEQ0v8tS6cuW9iK71dl8repUN8ZLMw51J4FeTx47nRGIzYr3r9pqVLktLkH1Hqc21ReiUl3gU2LIMB+QbwXWK6wVyQ4PjtrRCxTDyPT6cL9HxdvZNuQKdR2DGKW0q/XrrQntyVvicXxuZvXINx030zGFR0o2NVN1qvXHIz/tulUcDsFyFOh8XUXw94oxEGanWR6bqLg3PzUGXqRdzDmcmR+H30rpexp3rFpx22Z81/7b2CGcSMzVVWyvbZnbafn3acyEnA4meEx4zN7oMy8Ic5wVlni2JAGdTVfN1V/OYI0D9PTYdWn1rC2FdEtXUPLlKMfVo+XaOV4eDZysMZvAp6k7lc2c6psh5moPne3JJrEzJ7JwQ3WyP9uy00kJCdo8L7djax5RctozuKNvGWuB5fWnNyl6Z4XZ23db7Vap5B8XU7KFdWiaH63xj0w1vbTehvVqe24GxfZRny/3J9TGpoS/skre1uklW7JZU93lVzM0FhNPtEtPC5HKzY+t4NRa0njurat4fK/GyEbe1rtw8k+0ND11TSb0I0HUa2SsaLPtW29zkeekfhs3CTPLFcaiuIp1MyOBgWAxbdjerJ3QyiqjWkXR3YS91BTt7NxWVdMw5uLh+OGaSuXFNmdzjaXXjjrLD60dqqTDrG6dse4y7chW+kYRjhfb+oZhzwSRJeKHcJDpv0vgkC1I+g0ailBTXmVol1QNVpE52rCSD2BDzNF/LYGnvrokxWQvnJSZkV1k5dqfa1u3+oPN75pCkxqa5oLNiG+PlabYx8Dal8OuKDK+9IGgUHLUZZa9MmWV+nfvLWGTdfNdL2DwbyPWKaa49lU/jK7mhjX3oB4TGqxNrw+x7vTHUmKXFZZVax+VRLa5KrtNan5wmdXE+2JlSgD2JHvidG5vl6notgsNEGa5sdrylzeEUSHKLBjpuTc/d5RqK82m26GNsgOl1EDlDVynuJIQUoYRSqQStegu0wdAszNksjeAMSlxIwDkeInNhGPOtb9DCabrSTuvdhMVFd135WIR7ZaQegoA1M3pxHi6yuLL9cHI+l36hc2RVHVETaMp6WDtn8jSdJ9HB3iaxze/O8H5UGEnmorkx0M6ePq0EJSzOoottt/GCKuZHnVEP+aBP88l5DzTqmEgzjsCPh5VmLZNJHdDaydRWTEhaTOYxGVZcVc0Bm7mrC2vgmtbEKbuclWe+cK6V1tvNTrybW4ukoQ+htiKxJqT9FeSzK3L3mJxORHqTOdo3y8H1cwULGH/nODHKX8vgFihL9dQly9vKXUED+WetCugNdsidq425NRn650RoGZ6lQIj68xakyXDc8QqQlAW6GJrk0A/yNS0W1rlKyDTdH/JFzOXS6ca58apezOVCOddBOjWlIYgpMInjXnR8wjjvvA2GBhdhsNeT3LlZJn/sDrZbMqXANOf5lg5V7bhI6IFQljNp0EpRCGlld8qWvCOVRFv7eLFd75PBFxZ4tT9i+D6q+4ZZe3M/svu+W0swwlcEO2iSmlfygbQpY3a9YXIdi2nsZ9dpJhJeGhIbnr+x4m0TF9HCpnGeRw8c1eZr8bpUjplxStxtN6kiI83ktYaZwBWoVBbSZnM5qLeen0DRrgRNJzy2EJedfrFIyg8mJC1NAIpuapBNVjUqq9ZqQe+xxfJSk9eDh4VCSUxlPbdLDovyfSQZTGdCJMAWsdIEVF7mxpHm+7m1c2IGhG4b29rWoDV9qW1QZUUv5vnZwRezXpqmnBIOpD5HI9k0ZcNOr1LfyGwrMrncUtbllBkHjRpc1IZZRewgvGp9aLApsyy4TphsQ13xDqAmq6OnSrjp1Bsy2x4d6cqdOZJZClK60JKtBeGgtGZBMl1QZy3fdMpiqTbcnrNWEJ63E086z+aZk0kkt7c0YqskSqHNDtwuNrJ9fiy7k6Vvuhs+bK4SGWtiyjiXxjosj+lsRSyPKzwR+ri8zbmOXq+JNBj2fO+Gs5l5ElPXY27tWbcouYtTsNrVBsYdIoXLUIdzTIAt1cEW5GzCUKGTT8utKu6BmrdNHCtcezLy3BIkSfA3hnidpm0sDMIOnbnLslhWmlacB38r7CehWxlM2Df83PKrdblTOZ624+mwW+1DqioJnNh3OGYujlicrmd2n9ZJOB9gV9zQJx2EyV7va00MDWHDqnst1ZkFmpPJLl1nOXtub058K0wDww8xYbSnLX80mSZO7ZuLHcN5aWlgYJOzKJ+3sRDzq1N3lsJJhe1TfuGkZKxXNefq4Xzu1KgTCl1GG9Kh3GX5zsd04tTyohFW7SLd2VJ8Xh5KdpnJy724JfJostZdfcKXehredhu5wlEpPPYq8KGbnYU+qwZG2JNTGqfTzSKla6PdGLZht1urKCMS9S6WTgpUf3ZMtYpnF11KLkSymZ0cqikuHkWSuVxpvC91VdvZ6E0aNpWx8RvQqk6IE9FGvYpXm8fwMJ6qUVjutC4JOl8l9Cy1WQHdSyGMjt2wKNFEgol3Ywp20YTrGKxuw/pwyVaVyot0aenz9lTip0w2QSGWDGkO1+XZZLEy6sKuF2lzWuBMbWqazrQJNZ2p00T0BzxwJsItD/PCQctUb3a4bqN9vzr6cTyTJ6traUC4iKLbKZtHiy6bTjdn3dkyKTnMc5fgD1HKsat1PJ2s44KPDoZ6GDyz5Zf9tHflKqdXdRkDXLN3auhfJYY+R8JwyNeJcVUTZRdPXXPTNEdtGw2LqlBmdqF0CmvlVwkXNJppuGXP8MIg+hgh5i5W4YdMMKkrxW7W5fmkh8q6jO213Z7gkGVaR1jXGePWW0MdJPSMLRVMsmgYZg0eah3dd/JCzRxs2VRL94jx6nyCNml13lyJqK7M7ZYmNnOfXBVlXgTexKtU0r9Nt2LndMpZixT/aDfLdntayqK+xA9dSpULfTCc1enMVJJuD6mrEs3SF6Y2T+L1EXNm1oUnWkxIVk1hccqB9/jbOCasCp3cmbZvXqq8WorAuTiCwgkXW1VTgRh0tZ0a1exyjkM6wEsUOjuac2VqdHtFL8yuA6p0i5XWiYY1kYkevQNRGvltvRJm14WrJnmHlrulcl7M2QXEd9hwTm045QyXyrDidqpuJnrD4dolXu21sOXNugphftSJLcI2bTZI1iYgKbET7Wi4md4FLK8FPd9YhxYV8dPMXveTgRCDC7mh8NJZzlVuPXPowiytZIrfZu0uCy749IJ1O9veTx1CtBnYrG8FUrfz6+ncMdODn0lV3C+w88QoNtzqMN1Hnb9dMSuHNlljsZKp0wzi+jyeEUF4O9XXPDuGuTh3beyIqsXB6Se9PjMHH9tNKUGuHNotD8WUbCcaJebScmc0uopau1sfSef50Io0sxyuPSqfD0fiIEa5t5W3Z/Hgom0Bptu5ma65Bg3nGV1c4FTg+6FlmmofimvOO3Jp5go5flWw5CoH51Asbc4hHWx/8c9ezYGERzNKTrA2rfgGD+SJg7srchi2t4HS0EvASmQ7G5jFahJ0Q39aA2I780/DToyziu8okijm50rWleNaPIRcEc3Wobswty5DE+7sXMttrcHW3A1UWojXrRKPTe3SX60nrCdsozm4JBln+nSzDW994BNkuxSjTtiiAml1a0GX07p2PHFWJbyzWl4vvlwvrh1+XaO7VdsGsx3MZLPFYcZVEepFdXd1c+0S4OF2j9HJhWVddhJPmV29Qosc37J0NUkq27VuXb4FOH7BDoxjkca+rCmJchRpIySeJRtDyNGKm3sCYW175WLs9JmWMA6d4pFw7YkyNeV8zYiGDtKim1GzXRrQp6IiL2teW3XFFKUW8sw116kv7zDANrJ5TNMwSToLY4dCXqkQpmxotSzjZsCgojYfJG/WSayHVlQ4sZqelD0bnR9V8tS60xl16VCspkVaJ3O7mklWWPWT3fWK3i4tKfSVoEiXTdQdEyfsQcz7i4g+RpPiEJwDtAkAdd1lhe4Gu/V6Nz3YIRME07M/I/iC3h7Uvd/hLHuKr7GA9vUhvB1hvq0HbpMca9ixw0HW2QIP3NRJsD1ZB3aqhXMJXWf+dscdqUi7trth3qkLhZgXGNeulOPyBprLQLNXLKLU0MvO/mVHSrNCrRV8v5XZWPAXKs9RjS4JiQZ2yoWqZT8slocglLL1ZYNRETelq4XQhmgw39hDOb1xeEHSDItTp+hymuEn6aTyVstzpien+36vQJPo2hRvGecEJ6iIM3pTSiZBuqaZxEmVBYualnjEVtj8gsfk4UhufdyPl0cKlg2QZoRC2PX0xC83QwCkYSej5+lmgd+GrQfomXRy4w2f40PD+h0pel00C4u69w7kxphcU0q+RiXDbQnldpxFapJcrLaGM7bD8WZEnvpZFjaLIWVo340CbNNFfHa4HPy1T6O4nS42tW8d5p4FMAkkcLhTe14QjhY/wxagLPxiH+532/Q0yW7lZLUzvaJkQApiWanh+EHannRw2EKcgfm09Ae08bbizA66ywQN2uZCsxCOLdQK2FMkBPyliLCznAsuASjfGwL1iE8m2OmSLSK8MGc8yXK3xgJuSxZKDiclTpqgBqF5YnIBbKzh/IpUS11NLTBfncLFViRUpmNlGK9Ykrom7PcwX8UBp1h9oJOoNttpU2Uj4polJTcOXS2jEg8G/srO61utNSsyWOSe2S850gr9QwT2kgS8cAaim8OFc2wxxTJxrcU6PdBXZt7mwRrHK21tEROWMC7uNpjxx1W/iFTj1lX8kDH+8SSg8oFCVw5xETt059s9I0wdapfEDDYFLmWne5PMtIuSGLNNoRlKVFBHrSCUBDszDtHQILLZTqAG2EqypXMTJiza6oFgW4tiuu2kc5DucmJgkgjI6hpQBLVsLoRXa6iUikuW9g22xFKn6cRidcF3oblF9dxgWJo4ob1yRTeW4JVK461nFbs75fuqanZC4TKzSOb2p8AA+x3EKdlapywABn9bXM6qW/jMSd7WMOkCZrcnNiesEgTh7y+fXsbD6OeR8l96aTye8P2vHTQ+zgTfXjHdj5OB43+58/ry18T66dNL7cVQqMehapN14fP48R+OVD//Ky8nRgrD433s+Ebs2r6dwrdOOP6u6CUu/K5p6+FbU2bd/WD304vbNeMvHJpvzwPsl7tyeTWehv+DMuMdUF9iD3xry2/P32e8jD9EGN/2AD92WvC8DJ/nzZ9e/AE6LPaabyRDfwN1Ner8fOsxHtGOrz1efv3/iLVCtsYlAAA= -->
