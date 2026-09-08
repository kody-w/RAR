---
name: "rar-cowork-cookbook-bulk-update-analyze-product-quality-data"
description: "Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_product_quality_data", "rar_sha256": "6d357e2ad62e92f5c2947a2933acf3083d6e913ada876a20fd889a9504c1ad67", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_product_quality_data`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_product_quality_data_agent.py` and in the RCI capsule.

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

Analyze product quality data Bulk Field Update — Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity / environment to run against (defaults to USMF sandbox).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of product quality record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 6d357e2ad62e92f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_product_quality_data_agent.py` first:

```bash
python3 bulk_update_analyze_product_quality_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_product_quality_data_agent.py   # or on stdin
python3 bulk_update_analyze_product_quality_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product quality data Bulk Field Update — Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_product_quality_data',
    "version": '3.0.3',
    "display_name": 'Analyze product quality data Bulk Field Update',
    "description": 'Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-product-quality-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa98d2999191b1be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-quality-data'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-analyze-product-quality-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity / environment to run against (defaults to USMF sandbox).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of product quality record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze product quality data records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze product quality data records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th', 'example_request': 'Bulk update these product quality records in USMF sandbox to status Approved — show me the dry-run first.', 'inputs': [{'description': 'List of product quality record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity / environment to run against (defaults to USMF sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many product quality records at once and want a reviewable dry-run preview before committing writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeProductQualityData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProductQualityData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity / environment to run against (defaults to USMF sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of product quality record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeProductQualityData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPaWLblX6Hvi+h0PmwjNCJ3VERLCA2gCQkQKF3h1DzPA5Ky67/3EXCdmVWu11Ud/alxOADpnD3vtfa54rc3q2vDon778qZ7Vr7grDSNQq9eWLm72Bb3ok7AW5HY4P/CKfK2juyuLerm7eOb6zVOHZVtVORgO1WWaeQ1C2thd2my8CMvdRdd6Vqtt2iLRVkXbue0i6qz0qgdF7XnFLXbLKJ8wYy5lUVOs0BwbMH+d30rLT6kXmClCy9v57VnXWI/Lhpgkl0MPy/6yFq0ofduHjNv22nqoky7IMq/ANFtV+ezJW49fqq7HCj3+si7L+b1D08Kf2F7flF7K8tvvXrVtFbbNR8XpdU1wAdwZ2GVwOTeSj8CXcBZb7CyMvWaty+//PXjWwQ+v3357c1JrQZceqOBy+eHr1RupePkqU93j09vGau1gIzUygOwuBxBxHPwvfRqoCkDl1zPX7y+fWi81P+4+M//TO5WHTQ/f/maL16vr2/zPw04NLvfFlbTeu7CsUrLjmY1nxdUerfG5g8RaEDC8uDzc+fvkopy8Zf53oenks+B1374+lYAE6w5nV/ffl6AEHx9A8EDnz/PUsoPP39Oi7tXf/j5dzlNZ8ceyCoQBqz+/O31/SUWLPx9aeQvvunqbvvSBfIflR4Q/gf/5tfT9Je4V0i+PRd/KMqPix9Lnv35C7D3WZI2kPtjsSAGYOfb57iI8g8vHSDLXm7ljvfh538m1gk9J0mjpv2X5P7yFBx6lgui9QrJzx8f6fvrYvny7bvMf662BAXz73gClr+r+x6ofyb7kdm/E51GOSj+91z+UNyPNiz/svjln/r2X234uPC/vjFeGvWg7uzU+7L47VEiv/zk/n7xp7/+DYj+P4rRi652HhK+ZVYe+V7Tfvv2y0/N4/JPf/3lp64EVexZ2beuTn8k80dxfej5UwRfqz78eS/Qf86TvLjni+89tPitKP9b/bfPiwuAAPf3682XxR87cX4tF7MT70qfIfhDNzbA1j/E8ee3vwEAyoE3AGDm2wA//uM/FlLk1EVT+O1Cd4quXYAEt1HmzcafwggAbfNADYCEXt1EILCvdaD+5wzPFgNU/PV/Og9U/eS8QH81o/m3J45/s57g9u0F5t9eYP4N3LR+/bw4AflFHQEQBtitUar6NbcCgOGzbgDBjVf3AK/ssfU+gbb+NH+Y8f/Xf1XFt4e0z+X464OeoicOalthxsCmS73Ps7dG6OUv3xzAaN7gOR1QlBYOsMqPAIZ/BFFoirQHGDpHpkmiNF24EUAZwGzjQzaI3pdZ2K+//mpbTfg1f4I2snhSXrMCC76bs/j0Cbjnp1EQtl9zzwmLxU+//e2nxf9a/Fe7HsJnHSrgkFdugIV7XZEXoNe6DCyb+RGAvOU+cvPb315BBmJywNEgk5E/c+68GdRq4rnvEdd56hOM4S+WWwC+KuoWMMEiaj8vBH/x3V6gdL41c0VYNO3C9Uovd73cGYFUC7jzPZJ50QIObqPGHz8uAE0+tP5q19bDxAw0vdX+upC2KmCmIp05v34xFdhc5BEI//d6eF4HQuqfmgX9LuLzQp6rE7BwbZVhbb10+NYzLzMpv7YD4dYi9+5f85mJvTlUj1Z5hgcsApFxXin9NOcczC4ZwIXnwNG+r7Fm/jw9eLT+mjevNrBq7zGeAFPGRdBF7kwO/+NVUk1YdGCwmeMHLJ0lvbLgvrLyqMHXFPAPU89cxYt5WFiwj/noOTMsvnYwtEYX/z+PUI+ocJy246jTjlns5JN2e2ZrnirnrD4H0dnYee+jM38fbd7h6x3Fv+ZpBEqvHv/Hc+Ujx681T2TsapASjdIe8kGBgWzNch/1P9dzXT9C/TV/p4uPwNsHNoISAGABmmkO+rvC+e67pSFAhPn776PDKxczdIAaX5SdnYL68z3PtS0nAVbVcw+/0gyawZvDdw8jJ/yTV3O2QM0B+QtgRAS6ElDK5+8Q/rz7bvqfNj4npHnLY3rsQAvXDwHADm82cAa1ezTnwWqfQzzw88tDCHAjK9vZdxs0UfbxddGrvaqLmqidAfMZV68EoP1pfn96Ol/1hhL0DQgW6I6yA9F99NMMNRmYf4ANAFJAfWRRDuYBEJRXEB4CrWwGBwC+r3p7SnxcfjnkPZpwJrL3jbMj8555Nlj4wHRwZfwjhpx+VCZAXjaveOj9+0r7rm2WPeNoA7AQaHy/+xwiPj/ngOegsXiX++UfTkkf/r2D1IPZz38ugC+LsG3L5stq9WTjdzL+DFBs9bS1eRDzpyc6fHqx5qcXRHx6QcSnGW/+JP/p+pfFv2fjn0S8euTLYv0Z+gzNt8RXjb1eICTbT/TtEzrf/Zpr3u9YC9QXGSiyOYEjmAS+E+P7EsCOQQ2ACyx+EmUz8+sdUPqDGUA2vuZ/LPq56QDx5MFcpE3xBzB4TAigAZ7J+05g4FbeAt3uPF8G3uf5WDab33hvX/IuTT++AST1/uUj3UxV2VzfzXwcBOEHQ1sbeY9v7/A3f/7zWXk3AKB3QGu8L1k8MHTxxNi5d+ay+zvo/fhO5i9/HzxlPSjDnd1ox3K2+3nim2fEB1wN7T+qVx4frPTzgvEANKbNH3vgRXAzwf+hVZ+hBiF2gIcfZx4DBoD2AKGenZ/b3GqSB+z/0JYHGX17ktE/GvTgnz/x1Qp86KO6yGdqf58lrODR5IsP4LhsdSlILrgxM9t3YvuhbjAnfAMx7p5Z+bPmGSwePPuh+flRMmDx4rF4vjCPGSDA4/wB9E3zHofmh3q+D+z/qMYAs9EsxC2+zJ58fGEueAeHrI+L7+clENnXCXbW4OVd9vbll/msNpfaY8v8AewBb983ff9TjO29/fUHdj1t/ha5P/BfBPtnLvrxbLEQmOZJgnPCf+D0QzpgCcC1s6G/R+B3O4rHAXK2A9jdPv/e8dsb6BlrBqdX17xOIGA5ANVPzTxprQC8AIXg+xMIwL3/67PJS04TWmAmBoJwF8EID7ZcHPZI2MccmEQJCyYRxHJ8BNogLu6RawRYuCFwC4Z8d7MhLRKDUGcNNhFA3hNWvs1jZTTbNhsGQvIJIJP3+21wyX059XRijtj3o9ADJJ6+/fZm4yhYyaONQD1f29VybeMwYet7e1njXoEeqfqgy1ru4e5wtk1Rrobcoak9Bq8hUi48Sk+1vZVYqZRkg0NwjUqp0nGDnqa937ln9nzRUwVO9oQ0BdNZMraH+lRCeLoknaobsGu3KdKWh09QlRjawTjq7PJgGEmEQ4Kp8+w4HfBdtYSiRByOaJHr/bSekI2mwYllmWfxoNmQ3+S9vlKWunorTL0Umpi6KuEth9dh5+63or0iYnIpXvo15PQDx+iHdbJnNQeSA19s8Q1XpM7Q7aLlKTiv19XhViE753o4mawfhQfLzevNybroncvcWdwSpVsnJJNox7UwDp1YG3hiH5c7Q78KaXLQzCoztEooPXaMTEy4NSOPpuc0zuGAcbdlxmBGcotr+Vrz9nrpXwl82cUkfktQ3++Xq63r95TDHzXhirK80KRBztnsQUK79ZScgzORH3v2shEQW5S3m3F/8kgdvGcG7GcoK/J6gtCUFBTT/lScgpWS+eO5caobccA30sWknL055GJnG3qTjkWvtXHZOuWYO8dIL4R6EmwKuYrQuuewtM+svlWVy3aKj2xCbqUIDpd+KrQH2tgWFzHT7rSJUYJxWg9J1ujcHbEGuOFWTSgaF7uIECrYEndstGGPQJCW6aep551MsC6uVRZBURnCmucKp0SVNDwOdInuYseCSpdNvJQ1jC1zxm/0KnbLo9l6427fa70Vju2xLx1sXfgHLbXcw4D2baYSI9tl4bKMqkLYHpN6L+j3eO3r4nQE4NOYu3Cjy1va7G84G8eOsyVMeD9SKCIeeIFbV50HV1AhicfLTQpRWmVVdHnecim+NU+TGZWOeaEqTm6sHZzeaCNsrPuugwlwWojOIa/UxGE41bTVYW1eamaxpQlBJ9ACoc/lBrPjjF8S1IHZjpd4o9Ub/HTenYaTfdyEjaHS+zQg6Q3qZUPlRldNK9VyLVEleoP5dJlw9yxs2c0xo+5yTN3TwLwM4U18/C+OlevvM3itDpY2GYdLiGRCla9Sf3lB4im3z+XyLg+8QPqr+LR0ianJre4SlPK+CZImN4bgjOtIfQkbTcMSJULGSGvGFG8vdM5sb/y4E3hhhThCvaErMQlN3D02OXKvDSnFNd0z95N3KRX41GqZc0+ZUNmWfHy5DAF+2TIIVeEkxfC9nzuK327EFBfgAWvvTcfIt4nN7kVPrSs5M6G9243yxPdU1YCWrV1OhZVcYO0Dsg1TuzyPLVSZBn6VdD0l9U10SOCQpFB2iWI4rySbuDNhIjyhrc1q55TmxqvH+oq5RUWtEUtyvcwKmFjeLg5mhiTsuoMhiVbbS5tIC4LlqGpX7IgVieUlEMqsDpecjkUZhmqMpK/6Gm/Ra6RNNuvmq93E0wJVrfmb5F9W9DJCSEgqMabg5YtpwyZmtZQiX3XbSmP3ml24OwGPFYQ2EHNgzDTeuh1FyWjZH7CoIkufUA8ae2CXNMVL1IAT+VpkY9Ic2Ts/BBCprHQETaELwk/D/WwtPSsOA+fMG7TsSOdmckTHjzOan8jsgpqRAVMWpOzjs5Ab8P3eNRJNMFtUqpP9DZfi47W82XshjDiw2ujzi0Hm0t3Gpmu249j9NV6qUX+xVF+J96saoqIKdRhydeUV+tIb0MSN01awPIqE16ODLZ1hUqir7I1j4A57zFPWaqx17kie7lEgU75G5yyRaemtoXlvuQ8DG3a5gMOPXJmlJ9PFFRqxClVgUGTjJulV3BoorA6byKM15xhcN71EiRtp7wtXPcN2op2YWXkMt24uIeVIkhBkAUjO9yaLcX4OOVjDALgoGfyMK65cYqf00tagvqm1FB4wIdwGQpJIe5Rdd84dNeGr4d8JO5bYfUY7W/jeEdftzRiOGVqbK4EshOOJuZ68epluQvcq0l6D0yurFVVNjsMOlth0Nxr7beYySUeoMUQ41/J+3GTn4kTQkrBB0nN0voXqaA5Nm8UQx4kmuznJJLFSjj6OuNemEJLWZGlx6d1Xd3zpq9ceJuX8NLgKGyE0nKQeyPRqY4gUS7lFYGwEylHlgwbYP5SvYnkkDlspQJGbH2+5qiJ4SakrOxLd/dTL2TliltRpdZMsIqb8Ass1KQnJIRZU3U7kkqOD5rjRcYZXg/NlN4icdjrAgsEaHGSFJaKeQXNnlVMcV5O1G/Yycb3GXBVdiaxuBCjbRKfrBinAcRnjsnXAWpivF9rNcqOcUPngnhWCQaibsXE1+yTDCEqlumGrgRNDN09i64mA0CUdFUOQ88feXjUjSod7UBAOL++yfN879xVN9pPYadlBDSVEz6iQQre7g0QyBUdKgqLayulsb4tJTQ4SvvU3/YUmDkiQ62d3fYHC83Eb9XdDv3QGu5QoM/M3q9LR3SN2kXXlHOqYLiYVddmFJbfV7QrP9pkfkYbTbrVDeb+Joo4BTk3lTYCueFS2976j3yLDsWm4PTCQ7gg3PFMS2vRZzih2EzuMLru7UjolO1upOrvt6jpOp0jkDkRQsfX2zElooZOrC3Rv0u0GvW9NGtSiraYgxyiz8RVyd+wMug2QIBUhfIlkgZVFd/EUB26NmuxY5J1XQ160w7A6SqiTczmO626HVNr+UkRXUomEvD+eT1SvoUekkdb7PlnuL1RzJ6fT4aztpv2BE5DbpaTPVWTcYoxHb8V4M5iD1RQiiDWT7K6ZLI9yqW0stJWENX2CzNUyzdCAJiIJNm8TH95at4KlxC3PZ6ty+xrb3xUCNxuByc08zNoOFgV4x2hUONYFvWzY9kjbPO33zFnSY1kkcZdPSdysA8S7o6mysXn9Nm2rOuHQrPO54QZZJbxrS53T9f2tvBe7ynNo368KLTSmluPIiKH2d7paM0Z0sNDuPvoNiRXCobUJKaFRfBJFwAbEQbFUGrp6a4oh2ipjk6NE1/fYRGgrCo5UKdKXHReMLn7SRZc+wvApQW2oj/vTGafO4OCDyXLlENZ0js/nZCccU2k7ClEpWD4a8NCe2OwjF+RimjpuKfn9KsSk5MC4Cc7Ym1Ny56Q+pWxiqa7PCWfEOLNfD2OlZ8N+lQSXJaBNtqqm+1VHsM1E9eW58w5sKmhJxaYsdcwjvdxpgoQY5ypM2MkMxmToTtQw7HWmxVbHeGxbil1f3IMYjuzBGvd8FxH2+TCVXCulUH+8UtF4u4yjMlmxIBjLPVpbWo6hzTGp+iu3M8Fg3NTllb2Q4kVFBSqRGsXR1l4VMGPKuApVl6h1mw5LNO2MtDsc4PMNMW5jW6dycvLF2AAz/Kk6pFmJIQLre+RAUcHe5E1M1bfb/lDxmV81dmUexyhFS5qVJEmmDpFxvJPeFsFkBtpSprhNGYTxEAVKSRheBtKmKPax7q4pbXndI0to6+Senlnn2ibHRFdgN11dOcyOxhDAwFRU7ZgNWTzc8G43TiIUwAGx7aujL/C4eJYu5DHlZbqTyvW0hXgeYjcK0+0EGN+VR+9C9trpSgrBpfQawVaj7EaY6G1ko0kRK2l7ofhVt4E5ivRuZ3VdH+9uBHiRsYg1ZtrpVuMvkC/F1mrDr6okIojdvYaHdILXl9Aa0Bg9GdqKgtpEYS/McmVSBA3jzaXsc4Tb9iJ6HSE1oDFBhvDJZ5LTtaMQ+D6QES9usCjIU+WOdqWitMzudsQDdjrG1qCu+Ynizog7IUNVGZTsXjYxIwHa5y44utW4JSen8VGub4MkuqEcQukhOpnQeB5ODOcVskQGMjPh0wnTT1u1u1DQoXIZb3e+7eOtAZ+ZRHBuBIFuvHhDuLm9nm5he4oEYUdczjCxk6+3234bshzDa609ZowjSUKMioLD5F15q23RKoi1ilb2WT0TyUSt/CqfxIspGgeW8QRL7O1SGo+2cj03BjX5kIudG2V14K+bm0ig2WrLjDdgNZ5Raz42ustOOLkdloHZ6+T0obk+jnR3Dq3ipnDT6Kl8Wq45NTlxVZIArYyIxicGGpueK7drfrOHVjfmWFddeC5QC9eupqKSVWuF+z611bhTrCvpLPXyZhyOq3TYH5N7p3gFtzy19Poycc1up9w4kRkPsEsQNRj8lczWiHjc2FaWFfyV8vtKIqg1emA4HtRNeor3W2TaeCtibfTb0sZLqGo81yf9PnHlbLtBLOuU0Qf+cACHOxLGxYheVX2KGOhU7IftsDcBigxLc5doFGNcfaYIY9wHAB12fFZWZbf1V6djnKfsNmxttW6lQOjaSwv5EDyiplWUOunqq1F2RoOwtlKMr2t4XOqO3SdVR0AxS23HqopPpR61xVXiDBomVdyKLztsHQhUlmx2ne1sizi91eGRamVUO4T4XdlfWj3XSlEpdQReqvGaMKfuAKXc5qio/ZC2UiPLKUPouxu8WXqU5K7TVXhDOVVcqsPNiagL1vmBaXjSJgnamrFMytLWCXyPBpSKqF3R4PvaIik7GAb0BJ9lPhGk64oTDV/g7qobQUeY9O+qsnSQo6dq6WV1D3EyIteljvcnzJdMC3aY0r3dq5MrLgsyqMkNsd5lmO1rJsKwrXZdnX3QcuYB8unLBr5uCEsaGr7C4X179VvvMmJQCAs9zzoXG87dwHKVyGtu8BJSUXFUsfMFq/Xu7K+Wuc3s3csgRajleqkTESv+Xp77jMkw6+Ifr3F4dBnmeCBsEgRtuNVKlbkHZC0QV/u4TaWy1nPIw4rtmCM6e3TTkr2vtMsp3dgplsuENECN3BZsPxG5dSDv6+UuJesjgdFqqyda6+KT3MstrRd5GOC8T207hk9glPPNhl2Nvb9KJr+5WJqemZWa46cVawfwzb5kQ79cFhx23nsAMg9i6lb6kBd3UY7P9h7Ld5NOr2V/c3CS9Y2/4oU3BUclKGydFjwsXlJUEi5PXh77kG6uypsc3crSzcDEqQ76jZBhkqhvnpyJMrc8KmyWr80p6yVHC9KhudtDWPf9cr9D9uXSHXtv6gjhSAfyimzrmughZKsrvSgRGdOqHd5MpsyPyeE0HBI12uz2zlRXiU309zK4VpNlto7L3dmR3JWWTI4ujysRcUlJQ4VvN1Vi5UER6OQo1MndUfueY203Ax12vu/kM9y6x6Au+lsw3gqyIQ/rtb9vrniY5axCl65X244n2QrB16pAiIqiBdrShi9yH4Y17nTJ3rk1bmMK58qJjpl6Vk48yQ/EOsz05IjTMUOquivCgAFtE2rtFBzRj/RUDghT3UvnAGZ1WlatoedOfQyOPfyu8JCGgl1+rHkISXnL2mXkklMxQPe+v0SIHswWqDgdEbnXff66JQSIyXwKj1ijnXaSgtUumokXOfSzXsGOotbBG6jAV6SAbpXejw0iz7xDlHVQM+wIj06v8tGZdhNU9jKemCZyY6wR5iZKsS8TdWoH62T2dQ5n8QGzQeTXa1k9lhPtGh3VgyHS3ShGIxcHnx8quKxQUsAQEp+wgcMsyxiQTWBnvWxBdw8MxGZ5VNC2aur7afLwTb9N2bDiLfzEMJBxZaBDd+UNu6OEqGKJklUtpOVok1p18SpXQvRM70wmb1RFqpYAc6MzD0MkmKdRzYYpWfUQnWGG3stkY0WeqrYkz61LbrBpjaTsOBHSZgWXtoOSXaCnmZ9uCEQg83F/rNFK3akhV59yMPDjppeq/foIDRufbi2k064XGj/Z/ojr8dEm1bgqVxmUXRpB8+/KRjjjGWf1+7CeyPpC7PAaTjzpkMI1fxtAy/utQkv+2iPoFsY7fjPGCAfbp/tqFAN5ODplatJrugpVAx74K3Pba9l5ta7U/hYrgi+OyzsV39ajzmNmcYxAQx+W49a5Xitum/Gb4DyGpYP56Yk+Z7rqosr2xIYpe6jaCPIjWlX21FKUmnWENT5rNl1CJvKy2dmIG4DT+rkFBceUKnZCpIs3tIR9X7UUF3QuRLAUyh1BrI6IjqCFYTb0xu7CUZrGFhcKn4nh1SrIGFxoC0SwccIxjNTuoF4/ETrJHE6NMapbxOCExBPbqwvDSalNntGlJ62dWgf1wdh2DhvWIglGSq5rzOYs+Xg1TtwRJ9jkphC5YcqdV7LIPUybaU3Z57SxwVki9/hpG0lguMUylQDHNzJDy8bV+YIYjP3ex1Cqak9jQh83MKmkWtyu4+tJO0Vrd9us9gokK4QfbeJ4gE2vtWu7oYlrhVPwRcHVlVApzWqwXXD8iEjfgSi5R1PTs63j0d2ZBaDJLiNHivMl5lDwRrPp1WVKjorrsds+UjABKcSD6cmBya1s0rpYAyIiIuFDcQdGl4i4Lw+lBVoKdZdLHQunbgewp1j1zdnR8yWn5YYYZqYQWMt6318N5HBdFm5b5pMQ31aSkhuqEWLTuUHiQd2kkT4ERhZI+2yEbKMj4knH6rrZGtiaEyRvd2IE0Xe0iDrVvLanwfGB9AOeKrSOMVdtgiP2NIX3NXMRlr4iMGVo+nc8D2tlDec3enlQsqIdoopvjDzwCuawGvGoL5do0vcm74vWxV2vMxCCarsacngfIhPGrG6eZl5J7i53SJ0XV5UK7BjlJAVJjnYHR4CyDwVelbWBApr2TZlxeVhP7uR6WrLJtMbTa7O2g27De7bojh3CtkQHZxnrCT5Wca2D8PZWhDEp9bjMVEWhV3BSgxwP4+xetfZHcsolik8LdEddtsQG0O6+DA4ROHodCnFzELMQQmWeRS7rnuuS0LyjTNye1LCls3taitq1VU9owUMBMJXDEnIMey5Sr7kbt0V671aYS8KCa3hB2NdpjiiF4ZLChmdPXXHV70PXO/pyuUzU5AbmTFfHd9WtLDRorzErN11efQVdqp0anDekE3gK2ms+7FJX+yLyGyK9cP3Sxj1qkIeM6xPlYNW765B5fO9v2H4kNtOeZiiK+svbx7f5afTrmfK//UO3+UnS/7OHVs9nT+8/WXk8WPQs98tD15d/37S/fnyrnQgY9nxQ16Rd8HrU9XeP6T79q79UmKWMz9+SvT+6fj6Sb61g/uH1W5S7XdPW47emSB8/YAE77K6Zf6XZzNY64P2PT0r/4NTzISk4s31ri2+110b1fCnK55+meG70XDF/DV5PMMH614+qviE49s2ry9nj148fgKPIZ+gz8va3/w2k4bGAQS8AAA== -->
