---
name: "rar-cowork-cookbook-ppt-exec-run-campaigns"
description: "Generates an executive-ready PowerPoint deck on run campaigns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_run_campaigns", "rar_sha256": "6c1fea1123659aa5ed5b0379053b1886a29511f758f7c8cbba71a5a7d9dff5f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_run_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-run-campaigns:ad17c3cb6065ac3a92039d98053884bac3aef98819811e9f776a8cb4369d0a03", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_run_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_run_campaigns_agent.py` is
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

Run campaigns Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on run campaigns status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-run-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 6c1fea1123659aa5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_run_campaigns_agent.py` first:

```bash
python3 ppt_exec_run_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_run_campaigns_agent.py   # or on stdin
python3 ppt_exec_run_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run campaigns Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on run campaigns status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-run-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_run_campaigns',
    "version": '2.0.0',
    "display_name": 'Run campaigns Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on run campaigns status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-run-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-run-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb996be25ecc819b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-campaigns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-run-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecRunCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRunCampaigns'
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
    print(PptExecRunCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
