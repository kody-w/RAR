---
name: "rar-cowork-cookbook-adaptive-card-configure-and-maintain-cloud-based-printing"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing", "rar_sha256": "3cca559b7a5b907c38753ebb8f6dbfbbd09421d79f742e8c35d874e9f1a7bb54", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` and in the RCI capsule.

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

Configure and maintain cloud-based printing Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 3cca559b7a5b907c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` first:

```bash
python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py   # or on stdin
python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain cloud-based printing Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing',
    "version": '2.0.1',
    "display_name": 'Configure and maintain cloud-based printing Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-configure-and-maintain-cloud-based-printing',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ea19abd1c8ac20b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-cloud-based-printing'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-maintain-cloud-based-printing', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardConfigureAndMaintainCloudBasedPrinting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndMaintainCloudBasedPrinting'
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
    print(AdaptiveCardConfigureAndMaintainCloudBasedPrinting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
