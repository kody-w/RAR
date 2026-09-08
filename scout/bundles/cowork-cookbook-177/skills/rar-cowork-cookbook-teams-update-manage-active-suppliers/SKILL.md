---
name: "rar-cowork-cookbook-teams-update-manage-active-suppliers"
description: "Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_active_suppliers", "rar_sha256": "a29455ee80e4f197f73e55f0091d8b06ed529c32235591248c8facf27d6329dd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_active_suppliers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_active_suppliers_agent.py` and in the RCI capsule.

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

Manage active suppliers Teams Channel Update — Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the supplier summary, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 a29455ee80e4f197…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_active_suppliers_agent.py` first:

```bash
python3 teams_update_manage_active_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_active_suppliers_agent.py   # or on stdin
python3 teams_update_manage_active_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active suppliers Teams Channel Update — Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_active_suppliers',
    "version": '3.0.3',
    "display_name": 'Manage active suppliers Teams Channel Update',
    "description": 'Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-active-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3833d56f8c9be519',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-active-suppliers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-manage-active-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the supplier summary, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage active suppliers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-active-suppliers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage active suppliers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.', 'example_request': 'Draft a Teams update on active suppliers in USMF with an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to scope the supplier summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on active suppliers from D365 ERP data, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageActiveSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageActiveSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the supplier summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageActiveSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2n6oKBGKrFx0xCAFiFTtIro4ym1jEJhYh8PR3n4N0q2x3u2e6J+avUS26wDm55y8z7+HXN3/o07p9+/xmxn614v2iyNK4XflVtGLqsW6v4Ku+BuDfKqyrvs2Coa/b7u3DWxR3YZs1fVZXy/ahLP02m+Nu5Yd9do9X3dA0RQZodb3fD93q0tblaj9VfpmF3QrFsRX3301GWV1qwG6VgC3VqogTv1jFVZ/101OGNu6HtgI0V1bsl93HNvajaQU4XaN6rFZh6ldVXKyauutXTTEsCzv/HkcrOvKbpxiM30Yr0TyqqzHr05WkCd2T8m3IwuvHRda6WgGl+rrq/msV1UCBqu5fFLP+E1A0fvhlU8Td2+ef//rhLQM/v33+9S0s/A7cenvKZTeR38eKX/lJTD/VN9+1XyxV+FUCVjYTMHUFrpu4BUqX4FYUX1bvVz92cXH5sPrP/7yOfpt0P33+Uq3eP1/elj/GUK36NF71td/1QMPQb/wgK4ClPq3oYvSn7nfW6oCnquTTa+dvlOpm9Zfl2Y8vJp+SuP/xy1sNRPAXO3x5+2kFvPHlrR2Wnz8tVJoff/pU1GPc/vjTb3S6IcjjsF+IAak/fX2/ficLFv62NLusvpoay7zzauMwa2JA/Hf6LZ+X6O/k3k3y9bX4x7r5sPpzyos+fwHyvmIxAHT/nCywAdj59imvs+rHdx5tDSLOr8L4x5/+GdkwjcNrkXX9v0T35xfhFIQosNa7SX768HTfX1frd92+0/znbBsQMP+OJmD5N3bfDfXPaD89+3eki6wCUf/Nl39K7s82rP+y+vmf6va/2/Bhdfnyto8LkCatHxTx59WvzxD5+Yfot5s//PVvgPT/kYxZD234pPC19KvsEnf9168//9A9b//w159/GBoQxSBHvw5t8Wc0/8yuTz5/sOD7qh//uBfwt6trtSDR9xxa/Vo3/63926eV4xdZ9Nv97vPq95m4fNarRYlvTF8m+F02dkDW39nxp7e/AfSpgDbDE7QW8PmP/1gpWdjWXX3pV2ZYD/0KOLjPyngR3kqzbgX+LqjRxsCuXQYM+74OxP/i4UXi+rL65X+ET7T/GL6jPdQvuPZ1eALbYlqAbF9fyP71G7J3v3xaWYB23WZJVgHgNmhN+7KsrPqFb9PGXdwuaBxMffwRpPTH5YdVVq1++VfIf31S+tRMvzwRO3vhn8EIC/Z1QxF/WrR0U1A4XjqFoITFjzgcAJOiDoFElwwA9wegfVcXoBj0i0W6a1YUqygD6AJK2XudGarPC7Fffvkl8Lv0S/UCa3T1qnEdBBZ8F2f18SNQ7VJkSdp/qeIwrVc//Pq3H1b/c/W/2/UkvvDQQOF49wmQ8FmaQI4NJVgG3AUcDADk6ZNf//ZuYECmAoUUeDC7ZPFrM4jRaxx9s7Z5oD8iGL4KYmBlYOGyqdseVIClhK2Ey+q7vIDp8mipEelS4qK4iasorsIJUPWBOt8tuVTBDgRid5k+rIYufnL9JWj9p4glSHa//2WlMBqoSHUB/lvEfC4Cm+sqA+b/Hguv+4BI+0O32n0j8WmlLlG5avzWb9LWf+dx8V9+WfqC9+2AuL+q4vFLtZTfeDHVM0Ve5gGLgGXCd5d+XHwOmhXQj1RR9433c42/1E3rWT/bL1X3Hv5+u7giBOUAME2GLFqKwn+9h1SX1kMRPe0HJF0ovXshevfKMwZflf/vO5/u1bSsmPcu5dUlrL4MCLzZrv5/7ZgWe9A8b7A8bbH7Fataxunlp6WBXPz56jkXgRdNnjn5WzPzDbC+4faXqshA0LXTf71WPr37vuaFhUMLpDdo40kfhBYw4EL3GflLJLftkjP+l+pbgfgAdH6iIdADwARIoyV6vzFcnn6TNAVYsFz/1iw8IwXYBxgERPeqGYICRN4ljqPAD69AqsXe31wM0iBeMnlMszD9g1aLx0C0AforIEQG8hE459N30H49/Sb6Hza+eqJly7NfHEDytk8CQI54EXBx1eI4IF7/6teBnp+fRIAaZdMvugcgfYCmr5txGwPfdlm/QOXLrnEDoPrj8v3SdLkbPxqQMcBYIC+aAVj3mUkLyJSg4wEyADABiVVmFegAgFHejfAk6JcLLADYfQ/PF8Xn7XeF4mf6LaXr28ZFkWXP0g28csGvpt+jh/VnYQLolcuKJ9+/j7Tv3BbaC4J2AAUBx29PX23Dp1flf7UWq290P//DQPTjvzczPWu5/ccA+LxK+77pPkPQq/5+K7+fAH5BL1m7Vyn++KqVH1+18uMLMj5+h5o/0H6p/Xn178n3BxLv+fF5tfkEf4KXR/J7fL1/gDmYj7vTx+3y9EtlxL8hLGBflyDAFudNoPZ/L4ffloCamLQAuMDiV3nslqo6gkL+rAfAE1+q3wf8knALcCVLgHb174Dg2ReA4H857nvZAo+qHvCOlm4yiZcp7pkeXfz2uRqK4sMbANX4X5velupULoHdLWMfSCHQn/VZ/LwCGRp9XQR5kfv174bi4zNRVt8WfA+zf4TaD6v4U/Jp9a94+iMCI/hHGPuIbD8u/D/lHSiEQNB+ahaVXqPf0iw+UezR/4lczx/84tNqHwPELLrfp8Z7xVsq/u8y+OUFYP0Q6P9htQjYLRUa6LaYZsl+vwPpBFT8U1mederrq079o0D7pbj9oZQBQH6yeqXl98L4rJnTu7VsU+H+lNn3FvofObmga1mIR/XnpYB/eMdE8A3Gng+r7xMMUPF9pnz+CqAawLj+8zI9LRHx3LL8APaAr++bvv9WJIjf/voPcgHBnkALytVC6zchf1taP6euRQVAun/9kuDXNxB9PjC4/x5/7207WA5w6WO3tCkQyFLAHFy/8gk8+79q6N9pdKkPmklAxEeoLYbFMQnH28uGIi4EGmPYBYapTUQGMB5HGEKFKIKgGEZtkC0ZkqB7uyBEhKMIFUWA3iszvy79WLbIhQEqMEUhl+0GgaMoviDbKCJxEg8xAoF9KvCxAKP84Let16yK3pV9KbdY8vtssRjlXedf3wJ8C1Yetp1Avz4MRG0CCCGCSfbWHkw+itEdGs7Pums5+6IbZDDanUWOKJFRPxPRaaCFWbiG5uZhidh5hziKSh9wUUOYSxORhGIzBofYOII8yOAo79i5GbEQxdYYOZ9IYt75WCX1hjDJR1UWPdPB4LJjMjSWiMrZlnoOb/Ri23fk9WabF+gue6Rz7iNUEu74DPcbUW/iqZWNExcVbnXEzOG02csGRq2djISO6/lKRVlhOEyWu2XDiIaPXYXifH4MhjLltplOt0bQo2OnMYidH06MtNmwiGPf9K4XAPKZGFtwNOGSjshtua4MESszDNNaE+spUNfCTc4vGUSt1/B1xh5TfZTxgPUxXzo7ruv6t0vG5PtdL3XqzsrhlFSqCqWooPO8mSKgtWjfD/kM9Sh6rzLINmUFTkWSKUqnxMckKq8XzAxcoTExTzmJWnhE2frYeuIluex7YVvaaUbBloLSjkjW6niibw+O2K3bviKwjMw5VcjJjNlD/G135LOMregE3yhbzDMx3SLuJyP2aUrkCiyJmsqZKC54rCMeTzbUvO2UpDk3N2YfKILaCcK4q4qLLNIEZ96KWgoVmWTN7Ny7pes3bJ+KXjnnYa+d92XWIAY30EmQsy3e2ULVa8Os3Q/KuvedBJtTR7WV4ibcathOHG03DpLLKBzIO77LJplX291uiBQaetxJTEDuZ6PIGcRP8Ua3pexo4nblNNtbNWGoDbWqi5sHvDwOYyoy062e2mlvU1hln8/TcHJYgzSVzPGbjMfDx6GOyXg6lT3FbK2dWOVbDb9FiERfFYI++Yr62EMqtx1ql0UuYjU8NIWREmfvIirj+R3dmrC6ZVwChNvdkEzrKKP6qVFT9RK5541tSF0aZ3ttLe1mZ7BysW3ljG7XUzZ564ziz9dbteXvM8ePWSwd/MNVLcetrDI5fJhB2vEYIlpFW8Yzckqtce61PaT0uba/ibhDyKzz2OZNkWjSRjF539jo5c1Si+GSwUTa2i0zKLvosqYhcofm8w7pNSql2NASKeiOwj2aYLF0cZlkW04GPkayz2nnwzEqJYyd627bzrYyh9frsd8kMcOOl0QQ3ARCSTYndzf5mpx4K+7KOy6feuY8b7hqj7pX4nwseG9mzEKS1MdtgB+qYDTcsavtUNO9RN8phJHANMlF4R6pzWocYeVx7uQW22Fa6SDnPnuo8+HOuqyDJjiktLfzcbBPqW7wwokzTJ622V6XeKfOnMZgsQfPrsOEyhEpElHBG1h7LToHWxV1o8U9yIThKGjvfFuVVYVY56DaNpvHbZ630YMv3LFzkKTbGvttRWdp10sCTNUHk57Se6rO8KQ3LKUWkYqe0POu1F0MVfn9UXLpBui9v+3v/iYjGwM713qoxzdGusjZaAn26U7i0sFFWsWPynUXSXZyUsxbZjwyegykzraokd73GQfXnCQjBZpR9TasHfIqBAJ/t8L19tZdZN8+JriKowWCSxCLzLfzOpb2s2fsOEVrp4QaVSK9XI1LQuR7amT5S6f1jH0OTlyrb2NLn0KC11gnTY+1V6VGmMixxsLcww0N0SDrQYppFz7tJjvV5zIPFV/A83yH4ZA81RskWM9mfc0FPHPhcas95srDqfQ4k9nN5PNEDnj8GFaiSO3E3j9j1Fgld90avHtkhVfrztbo9qHw6+MpNdL9aQrv/BqbUSPjokcFn2gazrlGkVJ+RD3nqrCoF5b7uU92ZocdjYN2f0QnQ5hhIz2VEztIQnYeVXavICyzl3l5ju/o7e5CSXV1RDMRUz66Kn1o49cJJwU7zemCPcyUWeP87lxudRtmWHo/2WQIYNvZnUEUmaJ3CcVgf1PZ0nF1aeciGlzWmOFMBdobMn7AjzuWRmGNh5r4BDm3yWvd7JC2PLQrxQkmSgaxgv01f+w1YsQHi0Ogo1fsacmwmPN2HnuoI2/pDGNK2M3B6cAd2o49nKozgpPQVuU3ct8gLEs0FT1BKpIb1CGXNzHEoGvIEdbQWkY20nwXb7ACz9Dj1CV22rA8gmn3BLs5Si/JAn+j3NBJikzI53FmQp1FNhc9SPyMiGkhyOfgzFhX6yQq2wAT97tNzqo3WEM4hiPM7BCItCXtbd7Qz9x+yuxSv85ywN7Ek8qe9HVVhkquHG+X2bxZ1oO1SOs8t4h18LxgJ03+lilmnq/CZEJpsonmEnMZFdpc8HhCxX1LNQpqUmQiTPxDM7iKMeE+7lOGcQpk4quDxbO26JPbx9FqWMmbOnNMdU+JykasNqS218/JzVYiUNWO3C4RTncA5Ig4iIPgsjn/gHh14rYwd6MntTGyNT0e/figpw5uzzhHPWD9MDqJgASecxGcSDqxFO1C7CRXOrZ3eW5/55O7xGXnqyA8MDFw6vSsy0qzM289lp032yG6CfA96SKZKypHkROOWSe38bHWPFomssJOr8XpFJgjub4yfIB5LMMeHNcp+DA7F3tzrz64TJaE+HZSetOdnTiQj4dxF0Ic3ZxMYw4ZXOum+FZcTWN3Ny/8WQ4PQ2ntroxGbDZCyU+CHZQkmOgslokfqAXzD0dJ0s19V7uM0UZ7+rRnRXT2OA0tXSmlHYq9K8hcp5aGR+wc56J+gI/cWWPxDG/Ye1hJxaNgSGHI9L3HFsKYUalWRidT2rA1S8eN49BJbsOwpYmZIFvCiY+MrYYFa9hgLsaNCWtufZCpDbs/0JfOLHKNwQhi34Uswd7rgkYunmsYwb3ZnEbuIOZpGpWIjG3FciKz60HdkNhGTfJblevY7J8nxq72CNV54uDGfLztKlsW84t4K25S5fvTPtq3hab7CuK6euuLyTWs4kEXd/4hYqocFm3F7oNN0tGXJHdvXE/bmxFNWTQ+zLTnSIp61nkbZ6TzHDujffKPYsusg9gCl1QkwEfpwfhyOAOrbsPd5Ehze9rvWAJG2LgrGtjKH8GAjlddCUQkVG/yA31kQsIAUD2m2N2qAluqCAAvNsc2iatXTp0bUKNc9EP+KFukY6ZdO5SEDF3mXB3LRk5LfCbDkb7210N879XbdSvDmoBdFKFw5kMaY4JW74ZivG9MHcdN6F6GthEIYLRJTdC7GcPGZBo2aQ33LEjG4xKaBcEB/RhabpgjSHZ6oEuJq4QROYfe/dC7xDEbERGWMX8DhSLhqIcZ266PHjzGWjNS1NG3bV6RxzMzU9uzicPnWJLtrXorKfgqyJ200+fpRKGd0tsGyytCZo9sq1OQdMo316wlhp1hekju0ybEpcFFjVs9RhCm5a/R6YyIfO45/Yx40FwSKEJonoyiUqZghSncyjAPcF/1jvIRx8kWsU3XTY9nnd0ApbryvE8DKJY4+xg4YZaOVEBgYlY5e2oSYJy9cbvJMCCJVXdbbgZllFZvFjynnplJN/2kc6gp+Y+Oya+6EKXBTsFU6XGaTFKJToh5gHU1jzWKodG4yblsq575B2JF0r4JoPPWb46jbJ0GKoPVNVpmhtxwt1aNA1ENIh2BzlyfHx9UakFImCCtcGOuGbITYiwOoC5wrO2G9XfmQ2UM42CXSJrrUY0oaGD4RqZ5plETJlpvN6dWSh0aQxC/jWkzKWhazWyERDNr663r6tSaV7Nl7hvLIgMlvFzz6HLVzcaencdsKbTZ1yrEp1N/6ApjMFlYcdAuqM3m3haNyFnpZBSUvkkz/3K+dxpnZz6iuz5Bk3t/4nVuj7NlmfOHun54rhDtd4HQP04cAy64KBmHE1XC8c5pJelEGnVN79u7ytI5dI77TV2llFsyhymhdaNRDl2LQOLFMsJcZ847SOFQMrhYjGBvazuetgaM5u5x7evNGswWfeA1NwKiQ3e/d1PzREiSwxuTC1fqbSc5c+bpYludOyUo0T0AEdTTGP10GHnUVnGjIqZUOViq5SfSWMZtYJ11gC39HkYEi4iOZEaU9ZHcZ9dM2W75k3MDI4qDtnjMZVCTJbOqOR0akBF0k4n+YVKYddYcdr+zd1VUOaKBBYn5uELiLqH8rbwzs+uIaAfAo66tXGMPR5piay8t1hIFmkx+PPKoNAsEfYFv/M61D6ZzE0vkbsx5C52VOVvzTd48+klmdmNxMX3x7oy3M6zuWO1urTM9vw/49UqrJ7lRhng7J8MJRkei7KdcLyVY1jhDt4RtDW9t3N+yAp92ay4UaTiruB0qzAef3D2YaX0WkxldqzK+VUIwEe06h/OmB0mngsjKN/i2t62+4iE/k6trRieClbobyaPOQXxKJmPENVelKqvY5Jdg05kbXAvJPeMcGWvdZhuDOGTV5nDvFZ68VF0bxHhQWNZsN3i8i+4jyT94oIdz4omOGPy1ZFFDpeGbfLxo/BryDkbVd0R4TJWAINp5kPxURw9g8l7X6OaYmnBs8O7dKx/TUWCnOuuFEHs8XOMO3W5H5RY5mt9h9yHDoz1WEeXpdjuUMEZRJ+i4y+F20zgjiopQw51EMCZMxzN8sTS/4phUFG/SkLfc2X0MgSE2LkKu+xvRdejdOJXW5phrudCpGL3BxkBBIEQuinTN510/z1HMQYEXgrllA5HgH5Sk64dtF0czNy7QpK5BN6PuSitQg2l77RxfXQvBECEckvIS7xWIzDPEg8hYrUlLxaOYtZHilb3NubUthBzIw90eVbyRvZbqRCtksMYt7bI3BuvUe+chIHXF5vfYDU1IYu90+5hmUqZ2z5firvAhNtHZ/jCnLWqsMRJmqbi8UrnoCF2AwbIBoW0UOXFckjrmo+w+XXONCiN8sB8xsSxJqaG7Cgx9xhmCAw+yVDEmH8HYymmLUFJZR55eH50asrL7hly3h0A5esczeskn+nxlRIzU6CCgJqcyqgu7U7ikDdy4Nh1bGQ5nxY3d+O77VfGQOH2ebxUNpx3clyrf36PcuV/V4n4QRhZSCLlEdX6zud8ldlD8o8uWCx4IMn0+NO26uBJuLaW6QAmPNL7zS4CLVFHinVVV57gWqtO0MfqTze9gEDbXO5/eeeuelNfzge1iONx1eFzI6ISmctLdzBi6FTh53KegjKGzHkpQ121ze74f0Yhgx9G7G1gWOVBbChp2MLau56gp1HRHzBE5DoAFGV/iDtsdHS3za6QkVdRA5TTIjq0x7dNuOF/PeAZ7lnTsWjEJ6Y5OU6+Er2eXWss0oUYR406e06ItLaJmnuXMlqDXj82OGINoazlOvKdqZ1Ntu5pAHCrEgqMe+8gDOl/5UlNwGA6IotpSdXQoAuJIciS6FmWhN0B7m3sKur9eKtk+3j3IPw16T+80tHGHG9m56onWyhyCFbfBj/50SMhBUY391dtINWobm14pd+5w0qFhVueGdHf++tEWd5Fw7/tixucHamxEmFAUUgMtHBZNOTKdHgpOakHWzyZWgd7soWHlIGH13DGmJvY90d7mPCOGoaVKf6y1k+d5x7JvvEsTxo7cIWDQ3TByq8p5Vo67fFZ7eXNAiLxFyt5JH3yeloMqkPHJ6na4lXZVfrpzlX+nDZS3BwqMYHYVCwbjNbsxw+HCvLs8VQJsEXaZs44sZbhHHKdR60GhJYTTlcfaCOyd0VSjftkNhwzdq7aknC66XkfRZXsdOTo35jpQIXQCHueq01BGa0YQ1pXW9cmWua879GAGk7RF+IgYEsRJ61agrgflUXrrjUPwnqdDCMwiNJYGkadOBiOVx3SYhlGnNtKhzwiexZWb1nm6KmkETrH5GlKoG6K05E3ab06+MxATJGq9DDPN8REIpEiB3lsgL7fSd/rzXOSxW1bBo5h6Er/Y0s0pOvVEyQf16j3wwHV7HUYsfkvgXBLylNarZXVoeXWERO9I6S7mS/haJC9rSRhvSXrFtbHfchRCMuiRFvGYdDLTW8c039SxPUpopVk3iiq4iw1d1QGHVXEX08H9cBD8M16pE696fUs4ABgHEEaUHfs2lDOHst/MF2nwUmoiziQ+kmfKOt+wcwgb17RI9uaOuu7vGXu1+bxEIRQqLvEBrwwLhUZDvmjt9QBgwo5Ded9jhRRdMTQoNj02QyaXWuL2wrH3zQxfBlC4Q9yY96S7ruv73rSlXg9Os6yOo1Ka6vrwqD0XPXpYTQ21Nwv5CVKOlau5DUacOpt6aGSemY/ULRNFLGfYA3lAzRZ2bzvGxTYA6iIB4XX3gfHCTuoieGTnUDsho02nyFb10skMolYFLEila7FRsDXHasg8jvkOJwJKD+ATzuSIK9Xxw7xwhXV3j3zlRCbKbiisgbpWhoZbh17vBE1QvU3EBCQXxHoSLwK6znUetdYUwc0jqDGkpRzRqx3EiDlRplQTt6Z1t/NdhqQbQxCIbhrQvSJlBdmUhdttgmRNHuJTS009yvXB1SpLLpYgLOP70Mm5OqfWfXhQlDGmMJfiNl7D9aBlOlZ8r4tzpTDV5bRld/5uwCJla1m0wwpuNST5dF1PkpVAgxfpm+0GlrlcHA9axGhNv0O2DEzb9oGCIcmAd1dlvqPXfOCzkagpC/R1D25ACaj18PGQGgTw/52vXOwhk2huxrZrXiPQceLUnsfk8hKLodAHUmRw1r7bl5VYD/us89e4d4FIatsfaVTg56OGNBJkcOV2tgR5J20JKOepDbZD9t0w74wWsuzj8bElD6G13SpnhF2OPf7yl7cPb7+dS779W29bLScv/88OgF5nNd/ennieocV+9PnJ6/O/J9ZfP7y1YQaEeh12dcWQvB8L/d1R18d/5Rh1oTC9XmT6dkz6Ohnu/WR51fctq6Kh69vpa1cXz3cowI5g6JZXA7vl7dEQfP/+MPD3yvx2eNXXXxt/MWlWLe9GxFH2erxcJu/nfx/eoveXfL6iOPY1bptF1/cTeKAi+gn+hL797X8BAmeqta0tAAA= -->
