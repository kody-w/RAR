---
name: "rar-cowork-cookbook-ppt-exec-develop-service-policies"
description: "Generates an executive-ready PowerPoint deck on develop service policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_service_policies", "rar_sha256": "1abdad8688398668274f3aa09975606be0bd0e79b29ab21e4f055ecf00570077", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_service_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_service_policies_agent.py` and in the RCI capsule.

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

Develop service policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop service policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-service-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 1abdad8688398668…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_service_policies_agent.py` first:

```bash
python3 ppt_exec_develop_service_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_service_policies_agent.py   # or on stdin
python3 ppt_exec_develop_service_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop service policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-service-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_service_policies',
    "version": '2.0.1',
    "display_name": 'Develop service policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop service policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-service-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-service-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5761c006b54d2704',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-develop-service-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopServicePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopServicePolicies'
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
    print(PptExecDevelopServicePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
