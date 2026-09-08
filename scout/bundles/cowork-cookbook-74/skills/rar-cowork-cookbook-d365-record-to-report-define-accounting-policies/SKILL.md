---
name: "rar-cowork-cookbook-d365-record-to-report-define-accounting-policies"
description: "Answers Dynamics 365 F&SCM questions scoped to the Define accounting policies subdomain of Record to report (10 L3 processes), using D365 ERP plugin conventions against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report_define_accounting_policies", "rar_sha256": "3ed66549cb81caacfe5217c5b6c57b5d288e54fcf1f248bf9c74811ace51ef24", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_record_to_report_define_accounting_policies`. The original RAPP
agent is preserved byte-for-byte in `d365_record_to_report_define_accounting_policies_agent.py` and in the RCI capsule.

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

D365 Define accounting policies Expert — Answers Dynamics 365 F&SCM questions scoped to the Define accounting policies subdomain of Record to report (10 L3 processes), using D365 ERP plugin conventions against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report-define-accounting-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_record_to_report_define_accounting_policies_agent.py` and embedded as the fenced Python below (sha256 3ed66549cb81caac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_record_to_report_define_accounting_policies_agent.py` first:

```bash
python3 d365_record_to_report_define_accounting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_record_to_report_define_accounting_policies_agent.py   # or on stdin
python3 d365_record_to_report_define_accounting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Define accounting policies Expert — Answers Dynamics 365 F&SCM questions scoped to the Define accounting policies subdomain of Record to report (10 L3 processes), using D365 ERP plugin conventions against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report-define-accounting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_record_to_report_define_accounting_policies',
    "version": '3.0.3',
    "display_name": 'D365 Define accounting policies Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Define accounting policies subdomain of Record to report (10 L3 processes), using D365 ERP plugin conventions against legal entity USMF.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-record-to-report-define-accounting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-record-to-report-define-accounting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b99fd98a73fe6c85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'record-to-report/d365-record-to-report-define-accounting-policies', 'uses_skills': {'custom': ['d365-record-to-report-define-accounting-policies'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Define accounting policies Expert** skill for this conversation. From now on, scope your help to the record to report domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Define accounting policies subdomain of Record to report (10 L3 processes), using D365 ERP plugin conventions against legal entity USMF.', 'example_request': 'Help me define accounting policies in D365 for USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs guidance on D365 F&SCM record-to-report work in the Define accounting policies area against the USMF legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365RecordToReportDefineAccountingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecordToReportDefineAccountingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365RecordToReportDefineAccountingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
