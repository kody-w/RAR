---
name: "rar-cowork-cookbook-ppt-exec-establish-support-procedures-and-policies"
description: "Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies", "rar_sha256": "1f4c511827a033fec13155ed0fe33a92310bb8d653b5713b8257ac8aef452c20", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_establish_support_procedures_and_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-establish-support-procedures-and-policies:b6756a66e21b2fc0d1637e9032dc0780f762ba95ed6c370748af9acc3d5628f3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_establish_support_procedures_and_policies_agent.py` is
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

Establish support procedures and policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 1f4c511827a033fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_establish_support_procedures_and_policies_agent.py` first:

```bash
python3 ppt_exec_establish_support_procedures_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_establish_support_procedures_and_policies_agent.py   # or on stdin
python3 ppt_exec_establish_support_procedures_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support procedures and policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies',
    "version": '2.0.0',
    "display_name": 'Establish support procedures and policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-establish-support-procedures-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '963e5b46cb82d409',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-procedures-and-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-establish-support-procedures-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecEstablishSupportProceduresAndPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEstablishSupportProceduresAndPolicies'
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
    print(PptExecEstablishSupportProceduresAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
