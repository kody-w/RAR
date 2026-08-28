---
name: "rar-cowork-cookbook-ppt-exec-create-website-for-campaigns"
description: "Generates an executive-ready PowerPoint deck on create website for campaigns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_website_for_campaigns", "rar_sha256": "b463cf59cd46e10c397a45df26d40ba2ce345910adc4e68ea32a04cb9d3a2c20", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_website_for_campaigns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_website_for_campaigns_agent.py` and in the RCI capsule.

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

Create website for campaigns Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create website for campaigns status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 b463cf59cd46e10c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_website_for_campaigns_agent.py` first:

```bash
python3 ppt_exec_create_website_for_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_website_for_campaigns_agent.py   # or on stdin
python3 ppt_exec_create_website_for_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create website for campaigns Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create website for campaigns status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_website_for_campaigns',
    "version": '2.0.1',
    "display_name": 'Create website for campaigns Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on create website for campaigns status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-create-website-for-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '43531d746918038b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-website-for-campaigns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-create-website-for-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecCreateWebsiteForCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateWebsiteForCampaigns'
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
    print(PptExecCreateWebsiteForCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
