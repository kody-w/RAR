---
name: "rar-cowork-cookbook-pull-whats-relevant-for-another-team"
description: "Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_another_team", "rar_sha256": "afb7697ac50f79d1fbf2651299100ca62f4271f8acd335abdd79fab418fa4995", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "beginner", "read_only", "automation"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pull_whats_relevant_for_another_team_agent.py` and embedded as the fenced Python below (sha256 afb7697ac50f79d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pull_whats_relevant_for_another_team_agent.py` first:

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
    "version": '2.0.0',
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
