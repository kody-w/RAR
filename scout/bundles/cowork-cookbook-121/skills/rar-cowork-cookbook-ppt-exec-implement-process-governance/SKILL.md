---
name: "rar-cowork-cookbook-ppt-exec-implement-process-governance"
description: "Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_process_governance", "rar_sha256": "60689b742b18ac9ef9c2b17e9c7145610bd6b4690856ba8a65feeaaed0da5057", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_process_governance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_process_governance_agent.py` and in the RCI capsule.

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

Implement process governance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 60689b742b18ac9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_process_governance_agent.py` first:

```bash
python3 ppt_exec_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_process_governance_agent.py   # or on stdin
python3 ppt_exec_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_process_governance',
    "version": '2.0.1',
    "display_name": 'Implement process governance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac7a4fd00bf5dceb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecImplementProcessGovernance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementProcessGovernance'
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
    print(PptExecImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
