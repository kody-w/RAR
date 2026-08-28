---
name: "rar-cowork-cookbook-ppt-exec-insure-assets"
description: "Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_insure_assets", "rar_sha256": "b7ef16c0d7a1cd3130229174215756d47e6e5823c250858b04143163b0c8f9d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_insure_assets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_insure_assets_agent.py` and in the RCI capsule.

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

Insure assets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_insure_assets_agent.py` and embedded as the fenced Python below (sha256 b7ef16c0d7a1cd31…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_insure_assets_agent.py` first:

```bash
python3 ppt_exec_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_insure_assets_agent.py   # or on stdin
python3 ppt_exec_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_insure_assets',
    "version": '2.0.1',
    "display_name": 'Insure assets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fe5acbb1d88b703',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecInsureAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecInsureAssets'
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
    print(PptExecInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
