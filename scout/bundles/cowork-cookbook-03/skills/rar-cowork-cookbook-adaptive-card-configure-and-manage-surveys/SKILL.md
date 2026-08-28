---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-surveys"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_surveys", "rar_sha256": "259393295088f9063952f4ffe07c9ad0a8cfec13ccff34081c3f3fea767b0f3f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 259393295088f906…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_surveys_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_surveys_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_surveys',
    "version": '2.0.1',
    "display_name": 'Configure and manage surveys Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd608cd72fc7da7d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardConfigureAndManageSurveys(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageSurveys'
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
    print(AdaptiveCardConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
