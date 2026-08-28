---
name: "rar-cowork-cookbook-ppt-exec-insure-assets"
description: "Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_insure_assets", "rar_sha256": "92ac541bd331a15feee568f10b36ab98adb49aadee309b23d3a5ba05a3e83e28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_insure_assets_agent.py` and embedded as the fenced Python below (sha256 92ac541bd331a15f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_insure_assets_agent.py` first:

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
    "version": '2.0.0',
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
