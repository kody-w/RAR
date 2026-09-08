---
name: "rar-cowork-cookbook-configure-research-new-products"
description: "Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_research_new_products", "rar_sha256": "c1a057efc7ae5d966a81eae9c0831d7891ac15e87b049d807d916f0c634756cb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_research_new_products`. The original RAPP
agent is preserved byte-for-byte in `configure_research_new_products_agent.py` and in the RCI capsule.

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

Research new products Configuration Bulk Setup — Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-research-new-products
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
    "approval": {
      "description": "Your explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per research new products target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox or production; sandbox is required first.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF; use sandbox first).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_research_new_products_agent.py` and embedded as the fenced Python below (sha256 c1a057efc7ae5d96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_research_new_products_agent.py` first:

```bash
python3 configure_research_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_research_new_products_agent.py   # or on stdin
python3 configure_research_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research new products Configuration Bulk Setup — Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-research-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_research_new_products',
    "version": '3.0.3',
    "display_name": 'Research new products Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-research-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-research-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '24f3c386f1ee95da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/research-new-products'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-research-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per research new products target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox or production; sandbox is required first.', 'legal_entity': 'D365 legal entity to run against (default USMF; use sandbox first).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for research new products, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per research new products target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes', 'example_request': 'Bulk-update our research new products in USMF sandbox from this config spreadsheet — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per research new products target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox or production; sandbox is required first.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update research new products records in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureResearchNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureResearchNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per research new products target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox or production; sandbox is required first.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureResearchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9Oi1rbuX/H0rjpJNt3NTRB61a46gIiCIHIRJJ3qcAe5ykXA7Pz3M1HfTmel115rVZ1Px1RahTnHfTzPmC/+9s7tu6Rq3n16p4duuRDcPE+TsFm4ZbDgqqFqMvBWZR74f+FXZdekXt9VTfvu/bsgbP0mrbu0KsF2LXSDFmxbuF3n+kkYzMujNO4bd16x4Ec/zBdRmoeLKlo0YRu6jZ98KMPhQ91UQe937cJP3DIO2/eLm5ungduF7SK8hc20aKph4cZuWrbdYj2VbpH67QInicXmf+ucvPgxD2M3X4Rll3bTwtTlzU/vgYqub0pg0pu02YrZodmX9w8H3agDrk5VD/ytgRVg4fwhT4HiLgnf7AG+hqNb1Dn4+OnnX96/S8Hnd59+e+fnbgsuveNenobayy0lHNSXU2BzDqSAVfUEIl2C73XYRFVTgEtBGC1e335swzx6v/jP/8wGt4nbnz59Lhev1+d3839aXz6M6iq37ebwurXrpTnw+OOCyQd3ar9xuQWJKuOPz51/SKrqxX/N9358KvkYh92Pn99VwIRHeD6/+2lRNUBf08+fP85S6h9/+phXQ9j8+NMfctreu4R+NwsDVn/88vr+EgsW/rE0jRZfdJXnXrqa0E/rEAj/xr/59TT9Je4Vki/PxT9W9fvF9yXP/vwXsPdZih6Q+32xIAZg57uPlyotf3zpAOkOS7f0wx9/+kdiQRn7WZ623b8k9+en4AQ0AojWKySgEOcU/LKAXr59lfmP1dagYP4dT8DyN3VfA/WPZD8y+3ei87QEBf+Wy++K+94G6L8WP/9D3/6nDe8X0ed36zBPQW+7Xh5+Wvz2KJGffwj+uPjDL78D0f9UjA6a139I+FK4ZRqFbffly88/tI/LP/zy8w99Dao4dIsvfZN/T+b34vrQ86cIvlb9+Oe9QL9ZZmU1lIuvPbT4rar/V/P7x8VpRp0/rrefFt924vyCFrMTb0qfIfimG1tg6zdx/Ond7wB5AAI2AFbm2wA//uM/FnLqN1VbRd1C96u+W4AEd2kRzsYbSdou0ieUNTOQtikI7GsdqP85w7PFAI9//T/+A+w/+C+wh9/QO/zyhtVfAFZ/ecPqXz8uDCC2atI4LQFsaoyqfi7dGGDwrLKeNzU3AFPe1IUfQDd/mD8s0nLx6z+R/OUh5GM9/frA6PSJehq3mxGv7fPw4+yblYTlyxMfkE44hn4P5OeV7z5Zpp0ZoK3yG0DMOQ5tlub5IkgBpgD+mh6yQaw+zcJ+/fVXz22Tz+UTovHFk9haGCz4as7iAyCqMMrTOOk+l6GfVIsffvv9h8V/L/6nXQ/hsw4VUMUrE8BCUT8oC9BZfQGWgSSBtALYeGTit99fsQViSkBPIG9p9MZIoDKzMHgLtL5lPmAEufBCEGAQ3KKumg7g/iLtPi520eKrvUDpfGtmhqQCHBqEdVgGYelPQKoL3PkaybLqFi0ovzaa3i/6Nnxo/dVrHtwbFqDF3e7XhcypgIeqHPwzm/kkS7esyhSE/2sZPK8DIc0P7YJ9E/Fxocy1uKjdxq2Txn3piNxnXgD/vG0Hwt0FKI3P5Uy44RyqR2M8wwMWgcj4r5R+eEwWflUAFAjaN92PNe7MlsaDNZvPZfsqereZU+FXj/ki7sGAAKjgb6+SapOqz4NH/ICls6RXFoJXVh41+Mb2s42Lr0MM96exh+3zbKED9KgXn3sMQZeL/48HpTkojCBovMAY/HrBK4Z2fiZrHh3npD6nzVk5qNhnY/4xx7xh1Rtkfy7zFFReM/3tufIRk9eaJwwCEAkA9GgP+cBrYOQs91H+czk3zWyh+7l844b3s5czEAIXAVaAXppL+E3hfPfN0gQAwvz9jznhUS5NMAcElPii7r0clF8UhoHn+hmwqplb+JVl0AuP/A1JCgrkW6/m6INMAfkLYEQKsgn44+NXvH7efTP9Txuf49C85TEq9qCDm4cAYEc4Gzinakg7AGSgth6TOvDz00MIcKOou9l3DyQYePq8GDbhtU/btJuL6RnXsAZQ/WF+f3o6Xw3HGrQNCBZojroH0X2004w0BRh2gA0AUUCFFGkJyB8E5RWEh0C3mLEBYO+rzp4SH5dfDj1Ld2att42zI/OeeRBYRMB0cGX6FkKM75UJkFfMKx56/77SvmqbZc8w2gIoBBrf7j4nho9P0n9OFYs3uZ/+chT68d87LT1o3PxzAXxaJF1Xt59g+Em9b8z7EYAY/LS1/YOFP3wXCP4k9unxp8W/Z9qfRLxa49MC/Yh8ROZb+1dpvV4gEtwH9vxhOd+dEfAPhAXqqwLU1py3CdD+Vzp8WwI4MW4A/oDFT3psZ1YdAJE/+AAk4XP5ba3PvfYV6NrqGwx4zAWg7p85+0pb4FbZAd3BPEPG4cf56DWb34bvPpV9nr9/BwAx/OfntZmZirme2/mQB2INJrIuDR/f3uBv/vznA/B5RkfQKEAl6Ie4+uDOJ4EXdILxKw2HuWEeZPI9nH2R+MvjBz89ITaYHemmerb8ea6bJ8E/kcaXOSx/NekbKplhYTFj0swQ9cOi75FXB2aSsHsEeDZ0vgdYD1AhMLkP239kSReO3V/VHx4f3PzjYh0CdM7bb9vwRbHziPENWjzTDtLtg6C/XzypDXQo8GHOx4w0bgtaF4Tqu7aE5S1tqnIeFf5qj/F07ps1b6pb4LBXjbOmVyjAjr99vZzOR2uAkzPbRGnTdt/V/eDWL09u/avy9czCf6Lf1+z0Rtc/BmHk9nn3oOW/PQLzpv+h86fvKv16WvirRguMarOSoPo0K3r/4gDwDk547xdfD2sgzK/j86whLPvi3aef54Pi3AqPLfMHsAe8fd309e8/Xvjul7/YBQx7C9gs6w8j/1haPQ6YswtAdPf8e8hv70DbuSDp7qvxXicUsBzg8Id2ns1gAE1AOfj+BBFw7989u7y2t4kLhmew30ddhFiFkb9yQyKgSdKl0NANaR+hcDRYUTTq+igRUisPWdIBhawCGiUjxCfx5YogfQ/IeyLRl3n+TGeTZntAJD4AMAv/uA0uBS9fnrbPgfp6VHrAS/yqXI9cgpXbZbtjni8OhlAPXq68SdxCNgJr5zNnEPzFXF0qD5fLcqCre1fwMR0TxW2TtWIsKpmOiYfREB1HDrmlzFIJSwyXuxid7MAwzNotvHbcdqK/c9nMv/Rk35BUYKke6A7lntp65eQdKzg31tkUfoCeuHzMirBxNph9duyssJOwRqP0mDvoLlph+QqS/LEU9Ep3OKm9XtbnaZNvGmjXq5l530hZkU+bMFWYTm59DrH0tZsouXutyiUvOeJ24+hclLP5pdOIzk/tXSDWaT327Y3ztF1NRbGKL682jG9GKnNls8kO5iTcpWuOLatwr0zwlp9GDbVMIU8HdNnvyD0JWaG9RBk3HLlNeNrLZt8grbbpGY6B8nVRrBM3lTt1qbItGt7uOUSFN68f3XxJRV4AmRAU8uGNIu9ckQKnEDREOqm5yQbPrlsxxTmnVo8t4hnXY27l6324VjaFdfbyVRWH01EejusdcyYTaTrgNHbv9dGx2Z0jqtKGpBqeI/bnlPI9WW4tMz8ZVrptcx25GbraXLjVVN9yUsJzfzxc1zZWln7V3rmduDNPhODIA1sm4Z6WMz5t6yVmnu0zX5q7xOnRImwDsleGoh06RNU1xGUKhGUTsZI9+ADL23gboofbSqY60kkIVz8qvFBcl0XVoqmlskirC5Ky2erBSWzZtVTL+cWuPWqJDCqEXYWLoWPxyaKPqqPn8FU7nE6Cxlo1ORUcgZtws7dIfUsVclINNTf1/fXKbc0AL6prqnkphpz5O5XmDSd5zi4P2fu4qvNzv7OF4a6jyeVUlfW1czfy5kjsSj6iEDUfuWHqhwvnryhvzCTC8TxTDK4D1+2PeCx6HYa6I18rctajYpphMgrahs04WcSO3Tho0KY2rtsVsa+XCHygU1rYjBIExQ0lau2uTBMsIdZOe1jfzQplqWWIjX2Qmqi1KVq64E1Ivq8HeGr8+91NXes4HRGUVAOyvOL+alPft4V5YUOZDSIIhQkb2irbJVIXNnQc2hKBTNjAITnfCctueWqT4ihZ98YfxNPeNtIRP2an3My1q1P5/NKuA6aQB4GFxggy7cM9XtuFovG3FaNY43Q9evvTgVgeCmx72UwNd3M10JL5ZkPkG8c98ATrHZdmeNzGR1bxtjHCUBvDX2OVXjISwDKx3TeDZhlOEQi21xqRtqoklcegDW6lqHElQnofS006cCQnDX1SuFCmS1rIDITaeOoSOZ5cL97vVVRNR17ZzPM66i2V5RIccCO3KYp7iXlOUC5PTXIq7IE09hKRnFcdQ+jFZWkzadJ27s48Vpp1lSkxDF17yowlLpHHji/J6V7J1wQEW7sTktzyK4HzteJGQuhqW0jZqWKuR2va7877AdV5KuwpXBGwcp0pyAo2d0cLrnjACCN2biXkru75tSD1yR1hiy2W4Cl1hrgqP2a8dRQvOH5L5aac0HVuGi5tDHd6D2h3l19uZXKL8+EoEixNa0uMmSxTO5b9OpXVrXoU+wnyEW3txYm3Xet+leO9PDCNIR0HpI/3tcxn6N2ygnq93dy8RD7Vp9tW1GiBGpuEPgnIgdmWDdW499K50eolngwrLipiFbFDqVrwpceRi3Tf54wXMoHai1wfHSUbtRplEnEPvzcoPB0DIclX1/XlOI77fn0Q0KN12VmEfQv5JZrlkVEzthBt+F4S6EY7Cj7BKnpIUmwjT+V5bAsxVElj4MS0XjvJ1eXpCy9nYq2jHBc0Qtj5ux3sXBWSivqogWUy07Q940z7lSmWmdPtFWdKt6Y5lRnFIG6wZtvUQ3RJX09bprqL21W632Hk8cQXdY2WFKe39/QUxmbcyUav3LPNNW18xV1dQorhpfFahX1ahRV+IierEQ6NjMZe4aR+xxNxh+ADUY1aSbeRLU5waDdDXHB5nlmHaBBVtUIq5HpjL2Vve8xQ0WKcmGsswG4qdGc6LziU3lFLdtNVoKEbXvlqtFJVcoLymwTfKnR9RoMi63xGpmDK2vMbxo9jCxaXvipPhmhmKo9a10m/mtA6hlmWMsm0bn2KsWV8Y0FGEO4PnbSsG8bmIQXUZ7kLL+JFvw5hVvvbWjpI2IVhLL6Sp2Sc+A3PIkydm5By3MTL43SRFXnlxmcM0/N8SUz3qA6ClmvEMt5526V3NxJmWpFdcLRXeSI1wnTuB+zGhX1599MxjquUyQLHyqQQz50kYfdwjk3qZrPmhJ1oQVo7XOlwunET0SXCdnuuSDMhYoYVGQLxr2vndrql3aiMR2nXSyyuaaxUg6By7a3uAJa6bN47KLD1rLYOK+otxt33KoMdr4oejWdTUqmUUUGWguXWOWI4y+s+z0Tc5ZpY6r7ml5YZrfYnH544v9ldb6TUVleNc2VAypTB1ydDV5bJ0i1trMoCVDsZJ84C/tHNTsgn0MtMzuTE/XpcwjAqXkdeSvt9GPa8zVo8urZ0eUdHuwGxG8R00bxA5EiL6XWeuoSQTTJ1u17qg38R7lBQyzavMTbJJWA4VGCbpKfTQTjpjLS5cKawtWpbudgU0jqnWkv3ad63+8JVT3K+WW5gxbPSnb3XxgK0mzcst/hkIApLnezNwcXL034jpcGlPa9Bgu+lAmaQer+ZQodvC2ySO0mVgu0duohHeUfwshEOUqdDhnuz+/NurcMS35iOSUsSxkNnhYqdiTB3TGIcrptA6K9T6Qhm2lVpS7DrC3y6kBqiUEK1TZPb0r81R0P2AXlILkIFadUVEGrIOlTzskbT6GnbQwV6ly1f4rY53ni3Mi4Mdtof/aVFqQEmEfX5cAe4bGaC3m432Lk3dIRS6dFRK8HYQ2tDNQHQoAjjygdd4M64S+z5mrAEfeIyiTvvTX/JQ9FJ07K8dNuc4Es+iC9BZSmyhTnBJYOPm/tRsy/ZhtWthkEPR+/EOsYOHNRgH5bk8AQ5G/5sbnENG06IeC2L4wlR5eue1evOL87NPcuFlDqsKUO4CENg791CduAGlW1UuceajHl3pzwYnXo8Ss7aZPZ7/ZqBkSq7KGcPW643K/t0IJueg4ToBkO0TF2bICM5Z18cct6N3BAvyWgKZL3bTkI0LOuTgB0jkdX92jb3azAD97hNLEfupG86zTxJx3Zl7fuJYTfFZWL1oxNXFKo4e56O1nJ3v0pC2pyURjVQHdtVFk/r4QnAluHzMq3muJHfxPXuCotXIVVvR3swsx1vnJHmoG5z7BJh+Fk04jvdlaODXssY22FVYZabkBJr2jseFTi+4yNzpY+oxFvZbSvvW8s59WBmi3wTFI8NGkdUVl2eClpj8EZvbo27AmYSdp9xOynkFASJhYbd9Xp8ZdrzNe02ZO/mpnQsHIfUVkVKBES1IqbcOBUsXthUdizOl/OhFikiBvElyMlgjggRI8q0kctMQDCrc0vAtLs+hUnQnsxeTszs0lvre+IF2ak4NOd6TPrSwdH7iOw8s+jA2OLpncKeFWHqOzErsGPLQ0Q5bNz+uoOl7XTRh0LeFaJn4laJu+QYZCKMuOU5rZomDa63tBqUPsfFIW0PQdWgKelcLfbq5rjinNrbyPDIjl/6NXMLXOl6PnIr04MTiLgy98PoC8HZSQOMu9ysyQq51QUZejpes3Fz3hIaStLO9X4ZG3sIAlnTl02J00nTZQmbqWRwdeqdb0Wrta2sWsjf3kaRVlP/XlNsze8S22nFLjvEGhNpFYnHZ+BqrZ3qnN9tc+/I7tnI1Hf1sq6ZzB3CoBQKaST5FcSHbOUr60QqZH51HZgWq7hOEE6ntY9ephjaYZmx2mCHkZF1TSV0l+0zaSmiqj1w91VXMDSnexIiDGMkidv+yHTLO+KbOB3rUJorJ7HH4LTT3N4usFLuiD1NBSWB0cHNJkoeM5kyi5GrVtuxKNxdNml6tmSj+IovQwLA/81ooti/+1KkmKHkN3RYE9zZDfUeP522G9OBtnbYy0jjWsaonG9KEMECTtnX6LrTuj0blFOzPRyc9ditaLI4uztPMaCLohjL9fIUt9WocNsbQm6Ly7q6+GR/IJM9JdlaohiSlkGlQBTjDtrAVweGYq1HiU1plqadpsGxcovzSXYpnecOREcbubmTwNxwTzLd29yo66ZHww5LuoyBKOrqGo3eq469zHaay1oAgCaOlZKo3W+t5BJXVd4dqKtiIxi2vWOZThfk1uhHGOrhqJe8K49NUj6MO9Ca9SkQhxE9706atItGa22vxV5piTVL5kqSx1DKh0KJZWlNDe4qgFCrj81tJAhHhHEArnI3CD4MZ8lebTQUjcQsS6Fq6pblRdx6vhTGA3WGd3Y9niwq13C8gSf+Lu/7qghxtIl63sSaveYcABFzAXOuS+yQZsGZ5pJ1pokrnD6aNd0OcuygWbzWqWCAMJR1KK29ScFKoZWAoYNYpK/L8+ZibERy/jNVxlI37JLZ5dZE23bkrvE5cEMMjHFJf1AihfYt5ZhaWwSG1H0WpSnZ2+q0JcHZeHAHQMbmIezjXUbqg9OexK25UXbBdtvpEoSyq7wjIsuTz552WxFpeAkDgoDuQsmvHbzqCTRdYyPaB/t6pbJ0Qd91oRTCIxZXDk4Zpr8VWhX3dFeDz8cbx1OuB/elYK1YCLNXTrhftXcLsk9ldTv0hyW89736XOXVNqZQMFZtj4W9Olg3s0imQ8WIbF779MZCbLpZoseuhjIBXbf3FYrCJGVWt8aRXYxlRhIKpD5OiA6jIW4/NlyIGq2SpNSpLTvLq+tz5N8gfYMeGtYofbTu2gu81FSE5k30wk07YDJupG6Bg8FWJ1fiEoOU/HR1KJpcO0cFwIBT4CGSXmV7QOi8rWpaKNen6BIbmQspXQQv9/A5VY04G8UIxmzoQMd9nPN1v4GDI9qcYhIz7ymZXTppz7uhcL5xSAjA/0JUGyhQQ8C2dh8eYxYJGAbKL4Y2billu1tnBQpzVGvC5J73LmijZbUVHdao3l4Hgw46lsCY2krEHIAAaS+DEfSIfJNdL5I5ZwkTeL7MzhFTHlP6IFnrncbSW4haNVVzR1aptceWia8O3aa3d2flOk66cppO+sWN5om/jGwZqaIbhxf7cKP5SgjXprKuyJyduhLTUXi/J5HgNoABMNtUVCw4TBpG68HCYD93kHC1TMVY4rpOI5I6MO7iphidu0sqeR1umfp0WclXWT0K99JDJtWBaO4KD/ddKESpWIKz4aYX8WW5zzlbWG89QRelfJehsXzJBrgiVVIQM41TdflsN2Kj0+CQlWEBq9DBWa+Ze0WYI+KAs4IvdExxK8/YRcSH3Dx2qaV6h6NxKGstJxxUq4p8p0boHQ5ONo7fL9BqBQ3bkzhUPL202ltYwP5mVML1SihS+yYP0XBYL/v+aqzhJlMdU9kouowvdYh2tF2YRJuTWxIZ0TetyeG8IRj59lLd6iwg0qVW5z4adTs163ZEYh8IGTlRsZVAZ9KVb1l9OYHB3O2TdXpZEwhLxOcTXiGroa+u1EGoPStKp8vNsfFVeaZGMBFsaV/Xz9S9MbTbzegFl/ORte2U2a24ITmgTVM4u/4OPwgV1VuV4d9C6u4zCXdSbR2NwlUrsA4D9xe45CLnyvHTNoZ739HWpocfzrdS2wDwSbTbmUHGVUT7Kpjgz2hDSqoFFX0UDat6LPdov7+UeEUsA6MnxlWw47tz6J0GnQohdeLDIqBCeY+DohrpRD1clY70sBWeRv1tELtoMySSjvQBz/WwvoRX7Fq3vTbd+3ymBAUj1UEa167RjXcbJ+y+IxNmLEpD6XXsiBw26B2x2DRSL4m8UrnzqjAjr0Alfxs6PYtxbC6vpHCnmHuSxnbuELFX9VgqUAUpkrokqHZ/2bHoaLPyLbUSXW11cD7c5UQY1tnuHE2aQUqX+wqpzkU7aU1zGop7LZtohrVWQhojMYrq4Gxq1NuL1KmAljoWmcVIt7Qlnt3cx8ROPmVwp4RjMLkqnayVYX1NV/ndN6m43u3ctmlZlTb0lb89DziXaUTeHBMNitTDvbgVtKv0Eui3TMc1V2m9nup3hudSPKB8K8VZWLke8nCrNljuhD5H3AD1dOeVB/BWKXJlN1kHOUwuxbRfwkqztneKU469QCfEgQ1LLL+XZcPmRCnaB1qzCFIsYHGKVtNhaFNtCrYISuU0tsxvoW7UK83a7yKUYIpEnzBFp/jBLpQGQQVwLCyIq3tSlka3dPx62oMT81SIluLhp16zjYbUSPPgmtBWRJy7KnSWRkwrlBziHQrrTuk4LaJlVp4aqUjz6zLm0Uq41+UOjrooNGA9PJa0K+76S0cyU2E3p8MpxiBCLy2V64nAC33YzM08p9T0arnECtteQCdUR4oRpMhEcSmQTG+cjqW1SUYqPoIjwr6yBfRg02OIHwGgndqoWOtNeTOprsJTbVlALCqe45txFPjJIdUG5wOyknEU01SfvMSCqrNxtmnDXcKI6KUtmJsfw9iSHaSNF4/h1tlgq0Nw2JrkgbuQt6UuNWsUT3tAxaStQ/EWaUmcddYIqS6VDUc7SwsG7QUV8EU60Hi0omu7DMnTvbwh6OqK+g51g6nSJ4p0AicTZuW00e3YhqOPbRnJddRDYwVdftLak4asjpaCl2MB7y1bbFx1GUadLQcdUaFMB86VibfKvV5xcczpfY7Sb/e9Io2KWpz11gzVdbcbfFpz6GA51lMP7NYM34YdjaVKii9K0eQZVEKpUpF5+8hr6vq0AeeBAqwjqQOX3ltrdcqbXRoelgpk3nlPD7L1tSYP6+QY5Tu+zwUCJaYRllIGb+hLkGFDj68CGNvTlp6M8KUoS6G06HFP4cmxP6s6ol1vwQSte2RfHEe29/VwU1dJrSFssI4RO8FtZYD2N3XwAfrHwWHXGB7kJnu6zrLYYk2tgXfbBCFobNtaVFLlZX61PYsKWZgxp3MPZiLtyDDv3r+bn+K+Hl//qz+gmx88/T97xvV8VPX2W5jHE8LQDT49dH36ly365f27xk+BPc+neG3ex68HYn/3DO/DP/nlw7x5ev4i7e3x8/MRf+fG86+036Vl0LddM31pq/zxOxiww+vb+Zed7WyYD96/fcD5Vd/zyWYal1+6CrjTpY9LaTn/viUMUrd7+xq/nmmC9a9fWn3BSeJL2NSzm6+fUgDv8I/IR/zd7/8X9bj0QmsvAAA= -->
