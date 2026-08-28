---
name: "rar-cowork-cookbook-ppt-exec-define-leasing-policies"
description: "Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_leasing_policies", "rar_sha256": "da9703edf5623dd4a9054fb4fc79041072329aae6a6285f0aaafa77e7ea1c2ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_leasing_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_leasing_policies_agent.py` and in the RCI capsule.

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

Define leasing policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 da9703edf5623dd4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_leasing_policies_agent.py` first:

```bash
python3 ppt_exec_define_leasing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_leasing_policies_agent.py   # or on stdin
python3 ppt_exec_define_leasing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define leasing policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_leasing_policies',
    "version": '2.0.0',
    "display_name": 'Define leasing policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-define-leasing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd8b7dd3d584d5d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-leasing-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-define-leasing-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecDefineLeasingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineLeasingPolicies'
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
    print(PptExecDefineLeasingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
