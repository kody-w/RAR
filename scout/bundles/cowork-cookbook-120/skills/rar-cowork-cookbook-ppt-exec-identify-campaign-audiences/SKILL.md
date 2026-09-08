---
name: "rar-cowork-cookbook-ppt-exec-identify-campaign-audiences"
description: "Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_campaign_audiences", "rar_sha256": "57d638b17936e3f96dbe9d9d7c3e3044ab824201757989e9c81cbbf8c691ded4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_campaign_audiences`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_campaign_audiences_agent.py` and in the RCI capsule.

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

Identify campaign audiences Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
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
    "briefing_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. monthly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 57d638b17936e3f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_campaign_audiences_agent.py` first:

```bash
python3 ppt_exec_identify_campaign_audiences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_campaign_audiences_agent.py   # or on stdin
python3 ppt_exec_identify_campaign_audiences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify campaign audiences Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_campaign_audiences',
    "version": '3.0.3',
    "display_name": 'Identify campaign audiences Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-campaign-audiences',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e3d01d1b479f3554',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-campaign-audiences', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'briefing_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. monthly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify campaign audiences reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify campaign audiences for a 15-minute monthly review. Produce 'ppt-exec-identify-campaign-audiences-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify campaign audiences data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on identify campaign audiences from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'briefing_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX on identify campaign audiences status from D365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyCampaignAudiences(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCampaignAudiences'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'briefing_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'type': 'string'}},
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
    print(PptExecIdentifyCampaignAudiences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
