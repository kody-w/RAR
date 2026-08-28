---
name: "rar-cowork-cookbook-ppt-exec-retire-services"
description: "Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_retire_services", "rar_sha256": "f99bbf2215f411a856960e469c58232549df07e16238a85a06c3294d7d9fd669", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_retire_services_agent.py` and embedded as the fenced Python below (sha256 f99bbf2215f411a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_retire_services_agent.py` first:

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
    "version": '2.0.1',
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
