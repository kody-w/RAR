---
name: "rar-cowork-cookbook-configure-promote-employees"
description: "Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_promote_employees", "rar_sha256": "4aa7190ca9f153f44328a80868925905a9c20ca2726d8ac6dae93338a85a816d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_promote_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-promote-employees:5ad647e00d6cfb06a2babbc8c77de000bd3e5de0d3009c774f4b67960ea5c77a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_promote_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_promote_employees_agent.py` is
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

Promote employees Configuration Bulk Setup — Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-promote-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_promote_employees_agent.py` and embedded as the fenced Python below (sha256 4aa7190ca9f153f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_promote_employees_agent.py` first:

```bash
python3 configure_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_promote_employees_agent.py   # or on stdin
python3 configure_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Configuration Bulk Setup — Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_promote_employees',
    "version": '2.0.0',
    "display_name": 'Promote employees Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '761f58cc84276241',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePromoteEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePromoteEmployees'
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
    print(ConfigurePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObSLbvV+HW/cPuS7nEjqiJiXiAEEhIbFpAaneU2UFiXwSoX3/3l0iqsn17eu5MxI14OGxBknn28zsnE//+ZLdNlFdPr08b384g0U6SOPIryM48iM+7vDqDn/zsgL+Qm2dNFTttk1f10/OT59duFRdNnGdgOVsUSezXkA05bXKbG8RhW9nja8iN7Cz0oSaHiipP88aH/LRI8sEHCwIwAthBcVa0DST0rp9AQZz4z1AXNxF0sZPYu1MZZaryJHFs9wzVbVHkVfMCBPF7G1Dz66fXX397forB/dPr709uYtdg6Il/SOJrd9bCO2ewMgFigSnFAGyQgefCr4K8SsGQ5wfQ4+lz7SfBM/Rf/3Xu7Cqsf3n9mkGP6+vT+MdoM6iJRvXsuvE9yLUL24mTuBleIDbp7KGGKr9pq2y0Tg1MmIUv95XfKeUF9Pfx3ec7k5fQbz5/fcqBCDfdvz79AuUV4Fe14/3LSKX4/MtLknd+9fmX73Tq1jn5bjMSA1K/vD2eH2TBxO9T4+DG9e+A6t2Vjv/16Qflxusu96gnWPn0csrj7POdMHDkxc/szPU///JXZN3Id89JXDf/Et1f74Qj3/aATg/Bf3m+Gfk3CH4o9EHzr9kWwK3/jiZg+ju7Z+hhqL+ifbP/fyOdxBmI43eL/0Ny/2gB/Hfo17/U7Z8teIaCr08zP4kvIDqcxH+Ffn/baAL/6yfv++Cn3/4ApP9HMpu8rdwbhbfUzuLAr5u3t18/1bfhT7/9+qktQKz5dvrWVsk/ovmP7Hrj85MFH7M+/7wW8N9l5yzvMugj0qHf8+I/qj9eoP2Y+N/H61fox3wZLxgalXhnejfBDzlTA1l/sOMvT38AcMiANq17ew2y/D//E1rHbpXXedBAGzcHAAQc3MSpPwq/jeIa2j6S+ttGXqxWL6n3DQKjY7oDiLDbpIHEyo6TEdhGj48a5AH07f+4N/D84j7Ac/IOiP7bAwLfPiDw2wu0jQDHvIrDOLMTyGA1DbJDP2tGXreoqNv0y2VkB0SJ73Bj8IsRauo28f8Gffsn9N9upF6KYRT9awZ8YQMHeVADZuSVXcXJANk35B4a/wtAU4AfHzg7/tMWL6M9zMjPHlZyAWD7ve+2AMqT3LXvkF0/A0fXeXIBWDjarj7HSQJ5cQUMk1fDHcDb7HUk9u3bN8euo6/ZHXxx6F5M6gmY8CEw9OVLUflBEodR8zXz3SiHPv3+xyfo/0L/bNWN+MhDAxXgZioQwAm03KgKBLKxTcG0GhpDAUDNzVu//3H3wShdBqofyKE4GKtZM/rlB9ePGtwd8+4VoPMool89OP1sN6iLgF2guAHWAnldP3/NRhI5mFp1ce2/G/G++G76dzff+Yw+qR82BH66Vctx7i3qRme6eeW9QIsA+rAUUHcsjaNHo7xuQKAWfub5mTuAlXbz3YVZ3kA1yJU6GJ6htgaqjpS/OYD0aJwUAJLdfIPWvAZqW56M9bt61DqwOs/i0fGPOL0PAyLVJxBj3DuJF0jxgTWhwq7sIqrs2r/NC+x7RICa9r4eELehzO+gsYD7o49uWXyLPO1PXQP/U3/BjS3HBmBMAX1tMQQloP9f7cgoLSuKhiCyW2EGCcrWONxDa+yeRk3vDRdoDiDQXNzz5HvD8I4t76j7NUti4I5q+Nt9ZnCLpvucO5KBjPcAYBg3+mNeVze6cQNiYnRyVd3M8DV7h/dnYBPgkXpUAaTueQSC/IPh+PZd0gjk5/j8vdRD93AbVQeBDBWtk8QuFPi+dzNCE1VjRj1cAALEH7MLpIAb/aQVBKgD5wP6EBAiBpEKSsDNdArIDNAe3b3wMT0eGygghde6QFqQOv4LZI6RDKKxhhwfdEHjHGCFTzdSUOoDGwMRPyxcR3ZxF2bsaB8C2qMv8tRu/B898HgJonKsI4DfR8oBqjbwPbBlB5wAMqq/e/ZDzoevgLDpGP63RT+7+6Er9GMd+tuYdkDG74APmvCxhP9gHIDVVVrfQg4U13MNEjv1HwEEIuFWrV/uBfde0T9kef1TG//53+v0byV097PnXqGoaYr6dTK5l7n3Kvfi5ukExEhc+PX3ivflkWVfPrLsJ5J3C71C/55YP5F4xPMrhL4gL8j4ahW7/hiwjwtYgf/CHb4Q49uvmeF/d+8jBkYsA/jqDB8l5X0KqCth5Yfj5HuJqcfK1IFieEO2W4n4CIFHgtwRBtSGOv8hcUedRofe/fWBwOBVNmK7N/ZuoT9uaZJR/Np/es3aJHl+yuzU/x+2MiPAggAFhhg3P8DioA1qYv/29NESjQ8/b9tuaQTy38tfx2wCxQy0r8/QRyf6DL3vDW47rawFm6Nfxy54ZAmmgp+PuR97Qsd/AhuxZihGoe8bnrH5ejTFfxZiTCIgseuP5Tr/yMqR45+IgJsw9Ks/E1FvN3bygIa6sccSCCrvI6FrIKfXjkAO3AYSDeQOgMQWLPgzG8Cn8ssWFF1vVPe7/b6rld91+eNmhua+a/z96R0ixvt7B3APGbDgX2nQRmu+F9a3kaY9rry1UTfj3hrON6BYPBbQH16FYzfwdg++p1cALf7z02jCKgb16nrbGj/dBQEafG9VAQUAEl/qsSGYgNwBlECZLkbpzwDgfmAwDsfebf548/rX/e2fs/2VtD2KoH0E8Sg3cBDKxhzbcdypS9MeGEUcD/dJcOfhCMKAQSIgHIpmKMS3SfBoA/6j91L7wX+CjnYHkn8Y999pt5/uS0FJwEgKrCVsm0YZxLWZACXxgCBwbGpPkSk1ZTCSQUibcTHwFqMxypvaLuXZPoPjOJhD2lOU8kZ6jzbgLs/be4f97ol7vr8BcEzjUVrMtkflUcJjaJtyfRxxcNdHMdSjcR8hGTyYTn3CHyk/lj68MTrrrvIYoqDhA+3WZeTz+8O7Y9hRBJgpEfWCvV/8hNnbjjlxjGgFVwnc9zil436ZDMFOGS6J3uP7gT3mSC0p1lymWYCl+2ZmzY9OspKv1UyXGCHA5pNhi1xbSs83mbORWEriUqJxMS87wgGa2mIsqyWzqnFZ5a1dWZ/WRnyurucORom2TATKsWZDU6dNX+77fawwk8kOc+dnM9U32/mJszeSV5zlQJ0LNbU45JNKEmDhurDUeFoup7S/HGrDPWJ5iDZ50x/wtaeW5DDr9oWbDuluaIFD5a4wWlRtPS1jYDegp8waJxV4NUWP7UpCnPi6lw1WoJNtfZJXO6zAd856u8ncXdIag7BSPcHRpkt35u73h/1QklS6p/Z1MUyn+vYchSivx2U/N5NNbc0p3bwm18JaOtreiQ1fnbHthjlyzrC/avvAnNm8JqJ7WzhNr8N2j+ldhrqOYQ90uvPOyURHBFwuPDI/bwohUVNPRfws8a9bHrT7yVZmcG/lCtGRcbJlsuWu9Z4uj6vkKnWSSh6OBN/FoWRRjUud6sSVmGluWcFOXafkQSYpb8+eUqtM9NM0QDdqMjdbY3dNjmcU8WdUYB7O+7CktlarHFp0M0+IzQ6lrvZyhTjoYTNPmSLbH0y+rmZTRl/pe3mWHTbF0ZwqlQ82FG3dYG5ondh1tEd5Rpm2re+uldprHR4r8S2e1yk66EmTUebmmK3V3lxMZeAq63i5yp6Ftr3C1/sJa5oKah5lMVJi4QJjbDjou1O3d+F1e6QjDZ8jpT+Tr7goRBfqcCB9YTanS9EzNliqdRPVb6vNMab2fbSElb6L2m0twrtU2R2kUlgdXQ/15CSKZS8SEKY5JQQpTCQpEosrvyJo4cCIGUHAvVviaiKdU1gIFInFAg3oPVvXTEzv0PLE0csSuRji9eRwy1Jvsv66X644f7WLsYUqOg42F/tQb07iwd8QWasQu3UI833M0dxCvtKFmhqSM9gHZQorQn9cta5mlLpNc25nLewAJapYvc5CcwnLmEH6C2clCxtktxWO5iAvDvU1CvFTeIS1o1tFngWjDHHumDw1rxeh08n+QHgwxtXIRqmDc0dXIHAxY3PAXRenJ57SdMiczHSnnVBTwVpcTtkBOcOm1u5bBndTsYepUkNkJoQFtN7uHaMNMI5aT8sY66vV5kx1JkMZiVtIElrSAjdZzaya2PWuXAaMQKLbUG52HXMpL73nrydG1uaC4Ymr0wWne9++yvlpqixiM7TIaNBJr6TNRJiU5iZZM3HR7wOJF6kyW0xLPZGZXT0XzaGeRi2F0Xpv2aJOaAuBK7UM8YKzr6rHZlb1iMHOkXwiUNQhBGij5ftKKHeHsF0y4ZKM0ZVQLBr0stTrbkocIj5gjVSecDyrorsGXzjNKYpUQe+WiheuLCv1XaLMbHO3apTNFZ33gdt3rTAnJETzuWOp95c1frR3InbdaxJ82clYnp0uFe1J+4M3u4J9335/PG8JXTnWDlWhAtPWZhYZ9BlLuInPwPQJ3ygLSXXcobcVs0j5+KTILWOUhQBTnOfLETkp9Umy3u37eDdT7Et5FPK9Ma1X6Cnm8ooFQKj2yjrgWDqaCuh6KOhhWpuOYKtBGy6viUHZmtKsCVFjN6yjzk79porYwwQ5HEsArDUpqdwVaTcbYnGhOu96tfetnKlSctkRLBsW4nxuuudwN5gpxvGLaZCbWtSymy6Vrp6yxgxh7uGohcl4UDc1v5XzIzatY2uD8k1UBrQXXbX1Ze0IPS5ZE5por1PU35G1bizWiXOqilojkHyaSX3lVppN4DM2g08bgixgZqXMkaqoROuAL4+8FGjZPJ9kmTVYyz05ZSYXedWDXz4nNsp5rwSt6Tk9RnOzxYYR4ojHUn9wu3KT95TWeMtkI0bbwL7a/NEwzFaKB2lvrDpeqC25zJZndBme6c7TjFUh9mIa29GqFdgE37CZtcQ1mcLnxWmlMGWo7noiUGfC2s9oe1HOD26+EBM33WoHW5LV4By67UE/nTw3EZ0maTVmvRwGxU0Y4lRZzOB7brQycdsJTeVsZptjx8Op6awV72BQ6wAbcGTJM2iSiHs6a5ZXXjYDk9zkIdzMZicRXzBM4V8Yy0Mx0l87+9RCJHG9Lvi4P4WtEW/zDi5hkQiZeWIaQlyclk2xgjXC3Shtr++wFahll0OL76hwfTBV67DshP5Q8iqVq+daW4p9sC0sq80wBcfpounMw7S5rOxhO8fl1m5PNK+1ejgzpZWIRn1ej+tDczZfo6itIJ0uVpQHy/sNeXAGTOeO9Ybm667wFmeu2p6yVZmfL/0kOu5IerXnT4ksmzYRbdY0V7Byu0yI+aXX080wFEpCLAJWkWM9cgk24BkvMfNTf7JSMb+sOOU8iPkWW682V4qylhQbFaLnzrdhx/AL74Ix7fGck1yxuRp8IdLRqdn6pMEGp7be77T6nFosR2CwqKgMKhgleSbZCYHV1nnDm7jPWCFwHX21WHQVCLQenj22YotrLG8Rqti4TOSzeSbFy+S039piGYjmFp7SSwGZqu6FFzFxOCrY+bq31pueS+IVMahVfTqvuXXY2+tqPT3a5iSSljF/0hWPv0xcM9UKtBYZUPivrbaexvu1BlIPppAmoRJOPh87Up1fLhOJOtZdBPNIMsjbUME47tQjZcarmX6cImrZH3uwaw1Ag7y8RH7dm6cVuj56s8aK1i2y2M6Mjl1aGCLN81XJ7XS2nlLnUGqoktxmXXDQy13azTZ7Cl3UF4uEg52r7ZPB6o5HdE3BAnvAYz7bUlU2rOtcxzK+KtttIeAnY5IuZMPGk0vSiHRiiTtkbrEwujrVWqcdQncVXs4NmRPCLjaWYoTAGXsxuVaHQdkatl2dcBl5Lo+6ncWseLZhy1mSapae4KIhoqXEgLo28MfEY1im6Lcw215E/pAJXrBZR7mE1XC+Rgndk5b+bruU+GHOm0bTp60/6A7C2XrEntWyG8p4VbitgZ6ppeMSeWlSV9fQcZuWyUW/mehi3eXrWjWPVpSVi64TQMGs6m5NXWQRPp6ZjWylHqjN6nafB3NaFw/lPjdLdVgPErW9DvsgPZnCtVyg9Mok7SMlugMqt4FmXlG/z5JtTEmp51xJxEabQoJlo5OHFX06NUF62B3nxyXozCPJP0+E3N/MWGreDpKgL+Z0Kxg7BZUMc3e6ntwE5s9Cq6CECKrZTCyUdYbEa7mSkhSNu0np7bfWdKZWsYlrHSi/ZgTAqfASKpZ5NhEqE2wpiJmbmcYCW/B9w+Ed74ntdi0ZyMB5CUt5O24w5jyzKRvpOjOnCzgNeYKcaafaKC4t2C+a5yl3RPJZqrl0Fm6KTM19hAd9frKp7HLdcUMw2S99GZkvtdDIBPI8PZMCzLXtYSYTwuJaKxE113N1geb08iR33JL1dq3v2bMej8R5eOUYFmXneKnCewK0pgI9NV2l5A3u5Mwuu/TYLnmSpBulnil79QJArj6EEVKxGn3VGZHlIrtIj9wB4ec79KxtusWil5Z9GUbhxEXbS1oriltW6Hojdp1VsQixw7bRbBH5rnNMBTfKNmv/OBi+6VR1YNkyX24Vm2UL1qFQHod1g6wJsZwv9ayI+r6eYlqRCvWiMnbUue4Urz1oO2ZWFL1dpsFuJ2Gos/Z16tzl2/Ki+1ejKSnxECXznYuzKMxwuwmIOk/BDIUtglj1rz1SX210g/P0bGLVCTUJ2nI64Cpu0lLboRbr0wOJHC2rIfyVSasq3uLLTPG2NoZWFa3y65KTJS+1O4RCdcLekQUmX43DcspzZ3utzphD22ApWdGXaVGeBq90VVVYlsdUJztiQaqrydZd+PGs8OrpGrT1E9hcyBeKHiT22FMNkcBbspOEyRQuMKTBVA3JHSvqhDnO4brbZ3lxggl7ZvkK5hVkg1sLvjWknlp7oB+CG7itexpjB2syoffBlBWNBBOzWYbDcoYeCI6qpULCGKNiziY2V1hQbVWdaJC9sLMVsTdmw6YIYbjzlxrFYZtyoantvhH8tZIbJE3yqiEdpGRN5lhM9NKxvoYU3qQpidPZcT0RNitunwaXvdUG0bYgbbnI+FwjfT2QTXfZ45stP9Hr1Tqn4QhWiGFR0eVSPRWWh8xA9mptG6g5nm+P8KWQjCFoGAzl9GKWBTVysncbXzMES0A025sGhKLqJ9veVlW5oFVDUGaOjfaDV00UeWJOGoKa9ufQUpADHIoOGwfbGWlZWxc9YplDpUu38VvgwjzuWZYi8lNNz1FQtxGLSv3qdOQIxass19vSDS1lk8XylGeLzp1M6fMZmR/hRYmfzz0PNl2CHaOUzPWOgV8njuXZ0wUXenm6hEH/kDh6InJVTwgaG7SDJq4XC4qXrzPRMPPtCc2t/owTy+PF6iXcwnawy3WVqUmFIvNqp17SHr5stz3BSDkpTXRpHxZR5jaXJlyF01itZ+v5mVdDMcC5Js4XUxWhhrwOrm1ItZXZb2RuEufU1gzlzp7UgaE5YJe5TxeVs1RD0j6Yh4IYUoQ+bpWSoZiM01IXNAjZXPDZ9RW3AgsvSdXJAozxLmy0XanIDpMWq2HRKUVvoInH0sSkVpMaFI8Mo6azqWLESBLV6iCy7nyeYYyIaSaBgf0F2KmKeNkkKo3b6CCmOWjHY0/aoAR8UohQwKte0T1BCs7yDCeV2um6dS6d3YlIIoGyG9QTfrnwS4PZO1jYDB2nT+qt0wqaq+JNeV26gThx6MhdLWsMY8q25ibB3uqnuhRMuuvEx73Y1Kj5zrgMq/jsOa2CMUR4XilUXqWBdoV7BL5mGefU2AWnVpPprI7zAXQj6QLHkQvoVZZdRMdx1nGXDp3HaHbw5w4+dRm5Yk5gk6tsJ7qMga3thEBAdk+VLkGnvqoxXR77lUEhoP0upNSufAsExf7gFCg5EfzGcnF+rtVEvjAjzSDZkBbnnKytK/Z8ba48wqEKerFx7rhHQT82Bz07vpt40drTudXJj+CroLp+bjea1E/Pc3QrMPScvnKDPq9CPpJCPVHCWcSIO3XHkOZRRwjhyuHpJgzhPb0vE+6aeTGaA7TbcaeZql2Aj5SVv7xccbDLlo9afeKCfl8hNapoyZVGJgii4OghnA6Twm5YVzGU0yVBt02aTPdRbxPlJGEB/FKry2AOAYacM5LernSXZU14mbfNzopU0Gfmc/1Q+hfZnfuekHo9LnRiNolAPMCDe+1Llk7IPNxK6Fa6ADhjfYndel3Bsuzfn56fbl9yn15RhEap56fxg8DjWP9fPBkOr3Hx9iCC0yT5/PS/d4R5P058/8x3O+L3be/1xv31X5Lvt+enyo2BLPdj5Dppw8eB5X87mv3yT06Kx4XD/cvz+A2yb94/gDR2eDvDjjOvrZtqeKvzpL2dYAO7tvX4/03qt8cnhKebKmkxfo/44AXuoxho0OTj6Wx8G4iz8aua78V28/4YPs75n5+8AXgndus3nCLf/KoYFXx8ZhpPcMfvTE9//D+8IpmUPycAAA== -->
