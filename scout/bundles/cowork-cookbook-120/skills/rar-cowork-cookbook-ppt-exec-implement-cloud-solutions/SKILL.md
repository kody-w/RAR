---
name: "rar-cowork-cookbook-ppt-exec-implement-cloud-solutions"
description: "Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_cloud_solutions", "rar_sha256": "4e5ec5fe565f3f04bf769f8d99f5da19d320fb13f888573527982b4c00eca15e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_implement_cloud_solutions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-implement-cloud-solutions:a723190dc2a64170919112573fc4aca5e13e2a2f027bff587165683295280ff6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_implement_cloud_solutions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_implement_cloud_solutions_agent.py` is
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

Implement cloud solutions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 4e5ec5fe565f3f04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_cloud_solutions_agent.py` first:

```bash
python3 ppt_exec_implement_cloud_solutions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_cloud_solutions_agent.py   # or on stdin
python3 ppt_exec_implement_cloud_solutions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement cloud solutions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_cloud_solutions',
    "version": '2.0.0',
    "display_name": 'Implement cloud solutions Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-implement-cloud-solutions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8aab46af56fbd3b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-cloud-solutions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-cloud-solutions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecImplementCloudSolutions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementCloudSolutions'
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
    print(PptExecImplementCloudSolutions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
