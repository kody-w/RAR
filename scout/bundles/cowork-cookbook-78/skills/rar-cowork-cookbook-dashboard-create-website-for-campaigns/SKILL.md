---
name: "rar-cowork-cookbook-dashboard-create-website-for-campaigns"
description: "Produces a self-contained interactive HTML dashboard for create website for campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_website_for_campaigns", "rar_sha256": "b591066e2f22000631ad7f4c2a5e0fbb27d7c306828ed0ad74cb470f5df3cab4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_create_website_for_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-create-website-for-campaigns:8d1ded3c6e4010184be092bbbd1f81e4e55e9e8d45e0091905d98ace19792e67", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_create_website_for_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_create_website_for_campaigns_agent.py` is
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
