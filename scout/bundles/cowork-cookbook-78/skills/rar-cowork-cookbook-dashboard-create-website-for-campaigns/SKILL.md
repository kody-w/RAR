---
name: "rar-cowork-cookbook-dashboard-create-website-for-campaigns"
description: "Produces a self-contained interactive HTML dashboard for create website for campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_website_for_campaigns", "rar_sha256": "b591066e2f22000631ad7f4c2a5e0fbb27d7c306828ed0ad74cb470f5df3cab4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 b591066e2f220006…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_website_for_campaigns_agent.py` first:

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
    "version": '2.0.0',
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
