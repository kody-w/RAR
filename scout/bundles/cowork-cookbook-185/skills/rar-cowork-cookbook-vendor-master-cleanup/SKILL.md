---
name: "rar-cowork-cookbook-vendor-master-cleanup"
description: "Scans the Dynamics 365 F&SCM vendor master and returns an Excel workbook with one sheet per issue category (missing tax id, payment terms, bank account; inactive vendors with open POs; likely duplicates). Read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_master_cleanup", "rar_sha256": "a345862996c03f70d4fd77df7cea09869a87124551854b016466a6f5c5d3a184", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
