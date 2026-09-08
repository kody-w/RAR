---
name: "rar-cowork-cookbook-ppt-exec-document-safety-protocols"
description: "Builds a read-only executive PowerPoint deck on document safety protocols from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_document_safety_protocols", "rar_sha256": "b0760789cff3a620191d698bcc707d85e7ef9a23d6e64ff613a02cc0b992a51a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
