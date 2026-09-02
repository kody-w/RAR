---
name: "rar-cowork-cookbook-teams-update-launch-new-products"
description: "Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_launch_new_products", "rar_sha256": "69078bf55554f7f89365fafccdd25f8dc354eef93d51453d980b60d07fe8ddfa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_launch_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-launch-new-products:7957eb5b1978384db728c67d09319fe0aba89f4ca1ee8eb28a602649e980859c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_launch_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_launch_new_products_agent.py` is
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

Launch new products Teams Channel Update — Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-launch-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 69078bf55554f7f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_launch_new_products_agent.py` first:

```bash
python3 teams_update_launch_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_launch_new_products_agent.py   # or on stdin
python3 teams_update_launch_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch new products Teams Channel Update — Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-launch-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_launch_new_products',
    "version": '2.0.0',
    "display_name": 'Launch new products Teams Channel Update',
    "description": 'Drafts a Teams channel post on launch new products status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-launch-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-launch-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5cc7e6499c0200ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/launch-new-products'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-launch-new-products', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateLaunchNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateLaunchNewProducts'
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
    print(TeamsUpdateLaunchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
