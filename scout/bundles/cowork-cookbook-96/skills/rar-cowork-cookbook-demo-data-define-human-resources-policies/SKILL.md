---
name: "rar-cowork-cookbook-demo-data-define-human-resources-policies"
description: "Generates and creates realistic demo records for define human resources policies in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_human_resources_policies", "rar_sha256": "0abf31252536c3e40703fd7a29222983bcd83a5fc6739abf010e5c7a86517994", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_human_resources_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-human-resources-policies:fb8fdfa9c33d11564a4b15568dbc2ca56c5570309e42d9d6abcf1b347175373b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_human_resources_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_human_resources_policies_agent.py` is
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

Define human resources policies Demo Data Generator — Generates and creates realistic demo records for define human resources policies in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-human-resources-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_human_resources_policies_agent.py` and embedded as the fenced Python below (sha256 0abf31252536c3e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_human_resources_policies_agent.py` first:

```bash
python3 demo_data_define_human_resources_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_human_resources_policies_agent.py   # or on stdin
python3 demo_data_define_human_resources_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define human resources policies Demo Data Generator — Generates and creates realistic demo records for define human resources policies in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-human-resources-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_human_resources_policies',
    "version": '2.0.0',
    "display_name": 'Define human resources policies Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define human resources policies in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-human-resources-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-human-resources-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee4fbe431ea27beb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-human-resources-policies'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-define-human-resources-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineHumanResourcesPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineHumanResourcesPolicies'
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
    print(DemoDataDefineHumanResourcesPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
