---
name: "rar-cowork-cookbook-ppt-exec-replace-an-asset"
description: "Generates an executive-ready PowerPoint deck on replace an asset status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_replace_an_asset", "rar_sha256": "1a4f06aef5b7600ad5422f7efec5da55544732a00c58010a4494d022c52995d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 1a4f06aef5b7600a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_replace_an_asset_agent.py` first:

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
    "version": '2.0.0',
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
