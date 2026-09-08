---
name: "rar-cowork-cookbook-configure-manage-service-accounts-and-certificates"
description: "Applies bulk service account and certificate configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_service_accounts_and_certificates", "rar_sha256": "34a2caa2a402b641ea8dcecbf478e3f69fe811757dc9d0dd513e0d051a2db316", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_service_accounts_and_certificates`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_service_accounts_and_certificates_agent.py` and in the RCI capsule.

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

Manage service accounts and certificates Configuration Bulk Setup — Applies bulk service account and certificate configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a b

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-service-accounts-and-certificates
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per service account/certificate target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 34a2caa2a402b641…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_service_accounts_and_certificates_agent.py` first:

```bash
python3 configure_manage_service_accounts_and_certificates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_service_accounts_and_certificates_agent.py   # or on stdin
python3 configure_manage_service_accounts_and_certificates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service accounts and certificates Configuration Bulk Setup — Applies bulk service account and certificate configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a b

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-service-accounts-and-certificates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_service_accounts_and_certificates',
    "version": '3.0.3',
    "display_name": 'Manage service accounts and certificates Configuration Bulk Setup',
    "description": 'Applies bulk service account and certificate configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a b',
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
        "upstream_slug": 'configure-manage-service-accounts-and-certificates',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-service-accounts-and-certificates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2764467a0d77cc3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-service-accounts-and-certificates'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-service-accounts-and-certificates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Excel file with one row per service account/certificate target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage service accounts and certificates, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage service accounts and certificates target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk service account and certificate configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a b', 'example_request': 'Bulk-update service accounts and certificates in USMF sandbox from this Excel file — validate first and let me approve.', 'inputs': [{'description': 'Excel file with one row per service account/certificate target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have an Excel file of service account/certificate config changes to validate and bulk-apply in D365 F&SCM, with an approval pause and before/after evidence.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageServiceAccountsAndCertificates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageServiceAccountsAndCertificates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per service account/certificate target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageServiceAccountsAndCertificates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
