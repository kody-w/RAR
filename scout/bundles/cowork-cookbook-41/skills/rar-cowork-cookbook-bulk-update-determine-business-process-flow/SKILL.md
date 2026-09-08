---
name: "rar-cowork-cookbook-bulk-update-determine-business-process-flow"
description: "Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_determine_business_process_flow", "rar_sha256": "189188beeabcf9d841ea75f070169b4dd5390173f0fc86a9cf41cb77b6837f22", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_determine_business_process_flow`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_determine_business_process_flow_agent.py` and in the RCI capsule.

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

Determine business process flow Bulk Field Update — Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment only.",
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
      "description": "List of business process flow record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 189188beeabcf9d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_determine_business_process_flow_agent.py` first:

```bash
python3 bulk_update_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_determine_business_process_flow_agent.py   # or on stdin
python3 bulk_update_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Bulk Field Update — Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_determine_business_process_flow',
    "version": '3.0.3',
    "display_name": 'Determine business process flow Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '76ff0e1e6136b839',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of business process flow record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when determine business process flow records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to determine business process flow records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.', 'example_request': 'Bulk-update these business process flow record IDs in USMF sandbox to the new value, show me a dry run first.', 'inputs': [{'description': 'List of business process flow record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many D365 business process flow records at once and want a before/after preview before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDetermineBusinessProcessFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDetermineBusinessProcessFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of business process flow record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adeiWLbmX7Hf+yEzLxHBIINErVqrUZFJQEBAyagVyQzKPIp587/3QX0jM6uiqrtu96c2Bhn22fN+9j7Cr29u3yVl8/b5zQjdYsG5WZYmYbNwi2CxKceyuYKv8uqBfwu/LLom9fqubNq3D29B2PpNWnVpWYDlTFVladgu3IXXZ9dFlIZZsOirwO3CRVcutlPh5qnfLpYkASjatAjbdlE1pT9/R1k5LprQL5sAnDRlDtj4QJWw+dj2D8bBQtgusrTtPsyLgt5PixgQBc30sekLcC0c0nBczArPugIqdxYSL6ISGFOBNYObfVh0SVjMvMsiSpvcnXX/tmbhRh2w3C/zPO0+AQPDm5tXWdi+ff75bx/eUnD89vnXNz9zW3DpbQ3MNB/2bUOwLgcWrV92HZ5m7YBVgE3mFjGgrybg6AKcV2EDlMrBpSCMFq+zH9swiz4s/vM/r6PbxO1Pn78Ui9fny9v8RwdWAu2BL922A+7w3cr10iztpk8LJhvdqQUO7PqmmEPQgjgV8afnyt85ldXir/O9H59CPsVh9+OXtxKo8PDEl7efFsBbX96AR8Hxp5lL9eNPn4AZYfPjT7/zaXvvEvrdzAxo/enr6/zFFhD+TppGi6/Ggd28ZIEYp1UImP/BvvnzVP3F7uWSr0/iH8vqw+L7nGd7/gr0fWaiB/h+ny3wAVj59ulSpsWPLxkgIcLCLfzwx5/+GVs/Cf3rnHP/R3x/fjJOQjcA3nq55KcPj/D9bQG9bPvG85+LrUDC/DuWAPJ3cd8c9c94PyL7d6yzOWe/xfK77L63APrr4ud/atu/WvBhEX1524ZZOoC887Lw8+LXR4r8/EPw+8Uf/vYbYP2/ZWOUfeM/OHzN3SKNwrb7+vXnH9rH5R/+9vMPfQWyOHTzr32TfY/n9/z6kPMnD76ofvzzWiDfLK5FORaLbzW0+LWs/kfz26eF5WZp8Pv19vPij5U4f6DFbMS70KcL/lCNLdD1D3786e03gEEFsKb3H7cBfvzHfyzk1G/Ktoy6heGXfbcAAe7SPJyVPyZpuwB/Z9QA8Bg2bQoc+6ID+T9HeNa4jBa//E//gfUf/RfWwzOIf33C99fgHd++vgP31xdwf52B+5dPiyMQUTZpnBZuttCZw+FL4cZh0c3iATS3YTMAyPKmLvwIKvvjfLBIi8Uv/4aUrw+Gn6rpl0dvSp9oqG+EGQnbPgs/zTbbM74/LfRBOwtvod8DWVkJugnoSQDMPwBftGU2ACSd/dNe0yxbBCnAGtDWpgdv4MPPM7NffvnFc9vkS/GE7uXi2e9aGBB8U2fx8SOwMMrSOOm+FKGflIsffv3th8V/Lf7VqgfzWcYBNJNXhICGoqEqC1BxfQ7IQPBAuAGcPCL0628vPwM2BWhTIJ5pNDfceTHI2GsYvDvd4JmPGEEuvBA4Gzg6r8qmm3shaGsLIVp80xcInW/NHSMp224RhFVYBGHhT4CrC8z55smi7BYtSMs2mj4s+jZ8SP3Fa9yHijkofbf7ZSFvDqA/ldnc8JtXvwKLyyIF7v+WEs/rgEnzQ7tYv7P4tFDmHAV9u3GrpHFfMiL3GZe5i7+WA+buogjHL8XcksPZVY+CeboHEAHP+K+Qfpxj/mjpILDtu+wHjTt30eOjmzZfivZVDG4TPgYRoMq0iPs0mFvEX14p1SZlD6aa2X9A05nTKwrBKyqPHPw2DvyTOWceHBa7x3z0nB8WX3oMQfHF/28j1OwMhuN0lmOO7HbBKkf9/AzSPEnOwXwOn2CGech4FOTvc807dr1D+JciS0HGNdNfnpSP0L5onrDYN8BIndEf/EFeAVVmvo+0n9O4aR7u/VK894oPwJAHMAIbAEaAGpod/S7ww9PMh6YJAIL5/Pe54eXsGTFAai+q3stA2kVhGHiufwVaNXPpvkILaiCcy3hMUj/5k1ULwB2kGuC/AEqkoBhBP/n0Db+fd99V/9PC53g0L3mMjj2o3ObBAOgRzgrOWDamHQAwt3sO7sDOzw8mwIy86mbbPRDB/MPrYtiEdZ+2aTfj5NOvYQXg+uP8/bR0vhreKlAuwFmgKKoeePdRRnOq5GD4ATos3sEcZBtwyssJD4ZuHj7y8n1afXJ8XH4ZFD5qb+5i7wtnQ+Y182Dwyu1i+iN0HL+XJoBfPlM85P59pn2TNvOe4bMFEAgkvt99ThCfnkPAc8pYvPP9/A87ox//vc3To62bf06Az4uk66r2Mww/W/F7J/4Eigl+6to+uvLHJyJ8/NYvP75jwccXFnycseBPIp7Wf178e2r+icWrTD4v0E/IJ2S+tX+l2esDvLL5uD5/xOe7Xwo9/B1lgfhyRoo5hhMYA761xHcS0BfjJoxn4meLbOfOOgKkefQEEJAvxR/zfq470HKKeM7TtvwDHjxmA1ADz/h9a13gVtEB2cE8X8bhvLt7VEkbvn0u+iz78AawNfx3dnVzn8pnknbeFALPg7mtS8PH2TtYzsd/3iWzN4DEPiiQuPzozluFF2I+sXeuoDn5/hkkz2p3UzXr+dzhzTPhA6Fu3T/KUh8HbvZpAUxx06z9Y9q/Wtncyv9QnU/XApf6wJwPi9kN7dx6gWtnS+fKdltQKqBKvqtLBmKYfQWuBoX2jwpt58b1IFk8Sd7nBDd+VPKHRfgp/rQwDXn3F4AIReCVN0A5pE1ZzF0eAGQ2fVcumAa+An/3T/f/WeqMDeD+q50+qH5sf5pFgzBlDx1AcbTvxrffFfBtKv9H/jYYfWYmQfl5NubDC1vBN9hJfVh82xQBd762qY/fFoo+f/v887whm5PpsWQ+AGvA17dF335m8cK3v31Hr6fOX9PgO4bvwfq55/yrUQGMBO2z5c2x/o7pDxmgJ4DOOqv7ux9+16Z87BVnbYD23fOnjV/fQG24gKf7qo7XZgOQAwj92M7jFAyQBAgE58+aB/f+b7YhL1Zt4oLZF/BCVzS6Wnlh6Hp+RAcrHA1diogQCkFJ2sODgFjSCEotIyTyV6RL+xGO+h5FeeRqSUUYBvg9QeTrc5wBLAmaihCaxgAlhgRBGGGAzYpckT5BYYhLey7hEbTr/b70mhbBy+anjbNDv+2IHljxNP3XN4/EASWPtwLz/GxgCPVgjPKm/Qk6Iaubc95JRmrWGKVTFGr1+869Ff6WEZPhjBm43bRrjWAvaZ5KqExqwXjcagkUH+lr0QcrSjY3+g4zSZI0VshmsxGLbXYnhvvqXuU3YpnTLJoJnYlPEtiK3MrIPteHKd3iJ/eEX06VV2Wn1Jq2mr3E4LQVt2mzhKH0fnE9RWTdZJfuOnyAeLRaJiGhKlmOH2ux4y8Yra9UZGdOU2bL/FRFMTKaVZ2ZZxSZcCv1i3OMIL4tiK2VZZy+3wqNFdR3aSvD18AQhxuL9U3vEFFp6YKBTTuh89PTZqsGQaIm+52RO6y6WtmpVfO6IxaoPur7Zn0bdv1wXe0H+kyEwx2Ho9MSgQedLfYEHcHkZU+Tg8ginbNzhXZzs3uzlvYurTVrQblcouTAFhV3IhIpvEU7pOZIlHTvO7sEjUsZWdswLj7LrOpSWltYyBPIvde3G9a/2RGT3ONSs8oqw9Cetz1JEwVLO7F9lkYr5ELiI4eI2IQv5V1VHCw3OdFiexX28piSmtUx6b0XooI43hSh4TS5InlEt3CmtM+W02StsFsJNmEbnl5TbMi0XWl4GstdYyFSbhlLVwTm0DhRJMOx5aXpetTXVdnr0l45SxWu7lLjtq4o9mhJbZjv9JrTw2sp5UfmsGru/s47lWrnojxd78xV70+IeU1o/yKZGMWtIOx8KPI9vVtDSzktY3E7gRnPZNWGOijaLvd98iJcI9bqLwlurblGp8TE7UW9TVUhVOUOa4qu7oztBtnZWyFk+NsROmzVo95ut4WXVr4kxdbWxZQN2HwzzdFU8M3JCzK706XjUdwPxrmyLkoU2ARpSyKnDTfGgndnqrbW98JRBnwSsPV2Iq65UJzwDe1o0Zptjxh7F867Ymrptbwc8lsNmpqlewcdkcsMP+fHAoo2bmrvzOMUMxdh2VwI1CeCmICDmISd1B8acoNFmRmt62OgNbZAeqkEQxV804ehsXInotdCG12yO6RGOHQaTiqRHTb3qzxuDMg3t2aC2nc+2iRY5ewOZaq3RiIDhLu27kWCtCQ6L+17zJ1yRTevxuD1x+upY+u76FyzYz2ER7RLxntYMxh2zS1COOqho9n2JVE1G5ECPhZv+xHoOYbrcLPrQ0oTj4jfYEK73DnE5rxu7+rt0GLr3qHHFGFzmFreYuviYKq9gdaI2WmkYY1hnLeneG8YNGy0iZD57SpGsKgPnXt51KueoSJbhEI5rRikbNw9vO8y1guUM90jIwLdQT+AN6LvthNMGbp7avdKVx5Us8QUWDxU3S4Q7uwEKxjSdPRWljptkg67zXRM96IhsNOxH0uoQc3y1Ab2iuVZfoxR9wy3+G3H7WEZdVzMqrqjHBF3zhI3W6FiV4Mj7nObEzGcuWHwyLaXNi/OeD3eLgLBhm18yTUZor3VxRVhRROJ3U3zVyrsWbgFmdhpOY2pAQnsMolWGgsSKDC58dTTjawfVZPo75yPJKIX37zimtWp1XTnWD9x52USB8zJODuCmw/yFLv8ZstJ1p5hwoukThdcIXDqwrFSicd9NFhGxvfLII/ELatnjEJAy+GyVCGUkqJLxWVGXsQHl6MObSGK9LrqXZ0obtuDCl1Xw+FWOAKlZnaTpJnCRPp6u+WQK9GIzG3Zp1dj2wdqzPMivzHcHa3cGt2Gz3ra0sq1cMvN3blHm1sIp+mYri8lwB2ZZOALu9lwrECWgjMlo4YSd9nDiH6iPWoTJxYzrQ/jJPRVs8F1zgtv25D174XunWtje1w2AqZYu+tar1OFTUCdM2KnmeHZbk6Rhu/vkGjmiam1qYUNq7K66qekK4RqiagtqPQ1NrRoZ0C38JIVgT2wo2QqsXO4JJdMJvIrVNwYPy9uVFDcSbqXTJAZRn67U7p4Jw5SxZZjDBNZDi3rg3Y+k+Ow3Ka3oYVd/8j0RBkoG1nmAh2OPPR8EK1ociE4HDwU3kMRfIZQ6T6INS5gd/h2bhkzGVkO2zEFc3fbEXX2qbcXz+KOc4QLodK4Mm0ulkUnOVOTGb7BJ1WB+mlcxwGrBrRLXQTmtI0T1rFWp16GtlgOcci0VgMqM9VDZIKZe91w+pHsq7PjeAaTldrhIjY7/yp1HLaJtFpvtkfZmQazuDeOftkHJnrhJN8jdWVLqPzAD5ydRscNOknkMdiap9Wy7JJ+YrJGdSFpI/ajrXDNtjrDUpAyleCsaMs2qtRgMYpy3Io+Zn2yTQrVvocFb0gO57EUmVERLXNidU1d0Lk2U1rx46Yl5dvhTk9N6aVHxNi1/o3VDDGZLrImKcNxE6Q7TR+X0t487EqALvEevtsniVkv18ftwS5CKzJNIWVKdstuimDLqWfxnO+Hm18maYrkIYt1fIYs82rDx9laoqe96+ctBNgYZatvyv0Om+xNdBU26tUD/x1Ooxyld1VPctNujJFWWVt19oFoxtsiJSX5it5kXkjdVGiFs0Yn09roujaF7NCsbncVlxN3zLagcZ+paBegd0535UOaxS2174r4yug9EwX5bqdBRpqZSzTzxnO1R0WXSyFpnRZqhispbvhUUdN8maihi6/r2s1rifWu7rjsjYY1lhWiszTJ1u6OOrDcuLUtDz6k1pk8R1JppqmbO2vjlt83nZa4K3PU1nXWmmysHMObQnLCFTWT2kGWzDIbKJ0Vaa5U6/gCYycvFbhegs/Zlg0zhMBgZ6ODAnRriYR6v7lQUZKPsaDe+XXW9dhewNijwdympq2gVrI00SvWUSEqcsZI+44M+IwmnSZehiOeqSuPD8+eUVNXbpVDUX8rEbc68V1HcgZIFG/SBDOXWWjQ9QapctdHSfbEhvHROin7S7hx+tUSk/taPDbJWMZIbPY5PYqFrk7KjsdOBkgLos/u5BCd1hPM2jzraPSQ71rekhiG3Em3ituOukSLN74RNwGLH06r4igfGbTNqvOtgQuflSWuYVKHsHPq0GVk0zBCsi41w84s0D8GmQ/jSweKAOtTb9WoHMRFA5wQ8krqgiu5PdPH8bbJT1Pc0XS2uhrrrIXXV6xt4mF15TGGmEqMqqLKNw5LWnUV5gSZo5XsGbM5uFp6FKSrZdR+kbFoSPhYMWn1ZdP516SpjSvs3CBdMF3xbJ2JXhn1I4KbSO7m1bFNPWdZ7/RsmU4rgWsi37wGVYPjspuiy2u58VMAsp07kYXh2HEqyLLA6bg4bVa36OrcmUQ627abDoqQOxlS6TdJw5JgR3q7/coUU+BD/FhCnBGiq4sQYdmeIuHwcKj7gNGg+x1ORf6U+uWdbcaYx45S7o2iIIqGn5NpKAhFlxyYO7lThJhyKm+UljuV2tqXaIzFlT7xO3FP7tg28SioPaV7+egd67Lj1UiuibvRnY8ZRHM4jmyKxHKzAJb5FCUCEb34utOuJSs0TdUYkDUMEuma9fOPwqsMKquzcZfKY6kcuMMNc5kGdGEAcXmHOKKkqUvhHKWmw1FBdThfbyJk9jWeyyHeolk8DSvO7EvrglUketaCqDWsrrcdkTmZV53bR/iaqiODOrJjg1ZZhU1Wyt2oC34H+xpNyUOKEdbSih+6aG/f7BwLg3Oe98S6KHcSUjQsaEV2g/uJC513GLZRlNs6KDjNQq8ZMFi2HJ6q41GQmQ0tVfQZcsV7Sgk+fT/0wTGfgK5mBstMpTvqTnOCJhXZAndyW2OwLmdvgyu2EmNKQmBejimbXHvThpbjScdXYkYLFaph+06+0idzsFvJ7NBAteCVzx8hur937tjCnrFmp9pxjbjn5F6u5R07chdet06JwuHnDMD4Suu5oEanvqPzcugGxiYxMd/WIeddTmsmPRFtl0lNVunKEBC1uemUvTlg632EhGUNdgvrtQbnaxhSByK+8lvBAGO/4hCol+gbZOmFTtKuq5i/sVBps9A5cUs8lHu3OhLkSlHLm997trs/W8rY9AJyR2Vv79SbvoRYKGw3vokK18bcWwGD9MccdpupVD0Cu1PUBUhlNqUiE0q/pfllp2KjFHsERyfkvdL5bV7r0pr3cowmKddb1rdOgA481tVuoOZom7YeIWX95SwTzp2Nya2Uq83JxO8wUtO+mQ917tQQiUYoPGE4mkSl5nitLPGiVJLpqUckJ+UKwt/Uu/SkMP5IWISM4nIvCox96+gWlIqthh7RHORd0El9aE/bVZHraqmtd5fYc7br7GZ2ZALvumrsuIGpzgO2x1ONEgRlq7gosVkxUoC6O0uihRuwUdSraiVrgcQf16YOWjQtO6QvO7dttN0d102OkLVMGHYwXklxvfd2WpRu22K77BSDFW/V6pzwfuUJW/kGLTWqzXNeSK6Yp98iERmY8zikqt7JwbQNdaC8A69EmvE3g0EVh5G11vkV71ZOPJWwPXqmAi9llSJTuz5kiXqzBQk6I+22hCKuQGGfLKGbjRyCGFW46TQO6sqHz95hXVlLzaGwlMDEaeqG6nRwyDqgnLULkYcQ6mP40ioQha4bYu/pKs8WLW0aJeQ1aL2r4ei4bIdsQivKUVmrO7oT7a7gi1npWJX0haVYFHmFNe10UPPB4aBJFvBrZuWsSupXnhJdSSeJ8LyOB2rlUvnSGkaDjhg+mJCpF4ac0chdTpv3hpa9vjtXds0Em+XELE9Cvd2LFWV0SEgimyYhRKnOJzbFszJe81ZOwN0NM+Jwf4kaOMMFjTqderW5r/nc4yNuHWzcpgsa2wmoQTPtPX5W4yVeSSLbYqPc3x16sCIYFgt47Te5TQlquzxEeAF3RtJe8aQzMjhgDkVjX4zc4oWsw7ViTeBBCjX7M64LJ2SqRoXWYCQIa4JXnJJgtmBm3vJsNI5+rBrHA91MyRFu/K3gKq5fbO7iva+Di8/clSEkMf4S6RtGwyUl6qdCCc84qYsX8brkOeDlFTr5duui7rJVm/bYpBf8QEI01Yr36/1yuPdETG/vXdOS2tYxeFFAT5vLNkm81A/MIurAXoOiJe8YDGmZs8OpTCQd7g2QTsdG1CPrQufcndjk7T1lDG1rptqBL6hiG/STDCnNuZYYhNbdhFobm2S8SrAnG11gT5RCl051O8a2faohjD+qU69D9ymHbhfW56L8lh8pxJl6fp8YEbs/eaxRSVfhqqTopR0Lbbc/bUqRSdBLviMmAu88pplsL9/3oKzQhEu4XFOaTTnt2aBhLcpUzlOwKlaogHdrjI6VYk3p51BdCeKuMvYwYR6KJdnTMDHkEGTym1Ckp9zIR7ai0JuaKOGa4mr5VAhjNNpbSsXq4xYOzsEkuVdFCJe4Aa3KMpapoVCae2HVfdOa8pL17GPGK7p/F6il03CkiWp2cfDSWqiSEwvzToiE9+h06BTbmjDicmoQRU4v6Zakz0xIIRyFn7uzZ1oQHwtYVeMrgVh25IWoOdR17dvSYbx8UFxkDCm2FitNRfS6bcbjPSTjfsp226uKnlFE1Qlf0Ug6DKqU2CBrs1aYgLSz7kYxzOoawdX9Lq4TW8e97TKWDmDKLsE/i7fh+ryziWR733ZLzbx5/G2wB0WlKMO1GmgMwtUqQJVTp963BwWKsN7zS7pTNkd1AECurogr07mgQQvMMBHlBVN9Gak6siEJKD1Hg9l1DVmKo9JhRHWXVwOCHdzl5Bpo2OnHlF+iO7k8uVfND3ynO/enInDRE7BVXbuUqVFgz2Vf2kNrhpgdQl0IXVmfCMEGnK+NYLywopHz07Y2LC44e1jgK2PCOR5ltRABUs2E+YkcmYtrTQZPSGWZ3s8tByG78+lUc5v2hDNImlQ+CW8Agk8i15+GTbI5hU6NjkgEYIRnEzhrT+7xPBym63KZhrc8Cw/dPotrljh1rjvtp+iun2Qr7GjK0+7tOs96z4R3jFBrHGPry82SLO9BqZ8BWF71LGsoUYMGvltigczjE3bxx2HnmryEoU0AFzmLoYfY0WkXMXCV9kezmeia7uwhZ1uPxBDXVnt0yI5OdTLk3aXhqzMBgnm4u+Ot5vBpxPjT2G7jUxVUMkLSuNj3joQf6s3ycJMwcrlGnPK+qadQi2EJTZaTN1pawHhkcN6rxYFFmN1eo8XRk4OTWtcm3JZS0GjIdYev+5Xv5zWPRyfhjIbY0JkkacMn5IbqRHmEjPLmwrvDqq5cfqn0p3W+vZxQMW/SDNE4g7MZVKAwU4UEQ9dCRMYhnt5TY0Ty6Ta8Wkgfsba1wb1qWlMYiQ/oser6JUQkp+B6X7lHpoSGuj+5ztJb7nOQ/DcywbYqWYtkHm3Wh6B0dy7ico248+kaa45Rxg/+CvNRiiViP196Jb93aSKFnFvcQYaonMetruXm3SXRDPN1uvKz+3LdaBRfsv51y+/3sJaw8WCqqbuGuIKEGXWrXXzuHnki2i+zAuzfOYCTNd6r110Gz9NaS53cgIkQjZTSJSeV4c31d6gW2JDS1uTQi3tqOi4dLDsFljMsPTw+4K51W4Wr3oSxtNV3Ublcd9Pq0HEELnM45KSMa/gHrLGCoLJ039LQxre6YcituKcgTnLEgW/VA9alxalE3dGGOOiuBGm/5OgoH3uEW43NbU+rY1dcZKZhiyPsxPkW8/fbZtACGe3FbqxpLGLxTstVmT1UHSJuYqYz+gjL8019ZsrDztpdRThXljq5UtO0SaiBazZaHKojC++drVKy1dYssaJbmRecEfrB6Z2DL1gTopMQJQe97O8H6BQFKW9cEFaBfRkj0PTeVfwVr2mUIW1VQanaWp5W1eooGN7S7BMpl1wu2JgavHSibHnvD3fqfuOisNfUQj5VW5JM9nR1vcb22tIbeBcW8TXy7aTB97vOIvf43dsWA7yFSU7znVIbGebtw9v8HPr1NPm/837b/PDo/9kzrOfjpvdXVh4PHEM3+PyQ9fm/pd3fPrw1fjrr9nh612Z9/HrA9XfP7j7+Gy8rzIym54tk70+zn0/lOzeeX79+S4ugb7tm+tqW2eM1FrDi7xX943PUP5g2P0512/BrV359vPn3vjwtZpXCIH3SzKfx69nmh7fg9a7V1yVJfA2bajb79QYEsHb5Cfm0fPvtfwGhUevQPS8AAA== -->
