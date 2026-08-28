---
name: "rar-cowork-cookbook-adaptive-card-provide-ongoing-support"
description: "Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_provide_ongoing_support", "rar_sha256": "a006c9aec694bc3e58c6c574855838169750cf5352b0747e8af529031c73e45b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_provide_ongoing_support`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_provide_ongoing_support_agent.py` and in the RCI capsule.

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

Provide ongoing support Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 a006c9aec694bc3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_provide_ongoing_support_agent.py` first:

```bash
python3 adaptive_card_provide_ongoing_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_provide_ongoing_support_agent.py   # or on stdin
python3 adaptive_card_provide_ongoing_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide ongoing support Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_provide_ongoing_support',
    "version": '2.0.1',
    "display_name": 'Provide ongoing support Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-provide-ongoing-support',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9151188b581d751',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/provide-ongoing-support'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-provide-ongoing-support', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardProvideOngoingSupport(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProvideOngoingSupport'
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
    print(AdaptiveCardProvideOngoingSupport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
