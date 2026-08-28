---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-copilot-capabilities"
description: "Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities", "rar_sha256": "21f56d3300bd709118174cb856d2220bac0e4f9631085fc2b9885dbe3c45cccc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` and in the RCI capsule.

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

Configure and manage copilot capabilities Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 21f56d3300bd7091…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage copilot capabilities Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities',
    "version": '2.0.1',
    "display_name": 'Configure and manage copilot capabilities Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-copilot-capabilities',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ec090c026cffb43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-copilot-capabilities', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConfigureAndManageCopilotCapabilities(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageCopilotCapabilities'
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
    print(PptExecConfigureAndManageCopilotCapabilities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
