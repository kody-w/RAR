---
name: "rar-cowork-cookbook-ppt-exec-determine-sales-targets"
description: "Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_determine_sales_targets", "rar_sha256": "565721477aa04b6393d1d0c9081a2e13547774a1941a0476f022e0ce2540a983", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_determine_sales_targets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_determine_sales_targets_agent.py` and in the RCI capsule.

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

Determine sales targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 565721477aa04b63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_determine_sales_targets_agent.py` first:

```bash
python3 ppt_exec_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_determine_sales_targets_agent.py   # or on stdin
python3 ppt_exec_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_determine_sales_targets',
    "version": '2.0.0',
    "display_name": 'Determine sales targets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5626997349275e3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/ppt-exec-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDetermineSalesTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetermineSalesTargets'
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
    print(PptExecDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
