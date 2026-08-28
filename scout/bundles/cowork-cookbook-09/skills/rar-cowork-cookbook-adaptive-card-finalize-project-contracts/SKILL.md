---
name: "rar-cowork-cookbook-adaptive-card-finalize-project-contracts"
description: "Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_finalize_project_contracts", "rar_sha256": "4afdcc4469d6658fb390273f0db93bf966a55fbe37988bd2f1318c00f17b260c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_finalize_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_finalize_project_contracts_agent.py` and in the RCI capsule.

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

Finalize project contracts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 4afdcc4469d6658f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_finalize_project_contracts_agent.py` first:

```bash
python3 adaptive_card_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_finalize_project_contracts_agent.py   # or on stdin
python3 adaptive_card_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_finalize_project_contracts',
    "version": '2.0.1',
    "display_name": 'Finalize project contracts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '073edc4c07ce92a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardFinalizeProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardFinalizeProjectContracts'
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
    print(AdaptiveCardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
