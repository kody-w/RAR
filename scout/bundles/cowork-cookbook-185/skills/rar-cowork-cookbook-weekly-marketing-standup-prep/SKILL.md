---
name: "rar-cowork-cookbook-weekly-marketing-standup-prep"
description: "Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_marketing_standup_prep", "rar_sha256": "83556dfba32db0afcc05dc67d9668516d3890f20bcc41d6df0091e9b61811130", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "weekly_marketing_standup_prep_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/weekly-marketing-standup-prep:f24decf6440a027d77cf9850e1d13e73debf29613d3e7066ccd9622ef3c53f86", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "beginner", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/weekly_marketing_standup_prep`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `weekly_marketing_standup_prep_agent.py` is
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

Weekly marketing standup prep — Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/weekly-marketing-standup-prep
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `weekly_marketing_standup_prep_agent.py` and embedded as the fenced Python below (sha256 83556dfba32db0af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `weekly_marketing_standup_prep_agent.py` first:

```bash
python3 weekly_marketing_standup_prep_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 weekly_marketing_standup_prep_agent.py   # or on stdin
python3 weekly_marketing_standup_prep_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Weekly marketing standup prep — Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/weekly-marketing-standup-prep
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/weekly_marketing_standup_prep',
    "version": '2.0.0',
    "display_name": 'Weekly marketing standup prep',
    "description": "Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'beginner', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'weekly-marketing-standup-prep',
        "upstream_url": 'https://coworkcookbook.com/recipes/weekly-marketing-standup-prep',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2f2262191f29cb9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/weekly-marketing-standup-prep', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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


class WeeklyMarketingStandupPrep(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WeeklyMarketingStandupPrep'
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
    print(WeeklyMarketingStandupPrep().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
