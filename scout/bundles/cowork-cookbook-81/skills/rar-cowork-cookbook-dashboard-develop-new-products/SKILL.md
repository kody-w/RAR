---
name: "rar-cowork-cookbook-dashboard-develop-new-products"
description: "Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_new_products", "rar_sha256": "d9df357452aa25d635f94ab5e736393939ea102eeaea0972095941683cab5646", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-new-products:009b6ecbd38094f2a2399961959f0d655591fc34baedda138fae611a9164e130", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_new_products_agent.py` is
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

Develop new products Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 d9df357452aa25d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_new_products_agent.py` first:

```bash
python3 dashboard_develop_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_new_products_agent.py   # or on stdin
python3 dashboard_develop_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new products Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_new_products',
    "version": '2.0.0',
    "display_name": 'Develop new products Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9be9227ee6aa189',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/develop-new-products'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-develop-new-products', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopNewProducts'
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
    print(DashboardDevelopNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
