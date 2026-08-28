---
name: "rar-cowork-cookbook-pull-whats-relevant-for-another-team"
description: "Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_another_team", "rar_sha256": "2ceb7226baa8d49cebb536e273482599371307c9c923a269816b7094ba40be8a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "beginner", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pull_whats_relevant_for_another_team`. The original RAPP
agent is preserved byte-for-byte in `pull_whats_relevant_for_another_team_agent.py` and in the RCI capsule.

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

Pull what's relevant for another team from a campaign brief — Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-another-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pull_whats_relevant_for_another_team_agent.py` and embedded as the fenced Python below (sha256 2ceb7226baa8d49c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pull_whats_relevant_for_another_team_agent.py` first:

```bash
python3 pull_whats_relevant_for_another_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pull_whats_relevant_for_another_team_agent.py   # or on stdin
python3 pull_whats_relevant_for_another_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pull what's relevant for another team from a campaign brief — Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-another-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pull_whats_relevant_for_another_team',
    "version": '2.0.1',
    "display_name": "Pull what's relevant for another team from a campaign brief",
    "description": 'Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'work_management', 'beginner', 'read_only', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'pull-whats-relevant-for-another-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/pull-whats-relevant-for-another-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae8d2c168df658bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/tailor-content-for-an-audience'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'work-management/pull-whats-relevant-for-another-team', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PullWhatsRelevantForAnotherTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PullWhatsRelevantForAnotherTeam'
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
    print(PullWhatsRelevantForAnotherTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
