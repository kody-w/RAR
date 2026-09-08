---
name: "rar-cowork-cookbook-d365-inventory-to-deliver-manage-inventory-quality"
description: "Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality", "rar_sha256": "671cc6d2800942d3a62771d65e42687cbf82814b6159bdfed3b318c5270ca4c1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and in the RCI capsule.

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

D365 Manage inventory quality Expert — Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 671cc6d2800942d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_manage_inventory_quality_agent.py` first:

```bash
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py   # or on stdin
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage inventory quality Expert — Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality',
    "version": '3.0.3',
    "display_name": 'D365 Manage inventory quality Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-inventory-to-deliver-manage-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '437bcb2dce05c37f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'inventory-to-deliver/d365-inventory-to-deliver-manage-inventory-quality', 'uses_skills': {'custom': ['d365-inventory-to-deliver-manage-inventory-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage inventory quality Expert** skill for this conversation. From now on, scope your help to the inventory to deliver domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q', 'example_request': 'Act as the D365 inventory quality expert and help me work through a quality order in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when working on Dynamics 365 F&SCM inventory quality processes in the inventory to deliver domain, with the Cowork D365 ERP plugin and USMF conventions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365InventoryToDeliverManageInventoryQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365InventoryToDeliverManageInventoryQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(D365InventoryToDeliverManageInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
