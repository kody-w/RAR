---
name: "rar-cowork-cookbook-d365-case-to-resolution-manage-and-work-on-cases"
description: "Scopes the conversation to Dynamics 365 F&SCM 'Manage and work on cases' (17 L3 processes under Case to resolution), answering with that area's entities and USMF conventions; call it for case-handling questions in D365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases", "rar_sha256": "c47ed869dd094f0997e44d93c3fbf187c22f2c7885b5cb08b4432ade5f721a9b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
