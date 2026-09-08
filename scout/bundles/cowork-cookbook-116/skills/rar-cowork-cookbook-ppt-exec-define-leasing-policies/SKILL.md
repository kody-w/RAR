---
name: "rar-cowork-cookbook-ppt-exec-define-leasing-policies"
description: "Builds a read-only executive PowerPoint deck on leasing policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_leasing_policies", "rar_sha256": "6f77aac765fe60bbe9bc2c19ccac0628c7263797b2ad7f3f52928fb2444fc736", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_leasing_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_leasing_policies_agent.py` and in the RCI capsule.

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

Define leasing policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on leasing policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies
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
    "comparison_period": {
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-leasing-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped to, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Policy area covered by the deck, e.g. define leasing policies.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 6f77aac765fe60bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_leasing_policies_agent.py` first:

```bash
python3 ppt_exec_define_leasing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_leasing_policies_agent.py   # or on stdin
python3 ppt_exec_define_leasing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define leasing policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on leasing policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_leasing_policies',
    "version": '3.0.3',
    "display_name": 'Define leasing policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on leasing policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-leasing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4802593ddba4c87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-leasing-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-define-leasing-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-leasing-policies-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'topic': 'Policy area covered by the deck, e.g. define leasing policies.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define leasing policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define leasing policies for a 15-minute monthly review. Produce 'ppt-exec-define-leasing-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define leasing policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on leasing policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on define leasing policies for USMF for our 15-minute monthly review, read-only.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Policy area covered by the deck, e.g. define leasing policies.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-leasing-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready leasing policies deck for a monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineLeasingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineLeasingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-leasing-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Policy area covered by the deck, e.g. define leasing policies.', 'type': 'string'}},
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
    print(PptExecDefineLeasingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
