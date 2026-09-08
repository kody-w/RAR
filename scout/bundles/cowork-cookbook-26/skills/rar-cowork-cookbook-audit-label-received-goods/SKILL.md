---
name: "rar-cowork-cookbook-audit-label-received-goods"
description: "Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_label_received_goods", "rar_sha256": "0b67ace1985b0f058e76b87d35ffeec607e0ce56455b0b6f75770e5512be38ae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_label_received_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_label_received_goods_agent.py` and in the RCI capsule.

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

Label received goods Completeness Audit — Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-label-received-goods
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
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 0b67ace1985b0f05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_label_received_goods_agent.py` first:

```bash
python3 audit_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_label_received_goods_agent.py   # or on stdin
python3 audit_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Completeness Audit — Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_label_received_goods',
    "version": '3.0.3',
    "display_name": 'Label received goods Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06d33612d5c026b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit label received goods records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to label received goods. Output an Excel workbook 'audit-label-received-goods-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no label received goods data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads label received goods records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit label received goods in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants label received goods records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditLabelReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditLabelReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916d7PbVrLnV+HeV7W2H6SLnPRqqpYECCYARCIJ0pqSkXPO8Pq77wHvlWzPyLNvqvavpUoiAZzTuX/drYNfX6yuDYv65dOL7ln5amelaRR69crK3RVXDEWdgK8iscHflVPkbR3ZXVvUzcuHF9drnDoq26jIwXaty5uVtao9y/1Y5OkEVmdl6rVe7jXNk1xZpJEzrazOjdpV4a9Sy/ZSsMHxot5zV0FRuM1yWdTgO8pX/JRbWeQ0K5wiV8L/1Dlp5RdAslUA1uer1AusdOXlbdROH8C+tqvzKA8Aq9V2dADlRfin3EPUhmBbE3peuyqBcn6Uu8tSx2q9oKinVZl2i/B6l2UWuHxbCUR0ii5vm1egrDdaizrNy6ef//7hJQK/Xz79+uKkVgNuvawXncRFH+1dnd2iDdiXWnkAFpQTsHIOrgF7oEQGbrmev3q/+rHxUv/D6j//MxmsOmh++vQ5X71/Pr8sf4BxV23ordrCalpgK8cqLTtKgeavq3U6WFPzboBFiwY4KQ9e33b+TqkoV39bnv34xuQ18NofP78UQARrceHnl59WwLqfX+pu+f26UCl//Ok1LQav/vGn3+k0nR17TrsQA1K/fnm/ficLFv6+NPJXX3Rly73zAr6NSg8Q/4N+y+dN9Hdy7yb58rb4x6L8sPo+5UWfvwF538LQBnS/TxbYAOx8eY2LKP/xnUddgAiycsf78ae/IuuEnpOkUdP+t+j+/EY4BNEPrPVukp8+PN339xX0rts3mn/NtgQB8+9oApZ/ZffNUH9F++nZfyCdRiA/v/nyu+S+twH62+rnv9TtX234sPI/v/BeCnKktuzU+7T69RkiP//g/n7zh7//Bkj/X8noRVc7TwpfMiuPfK9pv3z5+YfmefuHv//8Q1eCKPas7EtXp9+j+T27Pvn8yYLvq378817A/5IneTHkq285tPq1KP9H/dvr6mqlkfv7/ebT6o+ZuHyg1aLEV6ZvJvhDNjZA1j/Y8aeX3wDo5ECbznk+BvjxH/+xkiKnLprCb1c6QKp2BRzcRpm3CG+EEQDR5okatQfs2kTAsO/rQPwvHl4kBiD3y/9ynkD/0XkHevgJ0V+e+PzlKz5/eeLzL68rA1As6iiIcgC/2lpRPudWAGB44VbWXuPVC5rbU+t9BIn8cfmxoPkvf030y3P/azn98qwT0RvWadxhwbmmS73XRaNbCED/TX4HYLw3ek4HSKeFA+TwI4DNSxVoirQHOLlo3yRRmq7cCDBrF5BfaAMLfVqI/fLLL7bVhJ/zN2DGV2+lrIHBgm/irD5+BAr5aRSE7efcc8Ji9cOvv/2w+t+rf7XrSXzhoYDa8G5/IOFRP8srkE9dBpYt9Q0AueU+7f/rb+9mBWRyUJ6AtyI/8t42g3hMPPerjfX9+iNGUivbA7YFds3Kom6XUha1r6uDv/omL2C6PFrqQVg07cr1Si93vRwU4Da0gDrfLJkX7aoBQdf4oIx2jffk+otdW08RM5DYVvvLSuIUUH2KFPyziPlcBDYXeQTM/y0C3u4DIvUPzWrzlcTrSl4icFVatVWGtfXOw7fe/LLU9PftgLi1yr3hc75UWG8x1TMd3swDFgHLOO8u/bj4fOkyQO6/NQzt1zXWUiONZ62sP+fNe6hbtfdsL4Ao0yroIncpAP/1HlJNWHSp+7QfkHSh9O4F990rzxgUv9eycH9sdJ6dwOpzhyEosfr/uSdazLHe7bTtbm1s+dVWNrT7m5uWNnFx51tnCSR5ivhMyd/7lq/Y9BWiP+dpBGKunv7rbeXTue9r3mCvq4FBtLX2pA8ia5EZ0H0G/hLIdb2kjPU5/1oLPgDpn8AHfA9QAmTRErxfGS5Pv0oaAihYrn/vC95tvvgIBPeq7Gzgp5Xvea5tOQmQavHpVzeDLPAWywxh5IR/0mpxBbAdoL8CQkQgHUG9eP2Gz29Pv4r+p41v7c+y5dkadiB36ycBIIe3CLhEz+JEIF771pUDPT89iQA1srJddLdB9gBN3256tVd1URO1C1K+2dUrAT5/XL7fNF3uemMJEgYYC6RF2QHrPhNpCY0MNDdABoAlIK+yKAfFHhjl3QhPgla2oEKafu1G3yg+b78r5D2zb6lSXzcuiix7lsK/8oHo4M70R/AwvhcmgF62rHjy/cdI+8Ztob0AaANAEHD8+vStQ3h9K/JvXcTqK91P/zT2/PjvTUbPsn35cwB8WoVtWzafYPit1H6ttK8AEOA3WZu3qvvxiQAfvyLAxycC/Inim7KfVv+eVH8i8Z4Vn1boK/KKLI/E96h6/wAjcB8394/E8vRzrnm/wypgX2QgrBaXTaDMf6uBX5eAQhjUAIfA4rea2CyldADV+1kEgP0/538M8yXNQI3JgyUsm+IP6f9sBkDIv7nrW60Cj/IW8HaXdjHwlunsmRSN9/Ip79L0wwvASO9fTmVLJcqWKG6WKQ7kC0DANvKeV09QGNvl558n3PPzh5W+rngPAFDa/DHS3uvHUj//kBBv6gG1HMDhw8oFRmmWegfUW5gvyWQ1IDpBYC5qtFO5yP02wC0t37LhywCQuRj+WR4ePFzVi+EWXFvsuVBbOV1dL6DWA8O1Vgoq3EWXBJC0WbEIYC2omoGWAFhQuANJ6e9yflaSL2+V5Dusl/Lzx2KzSPCM3w8r7zV4fbL8Lt1vHe4/E72BRmOh4xaflpr74R3HwDeYSj6svg0YwI7vI99zMM87ME3/vAw3i2OfW5YfYA/4+rbp2/9X2N7L378n1xPsvixx9xY9/yidvIAYAPnFrf9QS4HMgK/bOd679n+dyR8xBKM+IuRHjHgd02b8jo2AME+gBuVu0et3g/0udvEc0BaxgZrt2/8n/PoCAtpaHPwe0u8dPlgOcO1js3Q5MMh3wBBcv2UmePZv9P7vO5vQAh0o2IrYFG05HsoypI34CMl4NGUztIuTPiiUDoXQHuJ4JEWQ4LlN+TRJ04hHkihmezhjeYDeW2Z/WZq4aJGGZGkfYVnMJ1AMcV3PxwjXZSiGckgaQyzWtkibZC37960JSI53Fd9UWuz3bQxZTPGu6a8vNkWAlXuiOazfPhzMojZ9o+1JNqGa6u5Nsk5b7XQ17JpeJ6Vh7w60et/Ics3NomZ1g8An+vlkHQCCIwUZ7M6hwK5L+uix89zMg04azePYQvZms97G6Uw2M+lL1KPxJCKAYKa8j4IYSA/TadValpDr+ZDgN2sUd2qUaqIyzetq5GEYDtjRjB4naBM3ISshkelE1oGeE3STWNognKH9nO7VlIjpCjrmGXQYdMcuRXiHXE7KPskoWJhY1s3FQatmY7/LOslA1AbFieYhHLfjjeK8y+1xRHfTmIoRvZPWU+yWfn2VkKkdt+PFNgTJPqmdNl2npoj0pLgL/rS/WTSi3lLGYDQ7d6E+KjVCFA4cZqh1xg++bNYMrZgxCvv4vZpbClJgWBM8Bt9WjEGf4HValHJWSMqj5u/aukoknHmMvir1QyGJsXxV+dpWtaF1qHm6rllHs3eIOnMBL64V/awwkJEZLHUGbaf9qPa8QA2nLTNPOrG3BvYhF8frZVx7vimlrsZVu2TQrpmAZehexFB/RzKttfdvD5ILckLXOblHGmY9M0165bTbpXiICh1wBqWdrxmkH8tD4tTnY5CgtUKp3LSekI0WHbh8do4b/uGxletnLmknOD+l28y6n6TrKGvHai95RnlPJNXC1Km0u7WpaUQ7DQc75yWZEWGZa2sEiZjIFrZwKuZMdx8v122ASv7pgpk6mbGH3Ca33lRAD35dHE46JtYHTcUpDzo1gdPm5AE+BOq1bPtiMjiC2OAz8ItoGN1I70bZuBV5WbU6zyFbbHNgIiPKGZvWsZDYPOzxwbkeKazLnVxWW6i0NrewtdR1j9k30Hpdov3FP6bayRZO/aOdipZBNhybHB1GcMPKocO2UxVoG6EXYuiO/JwKfiTK4Zq5eMP5YMvhYHnkrlAyHsPkmbllJ/6A5gzC5WF093SC8an742ooGBtlNNTqFFRqbn9JVRtXO6XA8mNgxuu9MqZ+f/DvKo6PSS31TBAclTIaodxnDHGwU+cwzamSJps0ofCGE3V0SzSEP2722U3I2iTMa9YjiQDdHaY+6Y6btpB8gr/cjnaiZPFDxkOtgXearFWxHpaK4TYR1D4ewS7JdCERw+v1GFAaF02ur+aFcjjDa4ZiKe9IUkdsENoh3W82nR3Oh5sBoQn2MB8ZJm5nxGM0iTM9voavOwDT6S1AvdOwm6l6c58v0nxVY/VYsxvuyNxLaJ84ZeRD7gMJYIlzr0jlXUtdgayGACLFgGaH5Zl9dk04rEM3M1Vq9Id6g+VJGcc5zUda0OnjTWv4YTuonM9u570K15nFJuIsmZ1qmrlgJeZURpI+QznG2Tx37KaedQYHkVhZFpHDFlXINh3uj2hSq00re4+LobAOVBpNz530fm8W7rXJvN1h7+zmc+kfEyfB6Buq7pIk28KRtg4qPp9rN8Hqc1pTxzVEtnHYk7f+1E+gEEPZychCTXBqP1xTacUT4+zQN8e6Sa3BpilRcDtso+PnLYEkuext1norlTiHEwArYD2+yUc3FQ7ehWQOzC28dcylxCye6/urCnDjgjDKyJpNeYQvlMJSR5Wj6rRygBKuPZ9r25BoUbqPJXHkBvyI5qTHFR06G71zmrvctGGrd/LgSnPxld8i9kBG0m6D9KdhbeO54u4O13Tns8e9qz+wpK62bnxZNyERVeRcsbd62EZzQG51FhKEcBvLxm7GLxcWkXxmK+3jTWXHe3NnIBJWGl6P0401avlwwJH1ccK0wjioj/YoiHft4m7mZjiqJ/o8tBZ9kjbngI+rnaQlRMy0pzV3CBC5a6DQR7K7PqNcEEvbuvfLo25wOWue73N92BzvyIUXB8K6oWjEmuIREyzRxgIdxy6pCNFymnNkvtlpGU4j0Nlsaedib44P9xHlqH5RiqZK9JjhoUy3a7dgN7FvCT7ESzTeo8eDI7qyNwV7Az4UGxKEHEkyDWrGzLkPEE/p0QSS80d6jNPr+Ww99kOHHQ5qPx1tZi9PDLuT0tO93FXo5ZLyuwjHB5iUHuoFu/n7OrIi2l2jeDSLaiddNHLEI27fi4CSEFzzyjnMqHSa55q4jPTAhPppf66Y+02E222Uy/293yVSOYyDczbOcZnuJm13mOO4rlmXECzyKk20dLyD6Hxw+7luw5QUKFkRTNLr7uZuwpJ9Qp1HFVcvG+7agQEz4x/zeZiC3FRpUh6isOR3Se8frCvZ40w9MrkNzACK0emutolH4q1UqKZMm+cR3+K7rbbVGFibfQ2TNqdEbjfDNr8MrHc76icN8qGq5jMo7TrhwHNcxNmgD6z7oPCRzfauiZPkpFdpzUZ3tz/5Oqsm14MgXSTxgYpOs30InJrAanQ8zrlqjDBmxwKxkcI74lBEIO0L48KrnDRQ0ObGXOtBPEycYe320cBoV/pUhNGarU5rND2MDRrmx4hYJ+t6KwgInaU1/iiV3f44Bykary9nEKF+RNU5ZoIadnAjpITqEzU/iCMZmIGJYK11CJ2GFx7d42DeqQTfqqh8HcxYk7r6UQrruUUDac1rZwe+jo96BwVIcKiObdpZgrfdKXl7NoK7Nh60G6M70pRmsEFEV3IWMq8gw1BPC429a6RgslynnbxwOhjrPZTo2ObEbs6jZhJRMNbmHUp83hTKzanYQG0IW7obBQp2Mm553NhZaCetpAkIX3g1yUaF7LJne6f2d4SR5/6GmsrGyXaEGjyI3vWmnj5lZ5mN5TQ9cLoL7zv6bOiIc3bHq1RgxqmLCAXbJVGmYkSHnEJ5V1aTMFnH+TgetycD2ihGWRTUZZZPN1YXOXm9qcPztYwyNGykjF5DFqdXU5gPSo9dw1SKr0663QVx6fe7NqXw1KWg9U4wSizu7qJC7PbrcsPN024/aCdWHvfx8eRuiTPO5K5krNEmLdWxhnv1vj4J4iZ6lGY2y25yqokNSgUX7iixJ4M8zLcd263H1iKOVFQRNiNCMLRFeKdod3Z9bA1JlrG7T51xPDJmWXX6lFlnprm9bdFtAkSyLtS5SsN07mGlIQuU8/VrJyfH09qXS2GrHzeXKJm0JI71whERyrxkzl6BLfx4iCsSwS2IpMVrjKJjFQtxM1x4XNAjYbvWq7jcdg2x3gf9Grno21RqBb24JvzO1VGhntDHJeoM3pcljlbd8mBjEXmZ7zoVjipMkE7kWGIhjTMX02YsH6NADHyxpZiQm/DqtsHDEe0vyKUNjw6s5DSC+swIRg3auDxiItP8+Xa6ox3PnMO9btqtdN12xuhNmhzFZ+Ss48LeDkzROBrtRTqFG+S2tnWEz5yG8pTAqrKYBj96KoZm4bZH0VPB2oqu6JQjP0720TzXJwBcIo4RpPg4lx5Sxyd2nZ67bCI5MUiVkxhDxu0wH+/XdNQxT0phcm37zKG6EGKiTnyYwhAtXI97Qj85YZxVVFZG7OZwz7jt/XiYJcuT2NLceJfU7tHNoeqLA41yfJRZvpHpdWGieWjPPrup7T2RCAWZabCVaqXJQX0uYXtXaYX+4hdtRa/dG/8Qqtq17iQFkZlbYLYoJpGxA3oh8SbkZDhU1C1J388F6nqaSYOgTY+Wtd+athRqKHsoH+pQXgtZHC7yY7wlwshdg4qONiIXy65+O0aFeJ+tobGYupIQtNo1aMxkbIbzgn4fadGbwoDFh2p/E3AT53EPOvZYK5JkmaVwJHO3ta6B0apDCX3UHVMRrJDAOCh+MOtCCOFbFTLaeVzrjTOfQmtedy4hpqCaiZJgKXgWbq60otCHancvUgPmbrcNJm3524XlRrSZrlFwz4gRp8u4Mi2KwWwdnjEtQuhTRx33+JqjlJ1+As2ZzsbRBQ+ZaPC218tJNo73PUtrJFeRXrSVYrjYQwQGnzZhyzG6p0pMTZEEWmdM3AV42V6gHK2FEH/A+f5Q3CZND2Pxwl17cX80H/L1cOz8bDjFEZEyGHQnGaPtnbXWnC+KNogQtaWomDHwmwJAfi+ezPVEOO3tjHq5AFxnn/KZv/TX4JjI+LGqZ/U8nGsOJfeqgAvTzinLrHyUkGKN3gVTbao+0UwthjVNtYaQ8yWMEmD4S9A2nwd4K9OiHLtnyeYIkRDQto0E81QL5ka8be8pe0ydxD/ziKMJcYU468icr5gOI/XljrrtoeogzWYuxS4bkMNVcyEdTFrERNfXnkpQoxpJImkpH+GTmKVaNiiD4paPnIR4oGbsWnR31RSKIJMqbKyysHrXOlrIQXUjhrUs0FBrNQHKbrfJxXmX3+0Yeqigckh1VTpwoBblAF9vJ49yushBH9W9m7XQSiJ50yLX+xrOCFqbQf9jlhKr4ToyiCq/d4yNIU9qdtXT3ig1wXdF1VIr0j/ydwxrwXLL8u9muH5YuwA5y2Hb3nbMyVPQO3KEcDO3lS0Z5vnD79Mi7mb3Pt8zNyRQEt+HGuKSVH9jLjOaVyV7Tkj59vDPjz2zvV+jhwCXSJUmHh3criKKdFhDbe3sNsD0pZ44xr7h3Y0e9Uc/bVwwZPQg5aEpZ9LrGgxgRpEL/KkE/ZOKTVZU9Wo+tDZ5LpiM9B+zN2iseKauUw+fDVlOqRO99zJcGCKvTi86bbenu3f1aK/Iw4Le21w4WxXbhnd+GGa3heFO6SGOwaSGPvi9qcBEDsfGphzqspyutAspqSU7h3TjO3WnnyXZFKXbUVX4Qsqg6kAz/iA/TCNw5YrAxXFNHAxdKysigrZxspkMeu7PGHdlH5U8WmiFILGSe1N9w4QzvDdVr+1EeNOt71xr0qADxDNZUYkyZQdif4A0uWqvvVt2eAKGB3d3CW4FKRINK7suZN71x0wKuTvwRxJDMeMQykc+aax6L+2rzA4ddpv78oFFSYZ8zGIfFdleyYv0pMGdXsC3uDxq/hVE6I4CsWrc9ltd5S+RquxzOo/FbkIgyb5X4gGVH1ZMbyKrwLRaDuYTitiiDmMhYHXTLnevUHZubxxYUI9OObyWAuIBHTJPMZ0bEcCR010Ozr1xm8chqS6RcVsPZ2PP7kliDLNLo1KbnGdPB/rKDrrHa8gBR7dzq2rTmI3xfSgl6bG1NrIvG5aU++v2NGFHle0fPDmwlx2f9pxyfyQBC6E9Scn7eKTomopANJb+YVTKAMz4NEEMeb4ho6sJ58nhTO414mZe5RAum/PDlE0BOj8YELMMwVU2TRPVhUF3dUUL63bcjQG5GRATmUDvZB3LVL7KOY8wmeoM9fzgpNFNhL7PzlkskuIdtdloG260UWs9d+1ZGSdT8pkRq1PPhwmYtx3v5qCCS0LWBjQ4WaPEa85ByByrAkikkkw+kCoWzWZRZYrntjrJ85ezbCTO3nhIvVE97tADG/jEOXVbMalvZ+IuJDxEKdRVk6rqEEse741jaqJ6n6AbSBZvR7Pb3tiANwBcT3dPphG2MHXIv7bnx7WglJlWUA2xtwpsjrBVunM40ZUmTQxWd/BsoShVHQeTxHrnXPDTyZOotqRqjBgjv+nZY0UjhWgB+cYM6isxxroUSzrcd65weIS0eSugBZdXxgGPxi7nRfTWasx4quPbWYJkah+N5BTiSB1WuJ04vrbZY7cmzEk6EdUTqIpF1JREgmr9rRtzky+OGnWD5VoBQaLs/XDopGB/OTpIBJ0vN42N97Qf8mdxROXwJjJry1AvntOvg+HqVPp85g94lzctMxWm4cGbrerrObYbHYCuDS4a0mPv2sKJqe9yWlfn6WxHiPRIYKzq7mdGoD0oyNQ9snF0utPvxkUt+MZutkpruPS9G6Fze4rn7eWsx1AH6ecNZONaW5rk40KXwyW2MQGzfEtsSX2T4lmhoT3Kio5pd9SjLbU09m7n1Na6uXVof1udL2mztdiZlxITIe2d1YKh09jdYVoI7jsXLqUM31ebK2wd92dWw9DykNHzBNeJcL9q6nTfEzcwFdPWxsaJNatYp/HBQ8pauCDKSRWAW7fxeLKaUVcHi6zVpgUTU85IRFjiuww/DMwjM+MbifAMRrC4JqdGlwwJXucOPFVp4Tsd5veNsu1PhmIrRhFICdYAm+NS4DJq0wWOEQ4wTJpzCpf4gYc2h6ljW4ybMrP2dkKPMVh6jlx5JF17mbHS+3by9uNVdB22niuq5MneKzaRyZ41ZxyNK2m0/LrB4/X4ONCFs0s9myHYTMTIsL/HMo/Mlquyltn33ORI236Sj/Zua522c2bvddeaGqUVE8gjjvb+Tm54JLiTR5ve3oMtNQ666ssqJAZrQuba4d6yTYLRnuUo1uX+2LP9gFymfQ0LjsM+0I6l1n4QIrLQSNc7HCGEWCl6zzRFTZ2V3dVBSx+2snrurLTDewSli41zZHqYMR3+FKv9bAdshHF4cFHGBttvtsPsuXpLP051eKjiKktau1UaeU4RdnTguBGpsz81sXmzUGvQPB6/31y1dsfehEDNCvNMgI5seds0zKPg7zQOwRtGkajbXvOG7m6XigvxbQpT1tWO6sFRD/4+LXTQG1HpBY7lrWCqG92rIvEQu5J9jlHCEfZmvAfNmBSvHRf0apdhZ6uKvglVV+GHcj9w2uzNjg4RqthWMcpCd/viEV0Omz0aKFyMb2XYk84sHplltU+YQtMDt+5liuUPVDof3G0nXTUuvWgIQ627cLDE3q6zwk9xGDpDvBq40LoxcmbH73HtWClbhph1SGJcjXC7bTG6uxGrNg+yVEZEgUP4wVoRRmy36/X6b397+fDy+2HZy3/j5a7lzOb/2dHR2ynP17c1nud/nuV+evL69N8R5u8fXmonAqK8HYk1aRe8HyP9w4HYx78+zFv2TW/vSH09M347f26tYHlR+CXK3a5p6+lLU6TP9zPADrtrljcMm+UlVAd8//HQ8snqZXnTDyi2vBv1pS2+vL8X+by9vHfhuZHVeu+XwfvZ4IcX9/3NoC84RX7x6nLR8P2cHyiGvyKv+Mtv/we++k0l7y0AAA== -->
