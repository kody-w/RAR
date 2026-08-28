---
name: "rar-cowork-cookbook-ppt-exec-detect-asynchronous-integrations-failures"
description: "Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures", "rar_sha256": "d99c9467be722f349745b33a0fbeefbe9bc530ad51418136b888dd8b67c19fed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_detect_asynchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect asynchronous integrations failures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 d99c9467be722f34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_detect_asynchronous_integrations_failures_agent.py` first:

```bash
python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py   # or on stdin
python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect asynchronous integrations failures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures',
    "version": '2.0.0',
    "display_name": 'Detect asynchronous integrations failures Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-detect-asynchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31f20f9e482e60f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-asynchronous-integrations-failures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-detect-asynchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDetectAsynchronousIntegrationsFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetectAsynchronousIntegrationsFailures'
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
    print(PptExecDetectAsynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
