---
name: "rar-cowork-cookbook-bulk-update-enable-and-configure-audit-logs"
description: "Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_enable_and_configure_audit_logs", "rar_sha256": "9512b80a548f8763630549a43a8053ba4bee5130870dd99ddc0f123c8caa1856", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_enable_and_configure_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_enable_and_configure_audit_logs_agent.py` and in the RCI capsule.

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

Enable and configure audit logs Bulk Field Update — Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-enable-and-configure-audit-logs
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Target D365 legal entity; defaults to USMF sandbox.",
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
      "description": "List of audit log record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 9512b80a548f8763…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_enable_and_configure_audit_logs_agent.py` first:

```bash
python3 bulk_update_enable_and_configure_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_enable_and_configure_audit_logs_agent.py   # or on stdin
python3 bulk_update_enable_and_configure_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enable and configure audit logs Bulk Field Update — Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-enable-and-configure-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_enable_and_configure_audit_logs',
    "version": '3.0.3',
    "display_name": 'Enable and configure audit logs Bulk Field Update',
    "description": 'Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-enable-and-configure-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-enable-and-configure-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a3fbe45a5c78ffb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/enable-and-configure-audit-logs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-enable-and-configure-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Target D365 legal entity; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of audit log record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when enable and configure audit logs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to enable and configure audit logs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.', 'example_request': 'Bulk update the audit log settings for these record IDs in USMF sandbox — show me a dry-run first.', 'inputs': [{'description': 'List of audit log record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Target D365 legal entity; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across many audit-log records at once and want a before/after preview and approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateEnableAndConfigureAuditLogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateEnableAndConfigureAuditLogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Target D365 legal entity; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of audit log record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateEnableAndConfigureAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOi2LbmX7HfG9FVdclMQAYhT9yIRkWRWQERK09kMYPMM1hd/703ag51Tp7bXbf7U1tRqWz2XvN61lov/P5md21U1G8f3zTfzhd7O03jyK8Xdu4tNsVQ1An4KhIH/L9wi7ytY6dri7p5e/fm+Y1bx2UbFzk4furyZmEvnC5NFkHsp96iKz279RdFvrA7L24XaRHOJII47Gp7PrWofbeovWYR54vtlNtZ7DYLjCQWu/+ubaTFz6kf2unCz9u4nRaGJu3eLRogl1OMvyz62F60kf9Fxu18jD2pizLtwjj/CEi3Xf2QyKun93WXL8ra72N/WMz7Z3XeLQY7bptFUABty7Iuejt9N9PM58s09puFG9l56DcfgLL+aGdl6jdvH3/9+7u3GPx++/j7m5vaDVh6WwOtjYe6bG47qc/k3ualqc/MyotFOJssBfTA9nICNs/BdenXgH0Gljw/WLyufm78NHi3+Pd/Twa7DptfPn7KF6/Pp7f5P2Dqh+5tYTet7y1cu7SdOAVW+rBg0sGemu/Ub4DL8vDD8+Q3SkW5+I/53s9PJh9Cv/3501sBRHi45tPbLwtgl09vwHLg94eZSvnzLx/SYvDrn3/5RqfpnJvvtjMxIPWHz6/rF1mw8dvWOFh81lR28+IFnB+XPiD+nX7z5yn6i9zLJJ+fm38uyneLH1Oe9fkPIO8zKB1A98dkgQ3AybcPtyLOf37xAK73czt3/Z9/+Vdk3ch3kzRu2v8jur8+CUe+7QFrvUzyy7uH+/6+gF66faX5r9mWIGD+iiZg+xd2Xw31r2g/PPsPpNM4B2H/xZc/JPejA9B/LH79l7r9ZwfeLYJPb1s/jXsQdyBvPi5+f4TIrz953xZ/+vsfgPT/loxWdLX7oPA5s/M48Jv28+dff2oeyz/9/defuhJEsW9nn7s6/RHNH9n1wedPFnzt+vnPZwF/I0/yYsgXX3No8XtR/rf6jw+Ls53G3rf15uPi+0ycP9BiVuIL06cJvsvGBsj6nR1/efsDQFAOtOncx22AH//2bwspduuiKYJ2oblF1y6Ag9s482fh9SgGKNs8UAPAoF83MTDsax+I/9nDs8RFsPjtf7gPSH3vvmAfniH98xPMP/sPePsMUPjzFygHVzPCfQbw3vz2YaEDFkUdAxAG2H1iVPVTbocAw2f2AIIbv+4BZDlT678Hmf1+/jHj/29/gcvnB8EP5fTbo0zFTzQ8bQ4zEjZd6n+YdTZnJH9q6ILK5o++2wFeaeECwYIYYPk7YIumSHuApLN9miRO04UXA6wBFW560AY2/DgT++233xy7iT7lT+jGFs/S18Bgw1dxFu/fAw2DNA6j9lPuu1Gx+On3P35a/M/Ff3bqQXzmoYJa8vIQkJDXFHkBMq7LwLa5RAKot72Hh37/42VnQCYHtRr4Mw7mejUfBhGb+N4Xo2sc835JkAvHB8YGhs7Kom5BPVjE7YfFIVh8lRcwnW/NFSMqmnbh+aWfe37uToCqDdT5asm8aEEZbuMmmN4tusZ/cP3Nqe2HiBlIfbv9bSFtVFCfihT8M4v52AQOF3kMzP81JJ7rgEj9U7NYfyHxYSHPMboo7douo9p+8Qjsp1/mev06Dojbi9wfPuVzRfZnUz0S5mkesAlYxn259P3sc9CAZAAdnj1H+2WPPVdR/VFN609580oGu/YfHQoQZVqEXezNJeJvr5BqoqIDPc5sPyDpTOnlBe/llUcMPruBRyR9DeRv3RBQee6Wdo9u6dk+LD51SwTFF/8/d1OzYZj9/sTuGZ3dLlhZP1lPh80N5uzYZ086yzmTeyTntx7nC459gfNPeRqD6Kunvz13Ptz82vOESGB0D0DR6UEfxBhw2Ez3kQJzSNf1LJ79Kf9SN94BRR8gCawK8ALk0xzGXxjOd79IGgFQmK+/9RAvN8w+B2G+KDsnBSEY+L7n2G4CpKrnNH65GeSDP6f0EMVu9CetZkeBsAP0Z5fPlgW15cNXLH/e/SL6nw4+W6X5yKON7EAW1w8CQA5/FnCOxiFuAZjZ7bOfB3p+fBABamRlO+vugJjK3r0W/dqvuriJ2xkzn3b1SwDd7+fvp6bzqj+WIHWAsUCClB2w7iOlZrTJQCMEZACoAjIsi3PQGACjvIzwIGhnMz4A/H2F2pPiY/mlkP/Iw7mifTn4SCtw5pFjARAdrEzfw4j+ozAB9LJ5x4PvP0baV24z7RlKGwCHgOOXu89u4sOzIXh2HIsvdD/+08D081+bqR4l3vhzAHxcRG1bNh9h+FmWv1TlDwDI4KeszaNCv38CxPtn7XwPeL3/CjnvH5DxfoacP7F4av9x8dfE/BOJV5p8XKAfkA/IfEt8hdnrA6yyeb+23uPz3U/5yf+GuIB9kYE4m304gZbga3n8sgXUyLAGsAU2P8tlM1fZAYDKoz4Ah3zKv4/7Oe9eKAPArfgODx59AsiBp/++ljFwK28Bb2/uNUN/HvQeWdL4bx/zLk3fvQEc9f/CgDeXrGwO8mYeD0E6gRaujf3H1RdYnH//eXZmR4CQLsiPsHhvz1PDwg4AjcUTY+cEmmPvX0HvLHU7lbOYz2Fvbg8fADW2/8xLefyw0w+LrQ/AMG2+j/pXVZur+nfJ+bQssKgL1Hm3mK3QzFUYWHbWdE5su0ke2P9DWR6V5/Oz8vyzQDpocvz2WXO+r1F/A2gR2F0KvAbAdy5YX+rVD5mALuAzMG73tPU/sJi7h7mK/tz88ggFsHnx2DwvzE0EKFHT/MO3AQ4/9f0hl68t+T8zMUHfM5Pwio9zC/DuBabgG4xR7xZfJyJgwNeM+vi7Qt6B8f/XeRqbw+dxZP4BzoCvr4e+/rnF8d/+/gO5niJ/jr0faC+C83OR+dY3vFLlsG2edW326A/UfdAFwA/K5yziN92/SVA8hsNZAiBx+/xbxu9vIANsQNN+5cBrugDbAU6+b+b+CQZwARiC62dig3v/N3PHi1QT2aDZBbRoAl06FGITOBVQKxIjMYTAaRvHbAohMMfGHd8nUAyhVojn0bTnuUiALjGXcm0bpQCJd29PpPg894vxLN4sG7DKewA2/rfbYMl76fXUYzba1zHnkfVP9X5/c0gc7OTw5sA8PxsYQh3cWjkKL0IrMgjtYn/PnUu6vGLyyhUITnB08niU9S2/5ul8Xcje8XrIlrKGily6E8ZliDQMNOqrSHVT6qxZmUb4hHLtrp2H7dahHGamptVxStNn80jdx869+uyUaqJkRVy61MrreTCh82WnxbdTIMD7RqtgNka0rLnEcEzJWpzD1MqH46KpjI1kavs0cE0l36v7Zo8O4lZquD6y7tMhteLJ1e/B6dolSMzXMHxvLreRW9LqBU9PQutFQnYy+e7s9xy8IpszKwhjlV0oO8ZpXpAqeScEhHcm3Nh3kZVyj29enKJ6zRPR2juHZi9sVkuEFIVRII/cKBOifYOlBur57kDqbJGe8yQa2mU3baE9aZ2Sa39EdfuoIZojoalIhBTHT4R7uU60ipUIvVv6PYZiFH5osWw9rQSHpVYC7BKM2SaFds6G03ZAl7i+E8mtRxeld1ZSy5BaXELM0zVqLlCskLhGyiVytNxqqMtU3BCKmEZUttcmS9zxpNXf2UIQw9Yyt/U1SqspEeLAIljvKsh8kSXeZb/DMvqiGyDQiY1n7vtWzq6na5box+ywl1SK61Cdlw+1oEnpcodE+nl9bO7ZPThIALd4EgEanuvV4SidfYKXy9iWida9nlVb8arAWfGlM9zX96aUkKNg17EdT+baoji2O7bb0zQoXYIx900TT9rVMDpp6V5NlV6eaSFLsU2ycnVKYHrCIMyi5E+V1R9Lj1bTIKlhKnLKE5yWPClpWlPVbuqtKx+eDP7Mt5HjSIKDxrvYbFoQi5YQHGic3gwd1nCxVbY2tu7N/ho32oYuRJGNg82WYEgJym3LSHHCp/2dw5S72/Fct0d0akIbaTxfqroLbdwTP0QmmzSWimbdHbvqN0W88RCRulrwJm5RJ4QFQZ+CfgdJWFMM7ASNfXbcjleVdSJv2qNX6lKF41UkehMbOjkzCQNWr6IirJNTngO9lmXkV9fiyBk4whpUzkjN2UDG0iqLQTaGg+kNNk2tcrxnTZJtJj479AGEwsSF5FITkk0QdIh7K2m6UZHbMnQvUoyO20ScNGTwHHJnElxJZwKxm4oqAeyu9VVkhdVlbTN8HrCnLt1CTgFtQ/MqaYVldSyhjFTDbAKm9hCcdizXvZSN3Jd86muJkdUHzaBcfhTQSA+hUGXCjU+T2+N2OMuDakeCH2+D+y4bup7ZR7KvJ/eVHDskZzNVotfUum2LKkNZr0kRzuLbHbIRN36xOgnD5ShME709SFGRumd6W6Kwg0Eyu/L4gaNjQr21EHoQknNtXgmZIoo2bO07lGMX0i/pfrw6kbnnEEIXBTxs4JYhzPzG69v4FHYCfhmKs8a0ho6n2EpfCqljj35YL/fNwaDM4zXhIIug81Ol3ZT1cSzye2BjqH6mbwXkMpuwTZpT093lIqZ3cD5eiSWBT0BEQt+deWorlWwTWsyebqphgpYMJROHk+HSG7l1U241GXhsZseTzFawT0NHioLMwijiQDvQCGxieIJ4ZH4fB1dfH1giDOHDtmfqvcBZu3PuWrmy5nQ4MnB8sK1zf8DbbTwqyzg8riSJx+Ije72waySrrjZRrwVczIe7WPJn8treJ8T1YzrITbXdbLUeh8/oaTJyvewbTrOHM8BAcaBkiI6j5UWI8ytqJqjKKjzncmaAsJvC34w5su/VQOguMCkOYdLrEkFKxmnwMfbGyuXNy0JElhUpOoSGRdPHdX7A9/qx8BFZ4r3tQVV2tzYzI2mX6wm8a0aK5SP21h4T8XY9R9xB1FmFPW079rofJ3npgdbZge+ybiA3ttpbe9k+GXLqy/tEw80DHMcmArGQbElkJl9ZIUyyzYVnjeteSbWwGpApRFpdgoYjaLfNEt1KzKCdlz2VlHV5ifobofWgj2+Ear20fGXp+VZ/rqbudA7dPXp0OTBOF8FVapYXaclzzRJWdYr2+ztygzZ5IjYuFOpywJfnJFX2uSp12HrkSWzNQTuKaAKY5tbHifKCKbzp28Q4wNsa9UTIDTjcVwsdo/366uxraghr6tpyfVZeGWozsHssYk7W3WqG85Uf5DRrkyoSQgu+H9G1YtmOrQ5KY8eEH64EYLruTArSxuzzo7JZbRjWRZNMH/2hpvKIh8hpvaa0Q+G20aip+zQ+rnSphG1SXA9QeiiUFj97TR8eUQXlIXy11SR7mDxrssP4dutWK/TYL+V5LmRl0ZWWa2bpcN0ZOuGBurm4KNvdN24iy7DfUyI/rc/M5VxVTaKb+V2mpAPaTNgRJ0wrvKHiOcmvBBVnwB2mew6w8L6ND1KxP3L7zWmj4MlGZ1cY1EEooowsd8jK/XrimAhuEnGzvlUikuEd4+LSZKa+6J+csKovKqgO0hkRB43Y2zUUiYwUnq7rk7tvtdZQLCxMToUWVNVxV7IxT4Wxo0Xe0NlMap2ss7BKLox3hkXMjzbrZVMf8QZZFT67OXah1VN1eNV3mRvftabJohuhsBRxiO7ddNxFF8IZEpvIdokgn+T+MDE+y8Z5PTle364SwVCuh8S+7o1M8iQdDNSnleAqWqVFkXzqQd3MrEuhoxWZnrdWJgKYFFC4jOPeqgp7RVTZaQ9qdpUicUJerGHPbotcCqpgt8t3AzmybrpMRz/1WQvOPaZnhvxy7NZ46npnIYVzwmpclxvNHah7Jn9YnrZyeKnks7hz4w3H7JOdIHnrqzLu2bgtooxgV7cyhulCwyHa2ELHgHLltlqTewa2UtX2TaCtVtxYepdcgEX6OhdwGEP8xhK2uY4dM9jZTcFmPOAWnk1QYNJjYRF9QSl4lmnHnTjSLnYlSTCUYN2Bv+2Hi9ogd37PtcppTUboPSh2pKNu7auMDpp7GfLDdS3w4ia/UeOZKoWls3ZPxLg3T6mx32dCLSj3CS7Wl6ORe9LmznATusycWDlQVWJUar2f/OUd7jSOWbZKxd9Zi53Yy9qdykFQtnfeHvryjsXsqYYsKIdy8ihqVjWyd7+XM4OXLheK6SamCE0/TcW7BvGsPWAFLlnLNtaLmpMh6Q5DHIGlhuPmJ93UfPtymCBk02LLy+Qfd1e1kPLizowBfVDt9bQbTbs62N4Jhpv6QG5zUuKu21PCq0Lm2QPLN211FLSNLE2B4hFudjtcd51sjKNiKy0P3XUkdA+QRpLYYDtVaK/R455XciOBJ77N3eYAmejevK6RenUjtqUUBDuXRW2sYnTtnO612jx5FM2XrBSFEYMqa8kwO45e+80h3q0v4jG/7PYarY5Bhm5MFsHunbLxqjsm31cbc6duNuSt2p342LnJA5pKfEVtVyKkcYfwoG5vcESxeCGsr+5WpUN1b1wUuAyXl60pyn3HMNAha2PFozeryxHK6GpduaSroj5pJfWKmrJuWakc2jHGxevQ1NbuS78wstFjEWKk7ls2qiZoQ9pkwUhJYAlGdUkV3mW1lbDm0ZPb8lIUHdgjzBc9al2J+5RHgiBe5CSpQgLq1k5SsyI5VNtMFUO1hQ70hjVNZLheOm5rNDwV7OulVUhXSBwG3QQtcTlEiLSCA+x2cLZxynvDVVfzQtGS4xLCxSI4+O5uQMZxKrG8TfXlqZYzz+0UZ6rvcXHasGd04zJQuIOhBsWtfiLrgd/3PT7sYG7nG85RvxTitEpwjjqY6w3EGFak3K/poBciuod9AzqfuBg0wFME70DHoq7jk7eOPTlsb+ftLZmcm3VntpaeZZW24pkhwuSQYzLMD50L7q5yIvLK1BVyjQ40by+seO2mZdVGNuLlsE64EXbzHQmrF3HAeJnbcAN755OIl0zBMkNG28GgTmPWMbBddYh4rT8ONxZgaxrxlUfWjadX7Zh4hWEddlh33Ix3bKL1+HyJzHgFrQYQ0Iyx024WQlNHepl4ki1sOfh4CcYWRrgBu26UM7Ku1K5l9oXJybauXPsKH+DDrTkdJOIsYcVBP2tqXiM633IkkUsa755R5CZRuy7RBn53WMG3tUreTtigaXGFpsZNVYvDiNxZD+2T3Y7qrzSE9SfF2LoShaP3CA79ONPXdaR0eh9u3Eo4hQTJ3Itpuxldssu6Fq9aXxTRPrZbdo/QcbOlmhhvBDwdp3ogNpU5MVItXxCq5hs+KyxSsKEaoWQYggpkuJA4ZhvTYQ2ajyxyO9E9tBx3XNeEg4RLu6l2jOb5zFLAHbxMPXYXM6dtX1+9292z2CtXtUjc3k9QIt8Unj1cN/H+dG60YZ2CReHSDM0qdGXTjwP8GBJJKbrF+QpTF5yJlnVa4XkqRmPCCJ7qJwjrRhrOM3JvwCnB6+eOsYhKs1hpT3fNCkkcLt8yt3TYQKhoGlAWhqlb1xPoV1etJatEXl68HAWd35U4gi4+bWyDUky1kyrTUvt96ijDlu5NMVkzB7uDqQA5EHFXdaZ6OKzX+5iUFSiiQBHLnesasp31qMmGZGAF4yixqObI3efFXUnYY84z24DpICkrhJ3gVDiX+IQS2pOgdVwZrTx556a5XhnbVZD2tikT4xSlvbDfEkXoquvGqDndbhSrol1yTLKV7yiOna7qS3910hE5rezudG+2ueN0ioQ3pJFt7RbBUB81nIpxCP7erlhE8cfNJUHMsqZbG/KzPjTsJSxwNX+ZhGzUl5bEBwp5aU0DySd4mbIinZepFcNMt69LsiTDco8h98DAE9HteEoHhTqB7GxzPeGHrqrGRLeywsnYXYbCHk9qEqWZUE7dSXZ/8TJM1YleLOlbn2261JPoi7Q6LAcrFPJjcAsQE9qHjX1QOX+/ru49DAo3PJyXY9LFUoDuYJgPcNLYN5vITpILit12m5Bz4xTMiQnduPvTFS7iLBCslcdy9+BOsLRITEpr5HQ2Mo47LJNQpOkdveZ3N6WGfBl2+LzuTx1AStPPTtQg6TZVNebgexzajNGekdbtZSXFLbZrfDDn2pk5RlKvwoKb728V1XkbscL5oxsBkIJb2vc86HI9nkZxt/IGb00syWl1GBR21G2lZNZnXIjxS+AVmGzSnqseTYokyUru9ZIUlojNZbaKJxWk9fYI0dsTFfK1jK8llNkp2bajaRInV53H0Zx+PE6O3aMCMCUVYWWc0JljtjfCNSMjN2B7ONwcaN2cYA8kQ6BSt1bCif02h+qTu4TWK/U6Ecd0DEdgYE27aofW2h5wKUDkS33jrM1RR+j9jphspHeKm7GvMz4IAwYJOfG+OXFjZFrQINqjAnlbU8rh9SjbkGh5IblucI8BUxh2YjS5Ejy4dlYkGdIwxaFBMK2HS3x1PaPGt5bq7wd3wAPjUEGdNA6khaH5tuiaqudW2FFOBlQx+bKHUm8UT+KpgTPPvEjWqhWb8wZjT/s7sbuP3El1Vrshd3go4XRGs5rDqr1knm97iCIeL0evzb0JGUPUOyTZQYJrizQ3/kCugWN3JoozKk9UXqj1fcsl7D3wbhRdxqA5uew6D42KpW0TBBly6h1Biakg6syrq/ZkWRExkSbuxxPhR6iFQ445bKdO4bciUjmcK23J7Z1UoSsvV9XuJvlbf1gJhV0rDRpBUp/Jecfu4XB7cSICsXyJG+hSdbsAlVR/jV6x24qVHSRgVTjoI0RZCSpoelN1G6MuJ3rTajRGkyfhnkLTS5DdiUhoyaUPo4ZG3+GdXFFS5Bl6dcwpTB+JPEhBx6laUJa2THxROJ8VDF0+GN1VpnOlg1K/vpfsja86xQuOG28p0O3I6MTIkSWaE4ZHpBx2o/p0DdqH4548gv6s4Y16CdrIJd5Giqvl9FRAxHbvGjA3UcOmda7TlqN3xTFeee46mtbuhSvtTcZRrO0cJT9QD+GAuqSOsfnAsZVdikppyeKSO40DHyxt/t4rBxEvZY/MG79UwJzNicdKmbrzhGagY2337iiSR5VuGTlUqzNxvrvsEJdbZuthJkOf2Xs7eLetK5xWWQCaA46gKJqqid4H81M/Tbi4Cen9knJaiiYy6IxsDNszKkfAy3Z97Z0UC6Y8kAhreWlzTCJuJXy3xpMZEvWt8K6cml3G5cokO428czdXvrN4Jwf5shl1DBbFMydefGoyr5CQdfuxC3nWUvSC0HLKW7VN1jfGCWm7eher5DSejgbV3sx+LaVXWyDQo65RRdc6YCpokhWYP+8thMQ3Ir/mAqaMFwTLIWKd+QGSr6YiucFci5UkKWKrdchAcNZX97W9uVWRtMGUA81yycCD+Tpfd0K3CmCqXuUZPla7KyuOfH9QzMnzvLHZo1jVkLulh+m1M+gufZZbu06qkux8CF0ShE4W3bCObss8gs7l1Ac1sfetJcdOpwOWuFmsLMsJ7kQTjXR0t+IIq+QxrFJ8lKMMSld3K6Q5mnXBsVeJUFAstSlkE5CwlHNCf9urGhOyHEeBQVYTOV86mXhKt5gwMFzXnglXu5n0tcGgni9aRa15EZ/IaqxV2a3JkVxdEgY+3WqXTWSvgEPKENE8KqGL4VFtoBi0Q+ChfM5yCHUGru/Qy010PcIBsyGOo8oYKNh2JRt6H7HeSE17xj7aalennleeT256vNTuWQZoITNeT/PGpHdq4hHkXZ5Nh8YxRfpDm5XZKjJ7WsttzrUveDqlFgCsLJbj22lwkbs8Mmm9VFMoPS8xEz9TK3GDLb1h7R/P4XFtbIO7a+K6x1xZanfMjxfSvtBqO4DoUaKgN2vtGPsKnsLCdSMXWcngZ04fKGFNRYlJIKvojN3WrjcpTX8XrVNd5QFtwOaACGp9beuxRCvXhiUc4dJtknLuCkyKx3u3KRP16Nx2+UmseMHymItByrvBJW6GGq9gmFNDpFBUxrjeof6uN6drKzUxM5w6Fab1lFzKHduY0FiUq67SSRSnOJjZ8geuo6bjwDBv797mB82vx8X/lZfZ5odK/8+eXz0fQ315J+XxgBEUjo8PXh//S9L9/d1b7cZAtueTuybtwteDr394bvf+L7yNMBOanm+NfXle/Xzs3trh/Kr1W5x7XdPW0+emSB/vqYATTtfMb2U284u7Lvj+/rnpd6qBK9t7vmvi15/b4vPz+eW8Hufzayi+F3+7DF+PNt+9ea93pz5jJPHZr8tZ89dbDkBh7APyAXv7438BUltsejgvAAA= -->
