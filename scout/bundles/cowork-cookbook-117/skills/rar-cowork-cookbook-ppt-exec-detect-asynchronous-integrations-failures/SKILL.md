---
name: "rar-cowork-cookbook-ppt-exec-detect-asynchronous-integrations-failures"
description: "Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures", "rar_sha256": "cadacfb68841041d391022b1a686c80ac4c5b3cf74ef57ded94c085cec098375", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 cadacfb68841041d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_detect_asynchronous_integrations_failures_agent.py` first:

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
    "version": '2.0.1',
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
