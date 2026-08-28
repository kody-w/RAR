---
name: "rar-cowork-cookbook-adaptive-card-perform-preventative-maintenance"
description: "Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_perform_preventative_maintenance", "rar_sha256": "d61bebcb619f1fc6dcc8c77046ced19bbbb13883be71144ca8f0aa3196e6cfb8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_perform_preventative_maintenance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_perform_preventative_maintenance_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 d61bebcb619f1fc6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_perform_preventative_maintenance_agent.py` first:

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
    "version": '2.0.1',
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
