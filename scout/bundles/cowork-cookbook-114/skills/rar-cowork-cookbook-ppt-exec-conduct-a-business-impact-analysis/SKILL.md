---
name: "rar-cowork-cookbook-ppt-exec-conduct-a-business-impact-analysis"
description: "Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis", "rar_sha256": "2a27362881d7ceae49cc9967f540ecbfb513ab7d2bdd6c09d1d04d1f39d116c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 2a27362881d7ceae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_a_business_impact_analysis_agent.py` first:

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
    "version": '2.0.0',
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
