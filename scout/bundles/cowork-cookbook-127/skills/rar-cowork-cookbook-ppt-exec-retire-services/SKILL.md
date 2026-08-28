---
name: "rar-cowork-cookbook-ppt-exec-retire-services"
description: "Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_retire_services", "rar_sha256": "255c4ff7aa4462dc9525477b2fecc06d96d5998449b209e1fe46f844d4d9011b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_retire_services`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_retire_services_agent.py` and in the RCI capsule.

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

Retire services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-retire-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_retire_services_agent.py` and embedded as the fenced Python below (sha256 255c4ff7aa4462dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_retire_services_agent.py` first:

```bash
python3 ppt_exec_retire_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_retire_services_agent.py   # or on stdin
python3 ppt_exec_retire_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-retire-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_retire_services',
    "version": '2.0.0',
    "display_name": 'Retire services Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-retire-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-retire-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7f781ce74f21f2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/retire-services'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-retire-services', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecRetireServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRetireServices'
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
    print(PptExecRetireServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
