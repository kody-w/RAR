---
name: "rar-cowork-cookbook-ppt-exec-document-safety-protocols"
description: "Builds a read-only executive PowerPoint deck on document safety protocols from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_document_safety_protocols", "rar_sha256": "b0760789cff3a620191d698bcc707d85e7ef9a23d6e64ff613a02cc0b992a51a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_document_safety_protocols`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_document_safety_protocols_agent.py` and in the RCI capsule.

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

Document safety protocols Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on document safety protocols from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-document-safety-protocols
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
    "legal_entity": {
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Target .pptx name, e.g. ppt-exec-document-safety-protocols-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly, 15-minute review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_document_safety_protocols_agent.py` and embedded as the fenced Python below (sha256 b0760789cff3a620…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_document_safety_protocols_agent.py` first:

```bash
python3 ppt_exec_document_safety_protocols_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_document_safety_protocols_agent.py   # or on stdin
python3 ppt_exec_document_safety_protocols_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document safety protocols Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on document safety protocols from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-document-safety-protocols
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_document_safety_protocols',
    "version": '3.0.3',
    "display_name": 'Document safety protocols Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on document safety protocols from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-document-safety-protocols',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-document-safety-protocols',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '60b0ca083ba00886',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/document-safety-protocols'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-document-safety-protocols', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Target .pptx name, e.g. ppt-exec-document-safety-protocols-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly, 15-minute review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for document safety protocols reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on document safety protocols for a 15-minute monthly review. Produce 'ppt-exec-document-safety-protocols-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads document safety protocols data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on document safety protocols from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on document safety protocols from D365 USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx name, e.g. ppt-exec-document-safety-protocols-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly, 15-minute review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive PPTX summarizing document safety protocols status from D365 ERP data for a monthly review, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDocumentSafetyProtocols(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDocumentSafetyProtocols'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx name, e.g. ppt-exec-document-safety-protocols-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly, 15-minute review).', 'type': 'string'}},
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
    print(PptExecDocumentSafetyProtocols().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
