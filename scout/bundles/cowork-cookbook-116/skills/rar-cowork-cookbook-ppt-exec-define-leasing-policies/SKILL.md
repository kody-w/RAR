---
name: "rar-cowork-cookbook-ppt-exec-define-leasing-policies"
description: "Builds a read-only executive PowerPoint deck on leasing policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_leasing_policies", "rar_sha256": "6f77aac765fe60bbe9bc2c19ccac0628c7263797b2ad7f3f52928fb2444fc736", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
