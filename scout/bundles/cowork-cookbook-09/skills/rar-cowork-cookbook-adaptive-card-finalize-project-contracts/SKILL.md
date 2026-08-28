---
name: "rar-cowork-cookbook-adaptive-card-finalize-project-contracts"
description: "Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_finalize_project_contracts", "rar_sha256": "dfff56e9f2c4fb3b67ccb70f52321fe9ef033fc41708180e5c91e1737fe093c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 dfff56e9f2c4fb3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_finalize_project_contracts_agent.py` first:

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
    "version": '2.0.0',
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
