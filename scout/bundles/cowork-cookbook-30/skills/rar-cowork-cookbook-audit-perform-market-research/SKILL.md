---
name: "rar-cowork-cookbook-audit-perform-market-research"
description: "Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_market_research", "rar_sha256": "d966a001bbe0948f84299401916982bcbd33b9af45d26090fff10a2f1143ad44", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_market_research`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_market_research_agent.py` and in the RCI capsule.

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

Perform market research Completeness Audit — Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-market-research
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
      "description": "Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 d966a001bbe0948f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_market_research_agent.py` first:

```bash
python3 audit_perform_market_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_market_research_agent.py   # or on stdin
python3 audit_perform_market_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform market research Completeness Audit — Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-market-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_market_research',
    "version": '3.0.3',
    "display_name": 'Perform market research Completeness Audit',
    "description": 'Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-market-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-market-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '944fea706c72b213',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-perform-market-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit perform market research records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to perform market research. Output an Excel workbook 'audit-perform-market-research-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no perform market research data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform market research records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co', 'example_request': 'Audit perform market research records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of perform market research records in D365 ERP via the Cowork plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPerformMarketResearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformMarketResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPerformMarketResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVpbnV9G8jhjbrcyUxCbIjooYBAiBECB25KxIs4PYVwHu+u5zkV6m7WpXdVfE/DVyOIXg3rOf3znnXX59c/ouLpu3z29q4BQr1smyJA6alVP4K6p8lE0KvsrUBf+vvLLomsTtu7Jp3z68+UHrNUnVJWUBtpO9n3TtqgqasGzyVe40adCtmqANnMaLwYVXNn67SooVPRVOnnjtCsbQ1fF/q9Rl9WMWRE62Coou6aaVrl6OP60AGcAxr7KgC4qgbZ8iVWWWeNPrfuIUXvABUO76pkiKaOWAa8f/WBbZtGJGL8hWi/xP0R9JF6/KIli1cQDEAlKuwqTwl12e0wVR2UyrKusBk5Xa50D46X1lGQJmQNlgdBZR2rfPP//1w1sCrt8+//rmZU7bflNefql+eWquvCsOtmZOEYE11QQMXYDf7yYCt/wg/GawH9sgCz+s/v3f04fTRO1Pn78Uq/fPl7flP6UvVl0crLrSabvAB2JXjptkwF6fVmT2cKb23RKLDi3wUxF9eu38jVJZrf6yPPvxxeRTFHQ/fnkrgQjO4sUvbz+tgNG/vDX9cv1poVL9+NOnrHwEzY8//Uan7d174HULMSD1p6/vv9/JgoW/LU3C1VdVZqh3XiAMkioAxH+n3/J5if5O7t0kX1+LfyyrD6s/p7zo8xcg7ysSXUD3z8kCG4Cdb5/uZVL8+M6jKYegWCLox5/+EVkvDrw0S9ruf0T35xfhGIQgsNa7SX768HTfX1frd92+0/zHbCsQMP+KJmD5N3bfDfWPaD89+3ekswSk13df/im5P9uw/svq53+o2z/b8GEVfnmjgywZQNy5WfB59eszRH7+wf/t5g9//Rsg/d+SUcu+8Z4UvuZOkYRB2339+vMP7fP2D3/9+Ye+AlEcOPnXvsn+jOaf2fXJ5w8WfF/14x/3Av56kRblo1h9z6HVr2X1v5q/fVoZTpb4v91vP69+n4nLZ71alPjG9GWC32VjC2T9nR1/evsbwJ0CaNN7z8cAP/7t31aXxGvKtgy7leqVPQDcHmBoHizCa3EC8LZ9okYTALu2CTDs+zoQ/4uHF4kBxP3yf7wn1n/03rF+4yyI9j0TX2j+9Rua//JppQGiZZNESQFwWyFl+UvhRAC/F4bVsq4ZAEi5Uxd8BBQ+LhcL9v/yT+l+fZL4VE2/PME+eSGeQnEL2rV9Fnxa9DLjoHjXwgMlKxgDrwfUs9IDooQJAOmlKLRlNgC0XGzQpkmWrfwE4Em3AP1CG9jp80Lsl19+cZ02/lK84BlevWpauwELvouz+vgR6BRmSRR3X4rAi8vVD7/+7YfVf67+2a4n8YWHDIrEuxeAhLwqiSuQVX0Oli0FEcC54z+98Ovf3i0LyBSgRAGfJWESvDaDqEwD/5uZ1RP5EUKxlRsAQwLT5lXZdEs5S7pPKy5cfZcXMF0eLVUhLttu5QdVUPhBAapoFztAne+WLMpu1YLQa8Ppw6pvgyfXX9zGeYqYg/R2ul9WF0oGNajMwD+LmM9FYHNZJMD834PgdR8QaX5oV4dvJD6txCUOV5XTOFXcOO88QuflF1B7vm0HxJ1VETy+FEupDRZTPZPiZR6wCFjGe3fpx8XnS0sAEODVYXTf1jhLpdSeFbP5UrTvAe80wbMfAaJMq6hP/KUM/Md7SLVx2Wf+035A0oXSuxf8d688Y1D+B20O9fuG5dkVrL700HaHrP5/7o8Wi5AsqzAsqTH0ihE1xX55amkZF4++usxF+EXsZ1b+1sB8A6lvWP2lyBIQds30H6+VT/++r3nhX98Adyik8qQPgmsRF9B9xv4Sy02zZI3zpfhWFD4AwZ8ICNwPgAIk0hK/3xguT79JGgM0WH7/1iC8+2axL4jvVdW7wMarMAh81/FSINVi1W9uLhYjAqM84gR49fdaLd4DZgP0gaFXSyyAwvHpO1C/nn4T/Q8bX33QsuXZI/YgfZsnASBHsAi4eH7xIBCve3XoQM/PTyJAjbzqFt1dkEBA09fNoAnqPmmTbgHLl12DCqD0x+X7pelyNxgrkDPAWCAzqh5Y95lLS1TkoMsBMgA4AamVJwWo+sAo70Z4EnTyBRgA8L63pS+Kz9vvCgXPBFzK1beNiyLLnqUDWIVAdHBn+j1+aH8WJoBevqx48v37SPvObaG9YGgLcBBw/Pb01Sp8elX7Vzux+kb3838ZgX7816akZ/3W/xgAn1dx11Xt583mVXO/ldxPIGk3L1nbV/n9+A4WH19g8fEbWPyB6Evfz6t/TbA/kHhPjM+r3aftp+3ySHgPrPcPsAP18WB/RJanXwol+A1cAfsyB5G1eG0C9f57Jfy2BJTDqAHoBRa/KmO7FNQHqOHPUgBc8KX4faQvmQYqTREtkdmWv0OAZ0sAov7lse8VCzwqOsDbX1rHKPi0TFyL+G3w9rnos+zDG4DT4L8b0paSlC+x3C5zHcgaYPsuCZ6/ntAwdsvlH2de6XnhZJ9WdABgKGt/H2/vhWQppL9Li5eGQDMPcPiw8oFd2qXwAQ0X5ktKOS2IUSDkokk3VYvor3lu6QCXDV8fAJrLx3+VhwYPV81iu4XtE+LuvR8t2e0AAz6Z/cezfIC8zcvlhrMAaw4aA2DBow3E3P8p22f9+fqqP3/Cd6lUfyhRS/1ezP1hFXyKPj1Z/ind793ufyVqgnZjoeOXn5fK++EdysA3mFA+rL4PG8CI7+PfwiEoejBZ/7wMOotXn1uWC7AHfH3f9P3PF27w9tc/k+uJd1+XuHtFz99LJy44BnB+8enf1VIgM+Dr90vxfWr/T5P5I7SFsI9b9COEfBqzdvwTMwF5nnANit6i2m82+03y8jmvLZIDTbvXnxd+fQMB7Sw+fg/p94YfLAfo9rFd2p0NSHnAEPx+JSd49q+NAu+b29gB3ejyJw0Cw5ztdue6wZZA8BBHIIJAtjtihxE45HquD8Mu4YQI6kPYltiGYbjbOlC42yGw4yMIoPfK769LQ5csAqHEPtwSBBQiO2jr+0EIIb6PYzjmoXto6xCug7oo4bi/bU1Bfrxr+dJqMeH3qWSxxruyv765GAJWnpCWI18fakPs3I25dyfB2lhbfMweel3fzNKVbcGA0l5sWNDekDlL3G/HqLNsxk1Vlr+kxriGDsyFhCFOztkQlfdSrmS1emShdA+7EIRcrwcO9dbuZR1O/gWSZfxxGwz3dE5q2J56XjUc/lrd+GN/YApIu8nG2VCNm5uYCnzMwnsBb9bxgOqJPJ8bnT2aytnkdJjF1LUO0ekwopofJmiwkWcCFXSHN9uOqQX1XKMw8MW8m/YMySos5uDplilyc5SOkowQGVuX/Pno71LPrcw0xjOC2aqo5AcyMxpcjsxlI9xuNz/pewQqo9ZwBO8skEeh1WstkZyjV50bV0z4zTkdEyEZRIxa37a33IEeEEs/9vIwzDsU36xnP9nJI9JC+xYlcNzE7jhlH13UvPquxVP52c/PCORd87o3ZpbSYLp51DS2n9qHSEDpRRPIqMW3V9HyHKFlyKm8rkdWCYQWUnItg4/ngeNbSy4S42pRisI0F7qxp7sS1O7ZiaS0MW7KmIG4piZ87PHaQYOkQ63LfXrAxFwOrVrrqVxfrLTfkvO6zUaqM9XUEFgDo/iRK+vZyxCdsXdoa0OFBl93Nd0zpEvGt5Qksh0W4eweiuF1BWe9potnPEDLKK1NfccUulMjUhZdlWNTsRsV2h5MQ2EG7FG6BX0RcWEjnolmq2f22NVRWKcCYV38zDpnk92rFd5nk4gZMpxwhHEg5qNhX/XsZgVXKB7aLjVvTOayBrPhIu6Y+S0yayyCHuAZ19JjXFuqybVN/Nhq+M48Hu4OpVFpcBBGbS1nTFwFkanjkF0UB+N6jkHHGAuVSRqVy7YHwe+h2rQzjoePmGlXYtxZLQTiMNkdDkR69vCdH9fePu7662V9SbYKMkuZPh+JNTnAKf1QBGYfXyb2cMMNVIm2ITQ2IYVAxs20cCJtUS6P8yCkJShwthaXn9XxohmqjdXRozNOh8opYCkOwrG6CY/wTlqnOZY3XIh4UHhX2VuI0ocp1FCNkAb8xD+qzuHOpZ5ecVqFFIdVLqCNVA1PnuZkoKrCT6Not24p5lrTuGLuhc0OP+xC0pnGcxmvkVu6lY4mmvaJvRdo+TSDLL5JvKO7lCRetrUe8IaZn6oz6aCiopVAEilqD1hwoLhqzedXfnhMBUlTm1MOmvO0SNe3QsmgPQNvA8AwdkN6v1fUKrMbM5YOW12NROVoa9dZdCmR5gYyq+QkC5X98Xbbc5ZJVfL8QMWDqmd1HW+yTjrCrgDVStWhRL473da872W3DL+01lXEiRLsuz3YwyiNp8Mtm4+dyJBbWj7yM6xEFUuo0w65XLVYDxRDz30Gle1RSwqyThrmtoZbUZ2DlJvkiaQ42eAZ+YjY9x4unHSWCgTgkZkJZwqrbNxF4jUL+UiZ+o8D45gRqgep4ZqzZqZqm0a0wuQ1XcDA6rArZYIkXnt0LACYSQMLTdm0CXLiaio0izdWJTtZTSMPwTsFtpuLV83PWqRUWeigwtIxRWphcEZS7S7VhkLwwzm93cYyb1tMS4SznzFKMzWhRLl7kb9b97rsSi51Axnra9FIN1tMptc8R2FN1lxk2vPdWSpd7bLnepADiAIfIH5XoAfWUBuoCAqF3ftrl6BmpGQ3mupHnBrDBsyQ0lFPh6MyOAGxvd6t1iCklMp5zFS35Q0SqfPEJmcc9KC6s2e0vSSkCj1vVJNULmoJtx0dW4yt6tyVjktRG+/N/jYy7k7qrD0M0px8gNwWThL1eAgk5OXWVaHPjHnybCw96wc5CoW8UO+gZB0cNdmlQc+Vd4ckE16chUq2L0aVUQlB5uf50SMwq5qF2iNOt2GIkbw0bBJjGBVjd99qeLW12XS2+GYvalnJXo5tDlk8W7IuhO68QiAwb8DIqw7A7TEjijpj8rljS/TitbNrn46n8nLhz0YhFuOm9FQv2JutLUJHiqXX/XoYsrJaB9DdxfnhNOFhCDFaeStSUWFvNxhrIY67jtTBxYvbA99xeeXwNlsTpmdERcKd5gdOuVcGEsOrGznJPuCkTTS7Tn8525fkJJ1OgiBJ9S3WblTApbF81u/NmllXHBVN5xPP1Z7EbKDcYC2fFsS1XD5mTYYeJumXqWmia64uKcUQOUsi8nEzwg+rzJBH1ZbxXSoMJYUzc18c5gso0GK3DiYomouyDPxg4k6gZF+NIr3xj6LDWNu+3jc3v40AxD3i+2QM2UEigEkN9GKJOud46zSpmZNP9tr+ijH8HOzDyJ3ChI65EQ+N2YvX4sGJLp1qMsXxSq/Zo5HNE/D5cGb7eehZhGTrjjuyRigYN75kEtKQmUloq5pthXPHDxvrLFKlVaVRKUhVe8jut0hnfJVS0nK3w9PrBsPhNhZIfb5BDXuZAoWsG+SYyCdEpKguSHTNPHsiqFueO6NUiN+jQ3eHhlKILzM1R7ldzMyRuei6YaW1Ow0+mlK2VwSUbV74KxLEJx3OQkqd9CbKdkLSrFu3AcFRbKIBHZ2tQqEeK03edBkOmTrYY+00aslmt5s1q+dD4Q8Hm6QSD8UadfbE9bgjuZ7vitg0AgaTi47VorDijKQLbjvWr2n/Rmg8nZx2yhFUrpznzfG0pwYuI1Oj5jmG5innsdlG+siHEw9RPJ3qLOgo5Or0gEfnej2TmxIJ2bSwS5pI0l2F7E8321+nORcTkn2lMGEQBLESG8hrEYaUBVC+w/B4yU+Pa3R7dGGw7nC090StuWQWc1bbEwqNXnFEkWCfQMH1kpueDSsQ1EbFFUN3OnUXsyxNcsrmT/zcpNS1j61rhaxV/X4UTMIREoG7NgfWrKYcKj0m3z/WNoXVUBwroBLvDD7ztCKxHzXoOM3JD+fNUB+BQTPRuOX9gJ4OCOuS5Zg8OFbbaI7CTVZxOItHyB9iG7EhukRdXbuHBHklZb2WqKKYg9tFw5TqcCVHnUoON9XQDV/AdQ20vD05BruthlJwPCTFfrMZNOE8wTcpyiEc2SJ8QlR7b1NJ9ZakoPAx+Z4X65qdhCjJV0rdtYMYqAm628isbWGWmNcxf2X2otTfDyS/TR2FAklizMBwKmbM0TSlx15TLAWr1jD+EMxGO41jnbF3CCUPXl0pIPx5MdwmlomTqW1FDsUlU28n5ZabIk0ydmyioqbBezm7dvTD4+6qiuWLUwU90h1zjepuVte7w8mBqlrV+IQbAsbZ4ZxXtTxR6Dau2U19sx54HZ7u+z2SRdncmrPKGpccgSpje6bFtaUnmQAQxolMHoQHdzSuKQAed7rnD0EsYxRKWOMaoU6Sn6uhgvl8rkBHLodovu7vDRZIw4Yj+LXPFiLbEHdGHWoo6MajS8x0Vdcd3uS+doFueVLpPVEnsKUpfUTySRzF1KSZUF4JB89rgkLI7Aklb5HF294ROhsKN5M3E6TKjWCo5Hy71X3lqONVPfNgK6W2AmPd5RA07ZwqPrg4O1p4aiBxvFP6DEEYlzsSJWURm3W0E++4SsF+rmzsrNqi8cYa873QFlACQ2HZYXvGN+nbsW4C95JCXd/YNb3vaIa9GATs3Hr6kZJUSrSt5wYDswySiJ3kWaEcIMEOAi+hrK1H5d6Y+fze8YyYD9TS47ZIpUQIqqvHJKs57ALAhH3Ucyz4tObmDxI1B0IK2ZNKElOGoDCtbQQW0UXH5uX1Kb7Lh0t0HyhFumzPTnZq7jsbgZXydD5ixJY652XqXU7MGEMGjW9vKgch3O3OEqakOKYmK8EAZrC9PSjSFhOw0EJD+6BoRwkJderMndxJOaq37Z6y6NhxxhnSijtWYKhWe3M4nayzDgES2OkOcFdEs4xUHu1Gx3T/8eCi4X402E4/rukwwLuH05vbUU7CMzC3OJSD7epgwqrZLlkPknK7rcu66tZ2N4Sb+Vxu2mG4E5TIDWl1PHcCbyKtb/ilgdAquhHISm7ux9lC02KUJfpxuJTIRJyug4CJe2mvX+GTel0zd/3oUg4CmY2MlRq9t7ddZ/NxGwP6+6Pb742KBDV+rhzvQVJ3bBuL7f7RVztczglPxzgHo3Mcd4fEdWdDY6oTo27pg8rmO9nqrv1FkiAdjP9gHG4Fzbh1abrd78yeTS/61O1If6usvUsct7oh3GjqYJkWKuO3U8MLfUk1Lm6ETFAi1uk67hIY5fFzphaVWLiNtbv0J1oCJrjtTl7qu2kWX+c20bG1RAxu7hRK2uyC9BrAPacTCenHhpCVOh/R9doJcTAfmdf2evJo6ZQH+KEreI+eIfyRVe4Oj0TS4mmu8tlbE6fYbW+DPh5Bo5rLS8Wh91HwaNGS7vygjWfpHnfs2jDpOsQ38+WYwdx0E08mLmW4te7PJ40JBfQqsKD5J7fHbsofA4kYuHxodZfWnFa0bTxh92eN6Acpd/g9fCqUsCnKOZ983rJzqV9j+D55lLhMtIVx2e6nwqkIybjLZk176IlhbAPUR7k2pgmXaEw+NhnSQxfs6LLBdNxfm8lApkg2OzhpxzA9HLGE9sB8scmGkbscBKbMRznPpUnWH9SGx7gKn0LqOOQYwTTNPvAgSq5smUqMDW6h1WXQXHuzg4rzUdtFbmm5/shnaA+HO7YVT/YeN6S9YnW4TAYsBfrODT4Sm9GCRj2tZAKrNhsmXPsgTqgeKngr2wt2tsWYm0htzpaj30ovMO1WjRy5VI7E9rZDNqU9ScMVc42xt5LD45qnd82fT/jhyN3bApbNTZvO+3nrRjvB2Fd5eKGP5sDVPi5JEeGeTZIOSeqIFdvbHMO5xKeKvSnFwyQM2nRX3EJ1u0reHRs/5UhqfR7KsNkP/dRImiTjndszrizB5s1LmG0uqWPdUkkYVP3xvlV9fHuHrWLOhku/Pie2vg6T9HaK0fOdCKSt0az7cLhCIV9ovu0pPCmqPIkHYd+L/V7QkHE76tahdrDdySTz3ZjG5p7PxaaEzCPiU7tAakE7S0TuxZfdM3Haw+fTnr0oD4AKeSgPtoWU+9gOdMGzmaDlGb3eJlczmmQNJs7K7Xi1qEjBxjtFrEXbEh/XmPZ39gnlZt9W5jHf3kEncRFBKRwPoRQ3jDYUVMZbx1ZCgkP78M6NMMEHEbnUjr+pR5wIhtkmYJiIVQFjwCB7mubUz9cewWnWFRurfTzOF2FDPzC+ObfTBtuRUGgZcRFnG0TbCrU/5wA9MOMiK7Bt2Ak/XCc621rMJBMHW9hNicvO6SkVOM420C5m7X5KHtJsWdeszUSH2F9j+6p7+s0qrqe8ie7BXRsoLGkeyI0aL/ApK4LHQAz8YbufFUjek9RlRAszv2+sjL/gDHrN83k4hOKmSmBB16UrjsV8GdwT1InFidjP4oPlqDLHxKaHxXQUOFAkwvV1DPKS07iAXqNjxojKoJd3wmd1Hq6PLBHR2qnblI/UldG7OeQ25mIOSiBwX7DBkJa1FAb3It5J++LUbQ3Vz9G2pyFi9sw6OOfDUId8p5225No2aWtXdPN9W3jhHrZg/mHuTvXdWdP6YZD2hBDXVZNt17uQA72tZEd1S+rreds9Zj9FbkEN1xeW23qXLTojcBUIp+J8ChNLmHuL19dJLbfd7SBrG86M/Ci9Kcebhgo1HQz+nW1PD+e+FeewkWNF2chDTCZiZHm6l0LEQXcUYj4hdswBZN9JMXvCmbOl6Wu7Ja/IxcPUSZo5qLedPpl0SwtgmklDpTBPWs9ao+k2lXATA5dmN/DDFa66n3qWWNvzYdMZ3nxEuAvhH6RoKDnkuPHSa17G15MNI1yI5fR2JO6kjxmnnIuC7ERs8MmjcTi/g4FkzqUmN+8uuxdkgoGmjpya2eC6B0wAJ4Op1ofwahoHgVW7FrRVvT9gBntWIVoM0Din5D3e3S9mKXrpmMvr0WYPQ4hpfDdi9yyEJmUedL8z1apPyoGY1PYMLJwra3aIYNh9CB5CFtV+NHkuRMG8lseoRjaB99CDo2sUtRrQsOgcs9ilLvC9SCXJO7u9MmJjG5672RaxroL7ZKZyvzGoU8ih4Ryer8EmbE+au3bw5iJWlJQwD81D6O01cEgNim4S45HEmtigIWSAAamkcaF0Olysj9OWjhmp67f9TsucvujRLAzagVauhxIf8rWJHXYKLNSZnClYBB397bYC/fHByCRcpu4VEzv41bquxdrbLH/ju5g70J1sLlRqhcEyRAwFPV5wulfHg5NHHp/OqWv1rjtd+aFppwDZhYxNcBRzNVGU5Y5cKyIj40anh+UJJLn3WZCyvDQ4s9ERBi2f1yHF0lCEhRxc5I3UQxudJVgpekDbUaShs/boawKbH9PU1D0CMkaUid2NIHZBFvRNdwqxnbbZdPha3eRiStGbRj90EC4RFIqILLLmQU2aHLF3b35QZVdP1HeNd5Ozzc4gfXitqMrcFbgsQ9n91JiO+JADevCMNWru72aGw7PGDsyAj7TZ0+PjcV3jl5AGs5ykU22Q44ctBE3OPm32xhqhkmLrXc/haVeqR47CMpuY85psONCiacop5Yl0VygI3p/jGdltheOdf5xkH5Rb8QAhtB45ZzqewoybaDAOYwTK7eMyErGNDd/8UnOJ9QY7rrtD6YUIWqFjtRs8dSMiegOypGOcBvaGaN+paHpJYImXqHSrbHGM7OOHI0T7Ji/DDIbX8pq+Rv6abLUCV+gTrPD9ZUtxYD664IEChx4/3vdiSm6deTaaexlsKDy0QItGMAxJkn/5y9uHt9+OzN7+Z+96Lcc2/89Oj14HPd/e3HgeBAaO//nJ6/P/UJ6/fnhrvARI8zoba7M+ej9M+ruTsY//9GBv2Tq9Xpz6dn78Oo7unGh5jfgtKfy+7Zrpa1tmzzc2wA63b5eXD9vl/VQPfP/+DPPJbTnELIFqVfe1K991eFteDFxewwj8xOmC95/R+yHhhzf//YWirzCGfg2aatHw/cwfKAZ/2n6C3/72fwGd4mQ7Ci4AAA== -->
