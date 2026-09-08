---
name: "rar-cowork-cookbook-ppt-exec-manage-trade-allowances"
description: "Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_trade_allowances", "rar_sha256": "00d9d7d29d5886b6840fe88c64e2805bb43371cdff8bee22b067d23c5e7e8475", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_trade_allowances_agent.py` and in the RCI capsule.

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

Manage trade allowances Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
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
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 00d9d7d29d5886b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_trade_allowances_agent.py` first:

```bash
python3 ppt_exec_manage_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_trade_allowances_agent.py   # or on stdin
python3 ppt_exec_manage_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage trade allowances Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_trade_allowances',
    "version": '3.0.3',
    "display_name": 'Manage trade allowances Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3de1985ec7360c2b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-trade-allowances'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-manage-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage trade allowances reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage trade allowances for a 15-minute monthly review. Produce 'ppt-exec-manage-trade-allowances-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage trade allowances data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive trade allowances deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on manage trade allowances sourced from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageTradeAllowances(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageTradeAllowances'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'type': 'string'}},
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
    print(PptExecManageTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6a7ObSLblX9GcGzFVdWUbBAiBJzpikHiJtwABotzh4g0CAeKNavq/TyIdu6q6q2/fjpgvI/v4IMjcuR9rr73Tya9vXt+lVfP2+c2IvHLFeUWRpVGz8spwdajGqsnBryr3wc8qqMquyfy+q5r27cNbGLVBk9VdVpVg+r7PirBdeasm8sKPVVnMq2iKgr7LhmilVWPUaFVWdqswCvJVVa66xgujFViuGr0yiFZt53V9u4qb6rai59K7ZUG7QvHtiv2fxkFehV7nfViNWZeuuqwrog8rUTt+AFKiMvwA1gw/xoWXfFh5waJP+9Tfq2vwNJtWbZEBZVd1ARZo68jLgYFl1UXtJ2BGNHm3uojat88///XDWwau3z7/+hYUXgtuvWl1xwAzZK/0kshcdKa+qbz4oPDKBIyqZ+DEEnyvoyaumhu4FUbx6v3bj21UxB9W//mf+eg1SfvT5y/l6v3z5W35o/fAH2m06iqv7aJwFXi152dF1s2fVlQxenMLLOz6ZrELOKrJyuTTa+Zvkqp69Zfl2Y+vRT4lUffjl7cKqOAtHvny9tOqasB6Tb9cf1qk1D/+9KlYIvPjT7/JaXv/GgXdIgxo/enr+/d3sWDgb0OzePXV0JjD+1pNFGR1BIT/zr7l81L9Xdy7S76+Bv9Y1R9Wfy55secvQN8Xynwg98/FAh+AmW+frgBdP76v0VRDVC4h+vGnfyY2SAEOi6zt/ltyf34JTgG0gbfeXfLTh2f4/rpav9v2XeY/X7YGgPl3LAHDvy333VH/TPYzsn8nushKAPxvsfxTcX82Yf2X1c//1Lb/asKHVfzljY4KkPSN5xfR59WvT4j8/EP4280f/vo3IPpfijGqvgmeEr7evDKLo7b7+vXnH9rn7R/++vMPfQ1QHHm3r31T/JnMP/Prc50/ePB91I9/nAvWP5d5WY3l6nsOrX6t6v/R/O3TyvIAofx2v/28+n0mLp/1ajHi26IvF/wuG1ug6+/8+NPb3wDzlMCa/kVfgD/+4z9WchY0VVvF3coIqr5bgQB32S1alDfTrF2BvwtrNBHwa5sBx76PA/hfIrxoXMWrX/538OTxj8E7j0N13X1duHlxK2C1r08q/vqdittfPq1MILdqsiQrvWKlU5r2ZRkJ6BusWTdRGzUD4Cl/7qKPIJ0/LherrFz98q9Ef31K+VTPvzwZOnvxnn44LpzX9kX0abHOTqPy3ZYAFKVXHYlWRRUAbeIMkPVC+W1VgNLSLZ5o86woVmEGWAUUp/kpG3jr8yLsl19+8b02/VK+SBpdvapWC4EB39VZffwIzIqLLEm7L2UUpNXqh1//9sPq/6z+q1lP4csaGigW77EAGgqGqqxAbvU3MAyECQQWEMczFr/+7d25QEwJqhCIXBZn0WsywGYehd88bfDUR2SLr/wIeBh491ZXTQeYf5V1n1bHePVdX7Do8mipDWnVLhV2KXtRGcxAqgfM+e5JUPNWLQBgG88fVn0bPVf9xW+8p4o3kORe98tKPmigElUF+GdR8zkITK7KDLj/Ow5e94GQ5od2tf8m4tNKWdC4qr3Gq9PGe18j9l5xARXo23Qg3FuV0filXEputLjqmRov94BBwDPBe0g/LjEH7ccNoCpsv639HOMt9dJ81s3mS9m+w95rllAEoAyARZM+Cxfw/a93SLVp1Rfh039A00XSexTC96g8Mfiq+H/fprQr5s+aGnppar70CLzBVv9/NkKLyRTH6QxHmQy9YhRTv7xCsXR9S8hejSLoSVYAj6+0+61P+cZF3yj5S1lkAFfN/L9eI58BfB/zorkeqAqYRX/KB+gBmixyn+BewNo0S1p4X8pv3A9MWj2JDvgMMAHIlAWg3xZcnn7TNAXpvnz/rQ94gqEJF2cAAK/q3i8AuOIoCn0PRKFLl1h9CyBAerQk65hmQfoHq1ZAOgAUkL8ELgMpB+rDp+98/Hr6TfU/THy1O8uUZyvYg/xsngKAHtGi4BKmJahAve7VZAM7Pz+FADNudbfY7oMMAZa+bkZNdO+zNusWNnz5NaoBE39cfr8sXe5GUw2SAjgLQL/ugXefybLwyG3BXbYAEeTOLStBcQdOeXfCU6B3WzIfMOt79/mS+Lz9blD0zLClKn2buBiyzFkK/QvEXjn/niDMP4MJkHdbRjzX/XukfV9tkb2QZAuIDqz47emrI/j0KuqvrmH1Te7nf9jF/PjvbXSeZfr8RwB8XqVdV7efIehVWr9V1k+AoqCXru1SZT8uif/xVQo/PvP8429M8ge5L5M/r/493f4g4j03Pq82n+BP8PJIesfW+we44vBxf/mILU+/lHr0G4GC5asbANcSuBmU9e/V7tsQUPKSJkqWwa/q1y5FcwR1+kn3IApfyt+DfUk2UE3KZAFnW/2OBJ5lHwD/FbTvVQk8Kjuwdrg0iUm0bMyeqdFGb5/Lvig+vAEmjP71hmwpPLcF0O2yiwOpA1quLoue3578MHXL5R/3rurzwis+ASIHXFS0vwfde7lYyuXvcuNlI7AtACt8WFgZpDzAI7BxWXzJK68FQAUYXWzp5npR/rV3W7q9Ajiz+ApsBjD/R4X+wPvPoavX0GdNfpZ7wEAfVtGn5NPqbMjsn67xvd38xwVsUOkXWWH1eSl6H95JBvwGW4QPq+/dPrDsff/13CqXPdja/rzsNBZXP6csF2AO+PV90vf/G/Cjt7/+mV5PJvq6wOEV1L/XTlkYBjDw4uhPII+mF3SAvmDNsA+id8v/VYp9RGAE/whvPyLYU8yfegm0z1k0LhvTrAr/URc9+tZ3vUY8AVyDq+bbDYCM8DsXPevw0qoAIGYtqBI/PjW9AeilxfzTn2jwVAEwOaiHi29/C9pvrqueO7ZFWeDq7vUfDL++AZh7SzfwDvT3lh8MB8T3sV1aHQhQAVgQfH8lLXj2b28G3ue3qQeaUSAAhkMy3IUIGW4JAvdxAoPjiCACHIsQAt76Poaiu00QxjHhRxGC+DAORqPBNtpFBLbbAnmv1P+69HPZotOiEHAFCF8U/fYY3ArfjXkpv3jq+95jMfrdpl/ffBwDI3msPVKvzwEiNz6OYP7s8+sHHlfyyKjz5RSsGwFhrtXaZnuDhd2sQfY7Zh7Pl24OPFckuXYnP/LzfDxdj6f1SSBmc3tvmnK+M5VK5iRizERLm6FjbcICJ3rUuQQutOf0Uux0YSeeqNxNB25z5Wcr8xVtzsg59hwmcuYOHpSLvssxK8aLtRzHULaN2GslyxnL3m+n8eopo7Ax46Si7InlnEFO55seubboTFb96I9NacXZJdJQOHMGdFhvZfRYH7blMW1Km2SaQTmZwSl+bEjtxFjseNJ3+06xRCUwj/EmmCYey6hjmo/GdV1rx1OKJhRzO9K+wMzn3sqyq2pFF3WfrdfryA8RMxi0egYtuIry5JbcYZXGzQ6hypXVCxY7VIVZRhAj5lt26DiX4M5Z8bjnPpR00/qUzcGBR6ntYThPBdi53oT7Fr7LVX1jaSw6MevJb53dNiM2e/5ylI54SDgNfzRN66goangVDZE8F72MYfm94M5YPnYZNKkV0TTeFXYl7RqMCMn3xlQE90vF3eYKMhPqNI1amHF2HTfCSSzSozjTUS4UbsAyoTgdumkI+XVdniMqaOrrLTPH0lAHHLtm6kiXAS4X5owWN7YsjdSrZMnS97pesUJEp5dze/bFo3VWXQEvo+J2mntXpqBpyLejOrjGdkp5Rd/ad37sQ89L20tv13lfzApuQ+vLFT47G7EQSNrgOV0YbWYNNLU9/NqFmdHY+TwUc2FPmzrW/C3JTLJ/Z6fb4YilGJ757J7szqF+4RJ+JGTHzk0CRudtevTdy82GmZk07/uT7F9gIfTgQydd4MSPW6SwN8yWUUPHcLMzIqNBo0uHreHAPHJqHiUPW0JobFWsb7Eh0GMiOhsQNujRfL4SJxSDp/ZYZilSb2m3Vemrsu/pbRl21wBihXZt+jTur/3HqVt3gUbuVFrUXIkpZ9EpsVDuMNm2+bJzMdjQm+u1dUoidHNM2CS7AsPp7cgjdG6Snr3jidNIlPA2js3mQWGRGNuHFitm3RtDf2Yll1uHN3HLbG8xnpma25/PJr5z7lZjutp4pGy9bysZvewzPx9OvBm0txI6onJxN0XbnUbSqVXOLPQiGHMquRwfR1k3bwidHBhcr/DweJgogmjK8PGYeGWS8T2tCjcocRksWHM5JRJ1+9DozEUE7hS0YgVi/nDxm+uJR9vCauqhibJydZ1sI1eenezPV9hJ5JOJ9cMY4AYsAsqsFO3actbROOceFG6FwGWDhuYktQjQOcJcvwl2pdpqdXYX1SShym44jCoXIRzzYAM2LQ4nwd1SNHpU7sqwHyBMwDt9neZIvTkO1wccywwRH2kpuVEV3Eg+EZ82164+0eKca/kgnG/J6BQZExNkOPV3+aqE7pnWyItB1a1zxyx+GtZDBmfxIS9lCi/FQTmHzLm0N/pdwPnDUWdkXBoeil6O/iF/7PR+CPrH2cHKh5h7W+wuKxcWTzCL3upoYmiHTjmXB5TfnJMUidtbTD0MZJTsdDS5hEGbEI5VeC6DQwMxd6OgE1QRrLy4Wf0JL5ze7shrNzqPKY0UyjJPiUrEcC4o+JV5oKS6ZyxT4rF4R8CNhnep8iDGjLbLjNfpwGFNcSKGwyVHm2vPzru1dI1IzCHLQVCQA0/47TZz1cNDzm6pdogCT0ytXa0x2PVes7WB+ofAvGDE/oivZYTbPAQl4Y2gxHoHper+ePY9/R6wHaC+nD+N+dWdcv8gkLy0dwenJEfTcW/wBi8Y8+Cqp/nBPe5yXwAUGymn0nV9CK0c8GtzgZuEhURnzrj8pAqdRAsUfPKQEolH17seWf22hw/D2OeofLZTR8XuW5QJK+ZYc32KIwq94ZrWMUh32te6b28Pfunr7UW6yNjalpn66pYbPC6lDRnDLpXjVT5db3uRJbnCvuZEIQdT2JKHK4wYPAWJ62inITrVkz3H+8aUckpQ7XdrqAy1QoP8CSbi9XFtb+679niPDq6124p2IFG1vu9684GpnkXTCpuJtSOuYefo7schWUPHUD8jXsA3vZ9JvnC/cqO0p2lKcPjoeIwuLQkccZHuorfHjWLfJQnNUvNaqYIknU6ESikyUZYg1Wnzdj4Cmx7i45EVpDbjVM2qgaHmzVyEZQpNyBhXeQVJokyz7SjfRr7dolkkpqAoWNd6d4wZhfZtXL2MLlBvb4b3ks7l7UOGjPTmJLvtPqGjkltvOc1WT3KnDkN+J+ljtTWrKUBPOt/bUmv2R+/EZGyw3T/cDLIxFmV2DG+c4CAurtHxwVGFwU2ZQNANF822joVZ7UT2DRvWgkf5hXMtdOgGOZazKxikylpLehie62ox6CCCOIgPm1NRK7KwNRAblY6UkjH69ZSd5OsZrXQWaq7BzOK8aIyT6z0EkpGr5Bzxo8wLNmHdmba6ElfvDGAbHa0qV/NgXj+wjpoQwXavxIPQMa5IlNDUrOpOoo2pj7Mps3R74YrpkHK9Y4WQgVuPQ75z9ke1haQONIs9EbCQkm3Y09okrhfUKvwR69H71bPvxHzNHxKfbyRWugeP9kIze/hx65Te9meIcfHjcEKyUAkGUdek9VU6yRzG7M1oYhj93oQTlNx7VpgL8VS59e10PhvriwUn57vgjJpguIa65eskuxE0odvw6S7f00lz43U154CJqOLEQx29vUiyxxPMJZinQuEyv5pknd1AF1XcrgdJVVKlQYL2IpOySSCTE7MHREpOCTu5uxTvdt5wUcK7djOrgxBB5DoshdRWbyrWlWdeEvoDDGimTRoK3w7nw0Mp2eSwWV8EToCr/HBSU/NUY613vrKSTXrSgTvGDcvpJjyIQuL5A90l0j0juLY62zZIAdq9jfB5q5gnKurwIwKp60uiJIfW2GxOvkVQOUEL+X06TAZHP3RvUienFERF3kXlqac5OsFVe0MRO2JzP1GixR+MhzfQiLk9WjEGUEJViW2zFuMbawC1dPAT2bd78cSrmITpawjiYTIZOmCw0jeqqR6nNZxdUdi/K9S5K9aMKTWlUUhrMxYO2TnImm6q531sPgLYp0o8m/WMKY6n+F4wt8Q28nkv6hMUKCzOiu582Ju9f56mi75VWxx1REmEGWdzKyI28a3eZSn2kBhMLda8K1aay13WqlCfsEv5OFEXjBPGulp7xuOAPfJkePCe0B449FzFG49sDXpMJkPHIEPkKM11dqLjD1kPhYNTl2a7SYg83aVUyuLGg9oDZW4OZdom7reUfj4KRkq4dh5kuxLAn4g0F15HtECSe9sMzgg1kNIdqTQ5PD/qB0SFwN7I9bcTeuQVbG0iFHY6W4pPpWY8xqc+9UYJYmJ1TsMRxexdey6pbrgQ50tStxVZ21mAePexycUpt2MtM6meO0Sjc4R1ycw5hUoJMdlTaXrH1YPFyIF/ImA5GGvQFBvb457cRzLPG9S9yzvbRYwW2Z2OCI0o3Dq4yVAgqHCRuZY0cJZDamgtcroqpGZ7PQ6dVsFuijtEiqabfc843R2/skPbiTJo+T18Nj0ET7sUYQaOzTzUu8wCSlawfBdm60jEtLBRUt5zeZtlH3fDpQceFIsewR6uVspTdE0RyUiu8kae1Ktuc/OZZsSLzNvFmbqrfEVKNMyn2ek4ervcEMqZPTjcARbO1oWvOd6Y9uDHgzhTPkpmeL7Lhch2HscneFN23hnBBUT38lkXlNMRpSNp85ii4UgDPitipBfjaGfw+2B+SI3VM/PAGagAMRn5mBUxiPJK7BwV2aIw7AYWKrIz7MOSn1TJFq/LPWvlUhPWjiBykbZRCzPIDwy5CyiirXFZTdwWiaJzK+kB2OisK6hk0dMlNt3jXfeMfnRSZPaGqLXrrR1twg5wnBATmkgDRqbUXWul+ya7BNvOiOeC4R2D3QuXwLP6nAix0jXaYSjoYmdo9uHGwwJHtImKZEKzX9PVbZoLDVuX8U6dm20KF7c0QLX9SfL9ju+abu/KZ7en6tniOc/IYRWDzapu1zf9QusqRTObzkatMt1ByS577JtuvFXx8TjpRjP2PH3gZc0StqkD1TCTHkEBqcmaCMeEMuB9kjQXLPLvj4P7EAybP7Fr2zoNJzRv9PVhbmFtLWDoRtDjkBdVLXdIlOvoy1BvZlSQUNCXnxFuUDdaX2gAHhhqULt+xvh5FhJXJ1W1Zdf3Hcof4cs+F2m+l7lof2vS3pQtnRLqSmDCtpObLRsgwEBiu9mWvuKViJ2vDYJ54NMFqg6A3oYCvjd6rSDhHcak+7lHJNzcWKIN9gMVMUe3aA6nfWzQ7CBeAaKbxrc6Rl12IZ6XlxuTbSXEYp0zP5CKHcS51zSh52/M8hHURLQP45Hg0mhAblaAOBaaWNi52PW8rG92423gEk1qqsZ+hEN5sZU2wvCmgirnOjWoszljmxMMY5v8wdYbYWgf4mFz9my8j+va2qS4Cim6ZW3K5IZhVISIJaO16Mm5anphF0gTSw6eWdRF2GtisIbuxlo6H27axFrkpXogXWOldHk+bkiPhLypZ0MVasa0xqICbLO3AWZEUtqjmul20qOih3ZuLaXblK0vIlNFHfIxvoawXadp7GMaHXHUroIgbE1C435tHW7C3rptSIhxCO/A1SkKXXYSThZgy+gZTCX2xWknFh1/rRFpJzfp7livZW7TQ0m5ufckHN3NgBoPwemWX0/kgyX37PGa5DrPxW1+xU3YzzamCMnzcIuyduPzDxnH+alNT94dA5vaYN5J0UXe0qXG3PZFGvHSmpGdbBp0SoXYMTi3XF6dKkHbaXiE74K2Zvl97nQodXRK33fl5LA7sMJlTlmDx3opdUm4iUI7lO1g8h9Nk1bIoJVVJ+lDr1cxojv4PbaujxvnjfcDY5zoc3bSynLXXKV+liGwzc7Eo8/1nb5Jz2WjtggtN47VdhLksV7vWWJDw/sKvd6EsiO2aRhXSsfT0sjsFBzkIOMTJjunfLbPwkwwCiMHbSK3ny5xvkVjmNPFFKR9oMGkCDd+lm073tj0l+KGJ8m9VDilORQjndQVMxL+nnCFtXYz8sBIsfVIg/J1aHlJFT3kUQs7qHOuI6Yw1w3qKPSk+8W1Es2DbRdcYJbCCdcC4653VbpH5Z12mPG6lQhlQu60KIWkDKkDuo/W/MmZGHvoTaHC1e1Bkg3FXzutsnnID/5kZ7irWxUZk4WkbI7htotlZD27RWuv+2Tnyn4BvNxumFzfl6Fiu5c9mV+4R8BYrpPEoSbQrQSSW4CWhEX5WxH4d2RKxi1q2NeokTKu3mMonj2cY3cbKrUzNmx657mrwdPw2ZFgcdjzV3mgQGBo9X5+6G2ZJvZJA0ie6MqzziaHEYyuk7mzidrqRLvFnHqPcURbynNDbdodxjiyu5DsHveueDgBGeJYwyOeeC2RC/Ci1G/HHbnfcjKkueigVLsba96wi49oIwJfT9cS5e6bzt2RVnrkeWLwtkR2WDcH2AdlNsW3jlMHJql4UY41W1pcX0CLpET7plRuUkL4V6TAGySPZLHYNI7g3vtmaHojChUWm0MSi3jQWc/X4FJOUD6Pc06zQqF3F7Pm63TQu2mG8xHs10153UQKrmEPopWa416RHOs4gC2uobVqNK0ZeBz484GTtS1Vh4q5leazbEXusYNqgr7YB9DuW5JQRbMhqykNSZdeNiCsy+ANnPXkjuFEdC9f7cpXIcjIH7eBvO+QQ4RFSFztc/rxuBH9NdEPXjZR4TVOUugeaHq247GdLGmdmLSiBogqeWDrzDeG+b41D8nWRjq/xdbnh2/AvHhNK5Bam/WRsH0Ed7vpVJZE54rIw7U31xq6epNhJ26DBvKsQ37RCreNcLUU9/roAW62vaKUoF6UQx+huW30Omlw6oDdBi8bVJa5KLY+y9qm20q7bqIDMtdMJGttA7oe95ZYFkcjx6TJwizFwOoAO12KFu2MyYyYXcQ5R6/YhcpWYnY2Cd1RZkLxdR4V9K2Ix4LZxadtfO+RlJx3BTmPhEsa7u3s4xh9pCWWOzawo0aUqSeessak63ZDbGOca/Za5ViD3u8S9ywVFUqXA+/fdqA55vBo11vELO46MZe1grQR1Bm6aBfAxSSjZ3Vq1kUdTKnRbM2O3rfolZr004aQG29Q1m54o5GtHqWcz2+TlnxsqijaoBwUmNARy9uLVVf0wW1JduOUUACvfXxHFX2oZ/QuZcb5gKLMJWHwaTROsaKuOWw/iqyfT/HOFTokQLA+OF8EZz2MmzPCNxAfBIq76TdbStvqsMK2snWBMgKmNzO1g+zcIhWIs4LNHWq9W/PoPanLNNx7wJSq+lK8u2gU3rTolI7rid3vsAsfxPI64XLnurtvHOfknh32rHgoa7oPwhybELJunHrPoJGAvP6MP27N+dDMwS5Dm9LvNW9QnbyepYwl1bEbbhczAFueqCcV0LVKqkeagCqR0ANOcQptyq1zfW320taRmPxE8eemJNwuud+og4Dfj22i4GHBHvFTKK7vXqSE4uFRTLwW3WLaO3SpZuhZhfc8edLqPaPclYe0K+goZKIh3nH+fkjxYRtCyIW0oyQdmqJE1dwmySPBs2Zf8WA337fkvD70OZ/HKTsEhsfcL12lw4JOj4S1dhwVWmt9nJwJOkgiFRvMwcOZQb0bqiYT92u8ZrHoqhaje+0w4+jVcTkVJZ+gxAFj53Z7SPcURf3l7cPbb0dxb//tN7iWk5r/Z4dCr7Odb69rPM8YIy/8/Fzr839fpb9+eGuCDCj0Ovhqiz55P0L6u2Ovj//q6HCZPb9eivp2avw6hu68ZHlV+C0rw77tmvlrWxXPlzXADL9vl9cL2+UNVCCj/cMh6bsR4LJqwqj52lVfA69N35Y3/5YXMKIw87ro/Wvyfgb44S18Pwr+iuLbr1FTLza+H/UD09BP8Cf07W//F5bajVXHLQAA -->
