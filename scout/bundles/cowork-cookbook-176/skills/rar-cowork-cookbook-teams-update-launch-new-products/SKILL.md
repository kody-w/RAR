---
name: "rar-cowork-cookbook-teams-update-launch-new-products"
description: "Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_launch_new_products", "rar_sha256": "00a662a87878a9e6ea88b46e71533dd6dd8095ddc9acd9aa81992ee994e4ff70", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_launch_new_products`. The original RAPP
agent is preserved byte-for-byte in `teams_update_launch_new_products_agent.py` and in the RCI capsule.

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

Launch new products Teams Channel Update — Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-launch-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 00a662a87878a9e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_launch_new_products_agent.py` first:

```bash
python3 teams_update_launch_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_launch_new_products_agent.py   # or on stdin
python3 teams_update_launch_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch new products Teams Channel Update — Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-launch-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_launch_new_products',
    "version": '2.0.1',
    "display_name": 'Launch new products Teams Channel Update',
    "description": 'Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-launch-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-launch-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5cc7e6499c0200ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/launch-new-products'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-launch-new-products', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateLaunchNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateLaunchNewProducts'
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
    print(TeamsUpdateLaunchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
