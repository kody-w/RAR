---
name: "rar-cowork-cookbook-d365-design-to-retire-manage-active-products"
description: "Answers Dynamics 365 F&SCM questions scoped to the Manage active products area (8 L3 processes under Design to retire), using the D365 ERP plugin against legal entity USMF; call it for product lifecycle guidance in that"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire_manage_active_products", "rar_sha256": "02cc26363721221ec1e06c98f134efaae4178a6c587ab2c4adcd464ff94c1780", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
