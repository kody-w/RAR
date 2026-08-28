---
name: "rar-cowork-cookbook-ppt-exec-analyze-product-profitability"
description: "Generates an executive-ready PowerPoint deck on analyze product profitability status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_product_profitability", "rar_sha256": "bb0c12999104145f2248e2faf13a4a767658e54bb92718544b5eff2e198ea121", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_product_profitability`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_product_profitability_agent.py` and in the RCI capsule.

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

Analyze product profitability Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze product profitability status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-product-profitability
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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 bb0c12999104145f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_product_profitability_agent.py` first:

```bash
python3 ppt_exec_analyze_product_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_product_profitability_agent.py   # or on stdin
python3 ppt_exec_analyze_product_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product profitability Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze product profitability status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-product-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_product_profitability',
    "version": '2.0.1',
    "display_name": 'Analyze product profitability Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on analyze product profitability status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-product-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-product-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '860f46dd205ee37d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-profitability'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-analyze-product-profitability', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecAnalyzeProductProfitability(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeProductProfitability'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(PptExecAnalyzeProductProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
