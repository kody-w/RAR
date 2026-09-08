---
name: "rar-cowork-cookbook-bulk-update-manage-loyalty-programs"
description: "Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_loyalty_programs", "rar_sha256": "aaf91997eb88313bd07d81c0ed8cb4ab269ac49aa7be987bae2c7716a931e97a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_loyalty_programs_agent.py` and in the RCI capsule.

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

Manage loyalty programs Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF; sandbox first).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
    "record_ids": {
      "description": "List of loyalty program record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 aaf91997eb88313b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_loyalty_programs_agent.py` first:

```bash
python3 bulk_update_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_loyalty_programs_agent.py   # or on stdin
python3 bulk_update_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_loyalty_programs',
    "version": '3.0.3',
    "display_name": 'Manage loyalty programs Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b5eda514b4777c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF; sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of loyalty program record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage loyalty programs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage loyalty programs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co', 'example_request': 'Bulk update these loyalty program record IDs in USMF sandbox to tier Gold — show me the dry-run first.', 'inputs': [{'description': 'List of loyalty program record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF; sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of loyalty program record IDs in D365 F&SCM, with a reviewed dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageLoyaltyPrograms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageLoyaltyPrograms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of loyalty program record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916+fObVrbnv6L5vqqJ87ANAsTirq4aCYEQYkdCgjjlsINYxSYgL//7XCTZSbrdbzpT89PIZUtc7j37+ZxzDL++OV0bl/XbpzcjcIrFzsmyJA7qhVP4C6a8l3UKvsrUBX8XXlm0deJ2bVk3b+/f/KDx6qRqk7IAx9dVlSVBs3AWbpelizAJMn/RVb7TBou2XGzHwskTr1lgxGrB/U+DkRZZOTpZOy6quoxqJ1/UgVfWfrNIikUWRE62CIo2AfdPhsQt+sRZtHHwVabtTIbV1UWVdVFSvJ+J+J2XFBEQwK/HD3VXgLWgT4L7Yj7xUCAsgWIV2NoD6m4ALgOgVJ4nbTuf9GKniGYVgO7B10UH7ADKBoOTV1nQvH366ef3bwn4/fbp1zcvcxqw9LYBKp8eukpO4USB+FRNfWo2GysDpMHGagTWLsB1FdSAfQ6W/CBcvK7eNUEWvl/853+md6eOmh8/fS4Wr8/nt/mPDrSardCWTtMG/sJzKsdNMmClj4t1dnfGBlix7epi9kMDnFVEH58nf6dUVou/z/fePZl8jIL23ee3EojgzK78/PbjApjp8xuwIPj9caZSvfvxY1beg/rdj7/TaTr3GnjtTAxI/fHL6/pFFmz8fWsSLr4YKsu8eAFHJ1UAiP9Bv/nzFP1F7mWSL8/N78rq/eL7lGd9/g7kfYajC+h+nyywATj59vFaJsW7Fw8QCUHhFF7w7sd/RdaLAy/Nkqb9t+j+9CQcB44PrPUyyY/vH+77eQG9dPtG81+zrUDA/BVNwPav7L4Z6l/Rfnj2H0hnSQEi/6svv0vuewegvy9++pe6/XcH3i/Cz2/bIEt6EHduFnxa/PoIkZ9+8H9f/OHn3wDp/yMZo+xq70HhS+4USRg07ZcvP/3QPJZ/+PmnH7oKRHHg5F+6Ovseze/Z9cHnTxZ87Xr357OA/6lIi/JeLL7l0OLXsvof9W8fF6aTJf7v682nxR8zcf5Ai1mJr0yfJvhDNjZA1j/Y8ce33wD4FECbznvcBvjxH/+xkBKvLpsybBeGV3btAji4TfJgFv4YJwBRmwdqADgM6iYBhn3tA/E/e3iWuAwXv/wv7wGuH7wX4MMzkn95YvhsWQBsX16g/eUF2s0vHxdHQLqsEwDDAFX1tap+nncW7cwWQHAT1D2AKndsgw8goz/MP2aM/+XfoP7lQehjNf7yAOXkiX46s5+Rr+my4OOs4zkOipdGHqhhwRB4HeCRlR4QKEwAar8Hujdl1gPknO3RpEmWLfwEYAuoZeODNrDZp5nYL7/84jpN/Ll4QjW2eBa5BgYbvomz+PABaBZmSRS3n4vAi8vFD7/+9sPivxb/3akH8ZmHCqrGyyNAQsFQ5AXIsC4H2+byB6Dd8R8e+fW3l30BmQJUZeC/JJyr7HwYRGga+F+NbfDrD+iK+FrWQIUq60cBS9qPi324+CYvYDrfmitEXDbtwg+qoPCDwhsBVQeo882SRdkuGhCGTTi+X3RN8OD6i1s7DxFzkOpO+8tCYlRQj8psrvL1qz6Bw2WRAPN/C4XnOiBS/9AsNl9JfFzIc0wuKqd2qrh2XjxC5+mXuVy/jgPizqII7p+LufYGs6keCfI0D9gELOO9XPph9vmjsAPHNl95P/Y4c9U8Pqpn/bloXsHv1MGj+wCijIuoS/y5JPztFVJNXHaglZntBySdKb284L+88ojBZ93/x54GqDo3Q9yjGXo2CIvPHYos8cX/z/3SbJD1bqezu/WR3S5Y+ahbT0fNLeTs0GfXOUs783gk5e+9zFe8+grbn4ssAVFXj3977ny497XnCYVdDbyhr/UHfRBbwFEz3Ufoz6Fc1w9Tfy6+1of3QM4HGALvA5wAeTQb/SvD9w8tnpLGAAzm6997hZfhZ7VBeC+qzs1A6IVB4LuOlwKp6jl9X24GeRDMqXyPEy/+k1azu0C4AfoLIEQCEhLUkI/fMPt596vofzr4bInmI492sQPZWz8IADmCWcDZIfekBSDmtM+OHej56UEEqJFX7ay7C/IHaPpcDOrg1iVN0s5Y+bRrUAGo/jB/PzWdV4OhAikDjAUSo+qAdR+pNLs9Bw0PkAGgCcisPClAAwCM8jLCg6CTz7gAcPfVoT4pPpZfCgWP/Jsr19eDsyLzmbkZWIRAdLAy/hE+jt8LE0Avn3c8+P5jpH3jNtOeIbQBMAg4fr377Bo+Pgv/s7NYfKX76Z9Gond/bWp6lPLTnwPg0yJu26r5BMPP8vu1+n4EmQY/ZW0elfjDEx0+PGvlhxccfPgKNX8i/dT60+KvifcnEq/0+LRYfkQ+IvMt8RVerw+wBvNhY33A57ufCz34HWEB+zIH8TX7bgSl/1s5/LoF1MSoBqAFNj/LYzNX1Tso5I96ABzxufhjvM/59oKb98BFf8CBR18AYv/pt29lC9wqWsDbn3vJKPg4j2Cz+E3w9qnosuz9G8DX4N8a3ebilM9h3cwjHzA3aM7aJHhcfUXH+fef52F2APjugYz4BqBOCGgsnhg7p8wcbf8Kemd527GaBXyOcXPj94Ckof1nXsrjh5N9XGwDAH9Z88c4f9WvuX7/IR2fNgW29IA67xez/s1cb4FNZ03nVHYakBsgLb4ry6PifHlWnH8W6FFu/lSUXs2BEz1Sd/EOTL1Ol7WPYvU3gAKF75YD4F437Y/fZQhq/xdgxe5p9z+zm1HgUUDfNT8+AgJsXjw2zwtz6wCK7UOGwAEo/NT9u1y+Nd7/zOQMup2ZhF9+mlV5/4JS8A2GpfeLb3MPMOZrEp05BEUHhvyf5plrDqXHkfkHOAO+vh369t8pbvD283fkeor8JfG/o70Izs8l5vv9wWK/bZ61bfbxd5R+UAfgD0roLOjvFvhdjvIxCM5yALnb5/9b/PoGcsIBNJ1XVrwmCbAdYOWHZu6dYAAdgCG4fiY5uPd/M2O8SDSxAxpcQMNxQnpJ02TgUhS2xFwfIX1q6SGBT3ku7rgoQTseTjsO6QY0RbpOgHokuSQcGlsGNOkAek+0+PJsZgDJWSZgjQ8AcILfb4Ml/6XPU/7ZWN9Gmkf+P9X69c0lcLCTx5v9+vlhYGjpEiju6isXmoigJLTdudr7jVDJ+Jre1vp5EOToyF4TlmTvmhMlK5Sj8kPeon6fRflmzU+sqrDUeCQLUzbDs3xMq2Xqo849jjjxYp6LY4WJ/rgy6evQU2y9824ymylDZioDlydn96isRsodpbrRxNoRNFhgdk22TXgMJjssOVcVd+7sTaIHcs0nsBwIuz2CIY0/1fvBDGHITChoD2ECARExe86jRBM9gruyTi5f98aBwbGBpwkoSFjIYfJDre+L8XI2LlZ23BcySp2c9OQWOmUZ+3h3jvA7YjGiSstMew05KWzF8tzuDqawW99GS5ek8LS9HahTmJ0Sg7fIi24gUns9BKzMJ6wSYyyQ0FI3zcrrRWoVqEWLgZ5fudQQCUnphSQdRE7IdSVssuaEjHhlogfRIjick1aniqfXKMwGfpbHgZ3W7abiAntSbXWSjOW1MtwoyrKTYNhMc+Gae5OL2LmREqdmlpDHjYxnG1NxP5G74IaNVrQPVCJqlveUze765bxGNx2E5OFa3K6Wbn6Gb75w2CQ7LTwwFaqo0hbz4kulHUaTybyxWwtquWHGoJNSMxHsBOraLUg9asU4zRXTORABHHwtlN7iI8xHlKuaBzu8vVM4Ybqg2Q064aDImu3ePZGJk6uv32urb7WNzVWZn0WaquSai2PEieMvZcbgyDUvqduJhE5KG3Bj4p+L5ObXvX2EqkA1NrA5LDVuYxmnjDUd7Xbt2SqfbmAyFPgVe1vfTPJiNNSxiJBJGjpL3dm6sfGgqJyi0DSx5rSxXHQd3e3ruIUcd+Vpnlw3+3sfwCwVIfUGkQjrJHs3bdfyLHYV62wJQpWvDMm/dH6UoxIqr9Lc3mi3kYP2LTxG3tLNpmKj4uuwZ4gDajSXSIB77RwlwQEzslROJlyQer5Us+0ZkqfGQA+yAKt2xPZb5U7wI76U8CmX7oftzdptCAvf2OeaDrtyXZ0Ku+CjTi3RlRBdauaiDlUIcfDd3PW1mtsqvWaT8LiaaLmn3AhnhZZTBzG9ZhGBarw3HkzSM28ivI8QNNcnegS9xNBI0foodDI/MlsMmRBv3ahWttHuzqbEOtvksnWKIPAGVSLc7jL24jKGkiJiutuXortZ3lK5XV/11ToQN55ypUOxMY/eUYk0LF41+7Mf8GpsawxycKXpjud0oqc8ytykbU0tb1VKYO4aylIrNAhFrfwLj3TZ1dlllqEf7HrcijU9YSfFrwTVF1sq2OKIzmmbQj93IjxV/Jb3C0u2MRQZJ7c24FRowttI7JT7sEfbDM4Nz9grwrjHnVpiDXcsOM3COZiwr1vjylm39i6t9gEzGoIDZ/tiddspjLoxb+eQUhC3lLVbtxUsAzO5lLhwCbRuplCQ8+DY2tYJ5mljTKtNgot1eEUEURqH2MMigyVPcGYMOlxG+/6gZwcuASDZrCeCLJZifF25o3nnh76hFPis4iliTsU0YI1D2E4Sp8qenta5M/p7Cdsguz13lVnYjqCDlLWR1G5jSEaFyZT2rF9lEn7B1hySCXzcObeluLFjkbojUM+0E3kgIyy/epSjEFG0keHQds7OcifncHbg9Wzd9gMSTIXaLaddWFRZxoFwV2iG6LyrYK+KrXa++uuRoXwYo1FsxaTK1S8tTruqrmzYA7dibWbbb8ihzHeb7ogQa7laM7nFbWOkQdWRI7ZdbBXAkTvmao9eongwc74nep+d7cjNbCPRq+Xa2A+VMMlJukmL/dBfbrCw7JEr6gpGLmylbm9XV/eyC43jmSorl8MRalXcbhMQpXFjLT6l4UYbGAljG4bEFOss1SKplhw3oFzKasuyvmwJ97QfbqstOZYmtaWvkb6Wl9uhv2E5wLvGvE0RtwKwhTcr5bzzhvPJPTgnz5ogiKRWyrREJ4XJkTFjPFy4qCl1S41ruoGOipz6JyUaNDrxC7FYwQ21khQItTS/1ZndNqgHombFFSR1vbmkYYpCsLsfnuvuntSUUF76fLDWDVOyO3SlFtGqPEteesZvrV/ztnanFZ5i99r1dsjHaTzjedlfDEkamqQRJym/DGqh7RJCKwzJOV0EXNXM4HjP+22wOrpcnDOhhlfcNdk3O8Q4WDmb3B1qvKY0C7lnnZI99pYWdIqcVrsN7CwVik6H7ZK4201OZcmq2cr9XboNBad2J/6A6ENy64/oeWhPkt/HBLsnmJOGHVeZhSdKt5URYbiOMsdvmV3A2TBJ7pRon0iGQF/FnGAlhUmMlOEpwRPEbnus4o5fuVfMOzbahrE7WdJ5HMaQE3dbDzJn6Y1sXCgpTyY+QwVQDyQaBxPobmMeluuuFkUIv6FaIur6hhBlBhMTNF0nk9TBSCecSuuQ3dObOniOOV7uB0drEsToV4m9xzt4acbuvl/f+P3QyquIZqCjOfJ7iE+D88EbeEEC6JnFZKOeeM8oziyt+u3Jsgj2qFy2Dcaid2a/KbVBcLw2dSDM8HRtY8DcpgKNxJBlOHYReu4w4sJoNEJiuh4t3cz7Gu6Vir2jOkNaqJOFI14c68xxqtGtI1JWBydLUkGJUWmTrAlhuuRxrZprR9bZS3mxqzS+xEqxIvUM3zGOwd57Vsx3TnExQjZZ+2NgA9DhCTvlOLbPOb/kDrflmVnpObH3dkJxyHVQ8P0oPlfs6hp0K3of5NBW27aaSnvTteTyAwMNO15q3Os+vfiTney7XGCu4bE1dbGrwC6u3xpHCZaaCzYc5avF7g/ebcX3LshH6twiu62/3LK12KKwckxwWqKXrrrfGXygHgXW2ix9fFteLntVAxP4acmcR2wrbHbF6X5mlrKzVovlqbAqG625QBci1tovjcCsEyWmG6on1p3DMC4TTau9pNTo5MVlO6Z5pNEscvUbmGTi0mYVw0kklFNXJ2fk8mojVRHFGv3RMeC84fXxnG3zHqINzdeQ8nAMOdyfrrZ6q/DNXjCijWCZp4ATCCRc7eTbdqANoso0PIb7HanC/XGlRJiwi1EqIiWq4MktKocxVCP3EQnXttopunMabZVKd46e73osr/eCz8Nq7rH0IRuXWlkxl0zrUJxhG8PcJ/J6l/nMRew695CceG5fxvU1SSVQ2WOWcx1G7PI9e4gU48hxAp0eeWVp11JOod64uWGYEouMHBbCjW3ldK9lwvlUn70bUam2VzoC32y2APo4ro3guBCY05QuFcaATFOxOqftdgd0b02otZJvmc+tnbNwcut4Av+u9/vci72+FsYDv+JCQac3PLNJp9GMfRHjmxMorvtkG5cxecAhhrE8fkuveXbvOHsf29kifMVcg1jzS1aXbKwv1+K4DMnbZTWGq5vbG0aIHvw9YaNH2ltznSwjt7uZ66bGy67M5dOEp6hgcbuUsU1a3602UNROonc6yL2+C4FZV9xRSa1D02/22kCrk7VcBau9RRnLAypwxjFOuII8Sno3OYYBorWrJqRkcGqVxASWchfiPmlXCbOa1pfA/A55uz1eaKbmi/jdhWOIzNdJN3g737INv+G2XdNQFDtd2sjLWFLd3wgeE4ucwPxd13nMMKD5yWpl+LoNdocWSuMjMZBHSjJXR2UjU5XIXYS7Wmoqw0brymDdMzvcziQ0ZoTZQP7JZdKsroapdQEy7gRZoYQoTVqnkbzzUXZQK3YZW2rSHBEcVjHJbNUh7C6FeGEFO6LXCJEL3ZCxmZabg4Fa49hZ5paClCmhw6LOJldu9wyPsFN2YnDctrMzwSqbkBLYFt5veT06syqbbRoW54jKk2ppCG2YUYhllXMHb+fGR9rWYaFq5Uq8qhoV+gJ63nHMreAi3YU2/SHMbp2uFXEAK2J/78McHy5NtT8Y++XloiccIorOiN5bFyv3KiFB0mWtnI7y7bBX1OuA0zJUDl7n5BZ5vyyHwtOr6Gahh+sxhixoTwWN5p2W23t9AtGoSSuJvObNIRo631XlDoJOEwPpoQUGytATBS0twAxZ7jojjBhlNcXRMKq2rAoJ3ocKIS9xzUxrdyNZvYK29S1ud7yTXFeREB7w1XkUjuKJRY+tNBZXPDQlljcQ4eibDr2CdnDojA6ekQ1ySlsG1MfTkC9xHzHYbWFe1tK5gpitUhvro9OihwzJUjJiBbHa7FtqFPYehbln2XLP+GFlkak6LonTcNg4jZkvGVzAldtKg8OpuXeYZsgu4fdRSyU8yRKteWj7mqYiD9NJUysq0U1xi5O5PlwxuVb5G20rOeHIitdoFdx3VK7duQFMrKVY3+v1RcmOR4kcbzmTdMSFyu+NrB660UGNc6omEuahzuSb2CYPt/Blhx4ZOYOLaMv0FHYSt+uhgnF4qZNrSFx6MAKZqsCF5z07ZoibxW3MgcYoUe/lleBFq1ofo2GJFTnWUWQJlZhcSvbyhIgoXtxVBWLAuBQKmcnffQKM+RVTyYpL9QXakGGGnONBlhv3jrXW7k4o9HHZnTNE97HMQWwCiaceKyhAq+lR/HAgm+IyoGZh7ZSuw6fbkU8uae13KaiyzhbTLoW46XqviLdSXZucY42kfm7DirSETR1X1465tN3FXweuGpMcGdEYr9+wltpSWIu69oXrUTYi6PxG5BhChtpVdum1gEy5f4iF0AtYk0+TW0Hyuhh38ZiCXkAEMxVq8LHtDiHaH4cAKDGhwX5Hu2typdWpcfJDf5e0vUNFpXRBEDpr17bMxFsjvEbBUoAhtQ8pOWxMUzcyuwp79ALJ3fqiN6BehCsirqqwJdaXe+mYaKVqFyxF3bRsj5OyhlL+NIT343gd1wR8LM7utIk2W8eQt5gUIuwpUUZHol1oPKqtqneiKdUUdoCs3WHypUaa6jLcTVw6YmCguZ4KqR2xnFHuozTYqWVd6glOYnmwyFotjgnRMadt6e8TeAf1HQQ7Ht7gZbLqrICgSNEV0vVlb63E3WnvsPghxy+qLmCwyx5PqnGmRhK/CdVxBR2MNOBBB0f75njDQIyt4ggq2YnDtcRYG7mxQSCY9mwftYvV9sjqS9FYLhOlSYRqJTA9OrH1xWw6USN2TnDCuawlIk+/Tw2GBA3Vhc1+yW+KVQIgl96c63AkT8WwXioDWxkVI2ytK4s3/V2+uN3Odux1ufMUhFawvk7ipeway8Dy15zEK7wEKe4hv2/Se8kuKfQY3Y+NAMrQPb3GWMFuY/JU3pY07hraqb8RJiyKJAnKD01jkwez26SX1SCVRTqWduFVYhyKzwWThndWBKc+iBv/hPJQfiezKGMxmzxOIrks1j7GUEfZ8pbFEZHR7LxP3LtUrhwxsfIgbbkUvdYbPOID0MFq28nJfYLOMA1vN94GRW1MPJ63dlcJBq8QrFxEBaJEJDfoy9jfHHGKDu7NhW8K2pPz/gq55nCrSYpfF7Jvy7dbHzkld7W7WG66paPULkFap51lOT55kvSV12oEtQuoyVvrG1Po9SbwcVwyxjUs87Di88ON2Y98BHeerW9PNsaXYVU6Azrd71izdmxfhbbMXYPOrQ3b063NJss3fWI1XdGYGyZSoiklu3g4HZRomocFhW9PpAwT1UDpfoiRvNOtzALbjFhrkzRoXjEVolAX97iVHiKTjHfVdepgA89vwZJWK3vcXKjrleGCEooyv8WWJYoh4vLsW5FluvW5O7hnf9c7HiLRzvFOkdPdVFcV3128vhjI9KK5SVQdxZG/MSYDNf6odPnduEpXallCq62EV3BfT2umvZ4EKUzzATQHHKXye+EO4Mk+lMdBnw7c9VrBpidotkUiRSn0xk473ZzxoPsySZXRFfegEeUjiDLzgTAI/XKmjlfZjnI9O7VZ0G4rdVXAVkdfL8gddP5rn6GaahSD+z6WNSvqhv6uIZjJl3d6y/p5VqCh1vF8C9OZVeA9WltJT5WlysXVmWxFJIWQXhtT8hDp1gV0Yo6Oe3SH1MYxu8grx/H73eWATUs6ulXn8315RRoP1UO+am1nKR5tyb32JapHWEtXzXJFZC2Un+o8KGEnza6eLYTL/rg+lLgtXW8OfPVHrAjjXF+JwaXmLKSiioi5LVXG4ibYvt0sX3EN2fc5WcwoYaIaQkPI6+AmBxXzC8LsPKJftipNbKVDiPHiuS4nmHPbI5ZiBWKvNz2sni85mnK8vnP2si6C4SDaFNN6dACMYTwMtaF3vZxtrcbjQJSJ9ZgDlOvUCJXQVmn9ykchjK5IO8E2Pq7KZmti2KkjFdFDTDSSTgGCqyOh7F0aFqZ6M9ypSJPDY4aItVPwdOW30XkqewuWmBSFg3LlnsNxO0gU3xnDmsgjT0in1L0E5+ukCX3djAG+vLBSkG7Xe9GjdGZt1LwvbSS0JsmGW+/97mjiXppjzqS3U3zUD5B5EEQcJ8I9VsS10qHwiYHqXVrSWXLjy1Nxd240NN2Jsb51eN73vkpYpuD7RzdkW+La0xYZwy0FGTA4qpiw3mzdGjIJGbsfdji02W5bPNthbdnLm3NvthsLM8IbvxVrMsEH5MxDfEGaU3G2ls7dDI6wdaY90h9qc6XbbXIxeMjW67McQ1PiJ1f97le5iMoiQAKZlt0W7cDwg8HUxjRypWH7ckCEdbLuKlPFJ3djsmv2uDzpKzYUZB8JVDEpHUjwDyOWDjzv5bBoM3KlGJuuIpRtrIXZnm1zUM6w9NqZ3AY+EjtSbuNDT/ow6tJnIx7ga14Uu+JMDyKFxVpnqQai33p6HLcdIubasOk8I+BuZVzpyOa4jZBLjF3kOyT26t2Dtl7kK/v6COPnXd8lmpLhXQ3GiBDLFbLoYkm1fCPTXPV4gZSYpLZwvffBbi1ar9/ev80PjF+Pff/Ky2fzA6H/Z8+eno+Qvr5L8ng0GDj+pwevT39Jqp/fv9VeAmR6PmVrsi56Paz6h2dsH/6NtwdmAuPzra6vT5mfj8lbJ5pfen5LCr9r2nr80pTZ430ScMLtmvktyWYWzgPff3zC+QdVnsvN/OrIl7b8cuvKx1pSzK+KBH7ifLuMXo8e37/5r/efvmDE6ktQV7O2rzcSgJLYR+Qj9vbb/wbzDahUvi4AAA== -->
