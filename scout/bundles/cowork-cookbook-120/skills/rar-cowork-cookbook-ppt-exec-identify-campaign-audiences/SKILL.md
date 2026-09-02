---
name: "rar-cowork-cookbook-ppt-exec-identify-campaign-audiences"
description: "Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_campaign_audiences", "rar_sha256": "b9c20533fc77b8b534ee348c09e954a353b29d8c54e0fc5e1f5f6464f3359295", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_identify_campaign_audiences_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-identify-campaign-audiences:11906c98466dd824f4d1f69f78a52122e1f154401dd8e0217bc067392114de58", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_identify_campaign_audiences`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_identify_campaign_audiences_agent.py` is
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

Identify campaign audiences Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 b9c20533fc77b8b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_campaign_audiences_agent.py` first:

```bash
python3 ppt_exec_identify_campaign_audiences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_campaign_audiences_agent.py   # or on stdin
python3 ppt_exec_identify_campaign_audiences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify campaign audiences Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_campaign_audiences',
    "version": '2.0.0',
    "display_name": 'Identify campaign audiences Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-identify-campaign-audiences',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0044bf674b8dd176',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-campaign-audiences', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIdentifyCampaignAudiences(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCampaignAudiences'
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
    print(PptExecIdentifyCampaignAudiences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
