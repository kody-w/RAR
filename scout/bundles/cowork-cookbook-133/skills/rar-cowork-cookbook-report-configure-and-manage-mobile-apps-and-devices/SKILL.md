---
name: "rar-cowork-cookbook-report-configure-and-manage-mobile-apps-and-devices"
description: "Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "855f13c8b6b0d1fb20b930d3fc5b6620361246ba2bf388c9ea24aba454bd18cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_mobile_apps_and_devices_agent.py` and in the RCI capsule.

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

Configure and manage mobile apps and devices Summary Report — Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
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
    "breakdown_dimensions": {
      "description": "Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 855f13c8b6b0d1fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_mobile_apps_and_devices_agent.py` first:

```bash
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_mobile_apps_and_devices_agent.py   # or on stdin
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage mobile apps and devices Summary Report — Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices',
    "version": '3.0.3',
    "display_name": 'Configure and manage mobile apps and devices Summary Report',
    "description": 'Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-configure-and-manage-mobile-apps-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f087610de10b8558',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-mobile-apps-and-devices'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-mobile-apps-and-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where configure and manage mobile apps and devices stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of configure and manage mobile apps and devices for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage mobile apps and devices records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of configure-and-manage-mobile-apps-and-devices activity from Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a summary report of mobile app and device configuration for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of mobile app and device configuration activity from D365 ERP data for a posted period, as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConfigureAndManageMobileAppsAndDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMobileAppsAndDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for by-dimension breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-mobile-apps-and-devices-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConfigureAndManageMobileAppsAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9166bLiWJLmqzC3zSYzWxEhoQ0RZWU2QqAFrSAhgSrKIrXv+wJSTr37HMGNyMyqrJ6p7v41xAIcneO7f+6O9MubM/Rx1b59ftMDp1xxTp4ncdCunNJfMdW9ajPwVmUu+LfyqrJvE3foq7Z7+/DmB53XJnWfVCU4vhuS3O9WzqoNHP9jVebTqhuKwmknsFJXbb+qwoVCmERDG3wE9D8WTulEwceicpMcrNR191z2gzHxAkDK65Mx6adV2FbFaj+VTpF43QojiRX7P3VGXoUVkHMVJWNQrvIgcvJVUPbgwAfAsR/aMikjoMfq8PCCfLWo8tTinvTxSn+J9mG1D3onyT889TWqeo2sujgI+u4TUDB4OEWdB93b57/89cNbAj6/ff7lzcudDiy9nZ9aMd80oktffuojP9WhgTZgaf/SBRDLnTICp+oJmLsE3+ugBfIXYMkPwtX7tx+7IA8/rP7937O700bdT5+/lKv315e35c95KFd9HKz6yun6wF95Tu0AdkDpTys6vztT96774okOeKuMPr1O/kqpqld/Xq79+GLyKQr6H7+8VUAEZ/Hll7efVsCwX97aYfn8aaFS//jTp7y6B+2PP/1KpxvcNPD6hRiQ+tPX9+/vZMHGX7cm4eqrrh2Yd15t4CV1AIj/Rr/l9RL9ndy7Sb6+Nv9Y1R9Wf0x50efPQN5XPLqA7h+TBTYAJ98+pVVS/vjOo61A8DilF/z40z8j68WBl+VJ1/8/0f3Li3AMkgBY690kP314uu+vK+hdt+80/znbGgTMv6IJ2P6N3XdD/TPaT8/+Hek8KUHOffPlH5L7owPQn1d/+ae6/UcHPqzCL2/7IAfZ2zpuHnxe/fIMkb/84P+6+MNf/wZI/1/J6NXQek8KXwGmJGHQ9V+//uWH7rn8w1//8sNQgygOnOLr0OZ/RPOP7Prk8zsLvu/68fdnAf9LmZXVvVx9z6HVL1X9P9q/fVqZTp74v653n1e/zcTlBa0WJb4xfZngN9nYAVl/Y8ef3v4GkKgE2gze8zLAj3/7t5WceG3VVWG/0r1q6FfAwX1SBIvwRpx0K/B3QY02AHbtEmDY930g/hcPLxIDdP75f3lPxP/ovSM+/ELur99h+yuAya8v2P76gu2vC2w/l99h++dPKwOwqtokSkoAyWda074sB8p+EaNugy5oRwBd7tQHH0GGf1w+rJJy9fN/gtvXJ+FP9fTzE8GTFzqeGWFBxm7Ig0+LDawYVIiXxh4oCMEj8AbAM688IGAI6HZLyeiqfATIutiry5I8X/kJwB5Q7KYnbWDTzwuxn3/+2XW6+Ev5gnJs9aqCHQw2fBdn9fEj0DTMkyjuv5SBF1erH3752w+r/736j049iS88NFBi3j0GJDzqqrICGTgUYBtwJnA/gJenx37527u9AZkSlG3g3yRMgtdhEMFZ4H8zvs7TH1GCXLkBMDoweLEYeymRSf9pJYSr7/K+1+ulgsRV16/8oA5KPyi9CVB1gDrfLVlW/aoDYdqFoJIOXfDk+rPbOk8RCwAFTv/zSmY0UK+qHPy3iPncBA5XZQLM/z00XuuASPtDt9p9I/FppSwxu6qd1qnj1nnnETovvywNwPtxQNxZlcH9S7kU6mAx1TOBXuYBm4BlvHeXflx8DpoR0AOUfveN93OPs1RV41ld2y9l954cTru4wgPFAjCNhsRfSsaf3kOqi6sh95/2A5IulN694L975RmD3xuFZzC9onr1iurVEtXP5W+tz3t7snr1GKsvA4qs8dX/by3WYhaa484HjjYO+9VBMc63l7uWTnNx66s5fQpYta/U/LXj+YZq38D9S5knIPba6U+vnU8nv+95ASawig8A6fykDyIMuGuh+0yAJaDbdkkd50v5rYoAoVdPyAQxANACZNMSxN8YLle/SRoDSFi+/9pRPAOm9Re1QZCv6sHNQQCGQeC7jpcBqRYvfnMtyIZg8d49Trz4d1otBgcOBvRXQIgEpCWoNJ++I/vr6jfRf3fw1TgtR55N5QByuH0SAHIEi4CLQxZXAfH6V2MP9Pz8JALUKOp+0d0FWQQ0fS0GbdAMSZf0C2K+7BrUAMA/Lu8vTZfV4FGDxAHGAulRD8C6z4RaYqUAbRGQAQQ6yK8iKUGbAIzyboQnQadY0AGg73sf+6L4XH5XKHhm4VLfvh1cFFnOLC3DK5SdcvotiBh/FCaAXrHsePL9+0j7zm2hvQBpB8AQcPx29dVbfHq1B6/+Y/WN7ud/mJx+/NeGq2fBv/w+AD6v4r6vu88w/CrS32r0JwBj8EvW7r1ef/xXMOB3rF5W+Lz618T9HYn3dPm8Wn9CPiHLJek93N5fwDrMx93tI75c/VKeg19xF7CvChBviy8n0CB8L5LftoBKGbUAhsDmV9Hsllp7B+X9WSWAY76Uv43/Jf9AESqjJV676je48OwWQC68/Pi9mIFLZQ94+0sHGgXLFPjMli54+1wOef7hDUBk8K9Pf0v9KpaY75YREmQX6O/6JHh+c4G0mQ+y+qsPYrrsXm3dL383X++/X3vGIMi577tX3yksWg4AQABYgKrttP1SBj8A7fogqhYsBidBo1MDKs8uEBwB5QnI10/1otVrYlx6zCeuPfp/lEN9fnDyT++43v02Wd5L4dIK/CanX44AonlA7Q8rH0jTLZIARywWWfDA6bKnXn8oy7PwfH0Vnj8wzFKtflubnn3Gqx460RMCPqyCT9Gn1UWX2T9k8L3b/kfqFmhhFoJ+9Xmp5h/ekRG8gwkJWPbbsAPUeh8/n78clAOY7P+yDFqL859Hlg/gDHj7fuj7jyhu8PbXP5LrCZ9fl4B9hd3fS6cssAjKxmLlv6vBQGbA1x+84F37/wQ2fEQRlPyIEB9R/NMj7x5/aDxgu6Ty/1E2rXr+QvG6/BufVOWfgK1CZ8hB+vXVU/Zi6TNBmCyVtP7dOWcEMbbg+h/wBsyf9QhU9cXYv3rxV1tWzwn2KWbu9K8fXH55A5nogCh03nPxfQQC2wF8f+yWpg4G6AUYgu8vnAHX/juGo3eSXeyAThzQpAgiXGMe5ZIu4q9DF0XcLYb4WOgRLkmiCEauUZx0HdQNMYrytoGD4o7r4ATu+mvK8wC9F4B9XZrZZBFzkRFY5yPAwODXy2DJf9fvpc9ivO+z2GKHdzUBHJE42MnjnUC/Xgy8Xbsba+NOyhVqyeGW302xsS/Vcdt3LNLOt1hzmZOAoPpe7fMEpzP1LOB5m3RanvG3wx2hxyoPbyKUz3N0r7NGorIQq/xKpvMusWU0VAlMU9PdzHPnqfV3xTjlkygI2OGYJfv8fHL7W2RocjbNNyoNzgV/qYbZa+Uj1axxaVZNFpJCGJ6uActz+u18Fmp/p7Bs3cVXJ+1aRZQul5t7FXbKqbBr7mhZZyaB96lTHyJJlaRBSUTbwVG80N1d3eFrVZQkAhLyDQWrGJ7mScsHzYhfmluSOV10MIRe5jiZvXWTASnIztmwpOOfjsNRJM6eVOubg2lOXXNH5cct66I0sikIhxp1Pmf+rhVPY78/udp1syZDuG2gW2gcMJ7cdtpmM8+Pm76umbtlHS6s3bJXdSNwyi1et4eTbUcidpKxeytLqezTLOHS9nGUkweWy7N3yJn+It8ret61t/kAQeFYXO+nej6WXcnHie+xjOoTxk6wT5zxuAwVsxd6CaTE7RZ0zSjvu1N/lRB/EGfMitbwaTs9rhkr6nHMn5n8EiDEiQtyvMv2nalPRXSOd2GUnA1BzNammOWtCXX4VQrREy5yt4x1I4HD70eoZRlpc5K6eTM1gbVV7179OBYJYxBmcnH081xGuHWUWM5JaHZ/E5NJVVjLYvYyedvBqW+f7D7YHSxZshterj04lziVIUverPGpmCb0ALeSReo8lcvF/X5kLoV1zs/7Zve4VtHwSA8IGDOmaZNpWWEUMrUvS8xg5ttJVXYAjyWk0sjGR8XdQXHp2y0zJglyrtM9ElzbrRREXG+yC5Pd0DgyyLxiHW5dgeywwaBJHnXRf6gFyxYDu3YazKpNQmTYjeBt8IpMqrnTH0Iz8jxqyiEWFfgJGu8sRMUDc7yVnlCcEOk6mOTu2IZ9eoEO0JBM2rlTozVxK9IycHjHoNE0KFoqDIWTjUKDzZzuh/s27bNyF3S2rGmiOjIqBTndWoI7LUuLYNTigUoCipemq3jPYYaKqE4ynLv0EGJzeJzoSKLmqN1KJwePgta8EaeI4nHmmFfSdmROIe0kxJHZZev0OHvSGuFIYRgvzcBv+x0yhaIMoYfJabJjNR4qSdohcaNe2kYxd85ug4fDFRsTKAC9zs71pDN+rlGcmg4ZonoH1C6TGNncYDmgTClpw2F98a0Mqa9muobbx92bx57TXNhIM2yDd76lOWjuTGfJlqa9K5FteXGm+aik5NquYKEeL0fxch5zbOgJO2wKxHFIz9e6OWjgnO0U8RYGG84xDYZqHciMSt64eh12sOrsMiHb+AB1lq/MyD2rLxDBuvE9otKDVpebODyaj85WJUi84I0o452LsSbhQDVnFhFUQ4akYVKei5SB516D9RLPlce256mGPjRm+DgKWAonD9GUqeZk368ylG8Lk9TDwV2jzll3dEU5nKcqCNU1amwRxIrwLYPXnMrDGUk1mBoc540TqzEvu9MDoiMsZsfCOm2GbStfeM2rh9ny1jvJjXZuWRxuzIwFD3rq5eO4FyhazKrrce8hrKXP2TQNSo6bJW/bFE9Rzjk9lxfvdNU0SM95FQ6KkIX4Xb7r7dnGzhCoPpy1DXVZ0tTDrsd1pB4McSxxNcmvikrNeHkfR3e0oR1n19eQPcdpyioH78HuDtw9tyxHKjWfE3KMC8dEQgNXUp2N56RBNFxvRrOdHNuEIlkpz5TEEtRxwwicWq9vjFIc6AutPh4il8WVrTFs0qc41s4QvitlR+SsPb03UjH23BNvDMJwZnaBTSnd7mxYCJqPVp3gx4QuL2eu0LHDnNW3S3fg8mSNIWKCQOn5WJkHUIr8dmvlaiLe2GFTqF7k53oSha0fj/XVktZep1RrYZDEXWfUnteBNro/SM7tUJA2HF7XFDS6XU/XFcqEyTz45+O5ZqlDkTutwlfgQEXSQt2b+AYblIJPjU5Q0AfD7a2Y2G4Db+Qfa5bq+TPedKWxISe/uJTq9SIQRBEy7S3a7WchT4T9wGf2ka11TECv0xx1B8qQ0Ct5MhqmQFNi6+0vhovzOWXZBhsnaRiI1Ekn92fKQ1p6Ux3uBsKcTCSb6cqHEyJKjv6UWht/f6jX4llkYY2zDrUU477KIfA6r/cPm8n2TSUh2wOvalaQZ9CVMD37YVPYwQacUByUY4LfkHly2nmWcx0vM5Rn5932tI7F+4gnp1g0p40Q6o2SbEo5YJk06qx9JvPCxhdpKLxKoKra7mmnhLlgHtkxE0L7ASHi8CgkC0kPD8XTJhNBiGafcFEnqld+QylQst7fyT1hs3aQwDhecahI0VbfVmPSPBhhl0XX9DDN6fXAWB2C6zyPtBcjP9WpyTZmkaMXXbTo81CyMoOUx+KQwNsrSdL0nhmaQlLFyTRpnaV2UlpSXLpzxp19vIhujPbi3p3S7M481EiEtSQVxdyOrYmrmjk7HjTkBJBcc4rx0bRnQXXgXSVxdO35p3SQoBY5e3erEzMGb92WIzc2LqpCmF4zpELODOFZ9/NpwoczSgy3uKnzu5/MeG/ddWHf2Cl9i9REJogmQepTsPfpFI/QPb4LEXKfbblLdGMJSeAelplcJ9CWe2IVZsi8Zl1Zt9JEQQ8WoCy02WWMtuNJQh6KeCGjW/NAGWbOLpziF1rN37GHQ+viAW5meCOC0sybZ3QWuQNkmle3zzb8LbdO1b0loYvCol5q5nQI5k6ORDe3srwPzplR9aYaZ3Wf6T6JuxvVsNWTl8EB5pOhSt5wb0OJ9tmTLVJM4Zujy/KgIGy1Zmu2Tyde18XSfgiH5kYx4bWqnMmae47bJoeEvQlrkbFrvTfbGyEhOw85mOVjzO5H22QlmeCTjRgp8gEtA0Xbw62IBkzGiPMUAPDx0ujmMfBB0oRbuDu0CHYIuuyIGPEWRshbInB9tlU4RcNd+rE+ybhsaE6H2Ztu7dsyowsKw+j3tvIai4jgNaM0+wf0QAx359yxtbEdIe04VZ2CGpWS9dreZEBR0jGMNKYj7fUpJZcPNGiYLIIiXr8IpS8N5sOHQ9G7OGmpyaK5n7JjIeZ+lBz0WrokB/yEtE2Db1nslu7a7O7ZWXYyZYgRmfzE6jc+7ye3KrdGGKxRYdP4kBRERDw+JI610o69nCS0291MLp+lPW1AhrfP7YQ0AQp4W4ARuoogqe+l9+Bo33sXlJATHSRmwzsnCKq4IinyjheE0+3BnlVmz1YChXuqoxbQbiwYNNCzoUPRCSfQM2mYrYvWM1pWsMWzV1efsh6WDj3qj9e4OXZTTSFxygqNNOWZYPBHGidzoxVoPz9zl0qyMU3XEuOBBNpI3D3Nzii41jDR58KCxirNvB1Q/4ElneoG/j66kqYm+gJ34jmHr4eoojudy65Iu7+Mg6Djk1Ftp3FnMgzTyjvkcFtDPR+JLqi2u4Ge9Ky5PgDOHi3C3u1otMPvU+yeixMvH65UXGBSsk0Dy3RGPOKHjSuGbkXQdF2fBaTX6Dy9EdaFb0uDqRSPBvy9yG3w6mZDysXeXnVcwiVbvnl6XrBmFcZcDW9ZhcR1pWXvzqYuCBS/XAHazPeZ83EjhHTyVEl7ysxlVTDFfn1u51aCEAw0jHYxu6zM9rx73TTSRn+kaFcwhnzUr2v7Xj2Oe4K2SflwvxuZNomMpo3TQPl8CoMgdgn1Tuoyw4Bxhm25mBQ9jhYeG1rwBBY38XD3kDaETVO+GjGi0BJsvT5dGdihJypIBEoIHzxN27veCrpDPo7wtYQjY3ffrEd6zXmiICkxoyWE7WrcJUaubD1nHlSApqZApkYroNvOomVn9NYnhrbatd6cMSlLaoswC0uDi8JQYNDIymwqHU6FFabncDxgCBLsh5OoC8LdZDR5S0pzMSCS7htkLRa9sYZ2xDrLMisXfV3UZbs4PcY9bZpYYiasVMTW2qswoS9RkgwuMx/RmzWXpMiJmVRIkyfLCBymdPjTDqMuqPiYL8z18EDOxT2pr/bJDRHE5r1M6WG/QtODeZHP/Zo7xr7HVXtYuBHVlu62gX60NlRRYaaCmTA2brHQ1iAXL4c76Fvryya5tHusfHis0LPK5QTqaxrnqex5F928i1S/t69jeobu03ynTrUvPhTIR84w59MZXWO9Qstr6OKjKUUooAi6EStgGwneg1EO9MesjWEU7D3wHoAGi2zCi7TbGUfz2BKaXpxoPzvtM2TsUzUeCw8XaQB/k27vpjO1yxq9EI2KiR0X02kIJXDyaJbq7eK402yfyjSvOCM5YBESHsRCWVsCDdCHWu8FgRDB4A5HWL7P8XHM3HirgumicfJC7cJWqbtOZYdIF9UgQYtTwWpHKNvPwbnZ3oIevsP1Zt+PfPVQUshTfAW0E/pu5mmjNLpdeW1PxEZG9p1RIqRhqNqMrTfBzClYNswbSIDiwxbzxGjjbbEGM8/lpJkMDrsgWdiRImZy1NYTVmO22mO9wU0USW3A3J8OzpBakFluy7zKfEYfLHVUA5464NZks8BlFLdT4MvI12KzvmH1biNZm64ctMKGNnsVjutcteHHue6KwBxyTO8pI2xsimtqzkEC3gj48BDfKvXSEI6oJJHr0Lf8yFkFte3HUX8Mih9C7DVbPwiVfLgHCRc2QzR7Wy0JNF/XIJWB1uX1Op272cWcXdMZd9yL28dFMLJtvXP3+h0OaxiGhhBiYEvuSuHRYVcYL+HUi0eECPt7vvV2YS4qs0DHjiANjtkEQ3rrPGbeD4oNFbR6hRNjGqQTeTWGwT2zKGjS4srBY4jdZ7vHOeQZL7uE5Cw46bo9447lqtv83ImRNvv9jkAPde1AOIwC6JnjUfbcqnh0d3efu+p1LeRtti7HWrsSs58JTJrYoQEbZejXpqLg0R0ecZanJN09ZjKK7UhdYTc5o47aQysoA27RUaYRh8CIlukGDvTYhROve4YirHSr6nA5k53f3RFFoA0adFZCdA6lCMCn2jDdRt7g8bFqbNfB1gwzxHmiHZMUndft1aTKR9hwtlefjpK73d/SuLSxamsTt+3tkRz22uzMNkV4MMt50gOJ2/aQmrGIFffpCAV7esv7iBcjMV0p9PxICna7xfG6prvm4hZwdzF2azuu+Ro5VswNLQ7KyFWdxXexChPcJfPQjoBw9b6Ts7HkPdbQodbWqCatqEDTPGrmp5iU0GN0mwlpapotc3KvRgQ9hkohJ5mj9hE8t012hxGUb9pjw25chwLzI0XsVFHL1S4tBRDjw1WeWd9Kc35ve7PwQIhRLS7+7TqGt8iLN8yotDjSk3AxQC7oe/sMGi1N8o4ADZM9Q21oaFoL7d31b4ZpBvstbW1LvBcIrEcmYqOxloM+sHMWF7xMIrizETZH8jRol1bGJiPVNxmMoiCSZMUjH+p58vv7tA37PCXyC10NorCp9xqXDtzOpuGgh1p1h1nng5Pez6jaJVCzRrNM2+bTRD7u++tAOwE1TGCACraa4xNEuXWNInZNl1hfsOJw5cG8P8NO7s8xSq7Pl5nC2rG+m1RwYHt5Jgn8MB6IbiZET133/Qb0hHCyacdiGzewIMbqiBSRBXALGVSIltG8gaLEkvejKLo0N+4uYLipR1AaRj9otonC7X3PAej3KPUUKxVS4zYUQyqzq+FJ2mQ9s0fgiT2JdZbr7MQ3usltbxvU9ZyYkafy0dg9thGqOuQn8k6nLrvWeYKIQR6mXrutlHs44DcxNtL9xLBpWoNwZKpMV/2tzRBIsIYLPyAcXuDTNDnBySSlTpeXhOW6sWavzTbe6MSNSG4NetdiMXHnEr41214isJgkGX/vmTV6VB9C3J+zaEDH+wnCvDIGQxq+kUW+x+KtqNkYBMttN6PtbRqpe62ZcW1tegM9Kb1092po6wge71k38oyHvopI9uWRt76Fts6j6V3ijDYmkh5v5IO0VFcYYwrtFCeu5UY5Y5RE4wcydAxF1QLZHQt98MlYqQOB1LaQ7zry3enSTNAe/U2hUEpGtEghgs5M9XIKaC6vgqyS5lN15PXTunLiS9xjVmyfrjHnPuaJKzxgyzRdYzaUu6WeiVg5kEc5CRFxrkihTmNrg4CCSm6xE+3Cc56bo7XeV6l84DqadDGZtqm7XCRe5E9bmLzO/lwFFUAQpMBUZ00TLoEmGw7dDKZRxtoeBb2P6mHruDrdg+vWkHyPst01pvP0NThtuJG8gRKY78tcRWRmDuQ9m6VaGfQNheH6Rj4qJEQlQE+DdVu+1altZgXQPYd0Qrrd9+dTIc83ct9eo4CoPQxDd5JH8oI2ZMZekEIvPdClpeo6Q7Q8tDmJ9GnjcTMcHpUBK0qjkLnCpjTZ5C87FDqn2t7ywz6INFLw92d3z1+0W8Pv/MvGHOMHG177xzFUp4CY1s6mcRVyHg8K3Bqd58PlhEGzn8btlrsD6netvoa7CJMe2l3SwSSFOVK7FhojaYqtm1jFFc4RBQvvg64q1TYmoHV3IeeivTDYfY0S7WAO+Lr1KBm/bx4MLFNIyyBBB+r/HoNvEcqjJ8moxjBWtrA1RA06hAWhsAiPqwKvnaZOZwWGzC9wqshg2tnpAZlIgr49meV54w0kqJ9tZ0mcEalqw4Z7Z99HbE3jlbqpocse3wt26Q7HK2iFIexMorDcJ5rXlvB1XEcak2JA80BWt1hyrRs+o6o+pzdWIK03nD9Z8kAZeOBglyaRCv7GKap1UrfQ6EDkNcQon7LA7m5nlzwp7EvsfAQ4uSUxHVIC5H4P/WIXE6aXVCa2LkBRQCCaulUTPRSHE03Tf/7z24e3X28Hvv1Xnphbbg79t92Het1O+vboy/PWZ+D4n5+8Pv+XpPzrh7fWS4CMrztyXT5E7zey/u5+3Mf/xA3OheD0elTt2/3u113+3omWx77fktIfur6dvnZV/nw8Bpxwh255NLRbnh4GNLrf3uF9yQA+OP7r6Zag/dpXX1+3Jpf7cUm5PPgS+MmvX6P3u5Yf3vz3B7C+YiTxNWjrRfn35ymAztgn5BP29rf/A3kqvuazLwAA -->
