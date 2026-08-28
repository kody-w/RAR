---
name: "rar-cowork-cookbook-adaptive-card-provide-ongoing-support"
description: "Produces a reusable Adaptive Card JSON snapshot of provide ongoing support status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_provide_ongoing_support", "rar_sha256": "1260ca1b808cdb91fe0f6acf901715ebb3b62176b24e210e24260b2dc01df066", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 1260ca1b808cdb91…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_provide_ongoing_support_agent.py` first:

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
    "version": '2.0.0',
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
