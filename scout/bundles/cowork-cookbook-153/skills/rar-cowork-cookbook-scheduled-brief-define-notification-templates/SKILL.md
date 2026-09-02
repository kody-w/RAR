---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-templates"
description: "Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_templates", "rar_sha256": "9e7be4ca5be4a89d7726e00865debb3d950dcb675edb163f416ff7f692058e7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_notification_templates_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-notification-templates:647f20acdfb8d4697302759c45823a37ad24693c9ff35fc8bd8348d3195b6b5d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_notification_templates`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_notification_templates_agent.py` is
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

Define notification templates Scheduled Email Brief — Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 9e7be4ca5be4a89d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_templates_agent.py` first:

```bash
python3 scheduled_brief_define_notification_templates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_notification_templates_agent.py   # or on stdin
python3 scheduled_brief_define_notification_templates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification templates Scheduled Email Brief — Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_notification_templates',
    "version": '2.0.0',
    "display_name": 'Define notification templates Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-notification-templates',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '79ffc936993649c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-templates'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-notification-templates', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineNotificationTemplates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineNotificationTemplates'
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
    print(ScheduledBriefDefineNotificationTemplates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WXPjRrbmX8HoPti+VInYF3V0xIAbVgIgCXBzdchYEguxEisBj//7JEhJVb5u91z3zMOwoiQCyDz7+c45SP36ZDd1mJdPr087YGeIYCdJFIISsTMPmeddXsbwVx478D/i5lldRk5T52X19Pzkgcoto6KO8mzc7obAaxLbSQCS5mUWZcEXp4yAj4DUjhKkatLULqMB3kc84EcZQLK8jvzItUcKSA3SIrFrUCF+XiJ1CJASVEWeVdFIMe8yUP4NbqyiIAMeUudI2WSIByn3CFzfARAn/QuUCtxsSAhUT68//+P5KYLfn15/fXITu6q+SQm82Sja4i6H9p0Y5ocUkFJiZwHcUvTQQBm8LkAJRUvhLSg/8n71YwUS/xn5z/+MO7sMqp9ev2bI++fr0/hvC8Uctalzu6qh5K5d2E6URHX/gvBJZ/cVVLRuyqxCbKSC9s2Cl8fOb5TyAvn7+OzHB5OXANQ/fn3KoQh3ob8+/TTa4OsTNAn8/jJSKX786SXJO1D++NM3OlXjXIBbj8Sg1C9v79fvZOHCb0sj/87175Dqw88O+Pr0nXLj5yH3qCfc+fRyyaPsxwfhosxbkNmZC3786c/IQk+4cRJV9X+L7s8PwiGwPajTu+A/Pd+N/A9k8q7QJ80/Zwvdm/0VTeDyD3bPyLuh/oz23f7/hXQCI6z6tPg/JffPNkz+jvz8p7r9qw3PiP/1aQGSqIXRAVPnFfn1bWcs5z//4H27+cM/foOk/49kdnlTuncKb6mdRT6o6re3n3+o7rd/+MfPPzQFjDVgp29Nmfwzmv/Mrnc+v7Pg+6off78X8reyOIOZj3xGOvJrXvyP8rcXZG8nkfftfvWKfJ8v42eCjEp8MH2Y4LucqaCs39nxp6ffIFhkUJvGvT+GWf4f/4GsI7fMq9yvkZ2bN/WIOXWUglF4M4wqxHxP6l92iqSqL6n3CwLvjukOIcJukhoRyhH8YD6MHh81yH3kl//p3pH1i/uOrNPqA5be7pD59gDIt+8B8u0TIH95QcwQypCXURBldoJsecNA7ABk9cj9HicQbb+0owBQuOgBQNu5NIJPBdn8DfnlL3F8uxN/KfpRva8Z9Jcd3VEYLshLiOoQhO0Rv5y+Bl8gAkOMKfMkcWw3RsYfTfEy2uwQguzdki4sNuAG3KYGSJK7UAs/gqj9PKJ+nrQQL0f7VnGUJIgXldB4ednfqxL0wetI7JdffnHsKvyaPQCaQB7VqJrCBZ8CI1++FCXwkygI668ZcMMc+eHX335A/hfyr3bdiY88DFg13msRlFDe6RoCM7ZJ4bIKGcMFwtHdo7/+9vDKKB2sVAjMM2hHcN8MqX0Lj1GDh6s+/AR1HkUE5Tun39sN6UJoFySqobVg7lfPX7ORRA6Xll1UgQ8jPjY/TP/h+Aef0SfVuw2hn/wyT+9r75E5OtPNS+8FkXzk01JQXejXevRomFc1DOYCZB7I3B7utOtvLoThglQwWCq/f0aaCqo6Uv7FgaRH46QQtOz6F2Q9N2D9y5OPsj0ugrvzLBod/x65j9uQSPkDjLHZB4kXRAPQmkhhl3YRlnYF7ut8+xERsO597IfEbSQDHTIWfTD66B7G98hb/MuO47MrQJb3XuXeHCBfGxzFSOT/i8Zm1IEXhO1S4M3lAllq5vb0CLixKRv1f/RxsK14ZzMiwWer8YFKH3j9NUsi6KSy/9tjpX+PsceaBwY2JRRmy2/v9MdsL+90oxpGyuj6shyj2/6afRSGZ2h86KdqVBkmdPzQ5YPh+PRD0hBm7Xj9rUlAHkE4JgcMb6RonCRyER8A754JdViOefbuDxg2YMw5mBhu+DutEEgdhgSkj0AhIhi/0Lp308EWLxz9cw/+z+XR2HpBKbzGhdLChAIvyGGMb+iBCnEA7J/GNdAKP9xJISmANoYiflq4Cu3iIczYKL8LaI++yFPo8u898P4QxupYgSC/z0SEVG3PrqEtO+gEmGe3h2c/5Xz3FRQ2HZPivun37n7XFfm+gv1tTEYo47fCAHv7exR/Mw4MzjKt7qAEy3JcwXRPwWecPur8y6NUP3qBT1le/zAd/PjXBoh78bV+77lXJKzronqdTh8F8qM+vrh5OoUxEhWg+lYrH1n45ZFzX77PuS+fOfc7Jg+bvSJ/TdDfkXiP8FcEe0Ff0PGRGrlgDOH3D7TL/Mvs9IUcn37NtuCbw9+jYsQ8mNtO/1l6PpbA+hOUIBgXP0pRNVawDhbNOwLeS8lnULynDATYLBjrZpV/l8qjTqOLHx78RGr4KBtrgDf2gQEYx6VkFL8CT69ZkyTPT5mdgr84Jo3ADEMYGmYctGA6wRarjsD96rPdGi9+Py/eEw0ihJe/jvkGiyBsjZ+Rzy73GfmYO+5TXdbAwevnscMeWcKl8Nfn2s9h1AFPcOir+2JU4jFMjY3de8P9RyHGNIMSu2As8/ln3o4c/0AEfgkCUP6RiH7/Yifv4FHV9lg6YcV+T/mPgH1GoBthKsLsgqDZwA1/ZAP5lODawGLtjep+s983tfKHLr/dzVA/JtJfnz5AZPz+6BweITTS/rdavdG+HyX6beRi32mNDdnd3Pf29g2qGo2l+LtHwdhXvD3C8+kVwhF4fhqNWkawZx/ug/nTQzSo07fGGFKAwPKlGluLKcwuSAkW/GLUJ4ag+B2D8Xbk3dePX17/vJv+7yDEK00yPo7aruc7rEfSHEOgOENxLkmxOGETjO3h8C7hcr5PUL7LOh5LkKxHYBzl0A7lQYlGhqn9LtEUG30Ddfl0wP9du//0IAZLDU7RkBoHGAeQrk3BnzbLeQyD0wBFWZrygOMQHkehnuvQDAWrJ0YTPonRvs/4NIejFAsYe6T33mM+JHz76Oc/vPVAjTcIumk0yo/btsu6DEZ6HGPTLiBQh3ABhmMeQwCU4gifZQEJ7pZ4bH332OjQhxHGwIbtJWzu2pHPr+8RMAYrTcKVIllJ/OMzn3J7m8YZZxs6k5IGp/NxKjmRRbeHnrA8W9Vz2lx48zg4G16e8SsvjvRCiYtFtQ4ZOxICk1pmzMyoapZaM71kFYN6yld1vDjh+tFIBzVhqaEW57kccMug9hRq6URXDpXSql4nq8I7r+SoTm5uHReeRFt0TB7QxotOINkH7e2GT6YazsXZPL1p6aFhJxZKlUDZcwXdnu1kGh6N7bHMhE1tRuk12SpJdToq5c5WqCE5UvysqY/NiWxNJSpFfbtpZeFk4JhV+Gc57DWzIFnd5Bi3Va+MvCTBlLlO196mlZT8pu/2fVSFNF4kuwSrp3PRjuLNYV2fzoartZ5AebhSWO6FULzVoLitwav7W07rwvG0FLy9aMmmSxlDkrI3CVNW16a0Fn0tqZclZ+ObnDmuOUs925ESNyslKUCdymWCcnik5wzQsqgu9tMtY53zMnErVjpUcRH3q0Fbb7PauxWhfrPmV+18lORsx4dncxrPihM2JwQOrZIrPZDzuKq0fnvebFbgUPJX0zABKTJ9r6xx+kD2ThKUWUFYc2MPrntFJE87q6zKag8xd63ZxIxz3WqndHtHbvRDZdjJrnflq82eNSvGvUlFgt0EA5lmVSsSyCQtW2EZyXpR6mYuJI5hTY8CcNT9MFTiLlJYtwEHx/dpAVcI9+avnXCyPiwAJc+bgRvWx6rAVkspS/BCCV3rPLFd6MyV5SSaY51tOdB2K8Dmk1q6aDe7ja4Fe3ZvbWiI6s1ah57hSjthur9ELh9Trba5DSvV3rAXFmPs9pzK+/3p4IlbNGkX4m3CqstSYjdLp9hwVYDrIOsdcO1trjTKNHWOPjpkapKSlWExy7ZDzc7MSJ/osppkKUxfLQ/ltNOdbEn608uFm0ecSNHFUHXs0vQdPxKDi7NSr3kpi8NZltQCJIdajSIVSzpcWeTrcykur42gHkJytb4c3IS9gm5pNEWirnDR0Ct3RvrZWuo7IO+P+qLcL1Ww3HRaQPSRkia9JmXLyonPaHTi163szEx+l6hSXlwJfSl0rskN9NEmDwSJT7yYtrVkKI2t3p97MU7prErtCzpwtcKaVhascHNPZelV3Z6bvLHRS7e47ottT7WOOF1xvEfrzhwtDjRpzKs68Xv7uGLy6rZRNCEQushmFJub3YzbImpUb0dogdLLfnTMGlGEybA1O22K7vRzmR0a1eTDa3yL5wGlg+tq6IJ0T9dM22MSPqMtZ7KMM60te5rhhGs0CC7N+o5iH4p62CyONXNoMR+j5GBtX9FTVAUo52GXyNeCROHKi7UWlYyNIhLWDMxW9FmcXRc5ahjBgSwPOQb7OCew5u2wM9mdWl/pJZl6vqfIlkQ014xa4jtF7xVF9LxYRGHR5dHbTKZOh1ra1Ocas+K+Z46uK6Pzap0mN14rhubs2viQrHhC9Q/RPMMj90TNwdkj1ZCyxfVi2OOHWq5Rph6YHcxEa98qmse5WGqupXxAS3pQLuER8A7BmSdqKp3bw47L0I3UTPacQK6MoOQ4itnz1GAAcrGIBnXuTpoKixZU1roxz/o1iwmKHtBZjBnicMjzgj1tgEsR9io2yMZB94uBtQC/GVp/Wcxu2kDRk3mR5Jp7AHNXtCgtScNLsBRNTZpLs11jOf2Uv25sL1hElLDfdIkbV5JVedWywHHVj6ulKGEF4C+kGbXXQ6Npi4OcRQE2y32dd41ZOIf9mx6zw9lazwPdblh9B+t9nIQwPwHHzwnqBIic0uvhxq4ENzWuCiNmBMEZZjVxq2EZxJPzdRCOpuvL1D7eG4rWuxi9ZRUwVzRVHI5lh7FVoOM4xYU1rvDSxGu5206hppPjkZuK/n4KTIfog8kSm83ZiGVRYiVtRCsI0aK1Re1EJectmBcr8uLpgZEPR3urFWvoFoLferOrXNALTle15spI1+2qIELtKM1RTD3UW7AprCyUrvo0ynbhfH9LtrgpHy7d9Fac7ZNGVWMpz6RWRAtRdheu6vXokkqKON9kaju4LNUUJcznWLoRwcFyIQjh4c7dJejWnup0rB2UY0Mc2Y124wmpVoWq9c7OFjtMhfn5VmCp3mwEaU2y+2ppn5zaYKzVjpr6BzC5hcujhhtyKPcen3IrfXFbbe2G5DTBY1rHYSzTlSzFLK6TwWPT04YtT7OzlJ1uzs3CanB0ixXmmozM3eh4nvCudsaPmLffOTMpXpm3gwzwNDpJVu0tWoXaN7tVnG5nBduokXA5iSqLyobd2w1Q5JYDS13O+nALViZmCBt5zs0CV5ksrLwUg+s6ybLeLdUNmZ8wVZufJ3NcpSsas06udjSLubDZNLP92l9Oc8BdYE3M8jkEwFuwAstwvcrrwjNvVTk/4nEkHORp7s47bXLGV+R8CnB0vcHlHWZP0tLHT5cSNzVtV9HBktGmVzrZxG62YYQcDbz1mRGOKMcAdiso4jHcxSV75kHmzc34eDWvirQbugEidnm+daeTv7IPtFCfIGIta1w88GEwP8ab7TrQ3Ck7vzr8Ugx2s/Wh4qeM5uxELN+hQY7OWtNgqga3whtBgDqnJCVbx3zdqLfS532uXMA6eoIjMB3PAIhEn6JZtlqLs4JG1fC4ZEBKGz7MGOGGEWcNnG5YWxlHZ0dpTVF7IrM+SvR+S+MTCiXSRUqL6LBULxlx3s6XoryYbQLnwgMydjxF32bVghLsmVZv1LW25QxYgXYZthe0M5/lNiHkKV/sSnMmeWVBhupB0HbhHj2e0Xkk9Q45nyegFtRtLguLoxKuw3y1nzP7huens4CZnfiLnzjDjhQPKHpduUown6siMedDr1FOkksPsBXrh2C2iPnpynDJnvesCp1eTV/anX1HW/JBdj46G4NyLSNXz7cQmFEBdmzrCl7v6heFkmeyqVuGLEpbf7KWduv4FpGWZMa9qxKbZpqfrvk6LSz6KMf1dr1LB823zaIQl9ZydsxgtyMIR1KVzEnUW4OdtLSbL7SLHDZkYwq3PXAPu+tiYqaOLjnGcW+2Z08PDdbF9mE+94mNWYntRW7FcztztO7s+uvzhJSuOybBOdc8sDv2egUhfVHPul4eVPM0dDufOtT6jWHSWUIFnskLrHXQlYUopZM2xpfNVeU3J4lsrfVVjCJYAzc51Rb2KVoe9YO78LrYmuyT7GgBkJTaJENdQlrrNAf8zoNJQ8ww0YQBsV1HV4w+NMo83dR0rrF8ttHZmMftuVXPMGvWpo25FimUkXWl6uTzVirYyy7RS//E8uc2Nk8YF+9rZcn02X4hm9uqpGe3myAaeRR4gZ77MxnfrtOdiTXpye4EdxpTnrJcD7CC34a4c1s03YcxZU1SfZHuIi1WZmnury1WuoYzOtiuIUbMFiFzEfxsU3Dry3o2dFN2r4sXX9YJLTPtIO+gzdhlke53IWCzeUaAS5kdr4tpHUQRe5mrlWh6AqtMhFVyLk4ov9+gkXhcBlrtTLJ9OV2L2+0FGDtCL9jAtnBBIE+6wR9kQVwzs/J2vGhKsljHEjrEPVsTxxPRohttj/sof+n41ln0xmZoyqqtF+Y8kZSdJPhacV1LWzqUyk02uawrdh/SMebFXX7OZkWWrGSvPQzZzrkJ60TLCoZwjPlVOuXi0T5iFKz/QWwH10lk1qFNK/H0hJYmGRDSiU1mjcOIzQp4k9OWnta0c0G9+sqx2OF8mKRgghbxhDgGzMr1SZmsfKw36p7STpbj6D0nTKjLsNpKsKvHlEPmW3ianOx9WHfAJLaWxMORiNqcV9oNIy8YJmIhpaHuYhPFoTycugigEioYXCsd0UiIF7BJPFOtT3fLmu94y7UEuWescn4ZCjw57T04MGG4LGIV54UDqqNAmFa3o3u9NJoz3+A+7tUUzu+Ty8Rdhc3s2KmtjQfTfUetMkZkptOwnASnbYIf2mmZTeRWZXAOG9Bjy9yELb5nbIu0uJt0ihSnkIxZiXrrpR5NyGaTuHP2NM2dWgqC1bSl5LO55WfFDSXJnXAQ0UUsOTEEHGrBpt7NVSPM3E3doU71qBN575wyNW3Mup5wD1F67q5ic0yYIcuUdU/vTgA1FFVSpvlw8dcCmAj8gpyqTrGs5elsrQ0rVBgib8X6ectTOE74pyPL6+c6qexymQ+YIMN2pmkY/tat8QM/EairmoSoH3FnsaHsC0vAAWw6qX2uwzZJtjkaHZ/ky7wK3BZOHnrInAeaqFOpGWyuziHWrxanVX07l/aES2jA3Mp9eahdUj9oAM6GCuO3JMpQi7W7XOnzzGndKpVa47a2oqUuCRouZagNkmO1ZTnZqVWqaJaBipfCippcTpbG7vp21XHssTPQXLwNC17350E362w0cjlmBSfAibzGz2RKHA/uUTdcq1weuyCJpBVsVSyCaInQ80NBzP0rTy+FKm2nmJ66zWJunKSqO5zkzWV2uK0rUQ86OHkqNMfB1s+mF04qHwl2m803aDGZGWyCO/jU8MJzpKas6eggTdJVdR50n8uFbtrUWbg5HOasVqZLnzQTP2kaicadozLUh6kr9/RS571j0B0nm05ndVi07cmF53oXD0hcJVWTSYKFoR3s+sbkZ77YqLO60pvApglvUV4db8/Egzn4AC/doMPkOl1vb57D7+kJIRvpwuVX8mCuej/vpmpzywO+r/xuRRtDgDkSCcRcPKW9TV8zTkolijObcNYueVRhJpNAXXHTc91iXIClTOlzM0wmmLRhN9FyxTY6YA4ksGfT3W2RTVwYCi2zm8as1K/SOsbMjUpVt5xgiJJ33AlOkMaUvVYhuV8AjuAdhj60wSY4SxNWsuCcAoRrRUfndBpXIaA1OHmt7KY5C36wZ49kPF1Y6KKzNwF3PN5QlCPmkUzX6WlXpbDnOsteTxIYnFrdQ6vz8erKbfNN4WUJf0HXjJHzQk6vl6eD3USmQejq5mKhOOe4YWLhUwa3WlE0fe6gdEKo7ENvMU2MeOJ1M1IXJ+Qe4+ylx2bOcOv4OdaFxgrL5+ww6cjo2io+MIVc8AS7NRdq15aql4q7tlBBn5QY0ZyMiyrJIuH2A+yyJtLMDNYlZwZtI2BpL8Ea6N2mmpfKre9YwoFg9P2R4LvZ2mfXkYfaO+1AyJdI7S0Jc7ikqGG2nlFtrXj+4tKJ9OwksiwFLEGJ7d123i0Zf39SprQs0ZdebTWDnN9YkTFxUu96G8N73TieJe/SkovLTA3ALL7yPP/3p+en+xnx0yuGMgzz/DQeIbwfBPzb746DISre3skSDIk+P/2/e4H5eJn4cXh4PxYAtvd65/76b0r8j+en0o2gdI9Xz1XSBO8vMP/Ly9svf+nt8kiqf5yEj6eft/rjoKW2g/ub8Cjzmqou+7cqT5r7e3DojaYa/0amens/mni6q5sW9fur5u/Ug3dsL42yCPIo3+r87XFiAJ7Gv2YZD/eAF327DN4PE56fvB46OHKrN4Km3kBZjPq/n22NL3zHw62n3/43QdzDlh0oAAA= -->
