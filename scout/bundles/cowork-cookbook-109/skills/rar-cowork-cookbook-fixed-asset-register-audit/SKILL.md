---
name: "rar-cowork-cookbook-fixed-asset-register-audit"
description: "Audits a Dynamics 365 F&SCM fixed asset register and returns a workbook flagging assets missing service life or depreciation profile, fully depreciated but not retired, profile mismatched to asset group, or missing locat"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fixed_asset_register_audit", "rar_sha256": "f9ecdd88b07558ebe271f15843bc756526c004d6e4e181411812f3df200616fd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/fixed_asset_register_audit`. The original RAPP
agent is preserved byte-for-byte in `fixed_asset_register_audit_agent.py` and in the RCI capsule.

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

Fixed Asset Register Audit — Audits a Dynamics 365 F&SCM fixed asset register and returns a workbook flagging assets missing service life or depreciation profile, fully depreciated but not retired, profile mismatched to asset group, or missing locat

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
  Upstream entry : https://coworkcookbook.com/recipes/fixed-asset-register-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fixed_asset_register_audit_agent.py` and embedded as the fenced Python below (sha256 f9ecdd88b07558eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fixed_asset_register_audit_agent.py` first:

```bash
python3 fixed_asset_register_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fixed_asset_register_audit_agent.py   # or on stdin
python3 fixed_asset_register_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Fixed Asset Register Audit — Audits a Dynamics 365 F&SCM fixed asset register and returns a workbook flagging assets missing service life or depreciation profile, fully depreciated but not retired, profile mismatched to asset group, or missing locat

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
  Upstream entry : https://coworkcookbook.com/recipes/fixed-asset-register-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/fixed_asset_register_audit',
    "version": '3.0.3',
    "display_name": 'Fixed Asset Register Audit',
    "description": 'Audits a Dynamics 365 F&SCM fixed asset register and returns a workbook flagging assets missing service life or depreciation profile, fully depreciated but not retired, profile mismatched to asset group, or missing locat',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'fixed-asset-register-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/fixed-asset-register-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '38695a4c2fddf7ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/fixed-asset-register-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Fixed assets role', 'Output matches: Workbook of fixed-asset register findings.'], 'confidence': 1.0, 'deliverable': 'Workbook of fixed-asset register findings.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cleans up the asset register so depreciation, insurance, and property-tax reporting are all based on accurate data - not stale records.', 'expected_output': 'Workbook of fixed-asset register findings.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Fixed assets role'], 'prompt': 'Audit the fixed-asset register. Flag: assets missing service-life or depreciation profile, assets fully depreciated but not retired, assets with mismatched depreciation profile vs asset group, and assets with no location assigned. Output a workbook.', 'steps': ['Paste the prompt.', 'Update flagged records in D365 with the asset owner.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork ran all four audit queries in parallel and produced 'FA-audit-2026-05-23.xlsx' with: 24 assets missing service life or depreciation profile, 12 fully-depreciated-but-still-Open, 0 profile mismatches, 2 missing physical location (COMP-000007, VEHC-000007). Cowork added valuable context-aware commentary - 12 LAND rows correctly carry CalculateDepreciation=No (not a bug), and 12 MACH rows on CONSUM/T_CONSUM books are expected to have zero service life because they use consumption-based depreciation. No asset records were modified.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Surfaces fixed-asset data quality issues.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits a Dynamics 365 F&SCM fixed asset register and returns a workbook flagging assets missing service life or depreciation profile, fully depreciated but not retired, profile mismatched to asset group, or missing locat', 'example_request': 'Audit our fixed asset register and give me a workbook of the problem assets.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a fixed asset register data-quality or retirement audit in D365 F&SCM and needs the findings as a workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Update flagged records in D365 with the asset owner.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class FixedAssetRegisterAudit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FixedAssetRegisterAudit'
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
    print(FixedAssetRegisterAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
