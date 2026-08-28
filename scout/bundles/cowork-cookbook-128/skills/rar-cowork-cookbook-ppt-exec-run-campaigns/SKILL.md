---
name: "rar-cowork-cookbook-ppt-exec-run-campaigns"
description: "Generates an executive-ready PowerPoint deck on run campaigns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_run_campaigns", "rar_sha256": "6c1fea1123659aa5ed5b0379053b1886a29511f758f7c8cbba71a5a7d9dff5f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_run_campaigns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_run_campaigns_agent.py` and in the RCI capsule.

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
