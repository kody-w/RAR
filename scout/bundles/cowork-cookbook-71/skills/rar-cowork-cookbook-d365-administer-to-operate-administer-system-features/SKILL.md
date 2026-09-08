---
name: "rar-cowork-cookbook-d365-administer-to-operate-administer-system-features"
description: "Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate_administer_system_features", "rar_sha256": "d2dc7e3043760406249e78635b724059c3c48f12c70249477e825c5ce30a5cee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_administer_to_operate_administer_system_features`. The original RAPP
agent is preserved byte-for-byte in `d365_administer_to_operate_administer_system_features_agent.py` and in the RCI capsule.

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

D365 Administer system features Expert — Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_administer_system_features_agent.py` and embedded as the fenced Python below (sha256 d2dc7e3043760406…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_administer_system_features_agent.py` first:

```bash
python3 d365_administer_to_operate_administer_system_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_administer_system_features_agent.py   # or on stdin
python3 d365_administer_to_operate_administer_system_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer system features Expert — Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate_administer_system_features',
    "version": '3.0.3',
    "display_name": 'D365 Administer system features Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-administer-to-operate-administer-system-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dcd4441c68528abb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate-administer-system-features', 'uses_skills': {'custom': ['d365-administer-to-operate-administer-system-features'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Administer system features Expert** skill for this conversation. From now on, scope your help to the administer to operate domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.', 'example_request': 'Act as the D365 Administer system features expert and walk me through this in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM guidance limited to the administer to operate domain, specifically administering system features against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AdministerToOperateAdministerSystemFeatures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperateAdministerSystemFeatures'
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
    print(D365AdministerToOperateAdministerSystemFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
