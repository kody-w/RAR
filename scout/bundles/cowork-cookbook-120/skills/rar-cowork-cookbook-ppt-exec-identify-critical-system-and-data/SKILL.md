---
name: "rar-cowork-cookbook-ppt-exec-identify-critical-system-and-data"
description: "Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_critical_system_and_data", "rar_sha256": "2ddd2f432920e4af66d41b5b3862ef909d45079f254746570a6a9a01f04bdfa3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 2ddd2f432920e4af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_critical_system_and_data_agent.py` first:

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
    "version": '2.0.0',
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
