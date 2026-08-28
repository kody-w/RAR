---
name: "rar-cowork-cookbook-dashboard-create-marketing-material"
description: "Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_marketing_material", "rar_sha256": "71ceb2ad7f6b9b765c6854769f8b6ed188877a021f6a5433d0c762d51d26eda9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_marketing_material`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_marketing_material_agent.py` and in the RCI capsule.

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

Create marketing material Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 71ceb2ad7f6b9b76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_marketing_material_agent.py` first:

```bash
python3 dashboard_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_marketing_material_agent.py   # or on stdin
python3 dashboard_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_marketing_material',
    "version": '2.0.1',
    "display_name": 'Create marketing material Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c4ddf7ad9d21a31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCreateMarketingMaterial(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateMarketingMaterial'
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
    print(DashboardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
