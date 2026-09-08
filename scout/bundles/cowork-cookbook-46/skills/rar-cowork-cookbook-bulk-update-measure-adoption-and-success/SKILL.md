---
name: "rar-cowork-cookbook-bulk-update-measure-adoption-and-success"
description: "Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_adoption_and_success", "rar_sha256": "35daca2cb44b6603d1a2359e3a5a0940cd338c63068e9179e921ee292f349bc5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Bulk Field Update — Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of measure adoption and success record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 35daca2cb44b6603…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_adoption_and_success_agent.py` first:

```bash
python3 bulk_update_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_adoption_and_success_agent.py   # or on stdin
python3 bulk_update_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Bulk Field Update — Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_adoption_and_success',
    "version": '3.0.3',
    "display_name": 'Measure adoption and success Bulk Field Update',
    "description": 'Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c29d68b57be02966',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of measure adoption and success record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when measure adoption and success records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to measure adoption and success records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af', 'example_request': 'Bulk update these measure adoption records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of measure adoption and success record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of measure adoption and success record IDs and new field values to update in bulk, and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMeasureAdoptionAndSuccess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureAdoptionAndSuccess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of measure adoption and success record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G8N2Kq6so2iE3gGx0xSCySECAhBIhyh4t933fVrf8+iaTXVdXt7umemE8jh0MCMs+W5zzPyTf59c3q2rCo3z6/XTwrX/BWmkahVy+s3F1si6GoE/BVJDb4v3CKvK0ju2uLunn78OZ6jVNHZRsVOZhOl2Uaec3CWthdmiz8yEvdRVe6Vust2mKReVbT1d7CcovHjIeCpnMcr2kWtecUtdssonzBTLmVRU6zQAl8wf3Py1Zc/Jh6gZUuvLyN2mlxvYjch0UDptvF+NOij6xFG3rvtjLzNFY5Lcq0C6L8AxDddnUe5QEwzK2nj3WXL8ra6yNvWMwzZsc+zBKARbODflRn1sPA96cLywfOeqOVlanXvH3++a8f3iLw++3zr29OajXg1tsGuHx9+Co+/aRfbtK5e3k6CWSkVh6AweUEIp6D69Kr/aLOwC3X8xevqx8bL/U/LP7zP5PBqoPmp89f8sXr8+Vt/qcAD2aP28JqWs9dOFZp2VEKYvNpQaeDNTUvp+e1aMCC5cGn58zfJRXl4i/zsx+fSj4FXvvjl7cCmPDw/cvbT4uiBvpAtMDvT7OU8sefPqXF4NU//vS7nKazY89pZ2HA6k9fX9cvsWDg70Mjf/H1cmK3L11gyaPSA8L/4N/8eZr+EvcKydfn4B+L8sPi+5Jnf/4C7H2mpA3kfl8siAGY+fYpLqL8x5eOuui93Mod78ef/pFYJ/ScJI2a9l+S+/NTcOhZLojWKyQ/fXgs318Xy5dv32T+Y7UlSJh/xxMw/F3dt0D9I9mPlf0b0WmUgwJ+X8vvivvehOVfFj//Q9/+2YQPC//LG+OlUQ/yzk69z4tfHyny8w/u7zd/+OtvQPT/Ucyl6GrnIeFrZuWR7zXt168//9A8bv/w159/6EqQxZ6Vfe3q9HsyvxfXh54/RfA16sc/zwX6r3mSF0O++FZDi1+L8n/Uv31aaFYaub/fbz4v/liJ82e5mJ14V/oMwR+qsQG2/iGOP739BgAoB950zuMxwI//+I+FGDl10RR+u7g4RdcuwAK3UebNxqthBLC1eaAGgD6vbiIQ2Nc4kP/zCs8WF/7il//lPID0o/MCfWhG869PHP/6AvGv7yD+FaDw1xeI//JpoQL5RR0B3AVwrdCn05fcCgBsz7oB5jZe3QO8sqfW+wjK+uP8Y4b8X/5VFV8f0j6V0y8P9oieOKhs9zMGNl3qfZq91Wcsf/rmAEbzRs/pgKK0cIBVfgQwfGaFpkh7gKFzZJokStOFGwGUAcw2PWSD6H2ehf3yyy+21YRf8idoo4sn5TUQGPDNnMXHj8A9P42CsP2Se05YLH749bcfFv+9+GezHsJnHSfAIa+1ARYeLrK0ALXWZWDYTIkA5C33sTa//vYKMhCTA44GKxn5M+fOk0GuJp77HvHLjv6I4MTC9kCkQZSzsqjbmQWj9tNi7y++2QuUzo9mrgiLpl24Xunlrpc7E5BqAXe+RTIvWkC7bdT404dF13gPrb/YtfUwMQNFb7W/LMTtCTBTkc6cX7+YCkwu8giE/1s+PO8DIfUPzWLzLuLTQpqzc1FatVWGtfXS4VvPdQGM9D4dCLcWuTd8yWcm9uZQPUrlGR4wCETGeS3px3nNAbVnABeePUb7Psaa+VN98Gj9JW9eZWDV3qMjAaZMi6CL3Jkc/uuVUk1YdKCxmeMHLJ0lvVbBfa3KIwfFf9btzM3Cgnv0R8+eYfGlQ+AVtvj/uYWao0LzvMLytMoyC1ZSldtzteaucl7VZyM62wdS9lmZv7c27/D1juJf8jQCqVdP//Uc+Vjj15gnMoJIuQCElId8kGBgtWa5j/yf87muH6H+kr/TxQdg/QMbgeEALEAxzUF/V/jh6dvD0hAgwnz9e+vwCv+8IiDHF2VnpyD/fM9zbctJgFX1XMOvZQbF4M31PISRE/7Jq3mBQM4B+QtgRASqElDKp28Q/nz6bvqfJj47pHnKo3vsQAnXDwHADm82cM6VIWoBklnts4kHfn5+CAFuZGU7+26DZcs+vG56tVd1URO1M2A+4+qVALQ/zt9PT+e73liCugHBAtVRdiC6j3qasyUD/Q+wAUAKKK8sykE/AILyCsJDoJXN4ADA99WwPiU+br8c8h5FOBPZ+8TZkXnO3BssfGA6uDP9EUPU76UJkJfNIx56/zbTvmmbZc842gAsBBrfnz6biE/PPuDZaCze5X7+u13Sj//eRurB7Nc/J8DnRdi2ZfMZgp5s/E7GnwCKQU9bmwcxf3yiw8cXNHx8h4aPQOvHFzT8Sf7T9c+Lf8/GP4l41cjnxeoT/AmeHx1fOfb6gJBsP25uH7H56Zdc8X7HWqC+mLFhXsAJdALfiPF9CGDHoAZYBQY/ibKZ+XUA2PJgBrAaX/I/Jv1cdIB48mBO0qb4Axg8OgRQAM/F+0Zg4FHeAt3u3F8G3qd5Wzab33hvn/MuTT+8AfD0/uUt3UxV2ZzfzbwdBJUEmrY28h5XVjkDhPXYKP55r8yOAOgdUBrvQwBAAhmLJ6jOtTOn3d9g7Yd3Mn/5++CpmdaiFkRrdqSdytny555v7hIfgDW2f2+A/PhhpZ8WjAfAMW3+WAUvipsp/g/F+gw2CLIDfPywmAPTzJQMgj27Pxe61YDKASZ+15YHA319MtDfG/QnzvoTWb36CCt4FPh/PcjrnbvmDAJbZ6tL2+/qBB3CVxDd7rkef9Y4wwR4/mLZx6gfm59mdWBR0odeUCrNu+PNdxV869H/Xr4O2qFZiFt8nh348IJZ8A32VR8W37ZIIJSvTeuswcu77O3zz/P2bM6ux5T5B5gDvr5N+vbXF9t7++t37Hra/DVyv+P4Ecyf6edfaCcWe6Z5kuC83N+JwEMVYAnAtbPVv4fjd6OKxwZyNgo40T7/3vHrG6gZC8i0XlXz2oGA4QBUPzZzpwUBeAEKwfUTCMCz/+u9yUtOE1qgJwaCUNy1HAtxbAyzCQJG3ZWFoDjloRZuwRQGOy6Kkg6BwgTpUas15VHIyvMQCvFRjLIdHMh7wsrXZ/0BkTi19mEKjMBWCOyCpEQw1yUJknDwNQJblG3hNk5Z9u9Tkyh3Xw4/HZyj+W2b9ACQp9+/vtkEBkbusGZPPz9baLmyIX1tK7UNGTA5ToPelcLImm7brgl8cla7nXPeM6pSYIRicRqy4XExjFSTbcL1OeZpG9n7twMF590an8ziGglNicDIhXIGjE6dzhYz/zTKI3mn4rEn2fJgKJowbePjdA+P4XWIAc8PGlcdzZU2CdqaFYqcpdAkuUzGEmo9KLJEUkWENFSUo1dDEYVruIGYkTP63LnQTFZPlHJ5xKVSt2VJjSZiCbERtCSW6CjcOWG118SQrY+dNAlrarn0YlbhW9lAbt7Y7atUkFxhx/uGbrBl3spwshbRfbKsonvkBjvF5PTMMYrtWEmhHE2F5ll8d8uvrSXepmnCcoVmnUjdHDWUHxNnCrypT6yYxrw+n9aymsJ2p+LLY0LZ3X2HoiNTtJFPZ0go3AVXu51domvoI3eLVkzmhElO0Xc/EsVqheghzlvnUWy3XNvkZkdXanm2g4DTtjtcO4iEfC8jMuYkTZQyjBK1cuscuMHYezZ/tmr83B2WDHkJdStjiYncCPe9sUVRUW0iKHUuayRbo5liWOm1rPipiNyWOW1JPTJHgTMF5dqYRrHPr/vw1uuZLpR8O56uBNN6LWRuoihCFS6jg2O/y+X+ugtQD5ahk0y6kxWWRmxILJtaQ1YkRaz5G7gRtnvJFs7EOnQYBMS156d9hYrZ2cbQ5Tm1jeJg6HBGVWy1EimtlqULccu0kqzyaYlcoX6vE9aOSIRuCA/bqWqGenvS3EOuHbhaUFifjfepXt1CORcVYtfvmuwQ++eOHS7WSiKuzHKlr7jA2vZ0cmL3WAnx03SFe/p49I577T5UBUePbUynq/oswFJ8odPl3dJs+JJc1xHFCUf3Zmso17naVS/2uyZE+8MOs2I5v4nOQBzNKnH79HrnLhBt1BOHFW3gnjObCRpSOJ1taU0BysHale6ZxKnsuBPDwyQ0DAg5iAVa8jeGXonMdsUzG/Cf4YpUPtJXdDLb9k4arCNF6c3FoyMKdSfIcTGSQFaC3zCOMp5yCMags+Qxzfoa3gT1Yu8PxwOiQPjJazMB59Siwer7Vbw7SbJxjI1P7wOIVYJ2s+wLzcCYq364wGIWmnIf6p1plJtDld3DplfdJrZiBw8EPgPZcow1rYyIS8B3576AA9FhsCMtG805EvzITLY2ubtgYc1hzpLVxGaZ30VMlKFbhsfIWZN3Lbnp4pxIVXbbpCJbHGpuvy3xMx3Tmi5cpSNIDNXawYfAWJd54o33UMYZd9zuRgexolrYSllHHkjnIk16fDNUO4bksUXJa4oXdwbzxyy9Dm6FBA522TRxqNCTkV7tK8wUtBoWq6jiN+pJRrQYp1KT28jplTUVM5G1Bu9voXpOWG28oT2HaXAEK3ofsCxnBdFuwhp72vEGonJpbhsZd7pDuZgKl4E3rfFGJ9ujahpRpPS0AJZ/Z8VwFFt4BWBFG4KLdY7rQvY9CVGRhjCujh6SsC0x/tR7q81O5pZUu6S7iOfxW1+4h0FZHnt6gy7v7IHqZRZScs+6pe1538SXSHK4e38e6FoVtGHsaaXkLx6P14Jws92zv1LZihLQXdPLTGdJm7G1K5rl7hSppWbdoGU+npXBPNs66R0D6N6n4YgphAICcg5OPX1issPW88+iaFoSzlxtxJhOq9pH7gPBIRmtFc7GrBhZNM5KeuvY04U8jMVIC+FOJAPlIunJVLE2c94YZ4IZs3N+OXbdtlUGP0IcaBsNkQKa6S12WorlYX+LYoa9waKJ3KcwGiMRbVfLBkM7ayMVpsIuMyMRqTPCmiXsjJDg3lWVuJzXrlPBLTFJanAZp/2tABTDbK2tA7YIO1WeCBVhbMs8F80gDDqyQwlsjPRLhrbqCd+lzDY634jd3YT9YqdVk1HrgUgDclreb7jdxhv7APp8pcvPa6lXMfxk2DC59+hKM6kgZ2VbrTaCdM3Xezib7gB2dlzGkYD3+OWdKguJaodhbSHioVs2ul9UEKjce9XjfkUqLrTsy9pauUiSOrHUQOT1uOfABiHQyT3tnKTtIS2UobFqTRn1rbkZ+wDabV3liiAOXXd2JBkHuJfS68Gxi4AJfL2ROFqmMaU8O06y3KCctLVD0ZsO/HZfiF44Kqabc6GemSo3Onpss9eQxk65qV8JFqsZ1U0MbKXq+/oqD0sP9fLLdnVbIVof7JtqiNU7g97CKcNPuWQdHOYs40fJh6sSOoSTKF74Yq9pEH+5Hu0+zHiYlxHeEFg2Efd2k1/kU3KumvN+KnIS4m/FeSCcw44oDld6HwWCGm3ibE3Z5/VVbRKbwflR3IjtuLudWeuMiP3+7Ce0hFtaWe449KDJ9Wl5dJ10klsh3VxtVPPrVBFKQT34JSinY+WEtsTTg0NqQrSt3OlW8ByKGZxJ1wWwuAp31To5lKeIMpr2chBKeLsTlQSR6eSI88dOHa2lymHpOWmSmmmt604lgzMC7bGzcyTbaorkjXhP77Y0Ss1Zp/1GNPWqtqZ+tcq3e+GG39aXKy+LhU9RGpI06YXEqK2lmYhhnzRe5jCOOuV6tDeOEZLYiM4RblojeyurVsI9xtwaM7lLqXQbTNxEIo7XUSKpF1S58Cbbi9m9CNUTIbHKSUmKbGOCRqVpqvC4kqPWN2kmSogD3TiXa7w9IOzytlITrTrc9jSAwu0tOwt2UugH0EVe4DyTJEIqFdLCWnGvbXrYhJZphgWbdSQi5u2+G82NyyLnyI2velWV/bGWCnmNeM2NZsQ14DHI5hJ7o+yHPa7NUAF7xZ5qixNx5IVLwNnU0tkdqLVZR6hH71OZtHL9Vl2qNcwHHXHWxwS2yhVodyL+chG2+FCwldJsfb8qrqN+b3meirbBcVBKbRurnHQFVXqCNw7MpihH69MmcR0p2zOhnyrSMSDKltcOEMqp6kVjEPLmYQZ+ogf8qF0F0Hx6wtE4tAcf1ZkaP56V2IfkA10VhrM9gD2v3dwRo2t1ut8LweZggUmpQMIuwcjo5oZaRJkr5oCuVKqH0PtaHpByGyJ4QIpIflgzCAVdcNBX9GcyTMjudonsA5QEw0Wmu0NXXXhD7SnsHsSFbCiDcpWEc2Ff62pJb/isnejLeWyvl9U6PPLwJt2rThbWDF9H53x/cfzrKeKdS+6cx4vo0G0YJdN0oEqvhCyHPvKDs9QJZn8YIriqOtAOmHyQXG4Jf/RZd3O3zKUs4JO2tNWLkTgbXUPSWjtdKJWZWJQ57urI2tI0ThaXXRyonHxX5fKo2se8tGO6zXlplfWmLfTEplDVY3fmXFL2HMboopzbbumtrsg1o3HSanelndQ7BMp5yxzWt3EQl6ER7ffdRRN5n6h2/slq0WR7quTzLTz656hPAM4Vh1us4lQFX5H8fkq0CCem5jStk/iiw5c81V0O2Yu4B5Mtp21C/NZG/NW/5u7Fx+hes5UNiJBCKizrtUcs3BzYYZLg8gaje1wy/CpgkqgS9t7u4G3s/Hjk+KFRruPav8EVfepNvHE4ggz3fs2n4ZqzmkJvkXqC0SOcFXUd7GMBIlkUvSgaFWHO+jbha6s6aDfHXO7rkxsQurDbVsGhp3w50Lpa8kxTGzdr9VJfY+nWa6CmIf1GNqa93N7LpI9DaeuZB+soOBElhhzLFzQZcKhzJi6iuMsl/kzcs5wk8hObGtfqDt3YSbrdfHpCDfayx6d721hKa/Pmxu5MkU9K2LyxijaUw5jv080wDBmOkUJKFeXIIgLpsNwR7yaeJTJot/SEXbE+GSVB+UihXotou5UPoNPNN5NIwGOkCexWkdxp6i1RHAJMEy90PnRunTdm0RPHwvP1vhlwdbg7gr8UtJN0jLDLqMEx0mFINRSJjtcWz98zewpPVp8Y5W3d3wEPsmsY7QB0HEz9zDckIQ5VaKmt0UAwDWM+tjV1cQBJk1U7JizwXYxjJqUEuAM5d/RW13SNxSoDT43Pl8xqRyoYdGPArmY0dbBxJc6GKZ+YrrVCqS/sU9zJlkHR/vEqMBLmE7dkf7GMHYsw0AalFdHhBvjmbn2VBeSM+oavpketNY27qXOtit6YGtugGu+HlhOEjJquuG2gxaXl+ozXGyHbMtd1baBeH/roHc3ijW/3B3ZzvoRTFEk81HYRFvhWvjRiE1nROWK2Ks+xAwkKZFPwyjnOEciCjxvbvtVV3I3QWYvyIy2lcYJyhlXTpuHmyZUSTuO9VSJbVaDWuJR+c6tWSc0v8TuuDXJgV/jJ0s80Q1flwYsJoQkDzKdPPgyVsawzuUqfaaJl4eW19uFOkLOwOR5YMYEYa+Nf7oDvqD6DVxVqrl2tua/243bLxtHyrEg9mZMn3j/4kA4BqaceinZ0sO/CaqlI0zhtlQvSXMskLnc71ZaPu0Teb7YRVGRtk2zWZhoru77w+LOEgZigYXnnZdja29YaM3KPNxpll6DVsbhSWeitAzyUe7LPRSr2pKSKbffQZOfBHyR8cITId9pT1dZhjB7qZXlCCGeI7dO2WNprynF5D2FSbM2Ofd/1MuZX1zVbl6sk1aGSuPH5tcxrXuqbeLkFpmmpfAvq1ZWDSImecs1ThY5HjdIQZGokbdAVjHgn1wZsDoV+Onfo1K38A7Re1ZyAXv1CX952hC3QV9M4WVOmoPBec7zpWK2aku1ESxCusWr1cqmaicelrRSsSBxZBp1L9fHBvwUn+cis09IzDLe5H+/u+VpxmCWP6LCvgxFvu01ysrcQuUahtYCuOT264rwV48sMGhFsk/ErswmhfuITnbETGt6Y7rG1jOIEHRt9o3S7zrtSInfl/aGclqczgaqcelsTqbwu4/M47khpt2eSDIcssrlCxJ3141WtYKZuy9RKaeAcGNVucGRf4NaobK5CbKZLnRyUaXfVj2LP8wnpY/kd7M4Io0SxDo3SYGK3pVH4a7Trov6kgg13t464tS/DyGQyXNScLkrVg2ZcVkkDLxKIaEO356udd2sxjRtW62WqXuW2MnYC7Je4QfSnYkSg7cbeVpJS0uLlwJLeKWql5Vq4F2Mf7dOhBPvjXcamq+050W0uX9UVoqfrZkvpojNVA0Vb0tqMlLWP3DSD2JnqMJG8ePeWWHtlM7++D6Fd07EWCvmI2ewt3wTLsCE2e4L2JuYsYnY52t6yE9grIgnSHTQiZUAkeD3eTRbZiIhGZ1BI3cjTbastBRHfY+1hRWHyeJA12+Phwj5aWe4TiXeC1tGWAn3E2dniiCHuLOJmr/Rbb3BXdoWdGrsKPSfeQKBfjwiiFE+UFKKCUpmtgfS7HE25fYlSpEU5DhtrsDthOhZZsBNg9jEzea9oOXiK62nFrWV9UIb6bmXWlmrW6k2i3I0+3dDayBmzKw8RIxNEMA0cqg52Oyha6m0YmJLkUTLQftftYstHyFUde6iMkltnhScIEsLQShGtwwrsmHIvQkzEagljL0pnbI/cMDkjTa9HppEcXJrbrc611+AY7A7Dcb+DEL+JA3d1VXmMZKm43vdVK8LXkGpOuqJ3e5Yajgqakt1A2qtyrfUbEi0tcr02cv/kuBqkNGfo7u+oKkXl0zrxOVA7XofeT+aQXxtPYDagci0Sv+fo1kNbc+0bqYjuSBtZ4TCHKxFMrCg5ZOAOumBE5eEul9rT1iDjeMvJZZJdPNtqUG7VUV5FhXysto41LsUxd20k348nvvcT+e7bzNJU1t1RGgcXTzEe28vXqSmxYHXua/QW15uGL+6Cm612q0Lp+T4d3RttNlvc3JBbWFCoCuF8he7u8YoJVWYJOvTz1XP6SxhX9wNbXVS8T65ZFMWFrnrQYT8Q7IlsI4yq+QOpZx2sIL2zHtzA08Mrl3qYWouHHGo5b2zXBkq1tBTItoev7g47RKUyMCZ6o32iqZGbPC5lRojXR/i2jZdL6Lw8Le1VgWA1WVXMcBO0dn1ZH0/UEdmW28nG4L0LO5FSFGgLo/aUH2XcQrQ2Q8WVWkIXa3XRA7NGHXFSIDttzGy1iTXJjO+dPgZ4J7k5Uk553+nrJrt0FBFIqb+SHBtbW4kZrg7MYfAvaOJ3CEtB0Vk62sJoHpetyF4F4B+hBoiJdZTblc54MVBXBTS4dXrmlEj0WsnIMNbW1nJlJyEsILm3YjLZR3xeNSAcCvXjsMTdibQH8QaV5OjYy4ie6GlUIoHi7nnAwjc+dmVpCXkQmRNBMEAV53LSpLRnWV+68XJsu3V6xVGmW3eajpYspRXU8XQkmnTZeKSL4CVQ6WGbSF1mIKuOg66uTV4xO36TRUo+LFsBQ/AJkty233oKb+/wECZGAu5PtpZhzsFPugsi0vD1EIuIFxAcGnjWTqKo4ILKxbhhhuCGH+z1lr1sqTNxKHbZ2a8dGpO27XBrqSZB1p4uy1lyw3f39Uhr8q6Gdo4jmatuhdMnXIElrhHdGxRhMLPKQ22pXzVKgniNQkd0haSGq9q9KBFxT1lt5Lfk0oEQKdFdUHWM3S5JYNSw57HlhmFanOPRNmn661TJRGWtOjGf0FE9oyaVsom3xqHt3a3Was1b7bDzmN7ROlxfx0h79+4q33MnEmH0zo7B8LXEx72qinka6b3pVQRwrHXHihqgwzko77lI79ICY2lti5JZ5hzKQIjkbXksjuTh2GUwJu44VJN6vktDc8DivFVPYbtBhrTcj1f3xAzFDg6ijOLxlJrCno9ORk7FbbEaOgh3IWRP6V4Q9nWao3KiU9Se3HFqV+wuw9j17rTcdskpOYdc71wstru1hQIfFGYgtaXhy8Py1PXBlWScwJOxXvERijZs9SAHJF3FPsm4/uWcDWOMThzXu6GKrU/x4JObzrMrrd4wNE3/5e3D23wS/TpP/rdfcptPiv6fHVg9z5beX1d5nDB6lvv5oevzv2/aXz+81U4EDHse0jVpF7yOsv7miO7jv/qWwixler5H9n5o/TyOb61gfun6Lcrdrmnr6WtTpI+XV8AMu2vmNzSb+SXe9wP59yPTPzgFriz3+QKKV39ti6/Pc8r5fpTP76Z4bvT7ZfA6wvzw5r4Opb+iBP7Vq8vZ7dfbD/OafII/oW+//W/5A9FBQi8AAA== -->
