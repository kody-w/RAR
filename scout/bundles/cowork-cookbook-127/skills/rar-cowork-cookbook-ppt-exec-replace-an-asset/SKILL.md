---
name: "rar-cowork-cookbook-ppt-exec-replace-an-asset"
description: "Generates an executive-ready PowerPoint deck on replace an asset status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_replace_an_asset", "rar_sha256": "1a4f06aef5b7600ad5422f7efec5da55544732a00c58010a4494d022c52995d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_replace_an_asset_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-replace-an-asset:21b5d5400ea0a5c928cb0380686d06e203e1c80c8cd28ddf31080e1f49feec84", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_replace_an_asset`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_replace_an_asset_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
