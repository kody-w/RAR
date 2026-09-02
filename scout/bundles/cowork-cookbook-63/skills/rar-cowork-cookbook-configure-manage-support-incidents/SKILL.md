---
name: "rar-cowork-cookbook-configure-manage-support-incidents"
description: "Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_support_incidents", "rar_sha256": "7bba4b977d2b457c1b75a698b551aa1b122788ecff82509809259a9d0889a9a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_support_incidents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-support-incidents:72c507c89bfab3a8fd8604a3f853e049f03d96b21c60b2cda16b4db282f78a7f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_support_incidents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_support_incidents_agent.py` is
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

Manage support incidents Configuration Bulk Setup — Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 7bba4b977d2b457c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_support_incidents_agent.py` first:

```bash
python3 configure_manage_support_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_support_incidents_agent.py   # or on stdin
python3 configure_manage_support_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage support incidents Configuration Bulk Setup — Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_support_incidents',
    "version": '2.0.0',
    "display_name": 'Manage support incidents Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-support-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-support-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '654bffc250c9f16d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/manage-support-incidents'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-support-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageSupportIncidents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSupportIncidents'
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
    print(ConfigureManageSupportIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjyHb9K7j8oWes6mITi+rFi7AWBGgDsQkxPVHNkmxiE6vQeP67E0lV3e154+dxOMLq6BaCzJt3Pfck2b892U0d5uXT65MK7Azh7SSJQlAiduYh87zLyxP8yk8O/Iu4eVaXkdPUeVk9PT95oHLLqKijPIPTp0WRRKBCbMRpkttYPwqa0h4eI25oZwFA6hxJ7cyGV1VTFHlZI1HmRh7I6grxyzyFq8I7RVMj3MUFCeJHCXhGuqgOkdZOIu8ubFCtzJPEsd3Tu6AXqA+42GmRgOrp9Zdfn58ieP30+tuTm9gVvPU0fygEtjcN1Ps88X19OD+BOsKBRQ8dksHfBSj9vEzhLQ/4yOPXTxVI/Gfk3/7t1NllUP38+iVDHp8vT8MfpcmQOhxstasaeIhrF7YTJVHdvyDTpLP7CilB3ZTZ4KoK+jMLXu4zv0nKC+Tvw7Of7ou8BKD+6ctTDlW4eeDL089IXsL1yma4fhmkFD/9/JLkHSh/+vmbnKpxYuDWgzCo9cvb4/dDLBz4bWjk31b9O5R6j6sDvjx9Z9zwues92AlnPr3EeZT9dBdclHkLMjtzwU8//5lYNwTuKYmq+n8k95e74BDYHrTpofjPzzcn/4qMHgZ9yPzzZQsY1r9iCRz+vtwz8nDUn8m++f+/iE6iDFbBu8f/obh/NGH0d+SXP7Xtv5vwjPhfnhYgiVqYHU4CXpHf3lSZm//yyft289Ovv0PR/1SMmjele5PwBus08kFVv7398qm63f706y+fmgLmGrDTt6ZM/pHMf+TX2zo/ePAx6qcf58L19eyU5V2GfGQ68lte/Ev5+wtiDOX/7X71inxfL8NnhAxGvC96d8F3NVNBXb/z489Pv0OIyKA1jXt7DKv8X/8V2UZumVe5XyOqm0MYggGuoxQMymthVCHao6i/qmtxs3lJva8IvDuUO4QIu0lqhC/tKEFgPQwRHyzIfeTrv7s3JP3sPpAUfUdH8HbHw7cHjL194OHXF0QL4cJ5GQVRZieIMpVlBA7N6mHJW3JUTfq5HVaFGkV31FHm4oA4VZOAvyFf//kybzeJL0U/GPIlg5GxYbg8pAYpHGiXUdIj9g3U+xp8hggL0eQDe4d/muJl8M4hBNnDZy4EcXABblMDJMld+w7j1TMMe5UnLUTGwZPVKUoSxItK6Ka87O+g3mSvg7CvX786dhV+ye5QTCL3PlOhcMCHwsjnz0UJ/CQKwvpLBtwwRz799vsn5D+Q/27WTfiwhgy7ws1jMJ0TZKVKOwTWZpPeetGQGBB4brH77fd7KAbtMtgYYUVF/tDo6iE83yXCYME9Pu/BgTYPKoLysdKPfkO6EPoFiWroLVjl1fOXbBCRw6FlF1Xg3Yn3yXfXv0f7vs4Qk+rhQxinWwcdxt5ycAimm5feCyL6yIenoLlDAgwRDfOqhmlbgAxmgtvDmXb9LYRZXiMVrJzK75+RpoKmDpK/OlD04JwUwpNdf0W2cxl2ujwZWnv56Hxwdp5FQ+Af6Xq/DYWUn2COzd5FvCA7AL2JFHZpF2FpV+A2zrfvGQE73Pt8KNxGMtAhQ1MHQ4xuNX3LvO2fEYr5DwxkNpASFQJPgXxpCAwfI//PhGXQfcrzCsdPNW6BcDtNOd4TbaBZg913ZgaJAwKJx71qvpGJd9x5R+QvWRLB4JT93+4j/Vtu3cfcUQ7CgAdRRLnJH6q8vMmNapghQ8jL8uaNL9k79D9D18D4VIMJsJBPAyzkHwsOT981DWG1Dr+/0QDknnyD6TCtkaJxkshFfAC8mxPqsBzq6xEJmC5gqDVYEG74g1UIlA5TAcpHoBIR9DpsDzfX7WCdQOp0j8LH8GggV1ALr3GhtrCQwAtyGPIa5maFOAAypGEM9MKnmygkBdDHUMUPD1ehXdyVGajvQ0F7iEWe2jX4PgKPhzBHhx4D1/soQCjVhrGHvuxgEGB9Xe6R/dDzESuobDoUw23Sj+F+2Ip836P+NhQh1PFbF4BsfWjv3zkHIneZVreUg433VMEyT8EjgWAm3Dr5y70Z37v9hy6vf+D7P/21LcGtveo/Ru4VCeu6qF5R9N4C3zvgi5unKMyRqADVt274+V5snx818vmj2H6QfHfUK/LXtPtBxCOtXxH8BXvBhkebyAVD3j4+0Bnzz7Pj5/Hw9EumgG9RfqTCAHAQdJ3+o8+8D4HNJihBMAy+951qaFcd7JA3uLv1jY9MeNTJHW9gw6jy7+p3sGmI6z1sH7AMH2UD4HsDvQvAsPdJBvUr8PSaNUny/JTZKfgf7XkG7IXZCt0x7JVg5UC+VEfg9uuDOw0/ftzs3WoKgoGXvw6lBfsc5LnPyAdlfUbeNxG3jVnWwF3ULwNdHpaEQ+HXx9iPnaQDnuC+re6LQfX7zmhgaQ/2/EclhoqCGrtg6OT5R4kOK/5BCLwIAlD+UYh0u7CTB05UtT10R9iUH9VdQT29ZkB1GDxYdbCQYJI2cMIfl4HrlODcwH7sDeZ+8983s/K7Lb/f3FDft5e/Pb3jxXB9Jwf3xIET/gKFG5z63nrfBtH2IOBGtG4+vhHUN2hfNLTY7x4FA194u2fi0yuEG/D8NHiyjGAPu9421E93faAh36gtlACB43M1UAYUFhKUBBt5MRhxgqD33QLD7ci7jR8uXv+cD/8pArwyhEthjMtOHN92SJv1PZbGxjbpsxQJsPHEx0hvQjsE7tKYQ7iejdPO2HMIlvAZ1mZ8qMYQy9R+qIHiQxSgAR+u/l+w9Ke7BNg0CIqGIhjHscfOhGE8whlTjIs7DGXTE9ahKNy2cQcnCIZlgev7LEFhExabENTEnngYy8IvmxzkPYjCXa23d0b+Hpc7FLxB+EyjQWnCtl3WZfCxN2Fs2gUk5pAuwAncY6BbqAn0DwvGcP7H1EdshtDdLR/yFhJESM/aYZ3fHrEecpEew5HCuBKn988cnRg2c2ScXQitpP3gHLMshuZx7xyXeI1VUoFLTcfbu214qvsoDU/Fqt4S0mZ9jnYzuT2K05GyGnUas8nMYq1uhEYt8nZ5zCWs0s2ebVejTKgaSo3WSjVJRM9bE+tjpRn6xrT3tI4Z9cU5FUZWesZmcyjCmb+TU7xZKrg+Ln2/TYxsZSRloRt6tMdOErPTNNAH29iOJHzRJcAg9oU15jILlzaRZhd95a2pNA8d84BysXvBqVxbiaFk9P6OK2pvhvEdJrUtTeOuaVKjSduGqrm5jFFQMqkZTXRbERZ+Mt+1Jm9sShBZh0LZkIpxVvtEzCRaSUe4FbvJBhbgrpfcAteruphQka3yKbdexUpBGvszR6OSWS7H531tVEboXVn1yufrMjphly7NcLVO6Gkpu+ftWR2VyapkOLsOYgc7xHu3lyGnos3ESZRQvagr9Wyk0Tk+jtGu5ZI+O54NPUz9dkJN99URrLk+DJfpihjj0o5sM86auYweEcFUtPHYJmf6leiaGXvxSqstiO0JP65HhLebxxh5TsQr6+E8fl6d51GlJlbtpLkcx3i6J+blcRc2eFjqzkErdppg7s6ntG8n2frQHmot2pUzIIcA2Lq4xkKt2hhutt+cL8ACzZYlQJll+21SX+cTl21GAMVWlXem5oRNZmP8uOv2frm9gispWd2G9xRdrc9nMhltC9w9kMtL2hvxxRuTMXR/OsVFlaGOdCtOi2ymXDGSisuZP9qc9IjXW/Z44FsrjtxtQcmz9eo621g6G7IXlGmTs6gZhOnFvF8wXTcBdXr2MolTeNoQjuB0uuxMo9j5mrUlGO08J4/EIY9JjMba7uh3+7gHspVPuiogpUTX83YsLwRuhIINQ7vuUdjganYYTSZX3fJVoGbOrCjc1r5Wkn5YM2ZilBq1Cj2L95NFwW+Ph8t6Eo5wtPWp8WKx1Jr50SxK1YVAdE3azk344yEJtkvtQFxjjSuBsJxzUzJqpH0ucFWWnxlOwaKqOfEnRa+Vpbaqir6XMsmVVucxq6+ape4I2bWVNXFXSpnPXUPi4mG+26RypZjh4lTsM2tbdvJOIq6S3iySht1dVDIo1Gu1Q09+d5X2amUGtrYfsUZwWKKb2jXP5+syyHUOY/hVyeYOIegoJ/Gn6rSLbX4XGeNkQoc56lRnSy5NOY/Ynmjq6WGkMOYqPiaXfrqjRbHb8wd6QpI1NMSvLhib41sHRTNNI2DBAynB+ytc8VB4mUqQRXFgKdZRramJ4+VlZAlLgnamp+s81GOWbBKRMCp9J5iCJZUrveNm430rKDnLFmsJrOpFgafKhjorIzEhyF0qnnxf51fbMXY6myOuGS1O53OHjUyplTYhO8r768LJ4vCAhXM2xY1uXm7Oh0tHqmuFS1vRKM/kNtnyBZ6F69AqDDfvI9qXZoew3VbtskvqppEpmi6UE8Fsr8cJTgU9nhBy3JGn0OiOM49XUn2kY6xKTomE1ZmZ7LTLE2N49LI+AbMlW5Ps0Ey5+nngZrFQxF2x6qZEXDIzPhhtT+N+wuU+i9m8HVzJU9vyR+0YGEcsZEO9JDPRVLYx1fhxBMbLnbT2tBMpuLKAEqCysLWlVJum1vSRysxUUSq2eTDhlsE5IlVqyea8yC2qWWhJvTYV1VPA2Xq44HFIv+ueqULxONsFGxvLgyhfjLhi16jyYcx2jcApUzU3u42zcgklTUAclOTCb5oDuxN1cu6U8rTaHIRKzqgsaTP1QKuSheNoRVzZcWUmF/fEna/rg0hcmZY+GquV0l9But1Vi7nuz6NgPFmgu0zGkykhkHLlV9O9IvS06vorujZGjaopo8Q3cha9mn0w4gxlzpxZ9kTuxP2SDUKsONnCzriuySidqSV+pB1zMyVG4l4npRUIq/kmtw5zlJvjMz0m6GNasPZp5IWCGE/dke0VRtCgOrtoE2lhilo/843OCtA+GNfz2YjZE1i3aPoJ5Z6jraxRhFBvtkzMX2t0u6zMzUpbH8tIny74COMLFsh42ag6vS/UlBkl5cLFvGVvkd12zfFWuMuamqU6yYs9aaymV8HchtxBOq4a4eo2BlEEId86uaMSjujw06N8spN+OeftM2UWsuP45hTl9m6UxmKsV95c38RA60RxQllnN1y2hidwfMyMp926OsfJfq9bEbuS0wWRhNSRWNOexOARfQHNJZIacy3gDeemO8qLDNPTo8mCicypm5aq3U3ws2NwQWfMliFbqLWj4fIpIuq1n1J6rUr7tJue9xQu8a1qjzfdcmolxhwHF9YHh24+Mdv6HBNpsTaDqK/pmcvtRwshrzOx8HanA83KvFruFa729gzwlycy1axIqGPLXPZpsJvl46LekhfNd04X6YDFm8Vutjlm1ny3ocpTuE1swg6rYLMrhAVuwbiuxyYMa7HdjzZqbLv70iGOqEaau92hsgOBqZmcXh5ThTxOeLELPXZZCKaBb7DDbrdPR9aYpGYxy+S9HoSQCNgy58dp32CXhLUSUdqcTxv5slq7IpMvo4sFs0BXt0Y0UsLJ5ZgcRkEuT9XIqhktq6la9NN4HfOHgKZX6KJzrFwGpD32BHGmT+rpetYBz1stLsXJwjfzuepMqLXQohlDEPUk3U7DdDoU8mTDj8ix2TmCeTlN6Mw8991kI5cYQaQTRiKOzQWjs76O8ZzaGzZw9+JBkjZMXSz0GT+bh1Oi4dEg7XjISuQZGs4t1eG2nlkRUTTxzeKitVf7sFTDPNhZ3cWdVRkVFR0abIr5odLtRo2DFlIu2UuUmXoOwUTThdg4U7qWuZtaryAWrvxgL8yO09iPnasirrYYh1GCxrtzaUuqq/7SUfYx6hccusNIflrR++mkUns3niTRqb9aqM6P1FNPEPRJnXuJUU/R5KKMgjrjV5S0rql1P95749VEOzJYKic6s2dPc/PodMqB4bdb1AgmuVCFi6OoGFlibDVNdOMzRSiEuC70UaxWyoH0HHEidj2qtG6Xu7BRWtooW4uYyOWMVFYdLAFjoTc9SEiRXCZc3RZnsl+PlIN7NpLruBFO0QTjmBlD9/aMcDri6sYZb6ZoHG2ihvI8U95Vibw+kwUQe0KLC7yZL3kw99B1URIbx19vW5c094v2HFkQ40QlxcWtlqt07s5mQRxNLHyP6ZJgqYIwvzjoXJmP8WvgNNx86kYYV6pHNq8Mm2oO5qS3L80kascNYApGsxbG7EzbPe+QiZ1Hp2BlrfFzR9bzhVlJ3dSGSpmBsQ0JS4cUonBGeablUFuxFkJ+wa1br7xOCXq3i/ntRbrssovOB8u1vVsu1JIQryt/S5K2c542qndSizS9Os4qAsKFrNCkVkSOjccUwV5P6wtZuDGkJFM2kTbZYT4L1zO1AHNL94jxzJsXIdHh3hKIl4zieF9bsufjqah7wYJMYEWOfdvWuXTOA8GP3WuZOvHJpndEbk8IOiDGka5Lp6PhgdS3sL3WedSIOnjSMj+vGFN3N6h0WFm8y/XNLIp1GhiSZS/3vErw3PgozIK8ihfSIRodSyWFeZ/2W5tae/ZBy5qjaa9nkAzY02k9HdE4ux0frjRRoFO9K+ZzV1XaC6QuC67AD1vl1CZZ1Ukc0VZguZhjszXQ9SWBa7J76BOyIs2ikfrrnjfkpinPKnHUFZ3fnkdrrW7ppUpnzSZd7qepx/YmwPayu3ZL9hhPRiFJxpi+OowIug3HR7pLNNISLnCLjZqtaKPEjPIXiVmZYCwtW0cIpZMlhEcVAxf3wmiBoTtlv5OukS2I4ylL8W2tNUJzboJRerE72Snd7LpYr8Wo6qq1mGeKEF/Qi82u+tV010GyKzME6k5HuHAR5krES5MpqkugVsBsryeuuYi0CaYVF2stM+LVIerx1CJRFV+GY7pi/L6FmDGrd7KWeswRUJFznRw1DIAMRQm6R8dzdm0caRM3UbZFW1slstarRkx5QBWpLnxX4e02ML08xsaRfPE9ld2bhK/NdkbLzk2c4wPiKGVAUnl2zLj7VUYI9FxXwSlrYlpQeDS6yFoLDrRlOI0Wdlt3Tpz3OSmFOUtyUhlboiVIpURpZruGnF8TzxRnrNKljxmhH0mELxjTdW9OaM7v5fFh4XuecuAUEfV7IRfkfsQw8zZxsrFbxTa3JmW1aJY5qBjG6bb8PrbsTe4kOVFLWd6aSg6M3McxjC7RUiDBNlWvBdFiXJJzeRV4cjueSCFjXVmyTsXmak8muXK8cHDnXl+s0h5NEgoIYWlc91XDyiu+BdIY7hgz16nZkMeieTu71mSubFxDGKe5MTd5gWN4jeYO5ZLhXNlZsBYIHBEsRGFlwy7jR3EYGQldZVldz6R4DghXXS06M23GU4J1QvK46jly4lLq9YJlnBzIy3Vn1MvNMbwAfLf10xOQs7i3rgenmU4OM2UhK4zvc+aM4jxOPW5cLtp7OtA2C2sv+sl2qRxRkpqHICesuTJCEwNL6vVuJrNitzhgsjfxIvswVhnCw3B63ViZ4tYnuW+dHTYVmLOx5vArLbPzSZXkfijVEJ49EjQZ7zezRZTtuu2qDcilEjCCAnfc24WvER0/x30F+O5iyjCzw2YPaGK8yZcddhActXbLOkgYsl1Peosqm1WK+lFwWbRmVYZnqWz1WTsbjziwnwf0zJxQ+Qo0ppspgbKXK2q0LfOxfTy4Wc6AkxoJRVbwJcFBenpkyDkHuF3ppVfdRfmFhZ5YY9kQPRo1bU2PNy223wdo2F27kbmIDzK9xNQWkyOaJickuumcfY6XST3ydKyNdtcdnvruuLkysp/LPq73PFsyy5SJa3+/4SJOo2Z4OD+LM22MG6QHuc+VXGF2QCtifyjLbNMq61HJmuhCxxadvQ8mpnnpOlaeRyJdm4vSBRea7Xs00dryelhTMbDLPV92QRBqQrueCrlH+NPpTjm5K6tMqZXLuOPJXNJEg+bZMDlv/AmzNusst0abJbfo4LaC3I+WV3ybVaK/KDB/WWtmaPpradtBSYkrahffnmY7dkuL5xbftatYX0jZTl+F2fiwO0mrGDvTunBw233ljLjxeRRvmMy+TlFIrlV/avnJYQ4YwTxW4a5MMEFl5eOBobyg6VG4gUBFVRO14IB3h1C9NJdxRes+XUzPMrVqaabI6nY5FWSacmfXgKf6WrpWM9Xg04iaz3dxscTQbnnB1SUpVJlro4trQuE9uaPV7uRBj+qUZxf0Dp2igQjpw3wdTKdPz0+309+nVxxjcfb5aTgveLz1/2uvjINrVLw9ZJEMNXl++r97m3l/s/h+Jng7AgC293pb/fWvqPnr81PpRlCl+2vmKmmCxyvM//LO9vM/f5M8zO/vR9jD8eWlfj80qe3g9qo7yrymqsv+rcqT5vaiGzq7qYb/xlK9PQ4cnm6GpcVwevGxJLy2vTTKIii9fKvzt/sJwHA/yoZzOQCx5+Nn8DgceH7yehi5yK3eSJp6A2UxmPs4oRre8A5HVE+//yeGh15AqicAAA== -->
