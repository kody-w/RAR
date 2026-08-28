---
name: "rar-cowork-cookbook-ppt-exec-run-campaigns"
description: "Generates an executive-ready PowerPoint deck on run campaigns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_run_campaigns", "rar_sha256": "1dd7e8c118d22d0194fe85eb414c71daab9c66fc26c33f2eeba9b15213a043b0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 1dd7e8c118d22d01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_run_campaigns_agent.py` first:

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
    "version": '2.0.1',
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
