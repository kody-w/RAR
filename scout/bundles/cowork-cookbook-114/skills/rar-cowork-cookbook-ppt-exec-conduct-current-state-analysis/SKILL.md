---
name: "rar-cowork-cookbook-ppt-exec-conduct-current-state-analysis"
description: "Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_current_state_analysis", "rar_sha256": "480034430f13cc7896ff3ce1b2cd1d47345aab7dee1b529faf8dc58a04dd4eee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_conduct_current_state_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-conduct-current-state-analysis:03be078aa65b9b018e70af3313c2f01fd3fdf33e457a38b7d372b221c1c43050", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_conduct_current_state_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_conduct_current_state_analysis_agent.py` is
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

Conduct current state analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 480034430f13cc78…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_current_state_analysis_agent.py` first:

```bash
python3 ppt_exec_conduct_current_state_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_conduct_current_state_analysis_agent.py   # or on stdin
python3 ppt_exec_conduct_current_state_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct current state analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_conduct_current_state_analysis',
    "version": '2.0.0',
    "display_name": 'Conduct current state analysis Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-conduct-current-state-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b7459c06cf57262',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/conduct-current-state-analysis'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-conduct-current-state-analysis', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecConductCurrentStateAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConductCurrentStateAnalysis'
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
    print(PptExecConductCurrentStateAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZOjxrbnv8LU+2D7qbrZt75xI0aIRUISkkAgIbejmiVZxL5JAj//75NIqu72s+8d+8V8GDqqCpLMs5/fOUn2ry9O10ZF/fLpxQBOjihOmsYRqBEn95FZcS3qBP4pEhf+IF6Rt3Xsdm1RNy+vLz5ovDou27jI4XIF5KB2WtDApQi4Aa9r4wv4UAPH75FtcQX1tojzFvGBlyBFPhLzO69FvK6uARxvWrgYrnXSvomb+2PXvMJpWZkC+OYatxHiRU7dNnfhWidN4jz8UN6p5gXk/BEKBW7OuKB5+fTzL68vMbx/+fTri5c6DRx62ZatBEWbPXjPHqyNkfP0yRiSSJ08hHPLHhomh88lqIOizuCQDwLk+fRjA9LgFfnP/0yuTh02P336nCPP6/PL+E/vcqSNANIWTtMCH/Gc0nHjNG77j8g0vTp9g9Sg7eocqgO1raEuHx8rv1EqSuSf47sfH0w+hqD98fNLUY6Ghlb//PITUtSQX92N9x9HKuWPP31MR2v/+NM3Ok3nngG0NSQGpf749nx+koUTv02NgzvXf0KqD/+64PPLd8qN10PuUU+48uXjGXrgxwfhsi4uIHdyD/z4078i60UwAtK4af8S3Z8fhCMYRlCnp+A/vd6N/AsyeSr0lea/ZltCt/4dTeD0d3avyNNQ/4r23f7/jXQa5zAX3i3+p+T+bMHkn8jP/1K3f7fgFQk+v4gghUlXO24KPiG/vhlbafbzD/63wR9++Q2S/r+SMYqu9u4U3jInjwPQtG9vP//Q3Id/+OXnH7oSxhpwsreuTv+M5p/Z9c7ndxZ8zvrx92shfzNP8uKaI18jHfm1KP9X/dtHxHLS2P823nxCvs+X8ZogoxLvTB8m+C5nGijrd3b86eU3iBI51AbiwfgaZvl//Aeyjr26aIqgRQyv6FoEOriNMzAKv48gOu2fSf3FWC5Wq4+Z/wWBo2O6Q4hwurRFlNqJUwTmw+jxUYMiQL78b++OqB+8J6KiZdm+jVj59kTDtycavt3R8O0dDb98RPYR5F7UcRjDMUSfbreIE464CfneI6Tpsg+XkTUUK35Ajz5bjLDTdCn4B/LlL/J6u5P9WPajSp9z6CMHOg7iLcjKonbqOO0RZ8Qst2/BBwi3EFfqIk1dB+L6+KsrP452OkQgf1rP+1oRAJIWHpQ/iCFEv8IAaIr0AjFytGmTxGmK+HENDVbU/R3kod0/jcS+fPniOk30OX+AMok8Kk+DwglfBUY+fChrEKRxGLWfc+BFBfLDr7/9gPwX8u9W3YmPPLawRNzNBgM7RVRjoyEwS7sMTmuQMUQgBN29+OtvD3+M0sGah8DcioMY3BdDat9CYtTg4aR3D0GdRxFB/eT0e7sh1wjaBYlbaC2Y783r53wkUcCp9TVuwLsRH4sfpn93+YPP6JPmaUPop6AusvvcezSOzvSK2v+ILALkq6WgutCvY1FFoqIZ63MJch/kXg9XOu03F8ISizQwh5qgf0W6Bqo6Uv7iQtKjcTIIVE77BVnPtrDmFSn8NRrozh6uLvJ4dPwzZh/DkEj9A4wx4Z3ER0QD0JpI6dROGdVOA+7zAucREbDWva+HxB0kB1dkrPBg9NE9u++RN/v3nYX03pt835WIY1fyuSMwnEL+f+hkRj2miqJLynQviYik7XX7EXRjEzZyefRtsJ1AYDvyyKBvLcY7Gr3j9Oc8jaGj6v4fj5nBPc4ecx7Y19UwiPSpfqc/Znx9pxu3MFpG99f1GOHO5/y9ILxCB0BfNSO2waRORogovjIc375LGsHMHZ+/NQfIIxBH7WGII2XnprGHBAD492xoo9HW7+6AoQPGvIPJ4UW/0wqB1GFYQPqjG2JoTlg07qbTYM5Akz4S4Ov0eGy5oBTQW1BamFTgI3IYYxzGaYO4APZN4xxohR/upJAMQBtDEb9auImc8iHM2Bg/BXRGXxTZ6PTvPPB8GT6Dyf+WjJCq4zsttOUVOgHm2u3h2a9yPn0Fhc3GxLgv+r27n7oi31euf4wJCWX8VhZgLz8W/e+MA1G8zh5RB8tx0sCUz8AzgGAk3Ov7x0eJfvQAX2X59IfdwI9/b8NwL7rm7z33CYnatmw+oeijML7XxY8wV1AYI3EJmrFGfhiz8MMzzz488+zDPc8+vOfZ78g/rPUJ+Xsi/o7EM7Y/IfhH7CM2vlrFHhiD93lBi8w+CPYHanz7OdfBN1c/42FEPIjCbv+18LxPgdUnrEE4Tn4UomasX1dYMu/4dy8kX8PhmSwQMfJwrJpN8V0SjzqNzn347itOw1f5WAH8sfMLwbgzSkfxG/DyKe/S9PUldzLwV3dEIx7DqIUWGTdTMINgN9XG4P70tbMaH36/JbznFgQFv/g0phisfbALfkW+NrSvyPsW475zyzu4x/p5bKZHlnAq/PN17tf9pgte4Mau7ctR+se+aezhnr31H4UYMwtK7IGxuhdfU3Xk+Aci8CYMQf1HIpv7jZM+8QJG3gjesFA/s7yBcvqwzXpFoP9g9sGEgjjZwQV/ZAP51KDqYI32R3W/2e+bWsVDl9/uZmgfm89fX95xY7x/NAyP2Bn3qn+ztxst+16T30b6zkjl3oHdDX3vYd+gkvFYe797FY6NxNsjIl8+QewBry+jOesYNubDfdv98hAKavOt+4UUIIp8aMZeAoUJBSnBCl+OmsDS53/HYByO/fv88ebTn7XMfwUOPmGkCzCWcxyGdnkXwznAYk5AkjjpEQGGBz4Z+PARUDTrkJzL+iRLuASBe7hHkRg9ijh6NXOesqD46A+oxVej/0+7+ZcHGVhLCJqBdCgOw0gKMg2gbB7L8UwQkB7AXcLzcZ9iSYp2HCgggEM0wQdOwPkezTkY5fsUAGCk92wkH7K9vTft7x56gAMUK8viUXLCcTzOY3HK51mH8QCJuSNDAvdZEmA0TwYcByi4/uvSp5dGJz7UH8MY9pCwg7uMfH59en0MTYaCM+dUs5g+rhnKW45ro+4tmk/qdHI77dliVUrFDcM8a5mtjms6xzGxUeZ+F06mcSO1vXogNlSrelzDVpQtcvF2mKHqYrJmW04yDgGr72Sl2agqYBt2dYXjmilNjbNJb3LfWqrljF6lVjCzatXYdXZP4GV781M39Q3rksIa7aY6bXTnXaBJqhXELc5PZI8366TeHYjrrooVP02qjEAZJRUd+zjbk3PsFDhDIxCOu5DlU+evzENvVQf5ROzipMysoQz2u0uWRZ03X9CKyk1AfuL4DZnyfGJ4l+ONR7N1caw4K7eOuuIuO7xyTdyym72RVZpHq6eZfM59aQiW7fQoACJsDdd03LNZum59IyMzA9ViJwn6kl+ldj0kpJathqN5go6cNdbAzI4rs1zjetSdGObQ46a+8Bx8WTEyfyoXNbuk1+DWt1q+7EqL3PPMAsP76ggcVap0dV9We3q2RuuNtlEPs8q6Raus1k7JKT+Jbr5IB3nl1fNDT7byPJxvaNWnkyDEhqxsPDVvy0KeTKTmYrhiGTtyUeVTLth5DL5MzSJIzyuj1HE3OTTrXBM1WUCHxSDpjUIwTojXMrm6QrQ3Ii9KuttF6/ZZ3lrlCVhnlbRmiaaHKq6del/SapXJmYocTrMu8K+MRK5FbIgJlr2Yjl37g8zdusuNublzVbYy93KiszXlnzeLSjVoz5EPS3dY9pfDqdK4y1ocypjaC06jep4UHLB5RrXGtaoC5bg+UvvbzV8u97P1rY/sPZptZrsooj0mStMluPYA5c84bvVNxVRXjk8ayiZU8ubFS8JZzGSs2PTd0klqWruYJy2AP+Cwzs72CQdBJ4rmcd77YU5tthSbU9v5dbdtxKU/lLq8DCYic7ttLiRxmyTHg9D7FccK23CHHY5UTVXE1XCyVd9QTpLEnVVZjnScS0GtRo1pUvYtmyeRpri6SJXTaUXPGrlZzbKU6RLxkpvdru+GUDKu2aKsSQGb5bvKIoV0utm5uqXsS0tK5sXFlYxEJxRD46Z1toij1DRvp1xIMDE+dduT50b+8aZxFI9xNkqrm0UgqHSO7YF6m7OqUnLry4m7iAcVNzf9CV1zuOsuaPFUDZeMn2pkb3Ksg1YDKnBRp8/XkWGp/FGeEpO+o5s24je7k41P46170DWr3GQUldg31pS3aeNOfclApcuWm8t7azuogGomC162FpGkpHYaAp7SHFtSl621a9FsEnYSx5G7FTo5S3rOT3jlkPTZkuPERQpj9+QlrQMhFlvXk1I15dBScjlrtGs21POEcuAzXx2Nwq2C3knlDgviq7kW5a2piAUIphqE/yZN7XyVJbM9WqlAOx4SWeT6G7CX2nGRTsrAEHbJPs3MRGHIyTY3J2WxF4k8yQ7kdHZjwdKGkcVjlL0v5SHWj/YMx+n8rLQebcTlBMPXTcUvc/mwy6OjU9GKEg5zjg9S9uD4SrfZtstyzeubriBJxq3WxC7zp7SOZ/o82pqiS/J7W2XV08VR+TkVTwQy49BJvL1tY7FE91M6WINOFHS9itrcMZ2LyFz35wEzI7Q3qIIRTbBfcJ6mHY6EMhu2h6AiKkxpcpVZuiRnbhb7YXOWSp2frWiGF93KcOyGkgOi7l2xnbNT2U7U3SGUZRiIIqpHVtmFWrbou7mQzoxdtL11WSXURl65jky6Zr0/MbPAsRL9UCYOozjLVWCJw8WdXXcGlU7PyXaN2Q1m1EvySrGX9CoYJ3xYMcN1pVgROz8xNn05kXJGRXm5uVy6EZl7qhnsIp30eKgdXYCe+8ut2uhuQl+0eeGJjWkth1vNcIq3Wq8u9eZoH5d1iN0snueAFSQh2Cbd4XgccI7XpvO45cx2La42PH+YC+p02UA8FY0EGMVQXcMrf1yWyVCI2Joksb155hVstipU00MlY2/gB+1syR2FL7iIYadVVsTOTabibAekcsEqMyCJXHV28iabldIUne/75HqiIo9fV8VZYNJsGVTbQdjvy9IO+f6sWO3lBGi1v7pMai8qJz6L3cID1IFhCMHwNxZdO6sZDSPeSbeuNFGEejqsVYpPyhxumqgNxoYrdn3yCEm3+TA/NQTbJxN3aKlsma8zp7txYN8dSGkyDEBZz+Zmop+UqlMrXboAlj5QMZspkeEVJBG01GotpOxmkVBu4XQ7R6rMjq7V8ooWu1y4xXV4kQi+FXaWlGFhN9pZ86+1rdrtDF/BvLMOlLqZwWggI8KzSVVs8HTfCSHuD9YO7fmFKQjMZLvZzch9KgjhSZF1KZj2k1S8HRWjH8oNTl/9lUIbBUyJwpxNqk1rKYNadafe7qRGMNZb6ZzrvODydlb064SL7DmQaG/CpAGbuMZBSqsLtmsM6nqh5/1lTWHYDBgkxD7sNqNPk+vKJ4qOrSLgGGuil2oBXTLNPgkqv+PlQlieBrK5hEx+IY8JF/NL+3oyDpPS9HJeMRJJvsmqRYfD+moKrZILkcBapQ2hIN57mEHaPhubTHVYFAXWVWaxqRfVgVOFapvt5QYqj9fMrt9FpjNjSxIlZL6dcavQ3SbeWR56a+fVAu2T3iaK5rmZtkd9dxIDMil0dBJcVg55w67dUscrT+yumtiUWCPdOHa33eTaLZAOB3ZCr7uUAGftvMJOcGO0cv2Mv8pR7EnGtugtmkiv/SwUkjjU0rDrPJqc1SlYTVFdKQxXWreiFOg3pxvMW7W+1aoU8t7U2m93JkP35ARcueutnB1as4oF3Hfg9nXuCTtcm8osju+79gAbOyUhB9hRkDWDa5i8n9rX3GvrwXI0Zylht/m+MsIdzun8NeyP50gXxEu9xmfJsFHyTNpgucwRAS5fknLdttmFV0+dSSTi5Jhu2Zliu6rh7VzHTXy97nxsZ7BFxKRe4RibY0lRdjvvxal6rQ4ZXV4bfibAJi+sl3lSFWS2x2cbNtfFcy50xikWFXt/vfTWaZXNGZnNbzMmYU+ZTO9NPcbm+MU4lme7uiydjQXrYRuyGRcd7A6nyN7Dw+MkyjpFmk/P5XzbM1P7rKVr+brdsFdJSGrrpiXLPeiyNmTQNEllJ5+DTUfB5DlKvcUlLVj2KzY3LD1DM1vlJGK/iIrJOTE9I5UoyYnZmUAksbpmy+1SiJtUiTPYGxrmovN2tDKEqbmuc9RSNHpmDl1rDWDlVj3I7MWVgtVtsxMP/PJoScZC4mF5nO6L+cGYOit94auEP3MXLmEuhxIQsWncsGmaimGOb5cHpm2HXqhgS3yt5sV5Z6poCuyNkZ1313UwxOvDZLlkmRYTL9qmn+96A5Ra7uVLnkkutGoawqaZzH1YFbXGYGAv3ZuLYJMLValLoby9mbBbqbTVSTn3p7A/H4NrN73l5XwebAtut+tEP2folPW1pmH9g76udufpGV1lh4N+WM5YRnf2ATOpXGA3Bu6rnjBjO2nfbsQpQC/yeTMUYcPqAcjqaB7OTodJct44ajOX5SwB6eS0pHfYovE2ob3ZTg+qMl8P+1V8UU66M7MXepurKX/CchvNsJ1mEQALV9XWs1w62RmwXK0CYifsZ81SzkRpQgw1xSmJaVs3PTtwSkQlmF/i20EWje1ybbCbOq2YZVz1Anog99WkkVZO6G8D0adw1TKPPRAXSkh1/oJ37A4sJ5608HBqW0XswppEc2dYXozaqznxzFMNNa+JetOiHb5hM6mi0y2f+vO2j3gDZVa5d5S5jb9h/TSkIGQDaXJLDLld7Vj8dmk3kbXt0jXGbqKwSTgh7TWYG4D1+A4mSqxZG1Kn5xNl3+iK09lmf9MqfztH5XqRF6HciJli4XS3DdE4w+v2EK4VMkQL3gOMjOb45rg/2hSqsxW3EcIJtSG0c1A7FhfwJwdszmuyYdhVLNSJwPnR0Olspl40PN7qLHVBJ+TxiE6PZ8tRcv+EouaWY8EB59n60lZ8txa3p2NO7yWykfG1ZvuCTh2Saxt61GqecjON2N9U7ro19mKBLfnUitbEVUnn5zxZcPHmup25pNDIN2NLNeeCJtsuS4khD7xBCtueHtqhcLbaVahXB2OpDxW/XRo8pZ/VmSuQ00JtrsMkzlWux8kbvZv1Mhloc1WcrPQYdNfe2dtDEA+NtM0mLHO9JC4ugtMhaVIQqXNC67aEzvvUTFzoTUMn2iD5+fnGrHDMZVMGbjTwSYkyt0mux+Gqa66TMDtO424Q6HkArSUQ55rO1WbZHR3OXwsuLijXemiG0UCrmCTOm7pWhBMbVEuwKfjButFkr9iUulwLWxLQdCPMgthr08V612rKIsdAux6IxQ00AWFxBDeb2nNHjYNLeJFhD2fl1QRMptSWXMxvpLz2JpYY1lGwU8/sZbm7aZPFwW44g8W1ZD6Ea9m5ZVxRs2JD1pyJkuHV28xtPWZEfDe3G7J1c+5AXxZhGG7XcJcOpJB0N7d1M1/HV2VhL3ue31ZLhxFPjbEnuVM+0zGJUy5Ei4UEuvVLK14Q3N7dgAw2VOu1XLQTc+VeDqjtFKIqgA1JSAGF98oCPUqA1ercJ/ZBp/WMtJGC4/Sqogw1wSlKuUUhy3HrU9bMpVM+dy5ckGd2SzP1qknDuSjYWqtr/ZJUyHLPMewiP2SMwsK95rBY84CplQVM1+uSP+6vOzrEpgIIsP56YkoeL8/TOAymN1Q7F6hTJt6cQkHSn9kStrf1oHPrCb7pJJNbrAyWx61doKAuG3IzuiMI9NwlAPXwGq3lhch6HEq0Oy4RQYyKLLGlDtmFlAeNi7HVmaHcbnKJ0pi96HCfMs8tAhVQNHWHYLZw0Qu1d4HBontJVBUyUrKFUF9x+WyRdk4fCcw7L0v+ppxd7QhKmqcPKDF3NNGw5aUxWeUsw1i0cFuJB3KOeV1rc/2BTfC8Gg4Ck0121e5U97CBzIkJJQBxQjLT3dU+ms3udNGNwvccbY2bJjFx6XpZtijZlGANNFSz66mtGfxWR097djs312CIuEAV/MNtC24T/kpfBZua1hFBHYircJ2c5coSacOFBV3YkJudesspU0u7/bzaYUPHpsWGIbXtebVY5+QJzwR04GOMgc2lCsSOyq3tOtLqFJsbKGEf6NvlejgFHH/IO6GYLVjaMtkCS5ymE49yjhWYtZ2YmcmwNGlPruptsgmm/E7yvJVYsjs71su62U1zlzH0OaebdbVdVByGRkcZ8wJP9oe5aNPkicUJ5XjkQIguUGzluh7c5k//+fL6cj8IfvmEYwzLv76MJwXP7/3/gy/F4RCXb0+CJEthry//7z5dPj4jvp8L3j//A8f/dOf+6W/L+svrS+3FUK7HJ+Ym7cLnR8v/9qn2w1/8ijwS6R+H2+Nh5q19Pz1pnfD+rTuGq5u27t+aIu3uX7qh7btm/K8uzdvz2OHlrmJWjmcY7yrB26Cogec07VtbvD1PO+J8PJ8DfgxleD6Gz8OB1xe/hy6MveaNZOg3UJejts9DqvGT7nhK9fLb/wEnF9l50CcAAA== -->
