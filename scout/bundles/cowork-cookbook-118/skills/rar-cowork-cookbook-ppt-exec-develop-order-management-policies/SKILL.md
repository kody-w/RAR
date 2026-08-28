---
name: "rar-cowork-cookbook-ppt-exec-develop-order-management-policies"
description: "Generates an executive-ready PowerPoint deck on develop order management policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_order_management_policies", "rar_sha256": "3614cdfe1e067cc0c763a7a6d4cae8d8f6a455a38ba2bc9860d5bcce5540e908", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 3614cdfe1e067cc0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_order_management_policies_agent.py` first:

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
    "version": '2.0.0',
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
