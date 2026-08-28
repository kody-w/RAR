---
name: "rar-cowork-cookbook-ppt-exec-consume-resources"
description: "Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_consume_resources", "rar_sha256": "13996cb339a3c9ba81d66fe33ca0f2b7240a8a086f3959c0e6aea52094233bc8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_consume_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_consume_resources_agent.py` and in the RCI capsule.

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

Consume resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-consume-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_consume_resources_agent.py` and embedded as the fenced Python below (sha256 13996cb339a3c9ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_consume_resources_agent.py` first:

```bash
python3 ppt_exec_consume_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_consume_resources_agent.py   # or on stdin
python3 ppt_exec_consume_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-consume-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_consume_resources',
    "version": '2.0.1',
    "display_name": 'Consume resources Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-consume-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-consume-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea103b789df6d959',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-consume-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConsumeResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConsumeResources'
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
    print(PptExecConsumeResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
