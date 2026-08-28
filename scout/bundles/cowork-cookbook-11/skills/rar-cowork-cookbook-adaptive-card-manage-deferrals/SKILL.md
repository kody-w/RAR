---
name: "rar-cowork-cookbook-adaptive-card-manage-deferrals"
description: "Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_deferrals", "rar_sha256": "d26b7b824db2607e00fb0562ed602ef45be2375ba39432b0f16072a39c51e4b7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_deferrals`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_deferrals_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 d26b7b824db2607e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_deferrals_agent.py` first:

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
    "version": '2.0.1',
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
