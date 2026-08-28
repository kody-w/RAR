---
name: "rar-cowork-cookbook-ppt-exec-develop-tax-strategy"
description: "Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_tax_strategy", "rar_sha256": "0785f2583c19bb211f3227466184e8f4180a8a1f14f67219dab133ea2dd3f60f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_tax_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_tax_strategy_agent.py` and in the RCI capsule.

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

Develop tax strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 0785f2583c19bb21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_tax_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_tax_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_tax_strategy',
    "version": '2.0.0',
    "display_name": 'Develop tax strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1c9567716130a91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopTaxStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopTaxStrategy'
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
    print(PptExecDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
