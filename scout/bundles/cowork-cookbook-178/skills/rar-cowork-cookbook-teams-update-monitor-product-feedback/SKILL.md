---
name: "rar-cowork-cookbook-teams-update-monitor-product-feedback"
description: "Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_product_feedback", "rar_sha256": "164cb46643a924dcb55f241434673e5ea40cd815241ff5cc46a38fba481df59b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_monitor_product_feedback_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-monitor-product-feedback:7c98a893216fb4d867400f6f0c79ad6210ca6619b77c957d5291f1dd7fcba3ee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_monitor_product_feedback`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_monitor_product_feedback_agent.py` is
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

Monitor product feedback Teams Channel Update — Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 164cb46643a924dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_product_feedback_agent.py` first:

```bash
python3 teams_update_monitor_product_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_product_feedback_agent.py   # or on stdin
python3 teams_update_monitor_product_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product feedback Teams Channel Update — Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_product_feedback',
    "version": '2.0.0',
    "display_name": 'Monitor product feedback Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-product-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f61b82d5d522ff0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-feedback'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-monitor-product-feedback', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMonitorProductFeedback(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorProductFeedback'
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
    print(TeamsUpdateMonitorProductFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjxpbvV2Fq/mh7qC7EDnXjRjyENiQEEptAbkc1S7KJTWxaPP7uk0iq6u6xPXP94sWjo6pYMs9+fudkZv/25HZtXNZPr086cAtk7mZZEoMacYsAEctTWR/gn/LgwR/EL4u2TryuLevm6fkpAI1fJ1WblAWcPqndsG0QFzGAmzeIH7tFATKkKpsWKQskL4sEzkOqugw6v0VCAALP9Q9I07pt1yCnpI0hUyQpWlC7fpv0ABECt7rdiG4dICGcfewSOAUK4UbgBYoAzm5eZaB5ev3l1+enBN4/vf725GduA1893SQxq8BtwfrOfnPnPnswhxQyt4jg0OoCrVDA5wrUkFEOXwUgRB5PPzUgC5+R//iPw8mto+bn1y8F8ri+PA3/tK5A2hggbek2LQgQ361cL8mS9vKCCNnJvTRIDdquLgYDNVD+Inq5z/xGqayQfw7ffrozeYlA+9OXpxKK4A4m/vL0MwIt8OWp7ob7l4FK9dPPL1l5AvVPP3+j03ReCqCFITEo9cvb4/lBFg78NjQJb1z/CanenemBL0/fKTdcd7kHPeHMp5e0TIqf7oShK3tQuIUPfvr5r8j6MfAPWdK0/xLdX+6EY+AGUKeH4D8/34z8K4I+FPqg+ddsK+jWv6MJHP7O7hl5GOqvaN/s/99IZ0kBmg+L/ym5P5uA/hP55S91+58mPCPhl6cJyGBy1K6XgVfktzd9MxV/+RR8e/np198h6f+VjF52tX+j8Ja7RRKCpn17++VTc3v96ddfPnUVjDWYSm9dnf0ZzT+z643PDxZ8jPrpx7mQv1kcivJUIB+RjvxWVv9W//6CWG6WBN/eN6/I9/kyXCgyKPHO9G6C73KmgbJ+Z8efn36HIFFAbSAGDJ9hlv/7vyPrxK/LpgxbRPfLrkWgg9skB4PwRpw0iPFI6q/6SpLllzz4isC3Q7pDiHC7rEXmtZtkA7QNHh80KEPk6//xb/D52X/AJ9YOcPTW3fDo7YGHbw88fHvHw68viBFD3mWdREnhZogmbDYIhLuiHbje4qPp8s/9wBgKldyBRxOlAXSaLgP/QL7+S5zebkRfqsugzpcC+seFTguQFuRVWbt1kl0Qd8Ar79KCzxBpIabUZZbdUHv41VUvg412MSgelvMhgIMz8LsWIFnpQ+nDBKLzM3R+U2YQyNvBns0hyTIkSGporLK+3EoNtPnrQOzr16+e28Rfijsgk8i9xDQYHPAhMPL5c1WDMEuiuP1SAD8ukU+//f4J+U/kf5p1Iz7w2MDqcDMaDOoMWeqqgsAM7XI4rEGG8IDwc/Pgb7/fvTFIV8CaCPMqCRNwmwypfQuHQYO7i979A3UeRAT1g9OPdkNOMbQLkrTQWjDXm+cvxUCihEPrU9KAdyPeJ99N/+7wO5/BJ83DhtBPYV3mt7G3SByc6Zd18IJIIfJhKagu9OutRMdDUQ5ABYoAFP4FznTbby4syhZpYP404eUZ6Rqo6kD5qwdJD8bJIUi57VdkLW5gvSsz+Gsw0I09nA2jbXD8I2LvryGR+hOMsfE7iRdEAdCaSOXWbhXXbgNu40L3HhGwzr3Ph8RdpAAnZCjuYPDRLbNvkbf+q57i3oKIjxbk3gEgXzpihFPI//8+ZRBVmM+16VwwphNkqhiac4+roaEa1Lz3YLBbuE2+Jcm3DuIdbN5h+EuRJdAX9eUf95HhLZTuY+7Q1tUwTjRBu9Efkrq+0U1aGBCDh+t6CGL3S/GO98/QHNAdzQBdMG8PAwqUHwyHr++SxjA5h+dvtR+5x9qQAzCKkarzssT/ZrY2rod0ehgfRgcYUgvGvx//oBUCqUPPQ/qDFxLoIVgTbqZTYFrAfuke4x/Dk6GjujsJSgvzBrwguyGMYSg2iAdgWzSMgVb4dCOF5ADaGIr4YeEmdqu7MEOT+xDQHXxR5kO8fOeBx0cYkkNhgfw+8g1SdWF0QVueoBNgOp3vnv2Q8+ErKGw+xP5t0o/ufuiKfF+Y/jHkHJTxG+7Dvnyo6d8ZBwJ1DQN4AA5YbQ8NzOocPAIIRsKtfL/cK/C9xH/I8vqHzv6nv9f832qq+aPnXpG4bavmFcPude+97L34ZY7BGEkq0NxL4Od7Yfr8SLXPj1T7/B4zPxC/2+oV+XsC/kDiEdmvCP4yehkNn+TEB0PoPi5oD/Hz2PlMDV+/FBr45uhHNAyQBmHWu3xUlvchsLxENYiGwfdK0wwF6gRr4g3gbpXiIxgeqTJgTjSUxab8LoUHnQbX3j33AcTwUzFAfDC0dfdVTzaI34Cn16LLsuenws3Bv7jaGfAWhiw0yLBOgoaHnVKbgNvTR9c0PPy4trslFkSEoHwd8gvWNtjhPiMfzeoz8r58uC3Kig6un34ZGuWBJRwK/3yM/Vg4euAJrtnaSzUIf18TDf3Zo2/+oxBDWkGJfTBU7/IjTweOfyACb6II1H8kot5u3OwBFhDUh4oIC/EjxRsoZwCbqGcEug+mHswmCJIdnPBHNpBPDSDSQ7Qd1P1mv29qlXddfr+Zob0vLH97egeN4f7eENxDB074e53bYNf3ivs2UHcHGrf+6mbmW3f6BlVMhsr63adoaBPe7uH49AphBzw/DcaEBStLrrf19NNdJKjLt74WUoAA8rkZOgUMZhOkBOt3NehxgOD3HYPhdRLcxg83r3/eDP9vSPDK+jzncjxJ4EzoUQHHsNRoFDLhyGd5N2AIfOS7DIPzHgtH0mxAEzwe4kHAhr7nkgBASQaP5u5DEgwffAF1+DD4/12X/nQnAksIQTOQCs5QvkcxDEW6PEEFvkfTIUHhFEkxLAlo4FIjP+BwGr4LQ9r3KcYludBzKQ4PQpr3BnqPFvEu2dt7O/7unTsqvEEwzZNBbsJ1fc5ncSrgWZfxATnySB/gBB5AhiOaJ0OOAxSc/zH14aHBgXflhwCG3SHszfqBz28Pjw9ByVBw5IJqJOF+iRhvueyO9bTY42sGOHsbk7xkd7zsGHnbHhomrVTlIBrjA8NoYLpil4KvW4qxkJxru1q7477chr6EXvYUu7hos4vJ6medOW2D2qGXIzZA2UUHgDqb2hojmcfKmuJH4mgpdBbrl8UlmwOblchozuEqzp4azZ+jNbnsxps+bXlsf6DLPt15vk5ooMxkdz3bXa7WaNWCeT4adolSO13u1Wxq2JtUPumsaBRZSMaZ4tM7QsaJ0T5J3ENmUxmlTCqa764cqxTLnF0XrHrNcmwdOtg+l60kL1frUToJ8npXVW3hVjuzdc56By7lClCGP6FcT69Kb1aOVrniomRKXyMzdpJkKgizFOAXpaAvXmZdCbNyj+0uryJewcc+jssRulorMmrp7kQdrxh6WuumajNpMz12iluDtOUWqhIENRoTXadJmXzdjN1qWi2WuY1u003O6tsd8M8N5c7JyZG3VlbkNnmHX5ceS18WW1vllwF5CJ1COqqNLsPi5Mv05bx3caIwRHV+aO15HNF4bUq5g9VyFgeWcszKSrT363WaogTsgOcnOaSPi11j95vVzpWPOtG4SwytJ661uKI9tKYdbSbXTaHNDkqgnfdjKbT9Tb3XWdCZCcH3RXRaR4qtYmITtyAcrZqgm4sEtksPnql0W6kn0Mgem5xGrKl0ouRzT9qljRnQxwC2Qo6xmY00oNjWPPE9x8Xa1OUSv9ArFp+pmZxtuDNFA5Ex+jVxiikDrX09FgWXz8Q6NNE4YnoeVfD9BU4sRuHEk9m1vK6p5truD7FEbDN+fd4G5sjbkYFh4xr8MYyDuORJn1Z8bH+mexNHxQtoTuGZxhYF2KjtVdCyY8hNbPqs9lh2RlPALZaELNcnVNANOvR7XQ6Uvax36X40PVBua8mWcyiUqGS81JWq4jyvWl2c7luxT3Rpdt6LBj72FkdLb0CcyEdBCsbZcXs1wMx0veVoos0rMRXSrXI46uZKWZ5i5pqfp4HUyvt5c7CuVmZyzNHdFUquLqYjH/ByH88oFWPd8c53y26dHOpEWk6oJHF4aZpIFz47cvKo0LbYMgdLWrY1i8spLdhEFba72KIaxD0n8wt6LkqXa36hgHqRjycyXO3OaC6t5Xm0xQgisYLFtvMdQzlQ3iRMrby6+JTFM3HMkZk7D9FuHpHo1Oz00ijppTufFd4e20tzeibLIxWraXEblgqXXCeSIQYYFq5kTTEsoC7aSyJiZr/bGe3eG/E133bzKcRH7VRRIPbailKtdrqKZtjMlAsnvSQRQ7miYov+GFaE+WK02ZTuqBZ3/hG/zs6ZNmNHU8w9etr6jPIFeRB1eyXU1zVTjnFrZivu1WN3KBrG7J45DNBiesxUOrOhznUwKdiJGJSpeNGZNG8KgRmNnJ3qWlu76bLEJnlCWU04lwH2mBnRDll4aDU35Io0Ukbr7I1pHAiFRy3R2V51mhofzDNciQnojo/9GQapujN3xJZrgT+Kc57AOFMfo77EgTC9lpTjW6so2bWhogvqdsKO8oW9riZrv9DieHYQO4nSBUU6a9HxypCtvMvGRQVjN+fRvZJO8WKX+1XDyzSDJTq+EWtYyXq1WpV9u1gcFsFsWgoT0QalkqCa1Uqphh0px4tPDrVcmZmfmoeSgBW47ReLbbNUhOWosqwZtTJdbrK0PKfo1DV3HZ83WzNRlxf2tFWPrjghgtl4DXhxxUTVNGvpiXbyVCv2Fi4z5bP97hiPtBwEYdhzPMRh5qroonHMlLWFoygY7ZI0ZXG9UorGneTb3cIud7SqhIo0ado4dOx9Ek022REFuwm/6haoFtKzExfKlR+b4SU5ChbosFXQ6IdxJknhcX+Or5YC3OksWu0DOTfM2XbOoClzmmm0r4j7UDimGSv6zEqh+7k5E4ymvhT1Qdrr8bI27Wg1W1K6mHbOktM27nG3XmTqwt8IqLKrj5RNalNmjfrZ+Hg+tMBbcJYXzKwyo3UtWlp70t/RMHsyTarEPR5tpuLa14Okrcy2WFF4a1m+76mEdr64vLOABcWE7Z1qN0laRjDBJspMz9lZu9qd1ixjEOQKdMJuFxve4mxEoX3N+jGt+aRDMPuGNRXfLLZGIcNKpXrziiywKA2MNuJXib7H5D1VUNSslc7BJU3Y6SiQ6omm5dVkX/DRXvCMpammozJcLHxFQJtpTViK5xoT9VBeNqx3bjXvlE2WBzEZCVdjnK79ZK4t1dViRsrWDJNHuSfmU4/JSne/PApUPVKsWNnP0InPykWtjpXcJfhNrE+2R3DcC9ML2pajztKaWZRuU5lUo9lEOwt8H7YJZx87se2E0tldI8U6rLbKhZpfaeOkE7RO5srWMS+nPbrfzQ5zFDNHneSZ+10fVniL7RwZ38Jo38XlHGMBocbqkm8vqpbAtVTQ4bPc5w2U16YXB+JWqaCUA4pANA52Yif+8TQbpf42nxzC1VFo8wBPzcXULVZjZuytd0y6Ou+lLDGNfMnl2qwxdcGU64I1tmF7XY5iTk9M2DwtWZSwsT1fGgtyH9HzujistzUVL8fkFK0iDkIpbkIkMgxgUhqKquFyTvKys5jmHlGOg204d678Qkoz4twpS++0VFs8ZXjXXrX8ps4dPKHyy7HfYaSW6/OpdqCFvCYaGECOZGhrYbEaFypXeAk+nTKLdBvC0rTPXKk/rxYFz3QXMz4K55pbXIXcnY32+BEPJGzMKMVq2lInKlmlSXuNfJE9nl3TEnk2p2XgspQ59snmXO1cz7M2W2MSrVdGn2f8cj1xdU0RtdH1MBGzvp0y7YkxdY1eCr21VLyxDsrIJGbOUZdne20id/iGivHjqDUJI6wODSnIK1ifVj13YvYCldup0u7smaOMZobb1GXSz1XnaJcbec3TC+eUbKcZLVFqcZDoda/OIkvJii3FteXyqI/a9SlPZXZ/8XGN1dIYHTslWvqKWus9rxpzJ3KChgHndWXVpoU7RrCNgSphJzxjq0DhizW2G+vldhn70oI5XymulhRPmJOoMV02xOaIXkA/gjQcfqagZS9NxuSmPJKGkQV7yQwbo6fN5cYNFuaYpnboVlAYXAJsvo7nnhnR6lzcc0uBWp2VQ2BiisCwmqpnsrebNxJx9LJQFdRoT6Ese61dZXkkKyxiBOOwg7UzPSRe0VmdiupZmTRrrqtweTuyxqDatcIBFeyqGOuCRy/nu4jVI7LcHb0NMcLGsrIl9qa+MySOhtVjsaxnZLJpV9Z5NW/TIJO7CrbsRHYdG1KqyLOG4I/7VVZMYOxelw1z3SuCpa3knhRJqpqv55zMoYTS4YpoB9Z8VevL80b0RE2Py+OYyIJVavpkOefWdXb15ueIO6fqqtTRYkkIpLOp5d4o1bPRwqUOUa78uZJsRHd22ec1ireG3G/5a3+eVGq/PEjihG3EK6ZOlmDcz2AKlceG2Rogx2D9GWchkzmSpksbWUkrendsZXO73zbRYiKYa8EcTTW5EdPYt2r3JGeTTU6ZqrUaEQXJUA0uLqyxzAmTtWquNsyIkmpwFVb0IR7r1Tk8Jww6mc5wV9RNx4TLdFUn+iafjY8n3eRK2mvQI+BxcmZvNwzKLK1JtwJgpdH4InDJq57Aki7bFz1oJ6QRFIaQTVRiosSpR7DqxPBqO9s0CgjPQORA2pE1fjWpYsIHfR16S7brx5hVYEnHJ7CvSLqFXIzyy6nZBF23ppNqOtaYasSmmMO31ooxrC1xVWYH+ySNNQ5GKWpdR9QCJ9a4ywaOGW677CKd/aueG8uRxnIhtzslfiPIseLMpkROoRNMmdALY35ylPMYoykaLk7F0IQrcj41+Dlgz85c8SKMImYoRYd7vQ7t03qZ8JkXBNvU2W6uRzU4ywEd0F0TM5vNtMcoLAy5MRgdufGKtTG+x1JvRTRh4KO8zHDnLcgA0NSs3xq5Y0ZMUp+afRVLWWUG+0Qi/TYP11P8MHLE3sbmibSLhZHE+FycJho+pg11rpSd6lDZIVgArjmMOtKvKduJxp1Jhx27S0++AHq8lAtxFbEZC7g9fZ05hrzu9VmatYtw5Jx7eQrQuTAhqHS/HocHrOzm6OUSNU2X8N3UTghiR4bOhsP9KoDtSj2PrvgatpBbnibn18gZtbNkU2ztxMDRq1I6rN2pfBVkEsawnL1YJItspvDnBSeczYOBNugchy2sHhxQlE68ca0Q5aKY7tanTb2ycsdzz3AB4tFGYZ2kKPBJJiYXOoDohZKXuecuV+vZhgQV3c7FsHHa7KxEipHrE23MpyDeySONlG3KrqbbUr3MYp5L97nC6cd+RtFceFIhu3OWTX24XD0V43B7jtnRpLwYhISJhRh2akOh/pgud+u+nHlTtUbrs8GRRXHlufkaikEtmK1YtgTAN+fa4Rs1EdYZMdadVUdaWcT54vxsjK16Q/JRVAeeHy/7zXkWLGWtdww+UQil9UjH9oRZx+VcwSogMYqlKy/KJWGzkn8CGHO4VorfpZgYpvqVGJG7EUOrXmHb6aaYxudJzsyjlEpPmxNbpFE9nwob+upMxk5X8puOIls2vc56ifeCuS9SrjxpjuPOIU47fm7XNr2mcNImQR377WRjdfXl5NvgdAB9f9kuy4Ug1SqjNQo/z4iAWB4ExUoxqdNpa17Tm5jil7RI2KHlY8fmRCpVy60VLoKdmE1IsbPp5aDnpUbk7MDDXLUAAZjBLs+TJljAhWix5coIbeRpiCuxXLd4f2kjdqZVQCGN6/6Kzvww8FL04jTnnmQmGHc9OBy+8YNT7tmj3r/Op7wWUNvqIjicZVUjhTBQ4lwuGqIM19aRoY8stWoM0Gw4L+8crMbGPBcoG/5cJvvaOnHkojz06qFT9x4bEAmrx6180qqz0Bwt2d4IZOkT/XQ8GUfB0onkwCT8zgfxYn9YYYa7vfDjHuUtmbiOVA6PjuNym63lY6hnaGHkU2ghbnPMW/bU96PFzlEjwfYk4xy4435N+YR0LC4RuffMiZqut3vyQE2VVmVhT7py2J3fjxv+OvH3nnZAGbU5bVCsMYvT3DrXJ4/E3YKeLlu/cygbvYpkp6ATCJcbC2cjV0hUemctGWWZy3Kr4RZ/nK4quOiSc9Je8wtirPZnnJq0wlKjetW+jpOlejjGkhj0h8sUKNN4vz8cNnlKHM/xgmXRSnXoie4F3sb2ZoFxZRQOP5tEp622gvD0/HQ70n16xUcMhT8/DUcCj439v70nHF2T6u1BjmQJ/vnp/91G5X3T8P3w77bND9zg9cb99W9K+uvzU+0ng1S3reQm66LHBuV/25T9/C/tFg8kLvcD6uG08ty+H5C0bnTb0U5gJ9+09eWtKbPutp8Nrd41w39Vad4eRwtPN/Xyajin+F6d+7FFEhVvbTlszib18Op2CgyXp8l9xPAYPQ4B4PgLdCCsj28kQ7+Buhr0fZxFDRu4w2HU0+//BauP6aGBJwAA -->
