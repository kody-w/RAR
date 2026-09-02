---
name: "rar-cowork-cookbook-ppt-exec-analyze-product-profitability"
description: "Generates an executive-ready PowerPoint deck on analyze product profitability status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_product_profitability", "rar_sha256": "a57ceeff6479bfe5816ab2cbd5ad911646f169d0a797f9be5da1c99e5964c9c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_analyze_product_profitability_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-analyze-product-profitability:2eed47cec6626b410e0eef4d1cf26f49c55c114a617878f142bb4daa3bf5cfb4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_analyze_product_profitability`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_analyze_product_profitability_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
