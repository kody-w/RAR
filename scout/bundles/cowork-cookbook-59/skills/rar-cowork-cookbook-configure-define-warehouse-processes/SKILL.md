---
name: "rar-cowork-cookbook-configure-define-warehouse-processes"
description: "Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_warehouse_processes", "rar_sha256": "da9e972a5f8594421cd96f45d562ca48c4b908602626ab41fb79fbd19fd456de", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_warehouse_processes`. The original RAPP
agent is preserved byte-for-byte in `configure_define_warehouse_processes_agent.py` and in the RCI capsule.

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

Define warehouse processes Configuration Bulk Setup — Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-warehouse-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 da9e972a5f859442…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_warehouse_processes_agent.py` first:

```bash
python3 configure_define_warehouse_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_warehouse_processes_agent.py   # or on stdin
python3 configure_define_warehouse_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse processes Configuration Bulk Setup — Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-warehouse-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_warehouse_processes',
    "version": '2.0.1',
    "display_name": 'Define warehouse processes Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-warehouse-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-warehouse-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21dd1babf427783c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/define-warehouse-processes'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-define-warehouse-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineWarehouseProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineWarehouseProcesses'
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
    print(ConfigureDefineWarehouseProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bPayLLmv6I57we7H/ZB++IbN2KEQCxaEJJAgnaHW/u+b4ie/t+nBJzj9uvbb25PTMRgO4ykqqzMLzO/zCrx24vVtWFRv3x50Twrh9ZWmkahV0NW7kJcMRR1Av4rEhv8g5wib+vI7tqibl4+vbhe49RR2UZFDqazZZlGXgNZkN2l97F+FHS1NT2GnNDKAw9qC8j1/Cj3oMGqvbDoGg8q68LxmgbM9OsiA+tCUV52LbS6Ol4K+VHqfYKGqA2h3koj9yFuUq4u0tS2nARqurIs6vYVaORdraxMvebly8+/fHqJwPeXL7+9OKnVgFsv3FMlb3nXwXhTQXnTAEhIgZ5gaDkCUHJwXXq1X9QZuAUUh55XHxsv9T9B//mfCTAjaH768jWHnp+vL9MftcuhNpzstZrWcyHHKi07SqN2fIXYdLDGBqq9tqvzCa4GYJoHr4+Z3yUVJfTP6dnHxyKvgdd+/PpSABXuGHx9+QkqarBe3U3fXycp5cefXtNi8OqPP32X03R27DntJAxo/frtef0UCwZ+Hxr591X/CaQ+fGt7X1/+YNz0eeg92QlmvrzGRZR/fAgGjuy93Mod7+NPfyXWCT0nSaOm/bfk/vwQHHqWC2x6Kv7TpzvIv0Czp0HvMv962RK49e9YAoa/LfcJegL1V7Lv+P8X0SkIr+Yd8X8p7l9NmP0T+vkvbfvvJnyC/K8vSy+NehAddup9gX77pikr7ucP7vebH375HYj+P4rRiq527hK+ZVYe+V7Tfvv284fmfvvDLz9/6EoQa56Vfevq9F/J/Fe43tf5AcHnqI8/zgXrH/MkL4Yceo906Lei/B/176/QaSKA7/ebL9Af82X6zKDJiLdFHxD8IWcaoOsfcPzp5XdAEjmwpnPuj0GW/8d/QFLk1EVT+C2kOQUgIuDgNsq8SXk9jBoI/J1yu/YArk0EgH2OA/E/eXjSuPChX/+nc2fPz86TPedvjOh9e3Dgt3cO/PbOgb++QjqQXdRREOVWCqmsonzNrcDL22ndsvYar+4Bo9hj630GXPR5+gIYE/r13xH/7S7ptRx/vVNo9GApldtODNV0qfc6WWmEXv60yQF07F09pwOLpIVjPQi5+QSsb4q0Bww3IdIkUZpCblQD84t6fNBzl3+ZhP3666+21YRf8welYtCjZjRzMOBdHejzZ2Can0ZB2H7NPScsoA+//f4B+l/QfzfrLnxaQwH8/vQJ0HCn7WUI5FiXgWHAXcDBgEDuPvnt9yfAQEwOihzwYORPRWuaDGI08dw3tLUN+xklSMj2AMoA4WyqMYCnoah9hbY+9K4vWHR6NDF5WDQtKHCll7te7oxAqgXMeUcyL1qoAYHY+OMnaCp906q/2rV1VzEDyW61v0ISp4C6UaRTsayfdQRMLvIIwP8eC4/7QEj9oYEWbyJeIXmKSqi0aqsMa+u5hm89/ALqxdt0INyCcm/4mk9V0puguqfIAx4wCCDjPF36efI5KOgZ4AO3eVv7Psaaqpt+r3L117x5hj8IPICKA8oBWDToQNUGReEfz5BqQEym7h0/oOkk6ekF9+mVewwu/7pN4H7oLBZTs6EBMimhrx0KIzj0/70RmfRn12t1tWb11RJaybp6fuA6NVAT/o+eC7QDEAiuRw59bxHeCOaNZ7/maQSCpB7/8Rh598ZzzIO7QNK7gCrUu3wQCgDXSe49UqfIq+s7Hl/zN0L/BMC5sxcwAaQ1CPsJkbcFp6dvmoYgd6fr78X97tnanUwH0QiVnZ2CSPE9z72D0Ib1lG1PX4Cw9abMG8LICX+wCgLSQXQA+RBQIgL5A0j/Dp1cADNBot298D48mlomoIXbOUBb0KF6r5ABEmYKmgZkKeh7pjEAhQ93UVDmAYyBiu8IN6FVPpSZmtqngtbkiyIDcfxHDzwffg/xuy6T+kCqBXwPsBwm2nW968Oz73o+fQWUzaakvE/60d1PW6E/Vp5/fM3vOr4zPcj1dCrafwAHAjmWNfeQm6iqAXSTec8AApFwr8+vjxL7qOHvunz5Uyf/8e81+/eiefzRc1+gsG3L5st8/ih0b3XuFRDFHMRIVHrN95r3+ZFun9/T7fN7uv0g+wHVF+jv6feDiGdgf4GQV/gVnh6JkeNNkfv8ADi4z4vzZ3x6+jVXve9+fgbDRLXpCIrse915GwKKT1B7wTT4UYeaqXwNoGLeiRd44mv+HgvPTHlwDiiaTfGHDL4XYODZh+Pe6wN4lLdgbXdq2wJv2tWkk/qN9/Il79L000tuZd6/uZuZ6gCIWADItA8CiINOqI28+9V7VzRd/LiVu+fVRJHFlym9PkFTB/sJem9GP0Fv24P7pivvwP7o56kRnpYEQ8F/72Pf94m29wL2ZO1YTso/9jxT//Xsi/+sxJRVzxiZdHlL02nFPwkBX4LAq/8sZH//YqVPrmhaa6rUUfuW4Q3Q0+0mZgfuA5kHkglwZAcm/HkZsE7tVR0oie5k7nf8vptVPGz5/Q5D+9g4/vbyxhlPHzybRDAcJOfnZiqKcxCqYEFw/Qgq8Oz/qn18ygBMB1qXac9qMR5DoRbh0wSD4yjiuAzp44RLkKhj4bSD2wxMkzBKoqRl44hvU4xvuwjjuzhBuh6Q9wjPb1P1jya9PNj3MAZBHRcjUYLAGQTIZ1wLpyzLhWmaginfBcXg+9QE0OTT2IdxE5LvnewEytPm315sEgcjN3izZR8fbs6cLNuY22oozup0dr1i5AE7lnDSW11obglks3bMLZstL6LDn481vbMTra0svN45UkHtJZn14dP8bGKictsTGi8ccRH3l8WZt0fmdkHdlPANeyVsy3XMqFwKl854qlp93Z2qdaULRnfiDS8z92Fq0O06Q7a0vW1F+lggtnaazedHzDmVp/BgqTyXtJdlB6PHytDGo7Wd77AGmR8vEZIIpnppzzDuE115iK5wodmRFjs1fTwb+9xvLrtMREOVF2pZPLtdJeVHPYatXCdIWtkw46yv6UQP5/O+TmOKx/vTNtEsRVCbCDUuqSVfu6sknopTWwk6fx6Rw5EZEFqO5F6Qa0MjkXUII7WRzbt9Ih22O25RNKTVnjTCy2siYcKdWZVZa2fitWU3cZdd0li2RoRt02xIjjRsn9Lm0Osba4e5i/V+SxgBMdTWyYflq35TS2O87bTiZNhVLuDM0EuoaB4yPqlTX2GyxQEnUJKFjwJyiYTudEvPFHPdBOZ6tm1xlu2adV9dt5WHEkOPiaUr0ypOWsjQp0QGb/apVZ7EDXEej/bRNlK+Csqbqmv4vAwukW1wdi+rJRJRSWnoV1kzxR1ImUuH2Lzqk5Q2nngW8JS753Zbi+JUSTy6JrypLhXl75MSobE4ODgBdtpTSpO1vr8SO7ezFqiHzVdNk6TWJWvN62EMjTW2Dtdy1XrG3OoPhHU8CZRsYCkTeK5iZGfRCDcxv7m1i0sRyH1XXaSLU85DeVNfVWd2yPYwiEnnOmqJxNf5cdu2Ory+YfMGzYrslCA66uY7zTnbEkX3t+ZGLhZkKKAn5VBGZXXoGkt1z/BIDrNqdNPMjnBSr535Yq8sZAy/9deNdaXLm8zrXT0/qKccxp25Xs85vItSNK1NFJnpaOxE2CGyEbusqFUSaJ46GlaTrjS32S1acz0PxjRfFYaxPHpnTuF2rkmxWkYejpV5diSyG/g94aXWWeePbR6Q/LjE1B0a75admiTaIVZ3V1a+KtZOVJcXe7C9KDuHlXE66XznrGQcz+waPVq4eaJtfy+3cpALyGKVeYdyKW/hME2oXYqfVMH3kGWG+SyNUOeK4M67ELtyWkecBctNffo2V47JprsMfpIEPoGnoT/uTb5u+msSKKJ5jRIk1NuN3nmcuLaMJuyp04LwD9KGcU8HgiZXzMrvEk1beK4Mh9G55pa+I9Elb4XOcMWWGNzlglLcMJrF97WyS7E54ZBiZcU3LMiMwMS3rmmhWHlV6BS5aETSWLUfk9z+ghiz3W4rxCeRRLv0iBxn50u339ONoWXJEAvLuRcSDIcQRJJUtUM43UrzmKVyLaLGbfzIrMd2V4er8mYzgXiKiDorty3S33x+6RLEYslu0syaL7hwjx0Hs7CRWxjuEwO+7NxANM3QE6xWzHdCvclanoxlsQrwTbSmuZuYczwm4fO87lJDpy5VrGN6x4tH3drLTBeyHTuniYOcGwt14yXpnMrw3WyVdrA2+sKMULrDwe6VuRvTfb3YYgURqjKck1Ggr1E3ToS9UoOYVFRuQ+22cbOVVoS0u+IrqzsZ8uBv04ihFutNvEMvKT4TFHar3ozMyS8uqCq+Ct+coD5lY08jO52/BFbPUvjobJggMyv5qCSYkHgsS1/XcoRf8J2YpMryiG8rtJrt3Ivp4TuWFdldtOeNYx0Mo5EZ5ZKVgtKsg4bVcMQUY4lDTzHXu8PpGg7YUglWyc1KWSRPHMtQis7N9/CZiQ6tvik594YRVJdfZr5sEvRBY6X2fLvkeUIFGuDqmWydLhS2wnE+hMmLzG7mTJM4l84rbFdXd2CbRWUzFzmWRddTOcYwuutfWkKdC1YxUh1No9hSLFbOQkc0abW3rpQwRKmQmqBeIOFl69gK0/PllpepwGGzJCvy/CDyZ8N25LV+DEfH91bEZr06761KLI7K6ijk6VZwk8w7R/syNvIGlY+bnJnl8SVbz5dUn5y2qac5ac2fo3ZuRTdEFy5zTTfG3e0WnLMYLrmDGiuL0tzUN8+OGhAQxIw0BBDl2Jbcj8tLiB63jqT0V56qimpRmwV9yyS0uSLXy3URklqfo6aUuedCWIsktUnK1c26toa2Wezjuj467CruDBobJWRFiXxREWOwiRVVb7YKMbBBnxBBoO8AV+9kV1CMnF6yVWExfMcm7IkoFTgRBGZWhEuSsWe009H+ftBlNJd0rkZ6ERFPjsyt9spM8hY0129tGz0qvaHtF8awFq+G7KGZcd5uWrBjkYXKS6SLjQv0+lBiaLXdLNRtB9LoIptSulkyZsomIuE087GaZRp7jr3huOX71XgQZVwI6kva5gINK8U61U9a6LIwObPk1l3nrAa70c67OFEOOwcsp4hLn1aXoCAPabgOCVodQmfJtHm6T43hnNKCuLC7ur9JiHnNk5bZB+tMMGt9zEhF5y2Fu+xS4WaxOozReaVy2taNJSt2FvA1b9x0Y8hqwKw5G84qrvDgSta9eKdxW7JaOfPDauEIoi/HAVMOJuhWy12kS7SKDuRVrLehDFjcYjlmF1dDxcfs4SxViQDrGwOpSXU8XI8WCxqOORUhMO9RizaBnZi4jfJBt/jRBq1mtbi6UZFKEtGyfF6E1Mzv+4u+bHB7f9oK6AIpKAz2l3v/bHl03h/wGWYs65ZwMgwee72NhOiyL5m6dq35ijfyG86tlwk9g3GVX/DBIQzkMlzSks6ClgJvlsjKjnfN4bpWVDqr+ZmbI5IhXw6ItM539XoJD7PIK8hYnO2drYZm4VF1/VN3FkPMCraAxW9YbSWu1phVxV0OM5mLz5vFmWZDgb11HbHrZZlNj3a1ytnuyHXn2fl8FtWhyBcYEqLlcMm57RoJDS7Rm+E4syyFzLBolZjoTSu3u+yEwkvU5Jc4RzrnXeSoAMl0saX3xdRrwHlQ5WshiUwrbpf89XLLOpM4KDDgzFCeHwjTSlWL3KzBDlGOjFiQOQon405CdUxFwxlnWtEhdd2mqhjFOaYHvkLbpRses7Zq6WFHdmapjY6aHfJ6fm7xER6P1Kayopm9ZASC4HrxVrM8ItnM2veYytyedPcyUlYFNgV7/+TaB0aP7X1HHenh7OMXha7PceOhpHfxVvl5FXvuEdRuLImW0dHP2ZDfXcqgICSqrITFqmEELRW6eXzcdu4B39ihyG4oaVHDqWKJrBHqWdQd81avq5Ra3GBCsTcHq5eX2mJ7QTzEigSOTVe1B7YVuOjk6mmLshzZLmAQputOl0wVRvkwZUn3qI4qv2JuVbsWl8Z8mHUBhxOgsHYCjG32RzjXvKDDT+FtPdpYvC+TDiSIUKV8btRtx+EL0p8fr56Q8DsscHOeSGhyt+oWiSx5qcclaiOHJH8o9sLp2GZX0eKyYF2aymrJnW9DzIHG1AsOUlgBnlR9fmuqOVUNu1TTipV/cUdL2F21xtvlR9u3T7qN87K4Frby/sbtaVpZFJwfqZdMO8tr1Ze9xdDT0soYpcMucURiLcNM7ZC5kOxEEIFhIK25apS2vCTOI1uCo0SaHeKg1cUIc914Rqpsq/PUgeW3i5mp5Hsu903Gw9cVvzvkSUDgV8dO4SttcGbRpXoIe8PQSOf9gjQco9nehCYCdQzQTS7qdUhzWQ6rw/6mtjVFFmHKH41lQvZRUuGLUAfNtTiMwlm6LXtcSsH+WpvNTvicx3dXUsZOXl3neuGVBeAIOu/obDlDCOZgdkN3KxzKpS9MgKNM661mt5IVDkaKlbHi7sOTti7OlpxLMGp57KCubrHa7k2D0Rk3RkIXUy8bZF8u1UxeKiPBZguzH+fajNVX7hYD0AZg/xSvcrKYDbjhcLW363HGMfB2oXROW5/CmNnnSFEsFwzswOLKX3pnet41sAJk2qDwIxFvJwvavd66PZVfewTJFPVKxvM5ZdfzYEFy1QDPi/n8ys57e4meen87u25buhXRoWxYSjuNm7RKCjrWi2K/80SwMUBuy+tlftBQXWUF5Mbg8RC26/1Gkc7Eyg284y2LLTHO9tfLRsV6W5bEFtujF3SbYOK5wwCS9IbNTRI93tb8wR3p3jvS+K2RkoxvwrNqqyayluprEprDoDH9kDGsTmCkGHbnprD3YqPYswU+36MZRbB+cIPFBImrw3nma2xHgMygBmKwnHBNM+nBPOoovt0Utqj1e730UxIjMabemNre4B0sikn20nA7RlJS2V3ejrml9NU5HRGSOi2jSFyxmzqK9reGMkDZuvrVGe8yaXlbz40OH0OMmsn72UHcqHs9uKAUJu4qUaR1fhuK0Tp2oy2zNpsdxfuKtqc0hqOGYL1Ao3NOkburboRCw5j6bZyxmJ94q/NRZfDTWpGi9pxR/aGPd/1Vzltl1ZHkLb8FCi9ceWa7O4Soj+CCj95KhGJmW9wNZ8Wy0qzBIOfizB63whYoOfA7NsOZBmejwRlvW68behFjx/LYjquM9g8mbKTr45DODg6LtDpmm+eI6CSSzmvZi5a5YIG+a4+aIDFX3rxKbp3sdHG/9PHmhmGmAVeEUucmFis5F8YbBb4ky6CnahbtedY4Sks/joa1cXXUtW+nA4NH8aYWRctdrzjcEpetJTede23Jja91I9+fbMElOqROZFmzTXNFdm14ZdbUNdh1m8VCY0rFuZJSj1NnLGRVTaEdZp3CjpvMlBg2G+5yYk76LKXW51mKHXKTZj2c6e1aTq+0zfSdNYw3O+3nBrWwAdQYD+qxwtxucwtZjppCTgfCp/1WRWYEpcRXtfAuiG5K83ljb3Xb7xyiu1lzv+ixW7xbUOPsSmQ4aAzcIjsInrB3gopmjzP55PZEtpmbhLAwKcOTlhVJsCeaR29+tBwUnV0ud5qJuHPlduvPwtaMEEkJSHm/mokClV3NCDUMNPEWiCDySHS2QnrDLDl4GORCEq3DlqMk3thkm+KCnrn6iA5sd6CwVh1plxmX8JlMLHZnseQGr/zLQIY1TPub8WCeHB1r/F7a7FijYwXc47kTyu438OUAqnd6SdlbsJQ23kXgloTZFrKwzGVyZwSUR6iW1OCBZ2ueg9K6v8EA0TrXnvAW3nxXyA4hicicpxUak23GCejZvBxDyVle5Ng7pZrbJfQpHW0yoRFWPs7JM2pTpkStZ5rjx/mwXi/EjYRis2J72MJovFrVDcPhR2plAEowNE9QrtoobyhiftxITliKHYimONiHFLPAZNOwr4kQsOzLp5fp1Pp59vy33jVPJ4H/zw4kH2eHb++i7sfOnuV+ua/15e+p9cunl9qJgFKPw9cm7YLnMeV/OXr9/O+8xZgkjI/XuNOrs2v7dlzfWsH0e6SXKHe7pq3Hb02RdvcD4E8vdtdMP4xo3tR7uRuXldOp+fuiL9OPFKbT6QJMbotvz5903G9Pr4Q8N7Ja73kZPM+kP724I3BW5DTfMJL45tXlZO/z1QgwE32FX5GX3/83zCvwhf8lAAA= -->
