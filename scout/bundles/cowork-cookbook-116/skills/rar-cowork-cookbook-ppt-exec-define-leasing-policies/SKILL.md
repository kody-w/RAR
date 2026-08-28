---
name: "rar-cowork-cookbook-ppt-exec-define-leasing-policies"
description: "Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_leasing_policies", "rar_sha256": "bbb45bb3cec74a892d7b2cb9729fdd7c722463a3d1149206ee7d07b4f3236109", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 bbb45bb3cec74a89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_leasing_policies_agent.py` first:

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
    "version": '2.0.1',
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
