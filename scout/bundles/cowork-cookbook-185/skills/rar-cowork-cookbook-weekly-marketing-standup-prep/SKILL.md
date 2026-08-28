---
name: "rar-cowork-cookbook-weekly-marketing-standup-prep"
description: "Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_marketing_standup_prep", "rar_sha256": "83556dfba32db0afcc05dc67d9668516d3890f20bcc41d6df0091e9b61811130", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "beginner", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/weekly_marketing_standup_prep`. The original RAPP
agent is preserved byte-for-byte in `weekly_marketing_standup_prep_agent.py` and in the RCI capsule.

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
