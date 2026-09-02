---
name: "rar-cowork-cookbook-adaptive-card-recruit-new-talent"
description: "Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recruit_new_talent", "rar_sha256": "326375bdd21fdeda89c48a7a23752ed1490a00b36bb1b07598057c4262592aa7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_recruit_new_talent_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-recruit-new-talent:5977235f8939a80935246871dfdb6aea443892ed1af3a5ae5af2349c34717580", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_recruit_new_talent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_recruit_new_talent_agent.py` is
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

Recruit new talent Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 326375bdd21fdeda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recruit_new_talent_agent.py` first:

```bash
python3 adaptive_card_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recruit_new_talent_agent.py   # or on stdin
python3 adaptive_card_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recruit_new_talent',
    "version": '2.0.0',
    "display_name": 'Recruit new talent Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bff4c1bd4aad497b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardRecruitNewTalent(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecruitNewTalent'
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
    print(AdaptiveCardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
