---
name: "rar-cowork-cookbook-configure-manage-procurement-spend"
description: "Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_procurement_spend", "rar_sha256": "161d8204fb47f10dea054675692c8040cb1a45aeb0ef7540bbc9171b963c2c98", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_procurement_spend_agent.py` and in the RCI capsule.

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

Manage procurement spend Configuration Bulk Setup — Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 161d8204fb47f10d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_procurement_spend_agent.py` first:

```bash
python3 configure_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_procurement_spend_agent.py   # or on stdin
python3 configure_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Configuration Bulk Setup — Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_procurement_spend',
    "version": '2.0.1',
    "display_name": 'Manage procurement spend Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '526c93515deb5e55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageProcurementSpend(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProcurementSpend'
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
    print(ConfigureManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebOi2JbvV6FP/5FVTeYRkEHyRkU8RERBQREFrazIYtjMk8xYXd+9N+o5mdV1q2/XixfxzOEIrL3m9Vtrb85vL1ZTB3n58vnlAKwMEa0kCQNQIlbmInze5WUMf+SxDf8hTp7VZWg3dV5WLx9fXFA5ZVjUYZ7B5VxRJCGoEAuxm+RO64V+U1rjY8QJrMwHSJ0jqZVZ8FtR5k5TghRkNVIVAArzyjyFUpEwK5oaEXoHJIgXJuAj0oV1gLRWEroPZqNqZZ4ktuXESNUURV7Wr1Af0FtpkYDq5fPPv3x8CeH3l8+/vTiJVcFbL/xTIbC9a7D7psBhlA/XJ1BHSFgM0CEZvC5A6eVlCm+5wEOeVz9UIPE+Iv/xH3FnlX714+cvGfL8fHkZ/2hNhtTBaKtV1cBFHKuw7DAJ6+EV4ZLOGiqkBHVTZqOrKujPzH99rPzGKS+Qn8ZnPzyEvPqg/uHLSw5VuHvgy8uPSF5CeWUzfn8duRQ//Pia5B0of/jxG5+qsSPg1CMzqPXr1+f1ky0k/EYaenepP0Guj7ja4MvLd8aNn4feo51w5ctrlIfZDw/GMJwtyKzMAT/8+FdsnQA4cRJW9f+K788PxgGwXGjTU/EfP96d/AuCPg165/nXYgsY1r9jCSR/E/cReTrqr3jf/f/fWCdhBqvgzeP/lN0/W4D+hPz8l7b9Tws+It6XlwVIwhZmh52Az8hvXw87gf/5g/vt5odffoes/yWbQ96Uzp3DV1inoQeq+uvXnz9U99sffvn5Q1PAXANW+rUpk3/G85/59S7nDx58Uv3wx7VQ/jGLs7zLkPdMR37Li38rf39FTmP5f7tffUa+r5fxgyKjEW9CHy74rmYqqOt3fvzx5XcIERm0pnHuj2GV//u/I9vQKfMq92rk4OQQhmCA6zAFo/J6EFYI/DvWdgmgX6sQOvZJB/N/jPCoce4hv/4f546cn5wnck7e0BB8feDf1+/w7+sd/359RXTIOS9DP8ysBNG43e7LSAoBEkotSlCBsoV4Yg81+ASR6NP4BaIl8uu/Zv71zue1GH69g2f4QCiNX4/oVDUJeB0tNAKQPe1xIBCDHjgNFJHkjvWA4uojtLzKkxai2+iNKg6TBHHDEpqel8MDmJvs88js119/ta0q+JI94HSKPHpFNYEE7+ognz5Bw7wk9IP6SwacIEc+/Pb7B+Q/kf9p1Z35KGMHkf0ZD6ihdFAVBNZXM9oNQwWDC8HjHo/ffn+6F7LJYHOD0Qu9sVmNi2F+xsB98/VhxX0iKBqxAfQx9G86dheI0UhYvyJrD3nXFwodH40oHuRVjbhg9DTInAFytaA5757MctjjYBJW3vARaSpwl/qrXVp3FVNY6Fb9K7Lld7Bn5MnYJMtnD4GL8yyE7n/PhMd9yKT8UCHzNxaviDJmJFJYpVUEpfWU4VmPuMBe8bYcMreQDHRfsrE/3lPkXh4P90Ai6BnnGdJPY8xhI09hWrnVm+w7jTV2Nv3e4covWfVMfascQ+HAVgCF+g3s17Ah/OOZUlWQN4l79x/UdOT0jIL7jMo9B7d/NR7wf5gn5uOIcYAwUiBfGgLDSeT/8/gx6s6JoiaInC4sEEHRtfPDp+PQNIp5zFlwDEBgYj3q59to8AYsb/j6JUtCmCDl8I8H5T0ST5oHZkHtXQgS2p0/TAPo05HvPUvHrCvLuze+ZG9A/hG65o5a0ARY0jDlR3+8CRyfvmkawLodr7819XtUS3c0HWYiUjR2ArPEA8C9O6EOyrHSnpGAKQvGquuC0An+YBUCucPMgPwRqEQIaweC/d11Sg7NhEV2j8I7eTiOSlALt3GgtnAqBa+IAYtlTJgKViicd0Ya6IUPd1ZICqCPoYrvHq4Cq3goMw6yTwWtMRZ5CnP4+wg8H35L77suo/qQqwVjD33ZjYDrgv4R2Xc9n7GCyqZjQd4X/THcT1uR7zvOP75kdx3fMR7WeTI26++cg8D6Sqt7yo0wVUGoScEzgWAm3Pvy66O1Pnr3uy6f/zS9//D3Bvx7szz+MXKfkaCui+rzZPJocG/97RWCxATmSFiA6luv+/Qotk/fFdune7H9gfPDUZ+Rv6fdH1g80/ozgr9ir9j4aBM6YMzb5wc6g/80P38ix6dfMg18i/IzFUaQTQbYXN87zhsJbDt+CfyR+NGBqrFxdbBX3iEXxuFL9p4Jzzp54A1sl1X+Xf3eWy+M6yNs750BPspqKNsdhzUfjDuZZFS/Ai+fsyZJPr5kVgr+VzuYEf9htkJ3jDsf6Hc4/dQhuF+9T0LjxR+3bveagmDg5p/H0vqIjFPrR+R9AP2IvG0J7tusrIF7op/H4XcUCUnhj3fa932hDV7gLqweilH1xz5nnLmes/CflRgraswUMPb0/L1ER4l/YgK/+D4o/8xEvX+xkidOVLU1duiwfqvuCurpNiOqw+DBqoOFBJO0gQv+LAbKKcG1ga3QHc395r9vZuUPW36/u6F+bBZ/e3nDi2cMnoMhJIeF+akam+EEJioUCK8fKQWf/V+MjE8OEOPgwAJZ4DTuzgiM9GyS8XDMBRZGkTRD0SzhzDASc2zcIikL2BjwGIrEbNthcQa3WXrqEA47g/weqfl17PnhqBXAPDBlccJxpzRBUSSkJyzWtUjGslxsNmMwxnNhG/i2NIYA+TT1Ydrox/fpdXTJ0+LfXmyahJQrslpzjw8/YU+WfZ7YfbBCywTtLzqTb+rlhlH2c7kFcsazGY4tKnFBT/cmp6W8QcXRZeVocQMMD3eEOaqtqMCLUy91iUQWcrTtteXRUSUJMBWjDrNdpByXgrFYMvL+MJjycNWUwrWu1/WxPl1EaYtvK3YjFxcZV9YXEkMvBnlcnfQwYlEUeiJJjSbRTgdpc9gzNZ/KeMpdjKmAJtPtkjpdeDxemxdN2TiMV4S5yVNEGduRxh4LZ8D7LCpiwTXMYSetisSeK8bles38TixmKGh1auK2ZTpZ1v2k3Sh0P8vICpdjrcNXB9kG6fFqGhOhSw6hmcblMclkTfWwhcJeBbgHLA9VgpOKI1FGpeQzd32OtYOw2BeLk3Cb6SXGeluzKfiT0xt4v+tbzo6uqXRarOZ2e+KJVSzUOH0dpBXVYGFbBSHDO/beopa91NCb9qjwuJweNDkRC3y5v5hmw1EYcaDxfZVsS3LSHuXVQib2oiBLTs9P5R5r6isVdYvMitXZfK/vFY+mZIsfks6eytRFZQest5O8yKQZLgPNuR4LpedmpXFurrLVr08i1YScba5u66g62Xtbv+RLozar7HBI1ausXdTYY1SjBsU1O1kGX5ULB51x0sI8Hy6BtUhpnz1Iuk1hiTFJZ85hEYvXYnqpY7xkZoEb1bc9mBKz8zzxJ8p8IG7sTnKkxaY9hXJwqm27Mpm4Ka/9ObXNYeJvNil9kZf2Pu2508TmjMta35DX1BNN3iT1vnflTTRs+yHI9UlK8E7g4w7tn/Ir6AYwYUMcPw4VXV6xCo0x6kwU05sr3cxcjlg+qert/iKWVZeWDm9VfYAbZuXuNH01OPYSU6f5CebEKh5mqWnsErUgCwffofN1xYj6lHQmfbrxWfdq4XXrHXF5Sgbxmugt2pYJDOMOA2oMx7gKozoR3ERqyG1y7q9iPMGWpdfPdpurdxb2N50/qfSiyHRjXxsb/7pYrtUkr2wt3VuMZHXntSsoZOQL1nzYCFOByYVaUJLpvKLlS8gXlyTdGhcyt7VBnZpViHdN2YkEuDj6QsGDod9inrM9elsqCOhlQmu9egxOu9jfbVFsY6pU6GxhKROygdmy5freLGLVWyxcKVKIsa1HnZXAG2hzyVRVgMXrhc1GAt7slUyvnNBYHQxRCy08q1EJABKodKkmutXfaLLsojLGncHHWIwzl22VY7vFfGbeShZT3Ioj2xzfXjzPw/JTcqSyVSMda67VbSOAlhD1fDMh4kB2TbFeujMbs+uGjzppLpl07YqnqhSuZZNcZ6zFFStfWM568UYr7TBPs9De064mHIC72fVyQ5zim3Bj6H0vJaKj7Ccd1nV2cjJikZ4Ou5gEVa8FRdTfFNuHmWzJ5u2kFFrfZeGWE9K2W5bX6W65hdWYJUJ6O4TsPlpiTnVZB+26KqluWafqjkrpQstRwlLIUs1kiTinDcxTNyxUh5wPoS2HHg966eriu71O3G6XJhHACTV2dsROLBcF83wCBC4LTQ5lgk2SSGGNYex62HtGeHYBLeyMYckvzydymN7m+zVlXNenEL1US/vGrXeqXukwN4/qWotU/XhBZ8SGImbpQlL4K7gMu+iybItsTnZ8ulh2XiefrDV2Q4PjWrMi9Bbb5obb+LF6OMyUTRjYx5owZmeX5+KcS8PkcjwWQziv4TDvCErRW4HTKOf5Zu45dZXcLvz5RDd8u1XQ4Wx3cao7UlrB0j9QKF2kDnMpsLQ5pqmreIU7m+xuCQuyubLJ+SRSAE2j+qHpZdWwMTzAs8pZlP7JNHOL5sHEkA9dQ1KB228FOAFHAY5m3iS7YmdllR5zcD2CXSvvSP0k2vYqywiqcLk2lsBV44JI28H2ciqOKWuoITZcVuDSVpRyAXk1WwXn2MeFYTY3bHGw03yw4uGwYLBsnTnRJNK0GiTTaLdnilYvt1GVoLY/FOVlIft5Q1QAF0/KIZu6+VVkqhi7sQoTWancKLra9lgRbWehWl7TlvQLAt0OUWYv4WATRUcfiNWJyGagxArVlAnW8hUS3xgyXloJwBeOL58NMVLMJp4Vk9ZdJNvzcB1WpuAJglRIqFI4lYSLfky2NgkOvr4ql9Pr7njwh5MsWkNvwHY8k5j4EkbYCSK6nqRcdsUrt+e2FOi78zScrlZSbeFGNuM5ur6yieLH87ArdnEsW8PsFC1ZUE+Aap532bHJzF0Q8RjbbJaK6STiatg1W6MP/IYqz0S8c40DNtfXS6Y/KS5hXp110jubiVTmdK5Qtq9tYbAwDKZfoOxrmptdanO7NG6z1lo5yVB7zHJZKc6xEZXYXsvEOiFFuTdVbaAv6xNFen5t+EFxpuf4gF6leiveBCUXu+smkWJMjGKAtR7PopUuUKvDtuVuUyV0hE3uuZUtYaWxWFBJoNPyVDG91LyWy93Gdk6cUh1rcxWLGJpu9iy21q+n7Mi1RXsxj6EQ8ozYdeJ5UUbtnu6bmA456iqYwTZcHic5dohZ8eALGp5ulmgwdUhDReVkruhhK5eafNvGl3NZB/jVPug8LqzElmt0H63CwusEjpMslWDnfWuBeBcfhzVXYuLEVieEYlUxgZm7uU9SdKzMQnfbpoQP22h/HJLArmzYIQVYBgzd+7NenbvpwM99l54zLIE1mahmoGdxsdVin556ppRUW4a+VMEpkvBd4tqt2e1rbLbjNH9rmQSRrvJ5zgsOXymE7fvn+Wlolz4go22hhGIVYZd+Dtpbhea61sq872OFsu8Mg9/rs8Wx8IpbwBvY0WoO5bW6zR2VOWhz/tqorH5claeQOuqhuiTyo7UnxYwT5ntR6aeSNcOxSNG6Juro43CciW24S2WRxxxZ6lzWLq5b8dJB5DknfrGyYe7FaYQWNRlIS7bCQp6/JG7NsUm/RzloNn/OBAONL/ageiGfeVkhOXJBhMV6mfq3wGIJAbv15gLNwUHYcgF+sE9Hmt3ghFqvLrLN1aJ+FageXzk3JyOiZDETquki5Enmkpg0IMsDx7s1rTK8tNwX6WV3GrBNCm0bkpPH3FoOpFZyTg4lpqd79KCCQzn0Vode9uLUjaZKlw7JETOcFL/Cif9gUpp1nJokcSubpRKJ00HQJ/J0XW7a5qgajcZ2azMxFWO5ociYTFZ9Jyl7XN2TfL+N2dyS50NFyWGwbUYwb9w9ubKDDbfytqDA4p214YxGT4PmmNV6ecWZ+W16WdmrvdUqCy1cX6bgJIcyzyVCaZQuIHUnA5c1seZhHyb2fC02+jbTMFryEo52j8GgLbez27UWNwtj0qGpvyCpxU6vtKKCW/PAiNngfBZSQ6jMyfasa+6eJYOj7KqYoTsUp3coShqzYy4fWm6iKpFExaHiLtbWmZVJYc061iJWg/32WOa2FInkfMO5RgMEWeingbhs9TnLE/5yct33J/IYsLzb2Ip4kmRfq4Op5Cn0OqRIo9YaVjmp7f5IVGc/wEpuwwwdI3JzlJJSW3IwbXnGb6vDrdv2O6n3w33nxdZUH4qbdLzu4yL0UZHvzry09ttsD5Oyuhmb/YJaqLB9wDENIybTXPDxbeZu+SPH0zZ6YmS3d09MZedCMQeHTRBJbGsuNv1ZM6IbLlNzZsV285xeSVpn+dnuyvMMHWTiycmVeknVFeiWezeNbNPEJV2V82ohnrylZkwm/EbMmUMTnjou27E+adACZBfYEWm2sdgx4GSdWpcoSJEjiFYAzMBMezPzZmCTMqo6aadSlrH6hcDbklEX1XUu627qqBiNa4LlSgWx1TVLmvF9DItSJLeuXSsYtjPn9mUVo0c4L65hD9xGm57UyK05IdA9K4RLvJpseeo6m2zqdJU2M5+zvMB2N56AemBdLnbWqTLZKGCtAiMdZeFy2pRZGwvRZyijm+KRm9nA1oiB8zJtZuir22XaMnpZzpxFNLux6KTDJ5wdDMxGR+nJZDnFqD2gawZf4bjPMpKby3andqdZMLVyereGucqEZoDqGutUM8PDBBAf92jhoGA9W9taFNxuvBPuup18vs3rZd+rw2WaYHA7qGzYm0pcaCk2Bvua8SXkv8iMAT9G8mLvEmyr7l1S91cxMW+Cs3bRVuxybVOJC7U+sPatYbndZYVu0MZp8pKXthNvtsiZHYHSNNemwY2psMg6ysROE8wtubPcmUsq8j4C1q0tr2tG1YR6YVt4P7glWYsT06tJmuzjg2GuCV8sBd/TV6S58lycQn3Gum6c2mhwbpaHypanySqobEDUO4U1r9ftRmoXs3kxLdVt6cLBUm8rrhf0jEzdig1RO+SnIhWuD2R/np4POw3FbfW8YOl+cjJzcbbyOW56w6aODtvyemh3pzU5qbs5RmX1SohNZ9mX9doG0pyaySRvo6lDFSQOZ3gBTrR+aazNYBXO5F710is62W2CbpbEZETtV0cf41i80We3ZH/cr1IlPshzac9csLnSZNJWRRm+ar2FFeyn3nXdK4qnXZ1CP+jk1GZLa9EQTa/dnEtN7yzgCiv1iJk34Dol0bscQK/JoVGcJmoXrYXaDBOVZ9zJ6ltJBUsm2PdRSjPBilz2p7OKksWVmHCLziHaM7GhxRvTdDI4b3srJIhsrnENnWIMUdoyc4b7aaYrZ8kZJ7AMlMGZWphmeioGdZM5TnvCZqR6Drij0dKWY7DyhQWEQnJbM6LmIApp1Ri8VU8uiHl1Ra/UZG/0oQJn4nU94ZfbHpYdy9j1JJYCPGXKthVpF5+Q3HmTo2eXaUsU30whVlMbcqnJu3p6mXTVTl+KhcPbBgM3WE3VGmeD6t0G8ybkmZWkDEenM6VqJRdVeSn2yzDKOAnubZQIN88ElbGiU/MlGykiz3qOI6MCY7S91+10brGQDibuwon91p7ltR7i292eVhRschOZtDdDwiDgWDI/yYslHp6dYLZyFzzcZSn5dmPtz5Jsi7PNdrW/1d3ykMP/nCAr7ehE0kyoY2cyu3IXi6NX5NWTOjoosJm3GvbmqdKnldduVxLsX5xMgiVvEJy6wi57ar9LLslC929bOMzL/IIy61yRF5lCS4bPAEqjtxUZotMjOa3JdKJOJMEpMm+YrdgibY0bhjXm2rtN9P20xdHFbYNGMsZ2uICq/ek0JywTN1bLcojYE7fUJ8V8crKliW0cJhDqm3nfzW0yDVFcA4Io+lawnIdFP6O7E4UdTlOh0h1rcrvF9ArX00aReDUi8vnWNCqw8Lptol1xUT3kHMf99NPLx5fx5Pp5/vw33jOP54H/z44lHyeIb++i7kfPwHI/32V9/jtK/fLxpXTCUaX78WuVNP7zqPK/Hb5++tfvMMb1w+P17fjarK/fDutryx9/A+klzNymqsvha5Unzf0A+OOL3VTjL0NUX58H3S93w9JiPDV/F/ntLLXOvxbW6MswG98DATe0avC89J+H0R9f3AHGJ3Sqr1Oa+grKYjTz+UYEWke8Yq/4y+//BbLlSXjoJQAA -->
