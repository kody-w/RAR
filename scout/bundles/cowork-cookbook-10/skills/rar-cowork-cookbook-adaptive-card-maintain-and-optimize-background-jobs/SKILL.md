---
name: "rar-cowork-cookbook-adaptive-card-maintain-and-optimize-background-jobs"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain and optimize background jobs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs", "rar_sha256": "bbdab2c31899d5d0e3a2bbc5db0441ba4ecac4dcc595146643ec34ab1ffcd642", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_maintain_and_optimize_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-maintain-and-optimize-background-jobs:749cdac0c4aa2b0651f41e8776e7833dc3a600b5add8330381d4d7d6fd7ad8fe", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_maintain_and_optimize_background_jobs_agent.py` is
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

Maintain and optimize background jobs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain and optimize background jobs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-and-optimize-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 bbdab2c31899d5d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_and_optimize_background_jobs_agent.py` first:

```bash
python3 adaptive_card_maintain_and_optimize_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_and_optimize_background_jobs_agent.py   # or on stdin
python3 adaptive_card_maintain_and_optimize_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and optimize background jobs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain and optimize background jobs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-and-optimize-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs',
    "version": '2.0.0',
    "display_name": 'Maintain and optimize background jobs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of maintain and optimize background jobs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-maintain-and-optimize-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-and-optimize-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29e873a2f10489b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/maintain-and-optimize-background-jobs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-maintain-and-optimize-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardMaintainAndOptimizeBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainAndOptimizeBackgroundJobs'
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
    print(AdaptiveCardMaintainAndOptimizeBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
