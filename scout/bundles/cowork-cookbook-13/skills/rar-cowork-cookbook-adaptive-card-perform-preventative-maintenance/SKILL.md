---
name: "rar-cowork-cookbook-adaptive-card-perform-preventative-maintenance"
description: "Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_perform_preventative_maintenance", "rar_sha256": "49a0f3619d6c6be1d3d0f22716f95fbf5535dd047bc0677e4cac1a461b359e8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_perform_preventative_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-perform-preventative-maintenance:75d3cc0417202d9954cd2f28aad8895028402b6d3dd9d65f297bbe34aa592caf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_perform_preventative_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_perform_preventative_maintenance_agent.py` is
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

Perform preventative maintenance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 49a0f3619d6c6be1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_perform_preventative_maintenance_agent.py` first:

```bash
python3 adaptive_card_perform_preventative_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_perform_preventative_maintenance_agent.py   # or on stdin
python3 adaptive_card_perform_preventative_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform preventative maintenance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_perform_preventative_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform preventative maintenance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-perform-preventative-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'baeddee26c9306ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-preventative-maintenance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-perform-preventative-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardPerformPreventativeMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPerformPreventativeMaintenance'
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
    print(AdaptiveCardPerformPreventativeMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
