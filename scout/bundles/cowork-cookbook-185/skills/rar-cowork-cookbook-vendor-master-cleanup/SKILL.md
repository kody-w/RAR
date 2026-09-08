---
name: "rar-cowork-cookbook-vendor-master-cleanup"
description: "Scans the Dynamics 365 F&SCM vendor master and returns an Excel workbook with one sheet per issue category (missing tax id, payment terms, bank account; inactive vendors with open POs; likely duplicates). Read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_master_cleanup", "rar_sha256": "a345862996c03f70d4fd77df7cea09869a87124551854b016466a6f5c5d3a184", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_master_cleanup`. The original RAPP
agent is preserved byte-for-byte in `vendor_master_cleanup_agent.py` and in the RCI capsule.

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

Vendor Master Cleanup Report — Scans the Dynamics 365 F&SCM vendor master and returns an Excel workbook with one sheet per issue category (missing tax id, payment terms, bank account; inactive vendors with open POs; likely duplicates). Read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-master-cleanup
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_master_cleanup_agent.py` and embedded as the fenced Python below (sha256 a345862996c03f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_master_cleanup_agent.py` first:

```bash
python3 vendor_master_cleanup_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_master_cleanup_agent.py   # or on stdin
python3 vendor_master_cleanup_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Master Cleanup Report — Scans the Dynamics 365 F&SCM vendor master and returns an Excel workbook with one sheet per issue category (missing tax id, payment terms, bank account; inactive vendors with open POs; likely duplicates). Read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-master-cleanup
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_master_cleanup',
    "version": '3.0.3',
    "display_name": 'Vendor Master Cleanup Report',
    "description": 'Scans the Dynamics 365 F&SCM vendor master and returns an Excel workbook with one sheet per issue category (missing tax id, payment terms, bank account; inactive vendors with open POs; likely duplicates). Read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-master-cleanup',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-master-cleanup',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49f35294b69a2904',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-master-cleanup', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Accounts payable role', 'Output matches: Workbook with categorized vendor-master issues.'], 'confidence': 1.0, 'deliverable': 'Workbook with categorized vendor-master issues.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces duplicate payments and tax-reporting errors by tightening the vendor master before bad data propagates into invoicing and 1099s.', 'expected_output': 'Workbook with categorized vendor-master issues.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Accounts payable role'], 'prompt': "Read the vendor master. For each vendor: flag missing tax id, missing payment terms, missing default bank account, inactive vendors with open POs, and likely duplicates (fuzzy match on name + tax id + bank). Output an Excel workbook 'Vendor-cleanup-<YYYY-MM-DD>.xlsx' with one sheet per finding category. Do not delete or merge anything.", 'steps': ['Paste the prompt in Cowork.', 'Review the workbook; merge or update vendors directly in D365 as needed.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork queried 49 vendors via data_find_entities_sql, flagged 44 missing tax IDs, 48 missing default bank accounts, 0 missing payment terms, 0 inactive vendors with open POs, and 7 likely duplicate pairs (fuzzy name+tax+bank match). Produced 'Vendor-cleanup-2026-05-23.xlsx' with one sheet per finding category. No vendor records were modified.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Finds dirty vendor records and suggests a triage list.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scans the Dynamics 365 F&SCM vendor master and returns an Excel workbook with one sheet per issue category (missing tax id, payment terms, bank account; inactive vendors with open POs; likely duplicates). Read-only.', 'example_request': 'Run a vendor master cleanup report and give me the workbook of duplicate and incomplete vendors.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a vendor master data-quality review or cleanup plan before merging or updating vendors in D365. Requires Accounts payable role access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt in Cowork.', 'Review the workbook; merge or update vendors directly in D365 as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class VendorMasterCleanup(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorMasterCleanup'
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
    print(VendorMasterCleanup().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
