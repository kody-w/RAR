---
name: "rar-cowork-cookbook-ppt-exec-develop-service-policies"
description: "Generates an executive-ready PowerPoint deck on develop service policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_service_policies", "rar_sha256": "31441faa5e612840437fe587b833d3ca91f7803c85847475b210a812fa0c7f2e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_service_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-service-policies:2eefd19d1a6ccda185a00cf56ad9eba92b8407a62785a2f8964141121d0f9b73", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_service_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_service_policies_agent.py` is
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
