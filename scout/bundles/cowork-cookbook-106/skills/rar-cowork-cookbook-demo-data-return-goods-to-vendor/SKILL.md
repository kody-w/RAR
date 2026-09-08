---
name: "rar-cowork-cookbook-demo-data-return-goods-to-vendor"
description: "Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_return_goods_to_vendor", "rar_sha256": "af359e3a003ca51a7018e370c52839cfb27eac116b289e5b83c9032e417fdf73", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_return_goods_to_vendor`. The original RAPP
agent is preserved byte-for-byte in `demo_data_return_goods_to_vendor_agent.py` and in the RCI capsule.

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

Return goods to vendor Demo Data Generator — Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
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
    "legal_entity": {
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 af359e3a003ca51a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_return_goods_to_vendor_agent.py` first:

```bash
python3 demo_data_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_return_goods_to_vendor_agent.py   # or on stdin
python3 demo_data_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Demo Data Generator — Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_return_goods_to_vendor',
    "version": '3.0.3',
    "display_name": 'Return goods to vendor Demo Data Generator',
    "description": "Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4723df33d826a25d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic return goods to vendor data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for return goods to vendor. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-return-goods-to-vendor-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic return goods to vendor records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.", 'example_request': 'Generate 25 return goods to vendor demo records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use to populate a D365 sandbox with organic-looking return goods to vendor demo data for training or pilot scenarios. Sandbox only, never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReturnGoodsToVendor(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReturnGoodsToVendor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916efObSJrmV9F6IraqBttc4vJERyySAAlxCBBCUrnDxX3fII6a/u6bSD+7XD3u6emI/WvlsCUg8833fJ43nfz+zu67qGzefXpn+HaxEuwsiyO/WdmFt9qWQ9mk4KtMHfB35ZZF18RO35VN++79O89v3SauurgswHTBL/zG7vx2hRGrxrezuO1iF/zq+qb4EJal137oyg8Pv/DKZuX5eQmeuWXjtau4WNmrFqzolONqh5PEiv/fxlZeZX5oZyu/6OJuWv3s+YHdZ93KNGT+l/ertrNDsFgX+flLgAcW91bc6PrZatF7Ufn9ygWqdG/j3j+temnUrnzbjd5U+KldVU2c2820Sv3pI7DNH+28yvz23adf//r+XQx+v/v0+zs3s1tw690OaL+zO1t/ihIW287l5WkZmJvZRQgGVRNwbAGuK78JyiYHt4AJq7ern1s/C96v/v3f08FuwvaXT5+L1dvn87vlj94Xi9KrrrTbxTDXrmwnzoArPq7YbLCn9pslwHkgLkX48TXzD0lltfrL8uzn1yIfQ7/7+fO7sloCBaL2+d0vKxCLz++afvn9cZFS/fzLx6wc/ObnX/6Q0/ZO4rvdIgxo/fHL2/WbWDDwj6FxsPpinLjt21rAv3HlA+Hf2bd8Xqq/iXtzyZfX4J/L6v3qx5IXe/4C9H1lngPk/lgs8AGY+e5jUsbFz29rNCVIPbtw/Z9/+Udi3ch30yVv/0dyf30JjnzbA956cwlIzCUEf11Bb7Z9k/mPl61AwvwrloDhX5f75qh/JPsZ2b8TncUFKIivsfyhuB9NgP6y+vUf2vbfTXi/Cj6DksniB8g7J/M/rX5/psivP3l/3Pzpr38Dov+pGKPsG/cp4UtuF3Hgt92XL7/+1D5v//TXX3/qK5DFvp1/6ZvsRzJ/5NfnOn/y4Nuon/88F6xvFmlRDsXqWw2tfi+r/9X87ePqAhDP++N++2n1fSUuH2i1GPF10ZcLvqvGFuj6nR9/efc3ADwFsKZ3n48Bfvzbv63k2G3Ktgy6leGWfbcCAe7i3F+UP0cxwNIn1AEDgF/bGDj2bRzI/yXCi8ZlsPrt/7hPbP/gvmE7vADyFwCh9peX7V+eiP2lK7+8EPu3j6szkFs2cRgXAJV19nT6XAAILrplzarxW795AJxyps7/AMr5w/JjQebf/pnoL08pH6vptyc+xy/c07eHBfPaPvM/LtZZkV+82eICovJH3+3BAlnpAm2CGGD1e2B1W2YPgJmLJ9o0zrKVFwNUAYQ1vbC/Lz4twn777TfHbqPPxQuk8dWLyVoYDPimzurDB2BWkMVh1H0ufDcqVz/9/refVv+5+u9mPYUva5wAV7zFAmgoGqqyArXV52DYQnkA1G3vGYvf//bmXCAGcOgKRC4O4hdnLTWQ+t5XTxt79gNGkCvHBx4G3s2rsukA8q/i7uPqEKy+6QsWXR4t3BCVbQf4tgK+9gt3AlJtYM43TxZlB7i3i9tger/qW/+56m9OYz9VzEGR291vK3l7AkxUZuCfRc3nIDC5LGLg/m958LoPhDSAUTdfRXxcKUs2riq7sauosd/WCOxXXAADfZ0OhNurwh8+Fwvj+ournqXxck+4dBigpXiF9MMSc9CS5AAHXj1E93XMsxE4P3mz+Vy0b2lvN/6T7oEq0yrsY28hg/94S6k2KvvMe/oPaLpIeouC9xaVZw6++H71zN/FE2/NzNIOrJZ+YPXWBC2k2mMIul79f9QVLQ5gBUHnBPbM7VacctZvr8AsfeESwFcruagFsvNVhH90LV+R6StAfy6yGGRZM/3Ha+QznG9jXqDXN0BzndWf8kEugcAscp+pvqRu0yxFYn8uvjIBsGT1hD0QbYALoG6WIH1dcHn6VdMIFP9y/UdX8Gbz4guQzquqdzIQp8D3Pcd2U6BVs5TrW1RB3vtL6Q5RDLz1vVVLXIC/gPwVUCIGBQjY4uM3dH49/ar6nya+mp9lyrMx7EG1Nk8BQA9/UXCJ0hB3ALTs7tWGAzs/PYUAM/KqW2x3QL0AS183/cav+7iNuwUbX371K4DLH5bvl6XLXX+sQIkAZ4FCqHrg3WfpLKiSg9YG6ADyElRSHhev5H1zwlOgnS84AHD2LX9eEp+33wzyn/W2cNTXiYshy5yF9lcBUB3cmb6Hi/OP0gTIy5cRz3X/PtO+rbbIXiCzBbAHVvz69NUffHxR/KuHWH2V++m/7HN+/te2Qk/SNv+cAJ9WUddV7ScYfhHtV579CAALfunaPjn3w0KMH36MB3+S+zL50+pf0+1PIt5q49MK/Yh8RJZH0ltuvX2AK7YfNrcP6+XpAnd/wClYvsxBci2BmwDJf+O+r0MAAYYNgCYw+MWF7UKhA2DtJ/iDKHwuvk/2pdgAtxThkpxt+R0IPJsAkPivoH3jKPCo6MDa3tIyhv6yS3uWRuu/+1T0Wfb+XQHS7p/uzhYWypd8bpcdHagc0H91sf+8esLD2C0//7y5VZ8/7OwjwHoARVn7fc69ccfCnd+VxstEYJoLVnj/xOF24Tpg4rL4UlZ2C/IUpOhiSjdVi+6vjdzS+j1h/ssL5v+rQsb3vPAnRgCI90L374nkzzTxH6u8Bz3B4lXnCR7eq8X8oR7f+tP/qoQFWoNlPa/8tLDk+zccAt9gTwFI5uv2AFj/tmF7bq2LHuyFf122Jks4nlOWH2AO+Po26dt/MDj+u7/+QK+XdV8Aexc/CJjS5w7IOoDRf+JUoOzXfP3DJxjxyw8t/0qXX1559fdLvDh1IdwFKp+Zuwx8v/I/hh9X/6y2P2AIRn5AiA/Y+uOYteMPNHgaCQAc0ODirz8C8Yc7yue2bVEWuK97/S/D7+9AetvL0m8J/tb3g+EA7z60S78DAwQAC4LrV62CZ//yjuBtfhvZoCMFAuwAJxgftxEEd20CtSkEpX2cQlwCo3HGDRyMAs0FipIORjM+4dC4yyA45q9RKvACCgfyXhX/ZWnq4kUngqEChGGwYI1iiAfiha09jyZp0iUoDLEZxyYcgrGdP6amceG9GfoybPHit83J4pA3e39/55BrMHK/bg/s67OFIdQhMcoxRAdqSL8ktI10NBRdsINzj7JYjBCtOIRD725UD4N3hyk0rbt0q9IQk/AbN9AsPe7m6CRnEIFqF8vWSozOZIZey0oYhrE9kKARdx+FCvY18jqclfulSGM0T22+FuXxfpGHRLuK+NGJIxVm5EuTu4krwfu2wWEohtNsi++Ri3o2ElKNE1akD1N5rpJDhazznIuOlyt7r3a9qB+KUYe4fH3eQVI6BcEpsh7wA6ehI3YgvPoUmfOxVibxZkTXILKu68dj7khGuKGCCUe1lOk9cdH0rbQhjwgNbRL5guYZ3SOwPknscTD7arytOVThfD7dkwNiTOvITSZbBdbhXOUxREirEkpSpzM60VBRkQeQGMGMU9Mo+wrPAQ5TNwLEW4RxVWK7tLpM7EvuIASQ25ZV7urSZNfNNh6Z4qbpdOtmIlSFNtji5bfDJtM2Obt37hOs5tIQaLdKVuKSoe0btz5Pp0GiYexUiZ0o8vEFZXk81atbfkAg1mhJzmvHiVGuYw8L4u5ByXTkJYwobsjHBPZYd+I6jWFtpeldeuAhl0wbrU3ssyJycaFlTeLqlXB+RLC2UW8CxrKKHt/gZrOVKEPqztQwnxoru6lumZ7vu9GOp1oUNeI8uFKahQl+GfeE5YQZZvqS3RoCMYy7YAvPZmMzyuFxwEb9dDcI+Ggd4zCp91ZHTPk04RxeppR32EHX4szeU8HKLvfI4qBkj97uhWjlM5Oe4o10v004Yotyltgn/TR3zHa9pwPhxjqoSSGX7e2OseEoFumZRvAI3mrYY9gdfUo+S/ttyWtol2kZ1rBHpNv5bNbj90uDGOl6iglJ1vLRanLnzlu+wUb+tFchux0uQhCrWzMYuOCYxFuBYMTTKDwGHkNC/yjd9qaYD2vxRGMHLu8gXDmvzzklyXGXIcJjx2kyPIeFRl1ug2XCUrM9z3oBa9QjRS3n6uaPcpjztYiFRLEO4eDmrwc8YAysOjGbneyfs5lRHi0vrZXM1lD9YJCeg22kyp58S0U5zr8bl9HTZCtIGk+j1oO1oSONPUrMYyPArA0sQzbUPUsRmhdm5p5OqVX717rbYJNbm43AxUZ1NEt6W1btVbuF3mCrhcH2hxM/JAlxiwU/JtqN4x4qNt9eKXriUri7KzmPAcYYZdR5cEyY4k0THB1UTgTxJmidMaaH6kbvj5Z4rrS42KGagQiHQuCGZIqvqa+npgVRPXD2LuJsIT+Il5C/XovrFAmCyjWHyakCMb0LQ74ZhuMsMUO5NVpQxoRe7fikmFuLag41t9kebyF32J024jxqNtJ49gPWEiNmMVMh9SCV7ykmVMRa7+VyGvRAoXbGteTdg9dtWn7UDvHVDWkX8u1W2yXotNlb1ClHDzNsPlKTiu6ZuC8o7cB3mb8VBXdXFnIXH+5yg/UC3ZWpDJWWc0jPmgu5lNw/KiSGYu2U2+U6gM7FVB4Itzj1+dCFYXKUrvTmBG0f0EXbNiOw687eaPh2hXgm70Kr20WGJXBrB2E3R2TIXekacvWZOfI3JENNMxrP1ZCMdnanMGN/z+UjTV822XanR2s4ER6EFBEVfXuUGSvWvZVRj/V6jdEeBKV3yzfHnTPschUV9YSUDjVlKSoNdSrpBSfI3g0gZX2tkwXR7AZvrDO2xPQopPDspBzFC3p0xXFfGZJdqIotbyblwKsVVt2EfhLRZE87/Bq6n9hDLt6c0+iWThpAaSQceVm/1LfJfHDwzstbvKEI8pi759rbbtJ4YFlZ7IPtOqcVDc8OQ2FShlmDiNCP2t7Km5GO6qN01FkwAolTPrRHnwHNhaplSX25sVL6aINKMZxtw1x9hNZ2dz0ebNKLUa+heLKzNI9HtlSn2RR53Uub2pFUHlWPNnaHH3uF9nOKRuVtno35MbiL7OlyuRwygbwyaooblE7u95u2aKvcphlc3nRSj1LHrSJauobD8x65KwPj6yIkMnscrvZnROkueG2YtDzP8Oi2obmZ4o1DF9lA0/Vpi+QHoUYt88aW3V4pIJh1NARDA4NiUXOiNZJUFKavq22csjziSB3rN1Gj15u6EpFdvTUENA5Nk4/uxDbByGM5lzK36e+txOKb6sj6QTgdU1+57T3pot5iXLqT2h4uHMWfnNASs2mt1NN6DropI4Sz5QkN80hkafaOlx0i4zc6KnmddeRLxss+0o4tHh4do3HbUadCbb4f8Fngg8k9HBhfEhhNViNXw+5mWfNoNGjhfu/5jDX4OM2HqqmGqpoM7dpE08tp1+AX0hr7jhmhkkHq9Iw9Ypw06sbQJ/ug8yodP45xwWoD71vNA9VK5Ri3wlHuZYZvLY2/aWnVHBRxO2e6O8Bwk1zoWDJKBdB30matdqxJPZsTWsjz0t8q8QOpt4l922sIotvNodQLgrxm9yg71BUotnydTKyhsfaFE8otkzRnvZzHdsu0h20+bjYceRXPyHYdXdSRl9iMsy4KOaPn40bdwvkm0TkpC8tB6SQD5ItHCMpO97KbNJ1otblV+ynrHpsbu41lgmyOyfbSZz0R3WLMutfXdWwyfsqfNpGIsaYO5+v7RVKgjDDaCVZkWsfwbSZqcR7ms5DamlM2PFuZCf2wojpvK6+EeT4XhFkozOR4AVOMhDOTnrROcHXPD6x/a5TakkdkQyNYe4tJO9X0/Yxbpk3FztUcHRAv/IQ6N4Y2xdJkmc2cGQNDOI3ns3cq9OkjK2RjkO8RSJb0AcWJFgrv8mktcqi2ds5XjRuR3lLYcr5XtdDd8622dbb3TSqWKnL0923GTgb6sOIhObPHUcdN4nzmoe3ZWzvyxjNlJ4OS6KyGB0Tt9xt97luTKrAh7Am5EOIrn6LiWnO50GhMN8v9wVW1eyrJhzLYcBSCcT6SXUXbLQpE2ybC4F0lO5Vt+IJzrmK466PloEShNyVJlVxwE43SEE5ECUuco+2TKUfOl6wZrq6C7WEYN4xNZ1k7HtvPx+Io1HZAqjili1RaquZIt1x2GbkMn7SA4D1X93Spv8wCfLJdzqwKJAId21ZLZRW1N0isoYc67TPuovG6L9Xm1jvDeDeXbL2JFAwvTqPtBv4Unae5blDGVpijtwUxXZuOx1zUnO22Jatjci8IwkO1EBnkvPagw4cU9sYWPimM7R75cabmHjG6i+WyGXFxJb7BCoeH0rHlHEA/B+FWHYRh3ScpaW6PlhvCdanjTE3ZUih0tOhZ5W3Mkl1pk6l30pF5h0qje4tY/aJV58KdfP0CwC7ZVc0ZHa/w1tvvEAgqnAlSi5TcPB4uOtJMNztqf5wPmY42/NmuS+Z+wy+oD133vB2EFS4giS6eE7bFDc1KDmeHzycj8GTLAHut+gy2BXtB0E7a6XZDCmHMb+mNJTM/3Qs1d+BFqcwPkzDMyrHVCiNyzr635bbOcX8T0ZwiueLB7PrboQ/Vgj8nWaSkKcV22foE7ZNc34oNP9zpTcpQUr1DHeNCS9FJY9cOOtyNBwkdjhygpHuNJiPoWdHzKEozDzHqtaHggno4J8liOqo6SjYdkoHfIOMp4InpNuhx5dI9Vm/tclPD/Y3YHO/smPbHg8Xt9yev3E1bAgAa6R7E7g5x4fW4bhIclQwfaHglAyruoc5tioiA+obB7GzL3WJNpWuRvZvCYxPdjI011PqFNRAovGXCNcVHrj00U3M9XLgqMSTCr2Jn7ik8F/co5D6uj5lqrqpytg55v77HmLKtDL9z0ArNWLkM7US17ZO96Qgbyy/4Oq1vu0BkohitafRwURIFquBM86oakN0+HUO0civPUvVjWyabECr5qSTulNk0ayPAh67nikyDKekwGLEMzXOvX3SJHpuANw+o0u+CUYZkbGQxbptiZqkRFGA5XtqaJAKhk75hduOwN1V0VEFpZLsyuTKcYGrxWTzP1LhPGADxfS1kdow18QZxCwFvEmht0vhWcekKvdChMqBnJidx22FqFo2uux0d16YidlNObXBKGPnweukY88pZkJlWjmDc0uawM9aWJMr6QfT06xFA1zrfjSjJ+BzYSdc11Pdt0D/QxMpNlT9XfKk1aZw1ituxantSK7RL7Vi8Uirlat7AS25Tx2fClWchtrFCaLkBQw6XwcJEeF2JiZxSVp6eJcE4RTYsOuE8XmoHIP/8KILLzabcueEfE6i2Qe5JUDvVyaRaf2vETIVsuZ3fyBtpG/LCrs1G3h6JUNT16dKPAwZahVRN8xgJ4t4t2W1lbwMdyzdq3fMoW2eOjenw6OhCAiCvRe5M7il2TXo5vK/g9Z5i9+wVDcTifogljGfqG8qiRu+XF1omFHt2ZUZnUUXUYM0l77ayUwrzwBANAp/3TOiYjLMvz32/D1WWyGvY2ffC2iU5pUL08eLxlbavmC3Y82INRwq4exkobCft9bF2vAkRIjhnJTVXMRKmonGHlYAVIexKQ5SMPvjkTkpok/QnA8lJ/rJF5iKpGUYPytNJzvbXOjl5e/NQtiB3PddLeVJfW7BX8nWf87V6E31cLe4PRFk70D53moGCTqkOlbIZCNc5jsf9zi1EMpa5g6jIw2ZCjgh7TW9xGRS2kh5OMYEfIYg2ary2SN0pHsj1RjbiiGEnqQp38cBU9vWCFa3l+EpJBLcgGgjJCvVTthZGXWAZhIb7LoDLGb7FpyQ5jnc4mApIoDfVcKdw/Qg9Ts7sWdzmyHFQm+6xvemfdMspXe4uXBldZPfMbtbX6+J8mzIyZk0j6upDRAm7NTfpXBT6qnxSxEKJJrRKzUa5qliFHT39tHM034uOk9hWG2ZbWlWQF6qkakQ/ihE5ULsU5n0jjh4XsSe4IUg7wQytEj8TDulTVFuO6Rz6cw5H3G7u0Px+YKE2MnzlkhRg187PMkQaj5zxQdeeyHcUHRFnV8yI1ZU4LiJBpZttFlxmphbG9cQB0uXEAwDJw35HMaie4fc6EKycTTAsaxrucpfnc2zw1y5vrL4jghwyFXNdDqICNr+dvkZbCvE7umjbNbHd7MnHXcbcPojp/lKuNYWJQZ8HaXFkiJC/Yxng/GuUWb1mbIqElyWqQUcWyaqq6iuOsvNzud1oJ8QU2y1BQqzy4PY2fbptL7BtVod1J6LMWh3FHe+oG6TJlWNRBGTpn+Y1SSeABGxBa2+TluAiLJ4ViiNmTU1wjsyd+KAFs5rMoJSdLay06l0TAbI+zusJcvmB8zKY78zCqm990WvtDFhzl+35sK/SG0lTWZedrlnRILI8MOG1R+mzBxG5DzkkyXYp8bBOiqdybDZGme+xQbPdeqSitlJ9fOyiraUX67YknH69p5H9tVHuNxdjeaKa1U7g52umnNoDMWDxgJd5ruZeZ9w38bTLzHsSE3aUgVrc8TOLbEyL2XU4kaM3NGQh+4S7Y5kNRHOwAXyO6B7TAzPf+pfiamMlbxHhbt51RHEwlWaNN1fU8S73UwvRHX4uTlfOveyDTpthv/CSDCcl4jTKw9Ungm1/Yx67ODw+IqHepdvAvUgBWnSMYDZugHS3K81a6CmQLrat5A2xS7BuzNP+Gh8sOAKURW3OImPcOmZ/yUikGhv02h0Q22uyogA14jnwzRVvUAcxvScw7p6eormDzlJIzaLGTZocZfczsaujAEDqztrd+HOdjyi6JyodVk/Z5tKwdbImRQVyzaPOzBJ9Gh45X5KhNkbwgd81NSy2RpRUcyXJtJz45BTjsxrdFapNQYulwbMtojMkNLdO8Q7Nw6/2iRMKVm/yaZDplQxaU+z4qGvaW/t9yGu4pbrxtd0ezqZ5kFqH5mQGiUgZ15i9XRmQwUnRyCiwf95SPIY66QXO+Q2JdNLVq7z0imVr1XzUHZfzc3Lcpv5eaTDUtl2DfDSO3t1Ix4Iuapx5h8lSET9P8klaB0qzux6UqtBrgYkIdaMWWDYXRaN6MyxeVUa3iPqQw1Os+nf+Zp1FQtiRNmRBgAjxE7FDmLLiU3hNsp5REQZXqVJz7tO28W7jzcsUKaXFmW5J7TaiIUbHyYWxIfScexTjnE9GNGsFDOsqTghX6jIhpx6/KRB2ArvD8+mcJ2Uop1fZqM/4IfRorS1YFTQ6AUw3BOKScn2Ej6TaRGc/dDuObLzE6RrUJNbnhuov1lw+YrMGje1+vEuMy4hUNxtX68ZoO/5RC2cqifN9XDiCbmMJO+oHqho6+6FAh8ALidaRMGlmCSXHb6qFUlRMJ7sNhYQGSH1hW8l3AcWLsh12jk2din5jRfO+ZDVhh+8PQWjGwxxzOnYMQMfQsrsOsU8KXdjMQ9ngJqvI89o4xKfgXNGJZR9bknIYTSJL+7xzkr15upUPlrlQl0fiHPuaim3ITSHbNy8KilUBRHV8QNLNJnAoOqTIoykE8FTuHHS8k/w8HfKB3px3KIEd8S5tey6uVdI20B7p58Dtk34zQ+oAulj4OHkkk1yazX0tM/FdmTpcYAJAqb3g29d1hWU3Eh9lETue9j24CEq69ScmMscrSlLMFVR5AG95NaXCNaLvwhBQD5zdqiGv2Vhc12UbSgj5IINzOJiWl1z9rhPZ84iCBqh2E3vXRt0FbDlddUeXXIqUlPrwNZUwLxRzKp0WwzgbrnD49kDvR2EPqbbv2p6Dc4/Z5bdEyEgboWZwaa1SWn/fcQIBiWuLjIVsr/Gm2gcnpu/vER24AUvQAsGu3dHPH3HNPbDcMKXN3baD4ZrJKkVFvnw6yBpjSKfMhtTNg5b6yhUPU7dlWfYv796/W47K3o5q/8evhi0nPP/PDppeZ0Jf3/x4nkX6tvfpudan/7lKf33/rnFjoNDrMK3N+vDt6OnvjtI+/LPDwGX29Hrb6usJ9OtEu7PD5RXkd3Hh9W3XTF/aMnu+9wFmOH27vLfYLq+2uuD7+8PUb0a8W94hBIssb1otNry9cfm8vbzT4Xux3flvl+Hb+SKYP4EAxW77BSeJL35TLba+vT0ATMQ/Ih+BF/8vHRWoAzwuAAA= -->
