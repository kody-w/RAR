---
name: "rar-cowork-cookbook-d365-design-to-retire-manage-active-products"
description: "A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire_manage_active_products", "rar_sha256": "5c50b707fb0a6912ce8ab64df4682077ee1af5acb996b5cf7c59f35f5affa5aa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_design_to_retire_manage_active_products`. The original RAPP
agent is preserved byte-for-byte in `d365_design_to_retire_manage_active_products_agent.py` and in the RCI capsule.

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

D365 Manage active products Expert — A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire-manage-active-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_manage_active_products_agent.py` and embedded as the fenced Python below (sha256 5c50b707fb0a6912…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_manage_active_products_agent.py` first:

```bash
python3 d365_design_to_retire_manage_active_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_design_to_retire_manage_active_products_agent.py   # or on stdin
python3 d365_design_to_retire_manage_active_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage active products Expert — A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire-manage-active-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_design_to_retire_manage_active_products',
    "version": '2.0.1',
    "display_name": 'D365 Manage active products Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-design-to-retire-manage-active-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-design-to-retire-manage-active-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b126a67b2b00efb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'design-to-retire/d365-design-to-retire-manage-active-products', 'uses_skills': {'custom': ['d365-design-to-retire-manage-active-products'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365DesignToRetireManageActiveProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365DesignToRetireManageActiveProducts'
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
    print(D365DesignToRetireManageActiveProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
