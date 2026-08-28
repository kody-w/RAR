---
name: "rar-cowork-cookbook-ppt-exec-create-website-for-campaigns"
description: "Generates an executive-ready PowerPoint deck on create website for campaigns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_website_for_campaigns", "rar_sha256": "f5950c3d39a948da29bda5b2603e70e2c7d8ba1b0222f8ea007ca93833222f5a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 f5950c3d39a948da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_website_for_campaigns_agent.py` first:

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
    "version": '2.0.0',
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
