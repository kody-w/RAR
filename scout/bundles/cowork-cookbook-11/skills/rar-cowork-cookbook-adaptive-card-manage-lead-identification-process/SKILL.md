---
name: "rar-cowork-cookbook-adaptive-card-manage-lead-identification-process"
description: "Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_lead_identification_process", "rar_sha256": "ebe1bd132ef9fc2b489b9543f58e282fbd674da580a2ff522c7f39d6e4e763bf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_lead_identification_process`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_lead_identification_process_agent.py` and in the RCI capsule.

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

Manage lead identification process Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 ebe1bd132ef9fc2b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_lead_identification_process_agent.py` first:

```bash
python3 adaptive_card_manage_lead_identification_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_lead_identification_process_agent.py   # or on stdin
python3 adaptive_card_manage_lead_identification_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage lead identification process Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_lead_identification_process',
    "version": '2.0.1',
    "display_name": 'Manage lead identification process Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-lead-identification-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7e721ba734d6b92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-manage-lead-identification-process', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageLeadIdentificationProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageLeadIdentificationProcess'
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
    print(AdaptiveCardManageLeadIdentificationProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
