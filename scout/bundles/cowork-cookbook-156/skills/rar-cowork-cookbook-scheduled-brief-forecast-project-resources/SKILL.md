---
name: "rar-cowork-cookbook-scheduled-brief-forecast-project-resources"
description: "Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_project_resources", "rar_sha256": "f036e90de9548fb9af5f301820d851ba2ed18798f5a1af72a29dab660fec1ed0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_project_resources`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_project_resources_agent.py` and in the RCI capsule.

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

Forecast project resources Scheduled Email Brief — Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 f036e90de9548fb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_project_resources_agent.py` first:

```bash
python3 scheduled_brief_forecast_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_project_resources_agent.py   # or on stdin
python3 scheduled_brief_forecast_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast project resources Scheduled Email Brief — Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_project_resources',
    "version": '2.0.1',
    "display_name": 'Forecast project resources Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2714468ab3e88ad9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/forecast-project-resources'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-forecast-project-resources', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefForecastProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastProjectResources'
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
    print(ScheduledBriefForecastProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPaWLbnV9Hk+8Ouh51aQBJyR0eMFgSSkAChBShX2Nr3fUPU1HefKyDTVV1db7rfTMRgZySSzj37Ob9zr/LXF6trw6J++fJy9KwcWltpGoVeDVm5C7HFUNQJ+FUkNviBnCJv68ju2qJuXj69uF7j1FHZRkU+LXdCz+1Sy049KCvqPMqDz3YdeT7kZVaUQk2XZVYd3cB9yC9qz7GaFirrIvacFqq9puhqx2umR1AbetOdssibaGJXDLlX/w0C8qIg91yoLaC6yyEXsB0hQD94XpKOr0Al72plZeo1L19+/uXTSwS+v3z59cVJrab5oaLnMpNe/FOJ/UMH9U0FwCa18gDQlyNwTQ6uS68GemXglgvseV59bLzU/wT9538mg1UHzU9fvubQ8/P1ZfqnAh0nU9oCSAFqO1Zp2VEateMrRKeDNTbAyrar8wayoAZ4Ng9eHyt/cCpK6O/Ts48PIa+B1378+lIAFazJ719ffpoc8PUF+AN8f524lB9/ek2Lwas//vSDT9PZd0cDZkDr12/P6ydbQPiDNPLvUv8OuD4ibHtfX35n3PR56D3ZCVa+vMZFlH98MAYR7b3cyh3v409/xRaEwUnSqGn/Jb4/PxiHnuUCm56K//Tp7uRfoNnToHeefy22BGH9dywB5G/iPkFPR/0V77v//4F1GuUgod88/k/Z/bMFs79DP/+lbf/Vgk+Q//WF89KoB9kB6uYL9Ou3437F/vzB/XHzwy+/Adb/RzbHey1MHL5lVh75XtN++/bzh0eJfPjl5w9dCXLNs7JvXZ3+M57/zK93OX/w4JPq4x/XAvl6nuSg7KH3TId+Lcr/Uf/2ChlWGrk/7jdfoN/Xy/SZQZMRb0IfLvhdzTRA19/58aeX30CnyIE1nXN/DKr8P/4DkiOnLprCb6GjU3Tt1HDaKPMm5bUwaiDw/9GmgF8fXepB9+xok8aFD33/n869h352nj0Ubt560Ld7c/z21gq/PRd+e2+F318hDUgo6iiIciuFVHq//5pbgZe3k/QSEHp1D/qKPbbeZ8Dn8/QFinLo+78u5Nud32s5fr93/OjRsVRWmLpVA1i8ThaboZc/7XMASHhXz+mAqLRwgF5+BBrup3sLT3vQ7SbvNEmUppAbAbEALMY7b+DBLxOz79+/21YTfs0f7XUOPVCkgQHBuzrQ58/AQD+NgrD9mntOWEAffv3tA/S/oP9q1Z35JGMPGv4zPkBD8bhTIFBvXQbIQOhAsEEzucfn19+ebgZsAMhAIJqRH3mPxSBfE8998/lxQ3/GcAKyvcmdEACXom4nNIvaV0jwoXd9gdDp0dTVwwKAnOuVXu56uTMCrhYw592TedFCDUjKxh8/QV3j3aV+t2vrrmIGCt9qv0MyuwcYUqRvuDcRgcVFHgH3v2fE4z5gUn9oIOaNxSukTBkKlVZtlWFtPWX41iMuADvelgPmFpR7w9d8gk1vctW9XB7uAUTAM84zpJ+nmINxACB67jZvsu801oR02h3x6q958ywFq55C4QBoAEKDLnIngPjbM6WasOhS9+4/7wH+zyi4z6jcc5D/65nhHdeh1X3UuMM79LXDEHQB/f+fSybt6fVaXa1pbcVBK0VTzw+vTgPV5P3HDAYGg6cYUEE/hoW3VvPWcb/maQRSpB7/9qC8x+JJ8+hiXQ2UUWn1zh8kAvDqxPeep1Pe1fWU4dbX/K21fwKhv/cxECpQ1MnDljeB09M3TUNQudP1D5i/x7V2pxIHuQiVnZ2CPPE9z7UtJwFa1VOtPYMBktab6m4IIyf8g1UQ4A5yA/CHgBIRqB7g3bvrlAKYOQWnLrIf5NE0PAEt3M4B2oKJ1XuFTFAuUwQaUKNgAppogBc+3FlBmQd8DFR893ATWuVDmWnIfSpoTbEoMpDFv4/A8+GPBL/rMqkPuFqu1QJfDlPrdb3rI7Lvej5jBZTNppK8L/pjuJ+2Qr/HoL99ze86vnd7UOmPFP7hHAhUWNbcW+vUqBrQbDLvPU8fefv6ANsHmr/r8uVPk/3Hf2/4v8On/sfIfYHCti2bLzD8gLw3xHsFbQIGORKVXvMD/R4l+Pmt4D4/C+7ze8H9QcLDYV+gf0/LP7B4pvcXCH1FXpHp0TZyvCl/nx/gFPYzc/68mJ5+zVXvR7SfKTG1W1DY9viOPW8kAICC2gsm4gcWNROEDQA1780XxONr/p4Rz3oBvT0PJuBsit/V8R2EQXwfXnjHCPAob4FsdxrjAm/a6qST+o338iXv0vTTS25l3r+zxZkAASQv8Mq0QwLuB+NRG3n3q/dRabr44y7vXmKgN7jFl6nSPkHTWPsJep9QP0Fve4b7dizvwKbp52k6nkQCUvDrnfZ9C2l7L2C31o7lZMFjIzQNZc9h+c9KTAUGNAaGNJMubxU7SfwTE/AlCLz6z0x29y9W+mwbTWtNkB21b8X+lqqfIBBDUISgrkC77MCCP4sBcmqv6gA2upO5P/z3w6ziYctvdze0j93kry9v7eMZg+fkCMhBnX5uJnSEQb4CgeD6kVng2f/FTPnkBFofmGQAKx+ZEx6FuB6FL5a+TVk+7s8RdIkh7hJHbQvzXHRJUksft1DLJzELo1zLJgjE9xzUcyfNHpy/TcNANGnngWdzCsUcd05gOL6gULAMrFqQluUiyyWJkL4L0OHH0gT0zafJDxMnf76Pt5Nrnpb/+mITC0C5WTQC/fiwMGVYMEbaaridnZDZ9Qovwg43i3I3R72mxnXZRZGAUdZxhEtDeTqLfnJsK0sIk26tOyi3P4SzQqWSvs3c0ksk2RC9OHAAvXgTMTd34dvNEJmVMHj8xZBKKeVNVYcr4mCmmsjr40mKGF80K0MpU/HalytiNSzr+mJHFErBy7EZb6V25nmzW1I6gqcnPpXsi70+pv6SvzWnG0kbwZEyajUht0J8vGDXk9lVgRMZutU74dXlCbFyyjVLGhYNp1VZYYMdJ1YeXyk/55Yz/5TPWi2EqX4bhSi7ZKQuGdedgSICRtlV4W5RNMSCeJXmkrn2EW4Lq52OlkRSi7djrDlHsyYPyrZTjocBX9PFKq/KQkh4wjndeLw6ymHjqpgk3vSzQXEuy+XWyA99aiX5oahPVSwR48owRd41ufnSqU8FjlJSQ5ycM06epMuFOCgXKToWJxm5rj1lvs5WJK9LBZo6gXkZWD4VZyrP5XJ79Q1LnDWufzgsDLSPtkeWrgP0wh8vpJHQMGgdhs2VkcUXZS4uMdZTnQqp+EXfobWcd2pzqCSCEJmu2meXzVlSAmxjm2vFbC9mkklEUfIJpsHnSKlR2yFqa9Bjwc8r1WRL+kxmTmnFFR5S2tWwiSE34cxxRjo5R93cblO0puRDR2DkeWPfzvJxHFXjktmYj53idsuKlWEi8lotc5x317XQKVaxPzJR1ojNYQu3gSSHbs5YLWGE6kn2Cam4uhLeCde4ZYfNXHaSkuOk65zbijrONBRM+mW1bS/o6VLjtmgP10ZrWVyJZERZEbx0yfyVaF2UlkiVmkjFGqsuJjwwdUXmC5nJyQ0/FLfliVry+IIbe59IVLXaFrAsxxdqt9ojy9l1ty0P+Zly+XUwwqm9MrH18Vh6aHbKjkcJN1OjUB3n2MnZGld1NV6fveMGubSbbbQ8KufxNCa34KwQhF5XCQ96Vs9geeihMh9L1nV0rZqxh0vDHNsF2JGPkVquFivNifVICECPSGTGZUSnHcduKxeb1dB4HT5noyauZ+OmLAl+boAtQ9AmJ3eLK8OxNReXHWrvCllrdTxG+nwGtnlK5oQ9XtwIZLd1lylnIrvZHj4RBHXmzqZpnfdRYsE9fq4DCjudr0eJydfXWB9VxdJyj92uHVM5ZAskHBAlOCzhwTH2JrXOA7H2Ba4qtli91TXJvVVBU6HnUILhRhq8Yne0/SFOcJlSkpO/QHXjvDhp9XlFSV2ElSLWa1hLSkvraOpDVRsRO7I3BcF2Ik4EerW0OE9ZSzmlHCPcsvGz5Gr8HllrhefTBuMFTZqccyVrWBWuVE8hscTglrhYyum6SLQ9osmghnRcN0qlbQOWmG9yLhPOS6cZ0IXg8liWbY1Sc3fZCg/R3UGqd/ww3pTOFS/HVEfq3rpyKdo4h5Dz8LJSQs1Gl/41Ra1QbDG7FHDUOszmCTaP/FvnbwXhsNO5i6EW6pxX+pmYzfxxrSlRb1H+oM/Gne2Wc2pRadRCl2DakefdCjP0XsDQdIRthrLEECWrA4WLiL0J7XybY/wunoNqMHlioCNsdnCOTn7ONvshcIY083g23yCunG+R3drYEq0z63w+z7D8KLO0PQbNYSNU2kXIUOpgxtfdmbPGttaZYyrRQlZSplhhve2080Ew41tE23xpotei5o6Mo5tEOUvzG4s2CMeYQyfnmiZmB72Fazb2dh6GO4GeaGB+lau2lnj7dMFAZ7vMefPK7Y+ub7cJub9dRngXHc2Dga0QV5nPZItcFfilj+rbmdyAnOeJhJJvWnhb2ulWs/NMmbODNS9J2IUBzGxJQl+afjWOVDrLnZO0xjVEvITzPsvwkqF7SwxUU+SyxBnlRS2V6aJzXTGRNv4NVitbt3uEVl2mqtMFk0fbVEe1BJXjpL5t6kRlrUisCXilU6dQotzYBIUJ64aut2qq9TBT6ldXM2bJaa+VlbTwxUsXbzp9SchkE3Oq32iHyh83Hrs8kfx64+qUbSfxLiEMsZuV1u1kZ0lwK3yd0WikEUccSdM10WLy6hbVmDDi7SK4xszuhhZDEO1Jua20lWLh/JxiTwq2FxGxUriMWlmsU3rpSdHOmN65Td9elSsztEpSk9K8MWL6iMfrMTTHJgj2Yc2houGgMeHtZ0JIt0R9tiRlpx18VJUOKyHU9opgbMUgYHcIspRKFb2cq+ugodebz3XChqE1EdQ0vr6ZqH2Vl6hxUeXuYklpdS6FJSec6P2F2Q7ynq28aDVgni1isEizjFYalSbTqOqiyaxkb9wgZMHGL44LfnXz3c7MES9FE1dQV4tOoK+LJKR3m8yOKyU9H5Z6cxyHSOVoj0HEYDwdNosbZZ1Dt8ktysvNUzCOeVZE24uFBnvUNi1MYDZtpxKymsk4vkXdUzjjSWSlFZqR6u0pFGKELEc9oo6GeokIh2dAIiOJw1vdFTdMXjjrpLlysbVndCClOVNSBFozeAQALBYK+8MsctuDBnfWLtknZ3VFX9Q9PEP6tpwHpdhy6ijb+43JXIXttrvymCyCKQCvsi23s2DQdedz6jZrRVeYM9fjpZUCF2NmE+QdtM2tH5bEeS4s1Yvdk0WFdHPEay5eLF3l1N6382BQegEplUBGPMp2lSGqbgzN3GiL2xdwokb5NoCREIm2jBJrnMMcKW+Dz9RgfzR5q9iReDBzM88pT2FOYC6OhFtgoClaWa0Ppw1GNueSP/RevPIQyWROUiWH/XQwVsyxlVccbvR5yJ32hPW6bEkr5GYqfHSKsjrcZ7vNMYm2wuGyNDQHIE+54rLrVjxyTn8UXH05+igTp6WDdx2dhNlF8w573NPhRrDCBgyG67ZcMzrnursDSNeVnpW1JCbcGPSn/UoAAxsDRvZtcWF5etuVC6nalQl+AKMIcsTw2zViZltHPTCr3bFEr+v1aVhHGhJfpEt/JI65RHdhfCQrMEBalddgjrWrjpltCvbuZKS968rpHt/ipq/LIZXIC/OEZ/O4QQOlxHFPJOTUQ4SmFGwMoeQVutcE31xgad0ptEasd2st5y8rKkT2JagVAxmKeWqAIQRdF1nbrRabcrNYc8yWH0PqsEQ4/3LkN3Js66ygObg17GqGqfF+u+sY3au904wVhrnQiPaMLonOw7f2AguR0muUpivR0mwltju2VqAsg65yL2x8CYQR2Rg0P7MIKel3uXoxik1chRorMnml6Th+secd3SCVvS7AwquZzfixxBHnLF0SwbmGEY5XTZM7+2B1kzJNFLNgsYbdhkMr+3oEkL48LpeYAiem6hYNxedlEKRdHRtsWEoMlvpyMF9yCHsJxvgEcJC+5uVqf9JKijMDzt/Czojt/H6jkGhxtFbNIHAEBUYnP2JcWG+Z1u1RpZf3iXVh+AvGXhZZiMv0yW8zRq+7ptVcyaiCw2pf94d65+w4ZjpR2aQObzgVhZji5nDm+4MSqyq5C0QwHmONGZjS2hYHY+ZUh7bvcVGtFrtK5hc0I3dOrUgK7dIwuWPK8KhLptB5tmYc0k21whp2v9uO4XDcSLaJsVKYCd3WR84t5tt7qpAEe2EvNVe8sVe536+KJdFWDYGjzGoTdm2J7rHkUpi3weDjGc7Ny3BU3Jq5tWh92887eLuAnYMTU6TZmhTm1RVcrjtQR0PHjeR5FnpMSnbbaLbZ5ccOHRzbw3LaN5COp7gD2V7hdhcbRpfLDbbbMBdxydaJj6F7e8SJc41hMmmRxka/XgddN+VSNp1zXrI0E8NtYyyFfCiBqqZn7/Fmt+3lM8uz/Gh2ozWIS8LVwEZIp5ycimMKsfHrQuJs+nbBDGxZnogZyocLoiH9Wxv0AtOpm+uM37VKf8aGubnANxxBwjAVtTNapkeS0zr0BvPaOJvnruOy9Yy4RtfUi9PdYn+W0AMcI+kmsLiNwnBF7wEVyD3H5zfmJMorurNnpqnvUVpfkE1z5RJmxuDaGoy60e4Ai7l3Oi4bBOlJh8TzolW9sqlaoosHZ+cWtWHKhcHVBr5blvhwEnlR3oLNRDRyPkG38xtj9eGok43Z5gN89Aebc3CPmS9V1N+st8PObds5xsyVk4SNo1IeyjN1ONzg46bGBqVZa1vmHC8QHl+7uRCbKtyZBayg8yqG69OsWVerhrBIkhXPjEQKm4Rarq/I3gZjjJdZIUae6jbYroQ1ybY7TrFPt6bfwpZiddmSvY6wri/dI5nV8W2ergAo6wLrY+78dmZXs9XF3x6EwLZkdVfEnhc3RkSJdnuDEYc9nDeWGPl9MOc5b1VfUXe/UQTOpdTFNbxstuHhDFsSEvkNFVorsb+xtzSP7F3f8aBBgZK19+xpuTAiB1Z6v/P9slyD9kfDJmNy+4Z0YABh+MoR2It0XpW0e/OyjAsPgs3LvHqGc5ydeQuMYa0dHAsLzYvWQQuvsWE9x8l226j0PLKVG5I01+M1afgeC2we3pDCOpASfkF6gkDhl6RRZ12BYvZ8d2vWsMewqOkUlMPRvUPQ635DY7Ky8ePZsLYGR80c14SJmX6J53nVdDcMzNZ8gKGr+a4GBdTukbqJXMuu7N5AaifMq7mpXHd27bC+ii119jwbBP2ksKcNAHqXcK5CwY2yD2a1faqOM23h7Y87VUnmqKoQ6GxFt9o8ZPo1jexw74Jsrr2JkfNrdm6pniBxv5vvPJiN6PUS1BOJgViG5IG9tjPd2Z9OdutX3cbm1TJW5ofNuKZCcjU/0Vd84faIB4uuTw7RBt4SHDYPev9icCMT4upN55Ezm4fGxj1dcvLc+EylVP2aRZ0GdynxdPWj21LR6D1dsgzq+5s4hh1LCM6YP7gjsa1vyrYzzdlePudRgVctk/XyMiK2znVYUdx6fqVpS+ZCaWWeeCXbZpviiJ2X/dwMkN634f5yXHrubJM0RrCnF+HGjcl8qy+7wQAe4kix9pYSOWPQNRcF2zm7ck7rwL7tNhwrVcuSGmQruAx4xOzlng3bDlW8ktNMdLM9GPNu4OLtAiRiW8s1DEIGdimn6wVxyK3X4M0ebOcVtFeC3ll05NaJlx55GZmVzy3K0McN1cWKwFCQE54OFU20yxHB8vlcHjaK5ftcOKwJIeJU0+lZbnN0GYoNL9jMCVQ4uQhEPG5zZY8fry1PztvECW9Ej8HKzhbObgwvOJMbOMM9lDRN//3l08t0KP08Wv5vvFSezvj+nx01Pk4F31473Y+VPcv9cpf15b+j3C+fXmonAqo9jlibtAuex5D/cMD6+V9/bTHxGR/vbqc3Ztf27XweDDPTXyW9RLkLoL4evzVF2t0Pez+92F0z/WVE8+15qP1yNzQrpxPyfzDs8ehuUVtM9H40UUX59DLIcyOr9Z6XwfMI+tOLO4IIRk7zbU7g37y6nAx/vg4B9mKvyCv68tv/BhlMN4MJJgAA -->
