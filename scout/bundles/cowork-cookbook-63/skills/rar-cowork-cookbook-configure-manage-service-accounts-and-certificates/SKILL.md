---
name: "rar-cowork-cookbook-configure-manage-service-accounts-and-certificates"
description: "Applies bulk service account and certificate configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns a b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_service_accounts_and_certificates", "rar_sha256": "34a2caa2a402b641ea8dcecbf478e3f69fe811757dc9d0dd513e0d051a2db316", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
