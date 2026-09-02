---
name: "rar-cowork-cookbook-adaptive-card-manage-deferrals"
description: "Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_deferrals", "rar_sha256": "77975301bdd769241dd01cdfa8801e9c7e84a100ad62ca110d80dfeeeb61e642", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_deferrals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-deferrals:500c5d062bc159f29b5f79f16d22e973f48d446bc46cd802f20ada8028a3c8b2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_deferrals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_deferrals_agent.py` is
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

Manage deferrals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 77975301bdd76924…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_deferrals_agent.py` first:

```bash
python3 adaptive_card_manage_deferrals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_deferrals_agent.py   # or on stdin
python3 adaptive_card_manage_deferrals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage deferrals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_deferrals',
    "version": '2.0.0',
    "display_name": 'Manage deferrals Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-deferrals',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ab23900cc6b5fd4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-deferrals'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-manage-deferrals', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageDeferrals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageDeferrals'
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
    print(AdaptiveCardManageDeferrals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
