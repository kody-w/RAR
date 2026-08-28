---
name: "rar-cowork-cookbook-ppt-exec-develop-order-management-policies"
description: "Generates an executive-ready PowerPoint deck on develop order management policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_order_management_policies", "rar_sha256": "8d4daca1bf4e1c1d07ca0adef266b0671eed23b4f17b89c261042e4182265483", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_order_management_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_order_management_policies_agent.py` and in the RCI capsule.

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

Develop order management policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop order management policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-order-management-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 8d4daca1bf4e1c1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_order_management_policies_agent.py` first:

```bash
python3 ppt_exec_develop_order_management_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_order_management_policies_agent.py   # or on stdin
python3 ppt_exec_develop_order_management_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop order management policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop order management policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-order-management-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_order_management_policies',
    "version": '2.0.1',
    "display_name": 'Develop order management policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop order management policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-order-management-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-order-management-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '903c3adc958b98fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-order-management-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-develop-order-management-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopOrderManagementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopOrderManagementPolicies'
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
    print(PptExecDevelopOrderManagementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
