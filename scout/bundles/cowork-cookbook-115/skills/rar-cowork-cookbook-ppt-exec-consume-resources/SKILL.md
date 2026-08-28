---
name: "rar-cowork-cookbook-ppt-exec-consume-resources"
description: "Generates an executive-ready PowerPoint deck on consume resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_consume_resources", "rar_sha256": "df06a75c24277eb660e7f9b4f8280ba22f8a4f69891f723240da0e736ab5f563", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_consume_resources_agent.py` and embedded as the fenced Python below (sha256 df06a75c24277eb6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_consume_resources_agent.py` first:

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
    "version": '2.0.0',
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
