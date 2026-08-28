---
name: "rar-cowork-cookbook-ppt-exec-analyze-product-profitability"
description: "Generates an executive-ready PowerPoint deck on analyze product profitability status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_product_profitability", "rar_sha256": "a57ceeff6479bfe5816ab2cbd5ad911646f169d0a797f9be5da1c99e5964c9c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 a57ceeff6479bfe5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_product_profitability_agent.py` first:

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
    "version": '2.0.0',
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
