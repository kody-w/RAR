---
name: "rar-cowork-cookbook-scheduled-brief-measure-plan-adherence"
description: "Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_plan_adherence", "rar_sha256": "57e2df6708886022d7934dfb783a77667bcda8eaf6ab782cbfe1f5c3df31bfec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_measure_plan_adherence_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-measure-plan-adherence:0794e7f06e98295d53556886391cdca4fb0e309fdbdc443c3c1468f0c1c5213a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_measure_plan_adherence`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_measure_plan_adherence_agent.py` is
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

Measure plan adherence Scheduled Email Brief — Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 57e2df6708886022…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_plan_adherence_agent.py` first:

```bash
python3 scheduled_brief_measure_plan_adherence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_plan_adherence_agent.py   # or on stdin
python3 scheduled_brief_measure_plan_adherence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure plan adherence Scheduled Email Brief — Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_plan_adherence',
    "version": '2.0.0',
    "display_name": 'Measure plan adherence Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-measure-plan-adherence',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49fd132883305a3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-plan-adherence'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-measure-plan-adherence', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMeasurePlanAdherence(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasurePlanAdherence'
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
    print(ScheduledBriefMeasurePlanAdherence().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxrbnV+HV+6Ptp+oSO1LduBEjEFoAAQIkJNyOavZ9ByHw+LtPIqmqu5/t+64nJmLoqC6WzLOf3zmZWb89mW0T5NXT65Pqmhm0NpMkDNwKMjMHYvIur2LwK48t8APZedZUodU2eVU/PT85bm1XYdGEeTZOtwPXaRPTSlwozasszPzPVhW6HuSmZphAdZumZhUO4D2UumbdVi5UJICl6QB+bma7kJdXUBO4UOXWRZ7V4Ugq7zK3+gcEeIV+5jpQk0NVm0EOINlDYHznunHSvwBx3KuZFolbP73+8uvzUwjun15/e7ITs66/iec69CjT7i6ADPgv3tkDEuDRB2OLHpgkA8+FWwGZUvDKAXo8nn6q3cR7hv7rv+LOrPz659cvGfS4vjyN/xQg36hGk5t1A0S2zcK0wiRs+hdokXRmXwMNm7bKasiEamDRzH+5z/xGKS+gf47ffrozefHd5qcvTzkQwRzt/eXp51H5L0/AFuD+ZaRS/PTzS5J3bvXTz9/o1K0VuXYzEgNSv7w9nh9kwcBvQ0PvxvWfgOrds5b75ek75cbrLveoJ5j59BLlYfbTnXBR5Rc3M4Edf/r5r8gCF9hxEtbNv0X3lzvhwDUdoNND8J+fb0b+FZo8FPqg+ddsxyj7O5qA4e/snqGHof6K9s3+/410EmZu/WHxPyX3ZxMm/4R++Uvd/tWEZ8j78rR0k/ACogPkzCv025sqs8wvn5xvLz/9+jsg/T+SUfO2sm8U3lIzCz23bt7efvlU315/+vWXT20BYs0107e2Sv6M5p/Z9cbnBws+Rv3041zA/5DFGUh56CPSod/y4j+q31+go5mEzrf39Sv0fb6M1wQalXhnejfBdzlTA1m/s+PPT78DlMiANq19+wyy/D//E9qFdpXXuddAqp23zQg2TZi6o/BaENaQ9kjqryq/FYSX1PkKgbdjugOIMNukgdbVCHcgH0aPjxrkHvT1f9k3LP1sP7B0Wr/j0dsNJN8ekHgLl7cPSPz6AmkBYJ5XoR9mZgIpC1mGTN/NmpHtLUAAsH6+jJyBVOEdeRRmO6JODej/A/r677F6u1F9KfpRoS8Z8JAZ3gDXTYu8AsgN8NYcEcvqG/czAFuAKlWeJJZpx9D4X1u8jFbSAzd72M4G6O5eXbttXCjJbSC+FwKAfh4BPk8uACFHi9ZxmCSQE1bAXHnV3yoPsPrrSOzr16+WWQdfsjskY9C94tRTMOBDYOjz56JyvST0g+ZL5tpBDn367fdP0P+G/tWsG/GRhwwKxKPsAAk5VRIhkKNtCobV0BggAIBuPvzt97s7RulAUYJAZoVe6N4mA2rfAmLU4O6jdwcBnUcR3erB6Ue7QV0A7AKFDbAWyPb6+Us2ksjB0KoLa/fdiPfJd9O/e/zOZ/RJ/bAh8JNX5elt7C0WR2faeeW8QFsP+rAUUBf4tRk9GuR1A8K3cDMHREIPZprNNxdmeQPVIINqr3+G2hqoOlL+agHSo3FSAFNm8xXaMTKoeHnyXqHHQWB2noWj4x8he38NiFSfQIzR7yReINEF1oQKszKLoDJr9zbOM+8RASrd+3xA3IQyt4PG+u6OPrrl9i3ydn/eVXxUfoi9NSK3BgD60qIwgkP/f7uWUerFeq2w64XGLiFW1JTzPcTGVmvU+N6dgdbhwWZM+o924h153jH5S5aEwC1V/4/7SO8WVfcxd5wD4jsAQ5Qb/TG/qxvdsAGxMTq7qsZ4Nr9k7+D/DMwNPFOPOAZSOL7r8s5w/PouaQDydHz+1ghA97Ab0wEENFS0VhLakOe6zi32m6AaM+vhCBAo7phlIBXs4AetIEAdBAGgDwEhQhCxwLo304kgQ0bH3ML9Y3g4tldACqe1gbSjl14gfYxo4IEaslzQI41jgBU+3UgBvwIbAxE/LFwHZnEXZmx/HwKaoy/y1Gzc7z3w+Aiic6wygN9H6gGqpmM2wJYdcALIrOvdsx9yPnwFhE3HNLhN+tHdD12h76vUP8b0AzJ+qwGgY7+F7zfjAMyu0voGQ6D0xjVI8PRbnN5r+cu9HN/r/Ycsr3/o+X/6e8uCW4E9/Oi5VyhomqJ+nU7vRfC9Br7YeToFMRIWbv2tHt7T7/Mj2T6Pyfb5I9l+oH431iv09yT8gcQjtF8h5AV+gcdPQmjfsvpxAYMwn+nzZ3z8+iVT3G+efoTDCG8gqa3+o8q8DwGlxq9cfxx8rzr1WKw6UB9vYHerGh/R8MgVgKWZP5bIOv8uh0edRt/eXfcByuBTNsK9MzZ5vjsugpJR/Np9es3aJHl+yszU/XcXPyP4gqAFFhnXTSCBQOPUhO7t6aOJGh9+XPfdUgtggpO/jhn2fIPHZ+ijd32G3lcTt0Va1oLl1C9j3zyyBEPBr4+xH4tKy30Ca7imL0bp70uksV17tNF/FGJMLCCx7Y6lPP/I1JHjH4iAG993qz8SkW43ZvKAi7oxx/IIqvIjyd9D9BkC/gPJB/IJwGQLJvyRDeBTuWULCrIzqvvNft/Uyu+6/H4zQ3NfZ/729A4b4/29O7jHzkj77/Vxo2Hf6+/bSN68ERm7rZudb93qG9AxHOvsd5/8sWl4uwfk0ytAHvf5abRmFYIWfLgtsJ/uMgFlvvW5gALAkM/12DdMQT4BSqCaF6MiMcC/7xiMr0PnNn68ef3r5vhfgsErTM1xl/Jg0p3P0DnhEBhBkLMZic0R27FN3LNgF4PnnmM5No5jNmYjODnzYBuxCRTBTCDKyCk1H6JMkdEbQIkPk/9ftu1PdyqgjqAECcgQlIs6HknBMyAdjKIONcdwx7OoGWZSFElSlu2YM9f0SBO8Q23LcxGPsDHHwxBwb4/0Hi3jXbS39/b83T93ZHgDiJqGo+Coadozm0JwZ06ZpA3MYGG2i6CIQ2EuTMwxbzZzcTD/Y+rDR6ML79qPMQy6RdCrXUY+vz18PsYliYORG7zeLu4XM50fTUqnLCWw5hXpno3TdGuFh3KDoliJdrpz7LI1SXOL3qUUl+UpbmGrR1HjdrsAJ8O1rxFsRtFy3XpuqrKFmq1VITAF2sdrG7VaTIg9gsCpI71gc9Th09JQ8/oaC6lKHosTz/ZHl0vbo1gk/NVJ1mTczcpKMcNmDqoOKvfLQDsn4qG1iRNMBJuVPYMH/RzxU1jI8ot4djdCHgiInid8agnbSDWU61FvS98OjwfzYqdXa0VypV2sGGJl+NPiqCbzGN1sESmLOkLGmn7WVvUa26BT8UQsyRVOH1dc7NhlhR9rMjsq5KmqxGa15gT+UNtUvvbI0DMuKsLpaoqsUxwudLRzUDzhlsvBXrFEGQctWUjLGWFMV+oe3unlpNnLPBy0O56IDCaK7AE5FAm5LRU878soRK6xcuKKYbLGcmR9IZDSFD3EOdYHKzm0vVrqah6Xq0HcKVnkXItAuh6ZUjROWy5TF4Gx92JlTwyCfTrqoVdl3m6r8iTKrZrF4ghbdVjs5tWwmLiMZByPdVvHuGnqnTfPY5gTZyxeXRBqm7bXWinJHs+jGJ8W/qoz2s7SinKpX/S6Us2VeEjK3uKm9XGNlMXFUQqDV3x5QKSKXseirfHHRrk6nVsQZUOYGmWRkussVFs5Wg3akwiB7csepXLBGM47heyNk7E+oV5qRI0lbcuVjux0Jae4lbeu2FZMkH1a8gXr6xXjrVWZMvlhdyy6gz0XzpWwlqcr+NCuug3JCJpWX6/85jCLguRMBEmd2/uJOXUyGFlNWlKokZkYN/jZFfTgkF5BvIYOn+0GOYibbYw6eowUlmo2aXZcoVQj0rZXIHPP9y9Ra/kW5meXs6RY2WnZt9msu7YZDO+n2jCwuASQxUNg1lwKs2OtWGeD4xNKNyZqqpx4uGxMgWOtCxdIBx0+XwOLzSdr4XDFN9tQt5tZYXfs0KYJH6Cb0zqf0/E0c4+s4JPr2bUZ11b+UabjBREbCsHt4LBWlraGhvtOidEzvCNCPjdWiaQbsKEF1x218VuxKyOcnDQOabmygQjbzOCIVafGhzZEwmPEzc5G3GvOFpNJgoxRXWDE6fLsLWZms1wfRErSpt5kY/DoKYqmJ6JcRDCJtsQuCea7/bkTt+HK0lW+4tkhCp1ws7TX+vq6o2WFn3EtQCkpraRM65YnmGEcNTxrFYlv58puDmsR4x9yZDHfTC4sN28jbC8Uk4hVZHc6ZTj1qCWuJB7UYTU7IsZZQpCLVl5IMj4r5MGEj+uO4S7rpJdlVuMvOglbdFPIW8zZGStyFqiLvTXQS32V+Y53gAfpnCbwOdgl9mo3ZdUpWPKs+Qy5iuGRFzd8Mt1nW183y97PTGpukwnciZJYqhJLmbQgabrmo3WbD+tlsyssrrD3kTaz9NM6sgl10egwXNekI2Vsuo8S61QZh3U4bOy5dzyjprMWUa9UNJMMnRV9uQxTsdjlob8YJIsvJa5B6coj1piGqr0RnyrZv3ZLvMCnM9wLJvlGnGRB78BudmHiaLM09WVDBEu80yIBPgTTXs0rZrl0tfXMmYgFfYzUTZ9xx4u570LCUw6yXNBnWpSoUtlKJ9KVT/Bxl8k9YtTVVNC29QS2470zASAC40vhSLdZz1yXK7hj9S1aC4zmx7RqhsjZjUyzwfV53AjTDbvw1XR10pOdwy9K5ZQk/lJOE+JcLRlWx9ZaQcT91tRnct/YkkQS9uIQaHbf7jpmSGypR91UMlHneqz3g9ReapR0M2M297JitWX5gTG5KzKZuXGcX81LiPXnapfhBzqHzVXmZRRed+sD5u3ttqsPK2btTVHUwCpkSpHthWomwHz6jMJbXr+qMLmrK2x+ttl6UeyTXSwKCiEspYhhKMQuU43z5d3guVdRlev5nj3tzZZwF7geEgDxCFHbzkFIkwS7TUsTaYVutfRnnNKjOjvpNshxdTDqa7KP5Zkokbjc0XrmaSXn29lS11q7Ry9kWAh9pB2So8DEcYy1nTOxAr9BtrZi4YdItoPzfBDLyk4KmDjlTj4TUn1elOz8quGHdb8Uuk2VHlLbyLwVme3o4KpbO+eg784mc45mFOuDPgTN+EPL8whJXyg8y+v0oA+4u1YY/hArBlq25lKRdAobbITFGI6JSfNSTz1OZ5c8ujAFRNv2IbdZz6QrL6S1BzqO7tIxGiLtB5v0j2V4OG8XYeryXZUuHXq7qsIpVSiIYQFE2O5m+aGzUrq2d6XN7vi8VVFuIsThcZceeNLODaLsF7mwWx0CsdtJfjbhi36tahxaZ0s02edseZT83cU7xlipUuwgS95a952aSc8ta0miQZzIno8EVVVX1xpXj8MkVA0s0sOak1VlWxi+TXcLqr6y2FXILYB9IrNvdas2MacUJs5h0I6SYKiIP0WMU9lzSlZcFHOhBjZCCYxU5y4+0RkBLkIy16NJpDAabJSWy/Hp5VrxC1+5XIh2sZSy5HB0A143aEwRjBDbcjpTHkyFTtd8HkpRHR7sQNhOzcNm3nIgZdCAV5figmyz0zSlraVCoILr5MZWyoSCRuxNdqr2pHlYNypMKIlSwhPXjSgP9MZ2ZK+j5aJgAzlcVhofxXEkbQyTOKSXNU5iulwhhrFqC8Qe5iloX8wSNKOeaRzpRuQ7wxSzgUoLml0WS3rvW3NZsz2lTarFgAZwKNC7Zs/uRGUuCytUzZA9KhqL0252vMRolvHH0pit4KUUc+ZVKQleKpHd6jpvqhWpHASsUtbOcu6vQCMjVxhans3VPNt0zKaUdB5J0hkMIE4MxB3iKPriRJwn5/NKAB0MHV0SAzb3Nb7YE8DHSrQBqZgpW/E0Vy1irYmVW5C96yRHZDFNrurEb6o1R0h8QnAd3p0jriF5Kg7zhLP2s9gWVyTOBNteWwugi3V3LSZeuenQ99RcxY47ozESWBYEi9lnUmqccDkILXaP0MWl0LrLvmLlPbc5efw122cr/UAvKz6B8ToUy4LsCD4nDN5ozkktOoY+TxHz0LF54s7lfrvZDzV/oc6bs0bHu+sVlkWCv1YnJqkkbX0MNO26nFQFb0U7hzBJZ09PwijInL4wxQLDthg/iHC2sMgqzUIrOhxPaHhmKI1g6D4J53uy8Hg6r4t1mPJNGZwzG0tiC2VBDtUzikRKvuEqbAKydKFk+hBNNtWkdYnsTJFJW6C9Xp0SnSwqZUGUOXplvAXV75fmdofD2Xa/StUZH1dSzhlWng15sOG51SY1D+XRsjKQ0HBobbZeKAb7bHIkc4I9WPzE39ZKPBBGdalOe8mHp9t0yXGpD5NTp1IQ1OsPfsy4hetbJ6tvzikM4nmA/YOGra5VsOiTxVXvUuEyoRtF7DiluuQUfR66aEOV7MQ3Z3R4nbaGx8kZljnljEtU/cwqhNuTnXQ9tJM0jU9tXmZYKVxE2w/rihZn2n6eLoQ2itjqmClX0FdMkNV2aSXAyRi/Ljqwkmuj2D4e7bIZlmxU7+jpXoroIyEtpM0xH87VQlgtxRjnp/wxd+SWIJwcl8odXS9YWNqVCJn51Dq6OFdrkWz5/Ta1DgVWq1HCWDq9JtfcgQiiYFdZm2QfrZchNl8rTqLDspGG/ITF5JPCoBoWuu4WGEpxjMPALLaXXrEG9VivrTObHWR2PiEBMGX9yaloaT4p+ktvyhg5DV1Zbd0MnR9m2Nw6dpVXbSlZCERyPsVPbicJ+blyJtSe9hvqPBORiNvypp6gVDSYtlpmjpCca15a9h6+a+mrcZjXVTappap2URgtMe4yG1Jmi8IpJ9XaELhUy5nsaraNetbuwuoiJrONFFFkOgUrQvFKTwmKbK7mUj4njgeifb71KsXeiFVOnNcihhtWXxyLCjfZwe2bS5vT9U7GcknsOYduqHa2IuUNt5t64KoPcrly14ltzSemh5OujsyoKsII50Ty3E6gJhyS4MzcWeSb/bEVLuV5L9mJOKi0ZV1wdih5jg66eWT3ZudbuLCPeNCkzxlpKzMWRterqyrjdYQTWAJ67pOWefbA+g2Z9NKQm7LY0ZUAGlvlWg6TA0z12UZlex5VVqoRZLONe8LTLOuve6ZfDe5kB0dTdj9gp70xYV0Zw32THmZNO/FLIiSOmK4Uy9UxKvcYMCR5vYjUojO2Aljg+G16sbpcD+bNekagyTSLvMqb1La7JfYJdlp4nbbdK57lk5pHzxwadTJK1raK0yI4dWaGkF531VAPo4GEEEMjANYufaDccmPbEiZj8sY8DRQt7heriZl4so+fcG3V1Yt+3doqh7IVpjvMVs8xu/YmLKUufHy39RLSaPYnWrrYmYBcl+xMXXjrHWnjdrlZVLS351oKXea9NuPqq4kn2Ea3PWkxO1TrU+dn4YadnrrrxJKy0wXrIgbekL505arCqmYUcdn6vi8z2iJuGVtAB38v0ENeB+WGmVxsrU9cbKsm11k/YWJca7lLeGxRpHEpkmIXzTXTfIqj4EM9SMurCYSVECFdwsyROWwrBHZxhxQF2Vo6llLFk9Zx3N3EVjesdMqHVKJdOl3W7pqp8/1umon+bhWSS3hCIHIzT4ZVKzuevT4w+FlYXsq0NdC9OZGxRCd2MIIVFAC2sxlgPqx3881KKxnM7zwGW4h7m6U8m2dO6Bzl2P36ACBYDmxS1sPN5krKGLcrJ6VBqWlHbIoWlhDc3wQbC2P9eoMhLTqZ6QvXauspahVIdppk1ux83TrzSzWHy02yqNALLu4Rz5GQiY1bl6MZzDFn2WyoybI+OfaSihTUO1Kz1XwS9Du7v9SS1UrIfAOLW12ONzrL5/5KZkiJ1AcBo87o8mDp8ppBnHruzLjT1QuHmaiddhceuTpTWdMuZ35r1JjnKT1JLgeuajVdEnZnq7SIQ0GTMjMJedkh9tv5Uh/IBV0CGF2v9BO9yqhslaukMbt4pxhuPMu7WKrjz+fy1awW+uYaSdQGk/Ri5URLsFZc4k1pzpYEERDx8rxlq4DfCQAHiQudKMl+ekjh0Vu4nbDxWk5U9HKIZTXLM3NI8CSp8SES8KK6JNSWmXrTA2evMpuvV5NEzydXxrSqVl7JdddYle33k6nRxzC+zrnIK2KtrfYKT5LCLJwdGVGfGqalUVVqLAcmO3W4TU/8lMYv0imhw0KK22DLOJekZr05GzgKsRrSbHY899GSCitpT8y1yqFkSzMcbSCXXVKsOLTh94vF0/PT7cj36RWBSXL+/DQeEzw2+//+NrE/hMXbgx5G4cjz0/+7ncv7LuL7keBt6981ndcb99e/K+qvz0+VHQKx7tvLddL6jy3L/7ZP+/nf20EeafT3M+zxFPPavJ+bNKZ/2+YOM6etm6p/q/OkvW1yA8O39fj3LPXb48Dh6aZgWjSP7eTvFAJvvLxybbNu3pr87XHcEWbj+ZzrhGbjPh79x+nA85PTAzeGdv2GkcSbWxWjzo9TqnFbdzymevr9/wAHSlLAticAAA== -->
