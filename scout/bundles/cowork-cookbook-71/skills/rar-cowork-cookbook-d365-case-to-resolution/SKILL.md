---
name: "rar-cowork-cookbook-d365-case-to-resolution"
description: "Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution", "rar_sha256": "dda3a961023f6dcfb506a3a20d115aad81ae660976a24d67c95786840036f072", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_case_to_resolution`. The original RAPP
agent is preserved byte-for-byte in `d365_case_to_resolution_agent.py` and in the RCI capsule.

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

D365 Case to resolution Expert — Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_agent.py` and embedded as the fenced Python below (sha256 dda3a961023f6dcf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_agent.py` first:

```bash
python3 d365_case_to_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_agent.py   # or on stdin
python3 d365_case_to_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Case to resolution Expert — Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution',
    "version": '3.0.3',
    "display_name": 'D365 Case to resolution Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.',
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
        "upstream_slug": 'd365-case-to-resolution',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16cca54576658a8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution', 'uses_skills': {'custom': ['d365-case-to-resolution'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Case to resolution Expert** skill for this conversation. From now on, scope your help to the case to resolution domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.', 'example_request': 'Act as the D365 Case to resolution expert and walk me through resolving a case in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 Finance & Supply Chain help scoped to the Case to resolution end-to-end process against the USMF tenant.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365CaseToResolution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolution'
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
    print(D365CaseToResolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
