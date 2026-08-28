---
name: "rar-cowork-cookbook-ppt-exec-troubleshoot-reported-incidents"
description: "Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents", "rar_sha256": "f789aad0f908fef72c46edf02816c20e0e9e1786eaf2f32a5ffad4e47b8f4d80", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_troubleshoot_reported_incidents_agent.py` and in the RCI capsule.

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

Troubleshoot reported incidents Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 f789aad0f908fef7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_troubleshoot_reported_incidents_agent.py` first:

```bash
python3 ppt_exec_troubleshoot_reported_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_troubleshoot_reported_incidents_agent.py   # or on stdin
python3 ppt_exec_troubleshoot_reported_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Troubleshoot reported incidents Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents',
    "version": '2.0.0',
    "display_name": 'Troubleshoot reported incidents Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-troubleshoot-reported-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7f399b942d2d323a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/troubleshoot-reported-incidents'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-troubleshoot-reported-incidents', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecTroubleshootReportedIncidents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTroubleshootReportedIncidents'
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
    print(PptExecTroubleshootReportedIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
