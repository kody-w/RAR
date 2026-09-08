---
name: "rar-cowork-cookbook-d365-acquire-to-dispose"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose", "rar_sha256": "60a84f1ab4eb989902dfff8b7fedc829758c7803b07d8d5e6dbf7db92d7756d9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_agent.py` and in the RCI capsule.

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

D365 Acquire to dispose Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_agent.py` and embedded as the fenced Python below (sha256 60a84f1ab4eb9899…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_agent.py` first:

```bash
python3 d365_acquire_to_dispose_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_agent.py   # or on stdin
python3 d365_acquire_to_dispose_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire to dispose Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose',
    "version": '3.0.3',
    "display_name": 'D365 Acquire to dispose Expert',
    "description": 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-acquire-to-dispose',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '79d4cca7c8aece60',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose', 'uses_skills': {'custom': ['d365-acquire-to-dispose'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Acquire to dispose Expert** skill for this conversation. From now on, scope your help to the acquire to dispose domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.', 'example_request': 'Walk me through the acquire to dispose process for fixed asset acquisition in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs guidance on D365 F&SCM acquire-to-dispose processes, entities, or USMF conventions via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AcquireToDispose(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDispose'
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
    print(D365AcquireToDispose().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
