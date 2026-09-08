---
name: "rar-cowork-cookbook-fixed-asset-register-audit"
description: "Audits a Dynamics 365 F&SCM fixed asset register and returns a workbook flagging assets missing service life or depreciation profile, fully depreciated but not retired, profile mismatched to asset group, or missing locat"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fixed_asset_register_audit", "rar_sha256": "f9ecdd88b07558ebe271f15843bc756526c004d6e4e181411812f3df200616fd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
