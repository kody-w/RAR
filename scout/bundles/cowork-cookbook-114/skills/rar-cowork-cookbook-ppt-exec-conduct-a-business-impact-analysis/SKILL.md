---
name: "rar-cowork-cookbook-ppt-exec-conduct-a-business-impact-analysis"
description: "Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis", "rar_sha256": "5f9fc08df6ae76db2d2cbe2210816c940b6fae6809896958cb72b7733b01b7a1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_conduct_a_business_impact_analysis_agent.py` and in the RCI capsule.

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

Conduct a business impact analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 5f9fc08df6ae76db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_a_business_impact_analysis_agent.py` first:

```bash
python3 ppt_exec_conduct_a_business_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_conduct_a_business_impact_analysis_agent.py   # or on stdin
python3 ppt_exec_conduct_a_business_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a business impact analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis',
    "version": '2.0.1',
    "display_name": 'Conduct a business impact analysis Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-conduct-a-business-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2846f7c6a9881f3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-business-impact-analysis'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-conduct-a-business-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConductABusinessImpactAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConductABusinessImpactAnalysis'
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
    print(PptExecConductABusinessImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
