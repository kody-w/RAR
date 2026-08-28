---
name: "rar-cowork-cookbook-ppt-exec-maintain-asset-leases"
description: "Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_asset_leases", "rar_sha256": "3bc39ed437ea9fef2a29850e945c9b5b988b6c599dea3cf86d38c677da20e768", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 3bc39ed437ea9fef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_asset_leases_agent.py` first:

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
    "version": '2.0.0',
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
