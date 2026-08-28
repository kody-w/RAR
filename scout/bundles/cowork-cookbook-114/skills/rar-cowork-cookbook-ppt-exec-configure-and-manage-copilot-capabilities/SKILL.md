---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-copilot-capabilities"
description: "Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities", "rar_sha256": "7f9e28ca3e69a3b2e8b094bcd794994fe87a27eac81a642d830e554d5f36c1b1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 7f9e28ca3e69a3b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` first:

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
    "version": '2.0.0',
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
