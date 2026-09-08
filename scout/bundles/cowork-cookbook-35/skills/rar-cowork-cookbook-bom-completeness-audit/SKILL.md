---
name: "rar-cowork-cookbook-bom-completeness-audit"
description: "Audits all active BOMs in Dynamics 365 F&SCM and returns an Excel workbook listing hygiene issues by category: open-ended effective dates with no successor version, lines referencing inactive items, zero-quantity lines,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bom_completeness_audit", "rar_sha256": "e4d54fdeb06905171e1d3ae595f8e28daf6abb40733655f8dea21e1d91fbd080", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
