---
name: "rar-cowork-cookbook-d365-design-to-retire-manage-active-products"
description: "A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire_manage_active_products", "rar_sha256": "611f75399b0b976ef887b57fffe80c9303a2daa1224d0b100fa12ed181374033", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_manage_active_products_agent.py` and embedded as the fenced Python below (sha256 611f75399b0b976e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_manage_active_products_agent.py` first:

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
    "version": '2.0.0',
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
