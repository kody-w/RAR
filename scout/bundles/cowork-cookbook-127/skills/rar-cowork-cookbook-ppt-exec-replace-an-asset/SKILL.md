---
name: "rar-cowork-cookbook-ppt-exec-replace-an-asset"
description: "Generates an executive-ready PowerPoint deck on replace an asset status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_replace_an_asset", "rar_sha256": "986e88a55b66314061e08e87ba15e7d4ce0a4bbb72a39f9c47006fbca54b308d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_replace_an_asset`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_replace_an_asset_agent.py` and in the RCI capsule.

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

Replace an asset Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on replace an asset status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-replace-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 986e88a55b663140…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_replace_an_asset_agent.py` first:

```bash
python3 ppt_exec_replace_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_replace_an_asset_agent.py   # or on stdin
python3 ppt_exec_replace_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Replace an asset Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on replace an asset status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-replace-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_replace_an_asset',
    "version": '2.0.1',
    "display_name": 'Replace an asset Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on replace an asset status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-replace-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-replace-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd59b498b701f0497',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/replace-an-asset'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-replace-an-asset', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecReplaceAnAsset(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReplaceAnAsset'
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
    print(PptExecReplaceAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
