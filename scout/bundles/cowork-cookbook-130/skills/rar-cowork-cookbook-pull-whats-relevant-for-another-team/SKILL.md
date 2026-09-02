---
name: "rar-cowork-cookbook-pull-whats-relevant-for-another-team"
description: "Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_another_team", "rar_sha256": "afb7697ac50f79d1fbf2651299100ca62f4271f8acd335abdd79fab418fa4995", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pull_whats_relevant_for_another_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/pull-whats-relevant-for-another-team:f56a91b081bdd3feeefa23898db7f597b1f76cd3c1ce8fdca2e56364c50aea6e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "beginner", "read_only", "automation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/pull_whats_relevant_for_another_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pull_whats_relevant_for_another_team_agent.py` is
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
