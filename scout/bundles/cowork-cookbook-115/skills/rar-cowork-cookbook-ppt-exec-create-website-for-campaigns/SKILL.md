---
name: "rar-cowork-cookbook-ppt-exec-create-website-for-campaigns"
description: "Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_website_for_campaigns", "rar_sha256": "1112e8739102fd6f2d44d22ea608b9fc1c0ce591a33d6d7d19f49ca18e13cd9f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_website_for_campaigns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_website_for_campaigns_agent.py` and in the RCI capsule.

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

Create website for campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 1112e8739102fd6f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_website_for_campaigns_agent.py` first:

```bash
python3 ppt_exec_create_website_for_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_website_for_campaigns_agent.py   # or on stdin
python3 ppt_exec_create_website_for_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create website for campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_website_for_campaigns',
    "version": '3.0.3',
    "display_name": 'Create website for campaigns Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-create-website-for-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bed3c9ec9d52d1c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-website-for-campaigns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-create-website-for-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.', 'review_period': 'Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for create website for campaigns reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on create website for campaigns for a 15-minute monthly review. Produce 'ppt-exec-create-website-for-campaigns-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create website for campaigns data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on create website for campaigns from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on create-website-for-campaigns status sourced from Dynamics 365 F&SCM, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCreateWebsiteForCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateWebsiteForCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecCreateWebsiteForCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
