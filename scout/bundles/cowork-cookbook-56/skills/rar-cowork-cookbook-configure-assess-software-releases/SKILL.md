---
name: "rar-cowork-cookbook-configure-assess-software-releases"
description: "Reads an attached configuration Excel file of assess-software-releases rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, emits a validation workbook, waits for your approval, then applies changes and e"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_assess_software_releases", "rar_sha256": "7258ed2efddf7b26fd6bcae61a874583fc77ecff9846c72dd10f943432fba896", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6so2iEWAOzpikAQIxCI2SVDucLEvYhOLWGrqv89B0mtXdVffvj0xn0YOWwLOyT2fzPTh1zena+Oyfvv8pgdOseCcLEvioF44hb/Yln1ZX8FXeXXB34VXFm2duF1b1s3bhzc/aLw6qdqkLMB2LXD8BmxbOG3reHHgz8vDJOpqZ16xYAYvyBZhkgWLMlw4TRM0zcemDNveqYOPdZAFDri1qMu+WSTFYjcWTp54zQJd4wv2f+pbafFjFkROtgiKNmnHhalL7E8fFncnS3ynBTuDe1CP8/4PiyBPWiDL+8OZ/azJrMSHRe/MD8OyXoxlBxStqroECz8s2jgo5sssAdS82CmioHnYIQDKBoOTV1nQvH3++W8f3hLw++3zr29eBhQBym9fqgb0Qy/9pZb20grszwA5sLAagbULcF0FNRAhB7f8IFy8rn5sgiz8sPjP/7yC3VHz0+cvxeL1+fI2/9G6YhZz0ZZO084mdirHTTJgj08LOuudERgwaLu6mLVvgLOK6NNz53dKZbX46/zsxyeTT1HQ/vjlrQQiPCz15e2nBbDNl7e6m39/mqlUP/70KSv7oP7xp+90ms5NA6+diQGpP319Xb/IgoXflybh4qt+ZLYvXnXgJVUAiP9Ov/nzFP1F7mWSr8/FP5bVh8WfU571+SuQ9xmOLqD752SBDcDOt09pmRQ/vngAzweFU3jBjz/9M7IglL1rljTtf4vuz0/CMUgGYK2XSUCYzi7422L50u0bzX/OtgIB8+9oApa/s/tmqH9G++HZvyOdJQWI9ndf/im5P9uw/Ovi53+q23+14cMi/PK2C7IEZK3jZsHnxa+PEPn5B//7zR/+9hsg/S/J6CCPvQeFr7lTJGHQtF+//vxD87j9w99+/qGrQBQHTv61q7M/o/lndn3w+YMFX6t+/ONewN8srkXZF4tvObT4taz+R/3bp8VpBqDv95vPi99n4vxZLmYl3pk+TfC7bGyArL+z409vvwHwKYA2nfd4DPDjP/5jISVeXc5YutC9smsXwMFtkgez8EacADxtHqhRzxDZJMCwr3Ug/mcPzxIDTP7lf3kPwP/ovQAfekfw4OsTr7++4/XXd7z+5dPCAJTLOomSAoCzRh+PXwonAiA9c63qoAnqO0Aqd2yDjyChP84/ZoD/5V8T//qg86kaf3nAcPLEPm3Lz7jXdFnwadbwPMP2Ux8PlJ9gCLwOsMhKz3nWm+YD0LwpszvAzdkazTXJsoWfAGQBlWx80AYW+zwT++WXX1ynib8UT6BGF88S10BgwTdxFh8/AsXCLIni9ksReHG5+OHX335Y/O/Ff7XrQXzmcQT6vvwBJBR0RV6A/OpysGwufQDYHf/hj19/e5kXkClATQbeS8K5OM2bQXxeA//d1vqe/ojg64UbABsD++ZVWbcA/RdJ+2nBh4tv8gKm86O5PsRl0y78oAoKPyi8EVB1gDrfLFmU7aIBQdiE44dF1wQPrr+4tfMQMQeJ7rS/LKTtEVSjMgP/zGI+FoHNZZEA83+LhOd9QKT+oVls3kl8WshzRC4qp3aquHZePELn6RdQhd63A+LOogj6L8VceYPZVI/0eJoHLAKW8V4u/fjoMbwyB1jgN++8H2ucuWYaj9pZfymaV+iDkANW8cpH/xB1oGMABeEvr5Bq4rLL/If9gKQzpZcX/JdXHjH4LPuL9whefGtntn/ogTZddl3oAEaqxZcOgVfY4v/nrulhGI7TGI42mN2CkQ3NejpsbiRnxz57z1mumfAjOb93NO+o9Q7eX4osAdFXj395rnwY5bXmCYgAS3yAQNqDPogx4LCZ7iMF5pCu61lG50vxXiU+zNrOkAhUBXgB8mkO43eG89N3SWMACvP1947hETK1P6sKwnxRdW4GQjAMAt91vCuQqp7T+OVmkA8PB/Zx4sV/0Gp2DHAAoL8AQsw2BpXk0zfkfj59F/0PG5+N0bzl0TR2IIvrBwEgRzALODuhT1oAZiC4Hn070PPzgwhQI6/aWXcXODr/8LoZ1MGtS5qknTHzadegAoj9cf5+ajrfDYYKpA4wFkiQqgPWfaTUjDY5aHuADABVQIblSQHaAGCUlxEeBJ18xgeAv68+9Unxcful0DMi5/r1vnFWZN4ztwSLEIgO7oy/hxHjz8IE0MvnFQ++fx9p37jNtGcobQAcAo7vT5+9w6dn+X/2F4t3up//YTD68d+bnR4F3fxjAHxexG1bNZ8h6FmE32vwJwBk0FPW5ns9/vjPkOAPlJ9Kf178e9L9gcQrOz4vVp/gT/D8SHxF1+sDjLH9uLE+YvPTL4UWfAdawL7MQXjNrhtBA/CtKr4vAaUxqgE6gcXPKtnMxbUHgPIoC8APX4rfh/ucbi+E+QA89DsYeLQHbfNy27fqBR4VLeDtzw1lFHya57BZ/CZ4+1x0WfbhDcBl8N+a3+Yalc9R3cxzH8gf0KG1SfC4egfD+fcfh2JmALjogYSIyo/OPBQsnBDQmDuxJOjnjHlUlD8D3FclnyP9G6rO1w+k9WdV2rGaZX+OeXNj+IfS8TWYS8fX2Tz/KBf9Xm1+V19mqFjMOAWKwTyQvqrNnxS1FrQrQfsw+iw+qMuAQgCqJFCkC5p/JlsbDO0/iqI8fjjZp8UuAKCdNb/Pzlf1nbuP34HIMxRACHjACx8Wz0IGEheoMTtoBiCnuT6q1Z/K8qiIX58V8R8F2s218w9F89XaONEDcBY/Bp+iT89K+peHaGDUBrZwywFIUDftn/L81tH/I8MzaKRmHn75eebz4YXO4BtMYR8W3wYqoOlrxJ05BEWXv33+eR7m5vB8bJl/gD3g69umb/9P4wZvf/sHuYBgD8gHhXOm9V3I70vLxxA4qwBIt8//s/j1DaSCA+zuvJLhNUWA5QAhPzZz5wQBxADMwfUzt8Gz/4v54kWhiR3Q3QISBIKTgY8Eoe+HhIusQ3/tek6wXjkkgeEkGnoEEXhhSJHY2iMQ31/BIYWhGIqErkNSa0DviRFf5wYxmaXCKSKEKQoJsRUC+34QIpjvk2ty7eEEAjuU6+AuTjnu963XpPBfqj5Vm+34bdR5IMJT41/f3DUGVu6xhqefny20XLlrhHB1wV3W66DEVLo+6LJ2tI/t3tzZolwNxXZHCxvUWp+v8JEWDP7a6MigV3hzVqxNYsV4VBTb0Cbw8caXjWkbnT35Y6+qG9GWz5W5DMfC7E5HiXSLjc4eokqzD/dR6+wDvq00poQYx3Y6rDifxklUzDuX6DeCifVbXYRpXUBkMlVnaZuwBu+1ehw3p8SlV5AyGLfNYUhiKWuqs3qXXLNOuXYFluewyNwuCW4sTWQX3QdKXC5ZB1piSxGutShzEtgofX4U72ESYx1ak5bh6YihCHxm36o6C6gKuuqlexq3LNTpWQ0J5K3NsmwlDzxyzdZNA+43Y3nxiJCX6DFI0ENi3hNruPGmmzvYydUj3UlpLAjRNaRMq9EKpmwpNqgVTgU6DZYjl/F4sRiXv8mrTLls9rYXy+m9nQTbnlQJ7XfOad8mqXDx0pbHcrMjIXg62nRmlXakbs7nk0rEhb30JPRqV2NVNMW+SiYv2yoeLunR/owX3GF1NhnqVo3R3bGrA3vCY9++n0ZKdsfO3rNxTRhpZt5gfGtyiI1rcuNh+3wFjKHWgn7I0gNJX5cRI7JreByywV81WLEzkIisNjy/d1WG00XXNoLyuImp0oduPu5eVzv9vldg0ziJByfZ3uSTRBi9xSerawrLKIdz3jYhi9i+akRh0EfSRb3MvZQCccYK/LY/rHTqdJH0HrRCWkVVcgY1FRSYLXw9rhwn3DJX8XArhIvqRKGU5abnlufzcNWOo6BX3g31tDr1vISwEWHcYqgo0PsCZllnp9wKO7k7dMOp2LVgjhhy0ZEY29juYG+pAGfpipOrG7OsnM05bh2VviPuuQ4SMyk8ozrpDMKdnMntG8s/RFEwMt3yoPQnxe8vBb+BpMLakUapNqx9wRQooI8bhrx0zI532WI8s8hRhQ5cC7LBypRzl0tUzpukNBk9NInWNJ2joRm3UdX4HpqcG3kCZMnA1UkG67OJXN0hDurtO5RvmzEcdzyzLkR07UCJH+wa4nRuOEpgr7usWSPN1tURFmuoNc+TaHxhU4kQhF3tqxjT5xsypqNDSAT745JesckF360mV7iRI787bKx4KKolohbntu1NQ5e3LRud/CpxzimnGGf4wO/FDcZEl8vEb3bHIUBouWNOtJy0lOJux561TMQu4nhFMBAcIIei9+8JiJ7JvN1sTVvvTswpXm1Yy1fh43YrHMojb5YFVRfmaWqY+nokNodwr69u6rUSke00EkMPEYKzCny5O5IQTYSDXkd36R5PnHMyNqujrV7IA6YII4+BvGK2Y2ROtIklJAXDsVAgtQwPnu1cYiM4bXLVtVN67V08s1artWgtXeLM3bb3q83e6MOVO7SkzGLOxCjHy9ldF3cjm5wGh266wfa3rcQGZMiIXGum40APydpbmcyhRnJRx28H6lppvAXH7K7qQs8/h0NzsBpsxRGgE+UgtoPqRnHEdHTzzYmRZFsNLaNQNYIQe38V8/xhOubyJc4lx8ruKpbukkFJyF7tGklAt4Yk1VfBHsr82t2mRDjQAxe4/S0MlIZQ/OiSdve2VB0d2pHqal3poaykPZTodHfDvd2uR/dnxmi41U4Zx1hyApq6dbjShDyf3HzHyawguu/Ddb9ulsfMhcWOjlhLWSpYPCWmKA5LYTmhXcKAyDvmcMTpu9X1fuP81OjPEby5d96aa+/wNrYBOlYBtNX7ZBOdOEzYeTls62e1zqSSF3DTXvdqnFAJjNYEjinddVpqh22yKfs70kub4lgJ96vJCal0cPyVr+Owx41CHFU4H/PBmPZXTRHuOx7fwLqT789hbxPGYceUm1o7I0c4L6nNaSzQVhWxvS1uk8h19mntXs7iymkqS1RlwuFlomk5k22Qsy6eA5MipyWpuDAhoyxnsXJdWDYVZebSONy0g2IWBA8jA66uRXZLi4iHhPvl1JsqQa6HaHKCK8OymH8MgdvbnlruMb1yjiUiXexMuJSodjzKxqhZjMLLzRhAm0nvbJavVPm0brF6c4h4d1L7WCkPrnOM5F7WwvuVn9LJtW6HC88Ox0Lltli0X2IOvI7ASODT6zGPWxXj2U23PfJSEA+amGdRL7pKlaqmaI8jWwTyzqbOXcaGN5jNCo1YYb1fZkzfNtgmVZRxf7hvIVRB+ZWA705hvTRwyw6oy3HF7eiNFPZycmsw/ZzsW1JSD02HqD1OW1Fki5ciLfYgJE9pdWkxBRS04aqr8k7VeYnloqa/y9QdPXRCx9ODeEoLXjN047zfrQM6O+iidxllQL2lbzQjN3ee3ZbXBEYmnKcdE11pp94ks5KllDzuQMXf53W6S7N0S9Otfbr0a3bs9K7b3Zf2bWtnhQ5ceY9ucMYk7tU+iyeUDTJZUtOboq1x75Brq5OlKWZjOEtxvNMuo1f8dazNveSvwz1kJ7J4dVK975i1kJBcGfDcza73Nc5NoM4m15PpuFFPdRzCYWInMqMxsYh5GuzcQpyhExJ8S+8U2mzDY9WuIeSsCvxI0JuosfRo4k9sA1MhpesmzmeDBrB6kovkKu88FpLcc8JfxHi4qUHr9piD9i682mK0HrJZFsp8fhp97LihGaM4st6lFmvFc/mWOVPo+bQ+sJBRxgImsUK/I4NVy2ZnIaiCUz0JTOpKpDbu95moJnlUTFympq0mbGjFZz3jqLvq7mAndpKsN+IuZbuh5SGuE40tq20pJewrG+Hp0Erl21keeoesUnNiTJSKsfregd4IuVJ3O5kilYaOlGtTni5ICd/SU+ySO9RC1ylNKtEEeWp16L0L0VCyCMofyjbLyJbumMy02g7kp8pbc2SJqV9dr3pBWbbAy6h12ByyPY2i64NomQ2hZXcrKrck47RGViY5mjZSQdBLZzs2XTwJe/Pc0qu16p92uFGtEwB912yDF6sVSI3K6VImIhrrtGVi0nIs84RlxoGSh30q6Gth8O944EgGvWqyih9q6O7hN/Ow3V0RIXBJHI66ktsKfBTFgnW6CiC84JA9y+VuIIy1UI9LVexyQoRCdLRj/3zeyfCV2Sm+SsJLuL3fTcgcNyPo+O1luq3MVNhQ13zQqXx95i5yQUFGnprSKU7hpjNjUe8uLr4ZNd6BzTzaqR1ORMwFr0oRVfDVaa+uah0uCPl44NJdtzFqd1uiKxpjDpGie4Xp34ZuFKgqcNdn8iQnFHbDLxeVKMYKtPYBda60mtiauR5xGn3AIUsrN8ayljVTb3TfrS0zyMj6iERlv0+PE2fdAOKYhxREzna6reRcK1tqwmA+D9OkMgkMvVjutcUOEs40K3lFXwwQcyoWL61CFVWj5LJhq0TnFXM+DcMF3l7KitiNFlEeL9Yqa+StpR4dGlFHaLWRTuISaX0/yQOyiVUAykfpmDPysAtC+gatTBZ01UMAL7N7u/HtDtWmiHDl5DrEOAPJMtffYlxvb9md329LsvfggyFcTh1Sw9YNhkcilw45n/SHOm/Pd9qmXZ9VnJjxMkh1a3atOQ0owkKHDtbtvrYEpuEmebOT+/rIGs5OhgaotFMnYqI7Gmcycrz5Z4s4kfwpWtL8UhxaVrtCuHoWqKYOXKkZbASm8d0UVA5ygDiG3FMQ7K1wcxzVsoXSAjpzE9WbR3YP41WtFNKqjDYbKu+rtYYNuw3FVQVpOtqNlW8BLNPwUhS7rRTt3E1wpvlbya+kFLG0+u7BGq/kFC1k9Q4Rd5wUCsshvfoSUWwCScZMVlP3lUOKdcRWNNnIRatmytifjuXlhKWmrcCOubqE7K2HerO0z1V35ktqpE82S3hEkhUb7jBewvbOXpKVBYBesVz9QmBkgXdTeL9UnbfCaI+M1Juk3jdLX4GjyTYxUGkiFcWDlWrLeV2LkTV5B8g2vbVb+4GARbaNGmRG9juXYNH7IZBvnXGJBzOkBp/i9uj5LPqZpTfJ2cZXk6AIVWoFLpiuujs0Srcrlsqavh31cgTDmHAdgpWSbMYbtnT3W6z2GXiSbE5ZmyEeXsvo7h+P0NY/Isf2sE5vicuIJ37I/bg4nXrMYwkOQhTNVA/SenvgZLPh0XuJE6d1xoquxfl2LXVc3w57s2uj2i1dB3TZaoVkdX3W7ox+OBniydhTfpZAQqx6a9BsojYcQm2L4mOxHRW4K0+SyvKtc0K1RDrDHrlNVMfcm4LIEFRS7fl0Y8dZWJu2tkME1LakNaAXN+WpEfchC0EnnR8BEG5QRb3uORtF9jU0bgXPtrvKjKkRRf2TrI+mHkD+0nBUkHzUrpT2Wqiu1RzRAgo6COpStXa+5OmqKDjyzlhFRwo1k2q8eirup1uFKC+x5wra1uKO1BnejHKDqDbkRkTVbgxT3jDOUltX1SHyWQjN1MMm8SzkiIWkRUZhxrQhbB+4RBsdb9hlw8GP0NLY4JZU6qlwk5QEGfeIzxoVSUmiNbjFkFSc4d4ZiqHJaWqLaXlohrs1TqK5he2+8N0qOVZkQk22WyjOAVlF9rHZOd5+24AR0F03oaUuE4e6GVRXKCqxweELYYdiXU7nMdwXVqF0S4ysi13lXkNNKccaXR3diCRMiXJaeQKquzk+XluKbfPbFYIUizMJWbxlPYxTxlhQOywqIHV0nHtHF8AtYej38Fjw95XQrFc5RrQGXIdl2oaH3hQM2XFZwYO2eys2szZAA0ta5v5aEnHRcMK8CCvynlwsyEeWt4Ox3NW7i+pPQoavsA0TB1za+MvtvoTBHE7bO3iClmsKWhrHZYKtDv5NA4XnFGI1uWu3Np0fCITVhvJiJLSO7BO9g6uJJ0lpsLKs8XB+j6rHxgmbDPaCaqUo+8bhN/6BQ4rkWDpHdS9IYQc8hENwp3XymTommY3hx9V2uLdKjvbYerdqtPhAS9v2QkhVT0x7lhYkF+ZQ+0AQlOa10M0ovAKM5t3I0NYKIvbr9Zogu/6a3jhRmSLJINqJM0BrcJ30QDDTzSXqxNin4DSkfAolqY071XVcIsdjUbauVgZaCRlJu5LDU0qtuXRIIjiPmNGizdFS9ihapHU3wQHjSxtaa+vQ5A9rJuC9/HB0j+fW349Yti2DajhFDoN6opNqhIuWqxDf2e4wSpsjFYx4O2whxvZqA4tdgk9OFROzeaMlHmesg+mWpdW2i5jdkTtYFxQqkqwSbHUKz6cxsJQbGNnIRJPUixKoLOjxQyWuGeN+0wvhwjYKFtKILTO1OKEZDdrdBqTxHp2mgFriULeEms1JJUdNDkADilZ3lGH0S7Qcuk7GJ2lP7qKlWN+uPbTGd8hpp02aKC+Z+104qMaRwKCaXnJ7eeUn5RnbWYinkiFLMfG9uWzlpl4Pvr3V8GQv3XDUza3WTGB52rta5rWdI6O6oZsHD76cikjMNvE+TNN6u94WA9m0ud0dBSUf7nHIWmg9Xc6FmG8Uh5xcX/UU3zQKVinlppMd4WaQoIXgLMfzEI4rye5c+t49ICePjncnvjDCYEk03MamoS6FCulS3bbWuI/IwBO0nemuBB66CKedv45Pd4sGJbsLOS7VKMmhqGPRhgZ6aEuKXE8rjGKHiYBJUqkuHkZ1DX2SoCPbeyS9FLeb/DqQcEOj0dG0iVRWHL9d18gSTazwHttNTWGH0bzXFL2Bt8tstb6IkHERS0TsdP3c7mlWqlPVaXptOipCKAS3qWLSXeV7GMFY0y0mjKtcTBFKpS1K8FBuho4DK94+sLsNst1kEnEIeNkU1xTCO324uR3VQl6WS/l2xHCyEVN+sxouG+me5rF+7PI+YXgcD4LqylvhqBnrAxgF4dJaN6NG5ETPOLbEVJdLc07X6gYfhGNvsxVScxlp5kvMQDw476mGE/eKPHYWs0L4EULyu5Ws1f1yjLl+txrAbB1sadVMrzLiI9v98oZS+a6xjFQvycHn6BK63/N2DIdNy63YsLpMhsG0HCKjSIBNrk7uD6F8TggaH/yNfhdX4N7d9XT8XotaaxHueXmSb5nMj2cFzKdpPooYJANQ42W7GDqOinFlExRINhVFvclQkBobSj3jAMuhcVSslrMCg8e5dL1e6kvCU9EjLsJUWbPXIzbSvl7hBlMFB4vQ4RXs1C5jG2D42V5JYUlKiodVHdaQdn5Jzzhcb+TVuov87JLx93RXrz10rDMs9DrC0yxFDk3EQc4XmbGFm3WFo1CjCSwWnI2HiAN5xC9oScH5lYOEg+Fe3SDy2uuanFKrrVsTBwUK6k5nMGsM9om3j+L6li27YGwRotphywDTEpTattFoxA2aj9I4gbjPE63ocfmAIfhIdSmCx3cwZgFcd3yLci7A+FMgMffRF1yOcQ7MlLt73V9O3bEVr4Cm4O69INJ6VfKadrfZipug8Rlsg+PoSNLKXqtJ5aDWXIMS0DmGz+l+gGMwBxixM02XYn/x6zhU09H03bKLiYwl97do2UhieMr2ILmm7H7uO3U6nSq0vZPqnmoDDD0qhhhOBrrv6uYytP0SwxkCE/ZeKA0Rd81T4ra6XG4ns2BNeY2yrusSpwte1LG3mpZsQZymfX125F64b9CbYHd+h61SH/Hx+JIUSzuuL8IA9wnVGYKqVfkUQyJa3k1fhLr4Rqxym+Lg1ZXfj2FPOlKmqjuzvowe3Gs+rTHkyjyrBaKi/r7uwdCoDG57PjeJgBERihuS1gqIqtyKEjuym6UZ6WvTLS6FuCdv/C64IzJiuFs5RAioOa2bdpOG++Oxk6WWuJ3w4yH11GVWpn5AZCRL8UDnrRhgGSz4g6im5Xa9j8v7ruvsgQzBnIKTHE5j3hBkF1ymL64hKBFJl+mFPCtoXRqNaLVjDAq35i2XLUaK0LC+Q7liqjRN//Wvbx/e5iPS12Hxv/Hi2nxm9P/s6Op5yvT+/snj7C9w/M8PXp//HaH+9uGt9hIg0vOIrsm66HWc9XcHdB//9QsH8/7x+T7Y+wnv82S9daL5Zem3pPC7pq1HIFD2eAMF7HC7Zn67splfwPXA9+8PML+xBL8d//kOSVB/bcuvz9PJ+X5SzK+XBH7y/TJ6HVx+ePNf70B9Rdf416CuZnVfrzEALdFP8Cf07bf/A30x4tD4LgAA -->
