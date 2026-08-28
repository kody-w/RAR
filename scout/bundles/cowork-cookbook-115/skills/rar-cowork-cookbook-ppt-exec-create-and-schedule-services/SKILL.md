---
name: "rar-cowork-cookbook-ppt-exec-create-and-schedule-services"
description: "Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_and_schedule_services", "rar_sha256": "82afe041fdbde13d7834fb29427a2682f7d2c22a84312be42fe8d917544b8b64", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_and_schedule_services`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_and_schedule_services_agent.py` and in the RCI capsule.

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

Create and schedule services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 82afe041fdbde13d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_and_schedule_services_agent.py` first:

```bash
python3 ppt_exec_create_and_schedule_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_and_schedule_services_agent.py   # or on stdin
python3 ppt_exec_create_and_schedule_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and schedule services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_and_schedule_services',
    "version": '2.0.0',
    "display_name": 'Create and schedule services Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-create-and-schedule-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bb80887290479c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-schedule-services'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-create-and-schedule-services', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecCreateAndScheduleServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateAndScheduleServices'
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
    print(PptExecCreateAndScheduleServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpb2X9HUfLA96i4hdvqGIwYJgZBAC0hsbkeZJVnEvgv59X9/E0lVbY/vvXM9MRGjXkpA5tnPc85J6tcXu23CvHr58qICO5sIdpJEIagmduZNlnmfVzH8kccO/Ddx86ypIqdt8qp++fTigdqtoqKJ8gxuF0AGKrsBNdw6AVfgtk3Ugc8VsL1hcsh7UB3yKGsmHnDjSZ5NXPikAXc+tRsCr03ApAZVF7mQRN3YTVt/ghzTIgFwWR814cQN7aqp71saO4mjLPhc3GlmOeT7CkUCV3vcUL98+ennTy8R/P7y5dcXN7FreOvlUDQrKNjyzpnNPPXJV32yhQQSOwvgymKARsngdQEqP69SeMsD/uR59X0NEv/T5D/+I+7tKqh/+PI1mzw/X1/GP0qbTZoQTJrcrhvgTVy7sJ0oiZrhdcImvT3Ukwo0bZVBZaCuFdTk9bHzG6W8mPw4Pvv+weQ1AM33X1/yYjQytPjXlx8meQX5Ve34/XWkUnz/w2syWvr7H77RqVvnAtxmJAalfn17Xj/JwoXflkb+neuPkOrDtw74+vI75cbPQ+5RT7jz5fUC7f/9g3BR5R3I7MwF3//wj8hCg7txEtXNv0T3pwfhEIYQ1Okp+A+f7kb+eTJ9KvRB8x+zLaBb/4omcPk7u0+Tp6H+Ee27/f8L6STKYBC/W/zvkvt7G6Y/Tn76h7r9sw2fJv7XFw4kMOEq20nAl8mvb+phtfzpO+/bze9+/g2S/m/JqHlbuXcKb6mdRT6om7e3n76r77e/+/mn79oCxhqw07e2Sv4ezb9n1zufP1jwuer7P+6F/M9ZnOV9NvmI9MmvefFv1W+vE81OIu/b/frL5Pf5Mn6mk1GJd6YPE/wuZ2oo6+/s+MPLbxAjMqhN694fwyz/93+fyJFb5XXuNxPVzdtmAh3cRCkYhT+FUT2Bf8fcrgC0ax1Bwz7XwfgfPTxKnPuTX/7TvaPnZ/eJnrOiaN5GXHx7IN8bhLG3d+R7e0e+X14nJ0g8r6IgyuxkorCHw9fMDgBEOci4qMC4EkKKMzTgMwSjz+OXSZRNfvmX6L/dSb0Wwy93GI0eOKUsxRGjarjyddRTD0H21Mr9QHMwSXIXiuRHEGA/Qf3rPOkgxo02qeMoSSZeVEED5NVwpw3t9mUk9ssvvzh2HX7NHqCKTR5Vo57BBR/iTD5/hrr5SRSEzdcMuGE++e7X376b/L/JP9t1Jz7yOECAf3oFSrhR97sJzLI2hcugw6CLIYTcvfLrb08LQzKwXk2gDyM/Ao/NMEpj4L2bW12zn1GCnDgAmhmaOC3yqoFIPYma14noTz7khUzHRyOWh3k9VrgCZB7I3AFStaE6H5aEdWpSw1Cs/eHTpK3BnesvTmXfRUxhutvNLxN5eYCVI0/gf6OY90Vwc55F0PwfwfC4D4lU39WTxTuJ18lujMtJYVd2EVb2k4dvP/wCK8b7dkjcnmSg/5qNZRKMpronycM8wVjNI/fp0s+jz8diDBHBq995B8+K701O9zpXfc3qZwLY1egKFxYEyDRoI28sC397hlQd5m3i3e0HJR0pPb3gPb1yj8HlP+sPVu/9xe87C27sLL62KDLHJ//33cioAysIykpgTytustqdFPNh27GNGn3w6LxgUzCBAfbIo2+NwjvMvKPt1yyJYKBUw98eK+8eea55IFhbQQMqrHKnD8MB2nake4/WMfqqaoxz+2v2DuufYADcMQzqD1Mbhv4Yce8Mx6fvkoYwf8frbyX+7t3KG7WHETkpWieB0eID4Dk2tGgTjpZ+dwYMXTBmXx9GbvgHrSaQOowQSH90QgTNCaH/brpdDtWEyeZXefpteTQ2TlAKr3WhtLBPBa8THSbNGDg1zFTY/YxroBW+u5OapADaGIr4YeE6tIuHMGNr+xTQHn2Rp2ME/M4Dz4ffwvwuyyg+pGp7dgNt2Y/Y64Hrw7Mfcj59BYVNx8S8b/qju5+6Tn5ff/72NbvL+AH3MN+TsXT/zjgTmGfpI+pGuKoh5KTgGUAwEu5V+vVRaB+V/EOWL3/q57//ay3/vXSe/+i5L5OwaYr6y2z2KHfv1e4V5soMxkhUgHqsfJ/HHPz8yLLPkNHn9yz7/J5lfyD+sNWXyV8T8A8knpH9ZTJ/RV6R8ZEE2Yyh+/xAeyw/L8zP+Pj0a6aAb45+RsOIt8kAS+1H8XlfAitQUIFgXPwoRvVYw3pYNu/oC13xNfsIhmeqQLzIgrFy1vnvUvhehaFrH577KBLwUdZA3t7YvQVgnG2SUfwavHzJ2iT59JLZKfjXZpqxFsCIhfYYhyGYPbAfaiJwv/rojcaLPw5097yCgODlX8b0+jQZ+1gIgu8t6afJ+5Bwn7yyFk5JP43t8MgSLoU/PtZ+TIsOeIGDWTMUo+yPyWfswp7d8Z+FGLMKSgwVqUdZ3tN05PgnIvBLEIDqz0T29y928sQKCOcjcEfNe4a/x+KnCfQezDyYTBAjW7jhz2wgnwqULSyL3qjuN/t9Uyt/6PLb3QzNY3z89eUdM54+eLaKcDlMTpgNsDDOYKRChvD6EVPw2f+siXwSgVAH+xdIhUZtHyD43PccD8wxj6Ix3HdQBkcpGyVp1Kc81EVRm8axOeoAHPUB7TFzisBxh3ZIHNJ7hOfb2AJEo2Cobbu0S81xj6Fs0gUY4mAumKNzj8IAQjCYT9MAhzb62AoLpPfU9qHdaMqPfna0ylPpX19Gll9e1ngtso/PcsZotqPPHCWUplUyvV4x8oidCyRN664yxOl8rbuGyKYcuLm8ea7ojROrTWnjF8ktFNQzbXaWV9O+m6oAVYCah8eMBHxv79lYzjzUS0g/1eIyKiXFVlF8ZQ7G3jtYaqvsRCvQGceQQ8HKHMTQhXXcoMtmLk4LQy1s4aCsLd7vmmQ+s+S5sBWKeu5dZEXdekEqzEgBk+x8VeqYAc67pkdALQ6NjW9ZR3Rszaz12dq2pY6n95ttUjeFZaT6svWFnFlvatTPLJrZGwXNmLrbGcRsJkgHY9uv0kIRAjyfW6VW2pzWwt4k1ebL24U/M8nRnfVpz1/PaMwNnn05lua8uoHDGvDL4+V6YHMxlRGkcTNr6qaU5fZZImlNYXaOG6x5T6Uk3pbnUqtw9mkRZnNS0ldVbmyrbumUBxtHg/kgZRGI9ZlG6SQfnTuZ5svYjskNPV+DHRmH7s085gFNnJapbglKpey22rFM+faabpyDllxwOdvXO1p1LioRKph17NFzzcNKkuiMUmIKzyHzKphJt42497bz5SY9kANuGtoJFuntsUGOnHf0dcSqJZ1z/N3R1koGJ1RFacz6cOosw55tiNu0ROpOVeJbHapC2eO3GPPXR64kAAH2NY26VZYd5XB+WzIu3aKAQgV0j7kL51BdB7kS5lM1sTEswreZK1yzlW6tOsMMtfoyqNVe04Pal2ZL2m4LuRdK2fCiQ6WyN68s67L0toZt4EOPt4uFFAomeaw3s2S/PIYh4w6hlpT+MQIz5oLOzaG5bDOE2gd5fa1v3cAIWtiHYnpMGJ7XUjVJUOaUINdTdlrJ09NZnjJGTMk0Zl7xzCCmywuQzenlOltxFDesXTLYHrSZKXYn0nFnp2rG4m3oentqzqrchgpb3Sk4vLEH+RDk8VKjW5taxXitkKrra4takC3lupXCaC6CxYktwqMU6MGxbEBRiCTBrzOZi8jF6thfbEPF94E78McOdwMx5bxtXCwvqrvdowAVE/EiRkINblp4psnS1jNhn69XCASrxOjb+lIx11sRCxSxWK+6jYhD0x43ZgyWx806TCipIfXrPgj1k0zfSL1dVsSmj9IZR4SOU28stJghM9wvxU0gKYVU4LR4pTiPLp015QbD0V6wZoqoVR6tmOtVRk9hvTN2Jslam4W2wg40jHnB7zZTPJ5aMLKv2yjmO4yJF14ursUN5R469XrZS1PXASsv3XfZzaAIWeHRHTEnS+6gSJrOiBVDApiKGKf6vYr3Zy0DptOgZ7AQRbsT0thikxU4z8uT1820YJMLgpU7pyM9DZyoRi+J0FqtqW4O+zijeM056BIqzRk7TvpIo4dZvFTEtCpL0ZujqL8rGAgxa00S5XnL8dhAa8eqkqrdtc/U7SBHbb+ppL7jZWGexTzHEJLipkyaJPJVWrY35Xb2FunBImdVWF9Jz3R9dXOzyKjRFl2HVAZRhwgNBtheRdwSDEu0GzJzA4OxJhVmjasUuKX0bLo89J3NWDMlIHwZVHwUBc3C3g81n+3I2+lyi48tdVNNqoRUTisaLNJuQ3IbJ9M6G00Qwc025OBAc+9lJfVsaxBuSJdV073j12e1Chp6vtP4orbwgOzzgmUDsSEv+onYkcWaZONaQHGXjxebZdytyErkG43bojOpTYvD0bCXkq3FilbC+LLKctcc+b1b3xZXKThHe3Gghj6SNdsA64XrTjn1tijObU1wiuKAkKX2DTZQPG+XB1X0OIykuqxA3VaS0e1GiptiqSFYh9MVfeLoSq00kPtcVgdRYdJL3x8gNc5jlIHiFPksmjOV2dZrA8Pm5H5tcLDGMmsDRViwxa7qvBYarLuc0Y24UOvlPpFJhRiCulkub4kZCbci4MSbYSuw1cu7aB2s4gDCxkwZ0k2CKeFgx1uVYUJNXe021hLZnvD18oxswsVsu2KQtEl2/KUM6BXN7y/FBWWzmSuWJkkHEJ+2vdDsurieluGgJieS3JF1xnfZ+XJMcmWQAcVeqcLZFdXWQuZ6usuRyklspFmBkqOPgizu88ghVeW8srEcv+1XQ3Ol7LLmVnLCV3xLbQ4pTQGr3PR8UApd1Xsu0wg6eeCEPt2qIr619L4QB6Nl6M4Ldxh3LLZnB68w2oq4gQl4NbUlu5VIDmk8Gj9vaH/YrJXL8XiNEQptGedqDmsOCfT4hmo7xz5x8ioHjYld1AgLF8NpG3o0uKmLQPbaulSRlSClaitMpThUVusMpwlWtPbnlb6MTW2lo/oZyfc9scXCkxV1B46w9HI11aTd0jKKIE3w3AttJ4v4edxvtRyPXOKAwRmBVxYKxsZSQPWZcAsLxCZSRDldWQUx1bRD7FKhKWy/k5M45plDgKai4TjD3EnnCYqWRhxE2rHjzAOja5Eb7U4NljMr8SR4aIVoBkadMAFWhjmhl5zf6usCO8YEz7q8LnQaey6JYJYNRUDxiWcO5TXb9Jc2QG98uRhqfbERm1W5cdMFX5+XXCwtMkpl/eaiICEdRWa8dE4Y01CdqeXSxWlN96LdeoHVzkHdUq5x7sNTeYIwXi6Laj6c5dnsgMWNQw/1LlJ31JltbyistnS5Uq5OPdvGu57MBPTGEHGVpNNsF/tahKdq2elzjEh1ASjxNcid2jIA1rORJR63Jmda5B4jKlHpD2Q/1cv+5pzZ2+VsSFeyHc6bUrxW/aph7ctyLdCOhVbkeq0CUZ2HnCqX58RP2ZzAmAFHFuuTghIqUnXJkudOrEB4ZVOzU0WrF8HA09rsaucxfVEvgSdb6G2Z8TtsCXTc3SpiHS4MMkib/rrvw3DZDFcRNgv2aSo2biMluxxjNtKuF+jIXyLFjAiul+GcrQSSaCT8ClqSU7xzsosyQcCjsw32VqWg13CVHyXVQggdwPTch9I2S6OcS0/Ncn/LFM5HLmZsKpygG5aNl6haH3o189NVs5nbOlbwum0c/fQqAttS2ewiqS4cGI9NtmrwrbTAuil+TKktsxJWN9EnuH2u0p1O03q9qT0P9Gx6LIxVdtnNSdIklw6j66owh3qQ1OV01UxxlbXqHK/ErvJO2+WM9hXpmE6t1W7do/waWaQ3Tp7igWuJ0WlPOmVgboqLpUJEPOmidNRuTcZuTX55CFvZdqPSX5i43htilVP0eoOjB3ft2WYoKb5rWTvV0cNiu2zVxmZ3NNud9suYRfXYsS+JyU9V4mz5eximhXIQFCE9K9FBnha3CEG9XMbUTW1PSRG1Ij85leq5DBDtJIr47eCI14RwBkVCs4JtgGVCdR3oIdBKs0gz2dPtcMEcTDoZm+aamG64XSNdXxeCKKxyYZvQBa9QXi4kl3qPbY3aD2SLVJYYQh7OvBTMiGltHdaikWRU2W94VTdXRwLQrrSi5A24OUfHd5CTc1t3dlWZgah5QesTWHDrNXzg9WbLZDZXnRnXRNeC5kdaFm6dxUJpiqxxSrU4LpLtjcuFRW8uK7HvddJC11cUFkH5LKNSohLz7alxsvK6KPHWZnmGFSwH190zKZJXP625kxyLW34LWxdD6M3sUPanWzSEtHu7yJW0rkL4TAIrK9EV4zBntLAleUw2FNVK/Ck74LSEhUcotu/pch5detfUaKSwWI3pN2d3Gx/KaFk78w06by/gphMGPltT111/WBdG4VBe2R7CTUkkhyYB62RIGH1GSZVrEPTe0xkvDXCUacBquiTY5dZOMeqS2Z5axp4k5NVmDztBnMdEVJYBaROUxZGV4FRMeRl8V1euK6O1CmW9muakq88kgzjoq0UnUGTk7Ew/nIGQqlq0X26u4aym8ObqLDCT8GwN9t+HTlI0iqsqx0R3s8FynIg66X28y5jMAd5xbQWHWyDvyK179SiU5sn9QWSm6XQ2y0V/xyO8l1Yz8jqLCsLXsLad0hRJ9v4QAybZcQDRVix9QeJ1bJ/WC0Xa1tQyOLXmWvJrsY7PcGjpUJvvkZAlrii+uaxFjmYHZDc416N3bU8Hsl30NtG47Qa9rRWXc4qW9LYtdILctHy+yep9eIroDpxpPKLFOOXr0FQcxYBzqIOia59LWXKWeCmbDR1icFAPBRXUK8DIdS/5DtXlyyloz948ttWbQSLoQaYPbU31RC9v1ctUv+ZSJFKH1G4umNkoU1+qw/VMn9H4Tt8AxMZQVu05LT0eVAw31keiIaYhZUVSjXaOvU53ygFdNNZpf4MzNEbDtrkU8baVuZswM86udXKmVXg61PJ1dTTw0quZaOrUMmYT0SKiwrOjq74iwKHIvDDQ0ppurl0+4HAs2UyZyItrJgFutaFIisW8oNsjGZf1OSriBgJnIWqI5RO4OrIONh6Z3pbElVo2Jpxbz0yIevMZf7jh8poLsZXb9sx5Md8UOoNNDeEmsXiHyjtZm8YBYk8ZuV4HQY/15jZxpn685cmLVaunG2MZqorY6Mr3ujZsSkANlJXt5ilWE5ZEjyqqPoPvB98XBmRGnQV3U7X4rKeQQ9pOVyRaORvKs+FkwVxF90i0C/w45V1W52pXELq8Z5nOYU2HZ/iCGRwfSyVZz5n5rjePUljU++lFIAyLc3AJ8FV8OxkAjhxzfonsmXaoJYXwnMDDWyrIbuyKU/YGSgQaUXvX/MJGgY8TsJ9hGXuTg3U+c+OhJCH2HOD4xGzb665dHWmRArADVk4+6jhMZi6slsRm+zYDPoDNy7VbhVg7bbFzDs7HzgY3STA6vvHRRDDay7E8VGlLMdSmNjyqm6MsTqAYeZjVbefQsNA1M84xzM7XdI5WFEIhoqUtL07FWcMOU3vWSiuszEwlRzEDY3UfYGvou+yECAsVgg853afZvj8r+bzEYe+LXY1ExQ7LHZM6ilcs0Tm+QvDjWS+bqmFhF9Xs67UsLBDpzLsI2wpGWh/TMjk6yO4mgKI5YF3R7uX+QmoRIi1Xl5bMkBYUJnPhcHfPULvSpjliOr3V617cNisJwgnbybN6n2t+wrb6/CSjYcZ0YsxO6QqlhRjOSQxMCKuka+bg4hFoNp67dliMms0X0kWmpkbQxee5gG5PKuNf/YWfEp3nIAepQ938tGZvi9rpy6WG2ZGgY2VXnC6mU2bUcAS+595620QGet0Ffh5td4Q10KJsbZAVIrGnhq6CihFVLU4jA9gzv+J7o+vsI3WJd+tGdd226Yn1rF+tW5vuGlh4WfbHH18+vYwn1M9z5r/2dnk89vtfO318HBS+v3m6HzID2/ty5/XlL8r186eXyo2gVI+z1jppg+eh5H85af38L720GEkMj1e346uya/N+Ot/YwfhLSC9RBueMphre6jxp7we+n16cth5/HaJ+ex5sv9zVS4vxlPxdnfHw3K7BW5O/3V+0v++NsvH9D/AiKNLzMngeQH968QborMit3zCSeANVMWr7fA0yHtmO70Fefvv/GNvT6/IlAAA= -->
