---
name: "rar-cowork-cookbook-scheduled-brief-track-project-expenses"
description: "Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_project_expenses", "rar_sha256": "361cf831759605a496cee6d7a3badb675f54b7b5b6d4fafd24f433c588460862", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_track_project_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-track-project-expenses:f58748373dfde9ebfa2d93fe30176fdcaf856d13e99d8d32a50f722f63d0c227", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_track_project_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_track_project_expenses_agent.py` is
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

Track project expenses Scheduled Email Brief — Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 361cf831759605a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_project_expenses_agent.py` first:

```bash
python3 scheduled_brief_track_project_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_project_expenses_agent.py   # or on stdin
python3 scheduled_brief_track_project_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project expenses Scheduled Email Brief — Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_project_expenses',
    "version": '2.0.0',
    "display_name": 'Track project expenses Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-track-project-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7fcf107e421f4a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-expenses'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-track-project-expenses', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefTrackProjectExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackProjectExpenses'
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
    print(ScheduledBriefTrackProjectExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOj1rblX+Hl+1D2IytBYs4bN6IlJKERSYBA4HJkMRzmSQxicPu/90FSZlU92/ddd3REy1EuCc5Ze157H6jfnsy68rPi6fVJBmaKCGYcBz4oEDN1ED5rsiKCf2WRBf8gdpZWRWDVVVaUT89PDijtIsirIEuH7bYPnDo2rRggSVakQep9tooAuAhIzCBGyjpJzCLo4XWkKkw7QvIiC4FdIaDNQVqCEnGzAql8gBSgzLO0DAaorElB8Q8Eygq8FDhIlSFFnSIOhOwQuL4BIIq7F6gOaM0kj0H59PrLr89PAfz+9Prbkx2bZflNPeBMB52UQYHDXf78IR5CxGbqwbV5B12Swt85KKBOCbzkQDsev34qQew+I//1X1FjFl758+uXFHl8vjwN/0lQv8GMKjPLCqpsm7lpBXFQdS/IJG7MroQWVnWRloiJlNCjqfdy3/kNKcuRfw73froLefFA9dOXpwyqYA7+/vL082D8lyfoC/j9ZUDJf/r5Jc4aUPz08zecsrZuPoZgUOuXt8fvByxc+G1p4N6k/hOi3iNrgS9P3xk3fO56D3bCnU8vYRakP92BYTCvIDVTG/z081/BwhDYURyU1b+F+8sd2AemA216KP7z883JvyLow6APzL8Wm8Ow/h1L4PJ3cc/Iw1F/hX3z/3+DjoMUJvO7x/8U7s82oP9EfvlL2/7VhmfE/fI0A3FwhdkBa+YV+e1NPsz5Xz453y5++vV3CP0/wshZXdg3hLfETAMXlNXb2y+fytvlT7/+8qnOYa4BM3mri/jPMP/Mrzc5P3jwseqnH/dC+ac0SmHJIx+ZjvyW5f9R/P6CqGYcON+ul6/I9/UyfFBkMOJd6N0F39VMCXX9zo8/P/0OWSKF1tT27Tas8v/8T2QX2EVWZm6FyHZWVwPZVEECBuUVPygR5VHUX+XNart9SZyvCLw6lDukCLOOK0QoBrp7kNtgQeYiX/+XfePSz/aDS7HynY/ebiT5dqPEt8eut3dK/PqCKD4UnhWBF6RmjEiTwwExPZBWg9hbgkBi/XwdJEOtgjvzSPxqYJ0S4v8D+frviXq7ob7k3WDQlxRGyAxuhAuSPCsgc0O+NQfGsroKfIZkC1mlyOLYGqh8+F+dvwxe0nyQPnxnw4YCWmDXFUDizIbquwEk6OeB4LP4Chly8GgZBXGMOEEBtcmK7tZ5oNdfB7CvX79aZul/Se+UTCD3jlNicMGHwsjnz3kB3Djw/OpLCmw/Qz799vsn5H8j/2rXDXyQcYAN4tF2oIZreS8isEbrBC4rkSFBIAHdYvjb7/dwDNrBpoTAygrcANw2Q7RvCTFYcI/Re4CgzYOKoHhI+tFvSONDvyDB0AphtZfPX9IBIoNLiyYowbsT75vvrn+P+F3OEJPy4UMYJ7fIktvaWy4OwbSzwnlBVi7y4SloLoxrNUTUz8oKpi/MAwekdgd3mtW3EKZZhZSwgkq3e0bqEpo6IH+1IPTgnATSlFl9RXb8AXa8LH7v0MMiuDtLgyHwj5S9X4YgxSeYY9N3iBdEBNCbSG4WZu4XZglu61zznhGw073vh+AmkoIGGfo7GGJ0q+1b5il/PlV8dH5kfhtEbgMA8qUe4yMS+f87tQxaTwRBmgsTZT5D5qIi6fcUG0atweL7dAZHh4eYoeg/xol35nnn5C9pHMCwFN0/7ivdW1bd19x5ri6gMtJEuuEP9V3ccIMK5sYQ7KIY8tn8kr6T/zN0N4xMOfAYLOHobsu7wOHuu6Y+rNPh97dBALmn3VAOMKGRvLbiwEZcAJxb7ld+MVTWIxAwUcBQZbAUbP8HqxCIDpMA4iNQiQBmLPTuzXUirJAhMLd0/1geDOMV1MKpbagtLCHwgmhDRsMIlIgF4Iw0rIFe+HSDQhIAfQxV/PBw6Zv5XZlh/H0oaA6xyBKzAt9H4HETZufQZaC8j9KDqKZjVtCXDQwCrKz2HtkPPR+xgsomQxncNv0Y7oetyPdd6h9D+UEdv/UAOLHf0vebcyBnF0l5oyHYeqMSFngCPvL03stf7u343u8/dHn9w8z/0987Ftwa7OnHyL0iflXl5SuG3Zvgew98sbMEgzkS5KD81g/v5ff5VmyfH8X2+b3YfkC/O+sV+Xsa/gDxSO1XZPSCv+DDrW1ggyF3Hx/oEP7zVP9MDne/pBL4FulHOgz0Bova6j66zPsS2Gq8AnjD4nvXKYdm1cD+eCO7W9f4yIZHrUAuTb2hRZbZdzU82DTE9h66D1KGt9KB7p1hyPPAcAiKB/VL8PSa1nH8/JSaCfh3Dz8D+cKkhR4Zzk3Q83BwqgJw+/UxRA0/fjz33UoLcoKTvQ4VBhsdHHifkY/Z9Rl5P03cDmlpDY9Tvwxz8yASLoV/faz9OFRa4Ame4aouH7S/H5GGce0xRv9RiaGwoMY2GFp59lGpg8Q/gMAvngeKP4Lsb1/M+EEXZWUO7RF25UeRv6foMwLjB4sP1hOkyRpu+KMYKKcAlxo2ZGcw95v/vpmV3W35/eaG6n7O/O3pnTaG7/fp4J47A/bfm+MGx77337cB3ryBDNPWzc+3afUN2hgMffa7W94wNLzdE/LpFTIPeH4avFkEcATvbwfsp7tO0Jhvcy5EgBzyuRzmBgzWE0SC3TwfDIkg/30nYLgcOLf1w5fXvx6O/yUZvLoUy5AswRCO6wAOWK45djjCBQQ+YmjXsU2XpWhnRACOc1iHGJsU7jLjsUsTDm6PxwxUZZCUmA9VsNEQDWjEh8v/L8f2pzsK7CNjioYwBD2yXZYYMRRH45RJcrQNAO0wJmGZjkUzlEuRFmNRFu2Qruk6Y9IlCcKmWJakcZYeD3iPkfGu2tv7eP4enzszvEFGTYJB8bFp2qzNjEiHY0wojcAtwgaj8chhCIBT0EssC0i4/2PrI0ZDCO/WDzkMp0U4q10HOb89Yj7kJU3ClUuyXE3uHx7jVBMjGUv0tyiBY9MThjVWUhXRiL5OjX6bOdcq94Gn6LvIwTVJCLIYV0ymvASbU2jVejZHpTXaKMTWnc3jdZyPRLw8+LgwszgdtoyZh12viWD70iJqwajfUHPVqF1V1Feclcu5qmqHHTveJOw21q/bwpEX6GarmYGKYphG7PitcsyS6nKqHNhJ87C7wNnjWqmVRS/65tyfl/5mtN8aF3FeaG0sX6p1vI1q1R1NqF1xcfS4ErrDpfKPlLQn51TMFo56LskyjbBNfU3jEeq4TMBGVYsCZVGiXMgeN8Eu3o0vSTe31rV4OWs9S1XZpl8bnXo8c5MWwy2qMozK7MA4woWoojl8JhJCnOnA9by4GhXHkbiMx1jWL+QGFzWzrfWrQHpgYlKMwUMq70Z8FSdUciRz7VIoZryZt2PKJqXqcpCyvSOMPYKbOTV7upzKHbMWjDq3u9nGJZeJtQgzZUOfu1jodYuf+EYDTnkmU2q9pjPmIBJpNF+LNhMFY88TyFKTTgkYr5tD4YeqUVWHNkoL6TzuuXIHEupUaNuWOOljY2kXp1jTTeoyI3HOiETvMp7BzF6ZI2EUUcqp5VozX5cFZnSRLhYnMjSbc0ieYd/i+Wp1YpIyFxRzFHC9qBYUG+8PKGtvVgm5yUcWVxGFQoZqH+NNTeCN7hBRcul3RMDZxUHX5vr4UlH6LlSIzaYrx8alprOtnBTKbnFp0jadceMg6Oc+EMKz7/cxWGG2u7Y7dc36Mo4zO1tuR4cVaal73bDMNNomV8zgKom38ktaknVTkqRmnFsnNdJaCEReLRN7vN6I22qWpCOnS0dKF41Uniw5kb+uOfTYRGg4dQM3ba7XDEgFoSWbec8d2jDUr8yCw8TDbuZTeVpgqBcejUPgyEuXNwqtFtJSywOpu5qMmgR6yvC6pfbVfEea7caNPbzUJj0Zlyu2HpXhjjQo/uJM2+7i7vTDYqzl/lw7jrVZcd6JtlaRO2+7U4xVtBYSOVi5gRFtlsEu6LQ2qqSFsr3kl36f2KStSD1Jn+1N1u4PkFmTo0twPLUe86d13SntNkp4mTZAOLMT2b3o/TQBFJdrvtPEunElJkDc++lK4K5b7IpN7Hi5bVvswqqNLHD6yNboFt0fT021ChZnbS3izsrI+12rqOV2uzU1Zk34Yk/M2jGh4hsgmVjjofSprQQ5BgZZ80fnVPjCmgTsaFJJ16jGvIVBGNQGdbFgJDmK6oAK7/oFaoEIpALd584BpeKjxMjmTtUa3rgKo+1hEinmVe0v46UtrbUrvZ5t+1xsjisyOo4En+KW6WItpRfrSNtUJKNm5AYbxyH0cBEydLbexkIUHrFVWB+3Z1U9MlfOq92ePi5Sgdguea7iF/m6KJpQc0956GORLZXjejWFFdpvFdW3qUzLAT06KSjRB+pK6bYFZ2+XSh7W9pWOLREN58SBE6gdJ4Ewwg8UeWIF/XyMjLg6O7P5np2Oaj7U18xiUdPGiCFNUsI11gUu4WFamDTNhHLJyWnpy8fTtEoNnJemrLFuYzrXOWp9cmI/v65DZ9cIHH/J/RkVrs9XMGkCCqx59yBwDW/ahJGu92caBW4TGHV26kJwRrdRHnA4Hx0BbxgTfjU7jBZ12vHdJGYnc23V1kte8aKpbAaiLoeMnZMqlzm7Y7qbeF0yJ7Rq52yg0PgikWGq8KytLTy+KI4Vi2+NZLFC0+mpTieUXa/Mo5icz5o5M8bZwRjbGjBZTG4uUuqIZl+0nHueUZQbRUFj8buREhZMxq3XUiK6wmhT9uOjzcs4LU5T/cywUaOdiCNp1w17WvBLyqCr0nExYKAXJUTR6yEXXDSatQG92rtpGtOkMZuE3mI/WvNHqlqWBb8hF5urGuYFz85s0p9aPJnQQrOqPVXfsscjvggOVhUI6fqiUMdFt5DEI17YB39/npJKGJbsum0OdCKaoDvRkbJKSmt3sFfXKbbP0mnnTjOgeqJe08RanQuEnlq4LxhueWouwVqUp7S8AMqhMnqTCa77tDhR7jzWmrGbBNFoWwYTUvGd8ebqLJbHiYYmgtPGVbyvN8lqw9ISCzuwKB4wfmEedjENWVU8Xi3alGVFtpYutTrN/U7dJELXRg4lMAdix8yX8go33bxnFd2QcZgK8bTVAsi9ztpMY2KrSrsA9cR6wfKu4PNaoRAar5zk6XTGnsJerjQCNvTtkXVpV8MCvRR2wnSSxzth5FuL2Sa6zqaX7FQEh4BaR00e82iyEeBc4214ZnYiFVuZ6WssKGU/0sa6tW24tb7gw008nsQhdR3HjWVLVta3sb40JnlyjdAejjKjtlLwqS5f9FK88scaK2UZ7Ulclba0vF5uhBDfTvUJtmMEYnYoLKBMxMAux9doTXDJmub0cXLRLJUXAwzntFxeKakTbozjPuDhYIKCUkdXvMpbXaWI6GoLUmmvdNbFMU2YoW24WYWSq5DdUUy3dWRsm3xjr7BsETR0YPszdS0KnozHnR5rrZeJR06wnXyNjW00chU9zqehx2FKZjNCMW0YJkznrc3OjkI9kc8cS1wuE2e0LtRKlc4n2tgvr9drih4rTLdnTVSAkVd4YWqtUtwL9tcTRYlJIODtWHNTONVUBItmHZfMAsdMMMsbk4YyvXKmt5C5i4xpEj/v1cm0ifTqoLiuGkSph+G+nYu+YOf+YZ6AAzNms6WRbZLKU2AJ4ztVKcJta6M+JdvBqrvgl/2F2S+k/mrF4+MpO2SSJk5Gjdjlx/xCtPXZjNtg2QhLfcbPGdxE8Xp6EafifsRJJ3XlF1FIhZ5cEouTsEd1Nbdbown9XlcjX6gTcbqvZfNAp+dunpzHnIJHLLPZylOsCELOV3Y7pbPVglbjg9ehijlWz1NRNI3ONyaRvCV6KphGye4sxIExVvwTT1/2JqVHwnJF107EBbJwijOvmKsnaRaZihfOtqywNzBJB04pp9z+JKVN2I6dsxGeLtdMlek1KrfWflVAru+vhoPGO3aB5vi6PqI070xGnOFkZKXPrNopgq2y1gp+u9G0kXOw1pXcm8tw52Q07SioL4V+6na5KV4IYlVsmphNJlYPJ7LACnDJHQs6f1VIftqkAbeic7CZDrOUHK+qS6jHNrVuRIJfHDsfcI4EMzhAhatUO96kL6gQneVUPaUSkjHjIt9l+xLEROHnKx6YNT1Zs9OrteOj+ahiM6MOW34VKyuVwrHlZjRnnblpSKuM7S/pvjibbLOoI5kchSep3rLYylPnhdIeL/RR64XtNvXlrnKaetLvLtauTM2tWGBw7DpZwDzNG6s99B1JoDY1r4Nmp4FkxmtULc43QpQtNyqbVW5zNdfJbDNzsAU5E0B05Lh9iq81by9c+2JFUjzLM+45XGVyP/EO1liR2v2KItgK54kxZ48aQTsdNceDcwvuKM0CqpwYYkWYm23EOjvAa7FLRkajyORmIyo5o1HRRZ0Yiq4rvmcL/KXb7RboVgyugq5uBGvVZqd8RBl7QPlulsE4ttlkhk+xC9GdvWIfVg5nTRa7zTG7nHYGW8uKz5+1VUwL0xOppt5+qyWhl8QznoEcr0ZqjzJmJ6AzdMNkNNivYor201COR74r0ruMz9f2xuDgsMOrTrOBcxIKW8lstxjHywsmexuPLdirUm0iMrXoQhOJenRY9AsHrFOU3YcXBvYGB9ti9jIG+zOYOnlGatPyuqKkUzCvGIfipN7Zt4ZULzyc2eeZ02ezbaRoYo3SFA0WNF1cSiu5dgdyl+vBjuDJIhakhYtt2RlrRCs4qPrFLh+jBO0txxcsa/Rd2xPkkvZ7o5+Tsaic/UZcu4wElmKacVkgYppq9b5zgU162ftded3js7I84xEnkltu7TB7fEmj6ZzFIBFhpXropmCqGiYGJxMyAccRxxRpOnLP5n5ZZgd2Ha+ZqSPNEuIoo1aa6cHaUat+L22YnIywbM2ss1b03c5cxdZqpih53wiwK64OmxMxrRZ5v6TKPqMItU7UMROT5Wzhid14WxGZcZCaGTMZy7XRXGb1eUR03pLftRtgCPI6VrklOJFtlXQyt4y2Y3Z2Hk0xaOV1z174rNSvFCD4ZQucsDp1C/Ry3aWysCmmJwkN4p5LXAtMPXiM3EpOaHMC7jfcgqLFWcct0TrpVYzTMcYP2mLvj9FG1jw56KY4ioUnZlmlh3461gNGLIixvwjnsuNpxCJxCmZ8jkkgVGeR75iGDcwZyQQGijptTUBhMpwNJjUB/HnVntyAkjOZ9PRUD1xpj+NXPYypBtuk2Rmde7zYa2saDe2TyMrZVWVZtiFFXJ+1feDvXL5s6YlGBFg9m+wnCbZI9xoQxXaWLXt5tzClE7p2CF+aEVzGcASD7ndkWOHLi7fPjSJjmNWYOqzCLJhNLe9U8+UWbxuwkWZl1V62M7Qhj5uRNtrJ156NoWuk0FawLeOIlj4jGPwkE4IClCr1Wqnf0YfY9gM489X6pFmfjCa4uhLjE2RZzlhxVCaokjCjEd4t2pV9pICimeSCnev7Fjc2XTvhUGe8arTistliMY4S42O5z7BR1RjHrZ9VezS2qISZZqsrUJmIUM5oWI25hX9ZTjHpPMPtmjvuWSEkJWqymWUC7FCeQ5Vc5wjTxQRtQ9Y4GxR+jKjDesyt47moHEyTWK6pXd2O6vmEXTEuuVh4FFoKPaY1wtaq0qZwNg7NrrZuL2xmmMva+1hnSR+M3EkhFEwyvmLmTEQvp0NN51aJuVcssAoP2Jt9z2BudsUaXuo7jesIu02uedfmfF56TONL8wlFmrBqmd0VU0NTlBzd05fqqI+JRnXhkHNoRuKEFaLVQR2x9u4wa7IgKdSGI5ZlApO8XusMzY6C2kiTDQwrq69WpxYWyURYOmkzmZ2MAw+2POzD6TKdZhJt8NcjEe0qxdJdC2YsNztQ5mWuzdfhnl7iNcjnfTghnX1IFheTnRlUS0UzfTUv/I29Petz6urHUnx2TwmeisGOtONTJBxic+zhyUFOs9DsYzoOS7IPCrossJhZLTBwOK3tRQo29oILx1nbBua5qA7xym4qhtG9rsX0LmJJQRdDoJ7kOj1KmzE8khm26e8Lt6ymFMY1tZR7/XYCwASTlWysXred1+Ln4/lYTvfnruOvaHCso0ZmegUVSmu953o13el+ztTcsijKfU6w077Qcse8bI6TydPz0+0V79PrCKdp+vlpeC3weLj/9x8Le32Qvz3wCGbMPT/9v3tSeX9q+P4K8PaoH5jO6036699V9dfnp8IOoFr3x8llXHuPR5T/7bns53/vifGA0d3fWQ9vLdvq/T1JZXq3x9pB6tRlVXRvZRbXt4fa0PF1Ofz7lfLt8YLh6WZgklePx8ffGfT08Tz8rcqG9W4wrArS4YUccAKzAo+f3uN1wPOT08E4wvPFG0FTb6DIB6Mfr6WG57jDe6mn3/8PD2vixqcnAAA= -->
