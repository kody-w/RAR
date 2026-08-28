---
name: "rar-cowork-cookbook-ppt-exec-implement-compliance-controls-and-measures"
description: "Generates an executive-ready PowerPoint deck on implement compliance controls and measures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures", "rar_sha256": "7cbac06ea5a10a64ab986abba5605e569d93b0c9ea1ea691c5b2b7b8014520b1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_compliance_controls_and_measures_agent.py` and embedded as the fenced Python below (sha256 7cbac06ea5a10a64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_compliance_controls_and_measures_agent.py` first:

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
    "version": '2.0.0',
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
