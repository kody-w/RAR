---
name: "rar-cowork-cookbook-scheduled-brief-record-production-costs"
description: "Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_production_costs", "rar_sha256": "550b088a1fea0dc4eaa365a55da4502ea282d14a430811be4cacbe5d29fd93fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_production_costs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_production_costs_agent.py` and in the RCI capsule.

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

Record production costs Scheduled Email Brief — Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 550b088a1fea0dc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_production_costs_agent.py` first:

```bash
python3 scheduled_brief_record_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_production_costs_agent.py   # or on stdin
python3 scheduled_brief_record_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record production costs Scheduled Email Brief — Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_production_costs',
    "version": '2.0.0',
    "display_name": 'Record production costs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-record-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d096694a4c9bc15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/record-production-costs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-record-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRecordProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordProductionCosts'
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
    print(ScheduledBriefRecordProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjVpb2X2FyPlR5VJViEVt1dMQg0IZYJYGEXI4yO4h9X/z6v78XSZllt9sz7YmJGFVlpIBzz36ec+4lf3kxmzrIypcvL0fXTKGNGcdh4JaQmToQm3VZGYFfWWSBH8jO0roMrabOyurl04vjVnYZ5nWYpdNyO3CdJjat2IWSrEzD1P9slaHrQW5ihjFUNUliluEI7kOla2elA+Vl5jT2tB6wruoK8rISqgMXPK/yLK3CiVfWpW75NwgIC/3UdaA6g8omhRzAc4AAfee6UTy8An3c3kzy2K1evvz406eXEHx/+fLLix2bVfVdP9dZTkod7hoo7wqwk3zAIzZTHxDnA3BKCq5ztwRKJeCWAyx5Xn2s3Nj7BP3Hf0SdWfrVD1++ptDz8/Vl+ncACk521JlZ1UBn28xNK4zDeniFmLgzhwqYWDdlWkEmVAGfpv7rY+V3TlkO/X169vEh5NV3649fXzKggjkp/PXlh8n6ry/AGeD768Ql//jDa5x1bvnxh+98qsa6uXY9MQNav357Xj/ZAsLvpKF3l/p3wPURW8v9+vIb46bPQ+/JTrDy5fWWhenHB2MQzdZNzdR2P/7wZ2xBDOwoDqv6X+L744Nx4JoOsOmp+A+f7k7+CZo9DXrn+edicxDWv2IJIH8T9wl6OurPeN/9/w+s4zB1q3eP/1N2/2zB7O/Qj39q23+14BPkfX3h3DhsQXaAovkC/fLtqKzYHz84329++OlXwPq/ZXPMmtK+c/iWmGnouVX97duPH6r77Q8//fihyUGuuWbyrSnjf8bzn/n1Lud3HnxSffz9WiBfS6MU1Dz0nunQL1n+b+Wvr5BuxqHz/X71BfptvUyfGTQZ8Sb04YLf1EwFdP2NH394+RXARAqseWDAhBL//u+QGNplVmVeDR3trKkntKnDxJ2UPwVhBYH/D4wCfn1A1IMO5P8U4UnjzIN+/k/7jp6f7Sd6zqs3APp2h8VvDxD89h0Ev91B8OdX6ATYZ2Xoh6kZQwdGUb6mpu+m9SQ6B9joli0AFWuo3c8Ajj5PX6AwhX7+FyV8uzN7zYef7ygfPrDqwO4mnKrA+tfJ1nPgpk/LbNAY3N61GyAnzmyglBcCnP004XQWtwDnJr9UURjHkBMCqaBBDHfewHdfJmY///yzZVbB1/QBrBj06BzVHBC8qwN9/gys8+LQD+qvqWsHGfThl18/QP8P+q9W3ZlPMhSA88/IAA35oyxBoNKaBJCBoIEwAxi5R+aXX58+BmxAb4FAHEMvdB+LQaZGrvPm8OOW+YziBGS5wNHAyUmelfXUwcL6Fdp50Lu+QOj0aMLzAPgYtKvcTR03tQfA1QTmvHsyzWqoAulYecMnqKncu9SfrdK8q5iAkjfrnyGRVUD3yOK3djcRgcVZGgL3v6fD4z5gUn6ooOUbi1dImnITys3SzIPSfMrwzEdcQNd4Ww6Ym1Dqdl/TqVu6k6vuhfJwDyACnrGfIf08xRz0adDFU6d6k32nMaced7r3uvJrWj2LwCzde6MHqgyQ34TO1Br+9kypKsia2Ln7z330/GcUnGdU7jl4+JM54b2XQ6v7bHFv6dDXBoWRBfR/PIhMejObzWG1YU4rDlpJp4Px8Oc0Pk1+f0xcYBh4igG1831AeIOXN5T9msYhSI5y+NuD8h6FJ80DuZoSKHNgDnf+IAWAPye+9wydMq4sp9w2v6ZvcP4JBP2OXcBcUM7Rw5Y3gdPTN00DULPT9ffW/uYxkAMgC6G8sWKQIZ7rOpZpR0CrcqqyZyRAurpTxXVBaAe/swoC3EFWAP4QUCIEHgfevbtOyoCZIDJemSXfycNpYHpECWgL5lP3FTqDQpkiUIHqBFPPRAO88OHOCkpc4GOg4ruHq8DMH8pMI+1TQXOKRZaA/P1tBJ4Pv6f2XZdJfcDVdMwa+LKbENdx+0dk3/V8xgoom0zFeF/0+3A/bYV+23f+9jW96/gO8qDGH/n73TkQqK2kuoPqBFEVgJnEfc/TR3d+fTTYRwd/1+XLH+b4j39t1L+3TO33kfsCBXWdV1/m80ebe+tyrwAg5iBHwtytvne8R/19fuTO5+/V9vlebb9j//DWF+ivqfg7Fs/c/gIhr/ArPD0SQtudkvf5AR5hPy+Nz4vp6YQy30P9zIcJZUFVW8N7y3kjAX3HL11/In60oGrqXB1olnfMBcH4mr6nw7NYAKSn/tQvq+w3RXzvvSC4j9i9twbwKK2BbGea23x32tjEk/qV+/IlbeL400tqJu6/vKGZmgBIW+CSaTMEXA+GoTp071fvg9F08fvd3L24ACo42Zepxj5B0xD7CXqfRz9BbzuE+84rbcAW6cdpFp5EAlLw6532fatouS9gY1YP+aT+Y9szjWDP0fiPSkylBTS23amxZ++1Okn8AxPwxffd8o9M5PsXM34CRlWbU5sO67cyf0vSTxAIICg/UFEAKBuw4I9igJzSLRrQD53J3O/++25W9rDl17sb6sfe8ZeXN+B4xuA5JwJyUKGfq6kjzkGyAoHg+pFW4Nn/dIJ8sgGIB0YXwAfHYQumKBPxXBN27IVrmhiBmzjumAscRl0TpVAHWZgLDKYQxHIXtmlbLu6gtOfQmGcDfo8c/TZ1/3BSDTVNm7JJZOHQpEnYLgZbmO0iKOKQmAvjYBVFuQvgpfelEYDLp70P+yZnvg+zk1+eZv/yYhELQLldVDvm8WHntG7OccGqg+3sAs+WYjrPhHyV8TB2DPUes8vY1qq5VlYOmlDJYhMY0U6N8DBhdnDiIXhiDastxiqrZH5Rmehgx2mDI3KOE2N5lJn+zM89paoLNtzzFa1fm9zWhQuPEuMhD47XyoB1gdzXQ12zuMsXPKYFbZEg56z2vHmcbvh1ntknGdlrjTSXtUN/UWoZaXi0pbmxu9B6E5UwXCcFxjZ7RDRPF168uXERzPaXdULvrXVrwCcnDvfbUcCY+bKJy6ymFT62PWVOU0TbCgjuesemSUucmididYl47Vrlm9hAVcsSkfpMol4g1YejUSZuwabNCkPBLstai2VzrTS5QOL2Ms/4YoHQyvIkMquiHjXYvZB9KuoCpyLXcoOHlBUuF8tsW8O87JSCZqJnK7lyYW1m9dbSOtTSyAMdyodMds9ogtFcXVFIoVdVr1W8UVEdSHY0CURyfd5HdOz4qLNj1ymHH5NASM8LMHxVM2zpqmqEYM1RMFkmKPRAv96qwt7iix2NWBeLvvIDrFcgJ7dyaQZnYUuaw86qrcgsWUxi7O12vverg9xZFp5zcgWSYG+ehcJErlLUYtLpdi3MLVD/6BscRY95d8i5y2qIF6iNiVxxNUlXXtHoLE1TdRWt9Ca17SZwPXhfOQ3Boi7GsW6VSOghplMy8MszFm4CrbWkyJT7wyVueunU6ktTQ6wrnJ9X6G49H3oNVXPBhz3a2RtEf5j3TiTwWtsrlqVWS1rYrqggoG0i0OPC7YirN6YwovNVQpjDQGnhYnG+XnonvZYOc5CDPWpoEur6A6jL8OqQKXIdRzO8OZtzlivRuMxU1evhtje9zvcy9qDMYlG7joRCchvcG6ztzPWMnlnAt9YIFkwyzOh1E9hogV10dHU2ouom5bFhJfnQpWhvk4etvBHNBN8d+HWnzvbWvhY4bz82rKOa5NG2w3RM9M7RE/MQ+2Ksouh4u6wsl9uzKx87XvdqrkXhNkst9gCHu1pproKqaUcUbEXIQthyoSlbmyMZnzY8MiOdbuTmZO5d992p36emJJD8ZuOdBNi2YPhIH9KrOI5KbcL7RpuzSkCtBh5WcW2spLnvqdhJHTLN388PS/VwO0sYf6u8Ul/LnLoLRjQ86evjmMtXdG/WwXVhschVEUFRMZ3nIDqXwhPirdk4im/tztYUZxfvjO1e0nb9XMCXgZLV1A2lsptszRVLEHpe12lZRwag9g7NaeyIdtdcpnDaOtrsRVqX/ey6FRrSWkUjG+i3GbYprpKuJOatvBXbdZTvNptrZo4qNQvKsMrX+wKTL/t85TX5dhHHF/ks9A5Cn6O4ux3xYr4bUVVIdV0lWy5qbGeecyfOTm+BC/ssHSMaY5VK4fYd1skRal1WDILJeJwXi8a2uXNLWwXvaXwvRDweo0yzKnOqn8sX0JKS+TW00tnN3riZP5jWloL37o0Rsl4cUCG5hYrHEJflqYroMMQclqCpkx2Ngtt62nbXtvxFNVWqiRgtDY6qHtSpqbHHnDL4PiZKbY7zmoMEhcJHjthtZmGR+0SUbbHt9cCUMe6FSU+tpWZbjdEor7xTRNmNQehittDHBCeMio7a1TYKz+phz8CSSvJiN2fYZLkiGQM9BWLHrnJpuWl3x2WtUwVJNeTueGYuBrdximUjRYcrPOoHksOSqFVF4Uixep3o7n5Zn+DMHbvMO/kqha2kfUJylSBJ9UJc1/a2DdDoYCQXZ3ldYzThbVOEFjU9VE+CGFu3Uqnnp6HkTVm1NLx0IkM9Vdp5e8lOOKVRZ2NrYLbcBfqaXc1ZfE5J58sFI5HG66jZUEpKi7HLRe6tt5duGFpPWnZHlS2NSN+ZaNqlLFHtREUnSktGGYmpb/QGidiQ3rnM0RQ07QSvY9Hiyw3GF2qeKf1a3x007CSHR5dZpGkgqjLJpFhEZwbP3HRWExbuWUkYd33xkVg7rXDpXLAs5yiSLhbczOXrxgrCGNmJvLlSTztqadClYraGnsOIl4JBrEyOI25uDnozk1h8GRunmCyNhuVSnxxdpqrwetAP69OG9WJ7lOpMSS5lEMRtcgRT/XXmnBpd4AmJS6hoz6p4EZ843Bhl26I9MrHCbbAxJQUFLdYV1+ZBvJjMQjjIwmzj1yNBxo2f9vPlCuOEpcOQxVARDpFpoIEYvB82NGxdazwIl/CozFO91kk1W1wp1tU66wgiusqP8G5b4Gazk4U0CNhYEwgjy4N88P1ddXN8ablSfIzY98Reta5x3Z6GyF9tpCJVl5e2CM2LVPfsXk07fbe9MHnSxvKYuq6EgFxaGsfQqKSWVZt5dDzN4AWsHwTiyG/3mxgWlgYzF7ENximl5Z4YKbQbtI14jE74gdZOJ12QmqU8eoSba7zIjxIei7vtiTf72FHOmhct94GDn/PNfCUpVuHzvYLwsaTv8IURJgKc0tTVkHv9YoqpoaWgllD2qjqqfAmKKLmp+VHFKyI3OniVzUpRhsU52XjHbV6pMEMc3fmtckm2XGYkmaar3qY4dVMwxws9w4qCqRG+BB49XDQCl7dee7v1Wj2/2lwXlS7il/6ptfYprIayj+C4lIRbeETPXorUVItR12rtnvheri2v1ixKTDNUrlUmd+nSE9SAvRY+Y5hyktZ1W+DHU+ct1MZOOk7UujRU2zRGHO1GwfFJZ3h0qROymOt4upC9I6XGJbvJ0IIQfELHWKrBnOXRR8M1Ci8vB25XH4vMP9N2kW6Wc3WxWO7EwBO8oVavlwyPu6Ywz0xzE+DErmwZTXaV37fjsh79HUA1mWSrNGtybUDmPd86W63ZLpVQMD1nfW0YLx5PbjS3ttKuP9R5os44C5FS/uSstCBP9+uE7ZnaU5L95qj1tokK6ZVdq0KRL4BTk6jDt3pZ+dXxMkYOszaGKtyJt5O9MgzPlwalULixTrR5PoRiwnjuWJDiPtbpc3M+SOhZ4Pv1de+2YE5rYTz126FOSQ7P1kgRjOVqPYqWw93cQ3GcWVVukDpMV8mciKoMTDDorczXyrhG9ytnvk+zJJ7jEa6t2wXBuktHok7GhT0Rw804mYpxkFe+mmOO2KtiHC1QLV/3JxMeo13jVAuGWGolWZVuu4PPBk5KWLbcHAxpTuGKBIvS1rM0u97XfRwh19qUcFUb1mB28nyR4GHd3/TqIc7kIuMpnbDCuRwbvFFsxzA8gfrZys4Zp6+Li7ur4eKyKsxE6rUDsT4mCXFerbBQRI3d6FCWqQubbb/p88MVaUgVP7luwxEHBM7UUWlhcrsHYwUaDdRejU+EsZCvmx2qZhszoHJn7OphWTOFZVOJJm4bEQAWm8IkwAWXwwhCpLgqIZ1tKxXsbXlTuE4PrpKwJrteGzBYsklaBYgJa+fI0B2/8fDhcOr0xbBGHZZOTaHUYFtsNuf4QkVX/3RcmHv5lJNnXE80hr8YBhf4dsKWg81s0XIZtmf1vN9YfG/YhZQ7ogu2bNkCzPbLiuFgiSowQvHJza3meouJd3t1l1zEfKiOt5i9nJmUWCP6wrsFYICOb2qYcEcs2PBOqo8z/BzuZxwmYYeqI29CBrZnrYYggSfvdwW7X3vCFYF1ADyOxmowuZfYDWgTaBUNyvEmdPiO8lTKyXEZQ9zW8tHMtRqRmFkKt3DWMdpyG5K+BItNQVENs7GsQydyV7cfwzzib+hCNG8bwhmOuSsEMeyMBp52crpLqKszk0bU5xDkopuYpGlMNyQhiK0QNsZV0+cUSm0XJ0ZV8WF5vlotKUq+gjizA9NZ0bYlFERIsO2yF4iwXUXmYV6jexuVb02ww2hHb2UdLZzA9uTtfqCITh567zhSc99H1li1Va1yZqsjrc/nM7WeqQK8L4XTDJnPhBRehy5Bk3MwBvgDueeCvW3KMGIzMwmO0wgn9kp4OVxtTTw1likoxOY27HeHK0bVIW4xjLYgbYq/nbgZN2ylweqPTj87KUQzgmEpdhv8Iux6m3OkhnBAXoBU4XopKxJbDsi4d6nFeriJ5yhZVsHVsQ4kslEtPErbvljSTdY4jIVvCaFvmyoTNrvVhYYDapteMZ0JPCIdpKi+FcxV8IxDM89PCKYacpAM8DkjpQPILeWwd26LRX2Yt2UVX+YXb7YwqOOQtW0tIv4mq3xXUeBGDubWWMFesks6gl6W/KJfl7tl3V9TUC856V70SufsthE5IekGeYEablp5NeUnaHgEkyWNFVdLPaaL4EKA7cEZH3apdmolC90hrloP+GzNBTv2VPVgM5Y169JblUJvK55oc/R+SdldMaZdJsrUut7FyrLzNkfvJiWCskIX+MjxYHaqDcKNLLFb1AQteGhnKIqStTd0i/pyviz4cuTI/Cb4i0BmBVFHWTVDkeokLMm8WhZbtqnmp32gYrZZ9SI9X+tI5HDekqR7xxzbDjs2/ap0rzUmokduhYlIUQfR9toaO9yIlkjQMgS+3M5G+1bI6y4NRhNXdB/bHnYXNR9GhBD5eaQxfYVv+yAjKQXlx/NUqGWFzbzxYpsDhQBHd1yc1ZuhIvGcDAxx1gRcfGlP9NYhAuQabZalbXAruz1lO3pDdgfe3zK7wgVZaRMg0z2UXzGyfpvzygHXoxRXeorK8JV8snQDK4WFk8DobHWmDE4lYzpYuMvt0BHzjcVVsY94exolhXIc14SysMWZEi8WyG0W6Jw1CxdG0wBSmQI1IlkM2bTYjR7mza2pgnostl42n3UD3fcbCfcWluWyCG1oym69jbfJjs+6tXTTL7SAl7OZfdoXt2Bzy9C2SYoZS/Zt78HKSeWY/LhFnLlyu2WL/c4KMdvLB4IQusxqALiXkmEVHq7lrNmyHKuLNmWIbLA90IxPr09gLukk6nhd9qMZmbFqdTLOKTqaCCiMmYp6I/TisPbZbF5bhKdo7GH0KSXmbR2RwAxKwVS3rERG72p5XVasjWVDNqRtMZqH5LBx5CFUuXQorc5UU95C9fraUcMI29ceoVGaHumKmbdKt2rA7jl22dmR1GwDlwRklhYb+XqmkUbFVbrCj64NdmB9yy74i1Xs1pabzCKw22n1y9kNKQ8lLjuqu8a+ojBeycNmga3xo2EKmbg7synZW8sLBpLraPJOn89XrlJ5Z7wcG1lFJCS5IT2RavPZUl0X7crs9yrDvHx6mY6hn4fJf/XV8XSw9792vvg4Cnx7xXQ/SHZN58td1pe/rNlPn15KOwR6PU5UK7BreB48/sN56ud/8f3ExGR4vJud3ov19dtBfG360x8bvYSp01R1OXyrsri5H+x+erGaavqbh+rb8wD75W5ikk+n4f9g0vPI/FudPa1yX6a/S5he+LhOaNZvl/7zsPnTizOAsIV29Q34+Ztb5pPNz7ce0+Hs9Nrj5df/D+1VUujbJQAA -->
