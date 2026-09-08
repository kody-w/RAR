---
name: "rar-cowork-cookbook-ar-aging-collection-email"
description: "Drafts one collection email per customer with invoices overdue more than 30 days, citing invoice numbers, due dates, and amounts, with tone varied by 30/60/90+ aging bucket; drafts are saved, not sent."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ar_aging_collection_email", "rar_sha256": "2c57d835747e014766414626120ba55a1dc18a7c4894d91bf7ad6d565e35c96e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ar_aging_collection_email`. The original RAPP
agent is preserved byte-for-byte in `ar_aging_collection_email_agent.py` and in the RCI capsule.

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

AR Aging Collection Email Draft — Drafts one collection email per customer with invoices overdue more than 30 days, citing invoice numbers, due dates, and amounts, with tone varied by 30/60/90+ aging bucket; drafts are saved, not sent.

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
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ar_aging_collection_email_agent.py` and embedded as the fenced Python below (sha256 2c57d835747e0147…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ar_aging_collection_email_agent.py` first:

```bash
python3 ar_aging_collection_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ar_aging_collection_email_agent.py   # or on stdin
python3 ar_aging_collection_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AR Aging Collection Email Draft — Drafts one collection email per customer with invoices overdue more than 30 days, citing invoice numbers, due dates, and amounts, with tone varied by 30/60/90+ aging bucket; drafts are saved, not sent.

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
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ar_aging_collection_email',
    "version": '3.0.2',
    "display_name": 'AR Aging Collection Email Draft',
    "description": 'Drafts one collection email per customer with invoices overdue more than 30 days, citing invoice numbers, due dates, and amounts, with tone varied by 30/60/90+ aging bucket; drafts are saved, not sent.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ar-aging-collection-email',
        "upstream_url": 'https://coworkcookbook.com/recipes/ar-aging-collection-email',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7f6c065886d1533',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ar-aging-collection-email', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Credit/collections role', 'Output matches: One email draft per overdue customer.'], 'confidence': 1.0, 'deliverable': 'One email draft per overdue customer.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Multiplies the collections team - every overdue customer gets a personalized, tone-appropriate nudge without anyone hand-writing emails.', 'expected_output': 'One email draft per overdue customer.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Credit/collections role'], 'prompt': 'For each customer with invoices overdue >30 days, draft a collection email referencing the specific invoice numbers, due dates, and amounts. Vary tone by aging bucket (30/60/90+). Save drafts to the Cowork output folder; do not send.', 'steps': ['Paste the prompt.', 'Open each draft, review tone, and personalize before sending.'], 'tenant_caveat': 'Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork used 2017-12-31 as the as-of date (since USMF demo activity ends in 2017), pulled all open AR invoices >=30 days overdue, and produced 13 per-customer collection drafts plus a summary file covering 40 overdue invoices totalling $600,069.40 across 13 customers. Tone correctly varied by aging bucket - 12 final-notice (90+) drafts and 1 friendly-reminder (30-day). All drafts saved to output/collection-drafts/; no emails were sent.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Generates per-customer collection emails as drafts, varying tone by aging bucket.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts one collection email per customer with invoices overdue more than 30 days, citing invoice numbers, due dates, and amounts, with tone varied by 30/60/90+ aging bucket; drafts are saved, not sent.', 'example_request': 'Draft collection emails for all customers with invoices overdue more than 30 days, tone by aging bucket.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need collection email drafts for overdue AR customers from Dynamics 365 F&SCM, grouped by aging bucket, for human review before sending.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Open each draft, review tone, and personalize before sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ArAgingCollectionEmail(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ArAgingCollectionEmail'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ArAgingCollectionEmail().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
