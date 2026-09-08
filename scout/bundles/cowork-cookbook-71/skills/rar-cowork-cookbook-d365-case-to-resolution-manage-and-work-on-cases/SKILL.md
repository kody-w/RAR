---
name: "rar-cowork-cookbook-d365-case-to-resolution-manage-and-work-on-cases"
description: "Scopes the conversation to Dynamics 365 F&SCM 'Manage and work on cases' (17 L3 processes under Case to resolution), answering with that area's entities and USMF conventions; call it for case-handling questions in D365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases", "rar_sha256": "c47ed869dd094f0997e44d93c3fbf187c22f2c7885b5cb08b4432ade5f721a9b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases`. The original RAPP
agent is preserved byte-for-byte in `d365_case_to_resolution_manage_and_work_on_cases_agent.py` and in the RCI capsule.

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

D365 Manage and work on cases Expert — Scopes the conversation to Dynamics 365 F&SCM 'Manage and work on cases' (17 L3 processes under Case to resolution), answering with that area's entities and USMF conventions; call it for case-handling questions in D365.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution-manage-and-work-on-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_manage_and_work_on_cases_agent.py` and embedded as the fenced Python below (sha256 c47ed869dd094f09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_manage_and_work_on_cases_agent.py` first:

```bash
python3 d365_case_to_resolution_manage_and_work_on_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_manage_and_work_on_cases_agent.py   # or on stdin
python3 d365_case_to_resolution_manage_and_work_on_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage and work on cases Expert — Scopes the conversation to Dynamics 365 F&SCM 'Manage and work on cases' (17 L3 processes under Case to resolution), answering with that area's entities and USMF conventions; call it for case-handling questions in D365.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution-manage-and-work-on-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases',
    "version": '3.0.3',
    "display_name": 'D365 Manage and work on cases Expert',
    "description": "Scopes the conversation to Dynamics 365 F&SCM 'Manage and work on cases' (17 L3 processes under Case to resolution), answering with that area's entities and USMF conventions; call it for case-handling questions in D365.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-case-to-resolution-manage-and-work-on-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution-manage-and-work-on-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cef51efc074187c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution-manage-and-work-on-cases', 'uses_skills': {'custom': ['d365-case-to-resolution-manage-and-work-on-cases'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage and work on cases Expert** skill for this conversation. From now on, scope your help to the case to resolution domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the conversation to Dynamics 365 F&SCM 'Manage and work on cases' (17 L3 processes under Case to resolution), answering with that area's entities and USMF conventions; call it for case-handling questions in D365.", 'example_request': 'Act as the D365 Manage and work on cases expert and help me work a customer case in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when the user needs D365 F&SCM guidance on managing or working on cases, via the Cowork D365 ERP plugin against legal entity USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365CaseToResolutionManageAndWorkOnCases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolutionManageAndWorkOnCases'
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
    print(D365CaseToResolutionManageAndWorkOnCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
