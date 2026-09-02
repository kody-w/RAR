---
name: "rar-cowork-cookbook-ppt-exec-conduct-a-business-impact-analysis"
description: "Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis", "rar_sha256": "2a27362881d7ceae49cc9967f540ecbfb513ab7d2bdd6c09d1d04d1f39d116c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_conduct_a_business_impact_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-conduct-a-business-impact-analysis:31b8e3c5f6523ac22c88b80f824eef3d251704c01cde7b126607fdcb868f9514", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_conduct_a_business_impact_analysis_agent.py` is
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

Conduct a business impact analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 2a27362881d7ceae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_a_business_impact_analysis_agent.py` first:

```bash
python3 ppt_exec_conduct_a_business_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_conduct_a_business_impact_analysis_agent.py   # or on stdin
python3 ppt_exec_conduct_a_business_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a business impact analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis',
    "version": '2.0.0',
    "display_name": 'Conduct a business impact analysis Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on conduct a business impact analysis status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-conduct-a-business-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2846f7c6a9881f3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-business-impact-analysis'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-conduct-a-business-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConductABusinessImpactAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConductABusinessImpactAnalysis'
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
    print(PptExecConductABusinessImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
