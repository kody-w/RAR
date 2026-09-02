---
name: "rar-cowork-cookbook-bulk-update-develop-project-approval-processes"
description: "Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_project_approval_processes", "rar_sha256": "d8d26ca8ede4c587129003026c05d28be52c78c9eeca92e79f700c7e2680f5fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_project_approval_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-project-approval-processes:adb9cc6dc19d00db9907d229ba0223540ab0eddad416d612e943ddd4df9464ea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_project_approval_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_project_approval_processes_agent.py` is
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

Develop project approval processes Bulk Field Update — Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 d8d26ca8ede4c587…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_project_approval_processes_agent.py` first:

```bash
python3 bulk_update_develop_project_approval_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_project_approval_processes_agent.py   # or on stdin
python3 bulk_update_develop_project_approval_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project approval processes Bulk Field Update — Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_project_approval_processes',
    "version": '2.0.0',
    "display_name": 'Develop project approval processes Bulk Field Update',
    "description": 'Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-project-approval-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b371396b4d942e03',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-approval-processes'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-develop-project-approval-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDevelopProjectApprovalProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopProjectApprovalProcesses'
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
    print(BulkUpdateDevelopProjectApprovalProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejxprmX2GyP5Tdykr2RXmPzxkQAi1IQqxCLp8slkAgVrEIIbf/+wSSMquq7dvdvjMfhjqZyRLx7ssTEfX7k9s2UVE9vT7pwM0R2U3TOAIV4uYBMim6okrgnyLx4A/iF3lTxV7bFFX99PwUgNqv4rKJixxO58syjUGNuIjXpgkSxiANkLYM3AYgrl8VdY0E4AzSokTKqjgCv0HcEt6d3XR44YO6hrMr4BdVUCNhVWRQBiTOy7ZB0rhunpEubiIkqPrPVZvDKeAcgw7xQFhUAIqWZXHzAqUCFzcrU1A/vf762/NTDO+fXn9/8lO3hq+eBCibeRNKvAuj3mXhH6Ko75JASqmbH+CUsocGyuFzCSrIK4OvAhAij6efapCGz8i//3vSudWh/vn1S448ri9Pwz8NCttEAGkKt25AgPhu6XpxGjf9C8KnndsPSjdtlQ+mq6F988PLfeY3StBmvwzffrozeTmA5qcvTwUUwR2s/+XpZ6SoID9oGHj/MlApf/r5JS06UP308zc6devdDA+JQalf3h7PD7Jw4LehcXjj+gukevezB748fafccN3lHvSEM59ejkWc/3QnPBgT5G7ug59+/mdk/Qj4yeDZ/xHdX++EI+AGUKeH4D8/34z8GzJ6KPRB85+zLaFb/44mcPg7u2fkYah/Rvtm//9EOo1zGNfvFv9Lcn81YfQL8us/1e2/mvCMhF+eRJDGZxgdXgpekd/fdHU6+fVT8O3lp9/+gKT/WzJ60Vb+jcJb5uZxCOrm7e3XT/Xt9afffv3UljDWgJu9tVX6VzT/yq43Pj9Y8DHqpx/nQv5mnuRFlyMfkY78XpT/q/rjBbHcNA6+va9fke/zZbhGyKDEO9O7Cb7LmRrK+p0df376AxaLHGrT+rfPMMv/7d+QVTxUriJsEN0vYCGCDm7iDAzCG1FcI8Yjqb/qy7mivGTBVwS+HdIdlgi3TRtErtw4fa94gwZFiHz93/6tsn72H5UVHUrm271Yvj2q5Ntjztt7lXz7qJJfXxAjgkIUVXyIc1g/NV5VEfcA8mZgfwuUus0+nwcJoHTxvQJpk/lQfeo2Bf9Avv49lm836i9lPyj4JYcec6EbA6QBWVlUbhWnPeLein/fgM+wBsMqUxVp6rl+ggy/2vJlsJodgfxhSx+Wd3ABfgsbRFr4UI0whnX7GYZDXaRnWDEHC9dJnKZIEMPGANtOf+tL0AuvA7GvX796bh19ye8lmkTu/ahG4YAPgZHPn2GvCNP4EDVfcuBHBfLp9z8+If+B/FezbsQHHirsGzfrwTBPkYW+WSMwZ9sMDquRIWBgQbr59Pc/7m4ZpMthA4WZFodDQ2wGV30XIIMGd1+9OwrqPIgIqgenH+2GdBG0CxI30Fow++vnL/lAooBDqy6uwbsR75Pvpn/3/J3P4JP6YUPop1tvHcbeYnNw5tBzX5B5iHxYCqoL/doMHo2KuoHhXII8ALnfw5lu882FedEgNcyoOuyfkbaGqg6Uv3qQ9GCcDJYtt/mKrCYq7IBFCn8NBrqxh7OLPB4c/wjd+2tIpPoEY0x4J/GCrGF8VkjpVm4ZVW4NbuNC9x4RsPO9z4fEXSSHqGBo+2Dw0S3Xb5En/vfgYwAHiHQDLneMgHxpCQynkP8vsM2gBC/L2lTmjamITNeG5twjbsBlgwHuUA4iCwTOu6fPN7TxXpjeS/aXPI2hl6r+H/eR4S3I7mPuZbCtYARpvHajP6R7daMLRUHmg++r6maTL/l7b3iGBoKOqocyBzM6GepD8cFw+PouaQTTdnj+hhMe1hmyA8Y3UrZeGvtICEBwS4UmqoZEe/gDxg0Ykg5mhh/9oBUCqcOYgPQRKEQMAxj2j5vp1jBhILa6W/9jeDy4BUoRtD6UFmYUeEHsIcChH2roAAihhjHQCp9upJAMQBtDET8sXEdueRdmwMoPAd3BF0U2xMd3Hnh8hME6NCHI7yMTIVUXRhO0ZQedABPtcvfsh5wPX0FhsyErbpN+dPdDV+T7JvaPIRuhjN9aA4T3Q///zjiwhFdZfatKsDMnNcz3DDwCCEbCrdW/3Lv1HQ58yPL6pwXCT39vDXHrv+aPnntFoqYp61cUvffI9xb5ArMAhTESl6C+tcvP9/z7/Ei8z4/E+/yeeJ8/Eu8HLnejvSJ/T9IfSDxC/BXBX7AXbPikxD4YYvhxQcNMPgvOZ2r4+iXXwDePP8JiqHqwEnv9R/N5HwI70KECh2HwvRnVQw/rYNu81cBbM/mIikfOwBKbH4bOWRff5fKg0+Djuws/ajX8lA9dIBiw4AEMS6Z0EL8GT695m6bPT7mbgb+5VBpKM4xhaJhhsQW/Q5jVxOD29AG5hocf14y3TIMlIiheh4SDbRDC42fkA+k+I+9rj9vKLm/h4uvXAWUPLOFQ+Odj7MeC1ANPcOHX9OWgxH1BNYC7B+j+sxBDnj1iZZDlPXEHjn8iAm8OB1D9mcjmduOmj+pRN+7QPGHPfuR8DeUMIPB6RqAtYS7C9IJVs4UT/swG8qnAqYXtOhjU/Wa/b2oVd13+uJmhua9Kf396ryLD/R073EMITvgX0d5g4Pcu/TawcQdiN0x2s/cN475BXeOhG3/36TBAi7d7fD69woIEnp8Gq1YxBO7X2+r86S4bVOobOoYUYGn5XA/oAoXpBSnBnl8OCiWwLH7HYHgdB7fxw83rX0Lq/3mNeHUDb+z7TODj4wDD4MMYYwOCGHsuRhAkTWGuh4EgcAMKZwIGJ8CYIoMgoIJwTDEUcKFIg48z9yESig/egcp8uOD/EvQ/3anBdkPQzLAHwQUE47scCADl0xyLE2MMIzH4DqMDgvMATfgs548B8N0xAdhxyGKYzwKC4bCQDgeB34HmXcS3d1D/7q974Xi7ww/IkXBdn/NZnArGrMv4gMQ80gc4gQcsCTB6TIYcByg4/2Pqw2eDS+9WGGIbohuI8M4Dn98fMTDEK0PBkTOqnvP3a4KOLZchWE+LvFHFAGe/Q+devluUQSOloR0f23XCX7WSWmqetGR5sc60tbiTHCNLJBePCh7VFqPeYGfhRpyMYmkDelvmvVbZrTY7Nbsq6YjGBWHK9+Akt1aWXpMoTKWLa283Bh309BZcVqW793fHZYXpBmstp6g0zutIj43xaIQTPp1np1ovJW1TK7sT6rdFpzgMPifrEWsq03Ia13ZkJUq2zQLaMkszI5UkOBZ+bOvOsW5Ph4uHK5YtX+Qy0jMzXuFM5Z8Xzkxk2HUujTzVWI8C9aLmyvrio0ate5KO56Vfdk5qt8ZyplQ+35oug0nebLV3NQMULqpHwq7VMWURANGaAklRXHW2kSYlU2S8ObVS3I6muXQB9awufdrs7C6KyAgcckmrp3PZpfMycueVPpObyalZL9K5sSMk0t1XR1exbb/fNfGZylA3Wu2rWZ8V0iY5yMDC5ZPDSttlkSYhb++7iRRtiG1mcvP6ArstNd5twu2WkvBzrOgTXjlLVYJJqdKRbdoTwTVqYsP3+JGZWFuOsZaNNkWViV46IqEEOsgOpEappbiPDXtSlWuhwGPWrDIjWhg7RSqSs3bG2602c0mjTxcC2MVgM5HmbjUxfIGiialY2a4CNklNcHl+3K4OuLVBV3XWgBBT66B1J0RLHHm/zlJGS5uccftDLHuGGeupXSt64u4JbWedris7T2HXttaWv13akRqvd+NaWGSLFbfeqYaaLesFSrUxfjjUaHeZuqNsswm1eQ+W0+NpaXeXkUijLtPss4WVVllguP7Fo67j8yHnwu1JxZSsN6kTWTstVm9Hl+HH1/CY6r1pW/hU6JPTC5fvaSAGQPdaY0Sv2WyW2hes8tMQFbGClq/oyA+7VDr4u1NlX8edthaaeOlOmnq3iblmvXEXC0PZu7KtCX3fgi4huWVVOxex11zxEgWct9pWmU5YM1+a5/tJytBCmQPrwOndtfQEp08KP7fjzuaWMe8p4Zy/Vg6Pi76+aIVcX3QrpwJS0k2xqRA59D6fpO1sfvVB7O0mp7Po0b11qew9IerRCiMLQ1szGKXjrq/I66mqXuPW2ojUoQk8dUqQV0tmxVEVqX1grpWRabI1Sp+5I2js60Yxs/pIqiuQc2V6cVmFCufyxfL3QuMm+B7DgTQXl+pynlqePWqDvJ0dNzEauNnqcuZEeXkgNOVqGMz8okfTE7ZglmiKCvsQm/SRI2HeajPboRhuTc1RPmtpp+HPhienGbkj1jMFtZN8GctyKQUjgEuLFLIzpE2106NwGcUntjycNzKhZpM46WNCmoCI5rYkxRxdw6q30PqL9WiRUvjCNuPw7OGLpMOok8fJu/2MFyyaBynhMlOS1Veb7Vw39qwjK5zhGTlWE/FxNgGrixODEZ+1pcn519NR9yfQpctwO1kHrSRP/Tya+RGN9od+K1DoyS3wZRT4sGIYZR8H9aJtp+NdhF3VcEtvrcRaRrMwIQGT2cdRZLh1yoYttZ/1Wzys05FirEJ00hknhia5BDcWmq5UwcYjTVtlhY0qbvvLYVot9GO8Ett9YEXGHG1PcysC3MR0e15VN0ZtHEnO3My3R9VwFqPxRqEJLjsqykmvx4Uj930gtuKiWypzx3KoBR0fQ5FeE6UiaoRz1C9BWPNpb82is2exxMmL1/2Rd/YHN4JdYb3silBLknp8TOxuoVwPxmSxpbslEG17Pz9tmKlprjmrjC6EoSTTpC/jKV4mzclSvfXmOtPWajHWpiZbVeP1Od+P/POO5gyd4i/Odde2Zwyrav2YyuP1vtmzM56hZAln7GathpU09zw/6EZUJuYeF5EjFkXFqmLm54QZoeFSbNVQ31BHXzL0KsvtsRIc8kQBscZHV11d2KW1347G9jKi+lIiynNDj0uzOBo7MQompzKlJr6upDvLSlJJTPJroWrTxWwml7FbLnpik9CGnO73IVga3qQrj7p4ShN8IxlZJakjFQa0ZdsdYRjh+RrVpdE245U6WXU0Qfv+8nSpLjOeTLuLF+dLz0d7bO3WCzrt7SWLmsmIPq4626HyoKhI3cUK/BwdYR8a78XqWMaTGS5V8+O1YaVl7tAnw0KBOLGPXuAwlSDH1UQvbN3crS8K6tWqf6y3YNKN4myeElM4ydlSYDvys5UW7rHVnF3WZzOyerMxAvSSYpIjmYuFsiSiyykzD/OQz6mJdrGJ2SrotoEPUOlUOklDO5RRm3Q4PU2VncBpi/kqcGCVlqYG5/UxKLnCtCITN9T5RCO3oico3cqfnECMa7btXXtU4HnhbJ7wPt0yo7bXq62GXQrZ8HeVLCWlrKbElQV5RlsLZhsv6pUp5NFK5LeK5nm1u7SSnlmsece+1CERnILLkTjaZ2uqNBTtNnjRj2Rb57BkX0pLV0S11MnnhRwSnHTgl86VbNuu2KrYzOHjsViQmp4AjFkb4LjY+ks4aoJuDydnaYDSOHQXdhcZhb2IjRWms07gJiW2bTQhOm2Xfqcq89POFwaIdVyUWNiwBnbEDpnGz+YGixISXTP+ek6UxUbwaVafT0KBlnGVIBorN8uGNqaEDeJZSDMjbreSjtUpWUaGM7PjIgT+gh5H5WkKgvyYu05bk1bv7Y/HwGgypdhPTpx3Bq5byJl8pCYH1e1nJj/v63rL+xcmN1CSkZzyQqnNXJsbzqVZUvZ2e85pPEy8AEt5eztr8MPp5IVOaQnFtA321FFZymuztbDdHivkNbXeXwR9BsZShgmGoKTb5W5Hl9saV05jlddPh5VyPOspXVGiG0frWYRR+RxC+Wnob1cSRZnGgWVwabtYXeFqI17PVut5IbTy1lWZhIzn2c6+Gt5cSKyMEondWqD0ke+Usa+tL3McdXjAhCbs1Iui1DamsayI877okkSP+GatLzBMWAnS2GRSfK7otBlVJbclnKumj7kDFVd1TgSdFqfc5DRHizpb26U3ynue6C40hK/JJbF2s3W+vID9cYHLpbw+r6vLOWky/WzTp3NtrqJR4nPpbl/g0clXj9cCeH0S0yDmlXbn4h3uaJZ2YmZZ4F1oQt6xtspN85GVGMRsB7LV2bwueuNcxDpHHzstoufq8bA9yVo344GS5KlYbhd4snBMTRpPJ5HUtTnP+gtLnO3h6mhmaO41L8czkYhNqU329YqcJzaLaqAL1xkdGzUIs7IYQ6RORjpTTgRhtjzLlBnO6VxeSjzF60Et7AQR7dutb3SkrIkzbWWath5OuWJ/Igl1LlfMNLN4muZM3d/nbZvAycGYL6mjIF8nO7XNtzJPXeYQKG9OpG1Ni2tc4+h82ZsFGzadZy8trb/qmm0GZcDQjrrXO8osNkvoS0ufe7w5XzCiKznjlhOOar90RucFxRMHsYEVK24PbJYZTQW7w9ItDMm6zpvFaI4fSdk9euwIRmkR9UQcH42aP9ILsXCnOdZm+yQX1cS8Wp1vtgsiVbnEWTtRRyY+eexKiKvmjO7NBH81cw+LaTxhQh4rquuaang1WTFGArNxZnjo7mBIZh9gh0XH78qQNmqbFPAG5ShZD1bmfs7MXWzCBCCXBPw09xI3nR1yYkuQRSLNpr27H2kxDAh8ddAM/8S1m9TqqCzPT+ZoWcixGTR0uEvXfDzJTnLFLTfZunGMwnNTlt7NJg4aipF3NqpZK7VVJGA1M1P6Km3Q2lJL5tgAf9WUAVuTYVupk35MSmCH5tdKbxpWvkJJZxtrG+kbcrNfavsSXygOlov7w1geXbStYC+LYL6Jsqu7F3ESxbXLmqwnpVQyeiak9LiIDquQDUs11k7CituwxvJ03s1SZ+vKxvHQrTJG2eIs1Vz2y7NDN4F1PI43uVWuRGGMAUyZhn1vciCrMVIMsv0oaBiat/r5aLO41huWvJxxPFOFCyuh6Iz10IOgTNsLhhYoetmieSgS1jl0UPkkinVDdGV3YC9w+uJUFJxoFLW/AAt6NcMvyqVEt56vCSLHHUeTZjk1RDexVyM+TDRbYAzgqAcwVYgr5B2wXhkFNU1cV5dpLlh7mcaxWUslbGDrsdOdYBanbHecbYJ0WvdNIk4UasMV1yNYFfqYnewuI5v0170xmqAVLLxrdkrAdxMuzD0vCA5hT9EW4V7SOUy8dlKdme24wQTlQO4dka1O1HluJPTUYdbjazCjN6eziY6dERsVRhasfJSPXV4/6wKthkIdjEkjZ45lUQQj3GWdST+ZyF11PPQy3rBLDiVTUBVutKbCQt0E2jVlc9JfWughm/M+uro2+cG6co5N7XhtQm4E2ZtozAqU+ysfngmVObExK1A8v+bGG3JKSuJydb7i+kYdc3yw2VPapZRIAa4bdZmMwzactHyGmuTGBesAH0dqfnCW+ESitMlZrqGoJ7bBWU7m+8w7qBbvx1cwIYlregWaKPC2QwjsfBrOoFhTnFnVV7aqlT7oNqcqo8feRikVSjWyjWOjawU0HhYQOLFsvXhx3rNHozjQfcaP2GuZckyZiZ1vrYJLJWEhBXHpNdz5Abupkn0WQtja+MvNyt+F/hyd1JNKIMl0bZLU3BezMStrO9EOY5mnL/31kimNwc8mgoc3GoGLpH0txuuYnVfg5IJg3OJVsl7rey+fMm1zuYxl73JYnHcTPaaKzXiOyefLuPY6fg4X7PpY3mP+Ohmpx25XT/bW2LqO8nHEhSZbbL0Rv/ZbkrQi53z2gvPYreWaCPZjFjr6fK48/qTksxFLo407onl5fNnIu/W1mxIo2Yr+2D8t0gAj9C3J9dQo8I9e3hCsxnLpmJtkoUGHW3DlLJa5FGA7BcuNfzhxvDlaWwCbXncoSjECbElgJcB1xdTmNwQdxkanGrwoLvQdHqDq9Xp2lvP8RIBI6NxDyWQym+G7mLBtogaytKwsdtWNDGrDyEIRdeHWUfSts4Doyp5lYrEnnOWpba42VW2aZk1WZbvYMDOqMUVWNOMNk19hADrj46Lj/BlhmDi1IzkxXs1K3m6nAtWu+V3GydOpZdBb7+DgqhFdk4lfjiRxX6UWk6xXrOmfhXbcC77mCQnpyETsjdiMN3vbGi26kNy7l716BbQvkJvxWPVRmVqvzqNNdbwKpsHR+9TfQ+wuO5y97sOxzkviWGccxt2jnq2jebBqhUsHg8gQzuOtGQllKc9Lw2GsZlELQWBmQcTMSXk3PlCjs7i4hnIitmTWC6vdfgVEtBNOMyO4CnoB8eAvvzw9P90Oi59ecYyl2een4SThcR7wr28hH65x+fagS7IU8fz0/24X876j+H6KeDseAG7weuP++q+K/NvzU+XHULz7FnSdtofHNuZ/2sP9/Pd2mQda/f1UfDgIvTTvRy6Ne7hticd50NZN1b/VRdreNsShQ9p6+B8z9bugTzeFs7K5fftQ8OljH/2tKYaxYTyMiPPhfA8E8X3I8Hh4HCc8PwU99G3s128kQ7+BqhwUf5xuDfu9w/HW0x//B2TZybYjKAAA -->
