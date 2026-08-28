---
name: "rar-cowork-cookbook-ppt-exec-develop-service-policies"
description: "Generates an executive-ready PowerPoint deck on develop service policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_service_policies", "rar_sha256": "31441faa5e612840437fe587b833d3ca91f7803c85847475b210a812fa0c7f2e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 31441faa5e612840…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_service_policies_agent.py` first:

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
    "version": '2.0.0',
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
