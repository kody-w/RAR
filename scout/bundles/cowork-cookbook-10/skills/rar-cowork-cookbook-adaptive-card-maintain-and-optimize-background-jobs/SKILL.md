---
name: "rar-cowork-cookbook-adaptive-card-maintain-and-optimize-background-jobs"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain and optimize background jobs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs", "rar_sha256": "bbdab2c31899d5d0e3a2bbc5db0441ba4ecac4dcc595146643ec34ab1ffcd642", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
