---
name: "rar-cowork-cookbook-teams-update-define-service-workflows"
description: "Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_workflows", "rar_sha256": "a2d15774f1516abd0ccfbd96a9aad2cab9e2f75d042794f7831cf8c64221efaf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_service_workflows_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-service-workflows:0014207c2a1aace14f00fb3407260a657a74d3d81d92ec658027461eadbb3c1d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_service_workflows`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_service_workflows_agent.py` is
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

Define service workflows Teams Channel Update — Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-workflows
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 a2d15774f1516abd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_workflows_agent.py` first:

```bash
python3 teams_update_define_service_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_service_workflows_agent.py   # or on stdin
python3 teams_update_define_service_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service workflows Teams Channel Update — Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_service_workflows',
    "version": '2.0.0',
    "display_name": 'Define service workflows Teams Channel Update',
    "description": 'Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-service-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-service-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57c6689ba0876cd1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-workflows'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-define-service-workflows', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineServiceWorkflows(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineServiceWorkflows'
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
    print(TeamsUpdateDefineServiceWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aaZfiRnf+K0rnw9ihp4UWJOj3+JwgECAEEkhCQvL49Ggp7fuKcPzfUwK6ZxzbyeucnDDT3Vqq7n6fe6uKX5/Mpvaz8un1SQZmiqzNOA58UCJm6iCLrMvKCP7JIgv+IHaW1mVgNXVWVk/PTw6o7DLI6yBL4fRlabp1hZiIAsykQmzfTFMQI3lW1UiWIg5wgxQgFSjbwAbIQNiNs65CqtqsmwrpgtqHTJEgrUFp2nXQAmTumPntYmGWDuJmJVI0gR0hUAjTAy9QBHAxkzwG1dPrz788PwXw+un11yc7Niv46OkmySl3zBosb+zlO3ftnTmkEJupB4fmPbRCCu9zUEJGCXwEJUYedz9UIHafkX/7t6gzS6/68fVLijw+X56Gf1KTIrUPkDozqxo4iG3mphXEQd2/IPO4M/sKKUHdlOlgoArKn3ov95nfKGU58tPw7oc7kxcP1D98ecqgCOZg4i9PPyLQAl+eyma4fhmo5D/8+AL1AOUPP36jUzVWCOx6IAalfnl73D/IwoHfhgbujetPkOrdmRb48vSdcsPnLvegJ5z59BJmQfrDnXBeZi1IzdQGP/z4V2RtH9hRHFT1P0X35zthH5gO1Okh+I/PNyP/goweCn3Q/Gu2OXTr39EEDn9n94w8DPVXtG/2/y+kYxhc1YfF/5Tcn00Y/YT8/Je6/XcTnhH3y9MSxDA5StOKwSvy65t8YBc/f3K+Pfz0y2+Q9P9IRs6a0r5ReEvMNHBBVb+9/fypuj3+9MvPn5ocxhpMpbemjP+M5p/Z9cbndxZ8jPrh93Mh/1MapVmXIh+Rjvya5f9S/vaCqGYcON+eV6/I9/kyfEbIoMQ707sJvsuZCsr6nR1/fPoNgkQKtWns22uY5f/6r8g+sMusytwake2sqRHo4DpIwCC84gcVojyS+qvMc7vdS+J8ReDTId0hRJhNXCPr0gwg1JXZ4PFBg8xFvv67fYPPz/YDPtF6gKO35oZHb3c8fHvg4dsHHn59QRQf8s7KwAtSM0ak+eGAQLhL64HrLT6qJvncDoyhUMEdeKQFN4BO1cTgH8jXf4rT243oS94P6nxJoX9MOM5BapDkWWmWQdwj5oBXVl+DzxBpIaaUWRxbJoTg4VeTvww20nyQPixnQwAHF2A3NUDizIbSuwFE52fo/CqLIZDXgz2rKIhjxAlKaKys7G+lBtr8dSD29etXy6z8L+kdkAnkXmIqFA74EBj5/DkvgRsHnl9/SYHtZ8inX3/7hPwH8t/NuhEfeBxgdbgZDQZ1jGxlUUBghjYJHFYhQ3hA+Ll58Nff7t4YpEthTYR5FbgBuE2G1L6Fw6DB3UXv/oE6DyKC8sHp93ZDOh/aBQlqaC2Y69Xzl3QgkcGhZRdU4N2I98l30787/M5n8En1sCH0k1tmyW3sLRIHZ9pZ6bwgnIt8WAqqC/16K9H+UJQdkIPUAandw5lm/c2FaVYjFcyfyu2fkaaCqg6Uv1qQ9GCcBIKUWX9F9osDrHdZDH8NBrqxh7OzNBgc/4jY+2NIpPwEY4x5J/GCCABaE8nN0sz90qzAbZxr3iMC1rn3+ZC4iaSgQ4biDgYf3TL7FnnLv+op7i3I4tGC3DsA5EuDjzES+f/vUwZR5+u1xK7nCrtEWEGR9HtcDQ3VoOa9B4Pdwm3yLUm+dRDvYPMOw1/SOIC+KPt/3Ee6t1C6j7lDW1PCOJHm0o3+kNTljW5Qw4AYPFyWQxCbX9J3vH+G5oDuqAbognkbDSiQfTAc3r5L6sPkHO6/1X7kHmtDDsAoRvLGigMbcQFwbgFf++WQTg/jw+gAQ2rB+Lf932mFQOrQ85D+4IUAegjWhJvpBJgWsF+6x/jH8GDoqKAUTmNDaWHegBdEG8IYhmKFWAD6bBgDrfDpRgpJALQxFPHDwpVv5ndhhib3IaA5+CJLhnj5zgOPlzAkh8IC+X3kG6RqwuiCtuygE2A6Xe6e/ZDz4SsobDLE/m3S79390BX5vjD9Y8g5KOM33Id9+VDTvzMOBOoSBvAAHLDaRhXM6gQ8AghGwq18v9wr8L3Ef8jy+ofO/oe/1/zfaurp9557Rfy6zqtXFL3Xvfey92JnCQpjJMhBdS+Bn++F6fM91T4/Uu3zR6r9jvjdVq/I3xPwdyQekf2KYC/jl/Hwagf5DaH7+EB7LD4z+mdyePsllcA3Rz+iYYA0CLNW/1FZ3ofA8uKVwBsG3ytNNRSoDtbEG8DdKsVHMDxSZcAcbyiLVfZdCg86Da69e+4DiOGrdIB4Z2jr7queeBC/Ak+vaRPHz0+pmYB/crUz4C0MWWiQYZ0E0wd2SnUAbncfXdNw8/u13S2xICI42euQX7C2wQ73GfloVp+R9+XDbVGWNnD99PPQKA8s4VD452Psx8LRAk9wzVb3+SD8fU009GePvvmPQgxpBSW2wVC9s488HTj+gQi88DxQ/pGIeLsw4wdYQFAfKiIsxI8Ur6CcDmyinhHoPph6MJsgSDZwwh/ZQD4lgEgP0XZQ95v9vqmV3XX57WaG+r6w/PXpHTSG63tDcA8dOOHvdW6DXd8r7ttA3Rxo3Pqrm5lv3ekbVDEYKut3r7yhTXi7h+PTK4Qd8Pw0GBMWrDi43tbTT3eRoC7f+lpIAQLI52roFFCYTZASrN/5oEcEwe87BsPjwLmNHy5e/7wZ/p+Q4HUMfYKPaRs3MdO0AUa647FrEeSYxqmxSU1okyYdwplizgwHNjWZjnGapDBYcSyLsDEHSjJ4NDEfkqDY4Auow4fB/3dd+tOdCCwh+ISCVEzcwSY0TbrYBKNMyxnbtms5M8qcmaaD26Y1A7hLT5wxidMz0qWnBGa7U5sicRyDXnIHeo8W8S7Z23s7/u6dOyq8QTBNgkFuHNpjatMY6cxok7IBMYYKAwzHHJoA48mMcKdTQIKbBe5THx4aHHhXfghg2B0Oyg18fn14fAhKioQjN2TFze+fBTpTTfq8sy7+eXalXJ0Lp9lWlrKcxJVxekqDoKfTLHLC0WkcYSxJzbd65DeMxng7ba1jSRUvJ/P0ul0SBN3wS25xtijreJ0qwYURr6A10DQt64idy+EFL3K71yq+RguJi8oTRjZ7QogvWhULmGmXiQaK8WV6puT+1PDEmSDVcNxMSr4/utE5UC/KWq12EVdiQsZjkarWl9xssGiXHoGp8omqUKXEpYV8JX1MMPJkm8vtOsGqJC7YrFb7zA5PFDikGDZrlWjmxCF0ZzAzK/eIrqjyJAXcQmx9vi9rOcZqoNWYmi95LOW0tTte7maqturOdVD4UzlUbDnd0SeRsPnoislXxguLnIr5mKzPW/6it/qp3erpSQ0SW2W2IFZDBq2368k5yC0FLPiaKsbryki3ZcrSFdR8trGkaoTV65Zq5VDQJufdRiRzVdt6VXVVWIM+26auVOqxCGXNaEmTjbc4WKPhabc/q1rglptzxW63jhVFBMyqYN/YpV/59nrWnMpKvgp5XO3lcbOazvaUZ0xK1cyP6G6hxXJYElyucyo/ZhrzoBlLnT94+MbSxFqrDZEdH7WVIUQtKvg1H04IlaqwbbfJqVTxUnndcNE+SsSyWWKH1bk9LyQLPV+6TDyuy9Tx8SPe1pcFfbZCz2nr7rLLfHXExGFKab0UMLTSBdGa4NTQM42RfFaLqyC18fQIJOEsmyeT5e0pOaq5VLiYdXg64ftGR7s0rEh13Np5WC+7zbiyd8V6Hl+LtTbO6eU2hRlpFLvaUFUnnFhbq7tUSru4iNdEZkOH31QlvyuS2rAdTDirK8FVBREvDkWfGm1CNocTNW47TenOs6lAkwo+HUnm5mRY1AFdrihXtjaUg3Z2K/EzbYX1YL4tZ61kdaoQxNjJiY2ql+UC03K1PJJkEBqV4AWJy5o+xnFSMuZHW847r6JcHK8qkKv8JGbYsz0/UsuOiC2GjFWbFD2Ni7mjPjeZesWqQngyJbCQGwmXWH27x6Kg0QNqcZKUVexoZiduA3JGpza/6xx3hC/2OB6QPSc3us/uAl4Kx+FJSpQqP/tuVCwPvdEKU0yxuPxgFcs0ztAFsTJ520PHDErMWMuXLuLJptzVVRPcqmysne4q7HpVyxx6Nftt0W7LdsWG4sE8pquS6xjNS9F8fabtFXOeYfPpBnUoNgs5TonM7ZFFjYLD+FqdrVpqdIxainO4ek7tpbVL0J1kKrxeXrskUPX2uovj5FrSWoS5mLDryiQbw9WuNIobyr8cEk+LvcrhDVlU2/6krHCiWnhnr78IY/acAZfFcpFrYkxPytCet+hJnlrQjPyBjptxcDJzaTWT0dN8VIQ7Ns/qWeu789NscsgX9dn311N/IQJs3Fpcqeddl5rcOIoaLg7z674RTKOP0pOZnFXglQFXHfqy4e08Pa7CALT9pBRgv9i4mqTkeOgUedHuRg2vY8zcx3TNsI2d1S0Vt7HW7YwVivpci6MldzA9/2C76Irt3Hax32Q7m+5ZbjfNuIQnrifvsGVmlLLcEScf5+XMZ8OeUVjb2psnvlyzh4R3tFm+QHfRbCVNp9RhzqlXIzhFEzAhUXAZ9ye8oISzOy7s5EpLlwlDdBd+znQxwS/1NiLW0VlB42RfMh3oWJ+XR1IRkT1OO3m9JexpvmBlbtHXPMe1J1I0Em278/fO5BzCBm17lGWjTxOL81fnS8j3HElHasfIK+y6XV+PO15l6J1BnSaRQawS0k8NsW1xHKRGgO6vrBcvDLNfl07rbidnRtmR18ZJK1kJjpqmjMtV5KJJxxhLMOtEesGsz9wKmybLy2Q6cxydaNui75wtqKdpUE9PtbDcibOZmjLbOe8GUu+n5mG7NtSjrIEyPcnGmJmIFt1v8+1MiBJS3maCZLfdqrwYsXBeCTIniKMtjy3WSW5i/LJbLaLp1peIIzsyNjksSxsVBv++SPb1fk0yYOY70s6KI0Ies9d9LI7jo0MvnBFRYVVpV2smP/V8EuvdJlquG5hI1rFpUp6ka021+3UulN0km+kbfb5mNaIUz2LVcl1TX7xsYUBP0oEfLo8Ka7lNTp2E7ZgPN8AEB7EQrHI1c8LelQ2OXB6l1dyTrKZo+JEkne0NpekB7S98GZwI3K2j3YKJ6d1uTUnjiVrxZeDY494db5dd6Sn+We/3OkgytlgAcmMGCaCErTbujgYlhWiCFapG8tLCXmSU7lzCEytaS1h/d0xBh1mIxqTUrhXewdSxcCLi+WmDL+pjQgq2lza80a9lZ4tX7RJVvTHf8am+ltLYwYoM1wX5km0rUvFWx24qiXZ6DVosMEOulyHCO6Rsd4tgwRAsHlTbpTjVtoZn58ctAVfjhpeO69lhLcjHRnNrjXCLneYYV+XUCpW/61yqKU+TtX6dYpnA7Y4imMXFQY1a2xF9gTzlxZUVUCXzt9Qe29XsylDJsIj608Sj04s3p+PY0P3cl2XySOjGJMAMDvir1brs8iCjqh6WUXZXojkLOxicrFFYpjlzPE9NB53FI9wCK0nAG1EKJhPeE7ljFdD786lzleKMl1m2z8sLf+JQVDxEtTUtdJ7ZUtiWITjWwI8jReYoZ32GNZc8hDvLGLlaKtOuVFzi9T5lqXg2IkC66LptL2y6/QQ4G5v3krnJR0td34Zp5VTFRJO6AysVbHJZGt1lM3bTXYWJpr83e0ZQyxPfGAQVa8mRpTZLbKnZnBXLJXfejgtGoJ2aWkSgjq0JqoC+OPPmZtGe+fhSE+NF6K033Jk4T2F7Y5qiumxi+SQvWtktWEamnVNwnGAJSJQ4nS+03DtRc50666uJwRRolMyOY5zCC+OSEpJmeYeVPU7j3eQSgmWSg8WpZvH9kSYva8w/XeIqm8iN4U2nHBHljM96zTlJPAoAH4wYDTt0rmUwlwmtK+wkuohJG50lOvYL2OyF8QjmIcrhi4Qe182WOl5OBtvgi8seNpL7qMDA5Lq9bAy+aZ1y147zlDrya5PTzwtmNLZH+2K61Lp1jW70rhOicnXZRIszxS5tTZvaaEEdg+nFr9OzTF3xvPdZtFfrdU8THh8bCSp5WzK+nCVhArbiVurtxe7oTliSZxapMw6F+RRXUljUiVW+24lyMjlfvZBllJRwgXO65AKYHmztyIhwSeOSKoR4QiDOG04eH4i1qKgFtj2rjJxps1MymitZqslz68BscI8GXpqf82ZJmXKUJJkjFtstF2l2PrPSOA4dMqTl2Jb98kisZZpSeavO7U4NuG7idSpxcfLznnTZnRizsWyNir3GyC6qXgAfsR09ba7lCR/t8nWzyJtitk/Y/co2+dNhdRTHZV4ZoXmdk3MVNCMpW4foeq834Y5SNuTSDkd2MRKTEe809D7BtoonRRK5s/bFSnSmW0doZgdMbO1DZ5LJsduLTSccxvo8JYvpeV+KwUip11hhjZpMSFS3UD2BVxhDqiFQu8mpOQn8ZjPX13OlW/mSvxSOpq2SVzk/XvPFYT8R290qoc/YKJAK7wo8Fv5fnUc6u6qTw5qYRXO1yxdB7l0Os4oSD+vVCi6ETkacBtVBXodVslqKpLAfZVurHfWGTdM+zZ2lwhGpkjxO96eQzkRqVidwTSRwgrvd4uODI+DOntcMvHPqvXgsa04QmhqcRh02QVekcKEOFmjPmBI4Ld0wJmUcHIwUdvWBnBHTc9NP1W4ypQVcY0J6hnUbXIyO8cZMteYwC3HsVOaywFwTfcejc2+1uapKgzWAmo+ay5p2zaxPqSV/5kJB2fPGPpU27QW9WIstxTE2O/FiB1gheZjm7Z7WK8Yj2A2ahjlRZ9uZrGIEvj2MAd2uPF1olm2oE3QSuzyqgdTTrwItJj3pm32Hit6EYGsiJhKq32TTqYyiNYah3Yo+lt2YLl0UW6Iirtb6iJrMqLM6CTyLH00DWM7n7b7bMuOVG2BJwi5T5ji9elIzGS2cPTuOOlKsW0PVFWHBZLCckYGobthNvCeP+IKcLAMIeQ6NXxUIQdfWd4L5euJMGro2D0zHUKgmFzpX7A47czZRwnStrzZCK2/jeLq04fq+TXrGhpWftoWVwIxaxwMi2ZtL/QKCWRMdgiltmm20mzmNTShgpS0yhV7IG5Qbjcg5M97j2r7f0MU2Di/UVogsOi0OV0elShTHpimT+DsxkEddADwZtnP9CF3o1KZNDyXAyYAWCgH3VikrC96ZWMV1ucFPKl2JM602xztvomPUpAzUBjXJ05Ve7o9sPOJT63CcamQoXKpjzzacsdosFGoniDuNuzS4S/WJRPrkfm7GhdPC3l0o9+UOkw4Hup876/1oT1ZBOk8FcNw2JHHd63G7THWbVOpJcl1Ous261nvAJlVH1tRsJcxouPBIScenNpR38JkSLgxmvRFaXueJi91+lSyUDC/Gq5U3GWvzi+K753aFKQqhm/aFhzqzpNzkrnedpY4mNDtCV/VAbNnRNc1jw7fWcqehplQdSNcgr7PYaxVzIm1G5GSzcstCdFKsby2hJRZ24y/9jdXZOxQ2KGBjT21B7zxmJlpz3Yqnq3x2iUYEftjjpI85nXHc+X4ljrL1JDWWFmkB1Yqvyhm49ahe+cUG0NJ5ObZVMSvtdklJk/l4yfBobs4JPCLUZL/kGWq5meJiOCt8qXNDGEf8oWlApLsO4TX0iSKlkPRqqz1U2pIkSsuxOsgfJ2bKxG0IwZmOg+l6BNaAxqeO6dNH42pNtSPm2g02OutWq659knCWwoaYHskRRWxaXq8uLUHu0CkZ6WR8sJ2uMmjqVJnHyszEKXcy5iJYFw21vu7QWMeXmqUd1gvMsTFnymhbN1Cme+V4YPKFgrnuRlFQ2+QSE5s0VjhewEbjrMf1zKQvLpdd4cpTEDmMi/rLtROojVBe5sdO38gnbu9wkjGaXEwWJElKW9G+SQjULGNyQmP7S1hJ2THOLAk1FFpMTwtw9afuirHxywFsR9PO7uaVzbmdw6/qPWcfOKrsvXN2LaT0mOj7vrfXGzyFMmWibCWnmsHxiTfaV97UdTaavUEP+E4hlzsyIrd0WyvTnsWbM+fsUBg46ZpgsHh0xZxR57DHzeGwS4VFfFX9i6VnaCwzJ3QiG0rZpk5Iz9MNSU+Z3tMuXSWmMyYw1klxmS+cNl+zYLuSmmwapNfjSKh0aTRCCyUSk8m2CYkSLsdrcsbMcC5u5nEQzefzn356en66He0+vWJjiqSen4ajgccG/9/eG/auQf72IEfQBPH89H+3YXnfPHw/BLxt9wPTeb1xf/2bkv7y/FTaAZTqvqVcxY332Kj8L5uzn/+pXeOBRH8/qB5OLS/1+0FJbXq3ne0gdZqqLvu3Koub2742tHpTDV9Zqd4eRwxPN/WSfDiv+F6dgfhDkzp7e3zb5mn4WslwHAec4D5muPUexwHPT04PXRjY1RtBTd5AmQ8aP06lhq3c4Vjq6bf/BGczEVOLJwAA -->
