---
name: "rar-cowork-cookbook-teams-update-launch-new-products"
description: "Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_launch_new_products", "rar_sha256": "69078bf55554f7f89365fafccdd25f8dc354eef93d51453d980b60d07fe8ddfa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 69078bf55554f7f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_launch_new_products_agent.py` first:

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
    "version": '2.0.0',
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
