---
name: "rar-cowork-cookbook-demo-data-define-human-resources-policies"
description: "Generates and creates realistic demo records for define human resources policies in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_human_resources_policies", "rar_sha256": "0abf31252536c3e40703fd7a29222983bcd83a5fc6739abf010e5c7a86517994", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
