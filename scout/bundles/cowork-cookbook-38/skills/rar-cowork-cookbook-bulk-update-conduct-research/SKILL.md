---
name: "rar-cowork-cookbook-bulk-update-conduct-research"
description: "Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_research", "rar_sha256": "7517f28a3f41c0a0d2eca1e26a940cab8549bc040e5aed7ca58c378a4a5a1ee6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_research_agent.py` and in the RCI capsule.

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

Conduct research Bulk Field Update — Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
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
    "approval": {
      "description": "Explicit approval to commit after reviewing the dry-run preview.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
    "record_ids": {
      "description": "List of conduct research record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_research_agent.py` and embedded as the fenced Python below (sha256 7517f28a3f41c0a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_research_agent.py` first:

```bash
python3 bulk_update_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_research_agent.py   # or on stdin
python3 bulk_update_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Bulk Field Update — Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_research',
    "version": '3.0.3',
    "display_name": 'Conduct research Bulk Field Update',
    "description": 'Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f3747fc3c2b1776',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval to commit after reviewing the dry-run preview.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of conduct research record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when conduct research records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to conduct research records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.', 'example_request': 'Bulk update these conduct research record IDs in USMF sandbox with the new value — show me the dry-run first.', 'inputs': [{'description': 'List of conduct research record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of conduct research record IDs and new values to update in bulk in a D365 sandbox and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConductResearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of conduct research record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpvMbCICEKuirMwGEJLYBAIhJGWURbLvi1jEkp3/fRxJLzKyKqu6y2w+jcLChMD9+l3Puf6cX9/sro3K+u3zm+HbxWJrZ1kc+fXCLrwFV/ZlnYKvMnXA/4VbFm0dO11b1s3bhzfPb9w6rtq4LMB0pqqy2G8W9sLpsnQRxH7mLbrKs1t/0ZbzXK9z20XtN75duxG4cMvaaxZxsViPhZ3HbrPASGKx+d8Gpyx+zPzQzhZ+0cbtuDANZfNh0QCdnHL4aXGP7UUb+e/6redpvK4tqqwL4+IvQHTb1cWsilePH+uuWFS1f4/9fjGPn035MM8vwACgVhDXuT0b8e3pwg7a2QVVVZd3O/sEbPUHO68yv3n7/PPfPrzF4Prt869vbmY34NYbCyw2H6ZyTzP1l5VgZmYXIRhSjcDNBfhd+XVQ1jm45fnB4vXrx8bPgg+L//zPtLfrsPnp85di8fp8eZv/6cCI2eS2tJvW9xauXdlOnAHnfFowWW+PzXdWNyBKRfjpOfN3SWW1+Ov87MfnIp9Cv/3xy1sJVHiY/+Xtp0VZg/WAw8D1p1lK9eNPn7Ky9+sff/pdTtM5iQ9CCYQBrT99ff1+iQUDfx8aB4uvhsZzr7VAzOPKB8K/s2/+PFV/iXu55Otz8I9l9WHx55Jne/4K9H3moQPk/rlY4AMw8+1TUsbFj681QGD9wi5c/8ef/plYN/LdNIub9n8k9+en4Mi3PeCtl0t++vAI398W0Mu2bzL/+bIVSJh/xxIw/H25b476Z7Ifkf070VlcgKp9j+WfivuzCdBfFz//U9v+1YQPi+DL29rP4jvIOyfzPy9+faTIzz94v9/84W+/AdH/rRij7Gr3IeFrbhdx4Dft168//9A8bv/wt59/6CqQxb6df+3q7M9k/plfH+v8wYOvUT/+cS5Y3yzSouyLxbcaWvxaVv+r/u3T4mRnsff7/ebz4vtKnD/QYjbifdGnC76rxgbo+p0ff3r7DcBOAawB6DI/BvjxH/+xUGK3LpsyaBeGW3YAXTsAmLk/K3+MYgCuzQM1APr5dRMDx77GgfyfIzxrXAaLX/6P+0DSj+4L6eEZwr8+wfvrC7m/viP3L58WRyCzrGMAtgCjdUbTvhR2CLB6Xq+ax9V3gFHO2PofQSl/nC9mnP/lX4n9+pDwqRp/eXBP/MQ7nRNmrGu6zP80W2XNsP20wQV05Q++2wHhWekCTYIYIPSHmWLK7A6wcvZAk8ZZtvBigCaAtsaHbOClz7OwX375xbGb6EvxBGds8eSzBgYDvqmz+PgRmBRkcRi1XwrfjcrFD7/+9sPivxb/atZD+LyGBhjiFQOgoWio+wWoqS4Hw2buA2Bue48Y/Prby7FATAHYB0QsDmZCnSeDnEx9793Lxo75uCTIheMD7wLP5lVZtwDxF3H7aSEEi2/6gkXnRzMnRGXTLjy/8gvPL9wRSLWBOd88WZQt4Nc2boLxw6Jr/Meqvzi1/VAxB8Vtt78sFE4DDFRmM6HXL0YCk8siBu7/lgPP+0BI/UOzYN9FfFrs5yxcVHZtV1Ftv9YI7GdcAPO8TwfC7UXh91+KmWf92VWPkni6BwwCnnFfIf04xxyweA7q/9lMtO9j7Jknjw++rL8UzSvd7dp/tB5AlXERdrE3k8BfXinVRGUHupbZf0DTWdIrCt4rKo8c5P6+lZnpf7F5NDzPLmDxpVsiKL74/7gnmh3BbLc6v2WO/HrB74/65RmguUucA/lsLGdVQZY+i/H3ruUdmd4B+kuRxSDb6vEvz5GPsL7GPEGvq0EUdEZ/yAc5BZSZ5T5Sfk7hun54+kvxzgQfgCkP2ANWAHwA9TP7/H3BD09DH5pGAATm3793Ba9IzGgB0npRdU4GUi7wfc+x3RRoVc9l+4oyyH9/LuE+ikEMv7dqjhVIMyB/AZSIQSECtvj0DZ2fT99V/8PEZ/MzT3k0hh2o2vohAOjhzwrOONbHLQAvu3025cDOzw8hwIy8amfbHRDD/MPrpl/7ty5u4nbGyKdf/Qpg88f5+2npfNcfKlAqwFmgIKoOePdRQjO65KC1AToAFAGZkMcFoHrglJcTHgLtfMYDgLevbHtKfNx+GeQ/6m7mqPeJsyHznJn2FwFQHdwZv4eN45+lCZCXzyMe6/59pn1bbZY9Q2cD4A+s+P702R98elL8s4dYvMv9/A+7nh//vY3Rg7TNPybA50XUtlXzGYafRPvOs58AcMFPXZsH5358gsPHFzJ8fEeGP8h8mvt58e/p9QcRr7r4vEA/IZ+Q+ZH8yqvXB7iB+8hePuLz0y+F7v8OqWD5cgaHOWgjIPlv/Pc+BJBgWAOoAoOffNjMNNoDcHkQAIjAl+L7RJ8LDfBLEc6J2ZTfAcCjEQBJ/wzYN54Cj4oWrO3N7WLoz/uzR1k0/tvnosuyD28AO/3/Zl8281A+Z3Iz7+RAzYDOq439x693lJuv/7jL5QeA6C4ogvchTxzP8/nWAyGfqDrXy5xqfwe2s6rtWM26PTdpc1v3gKGh/cfF1McFANvF2geQlzXf5/aLq2au/q4En+4EbnSBPR8Ws+nNzK3AnbOpc/naDagHUAp/qsuDYr4+KeYfFXqwyh9Y6NUI2OGjXP8CsCGwuwyEDDyYGeqdoP50McDxX4ELu6fT/7jUXPXg+YszH6N+bH6axQLPZ4+FQRU07xY3f7rAt276H+VboKGZhXjl59mCDy/UBN9gB/Rh8W0zA3z42l4+/gxQdGDn/vO8kZpT6DFlvgBzwNe3Sd/+OOL4b3/7E72eOn+NvT8xXAbzZzb5J83BQlg3Tx6bY/snVj/EA6AHdDlr+rsLflekfGzvZkWA4u3zrxG/voFisIFM+1UOr/0BGA5w8WMz90cwQAuwIPj9rGvw7N/aObzmNpENulcwmSJQKljSNhbgqIvYiLf0XRv1l6S9whHXdmgCXzkugiM+Yfse5doE7WIUbeM2AYb5JJD3RIavzwoEImdlgBs+AnDxf38MbnkvQ56Kz176tlF5VPzTnl/fHBIHI3d4IzDPDwdDqAMvKUevHeiM0MPYW10lDXxrohg3xk483VR+iEqEZsV2jGkmVXVhmd3i/EBc2YlVZEZrTAg/UnKgHvfrVNczdZlTHuYN64NqjWI6XWlSo+Dx0vgeEa6UJrG7ciOcTSUe4+QcWeIpiKOrKMoypeEUZ+LRCoaoBh+DPW8YKNfYR0zCiCAPvEy8CV1miltL39TlSR4C0d9aw6mig0gLhsMd7oI96XhxpkRozsTX7Fa7sQ8HgdbGQmFchube9GhMn0i+3KOSe229q2tYPkIZU7xy4yN5Q40KYrxNepIc3thQbWXaZixDOiXa9CY5rfKlZ/HEzb0w8tW6tfG2cmsDuiHCiTQbXUwKPbhAR21icfWYjXg3ZaN3nwhSblDvLmMUMpy6JqHTTGX16GSRYxhF3vVgltK4jBUGOku3TQHxjnKq044bso7FM3uTbwd/KWzr7BBjOqOEQnw7NE6MdwY3Xtwba3j8qbIglVuxHRddJmHf5tLthKomv8TCO4cAC2W55GolcqjAHbajAXkj76daYJ+ace3tBStGBGNnM8TKHM3r5mLo6b2HQkkTNty0r/YNakgOZ3X7/kbaELnzNscmli8MQ9Z8ATWmULRyN2n3nQK19im6ElchH7cHlD+Z9ohLRdifxFrgC9fGpMlgmhERWgmV9WKbM/AS9ZGbfTb3w/ISwdLhTriSjUo3w7OKRArkwjtCTetUQjAeRjLhU1m6JdJd2BuYZUdyZlObfTmKu2Ej2zuoNsvzjvchP76cHHs9KHzu+SF8q7BLyR+mho3KYc1rNKJlA9ePXZ9wLqi9kTGa3QGtogM6VoyNNGtfybuzZ9a8n/HVybOdtdQQLXWruTLmvFSmLxeYSz2UKqZsozp7MSFIgd6bd0aH7VRdrgGqCdZhKWtxg2y1AyyTLe0Ul2xrdQS1vw6skqg0pDUdpihSVUTM6Rj24pHrN0e23+zTHGALvBnOa7OyWP8S0/BqgieNVi+OjQRLdhTw4khRblBm5xDviE3NNaY0MuPo8QfuUBfXuNMVUsp0n6xShy+PtXfg8T5n6UG10QKCQ+4c73WzGEPyekqn1SafWC8dilut7vKWXY6upBRb3revt/PBFy3LWleWIPtbOBlDKmaEQlB24Tm8OaGNcOZqtx1iYT94PnOObSVpJmofO7nmMmaZYz0J7Y+3qyrZo9BzYdwIpVBw0tarhZPgovCa4yGvWSVVoKQYY6mQhujlFa+SI9OiARxv1c3SYcbr/t4OVTflGbSxL7CTmTxvAf95pazyjUXjvLvPKp0/tAzZ26UBr5QxLM+ZQxIxFBZ9Sk9CqRCR4RonIuFLEdsaDcWtyXtMcC3CNoM+MOeSb+hux9HRKYLnQNbGNFSjTRFQnUqiZ3K12PWu4EiNeVz1DJt75b5aV/6qDsvE1s+MTCF9vD240Kqm8/FKt4cbHeP50t/BGUnXoXqWV9T1xjo8VxHWvVTQ3rekO8NiEclvr3eDP+sX1Ray9nBp1rqhSBusdXumPkpO33ahXJmctSVqETQjxeVwGsuTnznVUofZu7Y1LoiHijFLLCHZSKklRU/4QTltTQ7d7XRSXVKtN2IDqWfXzSHU7r16zkXODw6KUth7wrvsEYoOKHQXCTs/TbFGCNn7MReUXm+vqtDffXeFnNZMzuJ7QTGORpplh8m1LW7cMfuLzC/3HhIatbpGThOGmxZvKCsOGCJyO/cSuhErmIgZHYbYaa7T1kGooHCw5XFsU8UQLlvUWTPmvqGvrbg/G5GHmGORkndz68JskzgHXijj3N6GeoknzPZuEyEaXVpvxUStiiOGvTmsNb6+B1fWsMaCPas4dmcOS9eW1sXF1DSbHHz5lMPIliPbKMTUJVYF1FVpOktpquK6h/ziSsJ+we6YzVrWGp4OR9vTRb3KIG4jNxDCRjpFhfR2o0yBDyPpmrBwx2vXW34tlTLqa3e4Hm/oGVG1KoaC7HyGMXFZWR6xt8pprcDZdmDD9VrIit7D5F7gR0Q0vNOtsoUbc5DV9ZLHwmt1g/qJQU8jfShv+/2qu4FZHq96a5sKGf9AOLqSRiv2IGiGxe/jLVOmm8N1v05SSdoNAVHlJtKuYtBdjImwYiBHtX23T265okuuqHTF0io3p1ZFiwjDqVJEjfJy6lhmcHhNdNdQjKnn9FIuD6egpXaV7eCnCXF3B8wTOD6qj0hmlsay1faKIHFNtzwc8P5yiEUZ6+prhIS5HlZqVrlYP63jkffGyOnXg8jgCpNvLsG1Q7yVOjC8mC+VgXcSOtAPVrnmkShiB53Bwii3Mv9ssKKiXUkIIs4p459i2cOgG7S99Up6xGMVMW+nLhq3zU5IxAA+S/xYHqs0TGV1cFYZa8aS5PicWhtujsQCBrV7S6j4LMRJtCybXXlE9rpwTVA68YZzIYR5nWl7vAzd4zRwrluZ4e2MHk/1ThqUKdPW2iCGksCcdIW10hrr2n2WAMA5bodQOvM4bxKrGufOza0n5FHHRf/kBJ7SmjQP389mfHEEXW+cPG8J16TQ2paipV2n8l4e7CxOj6q3VNiYIcWpyCt5T2jdHrQkpXPFT9U52iYIVY4mCwmicsKW1yFzo7MVpDFDS/7mYErb2zXdyNtAkWhWEi81fziU++suTZA+Ou43kFBfBHOrqziMXqAbH2klyugmC68ziIz1JNRy8TgUkevuQ0wcr/G59yP6XpBS2WII1Fy5Kez7vpucE+RybKNeKnYSfWi1OiNek9q78iRlJWvQ/hld+l1+xT0q5q7HZiuucsm9xavoJlTpvlM8rjzqjoNHbh57nGsMXCqHZ4S0VStTJiO7mzEe95yNHktkOJ7HLQfgNlDY6+l6wEHbdVlLUV5JFXDZXloTXbTtCGy5MfRQH6synM4mvTlkwlEqFMla97q02lfySuo9R7QtxYYJTGQ23CZklVU9eYU/blCuZ0QG4UWZ6yK3kvMEPlyWpbajdqc9ZJNbiHQaGIL8K7pFRVPF+vM1p0vsqmI1dTZuwYZcZwoWjYp5rNQm3eV6tunuqHEgCQq+Wy7vrQukMtOKM1Ktw2KOjw9oWSnMNnOpgl111SGXS33Trc1hEE9oK0LTeoxsAT1bLeDDk+M5fqNvSi51R0csSwIlkdrPtltTBhGl6vKqK5e6EMOs3Rf2Id6cTD5vrysCVeiLwMu0oIq4xHHQCAv8JnJMZH9D2cC+CpNMnzbNBY1alnJOUmuw9zt/ppL82B6OzI0/+JdbvkGBbiNgcfs8qg3nS3SqxyeGPy6nbGqg6ECUAm7oyjYlq50X2C3NBwW66xQhuwu7ekQMbXNPIrhOMTgtnBto+tFzE0t4INs3OTpdZGVLwhIgP+10bInCEt3N1tzKp9VBJZjVwRys+83iMSFr6kzGY9AXS/dEv0TC+T7crrG2v1kGd8qWRaw5Y5XRk7XfTbus2bfJ2mUGL+eGQa+jzRFvxONxt6uV43aMj4F13u1MwSjihmVyDYdxVyVSoWrObCFsLcxGD0gtDVqkZFQIOh0P25hOu6oJXG1RvZ5qZSmHNK5LSZusREZzb0GQGIFVJtB48i2ZJvQ+Dw+nrNgPWnnsuaPN5DZ3stT9fSmX02Yn1ATKQN6xYs4rSi9iqbko/eBYrrHTx3vbcHprd9fBjq/KLs2QAy6eqXgbedsj5OmevNtxIQ23PJSnvUYkfgUwfnsGbRekQL60S/H2TJArf1lOxiHqYoU1Katgl0phhsKYbI9EUorFoG1x58ZPBCQox1ypDvKltmMKk/GSMkVzGU4MFtyKjbx3ZFQVNa+15Y6qudtBtrKbIrPVnbzyFXQ6Zlq3UlCYdoJJFWU3ksicR3eJFZ144eh1VEZi5vEShCJxiNk6jOzyAhBLM3Uc8reBeVGvik2e12FXcjC32R8AtF7IC1IlAzmQ18Bcc63uyyjoTwZItUeZ84lTQ20pgjAwFgkRnB5C6GIqnJ4T1zy0CZZmhE15WrMmOnadaKH3e77qcm1ZUd09HlvnknfD7tgfE0mCOZSQY76SY4k4HmVpwlY4xULHU4js+ROKHUsfrn0sCYu8Xy79UWBBXt4896R5lM5EhxV+Veqddu0mv1ze9hIx6Pw2DN0lft0Yqu8QNdts0FbqVBVe06Oz0fJQq3miZTp4p64wbkcbRr4pV5hwvFclvJLdgaQM41aQ6D1FzRTsfUSUxCppx0ynDOmaLhOrgz2sLsdupZGWYSCDFea4ZhDMRhJI4+bYRnSghNJLTCmnL2KxxYbRGgR2Re92OZckbUoVdmmjK++WXI/na3cB9O9Q036KmVizYURb8XZyRgOhEAWR5WOyPVxjoywUxGE0Jg15X9RZdL+dKMYpkQjTlpBKcdtmX2JE3GMHR6NH6mIEbGkW7p5it8uluGo8rdK0auWs6gu6BU3ANWwTXzQq3GcvJ0jN0WDfswSOomZBeX5QNkVe+m0GdX6iOizqefFliRXnwtVP4r6PEBLhyiCFWvZ4g6dTHGCd3rPSaWziZA8ah3pzR/ehEqBqOkzRHkXPJO7XWuSAtnyF7Q63ZUY7xLm1HNZa3RGKJ7M8o7IEkQNh3To6I7lU3oqBCNeMYAUbHt0slfjMrNbiflftz0sTbgLNGJfG3QsEIyjlYudcYGpZrpO8h1hbzxDYpkcas/abyN8mjQdzu1CRHb2/rpdjDekrGB5aaDAvuXrKEygoA9prGStqHOBngozK6m7hoZxagkTlyWFNjdQmNk86UfjwkUWZNc1dTzSxs+wpvlIBX58RxN52AhwJBOOmo0dhbVgEvp24VmdbVX6le+WU90f7zqLIrr5yI3PJuEi/rXKTcKb1rrkyF2VJX051D1dEjismlh1b1sVEiTXZVIdJ+Hw+B1lnpq4W+Viz832vbdORkRPFLJLTZVfCqO7K91vqoHevauBS9q+e6237Clltanu/Hr0dKd2w1CGboOmRwOaco88cxZAF//Eg8Du1o5QJj6pQsFcVaOE31uGGkGl0AhsptL5B57m696rkcsYSPiwF/Lr0SM3yTc1SLgkz0WgDBT5TnDvCLY94eKEu8WkY8laQmeuuqqGcWRm4FB+ElTBEfldbm8k3B/RGjtVUKpgVKqOvCctGKlScWzbHIjmgiYj194lP4uXuooaOUmRoRNRjgTWkATDiTFKycr/f2RWG9aG7wW9UQlf3Eg1Xja0fd+FqUEsLn/gdPTW0LN/y/t5jO7falEvSthUv8GNX39nUcD2dJrbVDph9usTiHUB2duvE8EoaiHW01Ubuaa+S9A0LCLDCkuWxgWNk0++ca+G26mWfT2kmuFQZWD5z92LOg1QwqZSCXaIurzlOpxSG4jBhbQffXg7wnTnnd4VEkIBAKoI6qBpbNVR/ngLi0MXoJrrttrwxrRHrLCNqd9Ysp2OEWOKdytW2cLNlrwzcJXAmZciJVa5JH2CqcotuCnW0dmRPXNArfnCWzF7zzxTFAbTOWwNeT11bTU6rezQx7VFiM0yUQtNqdXbxVZf5ab7LVq7qux18N01VtrSMJveunx2nsHKgbnUvDhlVQ7wzwyh9q0lHIAsnIM7nygVtutvdlKaPz3SScBuo7HPFvxpNsUk6z7+tQWt9bF27oiFpne6pdYUXiX+PisPd02Gl9HA4w3GVHhHWTXfC1TKhA1meUafR0XDJmgRoWskER0o4wca+a0IeJH06gqrfCBAqM8IhPGeggg9RBIsbrbxpylk8DCiRJmdRCxGR7w3LMwZ7V2m7gk/hTWptKTfW4nSJga0siSy3Ldb1MtPflvjejOiCrqildHczuhG8jlkfMdEP4iJlhfVhJ1ChQ5tMhwKW13qCv15tyDO1ZKCO9HJSV5sl6qRZb23YsW1tzLvC1XZ5wjkzsFq+W0O9spHoDrQ+p+o6yTnUtls0qVuHsJe3E5KIF8DEluoI94ReNns7qpRuP2C0LPQOAiHQhV4dsEAxTtPd9FrLqLq4ua9wg5ZKQI/JzYYTb8SKILR0QvbP9QawO52H6xuqcZfNNF3zm7VRKUM8edlezmhxohvygEyJ5cSSdvYK8tQFyj1rtRW5Vly4xqSu9id4254jYqQGCu7pK2wQORG0jJ7qWZyYR1LYyYyI98q2cY8raAUTAcqIQ2BKpCTHaz9025TE18nFK9RqaosrBrLmzu4pUkIlTSZvM/P0+yVRrdPSx9l4gnLJF+XeON6vW/3abdk8jurSBbtWhya8PF5i0V1I9mtkJL3Lyj7fG25SFP4+7kVny9sSP+XOzvDs6aC1cgr5uOjsXD9k+4PiNu2a5WTWbzweWU/5PWsYV00sAMBgv+h497VT6LbqHok1nknJGsUi0FF05NmAwh3SkGDxbZcGg2uz5NTf4FqSoBxOJJ8i4cAx7mrVnlkV1s9Qq/bYEoJZj0LJnQqXCNtCq82KI/DN2g2YKlrSt8hZkqezpJ92nre3MdAxUn1dUmA3V3byyoWjq7ryqlO9t3DtzmK5BLu1NzgGtSOq6BzfoUtUn/fDso9XXaIf9Cpfj2sZS+6yJ+1atZ2qIUEUl5gYAodUltkcWlisCs6+cGUS3gwSNIIGVbXqmh089OgMdXWxXFUgKHPCnYPXiLahnEAHR0vsShSqu95dA7dxpjLcEPCFsveudofOwSrWTkWpOCRxXU3V5h4YGkuY1I1FWsWpMfce1tWa4AXdwfg8knPZ5j3OPNDa5nLCpkZLKArfaAwm7JJORhL6fgCFZFTmJsxcBy6PKRlEaEStW/omeridDKimhYXLsgxZsRzDMH99+/A2HwS/jnP/R6+Pzac+/88OmJ7nRO9vhTxO/nzb+/xY6/P/TJ2/fXir3Rgo8zw8a7IufB1F/d3R2cd/9QLAPHN8von1flr8POlu7XB+KfktBuObth6/NmX2eBcEzHC6Zn6XsZlfd3XB9/dHlt8p//Y4gnb9qv3all9zu079eURczK95+F78HDL/DF9HiR/evNfrSV8xkvjq19Vs5uulAmAd9gn5hL399n8BYaEhHF0uAAA= -->
