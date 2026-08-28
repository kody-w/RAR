---
name: "rar-cowork-cookbook-scheduled-brief-modify-production-plan"
description: "Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_modify_production_plan", "rar_sha256": "44c48247b27a88bd781c68b0a11ab396f5ebc5b466567ce0945edf01f1516e48", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Scheduled Email Brief — Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 44c48247b27a88bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_modify_production_plan_agent.py` first:

```bash
python3 scheduled_brief_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_modify_production_plan_agent.py   # or on stdin
python3 scheduled_brief_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Scheduled Email Brief — Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_modify_production_plan',
    "version": '2.0.1',
    "display_name": 'Modify production plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '760bfa7f3960a4bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefModifyProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefModifyProductionPlan'
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
    print(ScheduledBriefModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZObWJb2X9HkfLBrZCcgVrmjIwaBhAABYhFClCtc7ELsmwDVW//9vUjKdFVX9UzXxESM7LQFnHv285xzL/nLi9O156J++fKiB04+45w0jc9BPXNyf8YUfVEn4L8iccHPzCvyto7dri3q5uXTix80Xh2XbVzk03LvHPhd6rhpMMuKOo/z6LNbx0E4CzInTmdNl2VOHd/AffDcj8NxVtaF33nT+lmZAuFhUc/aczCrg6Ys8iaeWBV9HtR/mwFZcZQH/qwtZnWXz3zAcpwB+j4IknR8BeoEg5OVadC8fPnxp08vMfj+8uWXFy91mua7eoG/mnSS7grs3+XvgXjAAvwbAdpyBC6ZrsugBjpl4JYP7HhefWyCNPw0+4//SHqnjpofvnzNZ8/P15fpjwb0m8xoC6dpgcqeUzpunMbt+Dqj094ZG2Bh29V5M3NmDfBoHr0+Vn7nVJSzv0/PPj6EvEZB+/HrSwFUcCZ9v778MBn/9QX4Anx/nbiUH394TYs+qD/+8J1P07mXwGsnZkDr12/P6ydbQPidNA7vUv8OuD4i6wZfX35j3PR56D3ZCVa+vF6KOP/4YAxieQ1yJ/eCjz/8M7YgBF6Sxk37L/H98cH4HDg+sOmp+A+f7k7+aTZ/GvTO85+LnXLrr1gCyN/EfZo9HfXPeN/9/w+s0zgPmneP/ym7P1sw//vsx39q23+14NMs/PrCBml8BdkBaubL7Jdv+n7N/PjB/37zw0+/Atb/LRu96GrvzuFb5uRxGDTtt28/fmjutz/89OOHrgS5FjjZt65O/4znn/n1Lud3HnxSffz9WiD/kCc5KPnZe6bPfinKf6t/fZ2ZThr73+83X2a/rZfpM59NRrwJfbjgNzXTAF1/48cfXn4FKJEDax4QMIHEv//7TIq9umiKsJ3pXtG1E9i0cRZMyhvnuJmBvw+IAn59INSDDuT/FOFJ4yKc/fyf3h07P3tP7ISaN/z5dgfFbw8I/PYdAu+J8vPrzADcizqO4txJZxq933/NnSjI20lyCZAxqK8AU9yxDT4DNPo8fZnF+eznf03Atzuv13L8+Y7w8QOpNIafUKoBy18nS4/nIH/a5QFcDobA64CYtPCATmEMQPbTBNJFegUoN3mlSeI0nflxDVxQ1OOdN/Dcl4nZzz//7DrN+Wv+gFV09ugaDQQI3tWZff4MjAvTODq3X/PAOxezD7/8+mH2/2b/1ao780nGHoD8My5AQ0FX5Bmosy4DZCBkIMgARO5x+eXXp4sBG9BYZiCKcRgHj8UgT5PAf/O3vqU/L3Bi5gbAz8DHWVnU7dS94vZ1xoezd32B0OnRhObnomlBryqD3A9ybwRcHWDOuyfzop01IBmbcPw065rgLvVnt3buKmag4J3255nE7EHvKNK3XjcRgcVFHgP3v2fD4z5gUn9oZqs3Fq8zecrMWenUTnmunaeM0HnEBfSMt+WAuTPLg/5rPrXKYHLVvUwe7gFEwDPeM6Sfp5iD9g86eO43b7LvNM7U4Yx7p6u/5s2zBJx6CoUHWgIQGnWxPzWGvz1TqjkXXerf/Rc8Gv4zCv4zKvcclP58Rnjv47P1fay4t/PZ124BI9js/3YGmbSmOU5bc7SxZmdr2dBOD29Og9Pk9cesBQaBpxhQOd+HgzdoeUPYr3kag9Sox789KO8xeNI8UKurgTIard35gwQA3pz43vNzyre6njLb+Zq/QfknEPI7bgFrQTEnD1veBE5P3zQ9g4qdrr+39Xs8a38qbZCDs7JzU5AfYRD4ruMlQKt6qrFnIECyBlO99efYO//OqhngDnIC8J8BJWJQNcC7d9fJBTATBCasi+w7eTwNS48gAW3BZBq8zo6gTKYINKA2wcQz0QAvfLizmmUB8DFQ8d3DzdkpH8pMw+xTQWeKRZGB7P1tBJ4Pvyf2XZdJfcDV8Z0W+LKf4NYPhkdk3/V8xgoom02leF/0+3A/bZ39tuf87Wt+1/Ed4UGFP9L3u3NmoLKy5g6pE0A1AGSy4D1PH5359dFcH937XZcvf5jgP/61If/eLg+/j9yX2blty+YLBD1a3FuHewXwAIEcicug+d7tHuX3+VFsn78X2+f7UPZb7g9nfZn9NQ1/x+KZ2l9myCv8Ck+PdrEXTLn7/ACHMJ9Xp8/Y9PRrrgXfI/1MhwliQVG743u/eSMBTSeqg2gifvSfZmpbPeiUd8AFsfiav2fDs1YAnufR1Cyb4jc1fG+8ILaP0L33BfAob4FsfxrZomDa0qST+k3w8iXv0vTTS+5kwb+6lZkaAEha4JFpFwQcD8agNg7uV+8j0XTx+13cvbQAJvjFl6nCPt1B8dPsfRL9NHvbG9y3XHkHNkc/TlPwJPIh+Z32fYvoBi9gR9aO5aT9Y8MzDV/PofiPSkyFBTT2gqmpF++VOkn8AxPwJYqC+o9MlPsXJ33CRdM6U4uO27cif0vRTzMQP1B8oJ4ATHZgwR/FADl1UHWgF/qTud/9992s4mHLr3c3tI9d4y8vb7DxjMFzQgTkoD4/N1M3hECuAoHg+pFV4Nn/cHZ8cgFwB6YWwAbDPIxaYKS7IB2Kcn2SQjyCcmEHQRwXXRIhHrge7mIEgROkF8BLDA/8EEZCBEeIAKMAv0eGfpsafzxpFsBhgC6RheejxALHsSVCLpyl72Ck4/gwRZEwGfqgI3xfmgCsfJr7MG/y5fsYO7nlafUvLy6BAcot1vD048NAS9MhgAHy2Z2TRBhVF4qCl+UYtOkCWaa2z4q+TUuwY7CCm24kVodT2DiRTRXzcHLzenW1jFn8nC90yIPP/o7tjJK/boqEYxaMgAfbqEOhRMF1mteapVSVvnuw1ay2ZTFD+kPm3TbjQm/hS2lUxiXUhYWgEeZRh7bujqQW/G2npHJ8ktoQd871rVJEu23xxhZTaMgVaTvoc1k8FkhSHcbzKWvxcp3ZrZeqy01VDQHuxwupEhsP3zD4xo6gAtHNZbLY8oiS30Zc2S7HeVdTHLqdQ7K1YYkNtjI5YdQ704R3R8SvDl1bE4armrE+JDUrE+dsDrsIeqpSbZSoErakcpwvV7LF1QXm+BF90Tt9cR49q15h1ZE7x8PRBHyPyaaPLdnlD56bBV3atOZa33KtnjT57TCMuEdq7jq4XGy8dkCabB0HN+tcWpMCd2rKw8j2PmYlvn0rNJ2w9CNjWzCd6Ifcpt1cPDlj2iGX0ibxYatuRVzwE4bpLmKSmuem8zgck8i0smxfkAc45XEEZvetXpriDg9HrG7c5NhIucx6KEtJaqNzveWW1f7YbE8tQwSC6CxP8iFfyENrVy5pOkc9PbE9ZeCwXrLWejS1o5erbDUH03knUYugznNVStdmgHtU1wUQLDR+hTMLB2XhoMmQUUv9nMxOV/MWi/Ghs7ik4gYNxdPBLxtz1R2QVkuLjEZ4kxwHxNE6I7qFsno7EXgMreTtbrCYuZot4B0d6sOg8KfAUgrb1vNGykLIW/qmV4td1ez39k7hNrFJWUJ2uqmwUahtZrv2ThP8+lD6R1gnmrI0zbDb7Q1rO57CHBb2xS3H2n2vhhHNL6FK23Cn+YXqhzaHYRUydjca61LGD1F47bA7ymw092TL+gY/+rIpxZ1ZmU5yNHgUVNCpaYtzzoIMpySuvPSKv25KF9fbRMhleWcahdL5Gs4KpOIhkhATHNW30x4jMverhMYTW0MYrdzwieEZXaz2WrI4wRIe84VtbqSjDdvGeZBQUHNyX10wYu77hCMHt8rSlFEfd0lCpL2eHK6cVfSokOQEq7hUu80Cp2jLBQEyL9nTnXA85zy3hPbUdc/6YheeL6GBFXR5RVJzsOsd5tHDuRokftHETq171qDxt8siEne1bt4EKA7zbnspq0sBUzSy588XzbYGMt3CuhKs6bg2Y2mfzfv6TLg+30KMYGQ3eG770CXV7MsKtJneuJmE68FtSjhILVvLQFeZedUquxuPUah/wvLbSdOvDoYYq66EhErpuMvyyMTRSSCiUmZvGNeIo5k09QH38kibE0kYa2aDqNfN1ULE2GTkTZVTFxmna+A/plsiI07uSz7wHKnxdguYPh6yLl8Jtq9mypbQ1MxwsIjr8IXUyY49pmcnrStbswhXEdbnPd91SJ+0UqbgBCQekwUhGR4EV8kNWRPcJQxz2UxGRqRZad6MBZajKtdCh6MSjpyLxK2z3C6xYLPfdrlBSQi97OBCMrQunJf8EC0uBSkDvD0JQ0KIhzkuHA6+lnbCJVCyZUKblyM30u3xmh2GWNBvErQtVthGVnaekaA7ar+9EmJmxMhKu+6uKyNZhK6i8/ulVESrwyodI1THjx6tNxJ35Mdmy+yiZKWfYvmUbTnEHeQrQ2ZnoR+vtIWUmjwUF/kUO6LrrH3QmPqE2wh+LBK3m5zScInb3a0vrEsetdZ6s9uSbLHbbVpcFDqfdM+LTeZlebux7SU13xstBF1FT+OFkHPaAenQawIXo3jNOZxzbsJ8Qzsyd7YplKIYbyfurrVinSyROTPXaz2q7niwRhiC5p3FzlXLC3h20CnxeGXT9EhVbJRHG2XgGRVpt81VEgthB1CnKiWM9iB56UpwUmWY4a04OCuuOb9bnxa+airGIb5Z15iJ9bjMkpZN5qse2TMnNUTO+1JzDkM6IGoqbpQstZPFfEcWN0fQveyiX3YQCjfwYcz2OMks8I5jrEM0bAwtOZHUftMJremqrZIRGNYaqTdytaz2SouevSMv1Yy3t0V7yHwSdbx+42fS3NH5xukN77a1m5KmqKUnHErqatYwaQ24gp+a/AgrNqwXfJyKpnRELjw+XJFrJ3R8sLYLOLQXS506MYfmBBr1eEwOJoYIdp6igi0HW2pteaK0Vjd1LQ5nvIr0YkdGZiUOZAUjhrZi2VqEyPKI2w596neYcywjS9qfToKERyfZ9BBPpsKAoxnTuJZinGSpyNDxKBP0jVbnbMBXOV/KSF6Nyz2n0+ppXfm0zc1rsTos0HXNrefSQBP9hu8pfeG5t/SKxM5lpxujeWF8AU69+SmJ/BEpasaAE108Cn5hMtEKsmOhY0IdhakTLDC4PYd23qLobMSQ5QO1GNf1CqqI1kj8i4IeIzhqabxemP3yqC8HOF6jZz2rJfUS5JpowG5lOKKoF6zAFxctYLFFJF9uTaKifSl6PFlsqMEJDzl7EOVdpKcb2N4cF2deVinda/PzEvXmyd5Q03LVRRTketBi5TAJQdpg9vCojcoVtG75KFoVewQWahM5HI0DLijb6xXaEnoLmRRbJK2TRnXEGu4uh+lYyXUbh7uOxcbFMcyRFO5Q2G7s4CIMSumGrVVJUlIgR1mVLsES98UoYuwqok8nucuvbVfhutGHmFodsp7dHfrt+nC18DE86B6cxoe+xLiqLLjc4qwjTrG3LZcIDqJXhbKvTDBtkQ2/Ef3jzrqqa5+VonSsLrcaGSvPRZbGpmdom52LZNqqtlbgad9V9pxuLzs49hpPyTK+iYb9TUbGSFASVXHpJuVztdZ536J0F1kZde2VORH6G7ujw/SmB3nooht+0NoyU0fW3ciWYIbrg17mopCxvdqG+4PI6YfBc6pdZovrLWbOC0zMpEXSENsN2PBJRmasAwc6++46XNL5xc7PysY6KSdD6caDEeR7US1YqubSpm+MI2IGzahV7dHIdozghu7RCG1IWe2XrXTco6rbZeyi8DNq06BK2dNDTlZxuuusLTLI7mCMVUlsY6lNMMK3cPmyXylQqsKkce3UzMpIfE2jmbk5S8imiJfNGlsvthjHrrYb4oyo1IHd2vpmKwmutdY4ss5p1ONNVsBxBNkavnMLO5nDFzSrXDOLYg3zsLy1A4pUqL5XTWcpWuZGP3GUeVzQBsaCxunyq0xJ8CNdjVs/ZRoiTFM9DpR4LRXJIbBLPT9IV0PtKA3MQspKRwrjIi9hPpUXi6ZYWWs7GTWRJK7wJZH28eYyxnopzy+9SC3dnEpqQb1koVUtOi+3BF9IT7Zi7stLhCfFxWYiu9reNqiCWhjXM2UKGoTaB9iQ47AYGvJII8U+3F2NoUvysFuWpXo48TYWcMhNLNWrotaZBaZ/NKxYrQzisY8ZslkbS4UVA/a6uSi3ImpILQyyy/ncX+EyHLVEdixW0+Jgr6NKSkXOYcGtsZOyp48Ct5XwVT5YF1lMWSnh4VtCUE1unaArrMrmwoPpFUHjqYtvIjPXkDnU9Ey24dWDdJTm6GnZn3f1Om7BQCLdjH6xqS4abMTn1Msy/5Ck6NLl5us5U/OW1i0ddtut/B1VMd1wzTBO9Ve8V5kUfLZX5hITTKHMQpPeqiTOKkicBsgRt/DtlkTsYb8t3dYl/SqwwIDY12HNk/vdeUMsIdgKMGVXnGp/TiqrqCVPlIxcBF50jim6u1wdT68yX0yLhbxd2VuKs3iiqfzBvy3gLbLYW6fadBOIso3V2q3s1NitISzNsPh4ZsKYdhnlpJlWRs3Zve4uunlBe/KwgnCSaAeX3Z9SPzTPxhI0Ys3bynVBnjgZgnF3dM2yxpz1LRiv165gGilEC0UeBX/lkx21IfZ7HuChH4bUJlyLlCQSKDQvQmxBtTWJWvtrBeae9d62csyoXJghKjDDRDVlbdUh8rCdm3kMghqDAKmGbqwiUvbGqk9cbKdehNttvWQUfs+46KrZDPoeay4FjqZdlh5veejd1lE74jf5Vjh7uV/Vu6MuarfqBrYa5Jhv9fUodtpGt885xQYWlqb5iKvMuEF92cLZ+V67dF0/OtrpFsa3Zr2PwbZ5vCYuYgR2lkhpwBTC/JKyCMCtYBWNtLOb+ytPVtBE26nzRe15pAPdjqApQ4GirL2KqWtnf1plPJ9fe+DOKOCASeQyFxqxsxzKl1b2QNcn0164tTOH0sHFNdS9cSuTDKqt58noHt1zhGWQK1mlN3OQt/sIszBt03f0uOk8sKle16iyZPhjQXpNuNzCl2HVn2hyB6PBuWPABi2wqvjoYwlNSDaMD/haWR31eWRYN0e5rZQ+g9Y5YwV+OSwxdlAbwV0xc4DarSFcoCO7wpfLTeGc5/AK4WVb8qFuKdnedq31qh21va4xi3a0T4q8OktqbyL1PDysEYTDeX0PUaOyRgu7EMLWvXJtF5A6uVZbLEO9pbADM/TtyNwI1c/moZ9cVO7IUHKdrkMiHTkestYBKde5D1C6Ww8+k4v7ulcNaBOtLkMvX1gNxaBGy5otbefb45UKk+y0xIl61yDRdrc6yakGgAZl0NJfiqSYHzOCIxFfvPHSMiCuHI91fi8ut0av4hGABi2Ex94mKn/hc6sNPdcuc3urzRG6wPdnYskj24URHg9WvsGkDll06wPF73SyRTxsLhMjqlHrm9ymkOmLSwKv0etxp1ojhkPt7owX26VAcCgF9bIPtqILFzMLy0F61IfC7W6Dhuxy2u6bC2gFQal7C5nCvV0x1g50EjLWrMChZy7jV3WPbC4mam9xawF7F7FcDtylzOprIs5ZUr8OZ2dV8EJ0BMXahCE5WGuZa2TLC88Ehhuk5HauFewEx3VcTC9XxHV95MRQI1UMFBhLsCuCOa8yAdRd0y/ZDuXNjXzl0J2NyO182QoLAYahTdWsTsfkhJ7m+A2R8oYP2aEPN61hna2QV6Q+pOnU440hdOhcxiSCr0giQRO8WOVGUiT9QFUc2Kte4IJwFg0erGyyW2PjnHHJ0rnREDlH9JC2Le662ntGdU3UDBmJyzkkpV2AoRjfXBdevZ9vCoYncfNAFnDiNB1rbXK4UKscEgwx9L1bE57WBLTdRgq8hpVNuVgWksbDCMzTxnVZRpd5keyrPV9RMBSh3Dq8eqZ/27InHA1wBKt3dbBXw+DsbQ/OoaRp+u8vn16mw+jnkfJffHk8ne/9rx0zPk4E314z3Y+TA8f/cpf15a8q9tOnl9qLgVqPY9Um7aLn8eM/HKp+/tdeUUw8xse72enN2NC+ncW3TjT9ptFLnPtd09bjt6ZIu/vh7qcXt2um33hovj0PsV/uBmbldCL+DwY9j82/tcXTpuBl+q2E6ZVP4MdO+3YZPQ+cP734I4gZGFi/oQT+LajLyeTniw9g6eIVfkVefv3/05g6v9clAAA= -->
