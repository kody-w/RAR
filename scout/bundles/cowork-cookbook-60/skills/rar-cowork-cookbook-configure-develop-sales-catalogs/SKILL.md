---
name: "rar-cowork-cookbook-configure-develop-sales-catalogs"
description: "Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_sales_catalogs", "rar_sha256": "d18c637372b8ef560f24d8d2e9c64af5b8c6d03a9cc66807e0200ca398c91136", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_sales_catalogs`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_sales_catalogs_agent.py` and in the RCI capsule.

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

Develop sales catalogs Configuration Bulk Setup — Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
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
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per sales catalog target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 d18c637372b8ef56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_sales_catalogs_agent.py` first:

```bash
python3 configure_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_sales_catalogs_agent.py   # or on stdin
python3 configure_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Configuration Bulk Setup — Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_sales_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop sales catalogs Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d04d691948bdb0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per sales catalog target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop sales catalogs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop sales catalogs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.', 'example_request': 'Bulk-update our sales catalog config in USMF sandbox from this Excel file — validate first and show me the results.', 'inputs': [{'description': 'Attached Excel file with one row per sales catalog target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update sales catalog configuration in Dynamics 365 F&SCM from a spreadsheet, with pre-apply validation and an approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopSalesCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSalesCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per sales catalog target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916afObVtbnV9H8nxdJHmyDAIFwV1cNiE0gCRCghTjlsO+L2ARk8t3nIsl23Ek/3V01r0ZexHLv2c/vnCP47c3u2qis3z6+6b5dLAQ7y+LIrxd24S025b2sU/BVpg74t3DLoq1jp2vLunl79+b5jVvHVRuXBdh+9G2vAdsWdtvabuR7C25w/WwRxJm/KINFY2d+s3Dt1s7KcCYVxGFX2/PuhRvZReg37xa9ncWe3YKFfu/X46Iu7+8Wtd92dQFof7k9b5klm4V6t7jbcdssgrJejGUHBK+qugQL3y3ayC/m0yyeGT9ZPPT6RtDxwT4ftoMWqPyQqc6/p/8BKOoPdl4B6d8+/vzLu7cYHL99/O3NzewGXHrbvFTxWSBzVlb6rOjmqedspgwwBsuqEdi5AOeVXwOmObjk+cHidfZj42fBu8V//3d6t+uw+enjp2Lx+nx6m/8cu2JWaNGWdtMC47p2ZTtxFrfjhwWd3e2x+YNaDXBTEX547vxGqawWf5/v/fhk8iH02x8/vZVAhIfOn95+WgArfnqru/n4w0yl+vGnD1l59+sff/pGp+mcxHfbmRiQ+sPn1/mLLFj4bWkcLD7rKrd58ap9N658QPwP+s2fp+gvci+TfH4u/rGs3i3+mvKsz9+BvM9AdADdvyYLbAB2vn1Iyrj48cUDxIhf2IXr//jTPyMLgthNs7hp/y26Pz8JRyANgLVeJvnp3cN9vyygl25faf5zthUImP9EE7D8C7uvhvpntB+e/QfSWVyAvPjiy78k91cboL8vfv6nuv1PG94tgk9vrJ/FIMNtJ/M/Ln57hMjPP3jfLv7wy++A9L8ko4OMdx8UPud2EQd+037+/PMPzePyD7/8/ENXgSj27fxzV2d/RfOv7Prg850FX6t+/H4v4G8WaVHei8XXHFr8Vlb/q/79w+I0Q9W3683HxR8zcf5Ai1mJL0yfJvhDNjZA1j/Y8ae33wH0FECbzn3cBvjxX/+12MduXTZl0C50t+zaBXBwG+f+LLwRxc0C/J1Ro57htImBYV/rQPzPHp4lBtj86/92H1D/3n1BPfwFn/3P3hPVPj/w+/MLv5tfPywMQLes4zAu7GxxpFX1U2GHftHOPKvab/y6BzjljK3/HqTz+/lgEReLX/8V6c8PKh+q8dcHWMdP3DtutjPmNV3mf5i1O8/g/tTFBUXHH3y3Awyy0rWfNaeZC0dTZj3AzNkSTRpn2cKLAaqA+jU+C0FXfJyJ/frrr47dRJ+KJ0hji2dha2Cw4Ks4i/fvgVpBFodR+6nw3ahc/PDb7z8s/s/if9r1ID7zUEG1ePkCSCjpymEBcqvLwTLgJuBYABwPX/z2+8u4gEwByhLwXBzMJWzeDGIz9b0vltZF+j26Il5lbAEqU1m3APkXcfthsQ0WX+UFTOdbc22IyqZdeH7lF55fuCOgagN1vlqyKFtQqtu4CcZ3i67xH1x/dWr7IWIOktxuf13sNyqoRGUG/pvFfCwCm8siBub/GgfP64BI/UOzYL6Q+LA4zNG4qOzarqLafvEI7KdfQAX6sh0QtxeFf/9UzDXXn031SI2necAiYBn35dL3jz7DLXOAA17zhfdjjT3XS+NRN+tPRfMKe7ueXeGWjz4j7EBfAYrB314h1URll3kP+wFJZ0ovL3gvrzxi8FXwv29tmsXmu96G6bJ0oQMAqRafOhRZ4ov/Xzul2SS0IBw5gTY4dsEdjOP16aq5cZxd+uw1Qc/yEOKRlt/6mC9Y9QWyPxVZDOKuHv/2XPkwz2vNEwYBhngAeY4P+iC6gGQz3Ufwz8Fc17M+9qfiS214N1tmBkIgNkAKkElzAH9hON/9ImkE4GA+/9YnPIKl9mazgABfVJ2TgeALfN9zbDcFUtVzAr9cDDLh4cp7FLvRd1otAHXgLkB/AYSY/QHqx4eveP28+0X07zY+26F5y6NV7ED+1g8CQA5/FnB22D1uAYyBwHr06UDPjw8iQI28amfdHeC0/N3rol/7ty5u4naOqKdd/Qog9fv5+6npfNUfKpA0wFggNaoOWPeRTDPO5KDZATIAPAFhkccFKP7AKC8jPAja+YwMAHlfofSk+Lj8UugZv3PV+rJxVmTeMzcCiwCIDq6MfwQQ46/CBNDL5xUPvv8YaV+5zbRnEG0AEAKOX+4+O4YPz6L/7CoWX+h+/NMg9ON/Nis9yrj5fQB8XERtWzUfYfhZer9U3g8AwuCnrM23Kvz+VSrfP7Dh/Reo+Y7uU+WPi/9Mtu9IvHLj42L5AfmAzLd2r9h6fYApNu+Z63t8vvupOPrfABawL2dEmB03grL/tRp+WQJKYlj74bz4WR2buajeAfQ8ygHwwqfij8E+J9tXuGvKP4DAoy0Agf902teqBW4VLeDtzU1k6M+T2yM1Gv/tY9Fl2bu3AoTdvzGxzZUpnyO6mec8kDugJ2tj/3H2BTTn4+8HYG4A+OmCZPgOHZ+ACfqv2L/PGfOoJX8Fzq8a/hV9wfETkb1ZkXasZsmfg93cCn5XFj77cwH5PBvnz3LRf1FlZphYzBgFysY8gv5DzWlBZ+K3DzvP8oISDLb5oCACyTu/+WcCtf7Q/pm/8jiwsw8L1gconTV/TMdXoZ0bjT+gxtP7wOsuMP27xbPOgUwFss9emRHHbtJHKftLWfyij+uymBuGP8tjPJX7w5q/PXqYBqjrlANgUoMO6eUO4Gzv2XD/JaMMxHP2GZAASPNnTixGrBaPJYvnki/tkh0+oOzdwv8QfliY+p7/S+pfZ4E/kz6DNmym5pUfZ4rvXggPvsH89m7xdRQDxnsNx48fMoouf/v48zwGzmH+2DIfgD3g6+umr7/tOP7bL3+SCwj2KBug+M60vgn5bWn5GB9nFQDp9vlrx29vIKVs4Er7lVSv+QMsByj7vpn7LhjgDmAOzp8IAe79x5PJa38T2aAznn9kWa5dAiMxEnXWfrAikADFvbWH+pRL4HawcsBtD8FsynUJYo2QPoIiiGtj1NqllkuMAPSeOPN5bi7jWaZZIGCK9wCq/G+3wSXvpcxT+NlSXwehB3aEr4B0CBysFPFmSz8/GxhaOuSVdIb2AtVEd21SOuuOu+wgFMPxRuxQpVtebQZNeLTQHPpkb0tXdwdd2u+j/ng9b2At9sszlfbuykLtcmte2rpCCNikD/TYHfdooBRbuAj203ZNTswezvyqSKOTFMmSLd837WFdu0epuKG6d0KFkyUVeJ57l7Kazt6Zh/ZBAMekYjFhzZ2vcS2Xd7SJroVIbK1Nddb1iu/z2uAyYXfaaVJDnkwO5iBD2uM1S2uipJGmb124JR8nxpZ1gs6usilb+eY4jesCj6u9HJ/Ovp6h/gmVm00ii/Qe4Hq9TXZEvtHRJrtv2MY83GWDV6dGOklmfzDJrEVgVwxHt79Uo9cXyUj1uqWIGEV1d/FCTp7OVN5o3/XradmuE7nymmHTmlmZImfc4CUiyqlQo3T+lpaWE3pVE0+s23tbFjWsfMNdTS4IN/iW9LGdsNrvU3rZcodbtl472w3uyOl01VnHCjOZyG8bM+NBTF6NXi25Wql7PlewrIQOhGgjoq8nzbTZSbKmrfTL/pqloRIs9ykSN9Z2vJTOUbqEm8iKTjlkWjeYuaWI7iwLnJO5w6HcYDStpFG/BmFe+4gCY8q6He2oOhtau+VyG8/LZhWfAwlpNhvpcNoZp5PUMvUm32fFuZL2K+TOwighx4YORTcf41RJz2A5U068fBTO2WrMZQLjsGqHQkexKdXoer9tNnl/I2TBPMB5ad90Z4OiV3Nax3yy4XeWlHXMMOza4tpxZyGEjeWhVkoxu7W3Xctrg1SkxhqBo/tGQ/s7K/vk3jC4uOS1ZdtqGVrTMtKyPoh3zDnVnJ4io06eBNm4Thfy1Ij49l5YG0xURPycKWWQpEmRGGsc3ZlOwZUkQff3TLjHvizaYnrI77h60BNTnDrSEVaoZJyuZ3tCr0cDn/YqC8vtpB5uUmVJq8A406qccXxohyIv2R2mDG4wrLLd3UmYizhFKqwFeIMGiY5awcCyY2BULKX0a1G6S62rT9FZ353ZqtiNPrUzjXG11EwrNTOrtramgF9A6BlXdeA0SQtqgT1ANMiAS8Uup51UUTeOw7Lk1htek8itvQq3fH4+IbvodLIiwgiZzjghBC2wDMKHhXHfDsJhUG3m4NO11oUo1QWMrB06E7WyaKBWXL+mwhQLSZhzautcnpqlJ1wl7diw280NH6PtmeV0Fjh/s4HbPZwcmVPV0X1DR2trO5SjmfaXnSoGQnJpvPpkIQgOTzXbwpvKldcjJGws67JXOa8UZRNxWNzU9hl52sQ8faPV/RFut1NyhZGbx+HBlT+OiVy6XeQ4fsSkkaiNRszgyoS11rUJrkvMFDX95rM7Fb5DqWAOFyZWSrpbTU3jkW5uIRi7NoelvqK721GVIVpLHKXZGwq+YbrSyEb/Tjln7HjmrhGn+eNmKxcrCscsRZgsO9b1XedZuAOd66EKq7DHqnTLrzXpxJ+pEFrSFno6hnXPNvR+pQq7S6Tv7WvWa/iNjY4KEP9OXa/GjbdN+7JlkPxm26ta2iPVjb5k6/y2LpdTk0Gs76MNGm5tcs9OLWq2EtxifjFqA19pu6vriSUx1a07FBJx9KxCv/PNHa2W6eqolC2/qk85LpItKXkEtcLIRNMpkpE0C/cGpmDNejfk0nrCuji1R11NkZCUDjf9cmKVob7uti6NJnvPQ5GY8RtcOfJqMDDX43Yypfi+bLbeEO9GLo2cSNosk0Kr073Vn24rrw8sDExNw5buj/srs76lVLvvunRfGbQdTvVKX+15UR9quqS4QxlyEb51FYsu7dXB02S9Ogfu0WHznYkfRk3wJexMjZvscOqEzh1gn95kVwRRLxoSmPaN8nbLmttMMnIYm6VyTq73M+Gs3PRqTd2k7hBKuayggGs3ZtPEgzGycrUEFSW7AK7wSGoCL0Ytt6WjwqsnuLzvbMyIUGR/1fe3uMdxLxguMA6VXd/DN9hyhnXHSqilWytWJ6eJXp/OwyZkd9usuLvYtD6Yurkzrd1JLpOS5xpcxQ2fz6OaZPfs6bIbBLREMJS8xShz1VbIIem2zKoTqk053NIilKsKN0wljDSVBvVKLF2zH0JYos6QZQwBJOzLIzMpgnH2GiSOoCpqdvtErNvQsLYrxrBoVvE9TjD8E9ltsH0pnbaoyqPCsjx5rdERwmbFaKm0IYyDbFLFlkrkjRmwfbqmJcJ3LunuIo3lxetXF29QtXuSFGUKkmXPsVTMyL5cDuHgkx3ujE4cckfPZIk4NpmbiLjM6JroyHD7kMD2REhfGxXh6LQ6O9IhK0Jr6yiViqcyT6InuoAIu1uzTWk4QawqDK0wx+W1ErN1bNZSQOVxE1jS9pSeTtTyrJ22YSYkMepLxPlWRbyroaphTOdRIW6lFEeSExz9Zcjo1cG0StsHrQwmrgOAh8trnFkm34unTRBWGyIspXzv9+lV2GXj9kCMky2I1X1ixqg1I71SnOJ0RIrOSqyLgORTfKB3BKMt13Lu1bC92mSJ3NHcZohkdpeZsj/UkG3u5TUeyuf43lklZY5bO7xQeB5xh/TaoFLNl6v9eYXLHRd1dq2nLMTakH10a8MJbZa+Jopv451aXE54d9S3bXr2T7lUwUa5MRBLZ0Nx28a1Kq8MyLj1RedvN4SXxY68l88ZT26CvUDF+5VZcvS1yrNNmVw8yaiT7fGMH09umQxBPFHlyEGJyXgatlYu1E0SBBq+ZqrtC8MWJT1LyqVgsnkIgq5jggXGbUh3yoEFob5sL9P9KJUJvxX8HTU1JG+ioXhEBGijsZXPrie/kCLbF328Fc2dlAVSVcgKadsjLQqiPEWc1a7b2FwbjCQxOs9w4q1FNoHalMWoD+1ZX8dTrNyPMbLLc8nZ59MIl5tVKUiDIFnbs46ZeaizdriTQR13e0zQk12GW9loG34Nuu6VeinTe9nHoXnvO53fHKKdZl9TW8oMmTpEYiK50HboCksguCO9bIoKX1bwziUcRFgxHAm6v9wl/BKZtDFVNC1r5NGMc9lWl1Ji02u/odyl5TcyWXUDTFJklgbLLJy8ig6nQr8csFZ0nEld1bTWFpAQXO/lSRi1YCXtzQL2dqyT+RBkrsolc9L5VkstWWt2550SM8wyDkfGPg6Na/HUaXcDJ2f8ZInaqT8hxUpRB82831r0blc1ysuQAWkn9HhsG8fzl8ml72O6q/Rcv1JQezAuKLeSU9rN6VNB6iZ1m8wT73DOmbhLVzJycIXWJmLgubyemEPZsXrq3jtdSy91QLfUoG6WTKB6DNlTTaeNlH2NtRG4N6iUiF654XEwcKMTTZa50lhsHjSRPZhZe/dw+aTfdCsrKo63yRuWT0VBxKxUkxuQb3AqppzoNiB1mE62y/Fm6Bm3q2Kb3PJ1I8ODRmwDsx9PMW5VZHTcR7Bj9n3SwpQ3FpywpMAEsZu0UyvLGEq3LYMMQ5g7nFTtU3S8xJO0NbdUwUhgaIC0LWeyqYA3hN4ZZ6iPPFDnOmxtcEfzRA3y6XLP7/JSY5PV0PEKIhODh1A1XUtHp01vZxLNNvGGcUCkXdaJlRk31lvxcJkkzp0LOyzKlqh5825X4rTe3hKftpWdqm9CpQe1yKHANOfs9yvHbJPtKPN6XzcXyE4Hr5mYrvVV2+oYvOGymy2KlwTuDvepQhoIYZPBgvcmug40WPUjNpq2ZCsdmgjpRHZUde2aLln7rMpyu5eHzeps0hf6chJyWQE23cKNWDpD1CPHkyT0h5TGHGmj4Fv5aHLeuaH5bH/dlMKtZtNufWpxEeHcU87gZXTVOow+aBmeFFaXWj7quDyBdHdTc4LA745HMtUAIJyZpdRtrIRQ8JXdyphSSZeGQmDlUlNr2JXSIbyeUnOp3eyUs5aFcSisoXYpj5mcxFkKO/QQd91Q7IHtheMqG/qMKNKqTQ1rfbKs22iqsbCu5bM5HOz+cAhgAfisC+Ltsd0xXjHWrKKcjKElKSgX7Z2zZ6GYalWNLU9hUw6HVKzvuJAnbJm4RKfcov1evgTZ3tgMKVQIq3zYmjx8s2CIZqDlii9M1zwR8UFr7Px6Usk1zTH+qqWM3BT0OgynKDWcvUreeGjZtXnUNoxiLstLhtzWBiK3Ye2UjhXRgtaiWV0qRzw1RjTzl0JNQKg4oaGOEIRoZEcYOmFBJjs2h47yiTaF7VK8xSZ+q7JbFW4hzBJTUxiaSTDd6Iraexc9bTbXwGsR0LrfQt4QmBCnlszy3KWm1GRha5bY1ihvEDdI3PLkOLmab3k42aUbMcNh2bQG/lxnigjwKEUS6+hNbi1Ah2nVY+eYsA21Ezh6F8rtwe8JxWCmG6+5ekiNHlLtQc45DBbFpU568jBQrcvqjpWiYhlGkAXiZmwtTgde2N2vSsUmomJE6disHaM7+A1naplNGGYFLFiyYpCNnHCJQhUeQEUKNQAVFHxkcKdSRD3f7ruzURZQbK13TLYyfeoIIQ527oboluhi7Xspu3HzaqhbZRLy3pdWIAFJyfY2bbqMnQjawiZvVpCYrzF+cgZYJLwOV60+qq/3A7P2bMXz22O5pm4oXhrUrVfGQCGLAj8GfVYm3eS5iZv78ZpYkwlSpV0oJ2fhRE5FX1aeqvvNkqBGn9vqnZWd/TSZ+CsDhw2bohhF8PhRgbX2EJQ9fyGJzpAymOaMguwaEhLyi1/A5v1wntCbZzWsytZ3Sp8MqmJJAluqYIgykoBbpRLcsLpkyLIStck9Hw9gRkDuRNWuYLvwb6N/UJPjzibwZUNPmk1gXb0HSZ4YJRaVpBhoCXfY5QgihNQ+g/EggNcOXHYHg+5GLgCcIBkOqTRHqmSuRaeJ11Yoh80jaicL3NU/Xxs9GVUwYBOliF5U6MRzRe4FyZLcq7SjR22FJ4SQIMxoqGTmn5WA4vP9cFtWo1mrBQOVZyFooQ4N1yR9Slhne7UZrddhtnP37nFpxcaOiiw4gGJpB5/7IFFGHnfNPRi52ZVEQCTZ3KZ0Cq87lAzn8WfIL9v7wRx0/3CKT1PcONGV4oqgYHYlf0OxXAz4o7v31cE+JCGeHaGmOOsIXGMkcijuHC8V/BYJhYoLfVWdBAHzsmrtktd4G9pC1x6XYUXpnnTqRiuxiUMW+aLWXhIwpOz7qzCJBjr2R4gac2hIOFcIblIxkSgPySh+FrPNRTiI9eYoye025ct9glCwdrvk+4l2Ob+53nvfEHjKN/ljR8QOubl7GlNYo5yU98pVt3swfgcK0wtGDzJNcrjGR1w699RjvRuxjM5tM6TgvKfWitgHXUD2PUkvTWfDgQ3E6BEONTFchquN7QQ+KC4wjasxQVR7Feo0KtMQE8GnINyRSMatVtL6ukyDy5QT3UDv3CNiKaavxFB+xPJdJOSnyYbuYacjSc67pGnol+5oi6ukKkdIJw5nuLRuNqfIKlZoYi5Fqp8Y/YaI6ztcZbUF7WSFKgLNd43hkidNgElbKZmU9iBAuDJYpTSdWiv3dciGLxl0xsu9tiarg6sej26v5SuXsnKcifel3eUc5GHX/WZkYEqEQYWfTI7JVQZz8fEmlBcwaMICLUsOtjn4dwZ0RrB39Q8iMtQYHvsHSnU3mIBN9eFSpBdR7Y3pTmTelKCELl3va6gOo7u3XnLCYZeQBQ6mBOhmrDg7kB0HwVpo4jAjOE76CdaCrLh5B2d1CSpXV+hVK/HeketuR1MxZNEVHN1sD+i0aiuiXpreNrVB/52K1D33trDvoibkYvcIcXoT9Nhqw9u2ysJblCZ5ZsytVDWFG0/ZJOe5SpiJlYGCfvRMCWsfuvBDyBB4HeXisNMqEQ2uFctt8F7lUH6vrrZVyxxXa0oWpHqfnonrWuUr0LaOjrA7Ult8jacJvh/vBI+UkGw4nlTLtXElMJ+km4N+cxBU2Y3BWPTX26oXiXuE4vSS8dIVJCsaF2UKCA32QpSm17HNNYj07Xo8YNcSVpN8OWKTQgkoH2TZGARWK4x7zL/wR6ryN6ddXh+dCI6OvA7geKjPba8wLpZFFbq2mjpQL9MGjGcOK6jaMFn82s+XWZ0KzYhjYnBvEqY3SGOVTMtisz6lZOGXznXNUUE2BHgqbs/H7UpJCBu0w+TVwGBpi7RNzacqgdwNrZIcsVI21iFeLzEib9PM8JYHOV9L43oPabgF37t1FZ+SM7XcJQxCQKmfiWDONEwC9DfJmdyvVweC2tw5B17dQV1D7e24MwZp4KCYGe8bH2GlMUnqHuthGaqWew3qkBjzhTVTnXfLXJTujuNVRlX4tdu3sOzfuM4YO3awnINLocZ9GV+WCOg6ebXTnQRNZW992LI9ey+J4/ZcpjyiJnahQnjvlHxr71B1oisew27KeenAmGvANJk22rkqxY21XwlLMiU9DnIIcl90h9PA7irxvtlgKqeF3G3ADNro0qBv6ZJh2/u1Z5uc8PqDUEzEYZMQKp4oBZvBSefbDYHZVCiC9vnCOCyHqnh3oKkrfgqyFR8Y/ZAFXhMMp/qCnYl27HuEh+ugOXl9f7+4EBSPAbGknaC3Va3zGQ0j78rV6uXyTLVZNqRgzMaMczYVgw3LAqZQdrB2g9ZRPA9UkzBaq1TkkHzQHW7ksgcj73qsB5FS7oc+v+qu5qtstL2vh6PVnkjMajtqiR0rd0etNIoq9nSRW1eOPm2wdcErHKbxR5U1eY6H8gw+Ei6YmKfyQi6raqv7Ck4R5oQYmpfubpUss9A9yLZIngqrJTkesV18J0vK8HL0HmMkBS93lG1ERzLJsV4ozqtht8YSzTfPeurVPYgZVsB3eeAx3f7c8lIZVxHCeEaKXJjpfAj8XQ+DzGa10IPo0qgpNyJXZYqkZ4azKviguoiPXoS1DQ3XKM/dwD6vfRa++4eVVwYlotE0/fe/v717mx++vh5C/9uvwc1PmP6fPcx6PpP68k7L41mgb3sfH7w+/vsi/fLurXZjINDzgV2TdeHr0dc/PK57/69eYZh3j883y748QH4+q2/tcH7h+i0uvK5p6/FzU2aPN1rADqdr5nc0m/k1Xhd8//Fh5leG4LisPb/+3JZAgyZ6m9+fnF9T8b3Ybv3Xafh6ePnuDUysdh67zWeMWH3262pW8vVCBNAN+4B8wN5+/7/Oo6OSMC8AAA== -->
