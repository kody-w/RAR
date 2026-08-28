---
name: "rar-cowork-cookbook-ppt-exec-maintain-asset-leases"
description: "Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_asset_leases", "rar_sha256": "8ce9edbf72671748afdd6db6bec70830be6dbd8adc1ab0c1a84e020cdcb9bbc7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_maintain_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_maintain_asset_leases_agent.py` and in the RCI capsule.

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

Maintain asset leases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 8ce9edbf72671748…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_asset_leases_agent.py` first:

```bash
python3 ppt_exec_maintain_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_asset_leases_agent.py   # or on stdin
python3 ppt_exec_maintain_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain asset leases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_asset_leases',
    "version": '2.0.1',
    "display_name": 'Maintain asset leases Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-maintain-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e8ca7ee79924785',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-asset-leases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-maintain-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecMaintainAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainAssetLeases'
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
    print(PptExecMaintainAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
