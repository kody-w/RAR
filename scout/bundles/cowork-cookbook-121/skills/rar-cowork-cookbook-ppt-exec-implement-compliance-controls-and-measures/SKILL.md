---
name: "rar-cowork-cookbook-ppt-exec-implement-compliance-controls-and-measures"
description: "Generates an executive-ready PowerPoint deck on implement compliance controls and measures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures", "rar_sha256": "7cbac06ea5a10a64ab986abba5605e569d93b0c9ea1ea691c5b2b7b8014520b1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_implement_compliance_controls_and_measures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-implement-compliance-controls-and-measures:18cdead22efc1b6543f6ff2ee91a7fd3824b167dc4272d84bd23532804e3129f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_implement_compliance_controls_and_measures_agent.py` is
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
