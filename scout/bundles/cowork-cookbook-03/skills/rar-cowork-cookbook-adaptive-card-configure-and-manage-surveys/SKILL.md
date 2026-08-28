---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-surveys"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_surveys", "rar_sha256": "07e38d68b1f98146076b934d580255d93cb10d5f619fccf58a08e862e757096c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 07e38d68b1f98146…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_surveys_agent.py` first:

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
    "version": '2.0.0',
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
