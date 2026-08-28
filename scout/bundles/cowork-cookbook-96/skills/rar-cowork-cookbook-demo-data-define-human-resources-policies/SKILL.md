---
name: "rar-cowork-cookbook-demo-data-define-human-resources-policies"
description: "Generates and creates realistic demo records for define human resources policies in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_human_resources_policies", "rar_sha256": "bbdff47a002275cd1c41295b8c57c150a857b48db82282e9bae51f4ff431ab60", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_human_resources_policies`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_human_resources_policies_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_human_resources_policies_agent.py` and embedded as the fenced Python below (sha256 bbdff47a002275cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_human_resources_policies_agent.py` first:

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
    "version": '2.0.1',
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
