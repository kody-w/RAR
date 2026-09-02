---
name: "rar-cowork-cookbook-bulk-update-plan-fixed-assets"
description: "Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_fixed_assets", "rar_sha256": "729154de8bf949e7665a0d8a75d52c717f5f49bebb3afe8e0832a281b11e5b38", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-fixed-assets:777b8d76d974e97d8a5eb1b8e84a2bc3f68c258c13988866a1312e9f10115380", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_fixed_assets_agent.py` is
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

Plan fixed assets Bulk Field Update — Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 729154de8bf949e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_fixed_assets_agent.py` first:

```bash
python3 bulk_update_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_fixed_assets_agent.py   # or on stdin
python3 bulk_update_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Bulk Field Update — Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Plan fixed assets Bulk Field Update',
    "description": 'Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cef2d87410fdc42f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePlanFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanFixedAssets'
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
    print(BulkUpdatePlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjVpbvV2Fy/rA9ykoJsWdHRzxACCEkkBAghKsjzb6IfRX4+bu/i5SZVR7bPd0RE/GUUZkC7tnP+Z1zL/Xrk9U2YV49vT6dPCuDeCtJotCrICtzITbv8+oK/uRXG/yDnDxrqshum7yqn56fXK92qqhoojwD5HRRJJFXQxZkt8kV8iMvcaG2cK3GgyynyusaKhIgwY9ungtZde01NVR5Tl65NeRXeQpEQlFWtA2URHXzDPVRE0JuNXyp2gwqKq+LvB6yPT+vPKBJmkbNC1DCu1lpkXj10+vP/3h+isD3p9dfn5wECABKMUAV7a7DAcheT6Lpu2RACW4EYEkxAPszcF14FeCdgluu50PvVz/WXuI/Q//1X9feqoL6p9evGfT++fo0/ShAuSb0oCa36gYY5liFZUdJ1AwvEJ301jAZ2bRVNnmmBu7LgpcH5TdOeQH9fXr240PIS+A1P359yoEK1uTcr08/QXkF5AFHgO8vE5fix59ekrz3qh9/+sanbu3Yc5qJGdD65e39+p0tWPhtaeTfpf4dcH2E0fa+Pn1n3PR56D3ZCSifXuI8yn58MC6qvPMyK3O8H3/6K7ZO6DnXKZL/Et+fH4xDz3KBTe+K//R8d/I/oNm7QZ88/1rslGP/jiVg+Ye4Z+jdUX/F++7//8Y6iTKQ9B8e/1N2f0Yw+zv081/a9s8IniH/69PKS6IOZIedeK/Qr2+nA8f+/IP77eYP//gNsP4f2ZzytnLuHN5SK4t8r27e3n7+ob7f/uEfP//QFiDXPCt9a6vkz3j+mV/vcn7nwfdVP/6eFsjXsmuW9xn0menQr3nxH9VvL5BuJZH77X79Cn1fL9NnBk1GfAh9uOC7mqmBrt/58aen3wA4ZMCa1rk/BlX+n/8J7aMJmHK/gU5ODoAHBLiJUm9SXg2jGlLfi/qXkyjsdi+p+wsE7k7lDiDCapMG4isrSgA65VPEJwtyH/rl/zh34PzivAPnfELEtwcW3lPk7Q6Cbw8Q/OUFUkMgM6+iIMqsBFLowwGyAi9rJmn3vKjb9Es3CQTKRA/AUVhhApu6Tby/Qb/8Uwlvd2YvxTCp/zUD8bBAkFyo8dIir6wqSgYAyBNyD433BSAqwJAqTxLbcq7Q9KstXiafnEMve/eUA8Dau3lOC9A9yR2gtR8BFH4Gwa7zpAN4OPmvvkZJArkRgHnQM4Z7UwE+fp2Y/fLLL7ZVh1+zBwAj0KOZ1HOw4FNh6MsXgPx+EgVh8zXznDCHfvj1tx+g/wv9M6o780nGAdh/dxZI4gTanmQJAhXZpmBZDU3pAODmHrFff3tEYdIuA90P1FHkT92smSLzXfgnCx6h+YgLsHlS0aveJf3eb1AfAr9AUQO8BWq7fv6aTSxysLTqo9r7cOKD+OH6j0A/5Ewxqd99COJ075TT2nvmTcGcOugLJPjQp6eAuSCuzRTRMK8bkKyFl7le5gyA0mq+hTDLG6gG9VL7wzPU1sDUifMvNmA9OScFoGQ1v0B79gD6W56AX5OD7uIBdZ5FU+DfM/VxGzCpfgA5xnyweIEkD3gTKqzKKsLKqr37Ot96ZAToax/0gLkFZaDHT03cm2J0r+R75h3+MDlMnR1a34eMR4OHvrbLBYxC/z/mkElFmucVjqdVbgVxkqpcHvk0jUyTeY8pC0wFEKB7FMe3SeEDVD7g9muWRCAG1fC3x0r/nkKPNQ8Iayugu0Ird/5TMVd3vkAVSJgiW1V3F3zNPnD9GfgDhKGeIArU63Wq/vxT4PT0Q9MQFOV0/a3Hv3tnyn2QvVDR2knkQL7nufdEb8JqKqN394Os8KaSAnnvhL+zCgLcQcQBfwgoEQGvA+y/u04C5QDmoof3P5dHU1iAFm7rAG1BvXgv0HlKXxCHGgQAjD/TGuCFH+6soNQDPgYqfnq4Dq3iocw0xr4raE2xyNMpHb6LwPtDkIpTAwHyPusMcLVA8gBf9iAIoIxuj8h+6vkeK6BsOuX8nej34X63Ffq+Af1tqjWg4zecB5P31Lu/cw4A6Cqt75gDuuq1BtWceu8JBDLh3qZfHp320co/dXn9w+z+47833t97p/b7yL1CYdMU9et8/uhvH+3tBVTBHORIVHj1vdV9eZTbl6nOvtzr7Mujzn7H9OGjV+jfU+x3LN4z+hWCXxYvi+nRLnK8KWXfP8AP7Bfm8gWdnn7NFO9bgN+zYIIwAKv28NlJPpaAdhJUXjAtfnSWempIPeiBd0C7d4bPJHgvEYCXWTC1wTr/rnQnm6aQPiL2CbzgUTZBujuNbYE37WaSSf3ae3rN2iR5fsqs1PsfdjETroIUBY6Y9j2gXMAE1ETe/epzGpoufr9buxcSQAA3f53q6fmOic/Q5xD6DH1sC+6brKwF+6KfpwF4EgmWgj+faz+3grb3BPZgzVBMSj/2OtPc9T4P/1GJqYyAxo43den8sy4niX9gAr4EgVf9kYl8/2Il7+BQN9bU+UDDfS/pGujpgiHpGQJhA6UGqgeAYgsI/igGyKm8sgW91p3M/ea/b2blD1t+u7uheWwYf336AInp+6PxP1IGEPxrk9nkz4+O+jZxtSba+/x0d+992nwDpkVT5/zuUTCNAW+P9Ht6BfDiPT9NTqwiMEKP933x00MVYMO3ORVwAEDxpZ4mgTmoHsAJ9Odi0v8KQO47AdPtyL2vn768/ulw+5cV/0oQhE26BO5SBOpRhEtamGfDNumRqLW0HcTHSWeJkQ6MUCRJ4rgFI/DSo3x4AcMYQk6KTRFMrXcN5vDke6D7p4P/vWn76UEMWsMSwwE1saRgDHU90vYplPIIHMesBdCSwFxs6RAw4WM+StmebSOW75HegkSW1pKEbRj2MBshJ37vI99Do7eP8fojGo+qf3uMCkDi0rIcEnBGgUss3PGQhY04HryEXQLxFhiF+CTpoYD+k/Q9IlPAHkZPiQomETBrdZOcX98jPCUfjoKVG7QW6MeHnVO6RVwIWwptisD9oIxJckEVwzVdIqEtme5KdE16v7BUZtsMURpei22zX8o7sYwk5tBdBHqmbGe9SuwyIxH8JF6qjdCt8yvPLtkt5hnX+RgvDSekuZzyzHGvnzpYLq6SVQ55mbnGpcjSVC+8nS0UZ52r5hRZ1qh4Kfbi0F4jPiEHT4Z5zN1aVq/fTDzXonOqivAlSS/xXozHvMS4Il3AnOvh57xdIByxk0N3XVr4og2t27koTpGj1FKViwouqxg5P4wY7ncrhDgVA+Vl3cw/xaCbXtEKVjxWTwwLPpRW1PanRKlsTYvYW1bFWyI8o8bWPfOVVmeSKEk30emay+jeSvWgq3uek8us5PLSz7Bh9MRk1O3tBWfXns4wTpKNs4Vmp16Z5ex665Tutryi3X67dS+GmSzlW9FQ69uuxe1OOaetzhKjssl2PWsX7H5eyZK8PbOlfotFLOTw43W3Mx1sX11MO/LKpUo5GMawJ+OMCU0usHzjwPCqkKl9HPpdJiztwa2cwF6qs5rzSkwvtd0N0Ysz3VjIftOkwH45jqn0eBbji9QsYKY6V6kRSqtNsrXqdPCx9NhvjvVYShVz2oczr9BQcRHG0fa85WMLDiiV0giMTM6HGemIu5TBTdh2G6RS0Vgfk0XfIgvy0iDXqBz3SE0OvCPfMk3nCqeUtpoUx/PxFFWGKTJkR+6GYliojHUVSfQya4RMulldlBek6dy6IIsbNA8PzGiL6/CAXdCME+Qdou1rTF3yK3GO+IZuiENVVqtxeRrD8JL462HnmWggGKeAyOcnq61PlnY1JdmS0115wPcFjGHtDinds4GKErILcX5FChse9NYtWkaL+YxZaXimEjMfADGzsLMSkXO3IjPvfFt3oQaLhq4s4euwxfhCL0NdipuAkKJhyfLC/gLvh7kVwp02W5ssMia2oM7Ek5EbR4cslXHNDA6GX07rq4SFFqyuDK6SVzSdCMuo3IOcY7aH234prMLNxRSWAdteIpHXFXWduryGOqp0Q3exI+azfZfpchrr/oXDNqPCnbxICtSrf+CW4nwpRUcmJiNx9CXtjI+mkiOLFbky3TIZsE6J5re5sMTj6JIPi9kGVuBy6LB9EVGOdpH1+QqhOiEtB1Axi+wSjsY6Zir7qASnjp4fnMNG1Xls4doktdbSA+Xh+nqdCJXY1P5NwzDVFxt9ts5gXzjuqFV7PVONt419Am9IMtIVOw51p+79QRdtd9FIuKV3vG8tkn6d6Bbpb7a77CxvySWnVRwuJTtsbcL9Qi07bc8iB2GzwzdZv9UMd7c1z9sB1el4DgtzHq+OXjiTOIO99fJZX1Hsxok2ThmFG4sInZGgYj7jsN2KpRp6XW2zgoh0w8GicHbVUpNxjpUK/u5N+FYxzE7ZnwiY6w1t2xNXHtMXbKsxOXnLDghmwWmmxHaGX7Wll2eno0WQVLVPheOhd1M41XluRjKjj0e3GFdGL9cruzZOx1nrH2b8BlVPzNJAAnkbroYQ1a4WamGwztdHas+hg3TYzQOaOsFrB03MfmmnF4DU2kWoKRPDLElgMVklDZXotSWqKbK6rxSy262XGL3V1jLX6sxBNbEGQ4NxwR6DkNYSUXWFOCNX9rYsx3R7xVzBD/Fjr/D9sj/79qXpzxbndHyG0ptGFIXsOPRixa3XXbR3iKhvObbYHoVlPEoJvSh6sx377BBnrXvm1rsNseJ26LrAkG3pElm4WKdOmjVr04Rnc3kFE5Rn7RVByHirucHtwr8u8kHsMhnjrXE7W9OKxIcmiZAk6+zQXdXIxgXkXbyCD1tlVhtZNmJkzQ2qeiMb31qhisbvmt04GI4W0vqJ3ZwSKncWY6ona1SMjBOGaLzGNF0+u6ba0bSPQhsk5kgei+uale02EjOlVLEl50QB05jFMjmzRKEGMq4dJZ+RozWpM+VqLrIieliT5yIpgpm3Q66ncrPx9+l4Phg7W6I6qevP+LUVrlbOzDu6FtEUXjfsAlerTlzIeidYV3jFIAq66hk6Es5bQjTkfVxtRjVidPKWjqLOxjzPpwKFUBGmpGqDXUh2xy9HYX0Z9uxJXnnysWCvyHp9ybTOnXvNTb5tyd3IMxa76I4z9tgJ/KrrtnBvCn2bwZiZJcjWlLQNzvkSehZp1qfiy3GAxa22UXqaYdxrYauKxCXR4QrquEQYwVFpulSV5c6aK6awgTn1vMpbq8lnm0bab7nC6GElVk9r+aia1sieAsFnVqS2uzpXXKVMb9PurHwfaHIg3fz1QS9VM4IL1kiNSKX5gY3Os97nJLRTQWc78UrsxvRptitVdVhaNybenprUDHdOZCLNuOglJpNH67y3OLDD9C9JQzjGFRfPaXk2TdaN5rB7Lk7CmLjx0Tp6kQOPBY+NIRzDmtCdkv35kmaUHHFZ3mvHss1vXL3wzYQ9z+M9vYoPQ7iV6EUzxG1wHteddnL1k7LleARNIwFvh60ycGUMF5pfoumimQNFhD3J4rg9p3rF9jLk1KB8fA1KZwiYEu3kOmLIZbjH0+agcOkKQZARk5GukLIbFyuddnACxT5TSC7ExeLsNrtKa/dNkoHKdncNtal4Ix8ctTwjhI7aIrXihatNlwkG72wyaAVN5FZ23tjXqrnmGO/1h6uZcwO8Cvtks8A60F9Vrb7AKZvHZxreqUYidnuE6YMs4prLBRbXhuJkpxxFkuVGEHV8cWwGFVkShljuZ20lFkphjGc/YGP60mdOU42qsK6X3OK2UctTcIQHheoD0bCjkt0c9qOGOzUqHK3wuNueto5/ElyNHHx4FWeFU7S4427N9mhcx+GcdAjLo940jOmL8ZgLzsJuBrS8KDNtvzXk3pG56lgHQXRJdqp/snaHYzCXxXHE02N5GfHjKveW3pJjZHe/xwp+bQI8GQ62Ru4W4nxVsQqMDLW92N7Oa9rKLos2XUfWoqzg6ARbjWPWaFo3+kWmMsTS4MDAo7Q70ZtjXG+6cdsZWuvyqlMjhw40fFvUUsyhbAaebyVRjHMPxZeqGrqyaqq92mGaJC9sO2ISrKUwWqISRVP3t5OwnKZS9qDGLLO8RtKeKGSRGeqQj1KhTQctdep1L2Xs5rhZei5lwhnvwBtC8SkhOtlmCmoLVXi3bA6o35UUtkUOlqBze4Pj1QSHt0bC2oIpnfk5raBZeqQdlVmdA4ynA+VYtOzeqq/xkCeyuHOF6OYUuo0kSeiiLGFsnSiSjwh/IlBdtpvqcrzIm9EMRB0Z5sVmj164HZ9oycmegXxgNt1c33ridUMTN3k56tYMw+h2h9Uk5XDrBnYsQVOL41FrimR7tRB6pF25nfkoF8/5vS/nKsG2R95doZiOpdLsSrpII5XcyMSHFXpOTV2UCNBmS2KxdmnqiDUVp5+vF90dSh/0GbV3Ud48u9w6xbeEenX0lm6TagZmVNA3cVFWb/gZ0zfXlTbr+82OuV3EUehviVCnAmfetNysYz51EiO54kS2nEVhWY98QI/HfVv6bMvW6IEmTsPRpWsWEyKMTRWbGenZ4iQuxFM1Nhv2YqWHTXwW+HR2MdfnxNc0TkIuC9nwc1IA28i+UvtSbOEup3nASHBWOrVI7BXWWilO9BtG3VxlfLbC7MLIujbxjCEz24NiuAZult5ZwtykctUt0a0CuGzmguHdZCK4VM2AUUxeE8JCgsc1L0anELHT3tp7RSrt3GzJI0xxoHiD7p1SGahRQzZ6dDC8g2ZfEc+MwvVWBC2l4AjUbJHoHIQ+K1i07NG6kVIzY3lEKGWm9ItLvOpyBD5kSCL2OzytVll7mqcRLO9WCnHk7BnVDgk/585BfcjcxPbcem0KSKGQfqjmLLGUagluZQWbpfO5n+/m+RY19bCYu8785lKenLWdNzcp77Lwhs4+pde42aq0bLtbBZW9KOozFCDGrBVB2eM8wBGBuRCz01lbHmnRcWWPC4uQYrAVj0k9yOH5NnOME1kv+g5xKizLa6benM2W2gB+nKyWS12V10d3wDtPI7FbAp9GYXnc111ADNFMIofTrr/QnR02s3y32JDrHlkaxx0vLoymj8hNZto6GfoLakhw7aYLYny4bny/jnE72G+Oo3kZBT/N0+SQAbBV5u05n8OwUXbzypg7e21rLg7Ggjv1K+18PGQZam9oqsFmNjJy6qXxWpgmLxFTs0u0vtW+twTjRICURWe0+9WOn59ldGm3We03ZJAu2VNMqxRSejZ9zNBoZ55W3EojOLUUjVgnuEumbsjGleZ9wDAzqz9sFnYUNpGm422WBTNmltEefzkqI6ql8p5d1uoKydc3LsNu2Ol2g5HNMvAlutdzvkKTxFuvD34Z+CDzFyJ9W1HopjyKg4kcTOIyoAchDoKRMYO4ZDJ3MC+yxIT7Y6/D1czXOBjmEUE5zMlIBt3XzLd+uOv4pvUIluCOEpoiDrXd7VVnPLMA1910dnSz+HA+s6RUJZxPrG+pMDc4j5CqzDyrfsvdXDYT5ao/KvMGnd1QlL+FAUE6vDCed8FerVqD2Azq/kxScLOwjrskqOUht7DMZuxF6yV+MsaqG7t4u1ZS3utcY8U5hoxuvFWICmRv0UF2wJEjT3kzTI7pKPDp23wf53Mr15wNOveuQ0wUWcHsBpQMkQuBsLTHSZXLD4Hj83OTaDvcs9t6jhA5khmSiFxvEQ22q5t5oR1kGqmI/nwD3JuKOhw7v0zYsS154oDgCZri6CaT7HrWIehuTpqahiYHR0L2ZoXrjnasbUEmBU0BxcuXLS6Pu3mKlivNPh94FnYdzCUZ4+ZHKimpxwNTsCvY9Tdg3+2Aeb5cYKUdL1ZGdjIuTUNZ9s3YVePaY2Eph4XrcBt7Cd9I1Y1Wj5fNSRP2iCRlu2yTK0vTaovmOOC213QHo6nakysfbueCPjMFTy0OLUkdt4S86UltfbM1GM2IcTXSfN8zBrtAz8ueGb1YjEVmVkkFb9JmT4hbeg/2iq10OlJiW8jwZjXuDsot441RR4z1spdm8xl9QncyrqMbIpAYKrouOoM8Cz4W2sgZWyXUcky2t17qVX4+0om7zANdwm301CcsdZqZuK0QduusRjk1aJJk2jpj8mpvJExYtIEQXkTPn9eM73KRq2BrhO9mMtrGbYplcc1liZvX2a5MZWVOMptmz8uRU9A0/fen56f769mnV3iBIdjz03Tc/35o/y+f+wZjVLy9s0GIJeDyv3c4+Tgo/HiRdz/C9yz39S799V/U8B/PT5UTAW0ex8R10gbvh5H/7eD1yz89CZ5Ih8dL5elN4635eMnRWMH9lDrK3LZuquGtzpP2fkYNvNvW038nqd/eXxM83c1Ji+b+7FN9cGU593P7tyZ/c6O6yOvpZpRNb9A8N3qsmS6D9xP95yd3AJGKnPoNwbE3ryomQ99fKE2ntNMbpaff/h9LW5oHICcAAA== -->
