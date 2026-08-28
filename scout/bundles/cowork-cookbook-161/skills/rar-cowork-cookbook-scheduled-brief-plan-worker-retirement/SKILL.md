---
name: "rar-cowork-cookbook-scheduled-brief-plan-worker-retirement"
description: "Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_worker_retirement", "rar_sha256": "c6f332627bd6fff42d4a0720730213bb5da6e71187ff04a2e977023ee69b995e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_worker_retirement`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_worker_retirement_agent.py` and in the RCI capsule.

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

Plan worker retirement Scheduled Email Brief — Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 c6f332627bd6fff4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_worker_retirement_agent.py` first:

```bash
python3 scheduled_brief_plan_worker_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_worker_retirement_agent.py   # or on stdin
python3 scheduled_brief_plan_worker_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan worker retirement Scheduled Email Brief — Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_worker_retirement',
    "version": '2.0.0',
    "display_name": 'Plan worker retirement Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-worker-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a89cca683f4e5bf3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/plan-worker-retirement'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-worker-retirement', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanWorkerRetirement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkerRetirement'
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
    print(ScheduledBriefPlanWorkerRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOj1pLvV9Gr+cPtobvYhEB9wxGDNhBCLGKRwO3oZgex7wKPv/scJFW1Pfadd/3iRYy6K0pAntzzl3kO9euL1TZhXr18flE8K5sxVpJEoVfNrMydrfM+r2LwK49t8DNz8qypIrtt8qp++fjierVTRUUT5dm03Ak9t00sO/FmaV5lURZ8sqvI82deakXJrG7T1KqiEdyfFQkQNfEGgiqviSov9bJm5ufVrAk9cKsu8qyOJlZ5n3nVP2ZAVhRknjtr8lnVZjMXsBxmgL73vDgZXoE63s1Ki8SrXz7//MvHlwh8f/n864uTWHX9XT3PXU06SUCB813+6V08YAHuBoC2GIBLMnBdeBXQKQW3XGDH8+pD7SX+x9m//3vcW1VQ//j5SzZ7fr68TP9OQL/JjCa36gao7FiFZUdJ1AyvMzrpraGejG6rrJ5Zsxp4NAteHyu/c8qL2U/Tsw8PIa+B13z48pIDFazJ319efpyM//ICfAG+v05cig8/viZ571UffvzOp27tq+c0EzOg9evX5/WTLSD8Thr5d6k/Aa6PyNrel5ffGTd9HnpPdoKVL6/XPMo+PBgXVd55mZU53ocf/xlbEAInTqK6+Zf4/vxgHHqWC2x6Kv7jx7uTf5lBT4Peef5zsVO2/R1LAPmbuI+zp6P+Ge+7//8b6yTKvPrd43/J7q8WQD/Nfv6ntv1PCz7O/C8vGy+JOpAdoGY+z379qkjb9c8/uN9v/vDLb4D1/5WNkreVc+fwNbWyyPfq5uvXn3+o77d/+OXnH9oC5JpnpV/bKvkrnn/l17ucP3jwSfXhj2uBfC2LM1Dys/dMn/2aF/+n+u11pltJ5H6/X3+e/b5epg80m4x4E/pwwe9qpga6/s6PP778BlAiA9a0zv0xqPJ/+7fZMXKqvM79ZqY4edtMYNNEqTcpr4ZRPQP/HxAF/PpAqAcdyP8pwpPGuT/79h/OHTs/OU/shOs3/Pl6B8V7Wnx9QODX7xD47XWmAu55FQVRZiWzEy1JXzIrmNARSC4AMnpVBzDFHhrvE0CjT9OXWZTNvv1rAr7eeb0Ww7c7wkcPpDqt9xNK1WD562TpOfSyp10OQGrv5jktEJPkDtDJjwDIfpxAOk86gHKTV+o4SpKZC4Q4oDkMd97Ac58nZt++fbOtOvySPWAVnz26Rg0Dgnd1Zp8+AeP8JArC5kvmOWE+++HX336Y/efsf1p1Zz7JkADIP+MCNOQUUZiBOmsni0HIQJABiNzj8utvTxcDNqCxzEAUIz/yHotBnsae++ZvhaU/YcRiZnvAz8DHaZFXzdS9ouZ1tvdn7/oCodOjCc3DvG5Aryq8zPUyZwBcLWDOuyezvJnVIBlrf/g4a2vvLvWbXVl3FVNQ8FbzbXZcS6B35Mlbr5uIwOI8i4D737PhcR8wqX6oZ6s3Fq8zYcrMWWFVVhFW1lOGbz3iAnrG23LA3JplXv8lm1rlPTnuZfJwDyACnnGeIf00xRy0f9DBM7d+k32nsaYOp947XfUlq58lYFVTKBzQEoDQoI3cqTH845lSdZi3iXv3n/do+M8ouM+o3HNQ+usZ4b2Pz7b3seLezmdfWgxB57P/3Rlk0ppmmNOWodXtZrYV1JPx8OY0OE3MH7MWGASeYkDlfB8O3qDlDWG/ZEkEUqMa/vGgvMfgSfNArbYCypzo050/SABgycT3np9TvlXVlNnWl+wNyj+CkN9xC4QIFHP8sOVN4PT0TdMQVOx0/b2t3+NZuVNpgxycFa2dgPzwPc+1LScGWlVTjT0DAZLVm+qtDyMn/INVM8Ad5ATgPwNKRKBqgHfvrhNyYCYIjF/l6XfyaBqWgBZu6wBtwWTqvc7OoEymCNSgNsHEM9EAL/xwZzVLPeBjoOK7h+vQKh7KTMPsU0FrikWeguz9fQSeD78n9l2XSX3A1XKtBviyn+DW9W6PyL7r+YwVUDadSvG+6I/hfto6+33P+ceX7K7jO8KDCn+k73fnzEBlpfUdUieAqgHIpN57nj468+ujuT6697sun/80wX/4e0P+vV1qf4zc51nYNEX9GYYfLe6tw70CeIBBjkSFV3/vdo/y+zQV26dHsX36Xmx/4P5w1ufZ39PwDyyeqf15hr4ir8j0iI8cb8rd5wc4ZP1pZXyaT0+/ZCfve6Sf6TBBLChqe3jvN28koOkElRdMxI/+U09tqwed8g64IBZfsvdseNYKwPMsmJplnf+uhu+NF8T2Ebr3vgAeZQ2Q7U4jW+BNW5pkUr/2Xj5nbZJ8fMms1PtXtzJTAwBJCzwy7YJAAYExqIm8+9X7SDRd/HEXdy8tgAlu/nmqsI93mPw4e59EP87e9gb3LVfWgs3Rz9MUPIkEpODXO+37FtH2XsCOrBmKSfvHhmcavp5D8Z+VmAoLaOx4U1PP3yt1kvgnJuBLEHjVn5mI9y9W8oSLurGmFh01b0X+lqIfZyB+oPhAPQGYbMGCP4sBciqvbIF33cnc7/77blb+sOW3uxuax67x15c32HjG4DkhAnJQn5/qqRvCIFeBQHD9yCrw7P9xdnxyAXAHphbAxln4OI4tMNJ2F77vzzF3biEkhpA4gqG4bROutfBIFKVI30fmFuYtSRLBcM9bLO3lkvAAv0eGfp0afzRphlmWQzkkOneXpLVwPByxccdDMdQlcQ8hlrhPUd4cOOl9aQyw8mnuw7zJl+9j7OSWp9W/vtiLOaBk5/WefnzW8FK37DNsn0IeqhLodsMXMq4VGpSXnnPNNMdEnWBtCJnQ66HS9Ul7OmBFFR2TfojS3Fjs4ZyH+q49u2kyQNFu7RfzyyqP1zQmqjUpDrAk8YKypZUrQWTHm2tp6CLXCqtAStUoK0rhzQOuiIlYtEK4z4yULXSTp/y260a9M7m+qNVdUnWSLogWHkV607nZXuugNbHYz6vsVigJ0+xOpNm3p3M8lOOo68RloR4WyVm0lfo6XPPLQVfblajgSoJmLU4jYtZRkMRHlJvxEQbvbrZ4SUaImUe6xilWp/DnuiS1wrUvY4oF1TbJ9mfGRzY8fOoyPSxRnhuVq+ooGY9fkKwVlL6fN3S+XZRtLicJ5l2qHVGej2Hpns4H7qZpyRjhu8sBiUHzOSSNEK6UTj+n6KDpaZw2+DU1SK/pjNY0MdWmLsUlbZwizog9vk0Oqeyp1ZoaK9FdH85Keb6pByLcjkrM7jcOwW4uWjpexCTrMs2lHTK+4vKeWRxLRYeYweztTB6jc+EmSH8Ni9JewefI650FetgZuY9W+6hD61NJ3WpFtlmWPEa1zva2WpTsubvU2fq8P3J1GqlwOsdqXYCrJWgh801PqQRyMoH4QT+dnUrZobCgdRfmZIv42BvMaTh0TnjW4E5abM8ivl7Zvg0NIqZa5H64jctR1EvitjuVF+46uKyxJyHMSBGsjNGDBeWD5q+t7Rqe35aW3KoB7gun0VgQV3h1zPibrMAbBkMk2rduw0E7rnjWOTaFiu3GDG5vWN6iia5jUlIn3WZ9O1D8lhTNvSIguTcehfqSr1P0YKo6aqqXZijLDpeSgr+Sx66aMxlljtQ5mfPkwApLuDjtGAu6LvtblyFzA1Z5eDW4h3QBSfkREdV5ZoR4H1kJH+WkhchRq5e6FV/WW8PnwloTMWO8YNwpOjLF2Avuti5sQmliLmiOla7mYuiedhuOFR30yEWoS4QWqgLXVqfNnh73WFSuM+Ww2ku3I7bfhIxsjs6Q7tsg2Wo38yKkIrvtHW85tvpuLsIkczr7VnhweMWRw0gJ4lhuOHSvx6Sgz03ikI5U5I6+oJ2H0Tk5CMb2PFPJZMKKIwrjcNiq7IE4wTaFbE3sMHTEsYiWrmb0O/q6w62ToCeCebtJt03U8vbGwIJrnngr2MsNX0D0ndSja3kOn8VdoTEnyvRKbqQDRrfKU0jB9QHzElxhnX2kEfVSSi4XxCr5o8HbaLCGTFB/uILgRXWmdh7KHQf+UOJzaH29qiZ+VRRBLhMHtfn1aUhgdX1yG4aud9tjr7qr04LNbhtGTfnCPXMHQqIjfB5nlSvsbyq8DJFEuWplIeW4EoiJFhpJJXSdWy0MMhOL/LKm6gBFcpvHxHRjoqqApVsyRDzZKsNdU4xi65qGUhys5JJYIT9YrXy7dlFdJ3LSVZ60GCrhHHuQH+8JZHGCEJCDoVxFqSL7cye2Rv5Kq50s2FBeG3Ds4OXOQkmJDJZly7siThlFCLvF3kkz2JbDvTbIaVbBghpQBIsX22O3tJm8YK78eiPuHPe2p1FfZ9Z5h/nR+bZeqWMN7/obtRNaVlHj8QD5EjI4rezpktqSKawimEd69l7i6SoAy+Mhxg+c6wdrR2DONFpnBzrYCooRcXYK4mDLyw4iiysnYw3NooV+RlC8UQPLso2t2xNo37I7zpQPC3IUdkes4LhuzHP5mtXhZbvj2IuU84dVTZi72q3mFyxJnfQSMiaBLpeQSs2blF+je85Lz/UtSXAf6auFdY0ZQrRHg2H2i2QXEnOUallpl6wwrO9qKVnJYR11MJHHVNl2ErqEcntxTAiYPEkMH4Qm6XlnsPk4rkVag7WY3aSxM9TzKtAi6CKWMajDkdru6jGybJvb9dsSsiNGDWo8Hcso31uxpy1dWTtopmBElKDOpbXmCEEoGTtIXwGkUbfo2uBx66xTuLyuxGFXcls3NlOLuO6RGsHArKaQRzzhoPV8HhUaru0leL5ds0ymK+iBDJU2s7UkRcJy1FlHgJRlr60tnusTGz+fNZNtwziL9qR55VMu2jDU1he4VBFlmM8qycg6bd9C5mLZ3oo9d8Rrk8xhWUD3SGGU5I7AIzLeOGotu4fryYSigkzm812zv7nmNaj283ZbrlE+wTlTkDNqa1CMs0V2TnW43RaWp+R8HWjt4USWCKqeVug1FeFFcSaMRWAEPG3ZhXc5Sma+p4je2OnO0ocp1uW33L7Ax+7UjopOr1ST90O+P8Ar4aipsRMv1KXpsTjv5WtNF4PjztdZvVTNCE3WLnMKwNwRGRCXCSNxtRsnydfz5HCTTW8LuwujVt1xFVfrSxtHzJmDDFnpOchMd/kagjDEkbFCWVrQ3vYhI6pQnRPzs26s4XTZuIqhdGTsXjVTFlsP3Rw8L/OdeSSs7b5QdG8bSWN75RQe5fQdwxVzS2E4Kd33gtwpIX9dQfUgn6PzuOq2Srw7GEi0uRjaSXHPplZv1xsUQiIerHJ5Hwlijs56F646itF4WIYWi8secepEZRxalpu5UOQCgZCZhsbnE6KfpK1fhSzmdLCn0TRSWElfldd43GVX+Sr6VjqPk47ao/hZqoRGS3AEwo75LSBSpOqwucQxh96qsZjZdFbdIpq8Omo97eTMfKwlLDGKYi5d9/pBNVbp4jJGh8t1gMWDfzKHG29sFxv9iG/V6nKQjnBIyJfDtlnk+pZlUStZzwVEWCNlmZCIQbdBKa8J/VQKC0IrBRHKr/MV7YTdyR2WjoXu+3h7OQk0oqy6td1sUWvuHri9U4dZERNmf0pKYycGjBhDK+8sWx3BdRqAq6ZMaXNZ6+l8dbsIHKFAjoFGjircDgMsX5ZcxRz4ONKTPXGiYifb4fMw3A7qlutLIz3Gc78N9aUaoUdzNAVElHiLsTIhNWiEHiBsX1srMcXF9dHr+qOWuUJQtMuDr91kxmUE1rw5aVMW1GgWeVMcTGoe1qSri0sUwbZwfynDZHdgh37MmW4UOtrMaHszOtTRsSDNKRQ76eH6cqFqJC/FcHEFLUfM0YW6JwdVup0531leAXfqdmLpdjHs8yo5Lvdos79uLnt8J++PZBtzOctEBnkwSiInDJnYZCLk0C5doySeZZfaYvVuA5WInO1rjYS2BdN6hUWS55AujJqn2hJDV5q+8opzI8cQfckzRqFtlmPOAdEGeKEVLUtYTJ6l+UksuQ0fK1qxtKvsunLnV/sMQHJZyJmosaV5sIXE6WFmO3K1pl/QTcHSCz/eCEncyPZVUnRzUUiErSkrSYQkobMIqT4trLIvtdJX6XAszO2g06PWpXuPxNpeoHeXqsu8lQHfrgyfD1BiO6tchlp9xar+TsRdUrWCojewPbUrUl0JPWqFHtvlBhdhDfQCYrczGfZiMNnC3SoU53Gpnp02JhZFKMdu2HBd6FTB0GjhCAnDzZe8s8CHVSHPjU0YbKmVoRnyiDCXnXdEUu24kK+jqFbD4C6rNXTao7IJy2uJ3lwridtEZyHz+i4A5b7fqlKKzLW9uQiqig42EZVT4m04o01wy83rqrgkDO9m6Agbh0hcQguOzFcLa58M6EYSE6sSIVs+0UgKCjsjTwLC6zhd6Km0gpHepLvRILAF2MKQmR9TdiOwe9hDS7RbZgXhQPi5LOC6uxFOCp+7ZUlil2HBHGCnHXqD9yCIWdyCBIC3QiZo14hQkbr7Jm939IoQNmtDdnRdJDACszclydplWDYLe34kggj0i7FAB4/aXtwTLwdSuBVC9ngoydHzV9dcIHFfk0Vm3pPUhhqI+hY7Vlst+jmTSsu8u6Y3xKNUFmwQGsJvR7SWNoZknvHM4M6aRBEb1Rlw5eLBHeddq0GScPAhd5fbGkzmYJ8O6xJluxd0JMssQ3173G0wnVhuF+ly1Rahusm5bj2k6XaTrQxqDE7tAlr7xy0S94Y4dKZuqEK0yjmEINbSVi03Q0LR9srSrjd+S4hLwi4KvSakHkw7vNM6sIsJbDRfoWHF6cctyuH8eTkfrwVjbFihG7gwoTYeMr816aA7m2FHOmAjvII6N2hFarBWxs2Plm3sRxTJm13MLzee2WaUlW9POEaf/YWxXCLMJjfrmgskXNOjzW2xF2KLzUpp6eqLCsZQCt/s1md3lSyDmKLRS7y5WfBGW7BdJg2S6pzcFmVJIxqjldhXZDBg6JU8rCkx86o4DVdz35I8xxxjOMscvlgG6ZxWYGFossDhKSOdnwNzjYurLbtWF7BwqM770ZsS6Dgu1/1pa6Kl28n4btMdqwo9SRJ1oF3mCDnzWsnoSvBkrps3rBtkexmmM9HzhOa2ydlROQrWqoY4Fw/1Db4oySVOkvyx3wiIhNJuNF4UXLo1o3fbrLbnM0Zzzta4NFVgaBvmZm90hiWh/qK7vBMefHbQqZ0pXx0VFtIFg93I2q6VNc6o3obKuhM3xvUuQjT4sOzEM91zGhdHnX8iQ6k3TfZgV5ZAZQLeVbcMj+Q8HKksD8AmaEl5BDI/3EJagHyM7s98Lo1kJpBdnRrNja3sAA0um5XhNgdhFLE1HipLG+eztCUYewnxmy0o4qFl8kW7PDFLn42zcZWv1wqclzSOHXATMRhtgzISUbssqRyu8ZK1satGE+7SkCFUWsVYi/YBfqOtzPN1iA1WVId1/ba3CR+VEGXhoPg4t+cGsXdJ0P4Ri03ojBp7buSo0b7Au1MK6RZ7S+SIhEiw9bpsXALZZRJErnw4Sa6XdU7i7fbq+spuFLfX3Q4P19l+de1RPdNxUyIqJvbGRUjfzlWV8l18uPFzxb+VFqgYTvEqcl47PjuethumE3DHu1nUYrTXDY5W3Y66bsCOcY/MR61UWXZP47mDddvVZhW4nByM9XARcVGSr3GPwrYRJggGk7rT2b4XpI4bCQpdbyyJPPguughVzJGuSMmXGEfeeBxnU3p3DTYtW8hNE1zTJaOL2pI8m8pxQY8n/KwEcwglHSs5jedlYmuO5ABXM47pC53rZDaNk/BixQc1CfYj3fWIsthBPSz92zzcpLvMJWPpgvuitlNzO0h3cBauieaW57YGD8nqwC4S6oZgVwynejZdCu2K6Neuw29ymNaup6Jq5eBqLLRmG60cV2vdE7GXGJzM554BkWkj9qWXYFXvtW1MsHDP7JfX6yWJYpqmf/rp5ePLdCj9PFr+my+Rp3O+/2/HjY+TwbfXTfdjZc9yP99lff67iv3y8aVyIqDW43i1TtrgeQz53w5XP/1rryomHsPjHe30huzWvJ3JN1Yw/cXRS5S5bd1Uw9c6T9r7Ie/HF7utp798qL8+D7Nf7gamxZ3bHw0Cd0Ig6muTP815mf44YXrz47mR1bxdBs9z548v7gBCFjn1V3xBfPWqYrL4+f5jOqidXoC8/PZfa6TXX94lAAA= -->
