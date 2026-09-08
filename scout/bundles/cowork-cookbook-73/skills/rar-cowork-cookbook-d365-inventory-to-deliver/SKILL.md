---
name: "rar-cowork-cookbook-d365-inventory-to-deliver"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Inventory to deliver process (7 L2 areas, 41 L3 processes), using USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver", "rar_sha256": "166e95af6588b92a03d7a449c7fbce7bbf2ecba2390c4a858698ec5b99863150", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_inventory_to_deliver`. The original RAPP
agent is preserved byte-for-byte in `d365_inventory_to_deliver_agent.py` and in the RCI capsule.

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

D365 Inventory to deliver Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Inventory to deliver process (7 L2 areas, 41 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_agent.py` and embedded as the fenced Python below (sha256 166e95af6588b92a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_agent.py` first:

```bash
python3 d365_inventory_to_deliver_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_inventory_to_deliver_agent.py   # or on stdin
python3 d365_inventory_to_deliver_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Inventory to deliver Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Inventory to deliver process (7 L2 areas, 41 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_inventory_to_deliver',
    "version": '3.0.3',
    "display_name": 'D365 Inventory to deliver Expert',
    "description": 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Inventory to deliver process (7 L2 areas, 41 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.',
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
        "upstream_slug": 'd365-inventory-to-deliver',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-inventory-to-deliver',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53ed7d0d752cf065',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'inventory-to-deliver/d365-inventory-to-deliver', 'uses_skills': {'custom': ['d365-inventory-to-deliver'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Inventory to deliver Expert** skill for this conversation. From now on, scope your help to the inventory to deliver domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Inventory to deliver process (7 L2 areas, 41 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.', 'example_request': 'Act as the D365 Inventory to deliver expert and walk me through the warehouse receiving process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM guidance limited to inventory to deliver processes, entities, or USMF-based ERP plugin work.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365InventoryToDeliver(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365InventoryToDeliver'
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
    print(D365InventoryToDeliver().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
