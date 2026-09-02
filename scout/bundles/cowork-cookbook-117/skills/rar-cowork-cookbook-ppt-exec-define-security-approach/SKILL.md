---
name: "rar-cowork-cookbook-ppt-exec-define-security-approach"
description: "Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_security_approach", "rar_sha256": "9d0cf5aedd684816d266cec8eebc412ca814b3ea3226a3535d327e7153a12bc3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_security_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-security-approach:c04f43fa999fe8cbe0a502b944173721cbeb0ea033c3519187ffec52f3041ef0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_security_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_security_approach_agent.py` is
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

Define security approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 9d0cf5aedd684816…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_security_approach_agent.py` first:

```bash
python3 ppt_exec_define_security_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_security_approach_agent.py   # or on stdin
python3 ppt_exec_define_security_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define security approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_security_approach',
    "version": '2.0.0',
    "display_name": 'Define security approach Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-security-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-security-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc49bdd666c5b170',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-security-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-security-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineSecurityApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineSecurityApproach'
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
    print(PptExecDefineSecurityApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
