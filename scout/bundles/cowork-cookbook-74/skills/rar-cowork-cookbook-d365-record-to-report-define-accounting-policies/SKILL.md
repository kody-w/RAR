---
name: "rar-cowork-cookbook-d365-record-to-report-define-accounting-policies"
description: "Answers Dynamics 365 F&SCM questions scoped to the Define accounting policies subdomain of Record to report (10 L3 processes), using D365 ERP plugin conventions against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report_define_accounting_policies", "rar_sha256": "3ed66549cb81caacfe5217c5b6c57b5d288e54fcf1f248bf9c74811ace51ef24", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
