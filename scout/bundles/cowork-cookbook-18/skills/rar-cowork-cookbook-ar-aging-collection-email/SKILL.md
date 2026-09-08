---
name: "rar-cowork-cookbook-ar-aging-collection-email"
description: "Drafts one collection email per customer with invoices overdue more than 30 days, citing invoice numbers, due dates, and amounts, with tone varied by 30/60/90+ aging bucket; drafts are saved, not sent."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ar_aging_collection_email", "rar_sha256": "2c57d835747e014766414626120ba55a1dc18a7c4894d91bf7ad6d565e35c96e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
