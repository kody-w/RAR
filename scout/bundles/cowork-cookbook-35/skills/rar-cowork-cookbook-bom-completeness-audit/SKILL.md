---
name: "rar-cowork-cookbook-bom-completeness-audit"
description: "Audits all active BOMs in Dynamics 365 F&SCM and returns an Excel workbook listing hygiene issues by category: open-ended effective dates with no successor version, lines referencing inactive items, zero-quantity lines,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bom_completeness_audit", "rar_sha256": "e4d54fdeb06905171e1d3ae595f8e28daf6abb40733655f8dea21e1d91fbd080", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bom_completeness_audit`. The original RAPP
agent is preserved byte-for-byte in `bom_completeness_audit_agent.py` and in the RCI capsule.

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

BOM Completeness Audit — Audits all active BOMs in Dynamics 365 F&SCM and returns an Excel workbook listing hygiene issues by category: open-ended effective dates with no successor version, lines referencing inactive items, zero-quantity lines,

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
  Upstream entry : https://coworkcookbook.com/recipes/bom-completeness-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bom_completeness_audit_agent.py` and embedded as the fenced Python below (sha256 e4d54fdeb0690517…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bom_completeness_audit_agent.py` first:

```bash
python3 bom_completeness_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bom_completeness_audit_agent.py   # or on stdin
python3 bom_completeness_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
BOM Completeness Audit — Audits all active BOMs in Dynamics 365 F&SCM and returns an Excel workbook listing hygiene issues by category: open-ended effective dates with no successor version, lines referencing inactive items, zero-quantity lines,

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
  Upstream entry : https://coworkcookbook.com/recipes/bom-completeness-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bom_completeness_audit',
    "version": '3.0.3',
    "display_name": 'BOM Completeness Audit',
    "description": 'Audits all active BOMs in Dynamics 365 F&SCM and returns an Excel workbook listing hygiene issues by category: open-ended effective dates with no successor version, lines referencing inactive items, zero-quantity lines,',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bom-completeness-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/bom-completeness-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd3f2700c2bd7c7d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bom-completeness-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Production role', 'Output matches: Workbook of BOM hygiene issues by category.'], 'confidence': 1.0, 'deliverable': 'Workbook of BOM hygiene issues by category.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Prevents MRP planning failures and production stoppages by catching obsolete components and version gaps before they cause a line-down event.', 'expected_output': 'Workbook of BOM hygiene issues by category.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Production role'], 'prompt': 'Audit every active BOM. Flag: BOMs whose effective-from date has passed but effective-to is null AND there is no successor version; BOM lines that reference inactive items; BOM lines with zero quantity; missing UoM. Output an Excel workbook.', 'steps': ['Paste the prompt.', 'Triage findings with the BOM owner.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork scanned 72 active BOM versions across 63 BOMs and 252 BOM lines, flagged 4 open-ended active versions (F00007/DEMF000007, F00008/DEMF000102, F00016/DEMF000030, F00017/DEMF000031 - all effective from 2020 with no end date and no successor), and confirmed 0 findings for inactive-item references, zero-quantity lines, and missing UoM. Notable agent behavior: mid-run, Cowork refined its own interpretation of 'effective-from has passed' after the first pass returned 65 hits - correctly recognizing that blank effective-from means 'always effective' (baseline) rather than a finding. Real workbook BOM-audit-2026-05-23.xlsx with Summary + per-issue + reference sheets. Pure read against OData.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Detects BOM hygiene issues that cause planning errors.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits all active BOMs in Dynamics 365 F&SCM and returns an Excel workbook listing hygiene issues by category: open-ended effective dates with no successor version, lines referencing inactive items, zero-quantity lines,', 'example_request': 'Audit all active BOMs for missing components, expired versions, and obsolete items, and give me an Excel workbook.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to find incomplete or stale BOM data — missing components, expired or open-ended versions, obsolete items — before triaging with the BOM owner.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Triage findings with the BOM owner.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BomCompletenessAudit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BomCompletenessAudit'
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
    print(BomCompletenessAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
