---
name: "rar-cowork-cookbook-ppt-exec-identify-critical-system-and-data"
description: "Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_critical_system_and_data", "rar_sha256": "9fe41cbab8f7f76dce7f2a8203680190117a74eb1e42573427b107d9729cf794", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_critical_system_and_data`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_critical_system_and_data_agent.py` and in the RCI capsule.

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

Identify critical system and data Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 9fe41cbab8f7f76d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_critical_system_and_data_agent.py` first:

```bash
python3 ppt_exec_identify_critical_system_and_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_critical_system_and_data_agent.py   # or on stdin
python3 ppt_exec_identify_critical_system_and_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify critical system and data Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_critical_system_and_data',
    "version": '2.0.1',
    "display_name": 'Identify critical system and data Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-identify-critical-system-and-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17b8dbf20164d188',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-critical-system-and-data'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-identify-critical-system-and-data', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIdentifyCriticalSystemAndData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCriticalSystemAndData'
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
    print(PptExecIdentifyCriticalSystemAndData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
