---
name: "rar-cowork-cookbook-audit-develop-chart-of-accounts-strategy"
description: "Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_chart_of_accounts_strategy", "rar_sha256": "c6d72a802ef05deef5d437b6061906ddd8882d8734426a088ff6611fef52b6bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_chart_of_accounts_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_chart_of_accounts_strategy_agent.py` and in the RCI capsule.

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

Develop chart of accounts strategy Completeness Audit — Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy
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
      "description": "Date range used to judge stale records; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 c6d72a802ef05dee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_chart_of_accounts_strategy_agent.py` first:

```bash
python3 audit_develop_chart_of_accounts_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_chart_of_accounts_strategy_agent.py   # or on stdin
python3 audit_develop_chart_of_accounts_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop chart of accounts strategy Completeness Audit — Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_chart_of_accounts_strategy',
    "version": '3.0.2',
    "display_name": 'Develop chart of accounts strategy Completeness Audit',
    "description": 'Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-chart-of-accounts-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bd71e090e5059b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-chart-of-accounts-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-develop-chart-of-accounts-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop chart of accounts strategy records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop chart of accounts strategy. Output an Excel workbook 'audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop chart of accounts strategy data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop chart of accounts strategy records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work', 'example_request': 'Audit chart of accounts strategy records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of chart of accounts strategy records in D365 ERP via the Cowork plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopChartOfAccountsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopChartOfAccountsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopChartOfAccountsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6so2CLG640aMxCaEALFKUO5wsYPYNyFUt/77HCS9dlV3dU/3xHwaOWwJOCf3fDLTh1/f3KFPqvbt85seuuWCd/M8TcJ24ZbBgq7Gqs3AV5V54O/Cr8q+Tb2hr9ru7cNbEHZ+m9Z9WpVg+2YI0r5b+Inb9osqWri+Xw0luNP1rduH8bRoQ79qg26RlgtmKt0i9bvFGscW3P/UaWnxYx7Gbr4Iyz7tp4WpS9xPi6hqF0XadWkZL6I0zIPuAyDn5uEiACTBhZe7Zbb4nSDgXlq6fp9ew48vUm0YhW1Y+vP6Wau6ylN/WlzTKndfW9qwH9py5uKC327wsSrzacHe/DBfzCYAyoY3t6jzsHv7/PNfP7yl4Pfb51/f/NztunflmfAa5lVNzxZQos1Lf/2lPqABhI3B4noCFi/BdR22QMMC3ArCaPG6+rEL8+jD4j//MxvdNu5++vylXLw+X97mP9pQLvokXPSV2/VhsPDd2vXSHKj6abHJR3fqXvp0QBtgfKDWp+fO75SqevFf87Mfn0w+xWH/45e3CojwMMmXt58WwPRf3tph/v1pplL/+NOnvBrD9sefvtPpBu8S+v1MDEj96evr+kUWLPy+NI0WX/UjS794gWBI6xAQ/51+8+cp+ovcyyRfn4t/rOoPiz+nPOvzX0DeZyR4gO6fkwU2ADvfPl2qtPzxxaOtrmHpgvj48ad/RNZPQj/L067/l+j+/CScgEAC1nqZ5KcPD/f9dbF86faN5j9mW4OA+Xc0Acvf2X0z1D+i/fDs35DO0zLsvvnyT8n92Yblfy1+/oe6/bMNHxbRlzcmzEGytq6Xh58Xvz5C5Ocfgu83f/jrb4D0/5GMXg2t/6DwtXDLNAq7/uvXn3/oHrd/+OvPPww1iOLQLb4Obf5nNP/Mrg8+f7Dga9WPf9wL+JtlVlZjufiWQ4tfq/p/tL99Wlhungbf73efF7/PxPmzXMxKvDN9muB32dgBWX9nx5/efgMAVAJtBv/xGODHf/zHQkr9tuqqqF/oAHj6BXBwnxbhLLyRpAB1uwdqtACk2i4Fhn2tA/E/e3iWGKD2L//Lf4D+R/8F+pA7Q9vX4IltXx/w/rWKvr7D+9d3eP/l08IA9Ks2jQEC5wttczx+Kd0YoPDMu27DLmyvAK+8qQ8/grT+OP+Yi8Ev/yqLrw9qn+rplweQp08c1GhhxsBuyMNPs7anJCxfuvmgooW30B8Ao7zygVRRmocPwO+q/AowdLZMl6V5vghSgDKgsk0P2sB6n2div/zyi+d2yZfyCdrrxbPSdBBY8E2cxcePQL0oT+Ok/1KGflItfvj1tx8W/734Z7sexGceR1BDXr4BEu51RV6AXBuKcK6es6MBkDx88+tvLyMDMiWo0cCTKSiLz80gVrMweLe4vtt8RDB84YXA0sDKRV21/Vzg0v7TQogW3+QFTOdHc61Iqq4HtbQOywCUywlQdYE63yxZVv2iAwHZRdOHxdCFD66/eK37ELGY/db/spDoI6hMVQ7+mcV8LAKbqzIF5v8WD8/7gEj7Q7fYvpP4tJDn6FzUbuvWSeu+eETu0y+gIr1vB8TdRRmOX8q5EoezqR6p8jQPWAQs479c+nH2OehdCoALz+6jf1/jzvXTeNTR9kvZvdLAbcNHrwJEmRbxkAZzcfjLK6S6pBry4GE/IOlM6eWF4OWVRwy+WoF/1g3R1Sx5D8QA3n/0D4svAwKv0MX/z53UbJwNz2ssvzFYZsHKhmY/nTY3l7Nzn/3ozG6W+ZGg3zucdxR7B/MvZZ6CCGynvzxXPlz9WvMEyKEFntE22oM+iDPgtJnuIw3msG7bOYHcL+V71QCqLR4QCSIBYAbIqTmU3xnOT98lTQAwzNffO4iXY2bjgFBf1IMHDLSIwjDwXD8DUs0meXczyIlwdu+YpH7yB61m14HQA/QXQIg5FkBl+fQNyZ9P30X/w8ZnozRveTSRA8jk9kEAyDE77uG2Me0BoLn9s5cHen5+EAFqFHU/6+4BbwJNnzeBx5sh7dJHlDztGtYAuz/O309N57vhrQbpA4wFkqQegHUfaTUHQgHaICADiC2QZUVagrYAGOVlhAdBt5gxAmDwq299UnzcfikUPnJxrmfvG2dF5j1zi7CIgOjgzvR7KDH+LEwAvWJe8eD7t5H2jdtMe4bTDkAi4Pj+9NlLfHq2A89+Y/FO9/PfDUs//nvz1KPAm38MgM+LpO/r7jMEPYvye03+BMAMesraPevzx1fx/PgAjY9V9PEdND6+g8Yf6D9V/7z492T8A4lXjnxerD7Bn+D50eEVY68PMAn9cWt/ROenX0ot/A65gH1VgCCbHTiBhuBbfXxfAopk3AIUA4uf9bKby+wIKvujQABvfCl/H/Rz0gHVy3gO0q76HRg8GoUZO5/+eq9j4FHZA97B3GbG4ad5OpvF78K3z+WQ5x/eAKyG//JkN1esYo7vbp4KQSaB3q1Pw8fVAy5u/fzzjxOz8vjh5p8WTAigKe9+H4OvOjPX2d+lylNVoKIPOHx4YvdcF4GqM/M5zdwOxC0I2VmlfqpnHZ5D4Nw2zhu+jmkZVOPfy8OAh4t2NuLM9gF7lyGIw1eheBWdvzwqCsjmopr5uzPcFqBzAMbkbCAo8aeMHyXp67OO/AnnuXj9oWrNBX62/IdF+Cn+9GD5p3S/Ncl/T/QE+pGZTlB9nkvzhxfAgW9Q6j4svs0oHxbvU+PMISwHMJD/PM9Hs18fW+YfYA/4+rbp239/eOHbX/9MrgcKfp1D8BlIfyudPKMbQP/Zq9/L4yPlgMyAbzD44Uv7fzXFPyIwgn+EsY8I+umWd7c/sRgQ7YHnoCrOWn4333clqsfENysBlO6f/0Hx6xuIbnd29yu+XyMDWA7g72M3t0YQAALAEFw/UxY8+78eJl50usQFTSwg5OMBgbgkjIQRjAVhGGEBuiY8HMZXFIwHQUCSJBKQxBpFEdyFSTKKcHy1isBCxMO9ANB7AsDXuQ9MZ9lmwYBJPgIMCb8/BreCl1JPJWaLfZtdZuVfuv365uEoWLlDO2Hz/NAQtfJCBPKmwxk6Y1R6iHtfd1ds6MlyOlVrDrva93S/6cay84SBE++bi5+qtzqLh93aZkd4A2kMlRzhHMLIUTrj+24fXHt7lHZ5lzoSEino2g+lte07a7rwct2spUM0iaM6mbWwhiFxkBLuXOiTqQyBwiKI66oi53YkN0GiQN/ZNQThMgTXEZKk9XXM6LWg3YZ9x5F9jytRilMkxbnQkoIO8EVLODeFL1UopIedly7Jbt2STpqftJRfOhgvQpyYa1rGUhsjc8QtTe8PZC/cej81D0WUnDJtf+HDxNvBKbTlDRWpDXFl1oUY3boOZflMTyJMASLs9xJiGlsr53qpYWsql9h16tKRcoSyhm2DfXCB7evxgiDo9e6tluTxThoYtaSu0GXLheRavyZ7hslMtfa4fZdXUiiiiKCrMXzPpepe8R5q8dxUZIKuIzBrHi6KQzhEHbuditw5RhIZeLQr8SadDvRkX8dVkhuM3Z2PPL5R2I5emQPGb1p0TedkfPDYi99MBHtm9fNSPtln3TP9q2eRXqEvq5Cq836qTqxQaGmWFRs+zOGroDWTSdeefh2d436zOnnYnU17DR/GkjJOHVQf9p1GqBxPbzydxy7BfYsaxNUgpvuxPeW2Yo6WYTGamx5Ehds4xugfaho7rYqV7W3cSTzsx5MjTlg2MhAPGfHFpZJNc9MiWHWv+I05KqphHg8mfjawEyZe18WB4raUXluRyib7k6vmybFaZud8O/WQGB/T7VEzGwR1bqnkLwkM3086DB+ao1Cw3bLZ427rb9cdl431LtZJE7pgmuCeKy4/ysU+v+UmXbkIUum4FXPu6dZu9LXXN3mz19kgifbIwbAPFiF3pGjIkRo59Pm439luqaCek01Rap1p6HZGxyG371y/3FzXLDNqB5ZIpInfOlS21GL4ilBtRKOI5uwKkiolDC2WRRjh09kteH9VZsU24YvELgwBN/ZHayUemJW4ZzLiHlL5jdxVgUx3doANQkuRKjU6HcTX3QRNtAIvy8MOd6Gbf90mVsXchVSO947St5sa7nvlsAtoAe6WHSyRg4WVKl1Jt8wXhDIydt5ItwRbuaed2u+Y6XAa8XMt77GsZLBTRjjKynXutKmwqJiFsnXmmXqzSU+tyx22eEySzL0l9ijoWAZic1rTUwTLF+nk0FNouEadB4Vnd8ZRI1D+RhfL3Rq5UIaI0D0nkNVNP+ahkIsk2dw8WeS1mtbqG4sjnUAJObWrNIzvisC5RXg1JBrr9lrJX6hsUPZrT0ACue0xrMBLCxICm3AsUhqZrBWcMMp1X0UVZxJQ78BqKVcw683eK2W8rnnjmGV9eN+Z9lUHudSbRWGQB2HcbyxTVdM7srw3Rl7u45uy2q73hAgPO1pSdMOpQeyv+uYuZjbU8ia3FYGYOulpyYlmTZa6wEwoOpNBmuv+wHGONtRqOQmRqWrhgJHqzYZOZEVSB9NTCq9qSZ0Q2xRDK2Ufcag6xsqBoTb4meEOHbbpGm1QBMEpCakeDVYG+V35xrbRlOZ626S9tDm1IsjTmjddF2sFqUJp2raZgHOxm3V17pK4DKzlAI2JQEbY0nJzEYKXCpVxqKyMKLneUuXZ217kC3yZpimNVSoO1oqe28uztjy5WAIf8MOK3eUQ4S9lnrgL8lURNvD2ziLmaXBO1kWVKOKOtcW1cNVdTTe6YzHKrbVb296gcReUyJrenjoM5Og1um1tTbgBSBKY6zhmZBKIXqZeBq1sc5rdI9I9vO6IK34xVIelROF61MmkLPYxGEllKdRLa6r7497H6849UQ6LxWaX2ZmaqOzkcqxVV92WFuX7oT3acn9j6YLa5FvdjkIvAe4g0rr0E2STbE05YLAO303yyu9y/F7tcBGWsW6lnAh7PMHe3s9cB1amYwtDxyvRkasVbe37uNwo3qHZirJaYiJa6ISG73ZcwpqYNCnBHSo2B4hIEgTu7BOD3g8oZEUNtiFLfCj38J3srncHcXQb48z2fmdJ7nSjY8YTcmazWbeIborjwfYPpggZQhN0R+yY1DuTk/PyhqNjHQMi1FK+rzClXE8563QTKtBF5hPufiujvpQwhC8c4xNtjOU2OE2xpHA5ral4faBT6cy5e04y+MSVbU0jwyySN/HJtgLnHHuJcan5EQ0yjWnXqqSWJ6zPR6me1ujtRIlruw6t8VLl56Ek61TFIYRnutBiN30C3Sf8TovuPlirt2WjEw4oc3VKb9k+jCR/dbD8dkdfico1pVNKZRubTOnjGBybeHnGbA7yDVKl99nxgkvnRrrFe9PY3VeKGl8aTOZ0Z6jHJU4xTm2mKW2J2CbxImVJNrg6sa5GCPXZduyzeSORht3Ft9ueYzATZSldkItx0KftSd1nzmqvtIOKx8tDGUysEEPEUehiYi+Ym+oKn0MU2ragV0l7O8n4qPPUEZiIpov6xLO7YzHF28qQPKmGs5uvliQnsf65xl372sMZa0tnaGsfeLaRPEefVuR5ZWblKJAnHd5nK+/qSLgrHKGrUnMqopF3v6jyaEITozPMhMlW563iXnLLk4VlsKNsEBCwUR5XwSk+JKSr26PQI3qJpiYVZtxxG7dIYjG3fVyK+g45cyIVNz6H5Q27tLPaZaMTG9rWkWQPSegmqWkoUiCsZN3fs96WhybR4ynrgmuw7PMVS8dror8SqiH52+VNBO1pcLHNyKf2jTA0q60QnZVge7jWID04QimTIsARcYUK7ATT2eFoUaLSx1OTXiL74mopk5URRlzv8ASKSumbd1HOpjY/TlRSCX12HM49XRmaaA9JVaR+GogJnW3jCwxsBFv+Xc+vZhp36s5d3U620PaZx+yH8VjETYNU/qSKqzaWauCArtrXkqcH6Ko6DmTrolvLYspb0uZcJh2YTKJoEJqgICuUnOwu+1PAotAdtNB0HLuIARoqGGpWCssx67iWyXOxVnquaIj4MNGmYJw4h13ppbxbWhd3Q4bmcnDhQfWJZLhDaxLVoduko85gXzmQKsqdgQzEc++K1G8n3twlWTOoXTnpzE1YA41BTEhDBhGrcrtza7I6Scl9nNok0Ed2j2aNxuo06MP1QagDcTuGzuTC+z3TovDaA7MtXAur0MedaUJCeXvOT+mF3fhNXqtKs0nO0HELm+q5VYVplLzYYMpVW2jL0pH9giddVIaBqfV1L48OP2YrAY2bYMygvOPcQmvtlXw8DlzKi4dwb/PLHX9aGuW+0ts1hvpX0ANhGWxRflFf5g6YOk3qutnxZKm2eZujeWN7onm0BH5UbzJUYeqWwLgQn1qHxghVtSaACRFvtLvbdVvn2o5aXWETcyifbq4n3IyPw/Vy4gvEWuPT2JTpMrN2e4NDKzQ9gJK4SXifiQL1xm7LgEli1R+EVY/QunRvC87i7RY/K0znRWtb0YdhLFSmWO/krSmUY+rEdKyd1gRfm1xo7plUS49ZN1YQrHdsLh6cra45COj9QOcIyUSjMo7HjpWSZAnSmoE4Ri2q0tvl9pqd+xt9Ca5FZLFieXKrFeZ3SH8idueTU9nVGIfEGnLq5Fxy1Srkt0J7PLD5rrxiYn1ow5N5ry+mvpOXaJP0lkOfkItudWxT9her1cMb0iFJNZIRJw8gV1km0W5rZHdegkDCV45SngUZriyhsS6ssoLH3uZYSpDqE37Gzs7BO6FUzgfNMmNOyXGv072RuF3k7a3t/XbqZHk8rdJrkm0lRTF1Ri6rWOZ5WVjtT9w9EdF9iuur7elCYVXXq+fisuTrYlM5Eathwtkbz7JbwSIjgwCEsdOlvDRFhV3F8Bzu+6YQPGR99jYSa/BhzWyzyfG9faihDWEiOn2lhWZ3as7dfrmsiKnbarTZlIR6pm49ye5KND+weOJw6hl02xNhGuYlktw1n3aqq52Y9W3NHTIxtehcjyuCOG34huKXRrLdQIxuIUkoeSV+zE7DekeJdMYEqy7RD9ehjtptRTnI2G2211QjiXO6LpV0SEj9qrOIVlgyjyxvdoFeeMgxe8oNEvJSg4ZheQuKJcME523sRRkt5NJVvZsyWx6iYw2fDnCx3N4bLWPyqyRH0XHpqbWUDeeGdeGqPW3JYkcEF6rJhpQRIHcUsdbzEjFrz+nADfIwTivMwrVlu6tBSxUgWa7mExbA5ZIlpGFA4nsX9h65WhomY9p46qyopeGM3GhRTrWUg7K+bVi6isIyEFvxcg72UiZw+5M0TKfrBbGUu9x29XGEMJG77mzljuv75Q3dxYaeuObGUuQ8aBhyTcvU4db4E7cq5cC5rrnrtuUigSZKLBIuWeZfs2y4aBaCBhKeMlZ15U+YxnN8pN79HNmv5Szc1E1o9HhlaZN41m54Mpz3yZAoElqJe0LAFIDcW+UOEMSWD7VB5KQhtx5VpLDiVP1lYDViA+8SqIoCfA3starbMDkiDQlGOkOGqamlup4LEK81D+q9i/hBQaHW8Fo+OwRKKbbrlaDH8VJhg/AmUVmgyg0yqckSld3r6egx2OD2NnJntJ3mIdPaSZaETHsd1JRBu96PurYb9laL80eyJuu7q/vHfW7UF7E2UFYd6DDFL5SUgGkLZ4Tx0AYR0paVveav8RVab93NEEI+VRe3w/6OYu1geJRT8vfj1SXgTtqh64Br9hWHUJexTGK+u0EQ1UekLiEgHvbF8XyG0CbalqhLMEGPLnuvcNf3bYXp20NyUtAmFchQ0s7n1Of33A7S6s2ZooOQJErLvlMrfVPljKtv5bV0HtmskOhN5zsDbhwDRhsMtT+Hg0OC2QRHA+26xZBd69OjagrbJKwp3ke9+47vBNKDedjOMYhSeZmorVIoRZoYJpNWI/wSQ9h6GNLrzhgO43BIdwVEw8vJYba5f9S15ip1Ro4t9w2sBxS8ZE5r0yqlcCmmqE2BbqfZhavDpbeP6OpAXY+thqy3ud77KNBG0vcsGR5TSloSolFR11TIRxA0q13BcasDezl5XGm1FXLKCTALnY7dVI3UxpWJMNWIaF1ZZ5xxtHECnRkVLtHuxkPsyq80NEYJOzVrs2aLTov94ogrRq4wUi7FMKPwuH1et216YeSjykTm7biSdl0pu/JdLEYhqyp2Ra6CeAw68TwRasYUq3J3TwiyEi0SxSYFPjZLCxIzTCqN1f280khhvfeFCWpHgbAIFIrLcoullnusM0HBdhp6OltyAtWd4uiyI0PZHcVJ39kV1YrIM5j2rwC8gtQ+oSSK+JDtHnBnp9g9C09DU8AWnhZRNrZrF3dSdHOIPDkI6NNkrdp1Szu72yG98Ci+IW89R4xegBqWFTK35Uku0a7C2pC8k8jOvsp7O3JjDqvvoOfhqDqXZXd7v4P+Z9AsKdK8MJ8YxlR2Sa4c6oY/t6uui6SDutVSk1/nYSjvfImetlBwgTP7MlUpCu1i1owcjjq3CkdHhsynFpEyR5+Gcax3keMl7I9ej5TZqj3nGN5xGNU3HS6nO1Bjod4fMBULZbWwl2viyt6TFSR2PLb2ybUFmQkIZ4UMarxFsDT1g6vsdAcUFfFoZxClUQte7YccZcL5hFI0UbDrG1+M23aUpVKmwpZHzfBqhfBFq0+D7OO+eq9owsiH8mIMxToY0i0kVcuRyjvySF5spjN3olOolOpW51ULxv8Rp80wP97dhPBY71Zi/pnf7Np4cNWIkekscqx4B6v3BvUN2xyhjC5gblcacGU33aRd4st+rVzEwW+aE6NRe4FE2SMqpShCsBxpFjdUB6W1AMHmHhhFngabXJ1AKCHN1W5QglgiCT8yq73fYCGtquaF3HZtxxwpFYx+Oxs605mGlYd9oi3PR+XMXuUd7NnW0rJ41OcEhEqCrMQL4mTGToA1bGCXm7wRAyiQEbjW78NJzj2nv8s2HqGFbOYV71J3RmIjBPNop1ftlXGySSLvbMW7GA7V+PWKmG6WNK3gyMw7Iz20Q8OgmsYzVuZfGMoL9SXhq2sFY2CqarnsiE4bS68xna0VmrRCzjCv7hlh+L0nEydYBMMrMY7YxT0O+6to5/bqGvjEbYAsmCEbH/azug+McsnZPUPk63Y0NreSUoogD+GY19yTKGu76up3m7LfjK4zukfQk+XQvlDY5eWKKhcc1ZDqfLCUXeQia2tq/Lu3IndCi8HW0rME53jAh3wYQp9B0JrBDSUTb+0yJwEOV5pfgxbN9LTKrVgLlS/uVV6aw10iwvHcGcV28voh9vt2DR+xy2VLwLF+wmKeriWMX61LuUM0uQ9KY0234y2BNWkT99RtJ2zFzodj9m4e82Q0NwmCyudhMryglZU1oktwi3lCdPTuNXkJQ7fDCY9SD3jl6hfkJFZhokdbvDm2R8YQh2aXuku/g2rezFcrOSX5YyNCq/jE3NZ3zFh6qeqcKXeUh/PqUJ2jTewlKFPw3tRwV+8W+DfODCx41fr7sIQcmQlKRDW3V+u+5DJiheSnDvZi6rQtTRfyPeveigRbY8k5veIOmM+FW4ZeqGUfEK4TY1Z6w72pNfZe4A3+td9BtihG2m1Tk80pEVhVXov1mncruovjJmzonXjB9o7CoOiA1zW6gqsDiGafwh1yX4kIS+158VKhxzSOdFr0YK84r0Uw5AhUGCEKcjlvVxCOQZ2DdtSWidbMcQiEnnA1VBFjSlXyy4UKsZzkGOG48RIupvRGaOwgNkws2I6dBZ132wCC7sfRNZlh5HgfulbOstnLSbsrefd8K9eKcmnzQdrZvZnrh2PgL5UbQW5WlT/kO0iNN5u3D2/fD9je/u23yOZTn/9nB0zPc6L3F0EeJ4ihG3x+8Pr874v21w9vrZ8CwZ6Hal0+xK9jqb85Uvv4rx4OzlSm54ta7wfSz4Pu3o3nt5rfwNg+gMXT167KH6+FgB3e0M2vQHbzW7I++P79keiD8XxQ9zgX/tpXX5+vkr3NbyfOr3qEQQo4vy7j1znjh7fg9cbS1zWOfQ3betb19TIBUHH9Cf6EvP32vwGwTHTwmC4AAA== -->
