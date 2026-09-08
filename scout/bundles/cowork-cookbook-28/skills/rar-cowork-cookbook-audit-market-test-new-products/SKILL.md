---
name: "rar-cowork-cookbook-audit-market-test-new-products"
description: "Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_market_test_new_products", "rar_sha256": "fda4bcf9c7806ba2bc66ba2a7b2e4e783912bc2bad493d238c920efecdb4106c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_market_test_new_products`. The original RAPP
agent is preserved byte-for-byte in `audit_market_test_new_products_agent.py` and in the RCI capsule.

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

Market test new products Completeness Audit — Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
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
    "date_window": {
      "description": "Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
    },
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 fda4bcf9c7806ba2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_market_test_new_products_agent.py` first:

```bash
python3 audit_market_test_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_market_test_new_products_agent.py   # or on stdin
python3 audit_market_test_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Market test new products Completeness Audit — Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_market_test_new_products',
    "version": '3.0.3',
    "display_name": 'Market test new products Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-market-test-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-market-test-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0244c0383750101',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/market-test-new-products'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-market-test-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit market test new products records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to market test new products. Output an Excel workbook 'audit-market-test-new-products-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no market test new products data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads market test new products records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit market test new products records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants market test new products records in Dynamics 365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMarketTestNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMarketTestNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMarketTestNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVpbmX9G8HTG2W5nJIhaRHRUxSCBAIEDswlmRZgeJTezIXf99LtKbabvaVd0VMZ9GuUiCe89+nnOOLr++eX2XVs3b5zc98soV5+V5lkbNyivD1b4aq+YG3qqbD/6tgqrsmszvu6pp3z68hVEbNFndZVUJtmt92a68VRN54ceqzGewuqjzqIvKqG2f5Ooqz4J55fVh1q2qeFV4zS3qVl3UdqsyGld1U4V90LWARlA1YbvKyhUzl16RBe1qQ+Crw//W96dVXAHpVkk2ROUqjxIvX0Vll3XzB7Cv65syKxPAbsVOQZSvFgWeso9Zl4JtbRoBljVQMM7KcFkaeF2UVM28qvN+UUDvCyDY/Fr5CagZTd6iSPv2+ee/fnjLwOe3z7++BbnXgktv9KLN6amJARSRo1F9VwNszb0yAWvqGZi4BN8BXyB9AS6FUbx6//ZjG+Xxh9W///tt9Jqk/enzl3L1/vrytvwBll11abTqKq/tohBIXHt+lgOVP63ofPTm9l3zRfwWeKhMPr12/kapqld/We79+GLyKYm6H7+8VUAEb/Hfl7efVsCsX96afvn8aaFS//jTp7wao+bHn36j0/b+NQq6hRiQ+tPX9+/vZMHC35Zm8eqrrrL7d17AqVkdAeK/0295vUR/J/dukq+vxT9W9YfVn1Ne9PkLkPcVgz6g++dkgQ3AzrdP1yorf3zn0VQgdLwyiH786R+RDdIouOVZ2/2P6P78IpyC0AfWejfJTx+e7vvrav2u23ea/5htDQLmX9EELP/G7ruh/hHtp2f/jnSegeT87ss/JfdnG9Z/Wf38D3X7Zxs+rOIvb0yUg9xtPD+PPq9+fYbIzz+Ev1384a9/A6T/WzJ61TfBk8LXwiuzGCTf168//9A+L//w159/6GsQxZFXfO2b/M9o/pldn3z+YMH3VT/+cS/gb5a3shrL1fccWv1a1f+r+dunleXlWfjb9fbz6veZuLzWq0WJb0xfJvhdNrZA1t/Z8ae3vwHcKYE2AFaW2wA//u3fVqcsaKq2iruVHlR9twIO7rIiWoQ30gygZ/tEjSYCdm0zYNj3dSD+Fw8vEgMQ/uX/BE+U/xi8ozz0xOevL3D+uoDzVwDOX7+B8y+fVgagWjVZkpUAezVaVb+UXgIweOFYN1EbNQNAKX/uoo8gmT8uHxYo/+WfE/76pPGpnn95FovshXnaXljwru3z6NOimZ0C1H/pEQCQj6Yo6AH5vAqALHEGYHopA22VDwAvFyu0tyzPV2EGEKVbUH6hDSz1eSH2yy+/+F6bfilfAL1ZvepZC4EF38VZffwIlIrzLEm7L2UUpNXqh1//9sPqP1f/bNeT+MJDBWXi3Q9AwqOuyCuQV30Bli0FDgC6Fz798Ovf3k0LyJSgPgGvZXEWvTaDuLxF4Tc76zz9EcWJlR8B+wLbFnXVdEsty7pPKyFefZcXMF1uLXUhrUCVDaM6KsOoBFW4Sz2gzndLllW3akHwtTGoo30bPbn+4jfeU8QCJLjX/bI67VVQhaoc/LeI+VwENldlBsz/PQpe1wGR5od2tftG4tNKXiJxVXuNV6eN984j9l5+WYr6+3ZA3Fsagi/lUmyjxVTPtHiZBywClgneXfpx8fnSagAMeHUM3bc13lIrjWfNbL6U7XvIe0307C+AKPMq6bNwKQT/8R5SbVr1efi0H5B0ofTuhfDdK88YPP2jvmX/+47n2RisvvQojGCr/z+bo8UYNMdpLEcbLLNiZUO7vJy0dIqLM1/NJeD/FOyZkL91L98Q6htQfynzDERcM//Ha+XTte9rXuDXN8ATGq096YO4WiQFdJ9hv4Rx0ywJ430pv1WED0DmJ/wBzwOMADm0hO43hsvdb5KmAAiW7791B++WXrwDQntV9z7w0CqOotD3ghuQavHmNweDHIgWt41pFqR/0GpxALAYoL8CQmTAg6BqfPqO0q+730T/w8ZXE7RseTaIPcjc5kkAyBEtAi5xs7gOiNe9GnOg5+cnEaBGUXeL7j7IHaDp62LURPc+a7NuwcmXXaMaIPTH5f2l6XI1mmqQLsBYICnqHlj3mUZLQBSgxQEyACQBWVVkJSj5wCjvRngS9IoFEwDmvvekL4rPy+8KRc/cW2rVt42LIsuepfyvYiA6uDL/HjqMPwsTQK9YVjz5/n2kfee20F7gswUQCDh+u/vqEz69Sv2rl1h9o/v5v0w+P/5rw9GzeJt/DIDPq7Tr6vYzBL0K7rd6+wlAAfSStX3V3o+v3P+45P5HkPsfv+X+H6i+FP68+tck+wOJ98z4vEI+wZ/g5Zb0HlnvL2CI/cfd5SO23P1SatFvwArYVwUIrcVtMyj236vgtyWgFCYNQCCw+FUV26WYjqB+P8sA8MGX8vehvqQaqDJlsoRmW/0OAp7tAAj7l8u+Vytwq+wA73BpHJNoGdWeidFGb5/LPs8/vAF0jP67EW0pR8USzO0y1QFLA/jrsuj57YkNU7d8/OOsqzw/ePmnFRMBHMrb3wfcexFZiujv8uKlIdAsABw+rEJgl3YpekDDhfmSU14LghTE56JJN9eL6K9pbun/lg1fRwDL1fhf5WHAzVWz2G612PPpH4C0fdMs0LbYfBXnwB9LBredB2z64v+jqZ8OIJeLarngLWBbgD4BGPVwAZKTP/2pKM+68vVVV/5Elt8Xpd+XoAV5n/H9YRV9Sj6tFt5/Sv97H/xfidugDVnohNXnpSJ/eMc58A5mlw+r72MIMPD7YPic4MsezNw/LyPQ4vHnluUD2APevm/6/pOGH7399c/keoLh1yUmX5H199LJC8iBIrD4++8qLJD5lcXRu/b/PNM/ojBKfITxjyj2acrb6U/sBAR6gjkoiYtuvxntN9Gr5yi3iA5U7V6/PPz6BqLdW7z9Hu/vswBYDrDvY7v0QRDAA8AQfH9lLrj3L04J77vb1AN9Ktgehx7mBzEVkFuY8D3UD4jlzSN9NMIicruhEHAN9b0QozYhutkGFAqDJiwIfQyBiQDQe2X/16XVyxaJFnGAIT6CgI9+uw0uhe+qvERf7PR9KFlUftfo1zefwMBKHmsF+vXaQxTiQyjpz5KzduDtlI/m/e5a1ZHKOwk3ikt6Iu2zcXHpE4miUrpPpsP1rrnmrDvqehTSil1rx/VobEQoQD2Oy0WT9Ay56+Ak2Wsz3s7uFjqR7taL8HETpSc7b9hzPsP32zZvbprmO6Zlizd0No6kqN/1Sdr6s2LpznrrR1BGngjJNKt9WnLwPMlddpwnzKolVWjN8GCnzJjbWCNXmilytnVw6LuVdXLHFbhpCVUZQ6k3qE23Dm5+G4xiI8m69RCszJoPmburARZ2O1W597fU6tvjjPUOr+/9TMna/oDkqOjhVhd4cJChk7vHpNbSaoNVru1RbBo5E1Uxr+l1jOyqqaPMFDrx1zXph6VEUhQ0kPndueLUsHGvJI4NuH9xhHtohempCzCxOeGtZXdWUtCRlGv7B7Rvxp4mpHkQXEMWEFGgSS8ksIOQwwm5o7mZkopz+6iJ+BTn5zo4F7PYiAdi27B7TDwG/PWyUwovKSYjYIZcn8TcZE3b0Y+o5dgSGw6SCzXt4WH42+QSJIOh76r6hl646IAN1W6ecuYYpTKbR/vjoS0kQzrat6bvkQzMI5DLJIJeng/Fjj47qhue79rgxSHhRDZOXeBGnGZdk29tPQtKheRjqO6SzLDnQy1cLsp4T+7Ifd+1wekCj+q2aNCrkZE7HRWPa5Ee8IBAxJ3VexxfirHUXIy+MEAYqXgQBlpqs7lsWc5NqUhSGZtTIsjF4QQJyYXK69YSm1FRpPBEHkYaQ3ndFtpmN8LGFrGPu6u3v9K3SJMmY60yO0Pf7k4d1qbmsL8nJsOh8N6xO7o5o7Kwd0i5ttpJ1IxcI+xLjaSd06IPscngdE/dxGCLhOk9IJNWOR/WpwwWsYdyjB9XG9qXSEpvzWhUBF9ORzs8KGdf5qnKK7EcsSInJ5WkwqpCK6KYwbEtXK1NbQ3lpgIVZsmP4hGnvOMmOhLtRpnEeMItYTSutHGFJvA3HYarYrsqvtvvY+PwoJRhK0mjmweCnliCddvnLYa2e0NH8kuLqa5WxeJdlY5MUu4RMd3lp10at/FGf5DxuPMfXJUZZGIPDn7gNeU2Oa6Q5vg1IfxL2DpcK+I1V9i6JQ5s1Ug7+FqmZuPJO4bcwWziOJOwY9TphNJyz1mwVhVYi7IWpuFqYaHXZnf1CSkWEE0cdsi6Is25sxvtngCbJUddO++s3eFinR9quD+ylSqwl5K6lq3ePI7yyOXDWLqCx6WyNsuRBpV+ufdBw3xabx7w+PAed2hvXUr3ACut3Spwd+PcozYy6XSaHFnPhSunrbPjFr6ewkOU+3fR7NN6j9l3a5efnctdr26qdao1I3BF9MFAObmb6U2OnpIhUce9HRlMb/OCX/cofppqTiVwBoDtzrX1gUOqAFHKiBP4gD/37q4UKKFG5QI6CXUgQEXBHlheHWxIaIWtffFuGWmjERdX/tYjj45EYhf56LH7FrMHe3eQzvtptDF0u0VaYV2SEj+qsNzSyD0Q3RF2lMeezj2QE4cW1i0hnRtN3kWIXkhiyHNpXtEcmsVuGXBbKj90NLsRRlXdaDpc9puQiMVdJnmZXY7kZkKKmKBS+bHNCJ27JvyFd0vbyFlcOw7eEQ/huNncy00DZaMl76QNnXO8rIbn82joGexwlEtu0pPcWRpl3/bRkbR1tHJR+SRO/F5EQSfKejhrSIp606QHZtq0dtIb5+IdrpGW8fReICxlOs/5tYSyqbhtmse6QYetO+/OhsCm8lHn3Av3YGdiLZhjhhF7PmD08UhQron2t8sOOjO6iWxTXDuwvkJz2rHww5pkrjJL3JzkkNq2tCGwcTYnq+e28aSaZ1ac6irq0yqqHIsYraZnddbGb3S4MfS22l81V+iuyVXn+c1m3Rs5CinOgTuLhR1fjoR0xBE253IHO5n946ERBz7pT+NcbdtepUq4Zvt84JmunlJ6vKsluUWsWNu6KhTHEt9g25g3tnNYmEVkIgJe32KRvCQpwwsgzsONNIo35KjLB0eqL819dziMXUoRLJHVbbClndOGtde7dpBL8xB4Ju3w/Y1VOVu/eUhl1GIgwflJhI1kb+4xIUtmkc+ZDoaOlI2GBguRt8eVOZ5IIrluT3kkasOgMk3VlbINar15YVQ2ULyboCo92vs3CyZ0rx63DNEiPlFKUwnv6IcmzmK2tdh8r5A3V8t3Upfmc5AemIzjd9zaODVD2O8ckIHjeH2UBXy6nwOTr1SZYc4bGetIqj/2gsIKDb42euJ6OkdWZXh0Jsk1rUYNUR/5w5qb29InuBmz6RN9T465jFoRbencWcD2dSSaYra/7wO7HKAm52zzeJhpzSpPCJVN91Tc+/SOL+zg7j0EFY+b7UkUxWIWbCWf5ePuLo1cNPCYbO+baI/qLUtcO4/lb9viXPCiRZ/WkUXtgmOFtTBz0/GJ2x9AeZVSSu6dnnqkoqKXO0Hi6CoI6SyS4Caegrmh01rSr20LOoMyKV0t2kPlodFYKa/88DgL85Yzi63JBKh9MGVmJrriZjEKadMjLbPug3KQovIJJhU0r5ZLTbciWFRLijsnF9C00DaV5Jd8WyD2cLoZdg7bO7u61J7ptMd29sadKtXnZI8cS5qa5XBnKUWJJTKbnlyETzb5QGrskeKqXZZcIdQJM4FDReiSM5eomDS0vBRH9GjRIn9f98EjI2ODyGgzIBTusGkuQ5n0xq4Qzy3k9ENgUTei5tZzrtcebZYSRUaOlBIRH0H7wvR3pSObB5KxDU2IA8eTz0QGb/I9LrN6i+X7gyjRQwObpiu6RclE6WE6VCyS9Ft4ci4TqhgU7ci7Q3gZJZrBfHGcRa3q5yw977bdxqjvEWWZ/sU0NEsH/VZ/fES7lBaDc7tPky1st8bJwmf9qkVlAxtKcUyItQ6fLhvIKcI1Il6T+jgixUORb6K/3iH7xKQlSb9neq0W1yB5dKMto33mtfb2SJmQDzFE6FocJMAsqquhgGHrhBlieJ17wcFTb4Hac7oOW+cyOjPa6ZJrjWrehD50cOyxH2y8U0xBPBfnGoE1QRNvV10wUkYzeI+NHDdruZ2fTsVZK0OrVijq0YF6Olyv1kXmuzGhR8RLDjdB944AamSaYYWShlmDzQP3oJHulS7M5i5VTu6a+Xzx8frM7+XueAjhjVj6e8NUdsxNwx6pnvKWZnJTSvSOe5H2ST9eiovUFnlwgRxmjafWrd/e2P4BtVGtWMjhgFGResXgEOJVOXPU3jucoqYP/ObQ+qa6Nm7KxOsOVOzvXDu10MiY6ekg7KU57wVtEHB0QxTJ2TRLDy2rzXFzrrG1ykNUGg0PhFIPDuB0g5TUuDaWovONdvQdOxD7yk1M9BgfrEI2Tmhd3DpzMNQHk/frW3tQRZGhuwkz7ojnalnYll1J1pc05Ta7g+UG3e58qm5ufomOiHFcs1kpuMeqqwnXOcecKKRmZpzEyORpEKqe2UkJshdvLWKGRHrWjN6ByVtDH9YYa1M+pNX2Yz7u/N44blqPJbtxaPDHaYcZcxaQ+OjJYaU2uypDrEYutKjv5dKTC2LGq9uUlS2pV+NYSpiJ7ewIpe9K7MLboHMvWZ/P0w41LsY6BPlmBnoRaHl6NLwkr4+RDtoJ1GLvyfZWidmsILnFN+jxesmDSuejDpWr/TEl/WyPnygwtgUjTD0A/Nu8C7O8QoiG0/iXsirOeyYVHc5jNTFHxNm2KczTdCQeZDetRUFhcMq+yGl6CLkgszKGv+CwdQADG6gOjqzZdkRIsNPJV6UhCj8pDaGq98M9NllFkIxZD3UXDvb+NfXFCbaN5krc7vhwD4x4Q/Ic73Ii0a9x9paYBsCvaT/K+T030/7octr2UlUucY3HmNxch50zQ+zxVpJnFZpkiD1cyXp/MDOu2YrjI/KcSib87nLbFYy+R9drdatJtzw3RLsNyN7usQojiHPUXrsURpCxRAYqc8iSvu/oU4I8uuu1dWghJEu1nD2Cm/hMwA8GzbX7WkTRBsbIjRpfTDEIrHuryWm/lS3U59AddQGhRZwnusfIXD4NTTA0SMvnMmwT1R4yOALzIGy4PHB3fw7T41k8Hr3LdhsfenSkHU/zO+0KaoYysRdgQ/x4N3okYE/uBNpTrmmvW5ji+Z1bdBItIRRoxfKtqeQ31JEe9rS1HY09KRwCB+Ft6LMNfb8hOF/JG0M4789iA0OVKZ/yWypgOweMfumZOKpyseVghLUuKrInhHWLRDbhQJnH5mqkl7wLYAU9ZCa/Yei8VDbagCU031pU6uzJZjK3dGqyulTN+/DC64pmorBTp0nXn9dpQawDJmpGqN3cFNJfO4hCqD7sAQu4lVz2YdoWOGUc70ViFOtD0zFXkyTnKDBmiujTTj0ETHsZt3LAnCMetGabxiV4NeramSW95tGVeY/joKMjcX8k241lom5ZDcqgYPNdb5K12QRKgl9R5NBfK7lQ5KhWKfaiH12Lr9vHfnPoUEm21oTcWB0rw5uLTrU50UMB/egxLzTgGJO2t40q3JChsteHYWKCncRixcTBRTQrwcQ8jneplmEgkeFXh+PGLrZQZ6n61B8iB6JE9x4MoBBRNUqJArO5+XfHpeZjjvdYy8gXT51KrGm5zPG3kbAN9vAthiaKhNIBuUrHfXxFrhAkQhh5CTU27k4gpEYlQ4CRD4oI4eGsYzmOH4vpzsJbrWBgzd0et0xskkfe8fT0UY+adjAr34uEdVpRdHCbd2Oscmp/e/AY4sOUpj/wR3e3EsYeEBTmy8ucUE3FYZWlQFKgYOOEFwony4PC1ngMC1MknvypRk1F2ub09mbk+xLCNw541SibxfxaR4OEiMM+mV2F7wS4TC3heKbYKX6ofeHLjd8LTvOwrTCQlYd7ovjKO1BzJ+GiB+U55Skb7BLgGz+5gJ4/0WIpwfw46vctqYaYxsJ22XUukR6tM4/ht8klXUIG/buPDRazUe4tc+YeVx/WVX9NcQ20I6WIM5LjpkEfx17aYL1U6zHLOD6r1+IN+DdTr8kIaXCYtS4imFzijg/DJKN1vz9svSgBQNaoyI5XuVCXr/vbyLBWxWIgwu1TGcuIpK+lczhcGHekFJtvhr18c80WWtvpNlY3ZLsmyfU5O1CJoXfXRzr3j1iJWqkRwgt8SzC8kKH0EmLIIfLjUM/8gawusDBD2yPOW7L/kMA8NfRSRd6k02QiN3w34tLd5aNBwT3ckEGfRQ2HnD2JWzRm5E0Y+SR+rat5rReyDVXYzRYVUWkeye5hn51hSpE01BwsYB5u4V9ho/Q32VAKHuVWPh/Cu8jbPhpDI3u9KCI6wBvN3VQ56I6YIM9EXohCLA9UTQuGc4EHlFtgzO0UUJx0n/qwnSSB2cLxtjbXRSUYQgQ6hynnEW0w8es65E2pvB84KmEMvtvcz5W/wQd76E3CIzxcxsm+5IKhrUAdjK7lGlHIku9gC06m7dqJXEfqMUS+pvWAxcfQ5DFz7dqGg5Td4wayPiaHiyOPNqIoV3udBlEZ14GZy8G6nNtz4myZXhT17s4R8wPOp0dYYXB0R+4qKsDBCcZty4VhOX/cmWkiS2TjF1U8HXg0ae/lcVNIZ24GM2HWHuESSQernxqbuRwMosA7hMeqChrkMdG4USpOyuxHiSgL6628VcfWPtREfr4ya/rANHdIDOgzdgqIaK8+BLhPgj6bTceINgybxFpp81qv8pPtN7XkynHDcNRm9KWzGRbBrbtfHjuANcHDwiWYCndKMiQnnIWC27mvhjN/2WBC6FVXeAqv25Cw+EJPipynoO0USO2muPrzMM+VqiU1t2mltoXg+CLemOPQndPNbgy97BptmgLJFVvGL4TVcaSCPHLKqHDdHrVmczrNWuzkrXtHdk1bnKYNLNGYTMaeLyuqHZAYqvchmJ+Wnwq2zoGsEyd12esNU0dky639aOeDgZ8abGGqGUqlaRRW9+cDiZnsFT8SHaWbZ5tszrdWwrRiG2zTiWmYcOZkW25IS3E3A9KdKDPyTOPW19uHwzSoi88SQsL01odwYW4n9EbPkjHtxmRwAxzbyd6uxdNx2JDOpoYqD4shA/YcQ9zSri0hJc9uGj+sjYq3nWDoID3K8YCbe2ZyfTmgHtf2kTkIFprMAfS6j0Y30sO98LnwgjLs7NIIcjL0Xu5PsX+ler9BhceZOqGlqdo5SYbtwOykrRUrrmM64Wa6+U6vq4/zcWjaOcKQiL1Qwp492wTOYwehlbGUBf3UowwkmiZD7vqIj+vBexgddb2q4trWeQPdErGAlEUD5nPI5ChWSUYUnmQGFY2xv1PEY3wgjhlOchzdIzKCPfLeKRRURiqUN85+TT5wY+17YyCvu4DbSGAck4Zk9K/4TdjVx2pNdBZCFNZxQhi9m0zUhuDtbhPDuHHQt9GIQR56Cju8QuhuK1O9R+Z+L3ubzSQH0VYfHo4sjjJ/lWkSjIAoJqd4qU9Eg6rGIXaaVu68GKLzOwZteXbPz7jHpjrd17Ya4PdEnGnRgGEN38eu7MKRKmVVsJbD/XSZg91jc74SxjnsaUTgsgQLSvx8SuB2owzRWcE8gYoGVEYdj0UhZ1incXP2OH6teFHghf6GHR7BQcQTStpxd2ojYQpp9i4jdI+tkdQyG6pKIlUB15IbAr/zeAhBVzWBBT5OJBaHruNEwToY/UDCe/Hs5MSJlFLgfK1NiqsdeVYQMhAWz/AdZgt8T9P0X94+vP12aPb2P3wMbDnT+X92fPQ6Bfr2ZMfzLDDyws9PXp//pwL99cNbE2RAnNfxWJv3yftR098djn3854d7y9759VTVtwPm13l15yXLU8ZvWRn2bdfMX9sqfz7TAXb4fbs8m9gucgXg/fcHmU92r9PLLCm/dtXXJuqyZjkWy8rlOY0ozLzu29fk/ZwQrH8/qv0KPP01aupFw/dnAoBim0/wp83b3/4ve4JG+CIuAAA= -->
