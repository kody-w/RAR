---
name: "rar-cowork-cookbook-scheduled-brief-perform-ledger-settlements"
description: "Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_ledger_settlements", "rar_sha256": "49374b27c0f7d0fb8e9c7e93f97ab7f45361f24d9839c007831a62df4ca7ec2c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_perform_ledger_settlements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-perform-ledger-settlements:237f2333821d02ea3effce14728247358f60e127e23e67ef58e7f74cef01939d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_perform_ledger_settlements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_perform_ledger_settlements_agent.py` is
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

Perform ledger settlements Scheduled Email Brief — Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 49374b27c0f7d0fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_ledger_settlements_agent.py` first:

```bash
python3 scheduled_brief_perform_ledger_settlements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_ledger_settlements_agent.py   # or on stdin
python3 scheduled_brief_perform_ledger_settlements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform ledger settlements Scheduled Email Brief — Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_ledger_settlements',
    "version": '2.0.0',
    "display_name": 'Perform ledger settlements Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-perform-ledger-settlements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e741da2e7ec84b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/perform-ledger-settlements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-perform-ledger-settlements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefPerformLedgerSettlements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformLedgerSettlements'
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
    print(ScheduledBriefPerformLedgerSettlements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOj1pbnV2Gy/7DdyiqxI+rFixgtaEGAEAgJ4XqRZrns+ypw+7vPRVJmldvP3c89EzGqqEwB9579/M453Pz1xWxqPytfvryowEyRjRnHgQ9KxEwdZJl1WRnBX1lkwf+InaV1GVhNnZXVy+uLAyq7DPI6yNJxu+0Dp4lNKwZIkpVpkHqfrDIALgISM4iRqkkSswwGeB/JQelmZYLEwPEgrwrUdQwSkNYVAu8jtQ+QElR5llbBSC7rUlD+DYH8Ai8FDlJnSNmkiAPJ9ghc3wEQxf1nKBK4mUkeg+rly8//eH0J4PeXL7++2LFZVd9EBM5ilEt+CCHcZVC/iQDJxGbqwfV5D02TwuunvPCWA/V5Xv1Ygdh9Rf7936POLL3qpy9fU+T5+foy/lOgjKMqdWZWNRTbNnPTCuKg7j8j87gz+wpqWTdlWiEmUkHLpt7nx85vlLIc+fv47McHk88eqH/8+pJBEczR7l9ffhoN8PUF2gN+/zxSyX/86XOcdaD88advdKrGCoFdj8Sg1J/fntdPsnDht6WBe+f6d0j14WELfH35Trnx85B71BPufPkcZkH644NwXmYtSM3UBj/+9GdkoRvsKA6q+l+i+/ODsA9MB+r0FPyn17uR/4FMngp90Pxztjl061/RBC5/Z/eKPA31Z7Tv9v9PpOMgBdWHxf8puX+2YfJ35Oc/1e2/2vCKuF9fViAOWhgdMG++IL++qTK3/PkH59vNH/7xGyT935JRs6a07xTeEjMNXFDVb28//1Ddb//wj59/aHIYa8BM3poy/mc0/5ld73x+Z8Hnqh9/vxfy19IohWmPfEQ68muW/6/yt8/I2YwD59v96gvyfb6MnwkyKvHO9GGC73KmgrJ+Z8efXn6DSJFCbRr7/hhm+b/9GyIGdplVmVsjqp019Qg4dZCAUfiTH1TI6ZnUv6j7nSB8TpxfEHh3THcIEWYT18imHGEP5sPo8VGDzEV++d/2HVM/2U9MnVbvmPR2B8u3J7i8PaDx7Tto/OUzcvKhAFkZeEFqxogyl2XE9OCzkfU9SCDIfmpH7lCy4IE+ynI3Ik8FefwN+eVfZ/d2p/w570fFvqbQU2ZwB1+Q5FkJkRxirzkil9XX4BMEXoguZRbHlmlHyPijyT+P1rr4IH3a0IYFBtyA3dQAiTMbquAGEKxfR7DP4hYi5WjZKgriGHGCEpotK/t7JYLW/zIS++WXXyyz8r+mD2gmkEcFqqZwwYfAyKdPeQncOPD8+msKbD9Dfvj1tx+Q/0D+q1134iMPGRaLZwmCEvLqQUJgrjaP8jQGCgSiuy9//e3hklE6WKAQmGGBG4D7ZkjtW2CMGjz89O4kqPMoIiifnH5vN6TzoV2QoIbWgllfvX5NRxIZXFp2QQXejfjY/DD9u9cffEafVE8bQj+5ZZbc195jcnSmnZXOZ2TnIh+WgupCv9ajR/2sqmEY5yB1QGr3cKdZf3NhmtVIBTOpcvtXpKmgqiPlXyxIejROAuHKrH9BxKUMK18Wv1frcRHcnaXB6Phn2D5uQyLlDzDGFu8kPiMSgNZEcrM0c780K3Bf55qPiIAV730/JG4iKeiQsdbfA/ee4/fIk/+8y/joBBDu3pzcGwLka4OjGIn8/+9kRunnm43CbeYnboVw0km5PkJtbMFGzR9dG2wlnmxGAPhoL96R6B2jv6ZxAN1T9n97rHTv0fVY88C9poTCKHPlTn/M8/JON6hhjIxOL8sxrs2v6XsxeIVmhx6qRlyDqRw9dHlnOD59l9SH+Tpef2sMkEf4jWkBAxvJGysObMQFwLnnQO2XY4Y9nQEDBozZBlPC9n+nFQKpw2CA9BEoRAAtDq17N50EM2V0zj3sP5YHY7sFpXAaG0oLUwl8Ri5jZEMPVIgFYM80roFW+OFOCkkAtDEU8cPClW/mD2HGtvgpoDn6IkvMGnzvgedDGKVj1YH8PlIQUjUds4a27KATYIbdHp79kPPpKyhsMqbDfdPv3f3UFfm+av1tTEMo47d6ADv5ewh/Mw7E7jKp7nAES3FUwURPwEecPmr750d5ftT/D1m+/GEW+PGvjQv3gqv93nNfEL+u8+rLdPooiu818bOdJVMYI0EOqm/18ZGCn54J9+mRcJ++S7jfcXgY7Avy16T8HYlneH9BsM/oZ3R8JAQ2GOP3+YFGWX5aXD+R49OvqQK+efsZEiPUwcS2+o+K874Elh2vBN64+FGBqrFwdbBW3oHvXkE+IuKZLxBXU28sl1X2XR6POo3+fbjvA6Dho3SEfmds/DwwDkfxKH4FXr6kTRy/vqRmAv7KUDSCMQxeaJVxpoKJBF1RB+B+9dFcjRe/nwvvKQaxwcm+jJkGCx9shF+Rj572FXmfMu4DXNrAMevnsZ8eWcKl8NfH2o+h0wIvcL6r+3zU4DE6jW3cs73+oxBjgkGJbTCW9uwjY0eOfyACv3hQ+T8SOdy/mPETNqraHMslrNLPZH8P1VcE+hAmIcwrCJcN3PBHNpBPCYoGFmhnVPeb/b6plT10+e1uhvoxf/768g4f4/dHt/CIn5H2X+/tRuO+1+S3cbF5JzR2YHdb3zvZN6hnMNbe7x55YyPx9gjMly8QhcDry2jRMoDt+XAfwF8eckGFvvXAkALEk0/V2EtMYV5BSrDC56MyEcTC7xiMtwPnvn788uXPG+f/Fhi+4ATj4gRBzHDMQXFgEsB1bYCRDD7DSYagZi6NAgxnAE4AmgEuNQOMy5A2cFGMJVgHijNyS8ynOFNs9ApU5MP0/xdt/cuDEqwtOEVDUiRLMKSFMzbqMg7qWjPA2gxgCZdlTItxSYqgMRcnHXZGsDaKMjMCM2nccUnbZICN2yO9Zzv5EO/tvXV/99MDKd4gyibBKDxumvbMZjBIkzFpGxCoRUDzQGMxBEApyHo2AyS4m+Gx9emr0ZUPC4zxDDtJ2Me1I59fn74fY5Qm4cotWe3mj89yyp5N5sJYim+xJQ2ulEsfCS3XooiwfIsH2HbjWLt5sjKEap1ppb1zI5UvTDKc22hGFZuDv2LnKcNv2yYFm+1ePPNN7FWbMOAHPqHsiTNJ4TON447hmi7sJN2Htq818T6u9kUhlmcFXPQ1jas16mcrMu1CR72CGMvq22UynUqF2K/80zWR9/oB5qXdh0HimqA8KLlLGgOq36Ye0elrpeS1PF5SknUCguiYzF7p+fO5YHtrjRqaY1Lqco3vh9X0UqSCtWgOSuHIKUPSLlHSVNtZtssEg1m5x5bbZP7+dKbmtbHG65OZlKXDchdquztWVzrDXTJ0zXqJNWc1oTbJlRIuF9JtrrGwOhGzNddnEZ01mZ2UKGZXOpzR+g2Pra95uj6q+kGoznapKs2ZLC4ozq3XoKilMtqFMp+f6m11wyUpLZr8TJwY9JyX8bGZkWoVGV6/PvGyQvjgRsWH23qfS7zF87q69HnVifjKpuJiTzPnAxa2KWcsbCtKcG++M+PMOF+tnb5owEqlzBjX1ZPt8OrVnaCnYpVecq1YS5PW0M543fOXxEqSwymcJPMLH175GsXW5UVoLr4jczEPqiQ4MQmJV2dpWkgCr4oLGuQoyaN+GRjLrDxYxQZzJa2FTrNkfRiyjRrsCbu56Hrr0tzlQNgLS7aUXr6cTGbXNwM7iOfSuK2VQufD3lldd8wEvSYoXnjY3pxkvWYtTW4/pa50u9P5zpCbwhAN+zbNihBDy4QMEhwV5q56ux12V6AfMsNQ00pM3KnNOtDk+6aoZNkQDpt1cJ7pfHIdjugpO9aJYSmCyjutlrOWljsmGmMluzL6mmqEk3O4CbM9N1tP3RWYcGy47UsOvfh0O53vNu7pNrDiFuc7lssxuTWUTEzJy23d+hq2188KjkU9T23yc+GfpbCGP4IeDzaeeMXkvqMDaU7N9P5cJntcS+31vNVBRFJrK5V0jxlQNBZ2Vr+Mm3TT8JfZ5jrvF/VaMw6ZpiqHm4jvVv7m6JzsPtk1XsxpN0M/J4ct19ngQBHLQAxLFt/mGS5AuODKtbVrJpdeiGK6jGOGO1MetUcX+Eml0qSwjC1vOUrFwu6GEHNlqBeTcDqb6iuwb85+lJ7IfJO3WHy+GaVAQmH84iZqeBWYJW0MYaCE2/qo4ZdbtRgUYXaaTTv7LGnsJvX4tIyOQVGc5kdOWp5ldEgXXpRhXilQ7vV8ZfUmugz+lh8suqccV9ln1c1r2ksmUHtMamh9yUomUVh4ze8X/vlScgtuLtHFWTdD3i0sE/PxKIxh2nAKaIWjx51n3TH2c3KrYxI5JHzuAL7n28Vp2t9AHWvRWp7ivGrsJWcfT0K3X2zj07rQEn1Ca0scbBTqRvTLXWvNJUMVDk4U+3h/RZ08PlwlIeFMIbT6661MzQtXqfHhTGqTavDyzBoEaWHzFhDCidH051xqBhGXpTkuLdgIJ/KpboiV580ZsRQbka/JRe1i61BHg4TVykvr3ibQksPOIaaE6smMr6wwpmEnyzWPaxzhWEbRbev5RFI4imGIKFbKybqxG0AmR7w7Xw47V9S2phRJu8aqTqthcrzMT0O75fLFbTtQE3ZpxEdJuzjL6VSjpBgPPY9jTvxucV7adnaoJko6R8s5tw7E0u86kp9rWVZeeZWtLixjeQemVGdzoktiS6ttY7c68mkQYH46HKY2v/CXFhMcotlgaPJ+ejAr+3Agqdn17EvHWzObLVHsCtDESA8T2rkZCW8QpwtuufJQUW67oojJWrwWxPbCgMlJDXfFxGYio4TJpS1I1Fyngzt0fFdzzQSlHN/u9twOFMUMENE0nk8vZ7VlaFFg2vlMa5dxdqRyvd17JE8u9ErdRZJlMLthmS9PFmbTxelQNBjZepNboh1jyxuTydDWkxk72fI0Q7a517PZrTAbmDtKas7TOloEZs6ATt5p1aqLL1vreMI0b59hiyxenW1uTpT2oJFTPJBIrOhna6Pqj8M5whcpurgIJ2kP0UE9MFUoKKBpgqWdFdculG3FkAapKK9rA1voJZujQqJiecGx7Ylc88FK7rIVriW2sXWlJBUXhBHKiRbIm2q9FXPcpo+uLA8b40RNFk2ZdfWkNSfNIhaoOq7A4MVeelbjPb1Xb71DXRiC4Bhuq+5Q083wCbUUF+aJPDQFGi6hhfZW6AAdq4PkgK3VuX4+R7u0yXQ6i/bL3bXYBoGK1RJHqjHdMQArIM7khuhxvgRgbuCLPhJ7MKs2ZbMMzpPSi0OxuQjCrrBzv1/stpWU+3InynDIXF77C3B5vKpXmh9qZcSnuz3dFgNsFKrO1MLjiugkdaHILuOmDbvNa7HOl7v8cvMMl8t3C9KRQH2L8uW2j4OLuR8yJeyM3jjE6GJ6wDHxONmrtTm1Swu/OitClySt2necXgsZvb5GW+JKbXZd4MywcnOZTXOAK2t6TqzL1BdDlMl7LWBVTFECADZXP2JpX1xhK7RVh2MtiBGVxVVn9Vy5uF6kXY6VnByFBbOLt/NjL24ifwpHJpVgMzXyhk4u83ZKLOrQtJ0tkZsHdZkPwnxvBTMTj7apmQ2FiUNTycxcFo7sdEa64NCuFT9Fy1zjtsBLpxa6qTY3FGVlEGBDK+pq2bNSk2NgYAMhcg45K1gOTaeLlt2ejWBRCkzJLND1daVoniWtSJusm1jf9fhiFkjH5JKd+k02CbF+Kg5mHm4q74RK/OrMygX0SbfbXnuw687QQ9nZWffOPgwBYaNerpdKQJgLwd9GEEU1am03mBVGssdp3WW+I5jLDG0WnbSQDhirwJ5DBUe54BYq45znR4pKQHKK0/le5z2tnxu0et3QxqKYFiewUx3HquXz/JBUxFzoKUpQ9SFczbaKOjvnJlUl2VxS0F7RlbjKDLWxPLYS9MhYKpx/0JPYYy5HLwo3hdcXnpDbBwXTKN4SSTG/JKdKOStco+Q2er26npal7MLP8dveRSllIy8VwcCcRAqKWZbFmmInIm4rOCjKFPSMs7/utX2QGIArLgf74OI6OITmCrc8nmzJ/lyQWb/mG51Lbo7bn9Qgo7fFoY5QSroqYtjy4nStEUyY11riRiU/WRAXZbO1qW1GszVXLKv9dgkTdGiiSbame87cXwO6hrWrT3Uoyc6ZnwyWwNIzap70tiYUdB7uq2Q626cFRSdlWxf8BeYn3dOw29uj2R4W1QLC95LlyP64Mnb8EiVoTvDFWOqm5XHGzc4rnlL4XAyGmCsdu6qEltNNbOVptcmRg+ss+ZNTl/uFcNtYYhI0E9yDhfgyZzZrMVEtPBdp/tjKzgDMiOusmzwMV2JyNtZNcKuqerfl2JvtubdOjFdU0EZBNjclbljFScKWs0Uo9zt7klrkojluQ33CxLZxgNORq/u7TB3mnlzi54sPdhjB9uiSwFltMj0usTrizumV1wNzG3ULt8ONRNEdRk3oa6rb3ro2JvkFznTzzRrH0FnpoXGft8dd5PieiK+y7gxO3irFTBGju+XtOBiHlUz1NZ+zU0nAtgtM8WRvDnwmBqxpb010uqqEK6ys6oIbKBijSw1kKj3mCbGXOdTOa+samZtrZ54pJdANzJ7iXea3QTtIaOmK6zVLKPIm2zOHieMZC5TzB0of1HXE66QXX5OYmmjzetUmJHPZx0xsxW5s224+MUhWoAvXkk4oVQsNYQo9YDpS3NfusCarU0Nu9gzsu3eWcOillWPfLkER5SxOrfB0W5ihujUV3+/AaarEnWztU7t2FtINq0KMILALJdn20gt8nx+MWwCiHbeRJ/h1RSorQxn2+2ZGpJ05Wdl2t+Y4v7k0y0Of27ij4LyrYdeIVa0JHCaHKy2b89DFYl3MdKvA1/6MqUprqOelsGH3cmgvXVMHsONs2lsvy5A7wy5OM++6iC+XdlpuJ/s0ZltAU/Rax+gwZvbsdun0oEvRI1Ojazmg6M11mSqujXlqMwG8TC8b9Squ7BJXLtzAzE3NOYBdmCu3BXU6kJLXHI7TdWRvYXlC0YawSya9RgvYgxuNs1LIZi6ZZn8+HSTV6fEWaCSpJIoy7OiTKLae1bc7qZpchLl+bK28nexkjBGlG7E5qcJGtPW682d6alnnme/W5SCjvld0Z9j7Sle3KhmrEzfHlWINmRVneJXw5hZHrSE19QnAJvWUvt3QMJ7rjutPF6K/WLPNKq9n2xu6NRq3YkV/jTN6WHvCYbexlu1hkCydqBrBNQ9wmkeFVrgpzOA3VEPBWYB2r1Qzn7eDWBrkdjndUM3a2xzrwVMOXQQ8uVDU24bB0knVROEOrOZb3kwtVLodp8O+Z7XTMD16WyWUiYOw87v9oKNLq5FmjMgxS4Fd2rxDEemW8OT1sourtUD6LMDERGYtjFndaO4KvIm2wHeSIwM3m4qUxnEL8mTM8069HXB2qVwPztoTj6SOMb2jaSy+uYknue38A8cUPim4Q1lt6wmgloKoSGSD2+xaEIdjdwkI6lgHbMZG/jFRlzMnTTgXn/T4fKqjJiVZqXUJ3ZaDnXRKb7Kus2ZeJ4W3bu2vFgQ5q5So0udGShj1tK031/rGlJY38fTV4urUKjY0+FIPAVsQfJo0VGKxYL/iDizoYa0kG+e4mW1hWlBzdLXYT7N+IaArBqXF5X4xW21n/SFkC1/p3HCgj3u5SUBktPLQ+07Y2rBtOeI1Kgj+bWaxaeN0YcJYwmRD2ww2nN2VslxNtiuZpeyDdJxm6yM9bZptWdZoi7urellebkyD3lrDuUkYLjeHrcHqbacTjLO7DftJRzUko6PYkfSvk6NzPRbBXJtIZwfWNHcS3GabDI+AGBc01TPksi2m3JY0k8nJ5toADgt1DI7aaYXVcEQSykYW8YZyDLrC/KZo4yKSi5mSHXM2jechKjJyNt9ktMhdL2YTnMZwOYYairOW7ccaPmVwrbXS04m97LuNvz/7zmqayNHE6RbkYXubaRhrcqtZxAyLbr7EOl9eY9lyNkAUCQp3fwKnTbZxDqZ3WgldZglOIqteLoM+zqS0ucqhsJPapm4PqzZkzvR8Hs8uDlf3RNkYK2sr5IeYqTp2CCyv6ac8XU93cMI4hUk8JL56a25kddXcPl8UMhmLFIYPE2wGKwJrN3PquLKpy/aEe/4uPLm2vzgM6Fo9kUFH57M+7E/NoTWVG0vxhGQ7YeRYrRvYTUey6+lclm4lPUT743z+8vpyPxp++YKhDE6+voxHCM+DgP/Z62NvCPK3J02CodDXl/93bzIfbxXfjw3vxwLAdL7cuX/5n4j7j9eX0g6gaI9Xz1XceM/XmP/p/e2nf/3t8kinf5x7jyeet/r9fKU2vftr8CB1mqou+7cqi5v7S3DohKYa/xamenseSrzcFU3y+vmq+TvFxve599fsb3X29jijfxn/YGU8ywNOYNbgeek9TxBeX5weujSwqzeCpt5AmY96P0+zxte943HWy2//Bxs1rg/6JwAA -->
