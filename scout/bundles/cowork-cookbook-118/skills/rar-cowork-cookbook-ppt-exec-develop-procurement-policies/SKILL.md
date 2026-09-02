---
name: "rar-cowork-cookbook-ppt-exec-develop-procurement-policies"
description: "Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_procurement_policies", "rar_sha256": "2d46fe53edfe9c15518c14ea7878ecb87f3620d6e7f4d7368e4f924aae201d4f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_procurement_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-procurement-policies:73682b89bc48fcd4edde0348447bbf5a3612a10b77e2f8ffdf2724ea9ed81bda", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_procurement_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_procurement_policies_agent.py` is
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

Develop procurement policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 2d46fe53edfe9c15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_procurement_policies_agent.py` first:

```bash
python3 ppt_exec_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_procurement_policies_agent.py   # or on stdin
python3 ppt_exec_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_procurement_policies',
    "version": '2.0.0',
    "display_name": 'Develop procurement policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0d7e6475aaf4c76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopProcurementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopProcurementPolicies'
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
    print(PptExecDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
