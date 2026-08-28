---
name: "rar-cowork-cookbook-weekly-marketing-standup-prep"
description: "Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_marketing_standup_prep", "rar_sha256": "2bfe126cb549e78b1643e46620e9532cd910a6ff0ff50aaea0a36eeb32a315aa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "beginner", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `weekly_marketing_standup_prep_agent.py` and embedded as the fenced Python below (sha256 2bfe126cb549e78b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `weekly_marketing_standup_prep_agent.py` first:

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
    "version": '2.0.1',
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
