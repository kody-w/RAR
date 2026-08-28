---
name: "rar-cowork-cookbook-adaptive-card-maintain-and-optimize-background-jobs"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain and optimize background jobs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs", "rar_sha256": "69521522535c700c3a41d42c2e0c02ba0179c2fec4bc4b1636626c08fd3562d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_and_optimize_background_jobs_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 69521522535c700c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_and_optimize_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
