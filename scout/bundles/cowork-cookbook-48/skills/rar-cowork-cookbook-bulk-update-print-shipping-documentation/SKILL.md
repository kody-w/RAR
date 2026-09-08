---
name: "rar-cowork-cookbook-bulk-update-print-shipping-documentation"
description: "Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_print_shipping_documentation", "rar_sha256": "5579558dace49e1c60fa3c38a5ddcb391c6a65cf8f8101f243371205b89fb7fd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_print_shipping_documentation`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_print_shipping_documentation_agent.py` and in the RCI capsule.

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

Print shipping documentation Bulk Field Update — Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation
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
    "environment": {
      "description": "Target environment; sandbox only for this recipe.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity, default USMF.",
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
      "description": "List of print shipping documentation record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 5579558dace49e1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_print_shipping_documentation_agent.py` first:

```bash
python3 bulk_update_print_shipping_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_print_shipping_documentation_agent.py   # or on stdin
python3 bulk_update_print_shipping_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Print shipping documentation Bulk Field Update — Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_print_shipping_documentation',
    "version": '3.0.3',
    "display_name": 'Print shipping documentation Bulk Field Update',
    "description": 'Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-print-shipping-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6076267427244d2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/print-shipping-documentation'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-print-shipping-documentation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox only for this recipe.', 'legal_entity': 'Dynamics 365 legal entity, default USMF.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of print shipping documentation record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when print shipping documentation records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to print shipping documentation records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi', 'example_request': 'Bulk update these print shipping doc records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of print shipping documentation record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity, default USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox only for this recipe.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many print shipping documentation records at once and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePrintShippingDocumentation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePrintShippingDocumentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox only for this recipe.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity, default USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of print shipping documentation record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePrintShippingDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOiWNrmX3GeiZiqeslMFkEg3+iIQUBQNtnRyo4sVkH2TcWa/u9zUJ+srO7sd7on5tM8FRUqnHPv93XdJ+H3N38c0rp7+/xmxn61EPyiyNK4W/hVtGDra93l4KPOA/D/IqyrocuCcai7/u3DWxT3YZc1Q1ZXYDvTNEUW9wt/EYxFvkiyuIgWYxP5Q7wY6kXTZdWw6NOsabLqtIjqcCzjavDn3YsuDusu6hdZteCmyi+zsF8sV8Ri8z9MVln8XMQnv1iA1dkwLWxT2XxY9MC+oL79srhk/mJI43dbuXkbb+wXTTGesuozED2MXTWbFXXTx26sgCXxJYuvi3n97NaHReOPPbA8qYHbTdPVF7/4MAutwC7gc5IBZ+ObXzZF3L99/vWvH94y8P3t8+9vYeH34NLbGrhsP3zdz36aLze5770EQgq/OoHVzQRCPv9u4g4oLcGlKE4Wr18/93GRfFj8x3/kV7879b98/lItXn9f3ub/DODE7PJQ+/0QR4vQb/wgK0BwPi2Y4upP/Xde9yBj1enTc+cfkupm8Zf53s9PJZ9O8fDzl7camPCw9cvbLwsQjS9vIGDg+6dZSvPzL5+K+hp3P//yh5x+DM5xOMzCgNWfvr5+v8SChX8szZLFV3PPsy9dIOdZEwPh3/k3/z1Nf4l7heTrc/HPdfNh8WPJsz9/AfY+azIAcn8sFsQA7Hz7dK6z6ueXDpDwuPKrMP75l38mNkzjMC+yfviX5P76FJzGfgSi9QrJLx8e6fvrAnr59k3mP1fbgIL5dzwBy9/VfQvUP5P9yOzfiS6yCvTBey5/KO5HG6C/LH79p779Vxs+LJIvb1xcZBdQd0ERf178/iiRX3+K/rj401//BkT/H8WY9diFDwlfS7/Kkrgfvn799af+cfmnv/7609iAKo798uvYFT+S+aO4PvT8KYKvVT//eS/Qb1d5VV+rxbceWvxeN/+t+9unheMXWfTH9f7z4vtOnP+gxezEu9JnCL7rxh7Y+l0cf3n7G0CgCngzho/bAD/++39fKFnY1X2dDAszrMdhARI8ZGU8G2+lGQDX/oEaAP3irs9AYF/rQP3PGZ4trpPFb/8zfCDpx/CF+vAM51+fQP71geJf31H8659Q/LdPCwvIr7sMAC/Aa4PZ779U/gncn3UD2O3j7gLwKpiG+CNo64/zlxnzf/tXVXx9SPvUTL89+Cl74qDBbmcM7Mci/jR7687I/fQtBJQW3+JwBIqKOgRWJRkA8Q8gCn1dXACGzpHp86woFlEGUAZQ2/SQDaL3eRb222+/BX6ffqmeoL1cPDmvh8GCb+YsPn4E7iVFdkqHL1UcpvXip9//9tPify3+q10P4bOOPSCRV26AhTtTUxeg1x5uz5wIQN6PHrn5/W+vIAMxFSBpkMksmUl33gxqNY+j94ibIvMRI1aLIAaRBlEum7obZubNhk+LbbL4Zi9QOt+auSKt+2ERxU1cRXEVTkCqD9z5FsmqBgQO8tAn04cFYMyH1t+Czn+YWIKm94ffFgq7B8xUFzPpdy+mApvrKgPh/1YPz+tASPdTv1i/i/i0UOfqBITc+U3a+S8dif/My8zPr+1AuL+o4uuXaqbi+FuFPMMDFoHIhK+UfpxzDoi8BLjwHDKG9zX+zJ/Wg0e7L1X/agO/ix8jCTBlWpzGLJrJ4T9fJdWn9Qgmmzl+wNJZ0isL0Ssrjxrc/1fjzjwtLDaPAek5NCy+jBiC4ov/n2eoOSqMIBi8wFg8t+BVyzg8szWPlXNWn5PobN8s5dGZf4w27/D1juJfqiIDpddN//lc+cjxa80TGccOpMRgjId8UGAgW7PcR/3P9dx1j1B/qd7p4gMw9YGNIJoALEAzzUF/V/jh6cjD0hQgwvz7j9HhFf4ZOkCNL5oxKED9JXEcBX6YA6u6uYdfaQbNEM/9fE2zMP2TV3OCQM0B+QtgRAa6ElDKp28Q/rz7bvqfNj4npHnLY3ocQQt3DwHAjng2cAa1azYAJPOH5xQP/Pz8EALcKJth9j0AtVR+eF2Mu7gdsz4bZsB8xjVuAGh/nD+fns5X41sD+gYEC3RHM4LoPvppLtASzD/ABgApoL3KrALzAAjKKwgPgX45gwMA31eJPSU+Lr8cih9NOBPZ+8bZkXnPPBssEmA6uDJ9jyHWj8oEyCvnFQ+9f19p37TNsmcc7QEWAo3vd59DxKfnHPAcNBbvcj//wzHp53/vJPVgdvvPBfB5kQ5D03+G4Scbv5PxJ4Bi8NPW/kHMH5/o8PEBDR/foeHjn6DhT/Kfrn9e/Hs2/knEq0c+L9BPyCdkviW/auz1B0LCflwfPuLz3S+VEf+BtUB9XQKr5gROYBL4RozvSwA7njqAVWDxkyj7mV+vAEgezACy8aX6vujnpgPEU53mIu3r78DgMSGABngm7xuBgVvVAHRH83x5ij/Nx7LZ/D5++1yNRfHhDYBn/K+f6WauKucC7+cDIWglMLUNWfz49Y6E8/c/n5b5G0D6EPTG+5KFnwAZiyeuzs0z190/g9vZ6GFqZiuf57t5InyA0234R13a44tffFpwMQDCov++4l90NtP5d435DCwIaAjc+bCYg9DP9AsCO3s6N7Xf5w+4/6EtcXXJurqa4/SP9lhguImHxXdr/vOdiwDqFd/B/9PGH2p48NnXJ5/9o4o/MeD31Ad8iRN/LIYHB/5QMpgqvoKEjM8U/p3p8zQys/LP/S+PAgOLF4/F84V5KAEMPs1fYh9A+zOMP9Tybbj/RyUumKNmEVH9eR4pPrzwGXyCA9mHxbez1ezL87Q7a4irsXz7/Ot8rpur8rFl/gL2gI9vm779u00Qv/31B3Y9Tf6aRT/wXgb7Z976F+aQxZbrn+w5184PIvBQBegFkPRs9R/h+MOo+nHynI0CTgzPfyj5/Q30mg9k+q9uex1dwHKAxh/7eUSDAS4BheD3E0HAvf/rQ81LTp/6YJgGggiCpAmCivwwxukYDVdI4i/DJeUTURQGSxpc8VdEmFAJhSJoguHLJYliCBFQdBKQSQTkPfHo6zyPZrNts2EzZgNIi/+4DS5FL6eeTswR+3aGeoDL6dVdwQoHK0W83zLPPxaG0GCFkcG09qBuFR/6nCkaQ3KOXUye1K29olPtILAWF9/6zXXwbDaddgrmb7uSuq15hVli230pJI1KEQqiqFLYYPmwjG1FY3aeXN53xR0KieLWkBUdkbmUFZveOR6bRnIyVbpifZZzfOvsxh2xcaDdBumEPDlBGb4zswqmyBjOJGXIdnpvZIxLe7BMmh11sQkxMizBOxwbMXXYnabm5dX2N2lyzto7JG1IiNREvFh3m3AdiIy/ccZbEnodulKMNZ8jpkwra+vimJw0GJa48lzfw3OrrI4rOD/mYeCYk2Hm09TsMwmplzh5l058RXWYieKyINMy4mfmVLMdA1myahzXBTg/QRkf8aoi9AqPue0QkvGlmuC9VSDRxeKX4goal8SZJPAM8W79yQi27VmKjrUVIebZkwY25XlX3hjKHWZVTZqmur8VvVZt/IYXocRvxC61+8DgFImRrj6k3PaVoR2VPQjBfdcOkkdMznZ3r2QtiXf52bbToGCFCSqWxTqv7xbFtPetx5JLPr2cLkW4plz/Mijx0djmtWVmm9u64iioM/wb2x/1yT1Z6cY7senh7JQrc7fRCtOTaGcUyD69mVaAlxjDaO1tB3c3DUaXgzzS3EUOMcV3Cv/YMPnk1QRf2PpEQMVJN3Ydzhdhu5QjlqonBx8lkEZJVTh4lw0Ncu0PiHDMxb4J4WJq9MadhHVBTOVEYVuykTHIEPt6X+o3mWXLYWon1lahUncE03ZXbLY/Gbl5Ky6FsLuOmh5RMH86IYjYm7fBL2I4MnrjIKWdvuawTNsmtzqRJS7dOWchX6F4lWvFQcjOlp8OG59Fa12gjuo4rhp3G0mT2SJSb69u5fJ2bIpDaPZpkp3OlGQunVaM9cMmp135evCU/MybMFuhKUPZ7nW/DdT06keEolsqSQAOwxvUdYNNxG13sburiUuRjk1RG3W/O4Wbw5ViD4q77hWXC68M611UEnPEa5hO+Aa/EhalJ3CfUIeAxFG1dKDtljxTiZLcUDg7xjSAYjMEAQquqtysT5Ox7I5ZbzibUhp7mT1iE3c7dJ584vXgvCVPF1i4yh217mS+8Vdy7lod7nS1mhsm6NUtKSPLYIt1nnZg011+2p4os256z8x1Ad94XsvgNEEFDUrv02R/47G9OvIObnQCnmOb4qotb/1dW3MXzLjUdL6xsiChgu4I3RyD6Y7+ylHKuLhLqEmcsIJmkHSLrDJat3modmixzbMM3w9LlkRCVzg3mYTmCiLB1Li+CcTRvZ8HelT7pYJfTqi7xo4RDerN6QSElGkJR7Lagm3H2Qq1vfbMIL2k8v1u5KsuRqmx7MyUkXSxB2tVYidokwZjob5ZC21KeFNhxxhnZ1saJwjO9OLIT4ToyJ430FoUllrpaHe4Uhx7Y4YF0k4AU91y6tb8fWR0a/JuzrUksXLf042i1PkhP+hXrurGxFbdPZrzqd6i0rIpVwK8Ke8AS2Ipyjzybiq8PC3jqySn53vlIyKxO+1z+FjFQpgOJ2HgspOm8qslxgtOmu3xQ5Vu7JMoDQdkQ7gsFoJ+Rq+DSVO4vO9XpRpqHY+lt1ShEmLwws4gGyrZO76+QT0ugy84vsIPAwvVBze2b1xw5S40CtqCvDMdwVA3XFo1KE8WMHnAVJG4b7VjxeshE93SYlO7UY4jeyH22fPJwqMyZyW9zUsnsXofYpcko6l30VcH5OR0moW79yVoC15XssrVfZjZ1yeG4Fgbv+bFNT03g8kqWI9GVbDEIrapFfMUbC+dQUG1tzshwYBuE7M6yM0gSpFW7n2XPvA7ZHfY8YrNKmW6FthREQuR3w1oRUlYPmVufHKYgbJGdCo3/Vk+oD2Zxwizk25grtbgOtl6Tnv1uvHEQZ1+p6wDHgzn9fGmFZk+VDqhjnec3nubVcjv5Uqxx8litNFq1wC+Lpm+G4vyjEiiHMr4qc4jEqbtq9qMojXUh1N/RDfx/gKT7eRESQJX+WoCnykADKMllUajhG5NEHVsyvpZXw+5ua7ZYINsQpPfHQZnavttuz6rKq1tV2kz1BABrVupwM9GGAeW7l4Y8WoSS/Q8KmuYK1V+MuWloJzo3Wi5yIFnb9ZtX4cxxGXXUt7e5Ui4c9f+ejQzscb5tJYP/OZ8jAlHGlDt4BdnpafMbd3fA29vjQSyWudd2d6GYFR3Fzwn4Qjbhs1oLO952p38tcyePbeqoz2Hh17OGKGHxp6U402+TGheqZVoiWjWtNu3JnbYlGFySotOcXLCQwnkSrO7XJtShCwzDjY8NkzLS0yinkLyVZ9bGikYDCPTqHA42cdEQC5bl+g4JxxbXN0QPTsNVgK5/k3OI9aZSn5pOHHsMNHOPMrolkikTNyGV2OL8Hs0rpP27Ar+5jDIm7utC9i278R6h7JWZdu3GEa1LN3IfC/L0wDobwNi503bLZ1sp9A9TlutzYxQWHa6XXdM0eaHKdltXNtuN4YWKPmSN/TsxMBcLQ2OjUZJpwoH/gSrGWNrO+ZATDSKOZfjej15eaVbeodB05Hvah1eR2fpVmebFaG6ElzczOooIQ6HYN6u9JPCCdStG+2Gjg45xKz2gETSLtNCi/drziulmF/tz2O6sygJ4Vk6bhzemeiogczthm3gUtProml1pz/2187m2zzvb9VKC42EvyKKjR31+tzbvL5dKj7ZByZ3Xd58XW+5pL3D9E67MRzJHy/mrVS4ScLXSiqR0Kl2UCvy/ECPPIQ+XEWF3qtJQPeuobD8mTkXgTPAgb46c1jJwJVU84V28AJktZfvCL3c9XR63A44pCB6UDkeoxgDRQ/cukWtTLUOTGRHV/O45sU25dlkXzb2BOjcZWn7XDOolIOAlZjbKxW5Bwg0dRGUs2o6yGlxPRdhIavbs99cqh0DkWZTngAjukw0kamjX3X+UN+3TUrx1sX0DbKvBXeKq7N7pqJ7I+sMr1h101ysygpWVcDxp5blW153JH8/ZQKyxqljC07fjS2PAszCF3i8Cev2oMuToYU5KH2E7ga+Gs0TYal42KJ8a5G7NZ0HRriP7AoZS5hEq7WoH2nJVVZ63vCJip2aba6a0pnZNB7b3JJg1LUM5+OAM5TQdDPZTJArVce56qCVe2bYmssrc2cmRx67D3Zs7S67lj/5A31TjCV/OZ+N2O8CDZFGp9hsvDBbDb7XiaPJbAHQ8akRHPY4MemFslF1i8XrTi5vhOQYpZRTVp7mA00cuVPFxvvOQQeXu7TdmJUnt7wGLs4eVL4RxCxoeWh7YuQc8MItJO78MqdT/NpOhqDY25hcqwxiTBK1uUy+mK1jXTqemJTu6fquQpm/vvKJ7SD3yoUyWdz3c1RuUSHXu+yym9rwEETYQQ0vxSXwDaMW97uC9Qjqeu68O7I/2ftuW+vHar3Z2xeI2aIecmhX2Qnwg7SSJGin75w1xnhBuh3GVC7CBF1Hu53kYawIJrJUxtYRFvGl5nq72EiNWr0xQbd2ErzfcfqOvCROe0uF8Ya7GNH0lXAoS228xOdkJSGYnCpyhBwLuhSqVJA3iSmXy1qb+hsAnI1FXTp2XDpntTTiftwgPV00nsS6ajYhIOUXNRSsHub2q2OH4+Z0YnKVZcOs06CC4XFDZATROOMTq3Fodg6dpdbAR9nZ8CI8rTNer2+dVsbaITdW7mY46+r5cFO4001LedTPLAsgiM1xQnRzBQiM1AR03NE7Kd2jkoptUCe4prqqRFpU16bPCvZF5JCk6no6vDQTkdleVpltr1d7XxFgBju0codz6CAIB52i812qS+MpyP0jflnJtZYIl4vuWPg9lBJIOkSqsxoO4VkDwDWo7e3WuLwYcVZwVwljrSaTnPfNEqpHOIvIpuOK0+7o6kJPrdBrm/rW4CkYwi6PJM5arsadcl21NRGVOWKlbu6dgQ9HdHuuXFBxMBPV5ujkhyL0Dudsv+z4oFib6YrgT0kYx1ZC+DI02l1G3OvjpULVtcKHgrCyfVqhC32bNVucPucyJZZrvT3Sp9OaXqeH0vLkKohiFfPUEC0TNT+4xH6whXsqenYAbZrrwEsgxs5UCUdHSYjzZUkM23GnLqGioWG4imnQHCFfZpAbbjdG23gCucRwg7JVjFQBHWOaH/n9FPhb6TjVvGCft8IUbDAt6eCz3g80s4mQy6q6iQcpKhjWtcxo1/chX8XuaFn9jSVPu70TscurrZfmNiq2/bkl4May785uiVDMiHc0Y5ej11b7wkW2Wi0LikZjup3xq2nLqchlOGstCWbwrG4DJZEUhi+TDh+KQ3AX1py5P5wSREdLNRBRRoyYM3tEbOuCjCvxGunSad3RaHnaOWCu1RtibE+lS4mGZxnn7SHgqOSmE+CIK/kX3qJ6lBDZSbHi06oVnTwoZflUKuJ0Dtprk7nsYS2JyHmiYneDJO2uha1119JZCUY5AheUYMCUVeuLWmx7I6JFzuWiENA+vLcrBcGdm3bn6BTmPPK2bO/0FRnPCWbKaXxQDWppdXp0gCKZ6C9HCDue7X2I5lbleT04FKjIcrWrxe3FIVfFTs+SUHIvRwHC9gARDKK1oY17s9GAErZqWZ5jcuoZ+MKOEL324EHvJq7EjgPc90zSh1OXyHS/AsgDF0KaUPJtaLUmbmNriKQ9ylnc0swivhUP/j7KjYsJEUIN3SdEopeFomOmf9Ea0d9qm3Sgs4LCL25+iehLehiP2/24O9NoEwcODTSSIyWdWUoR9QBho7TBS+eEks1ZhM8kDHMBncmxplgbAoZ9GI8OXGSwnhV00CodQofrWStHlzs5dmmGghTDX9ahsZPFpZFeCdi0tk7cIu4lh3ZVJGyu9bYiBQ5nJlNcp3GoJtGuUtMT1rRlUZ2ryCaFcb23Am8c0i0mDbYXrWuvSdJKE7UDyd52KXSlzwVsFrvbAR2vQQImlsnltkZbQ+e9V12ixg2rMGbjZShjcdQOE7FegynSvLV9GIfhPbSqLu9wQlDXketSWHAYwYkJJXdlHZH2qKEFwHePjuA4HSCFQUtb50zGB8M1TsHqIRhKt7rdh2w73Bq/RTmXE9GdXbhAANrVmHuEBxaNtZ49TXTVKdE+kAiRXEokKSjG9Qh1QrS/AIqkqbHYUboa9YaUt3pmubI71x93REUDtUfdX585VbUGcoXX+t1HNt7qfDKsNbq7Y+f62vTsTm3XKqyIR0UM2AHWkB1DDMcbhWuw5DRJLPQ5wa2GImmpeF/d77fEoeGtuI4lYdVKAZnUSQJIFsXF0GrFsU7XsBrslbvf9DI1XoliiyqkdPfOMomd8y2eQUl73XebKRLD5jhuS1XcaqKRWFtyebxzngQ1neud/DC9s5dj2jRBDqt0j6EoYe0sV42XFBqwHi+QaM/dN3Z6WY9Yqjouruzv2BDwjRdT443TUvxsuaVGXhHmSpBuyXnH6pDYPLHMejA3a6rcn2HpYAsHP2SwUagp8H8UXjTqHjIp5+wrK4qhrhfWRwYez3AhNbm9Vo5cdVlqSgu1yso0RfyKHo0Y1wOMUfex5+252yUuVZ+qLGhoyB67a1ByjKk4OxrwCkpIWx3DeBkZ5l2cbjRKMYl4W1vWFhohtrvAzRUyiwrOMRqlk8Ntv/SuPabGiBjZl27JWG1EqwD2hIIJocodmZNLcRd2w9YbXeqvNK1FGmRGTufuBdFdEc3dke71ijxnpXjPPboYPJKBSzs5mIgSivFxXGPsugAZ0raqvVtB2Na/Jut2r1cqVEOqtMfvVC+ft2v05O22l3OZmntFuln4liDiuMm3h2RaW75U3fubJGiVlpuTQ93We74P753LmdAOp3B+jysZhUd5DkmWF+9IsY1wAJ6yqKnTGNiYsJ1grBzB2KSSEJaKOodykdmMbKjbQ7juu369p02IDLkD7LG5QRSylhpQstcuu0ElkeBgQK6j4eFmi9FpVFZYTsb26RgRLR8T2iHQ7QAjIgyp7/fRVQvrONzVwypBMMVOa8Gn75zCJxgRCEdV94ndWQmjDFNE9d4p5VKzJxhHs9VxdUdb/e7AOQqPVhcZApdP2vEMaV1xUWBR5SaTrtztreFolRGdFpggVWW+s8k4diu2DaTYVWuvInZIeruXy4gQxU64Ue3SbsBpZh+tOIVNlpxwQyJrLwxeSkwBTV9O2yVcnqX7xee57bDnK95YyUuZ2ZG6UsmaAcExTIurEyiYdhMJ6N0Y9NGdwm68DRiKtZFB4ODAI5NUFhJSb55XcEtEbZVV4CAbwrDYcgeFbBCRiqjkwPUc05NG7YOhjCTBiaeEFWcYKKzfkCJxskuSzEXZp0ksPp5Pw2TuOPvKpWFpn30CPULZWh2iwlqy3fV2Rk7b9Troyr3OGgeSYLZLeU+OV5tJMVypRgw02bI8W6tGKA0q6r3KnjAoLfaqG10G7STStiqnQ3puxd4TT3FNS8tbbHjIkvKdZd8N8eD3q6U+OjSUXUJHPO8LGMrIirHdBMZqNijuyGpzn7bllVpbnEogEjnk7chnrbbyTXRExutS86xlMa1dJMYJWJqOoGGcbi3iQccssdUyBEK6ljKOZr/EYaIVhrASLVbGwBwYC2WgadRFE2gCOUDUClsHoDR3dKVwYnU88IzDklS10filvjH2a3uDbKBqQ1qrUOCyew3mhKbZmrF2pVb2HbH0Yy63jSTR6TUpGKTMBQIhJ2MpZXBQR1ZUltdsuaJpVKZ9cFYgs3J5ETqXuO2oJafHtmaeou6igBUaLpU6vR7VMtpoddak+TqyKruClp6qQ/IFpo6Qqp8jiKmtCwVx1dLYFfZU3caCCqsU53lve/Ch9NCsBjfx/UNMJ9et6jEAPHOdYZi//OXtw9v8KPv1QPrffktufpr0/+zB1fP50/v7Lo8njbEffX7o+vzvm/bXD29dmAHDng/r+mI8vR53/d2juo//6msOs5Tp+SLa+5Pw5/P8wT/Nr22/ZVU09kM3fe3rYnztCMZ+fsWzn98CDsHn949Ov3PqbX7hErg+v4b2dai/vl5PfVye322Jo+x91RCfund7otdj6K/LFfE17prZ69fbE8DZ5Sfk0/Ltb/8b4gy/coMvAAA= -->
