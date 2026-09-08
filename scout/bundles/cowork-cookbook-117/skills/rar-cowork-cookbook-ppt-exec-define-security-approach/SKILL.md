---
name: "rar-cowork-cookbook-ppt-exec-define-security-approach"
description: "Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_security_approach", "rar_sha256": "29fd84925593e6d36baae497512796492062eae5d21a4cc8f9bba9d306fa7799", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_security_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_security_approach_agent.py` and in the RCI capsule.

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

Define security approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
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
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Briefing length the deck is scoped to, e.g. 15-minute monthly review.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 29fd84925593e6d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_security_approach_agent.py` first:

```bash
python3 ppt_exec_define_security_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_security_approach_agent.py   # or on stdin
python3 ppt_exec_define_security_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define security approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_security_approach',
    "version": '3.0.3',
    "display_name": 'Define security approach Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-security-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-security-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '106156c1ecfdae5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-security-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-security-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'meeting_length': 'Briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define security approach reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define security approach for a 15-minute monthly review. Produce 'ppt-exec-define-security-approach-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define security approach data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute executive deck on define security approach for USMF from D365, with charts and speaker notes.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart comparison.', 'name': 'review_period'}, {'description': 'Briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define security approach status from D365 ERP for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineSecurityApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineSecurityApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart comparison.', 'type': 'string'}},
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
    print(PptExecDefineSecurityApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
