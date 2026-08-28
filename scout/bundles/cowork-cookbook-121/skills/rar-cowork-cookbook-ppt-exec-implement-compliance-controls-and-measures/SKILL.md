---
name: "rar-cowork-cookbook-ppt-exec-implement-compliance-controls-and-measures"
description: "Generates an executive-ready PowerPoint deck on implement compliance controls and measures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures", "rar_sha256": "64aa26d8c2f1437762d23ec18c6486ffc471835be71c273077bb69980ca5f85f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_compliance_controls_and_measures_agent.py` and in the RCI capsule.

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

Implement compliance controls and measures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement compliance controls and measures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-compliance-controls-and-measures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_compliance_controls_and_measures_agent.py` and embedded as the fenced Python below (sha256 64aa26d8c2f14377…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_compliance_controls_and_measures_agent.py` first:

```bash
python3 ppt_exec_implement_compliance_controls_and_measures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_compliance_controls_and_measures_agent.py   # or on stdin
python3 ppt_exec_implement_compliance_controls_and_measures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement compliance controls and measures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement compliance controls and measures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-compliance-controls-and-measures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures',
    "version": '2.0.1',
    "display_name": 'Implement compliance controls and measures Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement compliance controls and measures status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-implement-compliance-controls-and-measures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-compliance-controls-and-measures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee3fb28355d375f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/implement-compliance-controls-and-measures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-compliance-controls-and-measures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecImplementComplianceControlsAndMeasures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementComplianceControlsAndMeasures'
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
    print(PptExecImplementComplianceControlsAndMeasures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
