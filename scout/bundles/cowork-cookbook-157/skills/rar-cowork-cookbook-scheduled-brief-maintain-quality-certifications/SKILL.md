---
name: "rar-cowork-cookbook-scheduled-brief-maintain-quality-certifications"
description: "Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_quality_certifications", "rar_sha256": "5accab39611ece471f2fda2f747076c8455bce0a6d00588caadc40fe9b52716f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_maintain_quality_certifications`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_maintain_quality_certifications_agent.py` and in the RCI capsule.

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

Maintain quality certifications Scheduled Email Brief — Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 5accab39611ece47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_quality_certifications_agent.py` first:

```bash
python3 scheduled_brief_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_maintain_quality_certifications_agent.py   # or on stdin
python3 scheduled_brief_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Scheduled Email Brief — Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_maintain_quality_certifications',
    "version": '2.0.0',
    "display_name": 'Maintain quality certifications Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c2ec1d0cea81b1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMaintainQualityCertifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMaintainQualityCertifications'
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
    print(ScheduledBriefMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZeb6JLmX1Fnf7CrsVPsi++554zQAmLXwiLKdVzsIFaxCtXUf58XSZku31u3u6tnPozsPCngJZYnIp6IF/K3F6dr47J++fJyCJxixjlZlsRBPXMKf7Ysh7JOwa8ydcHPzCuLtk7cri3r5uXTix80Xp1UbVIW0+1eHPhd5rhZMMvLukiK6LNbJ0E4C3InyWZNl+dOndzA+Rk4UbTgZ3bpnCxpx5kX1G0SJp4zCWtmYVnP2jiY1UFTgeNkklkORVD/bQaUJlER+LO2nNVdMfOB7HEG1g9BkGbjK7AruDp5lQXNy5eff/n0koDvL19+e/Eyp2m+2xn47GSc/LRk9zBk+YMdQFbmFBG4qRoBSAU4roIaGJeDUz7w7Hn0sQmy8NPsP/4jHZw6an768rWYPT9fX6Z/e2Do5E9bOk0LbPecynGTSeHrbJENztgAV9uuBq47swZgXESvjzu/Syqr2d+nax8fSl6joP349aUEJtyN/fry04TC1xcACvj+OkmpPv70mpVDUH/86bucpnPPgddOwoDVr9+ex0+xYOH3pUl41/p3IPURazf4+vIH56bPw+7JT3Dny+u5TIqPD8FVXfZB4RRe8PGnfyUWxMJLs6Rp/1tyf34IjgPHBz49Df/p0x3kX2bQ06F3mf9abQXC+lc8Acvf1H2aPYH6V7Lv+P+D6CwpguYd8T8V92c3QH+f/fwvffvPbvg0C7++rIIs6UF2gOL5Mvvt20FbL3/+4H8/+eGX34Ho/1LMoexq7y7hW+4USRg07bdvP39o7qc//PLzh64CuRY4+beuzv5M5p/hetfzA4LPVR9/vBfo14u0ALU/e8/02W9l9W/1768zA5Ss//1882X2x3qZPtBscuJN6QOCP9RMA2z9A44/vfwO6KIA3nTeo/6/vPz7v8/kxKvLpgzb2cEru3ZinTbJg8n4Y5w0M/D/wVUA1wdVPdaB/J8iPFlchrNf/5d3Z9PP3pNN580bEX270+S3N1L89iTFbz+S4q+vsyNQU9ZJlBRONtsvNO1r4URB0U4mVIArg7oH5OKObfAZ0NLn6csMkOyvf1HTt7vQ12r89d4Fkgd37ZfbibcaIOd18t2Mg+LpqQcaR3ANvA7oy0oPGBcmgH8/TfxdZj3gvQmnJk2ybOYnNQClrMe7bIDll0nYr7/+6jpN/LV4EC02e3SWZg4WvJsz+/wZeBlmSRS3X4vAi8vZh99+/zD737P/7K678EmHBvj/GSlgoXBQlRmovC4Hy0AQQdgBrdwj9dvvT6yBGNBzZiCuAJzgcTPI3DTw34A/8IvPKEHO3AAADsDOqxIgCTpc0r7OtuHs3V6gdLo08XtcNi1oY1VQ+EHhjUCqA9x5R7Io21kDAtGE46dZ1wR3rb+6tXM3MQcU4LS/zuSlBrpJmb21wWkRuLksQBCz97R4nAdC6g/NjH0T8TpTplydVU7tVHHtPHWEziMuoIu83Q6EO7MiGL4WUxcNJqjuKfKABywCyHjPkH6eYg5GBNDlC795031f40w973jvffXXonkWhVNPofBAkwBKoy7xp1bxt2dKNXHZZf4dv+AxCzyj4D+jcs9B+b+YI957/Wx9n0HuLX/2tUNhBJ/9fzKwTH4sOG6/5hbH9Wq2Vo770wPfadya4vCY0CatDzWglr4PEG/088bCX4ssAclSj397rLxH5bnmwWxdDYzZL/Z3+cAngO8k956xUwbW9ZTrztfije4/gSS4cxsIGijv9OHLm8Lp6pulMajh6fh7679HuPanYgdZOas6NwMZEwaB7zpeCqyqp6p7RgSkbzBV4BAnXvyDVzMgHWQJkD8DRiSgjgC6d+iUErgJIhTWZf59eTINVMAKv/OAtWCeDV5nJiicKQINqFYwFU1rAAof7qJmeQAwBia+I9zETvUwZhqBnwY6UyzKHOTzHyPwvPg91e+2TOYDqY7vtADLYWJiP7g+Ivtu5zNWwNgpwx5R+jHcT19nf+xLf/ta3G18J39Q8488/g7ODNRa3txJdqKsBtBOHrzn6aN7vz4a8KPDv9vy5Z/m/o9/bWtwb6n6j5H7Movbtmq+zOePNvjWBV8BYcxBjiRV0HzviI86/PxWdZ+fVff5x6r7Qc0DtS+zv2bqDyKeOf5lhrzCr/B0SUq8YEri5wcgs/zMnj7j09WvxT74HvJnXkzsC6rbHd9b0dsS0I+iOoimxY/W1EwdbQBN9M7FIChfi/e0eBYNoPoimvpoU/6hmO89GQT5EcP3lgEuFS3Q7U/zXRRMG6FsMr8JXr4UXZZ9eimcPPjLG6CpSYA0BtBMmyhQUtW0IrgfvQ9S08GPu8F7sQGW8MsvU819mk1D76fZ+/z6afa2o7jv2IoObKl+nmbnSSVYCn69r33farrBC9jQtWM1ufHYJk0j23OU/mcjplIDFnvB1PjL99qdNP6TEPAlioL6n4Wo9y9O9iSQpnWmNp60b2X/lrSfZiCQoBxBhQHiBGj+iRqgpw4uHeiX/uTud/y+u1U+fPn9DkP72Gv+9vJGJM8YPOdKsBxU7Odm6phzkLRAITh+pBe49n87cT7FASYEIw6QRzie57gYQyJI4AU4hYRo6DtoSOEUTJEejROE6wWwQ/owTNC05zi+h8NhwLgESiFkCOQ9cvbbNCUkk4mo43i0RyG4z1AO6QUY7GJegKCIT2EBTDBYSNMBDtB6vzUFNPr0++HnBOr78Dvh83T/txeXxMFKHm+2i8dnOWcMxzXn7j6WoDqDrleM3GF6BadFz+6OaUjWsSqlyyNRSd7mpNfNuh0FE1HS3WidRdlh+/IMRT11gEgbNVDoYHEOvyBxNs/OKdXdmrk23lbymdXXQ3CwEauT57Tj7HOHwLbZxqgNj0xdvfMSJRD2naFUmXj1DJNMB/pS753EYObzxpynFpdfJaf0KrQnbtzccG8HRenaWttrwZJE+VucGcYhwZJ4LxpaAgAfE6j1jB2zuZTXgLglcyk9GsRS3FACtoDyLqtrwVeF3NOsYqQ7SUCDTqrp44ZmvL4f+o2Dx2JSX83ggKQ6ColJQ8IxGp3XWSGakhxAW0x19epowFUnELkqIkXLt5eNOMAMxm4bRxDJi7MSRkq1JBa39NiUEEsHZHvaWfJ6sW/OgtHZZKUPzBoRacO2WEk3TGETonyP40HXI9g6uZX+XLoUSe1VaWFv0fSy2cY0dlgSMOqR+qHJ1tU5N66sAMdbdK8Qqad4IsYxsJflHkuzo2+q9qIpS65dGaUlFHGA8/NxvJRV214jrN4f1SPRrIOc0CtdulK6a9q8dz5VuoFQOw4hoHErbYyGg0lnh9RKLcJ5fDQ2TpOPIbUxWufiYgbZIKeBr8jCiIoD1wmpmDdEd3INGjkwDUE0jKWpkb3Vj8yp3c0DkkNFzN97G4SWBXJ0LZuz0DB3Vm2tbi8bkGTmviwAGJy7rtpLqRwyGTYcIVIOm4A+Qe02aq9Wzxo3vE/Exp7jXWKkdYZHiQxTsne4wv0Wt031ZLsiv9byHncgs4wVy/ZzzxIPtOyuqV13PBXdMlGWmZyEnE1aSicVWk0VUj1Ph35+Kcyt3F5lkHlVGOFFGlNliA1Fi9OUoW5ks4YGtS5kOgyP4XyNEKp1qVX4gOsKn0UCJPryOs9G5uJBS3NviXTdOu5mHfZSrOrq6YRZqnDwZDNfDQeDbyqeMKvU7pWjZLqlCvkOuUoojSa3JnuZj1waFFwnmR6XLljhuk69uSmyYoHn9jIbztvrprGl9X43uqLX3Mqi49dDAzG3zjBwdY4durzo5v6REHIp3Cs4loaKomhHBZGzm5GY+xWddPMivxztQrCCowaNx4Vb6pWDCRis0ULM963LJeMppo2CJ+aS73HdCBWLLc2dXFE6CmukUghYuNjXE76yrul+0S2Oc/is0d0SqaG8SBXrknrD4kqoUNKV8SEz+B2qeuvNWBvJRptD1OUwr64wi4TVdb2fz+Uu3CKmAZPGcUXYBwdPzsu5i7ZqTYGqRE6JHOGur5wTH9o5VqCwNXo2jlDWkYQrIY7YsFlxWaGwpkWHobZTJAITQ0Qv29vhRh8kMI2t8ci3AlLQt7h14YkFNYrmpRZXfrMkSZfvt93pLHuNiKZbS+eYo3hJW7xYLcOBpISNDsxC7BxTo0YIWUWk0MuO8NtCjHdY7oSrk2eutBXt+2ZphqFalwzsRDAyyqtqfr6EmiiXar0cL0fBCRYex9x8AoJ3ucM4MDWqLOQsmxXZD4lpRTiXMphUhMMVCTKWGzi0IVZQymOVLBe8tD2OmajGV+1cYSRyYhPlZG0zbJSyaBH7DaVdHa1nF1ScrSExW2oX1NesrSV31jywOXqUNKVp19s2siPzsEjGEgW5pg2bQhM2keyK6G67kfRLlIQFushrF2qJ20KOK+2gs4yZ8YClaceTxgRj14EZ09tkXHLw8trR5/1RSHY7mg82EukxFonH1baw4+G0a7HT1se2EK1thIK1rksfA1XUFcQ11CwE3R02y9uQn7kShg6Hs3CBHGqbQGgQL+TrvvIgOuhX/IAtKNct0OUG9hRD5C/nNCzKXg/FnoE0Co5MEb0e4FweKIzRvXW66FBhc+CVks6qbM+KLBnbbCtHq/AUM62MpyS1k7soO0n0/kZvUAg96oh61s+3oo4OFyerzFMve+PqVggr24gWFxb0s41k2gCz+MQzwQaTNYjuAz0pbxQCCy1kLjC+wG6dBQooOHh0ClWXpRiK5olKNLHdtAYF12pJkttWz/yxqM5ny18MOMOtdhHaiB0BZxmnUJANgMoaGxlXe+GYL4k8uq3OJWhkbXFEasYh8VDIxSq3G7iPLkOcCbChXKgChx2rY9q6PSpDvKvU3KW22mjEy7E9cKmvj3KZBNd+dTlciAsPoaG3o5fLzFnh5k0pQ+eSJcsjLtZJ4xCyptO7snbsQFFLJw1wOZJJyNnaCrUgSS5TUY7Xh8rW5hKc93KuixRchnY9sidJVvR4N4hz1paNY+ql+fFmq3x1tUpRNNRI24SGjl0O1DoJfEmAlqudiEREVa0Q+hq4+EU+V+zWud4iYbUxtjIofje4pi3LJ1lsOttduVBGPwnwDFbmcm9mW0sSrow7Ipu5erWJi7m5tM6gkW2d2ZsyDbCUTte7OKAzireakA7i/YY0r7Yh7al9eVNIOeP7dWaZeJax8Gk0mWLNshJZivUOk+SULNtucNR1zXqmso2QcaMb/D7Xa3UR6SffXc4tDst6apdWrFmuoCic22FbWEnLtWfhKrsar7O3rSR1A4EjSuykxCWXVrLDE0u+7zEeNRssNlfewW7FnT+yTNtc3eHIlxoaMMe6CbZBayG4QZoEFHpCcBavauZqrRU1qlPiubpQNwFDKuJwjJXssGgUzotWLVkSB2MI8Z1jbyIOrjJ1mwW9G+EVY1/EpFucB6/TrpfI4kzH4XhkkaeCwxwuldpfDJm/+tVhlanVRrqVQn4utplXlUK2cg1VG6FrhLNbOQ5X4VjvnFtJGEN3OXXVeu+l8529RG52tYvHWoZEIddZm05Y95SllbxW4IQ35oJCxsQIdzp6ZBXBRndYeruaAMYlhwdmitc6fBMo9nZJqxTtElnSkUwe2U6WjMxm43XUWnkd0eYuWZ/VS3w1UZLfFO1ZPua3jU3vcPScCHgEupN/CiPkoo2ydG4LnaqopN4uFKbYY7q+5xCTsfVCL+VCNtMDCuVlDY2kvwwJiTg2thdDcAMtappxrpx34/o9jxUUB3JgY3p5XydmkfCIcYDn+sl1EJiMfeassQKVAX5n2+6UW7mQ7RYUWeZa7p1hw8Rzg9XneOKZLrISY7Is0DEV1dPSRNfx5pbVC6wREC3e2AgiFb4jhRefV8bVCu31Hg9ysqJS5lxXHleOO8Oha8tQDluOMThocSv54LBwBVbkUipZ3EZrr2cEPJdUY037a9Heb0v66BRqbTn0YOTp8YSs9H0nNtjQG5qYnPcWfD4nMmcdlfS29AcgU77Ycpq7rr0+1JB6Lei0FKIit4oc6ej+ukGTG2wG+XJpkp2iA80lLxr0cIsiRz82S50jqBpfcUG6Y3y1gDdJpKE9U0snAqKXWG+et+Xhtog0F92bMbQ1btjZOTtUcLHCMl2gY7K8NuvbVVmRziJHqvxqV1x0KvOmOp28rSL1xPamcfkA6yfsTPbJodODTInjTmSxk3jbDtccb02RtmO9tJszZ9pcv/IRVKOY9QLxCwYMOAsFHbwYlqkLWYOKOekxe7hub4SyseKlBMZ2h6N0Oz0nkKbnWZlvVioOcb6e5hjjLnxRWxcjTvpz80LgGuD9PYK2/k6Hl4ttD7cubBqN4tpw4Wubdn6Jovg8+iqSdAFkEhZxKXiSr31NhKACvl1UMCIoQSBfO4hvsAJqtPUI8RJhnYsTG2FoG1MKQ/GdmO8u3GmQ0CLUsTzrTIutIyaHxmbHLnV7xxRcv7CGS4AJ6EWutnEcrA9I1TirsojXxrVnXFOghRVUesiy6tuYsdjz4DbcgQWDYc1i/QXbpAGTGMjGVDT44pvpQuaxPTk0+96sjuPOGWHaz+2eQGELxMrkrygfEUusOXoy0qnCCSLn8357mwPyt/24wkRonlAQw/J+4GM3mowrPwvSTG15T4QWEXcJzoOIbKyrVvbqjgMU0HIatF4lsrCPb1DtDc4iSnHKi8QVxYMGJmqji7AeOx7AFHrG6TXau1tqgzUdG0WYYVLhMT1pLJ0g+lHc7CCUKdQTQ+wT93Dkqbja26zFrCKXiLFiIBY9n9UBrcM1zeOYYkX+fJ1IJL0PVre27aBdjq/pGyHhiL5BiotI9eSOCWB2U9pysxnlm25Jx5TZkKTCjAxPqPlcnzOnORNfYolLyTA6Sjv2aEdEGLKNfwbWINpR3vsRyvgNe7qy0smoRrt2ID8jQmpfW3W/6Lx+XfRq4Wb0ikKzJTMc1ws2zAlMwsUMWgteHW1jt1ic/VgARVatpWXYoyG19IndzuNAx2RUrHSjuOqslKyKcygs1DMXmF6wX0ZWOpRrzANzzEmB1hrmDBlWBH4YLGhdYs1h1ybblNLJMFR6q9H4ch87PBSpMVsLzYpxq0KKhkhdruQMXZrbgW+OEnurGnbkl10fHsc4xDy3uYrofCXjhzyzhuv8giIBRlDZtrnqWEIJN1hvxm4luFKYLVEeWjWys77srEgJTkcK9CiCJ8ljqSMd23d5GAjLhNdgvz4uQnNc+DTY0+KwDymdcDPPZ/F87vuztGhwZENSm+4crbKo5VAwfwnuOYSh7hKPFVJ1cRHC21LeUWBibLQ9cVjtUMLjh3ZY6dry0KcGWxAtpsCntb4iOe16IjX0suFZRtOqRQmRNnmoIEHd2O2RilltuYS7Yb7wNI5xPbnnx5vjhrBWQpRHUIy6XbvXkz3v3StS8+2CV+cju4ogKG7nKn5MJcXdu3nkjtXNQIne3IGWH2O4NqeLJsGNc6BgC5cirT5egN02RG/160IJNuUJ0TEFW/nrVeoaWi7Cvoyqc73G+9iZc0TJRWnGkl2dEMS83+h72LVwx8vPQ2Db/kggV/vMexYouFQoGYnclgyWLc6w4mrlgitJeX0ybG+Nhp1nxlJVjAwTHA8I00JMK1wrCg8Txtw2fMwxGNbR7U6kVH6g9c3V1TE8lW6r24IbBtZawicTHdgBAgESXebgHjx0e4tH/bA7QYYEpo8dIwYJU6tWYqm3syr2ySXHWnRQ6DCOBC8rfLHZzC2zHK+j49a+lGoe3VGSdx4Dyh6XOMXhQhwSp13negcxJyV6NxhLxoRs0t1Tbnw639TcWtAe2zUW29SylQlxyZXlrlE0K+uWfSIxl83aUp1wQM4XVct93ItvJKA4RXPt0j/O8dVqOGHdOFwWi8XfXz69TI+qnw+c/6evn6eHfv/Pnj0+HhO+vZa6P2wOHP/LXdeX/7GFv3x6qb0E2Pd4+tpkXfR8OPkPz14//8V3G5Ow8fG+d3q3dm3fHuK3TjT9YdNLUvhdA/by35oy6+4Pgz+9uF0z/V1F8+350Pvl7nJeTU/Q/8HFl+kvHabn1SUQ0Zbfnn8Xcj89vTkK/MRpg+dh9HxK/ekF7NKcPPGabxhJfAvqagLg+dpkepo7vTd5+f3/AJDRiKpUJgAA -->
