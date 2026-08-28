---
name: "rar-cowork-cookbook-adaptive-card-configure-and-maintain-cloud-based-printing"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing", "rar_sha256": "f9b2cbb310a77a5856940feac81977ac9c1b04a93e6a900008fbbcc51d90e312", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 f9b2cbb310a77a58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` first:

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
    "version": '2.0.0',
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
