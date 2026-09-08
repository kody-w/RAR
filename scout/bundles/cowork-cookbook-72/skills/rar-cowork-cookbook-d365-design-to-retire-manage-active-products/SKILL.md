---
name: "rar-cowork-cookbook-d365-design-to-retire-manage-active-products"
description: "Answers Dynamics 365 F&SCM questions scoped to the Manage active products area (8 L3 processes under Design to retire), using the D365 ERP plugin against legal entity USMF; call it for product lifecycle guidance in that"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire_manage_active_products", "rar_sha256": "02cc26363721221ec1e06c98f134efaae4178a6c587ab2c4adcd464ff94c1780", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

D365 Manage active products Expert — Answers Dynamics 365 F&SCM questions scoped to the Manage active products area (8 L3 processes under Design to retire), using the D365 ERP plugin against legal entity USMF; call it for product lifecycle guidance in that

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_manage_active_products_agent.py` and embedded as the fenced Python below (sha256 02cc26363721221e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_manage_active_products_agent.py` first:

```bash
python3 d365_design_to_retire_manage_active_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_design_to_retire_manage_active_products_agent.py   # or on stdin
python3 d365_design_to_retire_manage_active_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage active products Expert — Answers Dynamics 365 F&SCM questions scoped to the Manage active products area (8 L3 processes under Design to retire), using the D365 ERP plugin against legal entity USMF; call it for product lifecycle guidance in that

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
    "version": '3.0.3',
    "display_name": 'D365 Manage active products Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Manage active products area (8 L3 processes under Design to retire), using the D365 ERP plugin against legal entity USMF; call it for product lifecycle guidance in that',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a12da546092eda5f',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage active products Expert** skill for this conversation. From now on, scope your help to the design to retire domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Manage active products area (8 L3 processes under Design to retire), using the D365 ERP plugin against legal entity USMF; call it for product lifecycle guidance in that', 'example_request': 'Acting as the D365 Manage active products expert, how do I handle active product changes in USMF?', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user needs D365 F&SCM help limited to Manage active products under the Design to retire domain, with USMF tenant conventions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365DesignToRetireManageActiveProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365DesignToRetireManageActiveProducts'
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
    print(D365DesignToRetireManageActiveProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
