---
name: "rar-cowork-cookbook-adaptive-card-manage-lead-identification-process"
description: "Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_lead_identification_process", "rar_sha256": "220ce750fe28fe689919c7ce9d09bea3cbc52a7088bec1ebd5de12f59a139bc1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 220ce750fe28fe68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_lead_identification_process_agent.py` first:

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
    "version": '2.0.0',
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
