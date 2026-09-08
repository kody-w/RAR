---
name: "rar-cowork-cookbook-d365-acquire-to-dispose-acquire-assets"
description: "Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose_acquire_assets", "rar_sha256": "33e19674ea73aefa8bab762a60634bbae14d9e9e6de0a4f0c117d256e2ad2c36", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose_acquire_assets`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_acquire_assets_agent.py` and in the RCI capsule.

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

D365 Acquire assets Expert — Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_acquire_assets_agent.py` and embedded as the fenced Python below (sha256 33e19674ea73aefa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_acquire_assets_agent.py` first:

```bash
python3 d365_acquire_to_dispose_acquire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_acquire_assets_agent.py   # or on stdin
python3 d365_acquire_to_dispose_acquire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire assets Expert — Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose_acquire_assets',
    "version": '3.0.3',
    "display_name": 'D365 Acquire assets Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed',
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
        "upstream_slug": 'd365-acquire-to-dispose-acquire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63374b5cb6933e93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose-acquire-assets', 'uses_skills': {'custom': ['d365-acquire-to-dispose-acquire-assets'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Acquire assets Expert** skill for this conversation. From now on, scope your help to the acquire to dispose domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed', 'example_request': 'Act as the D365 Acquire assets expert and walk me through acquiring a fixed asset in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user needs D365 F&SCM guidance on acquiring assets within the acquire to dispose domain, against the USMF legal entity via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AcquireToDisposeAcquireAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDisposeAcquireAssets'
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
    print(D365AcquireToDisposeAcquireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
