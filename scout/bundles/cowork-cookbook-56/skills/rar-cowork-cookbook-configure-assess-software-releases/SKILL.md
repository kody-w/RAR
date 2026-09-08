---
name: "rar-cowork-cookbook-configure-assess-software-releases"
description: "Reads an attached configuration Excel file of assess-software-releases rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, emits a validation workbook, waits for your approval, then applies changes and e"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_assess_software_releases", "rar_sha256": "7258ed2efddf7b26fd6bcae61a874583fc77ecff9846c72dd10f943432fba896", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_assess_software_releases`. The original RAPP
agent is preserved byte-for-byte in `configure_assess_software_releases_agent.py` and in the RCI capsule.

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

Assess software releases Configuration Bulk Setup — Reads an attached configuration Excel file of assess-software-releases rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, emits a validation workbook, waits for your approval, then applies changes and e

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-assess-software-releases
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per assess software releases target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 7258ed2efddf7b26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_assess_software_releases_agent.py` first:

```bash
python3 configure_assess_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_assess_software_releases_agent.py   # or on stdin
python3 configure_assess_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess software releases Configuration Bulk Setup — Reads an attached configuration Excel file of assess-software-releases rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, emits a validation workbook, waits for your approval, then applies changes and e

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-assess-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_assess_software_releases',
    "version": '3.0.3',
    "display_name": 'Assess software releases Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of assess-software-releases rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, emits a validation workbook, waits for your approval, then applies changes and e',
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
        "upstream_slug": 'configure-assess-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-assess-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc375dbc7ccfdb3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/assess-software-releases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-assess-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per assess software releases target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for assess software releases, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per assess software releases target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of assess-software-releases rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, emits a validation workbook, waits for your approval, then applies changes and e', 'example_request': 'Bulk-apply the assess software releases config changes in this Excel file to USMF sandbox — validate first.', 'inputs': [{'description': 'Attached Excel file with one row per assess software releases target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-apply assess software releases configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAssessSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAssessSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per assess software releases target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAssessSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6so2iEWAOzpikAQIxCI2SVDucLEvYhOLWGrqv89B0mtXdVffvj0xn0YOW+JwTu75ZKbh1zena+Oyfvv8pgdOseCcLEvioF44hb/Yln1ZX8FXeXXB34VXFm2duF1b1s3bhzc/aLw6qdqkLMBxLXD8BhxbOG3reHHgz9vDJOpqZ96xYAYvyBZhkgWLMlw4TRM0zcemDNveqYOPdZAFDlha1GXfLJJisRsLJ0+8ZoGu8QX7P/WttPgxCyInWwRFm7TjwtQl9qcPi7uTJb7TgpPBPajH+fyHRZAnLZDl/ebMftZkVuLDonfmm2FZL8ayA4pWVV2CjR8WbRwU82WWAGpe7BRR0DzsEABlg8HJqyxo3j7//LcPbwn4/fb51zcvA4oA5bcvVQP6oZf+Ukt7aQXOZ4Ac2FiNwNoFuK6CGoiQgyU/CBevqx+bIAs/LP7zP6/gdNT89PlLsXh9vrzNf7SumMVctKXTtLOJncpxkwzY49OCznpnBAYM2q4uZu0b4Kwi+vQ8+Z1SWS3+Ot/78cnkUxS0P355K4EID0t9eftpAWzz5a3u5t+fZirVjz99yso+qH/86TudpnPTwGtnYkDqT19f1y+yYOP3rUm4+Kofme2LVx14SRUA4r/Tb/48RX+Re5nk63Pzj2X1YfHnlGd9/grkfYajC+j+OVlgA3Dy7VNaJsWPLx7A80HhFF7w40//jCwIZe+aJU3736L785NwDJIBWOtlEhCmswv+tli+dPtG85+zrUDA/DuagO3v7L4Z6p/Rfnj270hnSQGi/d2Xf0ruzw4s/7r4+Z/q9l8d+LAIv7ztgiwBWeu4WfB58esjRH7+wf+++MPffgOk/yUZHeSx96DwNXeKJAya9uvXn39oHss//O3nH7oKRHHg5F+7Ovszmn9m1wefP1jwtevHP54F/M3iWpR9sfiWQ4tfy+p/1L99WpxmAPq+3nxe/D4T589yMSvxzvRpgt9lYwNk/Z0df3r7DYBPAbTpvMdtgB//8R8LKfHqcsbShe6VXbsADm6TPJiFN+IE4GnzQI16hsgmAYZ97QPxP3t4lhhg8i//y3sA/kfvBfjQO4IHX594/fUdr7++4/UvnxYGoFzWSZQUAJw1+nj8UjgRAOmZa1UHTVDfAVK5Yxt8BAn9cf4xA/wv/5r41wedT9X4ywOGkyf2aVt+xr2my4JPs4bnGbaf+nig/ARD4HWARVZ6zrPeNB+A5k2Z3QFuztZorkmWLfwEIAuoZOODNrDY55nYL7/84jpN/KV4AjW6eJa4BgIbvomz+PgRKBZmSRS3X4rAi8vFD7/+9sPify/+q1MP4jOPI9D35Q8goaAr8gLkV5eDbXPpA8Du+A9//Prby7yATAFqMvBeEs7FaT4M4vMa+O+21vf0RwRfL9wA2BjYN6/KugXov0jaTws+XHyTFzCdb831IS6bduEHVVD4QeGNgKoD1PlmyaJsFw0IwiYcPyy6Jnhw/cWtnYeIOUh0p/1lIW2PoBqVGfhnFvOxCRwuiwSY/1skPNcBkfqHZrF5J/FpIc8Ruaic2qni2nnxCJ2nX0AVej8OiDuLIui/FHPlDWZTPdLjaR6wCVjGe7n046PH8MocYIHfvPN+7HHmmmk8amf9pWheoQ9CDljFKx/9Q9SBjgEUhL+8QqqJyy7zH/YDks6UXl7wX155xOCz7C/eI3jxrZ3Z/qEH2nTZdaEDGKkWXzoEXmGL/5+7podhOE5jONpgdgtGNjTr6bC5kZwd++w9Z7lmwo/k/N7RvKPWO3h/KbIERF89/uW582GU154nIAIs8QECaQ/6IMaAw2a6jxSYQ7quZxmdL8V7lfgwaztDIlAV4AXIpzmM3xnOd98ljQEozNffO4ZHyNT+rCoI80XVuRkIwTAIfNfxrkCqek7jl5tBPjwc2MeJF/9Bq9kxwAGA/gIIMdsYVJJP35D7efdd9D8cfDZG85FH09iBLK4fBIAcwSzg7IQ+aQGYgeB69O1Az88PIkCNvGpn3V3g6PzDazGog1uXNEk7Y+bTrkEFEPvj/P3UdF4NhgqkDjAWSJCqA9Z9pNSMNjloe4AMAFVAhuVJAdoAYJSXER4EnXzGB4C/rz71SfGx/FLoGZFz/Xo/OCsyn5lbgkUIRAcr4+9hxPizMAH08nnHg+/fR9o3bjPtGUobAIeA4/vdZ+/w6Vn+n/3F4p3u538YjH7892anR0E3/xgAnxdx21bNZwh6FuH3GvwJABn0lLX5Xo8//jMk+APlp9KfF/+edH8g8cqOz4vVJ/gTPN8SX9H1+gBjbD9urI/YfPdLoQXfgRawL3MQXrPrRtAAfKuK71tAaYxqgE5g87NKNnNx7QGgPMoC8MOX4vfhPqfbC2E+AA/9DgYe7UHbvNz2rXqBW0ULePtzQxkFn+Y5bBa/Cd4+F12WfXgDcBn8t+a3uUblc1Q389wH8gd0aG0SPK7ewXD+/cehmBkALnogIaLyozMPBQsnBDTmTiwJ+jljHhXlzwD3VcnnSP+GqvP1A2n9WZV2rGbZn2Pe3Bj+oXR8DebS8XU2zz/KRb9Xm9/VlxkqFjNOgWIwD6SvavMnRa0F7UrQPow+iw/qMqAQgCoJFOmC5p/J1gZD+4+iKI8fTvZpsQsAaGfN77PzVX3n7uN3IPIMBRACHvDCh8WzkIHEBWrMDpoByGmuj2r1p7I8KuLXZ0X8R4F2c+38Q9F8tTZO9ACcxY/Bp+jTs5L+5SEaGLWBLdxyABLUTfunPL919P/I8AwaqZmHX36e+Xx4oTP4BlPYh8W3gQpo+hpxZw5B0eVvn3+eh7k5PB9H5h/gDPj6dujb/9O4wdvf/kEuINgD8kHhnGl9F/L71vIxBM4qANLt8/8sfn0DqeAAuzuvZHhNEWA7QMiPzdw5QQAxAHNw/cxtcO//Yr54UWhiB3S3gASB4GTgI0Ho+yHhIuvQX7ueE6xXDklgOImGHkEEXhhSJLb2CMT3V3BIYSiGIqHrkNQa0HtixNe5QUxmqWaRgDE+ApgJvt8GS/5Lnaf4s62+jTOPrH9q9eubu8bAzj3W8PTzs4WWK3eNEK4uuMt6HZSYStcHXdaO9rHdmztblKuh2O5oYYNa6/MVPtKCwV8bHRn0Cm/OirVJrBiPimIb2gQ+3viyMW2jsyd/7FV1I9ryuTKX4ViY3ekokW6x0dlDVGn24T5qnX3At5XGlBDj2E6HFefTOImKeecS/UYwsX6rizCtC4hMpuosbRPW4L1Wj+PmlLj0ClIG47Y5DEksZU11Vu+Sa9Yp167A9hwWmdslwY2lieyi+0CJyyXrQEtsKcK1FmVOAhulz4/iPUxirENr0jI8HTEUgc/sW1VnAVVBV710T+OWhTo9qyGBvLVZlq3kgUeu2bppwHozlhePCHmJHoMEPSTmPbGGG2+6uYOdXD3SnZTGghBdQ8q0Gq1gypZig1rhVKDTYDlyGY8Xi3H5m7zKlMtmb3uxnN7bSbDtSZXQfuec9m2SChcvbXksNzsSgqejTWdWaUfq5nw+qURc2EtPQq92NVZFU+yrZPKyreLhkh7tz3jBHVZnk6Fu1RjdHbs6sCc89u37aaRkd+zsPRvXhJFm5g3GtyaH2LgmNx62z1fAGGot6IcsPZD0dRkxIruGxyEb/FWDFTsDichqw/N7V2U4XXRtIyiPm5gqfejm4+51tdPvewU2jZN4cJLtTT5JhNFbfLK6prCMcjjnbROyiO2rRhQGfSRd1MvcSykQZ6zAb/vDSqdOF0nvQbujVVQlZ1BTQYHZwtfjynHCLXMVD7dCuKhOFEpZbnpueT4PV+04Cnrl3VBPq1PPSwgbEcYthooCvS9glnV2yq2wk7tDN5yKXQvmiCEXHYmxje0O9pYKcJauOLm6McvK2Zzj1lHpO+Ke6yAxk8IzqpPOINzJmdy+sfxDFAUj0y0PSn9S/P5S8BtIKqwdaZRqw9oXTIEC+rhhyEvH7HiXLcYzixxV6MC1IBusTDl3uUTlvElKk9FDk2hN0zkamnEbVY3vocm5kSdAlgxcnWSwPpvI1R3ioN6+Q/m2GcNxxzPrQkTXDpT4wa4hTueGowT2usuaNdJsXR1hsYZa8zyJxhc2lQhB2NW+ijF9viFjOjqERLA/LukVm1zw3WpyhRs58rvDxoqHoloianFu2940dHnbstHJrxLnnHKKcYYP/F7cYEx0uUz8ZnccAoSWO+ZEy0lLKe527FnLROwijlcEA8EBcih6/56A6JnM283WtPXuxJzi1Ya1fBU+brfCoTzyZllQdWGepoapr0dicwj3+uqmXisR2U4jMfQQITirwJe7IwnRRDjodXSX7vHEOSdjszra6oU8YIow8hjIK2Y7RuZEm1hCUjAcCwVSy/Dg2c4lNoLTJlddO6XX3sUza7Vai9bSJc7cbXu/2uyNPly5Q0vKLOZMjHK8nN11cTeyyWlw6KYbbH/bSmxAhozItWY6DvSQrL2VyRxqJBd1/HagrpXGW3DM7qou9PxzODQHq8FWHAG6TQ5iO6huFEdMRzffnBhJttXQMgpVIwix91cxzx+mYy5f4lxyrOyuYukuGZSE7NWukQR0a0hSfRXsocyv3W1KhAM9cIHb38JAaQjFjy5pd29L1dGhHamu1pUeykraQ4lOdzfc2+16dH9mjIZb7ZRxjCUnoKlbhytNyPPJzXeczAqi+z5c9+tmecxcWOzoiLWUpYLFU2KK4rAUlhPaJQyIvGMOR5y+W13vN85Pjf4cwZt756259g5vYxugYxVAW71PNtGJw4Sdl8O2flbrTCp5ATftda/GCZXAaE3gmNJdp6V22Cabsr8jvbQpjpVwv5qckEoHx1/5Og573CjEUYXzMR+MaX/VFOG+4/ENrDv5/hz2NmEcdky5qbUzcoTzktqcxgJtVRHb2+I2iVxnn9bu5SyunKayRFUmHF4mmpYz2QY56+I5MClyWpKKCxMyynIWK9eFZVNRZi6Nw007KGZB8DAy4OpaZLe0iHhIuF9OvakS5HqIJie4MiyL+ccQuL3tqeUe0yvnWCLSxc6ES4lqx6NsjJrFKLzcjAG0mfTOZvlKlU/rFqs3h4h3J7WPlfLgOsdI7mUtvF/5KZ1c63a48OxwLFRui0X7JebA6wi0/T69HvO4VTGe3XTbIy8F8aCJeRb1oqtUqWqK9jiyRSDvbOrcZWx4g9ms0IgV1vtlxvRtg21SRRn3h/sWQhWUXwn47hTWSwO37IC6HFfcjt5IYS8ntwbTz8m+JSX10HSI2uO0FUW2eCnSYg9C8pRWlxZTQEEbrroq71Sdl1guavq7TN3RQyd0PD2Ip7TgNUM3zvvdOqCzgy56l1EG1Fv6RjNyc+fZbXlNYGTCedox0ZV26k0yK1lKyeMOVPx9Xqe7NEu3NN3ap0u/ZsdO77rdfWnftnZW6MCV9+gGZ0ziXu2zeELZIJMlNb0p2hr3Drm2OlmaYjaGsxTHO+0yesVfx9rcS/463EN2IotXJ9X7jlkLCcmVAc/d7Hpf49wE6mxyPZmOG/VUxyEcJnYiMxoTi5inwc4txBk6IcG39E6hzTY8Vu0aQs6qwI8EvYkaS48m/sQ2MBVSum7ifDZoAKsnuUiu8s5jIck9J/xFjIebGrRujzlo78KrLUbrIZtlocznp9HHjhuaMYoj611qsVY8l2+ZM4WeT+sDCxllLGASK/Q7Mli1bHYWgio41ZPApK5EauN+n4lqkkfFxGVq2mrChlZ81jOOuqvuDnZiJ8l6I+5SthtaHuI60diy2pZSwr6yEZ4OrVS+neWhd8gqNSfGRKkYq+8d6I2QK3W3kylSaehIuTbl6YKU8C09xS65Qy10ndKkEk2Qp1aH3rsQDSWLoPyhbLOMbOmOyUyr7UB+qrw1R5aY+tX1qheUZQu8jFqHzSHb0yi6PoiW2RBadreicksyTmtkZZKjaSMVBL10tmPTxZOwN88tvVqr/mmHG9U6AdB3zTZ4sVqB1KicLmUiorFOWyYmLccyT1hmHCh52KeCvhYG/44HjmTQqyar+KGG7h5+Mw/b3RURApfE4agrua3AR1EsWKerAMILDtmzXO4GwlgL9bhUxS4nRChERzv2z+edDF+ZneKrJLyE2/vdhMxxMyIhZi/TbWWmwoa65oNO5eszd5ELCjLy1JROcQo3nRmLendx8c2o8Q5s5tFO7XAiYi54VYqogq9Oe3VV63BByMcDl+66jVG72xJd0RhziBTdK0z/NnSjQFWBuz6TJzmhsBt+uahEMVagtQ+oc6XVxNbM9YjT6AMOWVq5MZa1rJl6o/tubZlBRtZHJCr7fXqcOOsGEMc8pCByttNtJeda2VITBvN5mCaVSWDoxXKvLXaQcKZZySv6YoCYU7F4aRWqqBollw1bJTqvmPNpGC7w9lJWxG60iPJ4sVZZI28t9ejQiDpCq410EpdI6/tJHpBNrAJQPkrHnJGHXRDSN2hlsqCrHgJ4md3bjW93qDZFhCsn1yHGGUiWuf4W43p7y+78fluSvQcfDOFy6pAatm4wPBK5dMj5pD/UeXu+0zbt+qzixIyXQapbs2vNaUARFjp0sG73tSUwDTfJm53c10fWcHYyNEClnToRE93ROJOR480/W8SJ5E/RkuaX4tCy2hXC1bNANXXgSs1gIzCN76agcpADxDHknoJgb4Wb46iWLZQW0JmbqN48snsYr2qlkFZltNlQeV+tNWzYbSiuKkjT0W6sfAtgmYaXothtpWjnboIzzd9KfiWliKXVdw/WeCWnaCGrd4i446RQWA7p1ZeIYhNIMmaymrqvHFKsI7aiyUYuWjVTxv50LC8nLDVtBXbM1SVkbz3Um6V9rrozX1IjfbJZwiOSrNhwh/EStnf2kqwsAPSK5eoXAiMLvJvC+6XqvBVGe2Sk3iT1vln6ChxNtomBShOpKB6sVFvO61qMrMk7QLbprd3aDwQssm3UIDOy37kEi94PgXzrjEs8mCE1+BS3R89n0c8svUnONr6aBEWoUitwwXTV3aFRul2xVNb07aiXIxjGhOsQrJRkM96wpbvfYrXPwJNkc8raDPHwWkZ3/3iEtv4RObaHdXpLXEY88UPux8Xp1GMeS3AQomimepDW2wMnmw2P3kucOK0zVnQtzrdrqeP6dtibXRvVbuk6oMtWKySr67N2Z/TDyRBPxp7yswQSYtVbg2YTteEQalsUH4vtqMBdeZJUlm+dE6ol0hn2yG2iOubeFESGoJJqz6cbO87C2rS1HSKgtiWtAb24KU+NuA9ZCDrp/AiAcIMq6nXP2Siyr6FxK3i23VVmTI0o6p9kfTT1APKXhqOC5KN2pbTXQnWt5ogWUNBBUJeqtfMlT1dFwZF3xio6UqiZVOPVU3E/3SpEeYk9V9C2FnekzvBmlBtEtSE3Iqp2Y5jyhnGW2rqqDpHPQmimHjaJZyFHLCQtMgozpg1h+8Al2uh4wy4bDn6ElsYGt6RST4WbpCTIuEd81qhIShKtwS2GpOIM985QDE1OU1tMy0Mz3K1xEs0tbPeF71bJsSITarLdQnEOyCqyj83O8fbbBoyA7roJLXWZONTNoLpCUYkNDl8IOxTrcjqP4b6wCqVbYmRd7Cr3GmpKOdbo6uhGJGFKlNPKE1DdzfHx2lJsm9+uEKRYnEnI4i3rYZwyxoLaYVEBqaPj3Du6AG4JQ7+Hx4K/r4RmvcoxojXgOizTNjz0pmDIjssKHrTdW7GZtQEaWNIy99eSiIuGE+ZFWJH35GJBPrK8HYzlrt5dVH8SMnyFbZg44NLGX273JQzmcNrewRO0XFPQ0jguE2x18G8aKDynEKvJXbu16fxAIKw2lBcjoXVkn+gdXE08SUqDlWWNh/N7VD02TthksBdUK0XZNw6/8Q8cUiTH0jmqe0EKO+AhHII7rZPP1DHJbAw/rrbDvVVytMfWu1WjxQda2rYXQqp6YtqztCC5MIfaB4KgNK+FbkbhFWA070aGtlYQsV+v1wTZ9df0xonKFEkG0U6cAVqD66QHgpluLlEnxj4FpyHlUyhJbdypruMSOR6LsnW1MtBKyEjalRyeUmrNpUMSwXnEjBZtjpayR9EirbsJDhhf2tBaW4cmf1gzAe/lh6N7PLf+fsSybRlUwylyGNQTnVQjXLRchfjOdodR2hypYMTbYQsxtlcbWOwSfHKqmJjNGy3xOGMdTLcsrbZdxOyO3MG6oFCRZJVgq1N4Po2BpdzAyEYmmqRelEBlQY8fKnHNGPebXggXtlGwkEZsmanFCc1o0O42II336DQF1BKHuiXUbE4qOWpyABpQtLqjDKNfouXQdTI+SXtyFy3F+nbtoTW+Q047bdJEecnc78JBNY4EBtX0ktvLKz8pz9jOQjyVDFmKie/NZSs39Xrw7a2GJ3vphqNubrVmAsvT3tUyr+0cGdUN3Tx48OVURGK2ifdhmtbb9bYYyKbN7e4oKPlwj0PWQuvpci7EfKM45OT6qqf4plGwSik3newIN4MELQRnOZ6HcFxJdufS9+4BOXl0vDvxhREGS6LhNjYNdSlUSJfqtrXGfUQGnqDtTHcl8NBFOO38dXy6WzQo2V3IcalGSQ5FHYs2NNBDW1LkelphFDtMBEySSnXxMKpr6JMEHdneI+mluN3k14GEGxqNjqZNpLLi+O26RpZoYoX32G5qCjuM5r2m6A28XWar9UWEjItYImKn6+d2T7NSnapO02vTURFCIbhNFZPuKt/DCMaabjFhXOViilAqbVGCh3IzdBxY8faB3W2Q7SaTiEPAy6a4phDe6cPN7agW8rJcyrcjhpONmPKb1XDZSPc0j/Vjl/cJw+N4EFRX3gpHzVgfwCgIl9a6GTUiJ3rGsSWmulyac7pWN/ggHHubrZCay0gzX2IG4sF5TzWcuFfksbOYFcKPEJLfrWSt7pdjzPW71QBm62BLq2Z6lREf2e6XN5TKd41lpHpJDj5Hl9D9nrdjOGxabsWG1WUyDKblEBlFAmxydXJ/COVzQtD44G/0u7gCa3fX0/F7LWqtRbjn5Um+ZTI/nhUwn6b5KGKQDECNl+1i6DgqxpVNUCDZVBT1JkNBamwo9YwDLIfGUbFazgoMHufS9XqpLwlPRY+4CFNlzV6P2Ej7eoUbTBUcLEKHV7BTu4xtgOFneyWFJSkpHlZ1WEPa+SU943C9kVfrLvKzS8bf01299tCxzrDQ6whPsxQ5NBEHOV9kxhZu1hWOQo0msFhwNh4iDuQRv6AlBedXDhIOhnt1g8hrr2tySq22bk0cFCioO53BrDHYJ94+iutbtuyCsUWIaoctA0xLUGrbRqMRN2g+SuME4j5PtKLH5QOG4CPVpQge38GYBXDd8S3KuQDjT4HE3EdfcDnGOTBT7u51fzl1x1a8ApqCu/eCSOtVyWva3WYrboLGZ7ANjqMjSSt7rSaVg1pzDUpA5xg+p/sBjsEcYMTONF2K/cWv41BNR9N3yy4mMpbc36JlI4nhKduD5Jqy+7nv1Ol0qtD2Tqp7qg0w9KgYYjgZ6L6rm8vQ9ksMZwhM2HuhNETcNU+J2+pyuZ3MgjXlNcq6rkucLnhRx95qWrIFcZr29dmRe+G+QW+C3fkdtkp9xMfjS1Is7bi+CAPcJ1RnCKpW5VMMiWh5N30R6uIbscptioNXV34/hj3pSJmq7sz6Mnpwr/m0xpAr86wWiIr6+7oHQ6MyuO353CQCRkQobkhaKyCqcitK7Mhulmakr023uBTinrzxu+COyIjhbuUQIaDmtG7aTRruj8dOllridsKPh9RTl1mZ+gGRkSzFA523YoBlsOAPopqW2/U+Lu+7rrMHMgRzCk5yOI15Q5BdcJm+uIagRCRdphfyrKB1aTSi1Y4xKNyat1y2GClCw/oO5Yqp0jT917++fXibH4O+Hgj/Gy+nzc+M/p89nno+ZXp/x+TxfC9w/M8PXp//HaH+9uGt9hIg0vMxXJN10etx1t89hPv4r18qmM+Pz3e+3p/iPp+et040vxD9lhR+17T1CATKHm+ZgBNu18xvUDbzS7Ye+P79Q8pvLMFvx3++JxLUX9vy6/MJ5LyeFPMrJIGffL+MXg8nP7z5r/ecvqJr/GtQV7O6r1cVgJboJ/gT+vbb/wFolJsU3C4AAA== -->
