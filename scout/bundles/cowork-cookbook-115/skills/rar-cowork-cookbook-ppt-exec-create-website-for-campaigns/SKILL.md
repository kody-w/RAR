---
name: "rar-cowork-cookbook-ppt-exec-create-website-for-campaigns"
description: "Generates an executive-ready PowerPoint deck on create website for campaigns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_website_for_campaigns", "rar_sha256": "f5950c3d39a948da29bda5b2603e70e2c7d8ba1b0222f8ea007ca93833222f5a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_create_website_for_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-create-website-for-campaigns:0a4f49401f5f50834ca320d96298f4953df724990f4a179701d5a16293ab5f2e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_create_website_for_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_create_website_for_campaigns_agent.py` is
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
