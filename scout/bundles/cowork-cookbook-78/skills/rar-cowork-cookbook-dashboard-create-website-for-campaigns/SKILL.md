---
name: "rar-cowork-cookbook-dashboard-create-website-for-campaigns"
description: "Produces a self-contained interactive HTML dashboard for create website for campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_website_for_campaigns", "rar_sha256": "b8274a05a085c7aa52f675b7c134c7df6be8f9864f3438d760c1d7f464358381", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_website_for_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_website_for_campaigns_agent.py` and in the RCI capsule.

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

Create website for campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create website for campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-website-for-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 b8274a05a085c7aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_website_for_campaigns_agent.py` first:

```bash
python3 dashboard_create_website_for_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_website_for_campaigns_agent.py   # or on stdin
python3 dashboard_create_website_for_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create website for campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create website for campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-website-for-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_website_for_campaigns',
    "version": '2.0.1',
    "display_name": 'Create website for campaigns Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create website for campaigns - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-website-for-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-website-for-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9c2b85a11d112442',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-website-for-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-create-website-for-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardCreateWebsiteForCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateWebsiteForCampaigns'
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
    print(DashboardCreateWebsiteForCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
