---
name: "rar-cowork-cookbook-scheduled-brief-update-product-assortments"
description: "Builds a morning brief on product assortment updates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_product_assortments", "rar_sha256": "e7dab8f191b42b1a4aa78ca5d5832c6eeefab34caed31a80dec54caeb6a8f272", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_update_product_assortments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_update_product_assortments_agent.py` and in the RCI capsule.

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

Update product assortments Scheduled Email Brief — Builds a morning brief on product assortment updates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the own

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 e7dab8f191b42b1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_product_assortments_agent.py` first:

```bash
python3 scheduled_brief_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_product_assortments_agent.py   # or on stdin
python3 scheduled_brief_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Scheduled Email Brief — Builds a morning brief on product assortment updates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the own

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_product_assortments',
    "version": '3.0.3',
    "display_name": 'Update product assortments Scheduled Email Brief',
    "description": 'Builds a morning brief on product assortment updates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the own',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b46721d5d21ba04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where update product assortments stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on update product assortments for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update product assortments, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on product assortment updates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the own', 'example_request': 'Send me the morning brief on update product assortments in USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly (weekday 7am) brief on update product assortments for the responsible owner, with an email draft and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefUpdateProductAssortments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateProductAssortments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ScheduledBriefUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
