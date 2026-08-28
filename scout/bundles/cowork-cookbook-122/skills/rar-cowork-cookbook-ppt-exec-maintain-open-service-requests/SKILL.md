---
name: "rar-cowork-cookbook-ppt-exec-maintain-open-service-requests"
description: "Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_open_service_requests", "rar_sha256": "50d7aeba160d71b0dbd1227c8467777c07a031fb0edc57eeb0688ff29b12a1b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_maintain_open_service_requests`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_maintain_open_service_requests_agent.py` and in the RCI capsule.

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

Maintain open service requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 50d7aeba160d71b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_open_service_requests_agent.py` first:

```bash
python3 ppt_exec_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_open_service_requests_agent.py   # or on stdin
python3 ppt_exec_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_open_service_requests',
    "version": '2.0.0',
    "display_name": 'Maintain open service requests Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e999649c50d10a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecMaintainOpenServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainOpenServiceRequests'
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
    print(PptExecMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
