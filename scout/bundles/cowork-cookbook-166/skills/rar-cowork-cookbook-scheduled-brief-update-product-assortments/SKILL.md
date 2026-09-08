---
name: "rar-cowork-cookbook-scheduled-brief-update-product-assortments"
description: "Builds a morning brief on product assortment updates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_product_assortments", "rar_sha256": "e7dab8f191b42b1a4aa78ca5d5832c6eeefab34caed31a80dec54caeb6a8f272", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
