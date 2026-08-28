---
name: "rar-cowork-cookbook-ppt-exec-identify-campaign-audiences"
description: "Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_campaign_audiences", "rar_sha256": "a7d3f0052e03c69ccd1e64e0321f6a3edc100f6e831054d68bbb1bf905f96412", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_campaign_audiences`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_campaign_audiences_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 a7d3f0052e03c69c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_campaign_audiences_agent.py` first:

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
    "version": '2.0.1',
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
