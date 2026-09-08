---
name: "rar-cowork-cookbook-configure-manage-signatures-and-signing-limits"
description: "Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_signatures_and_signing_limits", "rar_sha256": "610230f52d7d53f274365efefcb80fe7814af9626334129d4527a6f53b3b0823", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_signatures_and_signing_limits`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_signatures_and_signing_limits_agent.py` and in the RCI capsule.

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

Manage signatures and signing limits Configuration Bulk Setup — Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits
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
    "config_excel_file": {
      "description": "Attached Excel file with one row per signature/signing-limit target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 610230f52d7d53f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_signatures_and_signing_limits_agent.py` first:

```bash
python3 configure_manage_signatures_and_signing_limits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_signatures_and_signing_limits_agent.py   # or on stdin
python3 configure_manage_signatures_and_signing_limits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage signatures and signing limits Configuration Bulk Setup — Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_signatures_and_signing_limits',
    "version": '3.0.3',
    "display_name": 'Manage signatures and signing limits Configuration Bulk Setup',
    "description": 'Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-signatures-and-signing-limits',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2938a21af65a0464',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-signatures-and-signing-limits'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-signatures-and-signing-limits', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'config_excel_file': 'Attached Excel file with one row per signature/signing-limit target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage signatures and signing limits, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage signatures and signing limits target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef', 'example_request': 'Run the bulk signing limit config update in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per signature/signing-limit target and the new field values.', 'name': 'config_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update many signature/signing-limit records at once in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageSignaturesAndSigningLimits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSignaturesAndSigningLimits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'config_excel_file': {'description': 'Attached Excel file with one row per signature/signing-limit target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageSignaturesAndSigningLimits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916d7Pb1pLnV+HeqVrbQ+kiB+rVq1oEEkwIRCCC5ZKRcyACScD7vvsekPdK8rPfzHh2/1qqJBLAOZ371906+O3FHfqkbl8+vWihWy0EtyjSJGwXbhUsuPpWtzn4qnMP/F34ddW3qTf0ddu9fHgJws5v06ZP6wpsZ4ci/+g2TZGG3aJL48rthzZ80Jmv0ir+WKRl2s9UojQeWnfeuPATt4rBjrRa8GPllqnfLTCSWGz+p8aJi6itS0Bi4fa96ydhsFjf/bBYRGkRflpc3SIN3B5sDq9hOy7a+vZhEQIW3cJ9fzizmJWY5f+wuLnzw6huF2M9AB2bpq3Bwg+LPgmrxbvw7yLd0j4BlLwwAsqGd7dsirB7+fTzLx9eUvD75dNvL37hduDWC/emUyi6lRuH2rv6HVMF2lP746z8bLYCUAdbmhHYvQLXTdgCiUpwKwijxdvVj11YRB8W//7v+c1t4+6nT5+rxdvn88v8Rx2qWepFX7tdDwzju43rpUXaj68Lpri5Y7doQyBCNRujA26r4tfnzm+U6mbx9/nZj08mr3HY//j5pQYiPAz3+eWnBTDV55d2mH+/zlSaH396Lepb2P740zc63eBlod/PxIDUr1/ert/IgoXflqbR4oumrLk3Xm3op00IiH+n3/x5iv5G7s0kX56Lf6ybD4s/pzzr83cg7zMwPUD3z8kCG4CdL69ZnVY/vvEAgRBWbuWHP/70r8iCAPTzIu36/xLdn5+Ek9ANgLXeTPLTh4f7flks33T7SvNfs21AwPwVTcDyd3ZfDfWvaD88+0+ki7QCwf/uyz8l92cbln9f/PwvdfuPNnxYRJ9f+LBIQRK73pzYvz1C5Ocfgm83f/jlH4D0f0pGA2ntPyh8Kd0qjcKu//Ll5x+6x+0ffvn5h6EBURy65ZehLf6M5p/Z9cHndxZ8W/Xj7/cC/kaVV/WtWnzNocVvdfM/2n+8Ls4zHn27331afJ+J82e5mJV4Z/o0wXfZ2AFZv7PjTy//ADBUAW0G//EY4Me//dtCTP227uqoX2h+PfQL4OA+LcNZeD1JAcx2D9RoZ8TsUmDYt3Ug/mcPzxLX0eLX/+U/oP+j/wb90Dtoh7NdAcJ9+Yrw3RcA8V/eIP7LA+K7X18XOuBSt2mcVm6xUBlF+Txvq/pZggbsCtsrQC1v7MOPILk/zj/mGvDrX2P05UHztRl/fRSa9ImJKreb8bAbivB11tyc0f2ppw+KSXgP/QGwK2rffdaS7gOwSFcXV4Cns5W6PC2KRZACxAG1bnzQBpb8NBP79ddfPbdLPldPAMcWzyLYQWDBV3EWHz8CJaMijZP+cxX6Sb344bd//LD434v/aNeD+MxDAVXlzU9Awr0mSwuQd0MJls2VEgC+Gzz89Ns/3kwNyFSgagOvptFcw+bNIG7zMHi3u7ZlPqIEOZezGtRlUMHqtgeWXKT962IXLb7KC5jOj+a6kdRdvwjCJqyCsPJHQNUF6ny1ZFX3iw4EZxeNHxZDFz64/uq17kPEEgCA2/+6EDkFVKm6AP/MYj4Wgc11lQLzf42K531ApP2hW7DvJF4X0hypi8Zt3SZp3Tcekfv0C6hO79sBcXdRhbfP1Vybw9lUj7R5mgcsApbx31z6cfY56ENKEGJB9877scada6n+qKnt56p7Swm3nV3h1482Ix5AYwEKxd/eQqpL6qEIHvYDks6U3rwQvHnlEYPPxuBbY9R93xktntG84H7XGs0d1UIDUNMsPg8ojOCL/597rNlIjCCoa4HR1/xiLemq/XTe3HbOTn52qqDDeVB/JOq3rucd2d4B/nNVpCAS2/Fvz5UPl7+teYImsFwAkEl90AfxBpw3032kwxzebTsL6n6u3ivJh1nlGTaBvgA7QG7NIf3OcH76LmkCAGK+/tZVPMKnDWZXgZBfNINXgHCMwjDwXD8HUrVzSr+5GeRGOKf3LUn95HdaLQB14AVAfwGEmA0Nqs3rV3R/Pn0X/Xcbn83TvOXRWA4go9sHASBHOAs4B9HsDSBe/+zygZ6fHkSAGmXTz7p7wNvlh7ebYRtehrRL+xk/n3YNG4DkH+fvp6bz3fDegDQCxgLJ0gzAuo/0mqO+BK0RkAEgDMi2Mq1AqwCM8maEB0G3nLECYPFbL/uk+Lj9ptAzLOca975xVmTeM7cN78E9fg8p+p+FCaBXzisefP850r5ym2nPsNoBaAQc358++4vXZ4vw7EEW73Q//WGM+vGvTVqPom/8PgA+LZK+b7pPEPQs1O91+hWAGvSUtftWsz8+S+nHb+DzETD9+DvI6H7H5WmAT4u/JunvSLxlyqcF8gq/wvOj41ukvX2AYbiPrP0Rn59+rtTwGwAD9nUJQm124wiahK/V8n0JKJlxG8bz4mf17OaiewMI8ygXwCefq+9Df069N8j5ALz1HSQ82gaQBk8Xfq1q4FHVA97B3IDG4es8t83id+HLp2ooig8vAEfDvzj5zVWsnGO9m2dHkFWgt+vT8HH1jpPz798P1vYMoyCJAH+QK3H90Z1nioUbAUJzI5eGtzmZHoXnzwD5reC/I+5cy54oHMxa9WMzq/GcEOee8hk1X8K5CHyZTfRHiZg/VoonkM+4BSrEPMR+K0/Q70tTDzqZsH/YfRYZlGxAIAQFFAg/hN2/kqkP7/0fJZEfP9zidcGHAMOL7vtkfSvMc2PyHaY8owFEgQ/M/2HxLG4gj4EWs2dmPHK7/FHB/lSWAoRd8QVEB4CHPwrEz3X1sWTxXPLe9bjxA38WP4av8evC0MTNT397iAamc2ALr74DCdqu/1OeX4eAPzI0QY818wjqTzOfD29gDb7B4PZh8XUGA5q+TcUzh7AaypdPP8/z3xyXjy3zD7AHfH3d9PU/ebzw5Zc/yAUEe1QAUEdnWt+E/La0fsyNswqAdP/8b47fXkAOuMDu7lsWvA0eYDkAzI/d3FRBADQAc3D9TG/w7P9yJHmj1iUuaIIBORKBUQyOCDSgAgKLUAoHngMdXOR7NByFFI3gbrQiURLDcARdBTiBUi4ZEZiHeTCNYoDeEzK+zH1kOks4izfHOUCd8NtjcCt4U+2pymy3rxPQI/WfGv724pE4WLnFux3z/HDQEgE3KU/ee0uKjGJ3xyGVty1WrElNpadqrqGxcprHZAtLbI0k+f7YH+DBtI5tXjfqQWBCuyFuVaktfTg5FNzdOgcHD2sqlo23h6LL+BumEFNtwgRW8ufpcHZH8xDusUPXNeedeXLpwMctu8uxzil2BjkGrHm9IKPpO+6hQc7jwSfOZoitMQgiJQgnC68P1qU06r5fiKgx7sq7yun+aJmSUO2aaomoA04xJwvDqMzKltulX7X06TJRdrwzVWesuGxXbcndWduborkv6ysm1nlmmocxvEDj1U+nC16cpkMJH9FyfxlHyBI8hzBUX7MuxFgd7hPZ+LHU0Tea2x94/7JxHGJc7c+WQDCuW5gxLeibEZL1gqZD60rq+3EZVVe0G6HQS9S+OavNwVTPXrujj9dAHFbTesftMT/JqxUzRafNyhjIo1gENzmvUmfEJkhjlvk1iBNhw232R2dX8TBhQ7tRLyzZkRVtM9KJ0lTV/WD4nmC4LaKqeplSh3RVt3BuWuUeLQPrCJ+vRwK2TQFqZBRxG30tFn5yLkNDvQgDS/TGlBqH0Ugbe7wyqlKz3D3sxQ6Yy0vdXtoKhLu8CzEvl3wfM/xe5rvD1djGVAjLECbT/egmjZVV7m5/KApJ3Z+FwxA19nqtuuiJbHYi2++h7YhfDNn0XXy7pA5opWtkgsvTWjm7xLINd2mSF2LGT8BGra8D1T1iHV5imto49sko3PNwa7jIue7r9DRh9GW3ZAX1UJjLLBDtDFZCRZV1E038fZzjCU5pdsFA0vmqOnEqbNZ0CpUlba2P/L05YniZy4V9SFrdTdrCZJDGFuj9PhjIxtr1+321wU27kRIpGtB4Y265dmfhzQ3i8h7hB79QaC7K9gibifh5K3eb5a7D1vxdpRg86dAt62D5ne3gCL1fohRGHKpuCY/1xrvEizQtdfJKFjeZ0lLmhXTs1JESZro7rb7JbINK9ySNKXffGsnN7q5PomFBuQLtAoL2xukI7aSTfnGUiCCWmRPyInU2ff68L2qh6Ea4SykN29DD6iDuaKyxNhOD74ntJbhMhnTPw10NsVgIxYJVSircWUxvKaO4Ey/rMdv71uTyfUkjySTuDXRa15wTc66ZlYeTCcvZNmPJNaObhC0xCutZzOqyPt8Yu18dPG6kt3GOOpVaoNQag0Ocu9z6axIgzdEgh1LNTPacY6cLZzMWvlF1lz2Lk55nG26PF/6JRCI0VE/WAOsDQ119D69r6SwUe5M2oW0oi5Z3RId7099X1XLrLA+Bv3EKWsQn7WLvjlQtxtq9oxKVGa2zLTBGcmIHpr0XBNFIh7PSG9Zpcy8abqMShuCwfanwzT24a1fQfPYZcQUFv7ks1bW1ZtYn/4LdYCtpxRO+CpzrJVzJlnSZqmW/F61jvbudqTt96y6IphzXvCBRe7mwyKp18csByZs7s4ITTmtABQiWp31HGh1ecFSDhgJUCDTIhOi4Ip2BTdaiparXWpFrR6ULXKZuKLPZY9T6GJNbydfQWjSTe11loS1mprAmE6PcFCPT47CuWxvnvi6EOlP2+DlqhTSooJt3R90S3ku+Fy+DgTYapaxUPLrv1+ZZHO4JHmXtRkL5Q1I5e6OSFMZ0tn5lRvlaPR96SesiBgpXjUyVuCSl2nKV8k1zz7fM1lcJzT1Wjixtp6rM1hcqUTQ4zjUZzZHLOuCtu3XCeaS0qVzKTJ5wRj89+BA33lK1OwtCMeq5oZU1KqSarQhyW+12mUucRyhaZk0ibUuTaTjnLGzsUrg3cI6eDlyl1dK0T+ULTZass6ZuBp0Puc6e6tEr1lZT0Ky2l6bjRbHloClAEvGYvMFMeuQqs8CkUCasnuG5znW3VO1uSQlxu8KlbszmgEvrjpDNxL6bo+f4uU3Ay4kqxhDUkJXC2erY+8NNJ3mpQYClLxadHyxnBUAyg42U61JnG0KQETN7736jXFkUhUCzIMg6R3R9vRJc61FLlaeg5arsszPqamdUBOh+P3WxwRIp691i6UYjtzLRDnB2Dlv5cNNqWafX+1q/HEp0urH+5J/bPfBxRyIHruxYX8fhpO5PDB/K7lmT8EKOl3uQPIx/SJOCrXJBOeH1XbdHu+gr416nG5HwODgSEnE54CHAz2Y65MBc2PmcqEQ2UAXaXU35nAe4IImdROwJ0lktz0sVoir1CLv81h0xiWujwoY2JcIMO45J6Q7XjHiN0OJJ7lD0hBO+HcfJscjHSljV9bm6W8hNcfyYLc4ndnMydrq6Ta0uZ/PWuQ2UM+yHA6MezUxf2zpjNPSWMXJp0x+Yfh9fVrsLs1M7Bd8wtVGjpH4/Mqm6QbTgbvgZdriwSkAjga04JxODdhfDZiiubOM8qvzi7O4hOCvQ/c4CsGhC2rknz+ttjcPWNCo0efCTK9PxJgqdu/h48TWvXrto6q+1Pu5xVdztxfFqWAd/B5oKJHfPu7NQ3f0E1UFinHzb8KelYh2Y41ojtrtDDGNJQtFyrhhYZ+wvtTJ1YOrXxXsnZ7FOjMJJgNNLiim6fsxchyl4sWd23D05ZFJitLwuJa6pVSI+HEL3Njj1yrjvvPi6St38zBPiQRrPxSW0BHKpXco6KC+EpLv0pXEaVr85GWPHcuoTy4tv3gNZb+oSH+BhhK/3gsVXtebzbBgwzHY8q2cztcqooG/3hNB1xVDzce+iO6c70GqP7FrjdLrtN+rRRuAM32r1rrJ36UU/4aPXRZqSXGOYuRhnCDQ8rhaksYLudLPKOlW4k1EvqhvpVNc6TWWH46qXW+HU4bAoTVcTiRR2XbK5HTtUtw8oRyazeCV3NwVPQCRdRawZfatKqOGoEuzoeHfXcdNrOV5jVU1HCfaE1trvesmK13m6XeXN+nAS1grQFm70STqYK+2QHhm1PUsZEKPL7EbBWPq2QdyeLzXR62O2oxPxIo/JBim2aebI2aQMF1AN00DwuKN6uLQEdz/Rt3pKDiUyOulVPjmwHq/CUYTtkm+J40nNohXbTGi9FDd70aUxZ9WIgeVvTHXPctqtrb2LT9TLg+idthlawLp9ZpgokNAIihT/yrn5IHjZQSxBD+wMUE2dlk3YuHzRQbfpLghkkmr8aq9yAyQZuThw1gqa0sTwT1lu1qiRbMerpfscF+zd/JTHWdgzbY9a+wQ9DcF0OQhxa/etMiGndAeh65UrXSw00AdXEHYkAxJPa1eUQO4ucqpEtomSqSfinNm6NuGG9kGGDl6Y2TG/zjk0Q/tlqN2mPipVFpERxedKFHU5SkJtWNgyJ2dpp835PHKxIUKNKzhW44wScr2w5t0fad+YrNMF1/Uxv93P5S4f6hAfyWmtuVvjmK/JNcUjzFju1DVXNvI4HDT0NtDn3ZEU+U3DuNhW7XAlsYhdZXI1h2RHy/DvxpVyN9MyvGL1MupOrYZsYpG+dszKYWxFbPCitRwBucvwsb0G5sk+WiZ10kOl2ty0an8oTcg1mEyyit2xyFYna6eu1jgo60GkY6SdXFZUWGMdvDY3Z3+QUXwj7rz2PoJuPL9euCAm5IPMrON9cIuPhb4ErftOlXgN509HuHGYOHJZCJaiDhHO5jFGmna3lRMjuCxjfR2Jcra5wVhNHVZ+xC1LtZXMMOw919w7R7X29kgbwgqOV/H65mJQYKNcF+x13+FSahjCZKV3FgD15ZbxfTPS3fDqRqoTcJs16innZtutJetmlwZhNEJuoK2qIVIqGn2mg46HzZLQ2Owu9a5msgrnnKuYq+JQwAxZNLxZ8UIv7jZqNgUssxEQJsBhVT05G5uuMHbS1JVyPDoxuc9V0ilPlrCH16jZwhtzZWLsMsm7ohRQ8syPBzbozoHKHCBjzzFCcS64pWfK980FCb0LaFbgFm3GoGqR5TIqBc1mpKXGjvWBg9d7RNf5uFHPOE+t0clQSL7rhI2/mlA7PvcSGE9j74jIm2PkkpXdHbIjcBlXXd210cpWmrDYdcUGkEBhuusFuT3miUkQyL0Q9s1kgdmsroZyO3F0TWche+I4tx13WsbeliEyXJjxAC/bgq/woqzl8U6cJuiwQkSOIpAlka3w256wjSutBap+2InFTnKn45YnZVtaThNZpqejYapsnrFSahmmcEZlqVhTUXH0jA3Q2BpqvLsrve0mJqyaK57jGrM7Kkaip5fSAJX8QB5IPeKXmZGA/hGThnoJQXx07VYKbDhDgOcHbu0aSG84q8NI3fD0eIxAHk1q2tDwPe9t+bTq0wk7xPl1tx9GqzeKBr+xtsAJiA86BXyoRYUcERgjhSztluHxLDRIpF6wzSi5EC3LEH3kbHJy0n5FFtdBXIZVUdPk3sMT6GbDl4tuucsMjk9E1nErMoIPW9i6pYwq5bW03kLkhByN7VH0rVphRTDjstm49pBW7ppxe6qlxPcalbdN2Tfz/bgSh5OzGvrahkERua2n3Mm0ONhAWHOS2dS3UQWPaJuOo2LdR/CGFFJ1dLU7X9zTwL2tSz69SVU8NoR7pHaQ65/DQkcjkTxjF00dIldsQT8jVEYAYDuk9enKK+iRJq7efsjYXiGzQ6uLikLcjxeMXyqwFYzhCPGhzuDb+6oeERItM4AObRE6/WaFZZcpwCHzuOr6TYB6LZgOJtiqrMoPClGChwPIxCg6U2SNnTSLEpZXu0xGsQ6QgLgYNGnSFkzdkLCvl5kwQR1pYchqoCMjqh1xtAhGHyIwE11x19F7a1nupHDyJWxLnq/IHm1h213X5UpK86XnrzdG55aYh9JCqJvB9kwTTR9hRltw1t3pQjCzF5sE6pD7tQ4be6JJh01uLa+iMpTouMtJ7U5USZu6ZhEEORbE+l4R3ncF1LZXWoVYtJd6nllRdNcO6ymxOWqTrQekIWKI7u42sunCPb6FT1FnR3SD+mGCLAe9c33WPQhonoL7Snzci1HJEjiygodgkARCSpGAJK535h7VZGXhFMnfO1YVuOOYGBTd36iM38LO2oZRyD54GKRekVUbXeNK58iBW/O2PlFbcklR3WXKpzQ+llQs8lN/L63dTazvWiids2qKOy+xV+sqCuQAcVeqNx2vaV0KyhbvXRUPtRqysn5ziM7TihQm8maRlsrtd+zB2W1BD3+/F5hDRoJcMvEOLdp2fXa4zNC0jdWXrTlkhG8mhmLgl9ue95Zsp+KrjoLDK536HU4IbAUmdh+lEyg9DecGPyGrWD3gpW7nSCrq8Qid4MAHM7qR8icR95q7Hi6HgyciPSetfPjYxFRNbNXRWY/sGmWZEso4VGfRW+VzvabJXuif5O0wJoSFJe2ePS3bu0VeZtlp+BqsIHvLRPdicnYYgdRZKFChnkgB3wrkZluJtyut8HUJjHiEWoN3jICVNiJEceH9qIUaG1mBt1Vr0Jt1KmftAmG6bDO7uuQ9kuJqUUQs3++0q3gi+rNMdtOqBbPrcKJAzhXDpA6kqZ2SaUhWDs4R8U7FcJy8DfGFjgjPKb1s1Jv2SG5HTSJpBGmmXayXVxHFjO06O6+J23TJvGNmpq4PaeiGLYVqI2XJRT4Wl611xEDzyOxOhSbBiDUNFBubJ4WqIeK4Id24FBNcoSrOOCHCSucU5Kae8LA+tygjiWD62SU4HOlCH2UOZcGru+d5kdxRYaD6/nKlKPzljMmK10IbXZnu/vq6VmIjzho5YnR2g1MIF9KZXlZeeKGvd7ykWlLzUIjkuuJIkqddsI6aICwmEUZGstOoPL+22o3VDzgstMbR3ZyDVURR5uVEazU8WdWNH0t6NYQddNjTqMxOV2tZY6VxPfMwbWxDJ2VQTSrFlgt2K39PSsuje9KZC+SX0nCNpINCEXS8y+wNfN/upaueZtq1C26ceCQSN2zWoh2N6okkr3eJM2SQEkeJz6iqWJcpndWmHkK7HU6uFXoeKrZZjh51TztQaKniKM4WbbF1tork6rINUWdLvEYar1gnvj5SlpwEGLveXZpRoFyI5bPADzMeFlXsYgxaweO+jymY7GB4ibZ+evVbYtuU54ziKC9y9Z7Q2AIra1BBfNesW0siid7RrzJho+e+xEQkayDNRjQzdlpMFG8q5BWdUyJsm5fincKO9s3H5G7yfEKfoHwQ91W7NdujUQmBNWlbhEvF7T73dWsZYMcwWMrONu+JsFMzrRpdRm4Neh9bSi9cmgKmpKLNuqax0SSM8krbbmWLwHI/7Lzt2PpUGJswhNXibXLrs2pjS9mDrDHfXrEy3nfQVjlMvNNmdSKuMVEjbWXHONBJrFj5OFAhRLdUesIRkht5KifCmG425HLKbOk6GA3G98FgmVihpPmgjwN/dzzEX+HZgKQWsgzy1UYZtDZlck6FjJxAEtuPdmveSlNyc+/1AvKtHuaW/cbbEjF8IShEOboIpgx7KF5p5u4Iw2wilmFGItM4uJG0CnIdk2uc7eHM3rPeNt2duMCm9vERg5QeZXwuMXHRSlA1GDBQCglWkCdCxys54wsoG0K3IzF3FW9xUMtYj9+aCj5IzMrGz1HRbyIdzKNR2A2adT7vsaH1bWolhSS15azjXHR2h7rDVv0NNO1rCj5uO0ta3riy1KcLUnmNY7QbI0DhTR85VAwRmVe0CD9uK+o8bb3QlU77K1sNR2c4DzjSRsQKSay0Wjpqa+4TekqDlGdvQVPyJXfcDlczUDbDOJAUGiwLA6l21ujfuPBUxCfWOEajb+B6wJzX9OZknSxSs4Jtc/PQo5xEV7PMkz1OZVijK6rEgsHrkte1QrFLI9Pck1dZ1/3WH478kCES6nmcFMEUVFskXXAZtJWUUJJ7KrWIqxD78VDU0zmkEFzocUtcjryPF/YhULd6VnPklq0HfhjcJW1F0Y2ghYahfFartiTCW5S+lxmYqyd92YdYDSW+cW+pTYq1+/uqme64BDGsJvZ+e1AZhnn58DKfsr6dOf8335Gbz6T+nx1/PU+x3l9veZwlhm7w6cHr039XwF8+vAB0AeI9j/+6Yojfjs7+6fDv4197t2GmNT5fSXs/SX4e4vduPL/R/ZJWwdD17filq4vHiy9ghzd084uf3fxuMICO7vuD0q/swW83eL66ErZf+vrL8xR0vp9W81stYZB+u4zfDkg/vARv72F9AWb/ErbNrPrbGxNAY+wVfgUm/j+l+U2jnS8AAA== -->
