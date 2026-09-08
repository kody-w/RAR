---
name: "rar-cowork-cookbook-d365-inventory-to-deliver"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Inventory to deliver process (7 L2 areas, 41 L3 processes), using USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver", "rar_sha256": "166e95af6588b92a03d7a449c7fbce7bbf2ecba2390c4a858698ec5b99863150", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
