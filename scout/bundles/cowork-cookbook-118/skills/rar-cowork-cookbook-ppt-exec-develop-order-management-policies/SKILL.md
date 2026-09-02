---
name: "rar-cowork-cookbook-ppt-exec-develop-order-management-policies"
description: "Generates an executive-ready PowerPoint deck on develop order management policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_order_management_policies", "rar_sha256": "3614cdfe1e067cc0c763a7a6d4cae8d8f6a455a38ba2bc9860d5bcce5540e908", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_order_management_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-order-management-policies:9874985126f06c84868e6a6141ece6b5e4df19fd1070c804fdd1ff20c446933e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_order_management_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_order_management_policies_agent.py` is
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
