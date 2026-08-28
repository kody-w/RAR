---
name: "rar-cowork-cookbook-d365-hire-to-retire"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire", "rar_sha256": "45f50e5967de3de38ffc7d775f5a92b695130c30661356eff7cb68c6af4bd651", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_hire_to_retire`. The original RAPP
agent is preserved byte-for-byte in `d365_hire_to_retire_agent.py` and in the RCI capsule.

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

D365 Hire to retire Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_agent.py` and embedded as the fenced Python below (sha256 45f50e5967de3de3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_agent.py` first:

```bash
python3 d365_hire_to_retire_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_hire_to_retire_agent.py   # or on stdin
python3 d365_hire_to_retire_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Hire to retire Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_hire_to_retire',
    "version": '2.0.0',
    "display_name": 'D365 Hire to retire Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-hire-to-retire',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-hire-to-retire',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b1ef1a2229f366c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'hire-to-retire/d365-hire-to-retire', 'uses_skills': {'custom': ['d365-hire-to-retire'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365HireToRetire(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365HireToRetire'
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
    print(D365HireToRetire().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abObyJL2X2HOREy7R/YRiwDJNzpi2IQkhNiEQLQ7bHaQ2Bex9Nv//S0knePu233vzI2YLyMf+wioysp8MvPJrMK/vthtE+XVy+cXzbcziLeTJI78CrIzD2LyLq+u4Fd+dcBfyM2zpoqdtsmr+uXji+fXbhUXTZxnYDoFsUNmp7FbQxiBQ+s4szPXh/4D0tqiSAaIiew4g0Q7s0M/9bMG8vvCrxqodvPC96Amh5rIhzZx5U/fK7+ZvvmZ96nJP4FfUFHlrl/X0Cegxs2vamgJ7VHIrny7viuL49Aeexvl11BQ5eldpBi7VV7nQQPRbR1nkwz5KYuxGzvJw1dgjN/baZH49cvnn3/5+BKD7y+ff31xE7sGt15YYNKk2jFX74qBCYmdheBJMQD4MnANjAnyKgW3PD+Anlcfaj8JPkL/+Z/Xzq7C+sfPXzLo+fnyMv1R2+yuZJPbdQNgcO3CduIkboZXiEo6e6gnKNoqA0ZCNUA/C18fM79Lygvop+nZh8cir6HffPjyAlCt7Mk3X15+hPIKrFe10/fXSUrx4cfXJO/86sOP3+XUrXPx3WYSBrR+/fq8fooFA78PjYP7qj8BqY8ocPwvL78zbvo89J7sBDNfXi95nH14CAZOuvn38Pjw4z8S60a+e03iuvkfyf35ITjybQ/Y9FT8x493kH+BZk+D3mX+42UL4NZ/xRIw/G25j9ATqH8k+47/34lOpoB8R/wvxf3VhNlP0M//0LZ/NuEjFHx5Yf0kBilkO4n/Gfr1qyZzzM8/eN9v/vDLb0D0fytGy9vKvUv4mtpZHPh18/Xrzz/U99s//PLzD20BYs23069tlfyVzL/C9b7OHxB8jvrwx7lgfT27ZnmXQe+RDv2aF/9W/fYKnewk9r7frz9Dv8+X6TODJiPeFn1A8LucqYGuv8Pxx5ffACdkwJrWvT8GWf7v//47ZtHcvG0g4OAmTv1J+WMU1xD4mXK78ie+igGwz3Eg/icPTxrnAfTtv9w7z35ynzw79wDbfI0AzXxt8q8PJvz2Ch2BqLyKQ0CsCaRSsvxlolJApGCZovJrv7oBAnGGxv8EqOfT9AUCjPvtL6R9vU98LYZvd+qMHxykMtuJf+o28V8nG4zIz54au6A0+L3vtkBmkrtAgSAGZPkR2FbnyQ3w12RvfY2TBPLAAi4oEcNdNsDk8yTs27dvjl1HX7IHYWLQo3bUczDgXR3o0ydgSZDEYdR8yXw3yqEffv3tB+j/Qf9s1l34tIYMyPqJONBwp0kHUB/Cdqo2wBnAfYAe7oj/+tsTTyAmA8UO+CcOYv8xGUTg1ffewNU21CcUJyDHB6ACQNMirxrAwlDcvELbAHrXFyw6PZp4OsrrBvL8ApQtP3MHINUG5rwjmeWg6oEwq4PhI9TW/n3Vb05l31VMQSrbzTdIZGRQFfLkXg2fVQJMzrMYwP/u+sd9IKT6oYboNxGv0GGKOaiwK7uIKvu5RmA//AKqwdt0INyGMr/7kk0l716Y7wnwgAcMAsi4T5d+mnwOqm8Kst2r39a+j7Gn2nW817DqS1Y/gxsUZ4DKvVwPUNjG3kT5f3uGVB3lbeLd8QOaTpKeXvCeXrnH4FR4/74p4B6Nw5cWhZEF9H+575gspHhe5XjqyLEQdziq5wfyU6s1KfvozkA7AIHwe2TZ9xbhjWDeePZLlsQgjKrhb4+Rd389xzy4q62AySql3uUDXADyk9x7LE+xWVVTFthfsjdC/wjC485ewJ0g8a8PxN4WnJ6+aRqB7J6uvxf3u+8rb0IJxCtUtE4CYinwfc+x3SvQqpry8elGENj+lJtdFLvRH6wCzmhA/AD5EFAiBhkGSP8O3SEHZoJUvEP+PjyeWiaghde6QFvQy/qvkAFSagqrGuQx6HumMQCFH+6ioNQHGAMV3xGuI7t4KDO1v08F7ckXeQoi/fceeD78ngTv7gdSbQ/4+UvWTTzs+f3Ds+96Pn0FlE2ntL1P+qO7n7ZCv688f/uS3XV8p37ABslUtH8HDgSyMH1E50RmNSCk1H8GEIiEe31+fZTYRw1/1+Xzn3r+D//atuBeNPU/eu4zFDVNUX+ezx+F7q3OvQIqmYMYiQu/vte8T1OVmvLukYV/EPVA5jP0r6nzBxHPOP4MIa/wKzw92seuPwXq8wOsZz7R50+L6emXTPW/u/Xp+4l7Aac4w3shehsCqlFY+eE0+FGY6qmedaCE3pkYAP8le3f9MzEA0WfhVEXr/HcJe6/IwJEPP70XDPAoa8Da3tSlhf60Z0km9Wv/5XPWJsnHF8CC/l/vVaY6AOIR2D9takBuTAwY+/er955nuvjjlu6eNSDdvfzzlDwfoak//Qi9t5ofobfm/76Dylqw+/l5anOnJcFQ8Ot97Pt+0fFfwAarGYpJ18eOZuqunl3vn5WYcuaNg6dq9UzCacU/CQFfwtCv/ixEun+xkycT1I09Ver4vYjUQE8P9D0fIeAtkFcgVQADtmDCn5cB61R+2QJkvcnc7/h9Nyt/2PLbHYbmsS389eWNEZ4+eLaAYDhIvU/1VBTnIDLBguD6EUPg2f+kOXxOAbQFOhUwZ4EHOOzjK4L0fAz8LIPAJT2SBLftFeoQKxzBYBeDCQLBcMIPAtJ1iKVL2MHC8QgcAfIewfd1KvbxpAZq2+7SJZGFtyJtwvUx2MFcH0ERj8R8GF9hwXLpLwAi71OvgPOetj1smYB771MnDJ4m/vriEAswcrOot9Tjw8xXJ5s0SEeNnFVF+Gdc2VatZeY9jzKmYaxKSVzYZ+rK+mO9zvWq5g7DjkMOrhpKvO4irKxEs1xdXS8IJl9jIS9QNJ5jaicgyVgPnjQPLthG2jD5LlxJw75fzM8IudWrtVCv6dNKujXneL+Lb3NyyYxNNJJnHFtGnIhXC1M6L4/dkeTJNo+HvVM3IhCakKMpzbioVU/weG6OhRrp0c6qdCMIrvER9U9py5kCXJ4YAbMujFmGQ4jMxob0XHUhOFG6kSR5U61Ncx5ZSnVIyqPF43xrJVxZWa7hI0mV7iSpuWKmIOBEcTqGdub0C9ck0UV79NDjAV21jjczQTAvwG4OcIxemCZyKk91Uw6FlkcnvjSW2/1GLA/ZbHtDS6XxFOt2EHaHfnBvDTc2vXCUowKlmeykInEg+RneOcsjIwhb5GyczdpSTNrS0kjuV43PEKaSeMc+Sj1DKF1LK/G6cQZ0xecA+cPKqmZRpM8Y/jbXY608igmzHYfbAu5Sh0k4/iZfmUtBK2nlJkTjivvTFUFbq9oEEjV4Om5ZV3EIQ2E+EGPKD4euygYkMGARuWZ7RUfZWcPNYnxd6lvU8Sqz4ofxYuxV225thZDk0WZQzqGaNs1Fu/eXy10JerIq7/NsRtSHCj6axEUbuAvlZ6XfNAMvFRhbEXRhjIjcw2Y5wO4Sp+GiPW+qKkkwrI0OcWPq5igQwWXbt8waOaNmOB+wUOxJAJGl54fxrIt4EtiOZfCzTUxbuOlZ162xRXtmLvW6cZSOhY4TZaKdxs3sjIv7zpRRKmm2qLjaktwyinB3iJJECBTGmq9IBLGGpiQqZbmU2Z7pRWyfd7rVsOpWqSMWF6+2PR4cQRTrMTUQXzu4pTs/4kkb7dxRJK1uTtMzirpUqBILjOPJ+Lj0ZAduV6nJ04MXr2xrbFCt2vfJUj2fdbeM4dybabVqlohQ25vdNRD27Dm/Kf2RQndnSeZzn6S5iyGvlzv5rGdSluz6YTMHQU9VZtpS3PU8gGKW6eXWWK4bKqBva06fbQlpu3Ekh1PhGAaa5+pRNE7skBeh5Sl4v0jpsl/wO6qULxXRVVazMPvbQkWPs/LEHxsZs6pMOuWourHGy0outMVwy9HluK+j9nSNKgl1G3Y5anJ9QV3mCs+HGSwfK4EkNWMD4/Rl1JndrinWJ+O6MHl9tCUssFUdF0DqSGnJ7FY7RxLnodPF1na22mOb7e4QKoKi1X42N+P1NQuOwI3LGFu0A8/MXD3M0grR8MI4IMhFFW7EEs9PuK4ZvMS2slCoWrEZ5utZn5cEd7luZlEXL505HQxMxR12uR/Qp15LonFjihVfcGRcBIPBtkSu1tHK1c6JFttDEVwZYrvBhDxXh3ZmSjsvPF4xfLuLvZpCsm1TwJqxP+OXCElFVJXc0FRN3jKsZNzvmZN4NHlCyJSdlW2PQ9Ny9bhRcHbm34amEg1sQ8r9Fm6YRYIdL3PzOkuwMhJHZtxfJNunZrAXefgMVogS8WEnpG/0zJv7RUNym145h560yZyw50aB2UlIc6Y3i8WmH6jAvVXI8bTuFle6g1eVROfpVgT7CR5e2MGWsqTjKjuSfYiKQWqXB5Xr29Yk4R0bm711KE9kcdvVEuyJ4TEsaNbbalVCb24dJ8g7BMsvUeIiw2a3Y9hsk1MwjOHOtUAtq/OlkBbRhDP1VkQEOiybUKvJNWpdnNXWPnGhZBW7TN22/igz2ewgzXFb0UOPH1fF4iALnSdHxHkRsLOD2J89GKkP5h6ey1gyuFc97HaEnoxVtToju51a6/My6ZtVrIg9zXmzhpVZbK53wsW5pAds61J6Po8jgyWvKuxt5kg0WwZRvwj3672S2wqrVzJyTndbmqoZKREqFR8vYsNQQeLG6VEqW3Qxv85s/uzuvPPGpLTGluqNulhlbE8eQLJceasltq3He1tBQimh2NUIzJLKqEUcY4S3SyRFannSkh5RaLBPGAluiIVsY27o2ry6Xo2Wy4IxiBqNzilljHVwIPRLfM4YhGguZoP21Cw77OzIOFSEAlfehZbPhgHcdhUrjbu6YkQ4WsP0w8w8pHTD22jHLWCTWqnqOh/368jSZthiwHTMlhkusW/1crYzRFqwCWZnO6KqVm0lJblj8OTKMHYE25yPnV7evDWb6dm689YUpa8zLcEOXK7Jlnq72ci6FXw/Uyg8SKWtTaqnswnjeOWabhJfliYtGpYonA64YmoOJypBbpPMtusGZksy5t7fwZk9uHJnN8pBKa3wmPinjV6ujzdYlTQwSaUSni1ncWXSCHE76ZbjCop7yBjtyF7TbXNDI2cTwlt/5GlN4IMZKSKHQDn3u5HsC209DN4FgGm5kRSj+LbZZ56jlyD48M0Z4Tk2x+wObqVk7+VKIjphvt7dYn1TYMoV3yzSbRyfy7lKoDqD+fRIm8pSgBuY1W3N0zXyfMApbSiN/ba47mv+ukOKqzaGW8u82Iq8piU8mMGWplg5jcLEfNUpDntZ1ZLLakN3EosFlbjYxZZvFqmkiXKkbUdKxxEGzUlGIh3r9FSkeqLkKpJXoreeozsy81sYxkfeGMYVcS0TdJUhebCOLYBbZoA6mfg8Gek9VVSgemIwb3Dlact0Zt40aco10e4UzcW1lhiUNSThIo5JPysQrR/36e4Isn5wgtNJIvi4SCl/KQpKVJ0EIVwsC72TN+g6VArknPlS6fWj5cYAQaIuk1RrDyNHbc+sxJN4tLyitHyIDqIKz0KVO7jXwMi5fYvoRx1mBkTz+JDLhu36EBraVepmV2WoDrs5p0pGMqZ40cFJdqb9o7yz9Xm9OPcwnK1tYnFQOp0dyxgxaX5VCkPkUzjoWFsVFqh0Fy+SpWEMnBhqiFaqutpso7511mERu0vxGuxmQnUOiS03X/HGZrH2L0NCLUiRsGAc1dZUOj/DTWrFlZ7LfbQzSnzIknS/5KzANsygGEU60NbLGmbbEDsbAQZwYG0W1UGn6lQ0utYJ8yYc9ppPXLKlrunmRkQvlRQvqXSxVGtcJNc6RvaVpssbyZSW7K2OhdbSRDVFtuIxymxXUSSuPpab036lbK+wmhexPib7I6t6SWXQsqKVJDk6UsHPLO5M+iExP0WA2k2ay+1dmqT9wnRLQQ9pSyiKLguF6tp1FGuAMtibhMxG27VmOfzN3ugxdxyiRiPSkxAZKH5Qbu7Majh+W6nXHXb1F7xaDueh5BoJhNWQONdBCRu/O227jT7T/OSQqfwoYuUcX1tFFe6LfR+fj6Om882YZe6KWbNFb2uKso2Oi1OJX4SLgNNVFInt0Ta3WCxaM6VPxlHu1hnV4R5p+M3RM0gsTba7MMqicTTlsqC9dNtqVslXTqZmV/52ZdfZucgkmw3tZbvCWQ9eYVYutPsYPooMfJmDtghsIug+sj2ZIU+JG65oOt0szqwfOlzIol7YukJYIzx9zq06E5Jl4afwbJVxdhUSebfWg0AzuxtI9KK8tB2TWltlX+ubBQCP7oiTCvo/1tqSq5V6KBwhkR2B5WRCZByhTjD/oqzcnPQMHM2cYwKvTG5LXZZS0qYFjNI1YTiUeMB6ErbXeEFWIidgQrrAjJwk4xreNMjJQ1doWQlz8C93NP2Nj3gW5rTIsMJo1ZwnY3EyHHSdVfu5tNgh1NCmXrtQ00zMY9MH/LJUw/ayZMny6Iib9uQ2IkOuLqjkYga+rtl4TpNle9YLRIprOZpTS++I15tzJARbYondQnQV9AaqHpas3d1iX7oFzAzUunWbYTsZUXF6fiY2DtW3i1gYDfN0RtezJVmDXrahyD2/EhO6pWXzcLPQcH4KQQOIVeR8eaFXCsjdcIArEsfncYHL67FtJRVZeXl/0zKjS/0sX6uczIpd5pqycrEP5z2Mh1yTwUO2oqwdx8s+Ng8NHdlSgneoZEqBB1fxdbZlzwJ7lXvrSOFoUqeJecwCd9yEDYOP0liVsjfQBWmGgtqX40yHySHK9N1ZrwfpOrL7xQ6umgug0WSEF2bTE1Exnwmzy63txuU2lw8xUnO3JEFRxNyaxs21jKuYGIzTgz1RRPS3A0l1xVZe3/hlm2bWcqTzgDy10qrw8H1AzOfVZsNsEvqwdI8GZccDjaezFOngve9l3rLn0I1ZNS5/4UwEay6CxTsXexYkvYOr5HG8UbF3Q9hUypyE3FS3Pb4K05yi5o19y7rzbjXGhEkZIibt1j1XwY3HbI18bI3b3PC2lCKO7GbAeWzr5OEoOclANKFTUPKFPc3O7ZrqLrSj9BGOsvlwTDeegkQ7bGO4YHPoCshlt9DwkYmP1eyWkd1CCnMQ9WToF9SeQk+kaePFZejOHHPe19RRcZ32uGe6YinFm6Hg5yjOzPzKKAa6naen7tpQXoglO+t00y/tskXPe28nkpKmBWtS7MPaD3krOAznxbxNqIyxcW/TblwpniPdxsdsnLcyzIn2JhX1u2hFcKv+JItnya+dUpozGIff/A6sg1aL5IC52nIJOtBgKePnvV9fM2fOnvfSDeuqumxsryTbE1zx0aXEOMWS9pXLBGrqMqwoK9Qanx/XlFkesN3izOkszstEbrF4EdGde2EJVZDb1L9mN17tkeZyc7f0QkFbbL9V+6WzytrZ3MJrYiS5NvC9gGyk9raOMHR2I7Wbr1M3bdnvuewQNUG7Xm/EuVLCxQ1A7sBsbXr6EV4e69kFW2zIpc0FThIoEpY6JnxQLvx5pnhnpYwpfXZat0iTzBut52md1A68sgpq7wTTGBLUR7AhU1gK9EaIN5eG8XYWtkg9BnbXe8YOvyLYUGWnFLat4wFXccRbE5xws3Bl67HGSFB0KSU0z6dVfh29MYZ3J2mGZcVAgG38AWuKFpWDy9KIVSRc5vN65mFJSZtWN+NpxVyLRzk+3VL2Sq2vw9rdaJFwZNm0X4PIQwge2R/zUWLFOqMU1HRSTFXgAq2tgKpXGONaAVPf7FUdOisyVpLO8LqqM3HW9sjNrmjbxVKfjQzWNgSjYiR/Ske2CNHDLFEl4kBv9k5y7JNe4IjLEjQoGWmKKzI9iA29WLDNTmJVo74JLK958oHuODJY5Pyc2FHDZdhnB1k8RcvMl92eJlhpcTX72p0l4Wq9zNjlJdjEV4qifvrp5ePLdJ78PBX+Z2+Bp0O7/7Wzw8cx39s7oPuBsG97n+9rff6nWvzy8aVyY6DD4xS0TtrweYD4d2egn/7iZcE0YXi8Pp1eSPXN26l4Y4fTf+p5iTOvrZtq+FrnSXs/eP344jxfzH19HjC/3FVPi+br/VU2uMybyK/A7z8duMbZ9JLF92K7ebsMn+fAH1+85xvJr5O5flVMpj3fPkxnqdPrh5ff/j8WghqMeyUAAA== -->
