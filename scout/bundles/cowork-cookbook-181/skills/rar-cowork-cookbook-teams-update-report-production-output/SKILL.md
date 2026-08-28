---
name: "rar-cowork-cookbook-teams-update-report-production-output"
description: "Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_production_output", "rar_sha256": "13402b2c177b74fd64a6de9a71836f2ed599bc63465d2602f8a31fe7629a855e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `teams_update_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Teams Channel Update — Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_production_output_agent.py` and embedded as the fenced Python below (sha256 13402b2c177b74fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_production_output_agent.py` first:

```bash
python3 teams_update_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_report_production_output_agent.py   # or on stdin
python3 teams_update_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Teams Channel Update — Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_report_production_output',
    "version": '2.0.1',
    "display_name": 'Report production output Teams Channel Update',
    "description": 'Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f11de26cf197494a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateReportProductionOutput(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReportProductionOutput'
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
    print(TeamsUpdateReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716e7ea2LbnV6H3/SOpS7JFnpozzhiNiigCIggqlRopHouHPOUN1fXde6HundStU7dP9ejRJjtbYK75nr851yK/vVh1FWTFy5cXDVgpwltxHAagQKzURZZZmxUR/JVFNvxBnCytitCuq6woXz69uKB0ijCvwiyFy1eF5VUlYiFHYCUl4gRWmoIYybOyQrIUKUCeFRWSF5lbO+MSJKurvK6QsrKqukTasAqgUCRMK1BYkKIBCOta+f3L0ipcxMsK5FaHToRAJSwfvEIVQGcleQzKly8///LpJYTfX7789uLEVglvvdw10XPXqoB6F6+8S9/fhUMOsZX6kDTvoRdSeJ2DAgpK4C0XeMjz6mMJYu8T8p//GbVW4Zc/ffmaIs/P15fxj1qnSBUApMqssgIu4li5ZYdxWPWvCBu3Vl9CB1R1kY4OKqH+qf/6WPmdU5Yj/xyffXwIefVB9fHrSwZVsEaNv778hEAPfH0p6vH768gl//jTa5y1oPj403c+ZW1fgVONzKDWr9+e10+2kPA7aejdpf4Tcn0E0wZfX34wbvw89B7thCtfXq9ZmH58MIaxbEBqpQ74+NNfsXUC4ERxWFb/Ft+fH4wDYLnQpqfiP326O/kXBH0a9M7zr8XmMKx/xxJI/ibuE/J01F/xvvv/v7COwxSU7x7/l+z+1QL0n8jPf2nbf7fgE+J9fVmBGBZHYdkx+IL89k1TuOXPH9zvNz/88jtk/X9ko2V14dw5fEusNPRAWX379vOH8n77wy8/f6hzmGuwlL7VRfyveP4rv97l/MGDT6qPf1wL5etplGYtxIO3TEd+y/L/Ufz+ihhWHLrf75dfkB/rZfygyGjEm9CHC36omRLq+oMff3r5HYJECq15gMCIEf/xH4gUOkVWZl6FaA4EJQQGuAoTMCp/DMISgX/H2i4A9GsZQsc+6WD+jxG+Y5mH/Po/nTtcfnaecDmpRvj5Vt/x59sD/759x79vD/z79RU5QuZZEfphasWIyirK1xTCW1qNgvMClKBoIKTYfQU+QzD6PH6BMIn8+m/x/3Zn9Zr3v94hPXzglLrcjhhV1jF4He08BSB9WuVAEAYdcGooJc4cqJIXQoT9BO0vsxiCcTX6pIzCOEbcsIAOyIr+zhv67cvI7Ndff7WtMviaPkCVQB5topxAgnd1kM+foW1eHPpB9TUFTpAhH377/QPyv5D/btWd+ShDgQj/jArUUND2MgKrrE4gGQwYDDGEkHtUfvv96WHIJoV9DcYw9ELwWAyzNALum7u1DfsZp2jEBtDN0MXJ6FGI1EhYvSJbD3nX99nMRiwPxvbmghykLkidHnK1oDnvnkwz2OBgKpZe/wmpS3CX+qtdWHcVE1juVvUrIi0V2DmyGP4zqnkngouzNITuf0+Gx33IpPhQIos3Fq+IPOYlkluFlQeF9ZThWY+4wI7xthwyt5AUtF/TsU+C0VX3Inm4BxJBzzjPkH4eYw77fQIRwS3fZN9prLG/He99rvials8CsIoxFA5sCFCoX4fu2Bb+8UypMsjq2L37D2o6cnpGwX1G5Z6D6l9NCI+BYvkcKB79HPla49iURP7/Tx2jqizPqxzPHrkVwslH9fJw4Tgeja5+TFSw998X38vl+zzwhiZvoPo1jUOYD0X/jwfl3fFPmgdQ1QX0k8qqd/4w6tCFI997Uo5JVhRjOltf0zf0/gTdcYcqaC6sYJjhY2K9CRyfvmkawDIdr7938nsQodkw7DDxkLy2Y5gUHgCubY0+CIqxsJ7OhxkKxiJrg9AJ/mAVArnDRID8xyiEMEIQ4e+ukzNoJqwpr8iS7+ThOB89ogS1hfMneEVOsDbG/ChhQcIhZ6SBXvhwZ4UkAPoYqvju4TKw8ocy48j6VNAaY5ElY778EIHnw+/ZfNdlVB9ytWB2QV+2I8S6oHtE9l3PZ6ygsslYf/dFfwz301bkxzbzj6/pXcd3VIdlHY8d+gfnIDABYQKPODqiUgmRJQHPBIKZcG/Gr49++mjY77p8+dOc/vHvjfL3Dqn/MXJfkKCq8vLLZPLoam9N7RViwgTmSJiD8tHgPj8a0OdHqX3+XmqfH6X2B+YPX31B/p6Cf2DxzOwvyPQVe8XGR2LogDF1nx/oj+XnxeUzOT4dYeV7oJ/ZMMJq3MOO+t5j3khgo/EL4I/Ej55Tjq2qhd3xDrIwFF/T92R4lsqIOf7YIMvshxK+N1sY2kfk3nsBfJRWULY7DmmPPUw8ql+Cly9pHcefXlIrAf/m3mXEfJiy0CHjrgd6Hs49VQjuV+8z0Hjxx53avbAgIrjZl7G+PiHjvPoJeR89PyFvm4H7Fiut4W7o53HsHUVCUvjrnfZ9G2iDF7gDq/p8VP6xwxmnrecU/GclxrKCGjtg7OPZe52OEv/EBH7xfVD8mcn+/sWKn2ABQX3symH1VuIl1NOFM84nBIYPlh6sJgiSNVzwZzFQTgEg0kO0Hc397r/vZmUPW36/u6F6bBN/e3kDjWcMniMhJIfV+bkcG+AEpioUCK8fSQWf/d8Ni08mEOvgnAK5TAkSw23cmTKMzZCeS5MW7YK5xUxnBO3hwKXmc9uhCZKmXJzGcG9mEVMPMDQ+t2YUBSC/R35+G1t9OCoGMA8Q8ynuuASNUxQ5nzK4NXctkrEsF5vNGIzxXNgOvi+NIFA+rX1YN7ryfW4dvfI0+rcXmyYh5YYst+zjs5zMDcs+TWw1ENEiRruOoA+EnusR2kz1vTG77UuyPixkPjzm64tezAQ70qqbRV4FB8uYvSSzHmZMLmdCVIYl5alSvMdKycWWi8reCLibmiBN4yTX2K16m+sXJ9+td4ZA00dNCEBSZDeaS1CdWAddlZtUcRU7z9zstCz1vCY2lCUTl4WwBFnKad2RN3xR7JlSx6P8VKnncx1nYnKoXYO+6ZEYaORVMxbevBXKShc5LCeqC12rqnEDxi6wFJV292kxo720ICmvH/ZnpqPmJykjbr2hsR1GCaeDa+t4btF4I6qWNfXjZZcWV4EJqrZYuie+4CAjKcDPZdWiTiaIsAD4Bbtta40ydjHtNok41WtwM8UTvSxPwzIrRD0sHY/R1NogbyeM8MOwMk7X/GbmgljsKKnu8LkNOkdj6oRAeXtHnUVlvWmNRGhNIUm3Q9+QWJtebrHORyU9CTJLT03aTrfxsBacgjj1xDVR/L3Za0whoN1NlVyHOiv2ktwMlBZ2YokmnGNsuZCXVvs5uBm7DXnRsEJ3LWptb3bD6iyQSnA1wgO+LChZpadXxshOQyAcz4WQR03XyPkBKNbkmFCn5WzCzlzdOkwNNo30uHdZvKHomKZ60cRrsGJ7iXBETOxxipwckg7PdNEugKImre34BqDqIE0urYpL5JWtEt7enq6l7qKWc7Zs4aissSOY8sYy1GzOmtCdfDrUg996c6e/9N11ElrKeVmnzHpdZeh2Nl1FekbuTnvStLVNpKRzpu6SrJoaqoEreRk3q1VHz0TOhpKWayzb03VW3y7T6ZzQ1+4J29G3HP6gdg2S2vPJ2SSzvIWtdBelnU0WQ6PEJ4G89VMFXYgzOiEmLbRr27Bq54INtrQUkTFK1b6YsramTq6s7dTzbrqrNDEId3LU4jvRlMzC5rKAF/Wc5Oqlw59ihtU62tBvm4sT0v6OP+wBxdpH3zCogO4Ovh4I4WK7xHX1MJXVfE1GR+e69+ED4qTtKF/MBG1dnvTBTINO2nCNM4nVelOhfHlO+ei4UYHac3rkBLxQZwEnhsK1mJ2ZKDjMg5XjydL8aF8qyb7JSUxOlsTUEhyfwfnJMOHsqOv2uoN7i+4Ewb9Aj7tLc17z6+CwnTB2L9xKIWg23MDvrbYhK9OapfuFB7KLJ2PGWpmcV+1p1ic6MGbaJlCJPrzqt+ma3njGLNgUw8Td+hldurzXTDoxl/KwURaJYC685CyIC7SuLGeKnrByWVtXLfRRpa4IfW+SGHs7LWssj7eU4WFedLIBu1u4R5FjDgcQULPjMSJD+myEWi212wrdxjR+1rb6ZLKtBC6bWjeRXpPZojO4k2ANtn1CUW9BdY611htxK7s7/uTGOcANvXXzYK+rniAYqpgeE9ex8CFebTPRO/XLlKCc/XkB1u5e9AmLLu1Bxk+VUGGM0E3y6Sq+5fSRRwlBPh/6niIX0fl0iQCL6vPAmU6yuDRu84w4eAGNcTIzn5DZsJqRC3KO8mzL+FUcSMUJzmwLslUa7eICOpI6zeXX3OmwI4tQXWT0TTpIGu5S/bo+CriZklQEFkc7LDlK7ufXbjIPzSipNMxKmFSn5BQf0n5VL0KdZX2x1vnOExp3myRzRrJOx6htl1wumnxxPIpWlZwI2+3VaGuu/R2O3fyQITnzYpx6gTlelSXpaNh6G4aehOmDFfnJZB/64R50a+egR66DHsoLP8T6qcOrQDFPZm8CzkzTM8Ew+2HWgWrQo1it1DwlPBItLl00ywlhOJlKS26kLFIUvklbsy39GsXWbuAkO25/ghUd0TV/7j1xYRCTOXkrm5yb6U0fZI7pnptbSQqXhTZb7g2J7qjtdV8sl8PUuSXHva9sBw+osilnZUQsVXtxE2OaLWtRzm9kdlusTSKWzxnbTkNbzxRW3x3bZL1xsiPJgVgydVcnJd8V5iezuvkovU1Vg4gimZXyjZUSfhH75w43B67e7yxdXW+OC+eyqhYBsa1OOLkT8zoW7PZyKqdNd7vI0ubib7HT+Sqf66zMZop7XUhcnww8wREcv6UF1IHNqHGi48XRSIoAtomnfDL3iG0b2zMNqJgfusJWty24wY/sTX2ckVUnd9c2l4ViIhM398pq02vcE3umDFQYwkSqpGiuObONs1yvteu2C0jLW2ZC6zvozmQyLLaPCyHNLIWxT7lh+9lMOOyuuU/wMn3AdCkE25Iv6n0ooudgX5pSTujEYTie9IXqXSAv25/iS5vM060pYKlFQ8NOq0PO3lz/YqFFnev8sC5u0lxqOPIw4KuwGy4TM6abow7BfH1o5GZp1Up53KEMzKJAyNNTJ674UIdspU7yNHw5SY9WvT2fBbzwsmk8lwo4TnDXs6iVq0lhEXuV384qWlGXXJE2wiWYXhVsE5YqKCVnFlS0y+WKCifALMt3Cuclpl+sqEBaZSus0cjWL6RoDUu1tafczdBLVVXz2e5y2xcSBKLFkp7c1PUcyPu4oQ8a52ukssKGCSNWAZzmWCWx9pqWDztWyLRZgmGbLe0ONwsXtzdlkYYi1g7zPTG5MqxjXaolaUwX2AWqyIXgeOEvbdq4EUEkYj6lnITQ6cbshnUvxzqoJvXKcZYtvFzshlI9A3XLhuBy2OkrzSTT4lTpEbnpsH0klFzvSmq7FqcoOFM8OZtf4tuCXJ0O08PQGLurNFnQm3THVWQ23a43BkiX2ZqI+za7GQw+vSbzithBmC5Ou6l7I/iT568b9qJfvcoetC1fRqHFXvOptFjydsVNLdLdCVunDNI8osxWi2+X9d7n+fh0OCZRks41Zro8FoWZdyGwY6NiZ0anoR7YbFZid4qzpFuuHN7B8x2+vcXnvT5IG7htnQVbR4oWArDoVUwtxV7Ec2Zn7ayopTbnYxRXw02L+POti83axyFEzbS6nbWR65a3er73OI297MobnM862TYMuhNu1bl2ekfF1aKAMA6ByUSjlY0Nwazc0WbgFqyZsvZ1KGeyY6HuLNO8i2+HNHFNp4aGedzFNqd4Xao3J1OJ2c0JSzAn54JmNkO5BIJjYEfrHLqh7qRsKMnl1TFYf6jpQ+I7tDCUeVgkTRysorw2ZiRLL7wr0zT78oIlBdjMmWyxVy/CZLaLLDhpFU0VCYAXw8n2NgdxcfPhhAVuR48VsFUjsHLqX+2D47HnaRENizmcSLThoKQGG0faRtHrfOh7rJktqFxD5cM0s0NZnoux22P1Reg4oex0iyGvUZE6Ssily+SYy4zO21xKNDXVrLXlRabP5rS2Pc4Jz6qOGyA5Lk98La93fJhtLAPr5W5u+ra/q8+K4ob0oWAzOhBpb7NdOT7qwFAk9M5FGTyJF0c/KFXSPku3eDmj0vri3jaNi2ZuEFNiwB6A659A7rtiK89SMzHXMaHtmKiYbw5nuVAOxcKSgpXG2PRe7Sw4jxMZqy3admOz28uOzNuFf6v43cRcSJk5S9fJLD/FGMqcY9pX6awDPuv67dpAdWljSm4DxwC2WGjr9SCEnq3iDirtdpKkZYOscJdTIm/U/Y43esuca9rZm0R8NyVQINchnDVYxXGl2elalApdBRF3sJStC0cIvJVdF1ahBezpQS0l1GXKi6DUMjDQQ0dPpjOxo3cU8Gzl2Ju1WE1txlS8Kbm3So+JidKresnoKWeK4Sc5YOTpsOF38SHe2Gl9k+dHGteZgJODIbkwXOmTu9DsKwInNqqvnM2rUZRT1USDtZCoyTWOZ5maiRPGOzRwEbvaL62hB43cRfIcjlWOxG9bhpZnAzWnTuUOzemWYpKUaqohbDGALTaTmqnyY4NNM2VFwt5OpDbcRskzS7k6Sw/CEVMJddP1ooIRBDNfnOeLetiVlcKcldnRO8cpA8Nce+dEXjoF3udlxmh6u8IUTQeLWHIkbh/OyYRNnV7SJxcz3/r+2msowTy6SzZbYBSlbbgrveoTaWsvJCfobIncV5SZ525NndumY1dOXQ4uPt/45IEChWlInLEgxGRODcOVvxxFqdHW17jceNi2a5Kl7K3YBeO4lbQAqeejPNrTC7ODitTcOZwxot1EG9So9fqIysbyYtJ+vkEjxXMXPs3b4vKymk/Xl9BJs4xQm9rNPIo40+nM3hBA0hcmVp8xbsBYA70oa5tUrhlAHU+ay8EaZ/Rj44v8lmOWdT2s7JNS3kTPcuhau3DnChZE16b1uQTVrErxpeUvVvPhBqfXQ9rCDmEtuJVDcgcgKOUKgxvf656yJvYObqxXvt9OCszWgjpcG1RzLkJUxTEW3Zu6OlAGD+OP+8cVkW26KIXNeJWGdr0v4VZ30RUnKQ2EQtoX+ybJJ80wBO1kJW0OE32BbmVTcSfJUWJ0jltQR5ONWs3dE3vWLzdy2PM3R8TnbX2jT9TqWIuxSIrHYE/GqCRP5bmNX1InWNfbZHam9iA8J8JWWWc5qjPAacCkT4/CAtTDsPT6vse5yRmzKMVO7dPVa7hAXaU0n/nkaia0YnP17T3Pel17ucqXmh32tT+pUZW6EpFV1sOedZy1jxscIYmOCGCTLcrEtZiCadZYI/nD1L7NLteQwrliOgfaSuZbdneu1gQPgoHZM1zPLm/dZJFmk/3VKNNuBvx5YIvNLfEw6eKlWEJvePSw0ouGmbDZhpjWONqdWGDX5YROtQbA3czEW29XE2c2wePDrFyht55XaCXQaMZlZtc2PWRy0dU0CiTlIg/zaSgBh7Cvm6Y/E/PLNpjcULiDI8UzNhxm/sXVwcVPBlbHZcPFlKSh3U7aNThn7WMLpXcFtip3E36TneB4LmhRE85RtI7BYaaV06qbbcQiUiS8plyTrqY+yL14GXHWTM30fJ7G7BWTGCVj4VZDgthn1eFRIfbi4apj+MR2ghj+YqZ6Y6fH43DatXywMwJ3NYmbiHbbgNxvurk+nVjcHI2YYdGyy3kbKOtpxs+GYLiEN2+3co98xrt7yz+mYpvZtlsrmp9fK7Of8QMhyR2szyuT0QM7YdBO81jzzDeLBsQ3Lzok0566Bh4jiYAkyH3ZoE4hEiy2kLyZFLqYdZRPhHANj72+nR7ncV4pdW1iirTzvNW13dBbbaXCXONXG81dGMuWo7wttpvRAktf+60nK+SpqzaMjd/2LW1FOD3dnzece52Qq/UJtl6yzFmW/efLp5fxCPp5kPz33hKPx3r/z04XHweBb6+W7ofIwHK/3GV9+Zt6/fLppXDCUav7WWoZ1/7z0PG/nKR+/rfeSows+scr2PFdWFe9Hb9Xlj/+b6KXMHXrsir6b2UW1/cD3U8vsHbG/9ZQfnseXL/czUvykduP5jzPyb9V2dOi8c79FWMC3PBBMF76zxPmTy9uD6MVOuU3gqa+gSIfzX2+6IBW4q/Y6/Tl9/8NwxhvE6wlAAA= -->
