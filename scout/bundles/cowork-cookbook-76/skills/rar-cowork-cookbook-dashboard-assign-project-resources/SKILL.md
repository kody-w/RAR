---
name: "rar-cowork-cookbook-dashboard-assign-project-resources"
description: "Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_project_resources", "rar_sha256": "030716f609c613d63f5510e2544b5498669856befa96846123fffe158fb711c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_assign_project_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-assign-project-resources:4b8c53ca1f5860a032bc50a3728674569c09f93609559684d3ef9379382eca97", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_assign_project_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_assign_project_resources_agent.py` is
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

Assign project resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 030716f609c613d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_project_resources_agent.py` first:

```bash
python3 dashboard_assign_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_project_resources_agent.py   # or on stdin
python3 dashboard_assign_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign project resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_project_resources',
    "version": '2.0.0',
    "display_name": 'Assign project resources Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-assign-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a42b638f485b14e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/assign-project-resources'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-assign-project-resources', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAssignProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignProjectResources'
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
    print(DashboardAssignProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjWJLtX2FiPmTVEBlil4i2NntISAgJhBYEQpVlkSyXfV+EoKb++1wkRWRmV9d017P34SmtMoW415fj7sf9Qv32ZDa1n5VPr08HYKaIYMZx4IMSMVMHmWVtVkbwnyyy4H+InaV1GVhNnZXV0/OTAyq7DPI6yFK4fVtmTmODCjGRCsTu52GxGaTAQYK0BqVp18EFIEtVlhDHrHwrM0sHcTOoqaoCL0XyMguBXSMlqLKmHAR9RrIcpBXcD63pEKvM2gqUz0iaITzJ0Ihpw1UVkgLgQC1Wh9Q+QC4BaEH5As0DVzPJY1A9vf7y6/NTAL8/vf72ZMdQHzSXf7eBu6nf3rXv35XD/bGZenBh3kF8UnidgxKam8CfHOAij6ufBl+fkf/6r6g1S6/6+fVLijw+X56GP/smvdlVZ2ZVQzNtMzetIA7q7gXh4tbsKuhx3ZTpDTgIb+q93Hd+k5TlyN+Hez/dlbx4oP7pyxMEpzQH8L88/YxAHL88lc3w/WWQkv/080ucQSR++vmbnKqxbhD//Rahl7fH9UMsXPhtaeDetP4dSr2H2QJfnr5zbvjc7R78hDufXsIsSH+6C4axvIDUTG3w089/Jtb2gR3FQVX/W3J/uQv2gelAnx6G//x8A/lXBH049CHzz9XmMKx/xRO4/F3dM/IA6s9k3/D/B9ExLIHqA/F/Ku6fbUD/jvzyp779bxueEffLEw9iWGylacXgFfnt7bCdz3755Hz78dOvv0PR/1LM4VYLg4S3xEwDF1T129svn+4l8unXXz41Ocw1YCZvTRn/M5n/DNebnh8QfKz66ce9UP8xjdKsTZGPTEd+y/L/KH9/QTQzDpxvv1evyPf1MnxQZHDiXekdgu9qpoK2fofjz0+/Q4pIoTeNfbsNq/w//xORA7vMqsytkYOdNZCbmrQOEjAYr/pBhaiPov56WIuS9JI4XxH461DukCLMJq4RoTSD+J3bBg8yF/n6f+wbsUKKvBPr6IMQ3+5k+PbY8PZBhl9fENWHirMy8ILUjJE9t90ipgfSelB5S46qST5fBq03zr2ZsZ+JA+NUTQz+hnz912rebhJf8m5w5EsKI3On8BokeVaaZRB3kK8hU1ldDT5Dhh0IO4tjy7QjZPiryV8GdHQfpA/MbNhVwBXYTQ2QOLOh6W4AWfn5RvQxbAn1gGQVBXGMOEEJzcnK7tZ+INqvg7CvX79a0PIv6Z2KSeTedqoRXPBhMPL5c14CNw48v/6SAtvPkE+//f4J+W/kf9t1Ez7o2EJEbojBdI6R1UHZILA2mwQuGxoQjLLp3GL32+/3UAzWpbBPwooK3ADcNkNp3xJh8OAen/fgQJ8HE0H50PQjbkjrQ1yQoIZowSqvnr+kg4gMLi3boALvIN4336F/j/ZdzxCT6oEhjJNbZslt7S0Hh2DaWem8IKKLfCAF3YVxrYeI+llVw7SFHdcBqT00U7P+FsI0q5EKVk7lds9IU0FXB8lfLSh6ACeB9GTWXxF5toWdLovhXwNAN/Vwd5YGQ+Af6Xr/GQopP8Ecm76LeEE2AKKJ5GZp5n5pVuC2zjXvGTFMCo/9ULgJ236LDE0dDDG61fQt87g/mybEf5xCPiYA5EtDYDiF/P81wdycEYT9XODUOY/MN+reuGfeYNcAxH1yg5PEzYhbGX2bLt6J6J2iv6RxAKNVdn+7r3RvyXZfc6e9poQ27Lk98u53eZMb1DBlhhwoyyHNzS/pey94hkDBgFUDrcHKjgaeyD4UDnffLfUhXMP1t7kAuWfjUCUwz5G8seLARlwIxK0kar8cCu4RGJg/YCg+WCG2/4NXCJQOcwPKR6ARAUxk2C9u0G1g4cBZ6l4FH8uDYdrK73F2EFhZ4AXRh0SHyVohFoAj07AGovDpJgpJAMQYmviBcOWb+d2YYTR+GGgOscgSswbfR+BxEybt0HSgvo+KhFJNx6whli0MAiy46z2yH3Y+YgWNTYbquG36MdwPX5Hvm9bfhqqENn5rC3CaH/r9d+BAKi+T6sZOsBNHFaz7BDwSCGbCLXFf7t353v4/bHn9w3ngp792ZLj12+OPkXtF/LrOq9fR6N4T31vii50lI5gjQQ6qb+3x873SPj8q7fNHpf0g+Q7UK/LXrPtBxCOtXxH8BXvBhltSYIMhbx8fCMbs89T4TA13v6R78C3Kj1QYGA+yMCzq98bzvgR2H68E3rD43oiqoX+1sGXe+O/WSD4y4VEnkF5Tb+iaVfZd/Q4+DXG9o/DB0/BWOnQAZ5j3PDAchuLB/Ao8vaZNHD8/pWYC/q1D0EDGMFshHMPhCeIOB6g6ALerj2FquPjxMHirKUgGTvY6lBZsfHDwfUY+Zthn5P1UcTuppQ08Vv0yzM+DSrgU/vOx9uOkaYEneJCru3ww/X5UGsa2xzj9RyOGioIW3yh2aBmPEh00/kEI/OJ5oPyjEOX2xYwfPFHV5tAuYZd+VHcF7XTgePWMwODBqoOFBPmxgRv+qAbqKUHRwAbtDO5+w++bW9ndl99vMNT38+ZvT+98MXy/Twv3xBnOov/+TDeA+t6L3wbR5iDgNnndML5NrG/Qv2Doud/d8oYB4u2eiU+vkG7A89OAZBnAMby/nbCf7vZAR77NulACJI7P1TBDjGAhQUmws+eDExEkve8UDD8Hzm398OX1zwfkP2WAV8qa2DRpm7hLTxjMxEjCsmnMJMfEhBlTNMPaGOuyJIOxNM0yE8ohAbwcs+SEALbJjqEZQywT82HGCB+iAB34gPr/Ymx/ukuATYOgGSgCI7ExzrjQCJvBSYchXZrGMUDQFGXRFDthGHZCMxYMxWAigxOk67oApyeuNcZxmxzkPcbGu1lv7yP6e1zuit8gfSbBYDRhmvbEHuOUw45NxgYkZpE2wAncGZMAo1nSnUwABfd/bH3EZgjd3fMhb+HECCeXy6Dnt0esh1xkKLhySVUid//MRqxmMsTY2vsWWjLAOJ9GohUci4OzaTKzPTl7LOWdWeSdt06WcotxztkHbaMuxTOv13Nzesl2ri2i3YlOpfK6cmqxWdSeoAarvs9bmh0pTmaInrDCC0mz6TVW4hXmFZpX1Ewo7pOSFNf4sstX0slLYXgbjRzP0hODh1c50UcjVyyh90U9M5i+VMW43szpvX5qjsF5KdByQuGSpq5QnFqouVfsTfSabjfotVnsLcnOVt1VG6OX5HTqZ8CbF/1J9I75ZDfWCmzR0OdgPcnbDZ+zo0sfjLZpToyUdLztNYKq3N3I0LvuoHWzi8BAEw5xWodcqOlJoU9EaSkXmxQVcQo39OZQzckM64XVgSXVrvePiTWLqJmnFgXjc9wpv7ryGsfMuhTXhFGtQ7k+RMlCEOixlDu8Np2bzKLQ9XUCzoeCaRtc2tiWWtBaz2vb3bhcyrWdUynnndeLeb+ckIc5Tep2Z+xqw1CMFQ52s31X7ci1NmNM3ZIavbOKlG+3KZz0JsLusFu4Y4sO+fO6PbETX7PipFTn0VY9+qredLEV4Ov5WLRxn3EKZWbriZMdeGfnCti5EgnecjY7QytY2jhoe/p83IfnLYvDjMmSGtfjaCVwo+2xq+aHHU5slaO2JHCfVVttzGCpMEpsu+OjaWGSVpOMcSIRSefsyFKNyuG6m+y1M3HyRh3pydexoRu70AoPZ56i+smhVHDC807SaDYJtJURWnOSTuSwW3XO2twWibY6yS7TZT2Y0WhLh/msTdE5tZoJy7hfC/oxZ/nVeMRs66Kvz5oGQtpamUZopNaiOxcytpl3cynTz5vTka7VI+2oWAebQtbVIbAqdpLqNJjOgEwB3xvNpnhIq4E529Uq6x2WsOOMJsqSkK+OsDCXZHmZjVYMf1mfVsSxKkKsX23mrnQsrkYhiqgcLPfGeM+vdfsQnl1WpUhU42FTpA+Nt1puNqsjvl6SQor7tNufFppsdMnFXh7WSXxoKPnIxfrkuFfpaUYFTrWq9uv9MjuLpDhrYGIt470qYpRMeLaqXJk+tGcFqlxKHSRkqNdKJ5VhFdAiUdryyajSmbDqOrnLTyg4xHjkTl1aHNGcpdPGTK9DZ9KPtPGJ2NXFbrWN0RPOM6O95pqgQ5frjYJzwfZk7jUt3ypUG1nXsS74caEuMU8HmblNmHWgEnEpu1sDrPPDXuqOfrUyzsHmEFg8dmEmu9Kg2SZTrPNaDM1ps6p875IuditmAQpytQCpSmxwhS3Uy/FSFLu2CZR4Q+rKima8Bfx9dqyXYjlJ2L25UYnldTFNluNI2nrMJN8l9hXv11dzL1NYhGZbqxLm5WrUAOqQ78XzcYRJhSEd10Z1wC7HcYo1zaqz8GgeKMTOnERCwsKjDoEamJrHm0g9iQs8viZx4thd18WTvNDtOFlIZSyz8ymVEC0xy0v7OlLI8wFLxuciDol9wTua1GznaHpE7Z3L2dm6lyCXXApLclSHQiN7XCwAObaViG22JJ+T9MRSWWq3Bt1WuR4XkXI8WicdDxlU9VljdaW79Y6lRUwr/fSycvXNNnSz4ppMaWO3v3hcG9BKJ7uuHLbdPEmvipaUPo2CVW1KM3XMoskVY7W0IZOA9zyJO2pQwZp3pIhkPGfpc8am7DptN10fIy44pJjBFOZ2MyYd0Ze30m7qC/HZCs5HU59jmkKtOLzp5dhz2vVeQME5Wy21dQFw0r+ky6V7qNpC34abjGTqkxRDFtBttKr6eDcRcRwyP0Yp5Ain86vBJWIumctynLHX1Z7SXIbtaieFmTyrDkpyzlt2hAe+X1/JJetV873tuyjYLCdn4LpjbTLaHE8Te7tsPX1NXHfY1HErd4Geo/mU9Xwsjw7LjUzT+U7XDlJud4WqHOtRjKo2RiXFZNtw/qF3opJaBJWlFOt0WuzpKU5M96vdPI5VlwHZBVeKy9hUjoy+PRTHYmtaCrVRkmO8ORF721GSzPMncWLK+w3WpOf0mFCyxESUGE/I/Wg7ZclFqYFxm+zXBKWY9Qyn6tNZ4vo5mnsMFxlmzEJak2MpPec9p+hZvykJPtQFmRBCGm2ivhhTJNWcNsm0nliC3gBR1aO1dNHW52lk8yQxuhJtQ/viMSkcNlmCWc+d9Y4XeaGWa6l1TWzj2MkpNkaaOmkjTmaP3sywXD0UCzVsl4ALQXeWTkdMna6CBQtr7QiYbO1P5xMDq8tQyOc7M+g3TmDFle2W56OkSj4RbM2I2WfTTt6MZHFWtde205g23Dh0lVqT+YZan0ywEzQ+TZhcyXWx5wktGc+JWeJvZFIMk31V1nqiYdO5c6A8ftlZ+56rlnUwjaSTL3ABmaxs42CPT7skXZ05NyTxPFgQnVPipHwG06Bg4/mhiP1jGCvnuD6IB1+KnPB49pTQGatAwzyp5WU6tBfroiJ4F2NWBxDK6ng/3WmgTYxkF8lxNTkyjUPruhTIq64S2WwzYSwqF6RVFnkzbn7az42FqnB+7W7EI4Mqenyhdoejd/SUHiNHdHBEtS2RLLqNJE2PXXxcSsEkPcpLijnihclIYiH7adhj7RikFos73iyy1+A8qviqnUp1PreXe4ES01SNSDJZlnCwLMgjQcrodtHJ+VGpLw1vi7LXT4Mpz5faqc7bdVjsvF0rYH15Lsb6LvbA1Z9U2i4hMtinMjTcMCO5T1JLuHD7ZIKdVjwKB7/WWhNWToXlYb6BDBlJWbc4zSYXbTo9pHpQT+j85CpxJ3hdSXRFAiyaX3HTabSlykuC72UsOISho04nCyovKLXt+fygLSJRRo+kVgirNpj2xiLKhUalOaVQD+51eYlyGa+TxlmdkzkZ8egp3o5loTJ3EeVbpUfOpoakmLOrM99Bdl0vKD4OlZMgiyqsakoTD2RgQAqj95urfA7Ps2i5gCfqTZhMkwsl7J3l3PI5eNh2DDfUgsgI13yF5+meqSJxqoOr6DDnQJ2PTr6vaOAMB8PRVDglMU12dh+7+QwVEp7k3NzaLmMAtgYvGP2Eas5zYeMrrXhBbYvgY3KJC1Nxq21q6QSYaitejYjudH95ZglLplfJeIVJVymA02wPk/cQLihx78dz1xPnQkXO5jg/2gsGs8s2CdFP14vc3BiC5kUYc4pJNljRnXEl2N0KLdW80xtT3EVHck6ovHWIyoO3iAo9nAFjZab6LsO46aieEh7HRrUmCF1uC0sTZmBmtX6mMRG+0XUn3+NoCFb2zBd2pGmO26MwTeDMdw4Te+VPG1qn3bNI93zlY8RiUoYOvvd5Md0Sh1MbQ2ix2KBhK/bWc4LuewX4synG1CtuPd/lqKkdr/W+Btyp7ZLTqpEWai/Io7VxoJmUm9UcUzVsudVzpXRS1fQWrdG3kJpTzQ5BMm/0c7EtrUZkyb20o3diZUHmVncT4SJVeb85rMt6Miehv4IwFdRLoaXK3PcyrMZCOEKfT6K7izo+U2ZkJlxFjk1beTnTBDvkqqNMqL6KHgu1vlzOV6GglEJeOEtSzierjcByTkbGFw5Ob8VsPM+rVarg1eQ0zRfJfD+nS96RV0thcXHnea5SZ/bAWZZTSemp2jrTMhi1zXbLjc2yyU16MZ0vPaJO6m2S0qnSpxrfsxWP58Bcj+d8aEWqt2029eg6RXdWiI6LLgRs2uAXfFqCaDTuqIVZAaImCY21+aVLSNVcEPq6bEkiEbwsypWxo/FqifPwGBRz50ULVHeXUcIoPhBGYyZjowpRwsan100aOos5LuyLMF5MjB0nXeg6uOhzVFvVXuxGLLDIxcl1qQ6by4JOSu5qTNVXi93adH3CvZCV3fGuWvJlxhrChlTPplmMeaGNNqmTWqD2Fmdv1GeK0i0ag2DdkgPhtQUjlDydRhzvrTQ/J83RKIhRJUrri0Lv2PqoV7TUrHgwxbvLUaGu/J4Swqt1gB1p0sJ24/ndpZ+dNvzc63aoetqaQSbbm2J/3jOzEedVIRwBdyfOjkJUytAt2JQJpqDOWIrMa2lf7BLCwZMXzQxwapY55uXcR0uwkPmDNR1z2apqe9SPzhOD5VvahIxDUOwoGo2WXr897c5oxKR2gFfzSx0TxPUknoyLfdajKrZnsDLDLY+n7jLhpYij9Akj0IHSRz5/ROGobaeHUa9frpeRvtVmy3jKsqtlxUF6UDEZ1fF2Kx2cHKBGoOcnkqiW4VzL2k24PgtWaKJufLXovXTGSQ/IJFP44dq9MMRCRtt+Pp26wZlUse2iaXunjGRBaqb76rxiF+Wh0gJ5XMPIV+jKWM6462Wm1p0wFo9qjMrFqiUtL/TzCyYf9rNW5x18aRKyorQ1P79siC4ufSl1yRkwp75kbE8+79kFrbiMBwesEFu37BTNeNjvWjjm9Epr7iaVIk/lBTbbe0JOrmKPioT5lZ8eQ7cHvru0LdFfLd0rpJd0xxsacyZagaDGtVQnHBlYmx6LouvhGlWLmvCsBeOM14IrRwuKPQlzwChXghudjs4k2YxxluroNjPy3uExz164tM5XQBAuWStOlptM2XTorHL3+MUK+iS0XZNo5+Ki7YilpYe2pfhyR5J7nd5g7NhmTTzrYj5Nq+KYTWqQ8UCaTiR7wcABuWT83QzNdArbc+fDlrLZNR3ZmwjdhtjOPpwd9iihHusftwc221lXbjNrSBKfyieyvmjuWEYhPeDk7uI2E3RUEwcOHW+3bHncrjiyPBsx0yVKU41Cx+0VbMWblNU0cm/hfKU6hiqjEjbajycxO5rORHdyyVyrX4yZi3cKZXetmF4RcHDQWDS4k2wvxNUWMqKYGLzW9TEZLeD8e922uMxNZpG41NiJs9my1yxYhdqIIZeZcpExYrR2nMS4WqO+xveTDYAnsDWkxh3n8HrfcZypLKaCkNTZ4axcQ9MLUmgELJItQcATPUaKiXslxCs3awHmEsem73Cer3F063kNY6SuGLoGOHBVwjG+KEuqIdPu1J/GBnokqJnJnVu6W8nQHb8GtAzo5S41wyTresw4X6OJpU96YiK5F7Ca21pqd5MFutAztJxjxMkG0khdk80GnfnpaKllY89cePaEaewiqtQKXIXFaZJzZoh2qnKuqxHuLqZ905CcAU+6yiLA2EzciVh0EjXVYNx6Opna+dqVMzui+hPDUWjN1f1pmc3HGc3IhwS/LLNtn+/LDEzXO457en66vdJ9esUxhqCfn4Zn/o8n93/tsa/XB/nbQxY5xqnnp/93TyTvTwff3+vdHuMD03m9aX/9K2b++vxU2gE06f6ouIob7/EY8h+eu37+10+Dh/3d/b308AryWr+/+KhN7/a4OkidpqrL7q3K4ub2sBqC3VTD/5tSvT1eGjzdHEvy2xuId5VPH0+43+psWOkGw/3bG+IEOIFZg8el93i4Dzd3MGqBXb2RDP0Gynxw9fGGaXhCO7xievr9fwAOcHo9iicAAA== -->
