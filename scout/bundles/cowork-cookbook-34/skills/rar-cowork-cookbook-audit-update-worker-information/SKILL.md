---
name: "rar-cowork-cookbook-audit-update-worker-information"
description: "Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_update_worker_information", "rar_sha256": "c6f5ed36ae5a4a99870807d9e84301c622829e1912e6b36ec5d9458f375247c9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_update_worker_information`. The original RAPP
agent is preserved byte-for-byte in `audit_update_worker_information_agent.py` and in the RCI capsule.

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

Update worker information Completeness Audit — Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-update-worker-information
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
    "date_window": {
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 c6f5ed36ae5a4a99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_update_worker_information_agent.py` first:

```bash
python3 audit_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_update_worker_information_agent.py   # or on stdin
python3 audit_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Completeness Audit — Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_update_worker_information',
    "version": '3.0.3',
    "display_name": 'Update worker information Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '196b762a7284217d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit update worker information records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to update worker information. Output an Excel workbook 'audit-update-worker-information-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no update worker information data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update worker information records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.', 'example_request': 'Audit update worker information records in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants update worker information records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditUpdateWorkerInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditUpdateWorkerInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWJbnV9G8jpjMbNlmk1jc0RHDLkBCYpOAcoWTHSQ2sQpy6rvPRXp2Oquzproi5q+R41ks9579/M45gt/evL5Lq+bt85sReeVK9PI8S6Nm5ZXhiq3GqrmBr+rmg79VUJVdk/l9VzXt24e3MGqDJqu7rCrBdr0v25W3aiIv/FiV+QRWF3UedVEZte2TXF3lWTCtvD7MulUVr/o69LpotfAADLMyrprCW6gBIkHVhC24tuKm0iuyoF1h+HYl/E+DPazAOsAoyYaoXOVR4uWrqOyybvoA9nV9U2ZlAvit+EcQ5U/qT+EBwzgrQ3CzXflAOsA6qZppVef9InfbF4UHTts0irpPQLvo4S3yt2+f//LXD28ZOH77/NtbkHstuPRGL0pYTwUuT/ml38UHm3OvTMCqegK2Xc7rqFlug0thFK/ez35uozz+sPr3f7+NXpO0v3z+Uq7eP1/eln/ApKsujVZd5bVdFAKZa8/PcqDqpxWdj97Uvmv8VAC4pkw+vXb+TqmqV/+53Pv5xeRTEnU/f3mrgAhPWb+8/bIC5vzy1vTL8aeFSv3zL5/yaoyan3/5nU7b+9co6BZiQOpPX9/P38mChb8vzeLVV+PEs++8gDOzOgLEf9Bv+bxEfyf3bpKvr8U/V/WH1Z9TXvT5TyDvK/h8QPfPyQIbgJ1vn65VVv78zqOpQMh4ZRD9/Ms/IhukUXDLs7b7b9H9y4twCmIeWOvdJL98eLrvr6v1u27faf5jtjUImH9FE7D8G7vvhvpHtJ+e/TvSeQay8rsv/5Tcn21Y/+fqL/9Qt//bhg+r+MsbF+UgZxvPz6PPq9+eIfKXn8LfL/70178B0v+UjFH1TfCk8LXwyiyO2u7r17/81D4v//TXv/zU1yCKI6/42jf5n9H8M7s++fzBgu+rfv7jXsDfKm9lNZar7zm0+q2q/0fzt0+rs5dn4e/X28+rHzNx+axXixLfmL5M8EM2tkDWH+z4y9vfAPKUQJs+eN4G+PFv/7Y6ZEFTtVXcrYyg6rsVcHCXFdEivJlmADXbJ2o0EbBrmwHDvq8D8b94eJEYgOGv/yt4wvvH4B3eoScwf32h8tcXKn/9AZV//bQyAdmqyZKsBKCr06fTl9JLAPguLOsmaqNmADDlT130EWz7uBwsGP7rP6H89UnkUz39+qwT2Qv1dFZaEK/t8+jTotslBXj/0iQA8B49oqAH9PMqAMLEGYDqpQC0VT4AxFzs0N6yPF+FGcCUbkH6hTaw1eeF2K+//up7bfqlfEE0tnqVshYCC76Ls/r4EWgV51mSdl/KKEir1U+//e2n1f9e/d92PYkvPE6gVLx7AkgoG0d1BTKrL8CypbQBSPfCpyd++9u7bQGZEpRC4LcszqLXZhCZtyj8ZmhjR39Et/jKj4D1gHGLumq6peBl3aeVFK++ywuYLreWypBWbbcKozoqw6gEBbhLPaDOd0uWVbdqgR/aGFTQvo2eXH/1G+8pYgFS3Ot+XR3YE6hDVQ7+W8R8LgKbqzID5v8eBq/rgEjzU7tivpH4tFKXWFzVXuPVaeO984i9l1+Wcv6+HRD3VmU0fimXghstpnpGyMs8YBGwTPDu0o+Lz5cuA6DAq1fovq3xlmppPqtm86Vs34Pea6JnZwFEmVZJn4VLKfiP95Bq06rPw6f9gKQLpXcvhO9eecag9Q9bFvbHbufZHay+9CiMbFb/XzVGixFoUdR5kTZ5bsWrpu68nLM0h4sTX/0k4PoU55mIv/ct37DpG0R/KfMMRFoz/cdr5dOl72tesNc3wAM6rT/pg3gCBlnoPsN9Cd+mWRLF+1J+qwUfgMxP4APmAtgAcmcJ2W8Ml7vfJE0BACznv/cF7/ZdnAJCelX3PnDMKo6i0PeCG5BqceI3v4LYjxbjjWkWpH/QajE7sBigvwJCZCAJQb349B2fX3e/if6Hja/2Z9nybA17kLHNkwCQI1oEXMJlzDoAXF736sWBnp+fRIAaRd0tuvsgWICmr4tRE937rM26BR9fdo1qAM0fl++XpsvV6FGDNAHGAslQ98C6z/RZIqYAzQ2QASAIyKYiK0GxB0Z5N8KToFcsWACw9r0bfVF8Xn5XKHrm3FKlvm1cFFn2LIV/FQPRwZXpR8gw/yxMAL1iWfHk+/eR9p3bQnuBzRZAH+D47e6rQ/j0KvKvLmL1je7n/zLs/PyvzUPPsm39MQA+r9Kuq9vPEPQqtd8q7SeAANBL1vZVdT++Uv7jK+U//pDyfyD70vjz6l8T7Q8k3lPj8wr5BH+Cl1v799B6/wBLsB8Z5+Nmuful1KPfERWwrxapFr9NC1Z8K3/floAamDQAeMDiVzlslyo6gsL9xH/ghC/lj7G+5BooL2WyxGZb/YABzz4AxP3LZ9/LFLhVdoB3uPSMSbTMac/MaKO3z2Wf5x/eAChG/3w+WypRscRzuwx1IHNAB9Zl0fPsCQ+Pbjn844R7fB54+acVFwEoytsfY+69fiz184fUeOkIdAsAhw+rRZx2qXdAx4X5klZeC+IUyLbo0k31IvxrlFuav1fDBNC5Gv+rPNxSJJrFegvbJ8xd+zBZMtwDJnwy+4+VZRwEkLtFtVzwFnAtQD8AbCg4QEziT9k+i8fXV/H4E75Lxfmxviycn2H8YRV9Sj49Wf4p3e+N7n8legFdxkInrD4vBffDO5yBbzCcfFh9nzOAEd8nv+eQXvZgqP7LMuMsXn1uWQ7AHvD1fdP3Hyv86O2vfybXE/O+LpH3ip+/l05dsAxg/eLTvyufQGbAN+yD6F37f5LQH1EYxT/C24/o5tMjbx9/Yigg0RO0QelblPvdar/LXj2HtUV2oGv3+m3htzcQ0t7i5fegfu/2wXKAcR/bpc+BQNoDhuD8laDg3r86B7xvb1MPNKJgf4DH2yjEcC/aehuPokgCJmEipCJyg8FIgKMoiVIRQiFohPsYHgXbkNpsyRgjtuiGCChA75XlX5deLltEWpgCS3wEQBH9fhtcCt91ecm+GOr72LHo/K7Sb28+vgErd5tWol8fFqIQH9oQ/iTv1jYM6Y+RLhWX39j9etC5TYzU+EMY3ayZd6jbiA7L6UKX6bgi7/dyEbQc7UvaWpPJydzem7vv5XvLO47UdishHJ9kPd43+Dq0ERONtiOy3h+V8dZL+H6icsWV28KN/JZvJlOei2JSznkw3axelndGdF4f4hjKiCMOT7Ila9NVCbd5sRW20mbfIokVuTV/eeymfDfWeKXuc26vTMg1Lcyr7/Z8kbnmhqz74RGfoLg84VZBB0Je5edZMu/nSbi7jJufTZ+N3HPo3nJUA63HJYil+jZR1iWyKYWdJmNPnhWZ8a8cfO9JTKqyxsmH84VEJRu/d65xPj0Sch0TBInG8QkrCYIfyQiyUUgM40FA9gRbcmnWtNW5KWXAyL3XSHVjR5YJZaOFxju5T/qcPj/2vFsfiow5IruopyfDs8IkERBG3ub7Ax6X3Gl7ONwSzlD88367sRxhvBiOcaI3qOM6be1VxeYUKnlV83nk6/LFtSP/EAz+mWxuR6TuKKGwVM/RXVlCOmOiuRM+nmGpdo1H1Y59op9qDrq4W7e8VTo6WHgWXlpIFrcS22iCyCf3WHiUvJr7aI2sXSzvzeCkGIZQJ7fJ5hGhPHi3ECZFVlZ9yVBw07vC0h2vD8LVdsfqUScnSrVCsRAIWvMFHsoVm6ytrWXdbsghVqyHbTzKUCr9LR9NyVq4spWkeOumqlwNW3vpvU0VtRAOkJQ4bl73t2xmNpsUm0mT5Uwtqu/FQ5nPVVnfO4NjYeHCSGRmZiXp7Vg03bCu/3DZPspzuhbVuuLXtcdc0s6j6QH1L42bWVlp+G6t75udMrjddB8mOGWpm0JuPIi1aowxyRIlXaFhHhl1i1mFIIW4rfwku8gYK99Udt4MiJ7AMfpoYta/nM+XCg1y+cEcrgdyvbtvqUrvLLmHQmsNueDPt8gLat87ojN3Y+BMG2EzWjPp2NC4W9MqRqJ1Ya417V7CeACZBMROpLi1Wd7JDdGla/+YGYKBbP0scRqlVq5WpsNGqnTnLGLZMc4UyOgh9CC5JHPf3wZ61xSiacB2cxB6XfaagLRNj0uL7Tm1W4kcJiPLyCmr2p1xPORGX8H8SdtpBkPFfMJLkDA7NLrx8orTh4fbSs2IK87h2pbonsfgiNQlw464BjI9gMPDJQ0ZobKT0BU2xzTzjo6v6ABBpt1uv8bmoyAIYrHhDIi6BjeZ09BGFoc7dDceKYVfu2LvY4HrtlskTo1ihz50ukEItvY9bupUx+NbVWh0xTArOhGPogk6no2hUuz+Mj5sNso5pSLHIzFe3c1NtCxENGInPaGUclP36uxM7MTOmuwLgUg4rdsXnJnPYulCd0tVAlg8G+oGPu+z+jBPD3pO7jkiCYemz+IA9i9TckvKzUUybS1Yk0TbR6buZYbB9a678ddm8+gPtTNgdQ4LrSZDSofrUw0Q+WBgR6wU1SsvYS6APDjtEr6bU+a4zhAM1ujGVOKxjRKjBkmPmJodunsxP+6yQ35j+SK1XZYUSapCuvjuG9Ku9MnOM0t/oE5JkvmX5NJvthhDlScPuaomfMVnJU/sgHd3kZFb6wQua4HcbHk8xLePbUS6IwFq6oaXNKIgMlpk+Xr/aP25HEJeQm5FbNd0msXCrVfE8GpmLTNmd5loBLF98Oh8pQSNhM55wpuCgROcpZnTQYNpbcxidjTCaxnbcyFh963TY8PNnZiEk/kjI2fopeKkyQ1lfl/pVghxtVZrPBmRvSezBwaSmFxRRH29ySb1RrPSDVP7ikqmcxEYDcxWzY4numBbe9od47x+g/USe3Zg62RrVmwpdyrYnxuBTYXepXfhhF4V5gZfvD28kWZ5JteBXbdIOJS56CiXi+5s15K8pcT8klobJyCnOSSEXX3gWccuu+sDKlvBIzqEUOgQqOVAg6luum7YVX58GubreVxDa85Bw8IqIguRtvUtVhonYbi9lF/HCOPGkzVZdZn5e1ffn5Von/gctKlzxnS2JNPLd/kMc060P9bKBkS7vetv/Em8GBbc0KVljeZd0c73UqMrYdRz7mYdFTvUIJm6rEOTh4jbnJ3k/fzIKqU6gfQ8ZDMcTlN721QeQwRdut3iD6u9z7RbNenM5/w2R5F9kBGlYJ77XaWfi+7ibPuwQnhOZjS+NnBTVSwV08Yrzvoxx5W7jBVubcRQQb63pYYxhn3ipqloSk7OIvQuX1vMlW6xFrMUqHQSwmBNHpmg+qDXs8Xkd2WTbqxRIFulOl8ngnMvF5Wyw0CB6UaIkJgKz/FZuwaskNzLLMrvd0ff8xOxZknknip3zXCqTTEqtmpI+iykspHyk5sf0yGFBm3T0IqpPCrkrPXOUesrjz/4V2Rku011lsb5vkcqJyK4bhdnd0MQryhIsfM22vNVDZuk4bIMr/JweLnebW9AsFKptDzKNOsgO9uAUbYYElFsmtpMo9mCnXsYah6ZPrmSd/x25lxxj2QOoUJypgJvV95u2xay5e3K857ZO70OH5iMxjdEgduqSmMjf5O6mxWdC7mGzIo1YddgEptvd/uTsjXXxn0o+0BqSEjha+tgUYqC8qijhnyZ31qdlmjuNgZXW9PNsV5LnC+ZYqhv1K2/hnU21u+0VUkQlWNOxnTZgMoauqtbN6xQOQuTs0azGIZgBWm7eBxILDeYo1VAvgCv+UmzHpOaTxSadtgaZJyNRyYna2yHk3Hp4puoTLEBBKI4ugh0pqMRvcGZiAno1TpWlLrRelMXNr1Mp0Y67nFKEHijcOsRq/RAxxlV22/Vg4UewusN0oRZi+3zgZ2YNTpVh/Lm7ds6sQ7xAYHxvhysM+geeO3slp5CpCyWOC2bn/eGdSj7DMn0ZDgaB28mtzH7gB/t7jyh9VWEcM48jVJ8FMTZLY8FRykWBNN7ga+Ti1Geb6YOAtPXdtdHUaM9O9BNXxA7aJiHfYXVoDRuJsK5ieIUD/gRPhXm2GjBUJJ0Ydusx6P8bZ2IF2tbunvOL7N1GM76XVzf9s5dMiyGIsy9dDPYRhBuWc2JggbZVdKbu8NhwuSkrfID4UfBrslNDmHCUryKuKlnSZ1WOe3KGjydDErztQttHOVKNoT1hNQSxhS6huSwjNytpJ/3Uf+QeZQsOo+oJjVVK1GXbT86Qk3EX9QGgGlxSCj+ul5H8S1IuhnULjjUm1kWTOtUDhBJHngbm+V0XwrqsTgprvDoMauHj4F6TE+6fUpP56rQXAbXFPYqwWvdFna75EL4jClJB6VmZhvYEr4WZocHhx1HrN3TkOJrYFAIPt5PQ2YZClreYgYhvfmMsvf4YnUqabfn+mrPYbatg4vlMTz6mO8oZ+W4TgXctpmPvjKBCJ/QAS8lV+9m1Nia2SRzkir65M5zL3mcyjXLWp6PB0Xh8IxhKfqYXBW3I6ZLGp9dw+1P8K41JpODNOXi6VOEHW5OMjT0hAH5IqjVC+OyT+YTIWHHs6Xg68CsqLUecXEcGfi91SlXtQzQ91fzHnk8NOLcYRfzyKMH64F04pU9BnOq0oJMOE4FU1FdiHckvyp3L+ftsE1TBJZSX3so5/GSo0p/e+wzlrxam/NDZnLmMbX1Xmgs9+ZTzkW9nuEiwqsMPYz7Hk8hJ5uow61LByeBITiLdpcSs8hjLObZtWJ4GUhzYAsqiVCmxxjcLel+1P1ULo+GcDTanRy0vV9tuDx7BHgOnA4fBY7VJkKDW9gz9peNFF13wkVzPds81dF4PhMbZ9AvFn64x6XT6lJVT0OMKYzPC/mmpg5SkAYFXV2gVlUx3MHvTK/XZQCt05ucq0jTKPrs8Nv9vD/S5X17785KkyP6zhcVXO6raCOu10xD51W3neJ2bREQycWP44j22nYnezhDhkExz/35rDXkw9eDXVC0bBvCsTzJDF87U94Ixw3SjIoKpiZlliknVMVg3/mxU663oxaPrCT2cUudk016CALKK2T/ivNr/poLDOtVYtT0Xm9yRLBVO01P18J9f0BEH8dsObk6Oyz1A07iamV7PQbo/nJDod3VG5RIU0MTiyKVGDsqvNUAA+HEYbObbICRRT4Zh3At+jHOO6SQHB5cYYbzJLtFYZsIhFxRuTE6W99thnAnPtysO9EKQrnhbaBK+JD0+EUZhtSClHX9WB8Ttsm7yQr0QxH73rG5THefPykhR1jzXdueXNSQwJiqH4wtl/fApwKo2ek63Wm7sGin85roOCct97097E3iXmgCL6Lj8XKkUA33RQoqppPmc3vvbjfjDk0GIxB5+N72+7kWezbg9zzBioiEaY2mor6NXaj02JDk+VjgamiTPMzO82nEzLCvE1j3AQDrHtFu8uOavJYk6UdNZZqpTRP84UismerIDVbu53XIYt0F1dmoEyjsms4hCVp3qu22Ieo31Z6fYbu0yyBEJBmD7pRXm8MxKhIVpuT7fG4wGUoSdtgrLaWIlwuM9bp7PdlnzNMrv4/3dNmBkjA/0jyi/B5RDEgqBpgXSZzeoVY8KS0ryo9TpjqHrggHlkVNyzQFN5HQx0mLTK9Rt5BnrtNr4K1B9xKXJbu1uxlDPbT1T7XcPdQaEcS4IALC9cYxvsbIBVKZNaZt+M1mV1MDcSUwiIsJ8eJZ/KXZQWsdemDV3ZJJz9tF2C3MsyHXeVih5HAyqLTZysXjzo4kk3PAlnG/1vs70V4baodukc1OY72Lqu74eISD5GiAnp+YHiZUtXp/unSiUbskgZ6VmbnvNgTOPdra4RGJO1j3IQQjRORstrp4Pd6wnXQnIZjvQvxE9DUWqASZ01NuCEwJgfAHnxrli5hZGyiZ4HHYJ5Pr7GoJLtOzNMBrIY3nU1/4fqP2lF3Ol3MIKsX8cKhd5QnU1O1wA4n3M34Lh3Ek931KPpJCp7PeZEZ0TQXnEI2a8Son9cn3MIRl+9xMGzm7ojPs2zpZPuL77h6cHTFVMRat4AilcNVea8cLGVxpE7Lbwgzs+EHbBryWxPUk5YYu627DxzsmWRctPlZzY1UyDfrhIqdmHDTBdK2A9GZUpK5weu7TzuUnZun5CugKAoBBxzKaOlY7+pcACk4enXg2VmRsIMX2poEuHDOS8brBhwFhDvZE2/j2KI09rsJbYoyqBCk9hgMjIBbJKWY69jZ8YIrc0D3Cna57Yiz50L7FQmjtNodN37RagPGmaOa7azXUt3BLEmmdB5tzySHehQ+m5hruDrPbbIfmdgTzy9YDs2d/ZzWpJar79UTb7AwQX9hdBFjAUhIOM6cfwlNInMl14VaI2PXhQeJBHVW7jusSz3A27rTt8jLKUBfed7gtOUGyZaLzGKr8RB3d/LotffqoP+jNpT9HW5Sj2ySGzHgL31Cvyg6PzeF6baThnoLJlFs7/O0yBLRKJGIJxGTSDTaYaBnqLgnDFNYYZXxq/fNJbzWIinfUPceOJ2KwbvN+9npor5b29d6UNOieKBJPT3t9nDu0rIc9QMoNFtFzfL5rOmgCs+Go2p696+KjKkc9K3Uj7a+vBS03o6oGRTBI813gG8Tu9M0oNtfbbqSLUIe8ALLwAKWKcE1pu8A1KH3YP4xwk/Fyf9uz+8Y4K5Tjo34QwYko2+tt4YfrSVHimQoc2mjxbcqRGVxnjXnaxhEX7MrUMyprM5JJ6mzw+HFOPJm+htZVxo5Z0WWTb3MalWSHY81BXFUCs7nqBCNw1iNEGe3bfX6/HKceeJR0b1CRDc59oxNrNC1GDomDi3uUJenu3Gg0ROndukap1nQg27jpQLjdVl/HJxVj/OMV9r3z+nKW8UCQUCoN7XK6Ea6VuOH2zkc4DoGRSyWi3o8swcHya32B/Zawj/Z8vOayz4hDMIJOkIouj6KxxH5y5l2stVyCdVTdwhtKw2LS0OeTp6An5oBtA7uvGE+4GUczgTh79LfdRmgjeo9SzlW8nWCY5nyNlGl7AMPa6VbfYUQ+M37fscY4pKL/mKedeKxUTHIQBx06a2uvoQs8I/q2Go9HvNif2uPglqU02J3FPQao5JR572mc1J34HctS+VwmPFKJ83XHkDE8DC5UMdLumK9v/YZGK3uvHcXBQwmDOB8dHI8IAAGwHopZxj22sRp0CNeYvY2I4YlCuJad74aZn+4ZoYTOZbebZBq5VX0a+JYLYbQflKdGvzzWjqr0EcWBbjQ0iSze7K08oymVdkz5Wq2HIGiKco5tl6fme0BPuE5KSUeBCsvqDrGlJex0yvrRolN0o5b92gwjrOhMfBT1M5keTjuVQdeP60m9hHEXJSdcCrm0SzNv19o7BgSXAk14NtT95jYM/i40PSFE+iaGryA5QrNMChaCHufR81QWUnsOZZxTxGiQOMctb3LqFlGwrm37Q3Y/Fp6B9GS//ER47feo6D32YK7ZH1CkFJuLAUr6hRmGvN+ixPVCIYf9rAx8DM8c2tMPmtTXENRSougceW+IPFKF19GIY2xDuAQD64544qHkALtKQqtGF8uzyQgwY9npPctoaPagmjpyke7CPoHcx5u0u/ZMPBXa7DF37SgwWHCabjEtC33Yb/JwTGwi3DU+OaESNfUxFUEXmlROgYZRm5EAgBsVVWROKWpxnbsZ7NbFZGsiHqd0W4aGBzIpTHxrGzLjkEM2BuwElQNfj+IWJNhjfVdTXGrR4qIzjmyK8RRs+0G9jGGGSZ7sbn0BRYZdUkLucZ6do5bQ9NuHt98fkb39d1/qWh7g/D97VvR65PPtfY3no7/ICz8/eX3+b0v01w9vTZABeV5Pw9q8T94fLP3ds7CP/+Rh3rJ5er0l9e2p8esxdOcly5vDb1kZ9m3XTF/B4Nu/7/D7dnnbsF1eSA3A949PLp/8wHeaNdHXrvraRB04elteA1zevojCDAjyfpo032QI398F+orh269RUy8Kvj/oB3phn+BP2Nvf/g/BFCz36y0AAA== -->
