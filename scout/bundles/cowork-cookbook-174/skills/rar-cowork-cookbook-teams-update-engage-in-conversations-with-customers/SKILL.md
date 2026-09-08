---
name: "rar-cowork-cookbook-teams-update-engage-in-conversations-with-customers"
description: "Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_engage_in_conversations_with_customers", "rar_sha256": "b7afa20c3753e18105b5b294ff8934aa3f5f09ceb7e5c18bfb5fc60b2f5d7ecd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_engage_in_conversations_with_customers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_engage_in_conversations_with_customers_agent.py` and in the RCI capsule.

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

Engage in conversations with customers Teams Channel Update — Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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
    "topic": {
      "description": "The status area to summarize, e.g. engage in conversations with customers.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 b7afa20c3753e181…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_engage_in_conversations_with_customers_agent.py` first:

```bash
python3 teams_update_engage_in_conversations_with_customers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_engage_in_conversations_with_customers_agent.py   # or on stdin
python3 teams_update_engage_in_conversations_with_customers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engage in conversations with customers Teams Channel Update — Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_engage_in_conversations_with_customers',
    "version": '3.0.3',
    "display_name": 'Engage in conversations with customers Teams Channel Update',
    "description": 'Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-engage-in-conversations-with-customers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1565a06c5c8459b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/engage-in-conversations-with-customers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-engage-in-conversations-with-customers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The status area to summarize, e.g. engage in conversations with customers.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of engage in conversations with customers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-engage-in-conversations-with-customers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads engage in conversations with customers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.', 'example_request': "Draft a Teams update on customer conversation engagement for USMF with an Adaptive Card - don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The status area to summarize, e.g. engage in conversations with customers.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update plus Adaptive Card on engage-in-conversations-with-customers status from D365 F&SCM; it does not post anything.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEngageInConversationsWithCustomers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEngageInConversationsWithCustomers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The status area to summarize, e.g. engage in conversations with customers.', 'type': 'string'}},
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
    print(TeamsUpdateEngageInConversationsWithCustomers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9166beiWJbvv+K7/SEz27iXUdDoVWs9ZRJFZBKQjFqRjDKDzJAv//d30BtDVkX166ruT88YVDhnz/u39/bw+4vdNmFRvXx8UX07X3B2mkahXy3s3FtQRV9UCXgrEgf8W7hF3lSR0zZFVb98ePH82q2isomKfN7eZpldRZNfL9y2borMr17Bhs6vantesvDzm33zMz9vFnVjN229CKoiW9BjbmeRWy8wYrVgFGkRFID7IvVvdgr2NFEzPoSp7Q6QbvpiYVdNFNhuU38E6wDPxCv6fKH5dgZYh3ae++miLOrmsQ3otPVsIGTnLyi78hYH9Swu+qgJF0eJrx9r7m3kJq+A4iwmUK8p8voNKOgPdlamfv3y8de/fniJwOeXj7+/uKldg0svD4aX0rMbn3moxufUd/rWBuBBvVtiNldq5zewrRyBvXPwvfQroGoGLnl+sHj/9nPtp8GHxb//e9Lb1a3+5eOnfPH++vQy/1HafNGE/qIp7LrxvYVrl7YTpcBKb4tt2ttjvaj8pq1yoBqwcxXlt7fnzm+UinLxl/nez08mbze/+fnTSwFEeEj+6eWXBfDBp5eqnT+/zVTKn395S4ver37+5RudunVi321mYkDqt8/v39/JgoXflkbB4rMqMdQ7r8p3o9IHxL/Tb349RX8n926Sz8/FPxflh8WPKc/6/AXI+wxIB9D9MVlgA7Dz5S0uovzndx5V0fm5nbv+z7/8I7Ju6LtJGtXNf4nur0/CoW97wFrvJvnlw8N9f10s33X7SvMfsy1BwPwzmoDlX9h9NdQ/ov3w7N+QTqMcJNgXX/6Q3I82LP+y+PUf6vafbfiwCD690H4KMrOyndT/uPj9ESK//uR9u/jTX/8ApP+fZNSirdwHhc+ZnUeBXzefP//6U/24/NNff/2pLUEUg4T93Fbpj2j+yK4PPn+y4Puqn/+8F/C/5Ek+g9DXHFr8XpT/q/rjbaHbaeR9uw4w6/tMnF/LxazEF6ZPE3yXjTWQ9Ts7/vLyB4CiHGjTPvBqRqJ/+7fFKXKroi6CZqG6RdssgIObKPNn4bUwqhfg74walT/jUwQM+74OxP/s4VniIlj89r/dB+QD4H5CPtTMIPe5faDc5yeCf47yz98De/15RtPPX0C//u1toQFWRRXdohxguLKVpE852AiAH4hRVn7tVx2ALmds/FeQ4a/zh0WUL377F7h9fhB+K8ffHlAePdFRofgZGes29d9mGxihn79r7IKK4A++2wKeaeECAYMIYPwHYJu6SEGVaGZ71UmUpgsvAtgDqt2zAgGbfpyJ/fbbb45dh5/yJ5Rji2cZrCGw4Ks4i9dXoGmQRrew+ZT7blgsfvr9j58W/2fxn+16EJ95SKDGvHsMSPioWSAD27l6AmcC9wN4eXjs9z/e7Q3I5KBuA0NFQeQ/N4MITnzvi/HV/fYVXRELxwdGBwbPygJU0vy2iJq3BR8svsoLmM635goSznXU80s/9/zcHQFVG6jz1ZJ5AYo58EsdjB8Wbe0/uP7mVPZDxAxAgd38tjhREqhXRQr+m8V8LAKbizwC5v8aGs/rgEj1U73YfSHxthDnmF2UdmWXYWW/85jr/+yXuVd43w6I24vc7z/lc6V+NBqPiHmaBywClnHfXfo6+xz0M6Blyb36C+/HGnuuqtqjulaf8vo9OexqdoULigVgemsjby4Z//EeUnVYtKn3sB+QdKb07gXv3SuPGHw2CTOvP8Xzsxf5Gs/vfQz13sc8+4vFpxaFEXzx/1uPNZtly3EKw201hl4woqZcn+6aW81Zi2d3Oss3i/xIzW8dzxdU+wLun/I0ArFXjf/xXPlw8vuaJ2C2FfCJslUe9EGEAXfNdB8JMAd0Vc2pY3/Kv1SRD0D9B2QCqQFagGyag/gLw/nuF0lDAAnz928dxSNgqtk8cwouytZJQQAGvu85tpsAqao5id9dC7LBnxO6DyM3/JNWs4NA0AH6CyBEBNISuOLtK7I/734R/U8bn43TvOXRVLYgh6sHASCHPws4O2Z2ExCveXb2QM+PDyJAjaxsZt0dEFpA0+dFv/KBJ+uomRHzaVe/BAD+Or8/NZ2v+kMJEgcYC6RH2QLrPhJqxpoMtEVABoApIL+yKAdtAjDKuxEeBO1sRgeAvu997JPi4/K7Qv4jC+f69mXjrMi8Z24ZniFv5+P3IKL9KEwAvWxe8eD7t5H2ldtMewbSGoAh4Pjl7rO3eHu2B8/+Y/GF7se/G51+/uemq0fBv/w5AD4uwqYp648Q9CzSX2r0G4Ax6Clr/azXr88K+vpEg9co/xNI1K+zy1+/Is6fWD2t8HHxz4n7JxLv6fJxgbzBb/B8S3gPt/cXsA71uru+4vPdT7nif8NdwL7IgJSzL0fQIHwtkl+WgEp5qwBsgcXPolnPtbYH5f1RJYBjPuXfx/+cfzNe3eZ4rYvvcOHRLYBcePrxazEDt/IG8PbmDvTmz2PgI1tq/+Vj3qbphxcApf6/MP7NBSybg76eh0iQXqDBayL/8Q1kr/d5lupJ+/e/Ga3PjyRafFnwNQT/HnQ/LPy329viT1Hw9vb2isIo8QqvXlH8deb1FtegLgKhmrGcdXnOiXNn+UCzofmBDI8Pdvq2oH2AnGn9fYq8F8C5Afguk5/mB2Z3ga4fFrMw9VywgR6zGWYUsGuQVkCdH8ryKE+fn+Xp7wWi51r2pwoGgLn+UiDfDXFRT+wPaX9tr/+esAF6lpmWV3ycy/eHdygE72Ak+rD4Ot0Ajd7nzcdvBXkLRvlf58lqdvZjy/wB7AFvXzd9/dnE8V/++gO5mqKM3L+XSXsg7aOgg07E/pGq/n+pvfiBMQDXB6iD0jgr8M0y3+QrHmPgLB/Qp3n+avH7C4hmGzjVfo/n9zkCLAcY+FrPnREEIAAwBN+fyQru/U9MGO8k69AG7Syg6ZB2YKOwi5ErzEfWCLxyVg66wYNgvcFw28aCVQBvXN8h/ZWLrJ3AWQUuATtosPJI3/UAvScKfJ47wmgWc5YRWOcVAIn/7Ta45L3r99RnNt7XgWa2w7uav784BA5W7vGa3z5fFLRBHAgnnfNBWGIwtIP7Q+5vPNSazlpvIdP5MqmqbK9QVKU87srdkBVdqKa9quTavsjlXl/GNxPlA/ewSbr2rp7uqrD3sKTufPImew2FKoMhbKBjxdPF4bamBm8kL+o51JW0WpmhxaVTysdCbqwYnU3HbBTC5bFJ0jrWYnfU9EsU1GFsqNXQkNBatwYdJeB6I62LC770xSg5DHJT63pxvKzv4yk76BbbDd4hOFZX4rQ8353dUrCyjRelik5FidpYV35VqitMvtvDSeI36sE3M2vH3nV3PNawi5N0pliDVxbEMNKcYRFOYmu8HqNnK4XuG+buj9FJh3ITg8aMvHfIEjrRU4bA5Z5FRPlA26aupxFGSjtcYjGMRFabBoub9dIH7UGHVeTKVx3fCZVDScib8Vi51lYflH40ORxjLZUwz3c2X7JW5B4Mp77t4hssdxSS1/vmvjuu4ELqZfp+j2oqNAQRh4LTPisvyKU3dOw88LUa8g11hbyxPhilGaWaVu0QJkKGnNOUnWGbhgO7XaCvnbtmwZK/HkWi0o+2whTGsS4ODNNDfccW2Tnkq9I/pjFFbpkxZiqRh9WVyevtYSwIUbSnZZJxh32zvVxhSl+a9lVG9c4Gtsl9YyX264LQJ2V3sNvDXTxcWa33BCqMYk/ZjWHO11EPezwjTmXCLUUoOxgIQZkdxbYIratRMS1DNbtmWrm+5+MGvQTdySDsPZEc2yI8UOO97itK0ptDgpbwZNaH0Voqx+GoGwNy7xgcb+Dp5GTskBnqbS8VR9qgl/fciW4H+txzXLVzZWhSfOHOhk22tMha1bZRwcpIU8kpWm2PcEP727TFLL2C1YRZIT4ncDt3o3eaftWTq1CHWhzH64OWXzuNpPlK6LZVi8RRN0TeMYhpb7mTnHGHF83NkzOHvtXr46l3xP2msHO8EQ3fyoKcV9euxk9Ww6KBw5yy8qzmAmu7xnA1Ki+4V5oey/1lI4wNj1eTZdS7sxPhq7C55JR/UjwoF1EHc8+ONOWT261vmSeVyWqZm0spxXnEPkKRc5CkLdwkBn3gjx56XDHj9e6xhM1M6yQ9N8jNo5g+uPGZFVpdcaZx+mIcrpdTVltnJ7mG9gUzbOfIbTYiOkpUs8y2k20V4el80I1MKDmJuxvMGYSDMPHbESCdH/qU2u4q9dAzsoMycM/CTLjGpiN5GG7Des90iefq5o2ERPtutyViBRfN6FBGj5ehVp+NIBFUDYkraxkW5zpRUXt9QwlovUYiRzpwJHyEVpyXJYd7Vq9FZOxIc41XXllZCLZk9yjZ+qabwf0SGwt4CMejaYejcjxn6/OBo/DqhiqRxsc95zOY5JyVlMYR+sotlc2xqE8TJcd6SRwUqsDvCAebAYKbcIWecny3pejUUOjBP9d9HCNINhQkjKwa1YWQ8jCWenhXzG4/solB6Dh+83p763a1uMeak846SraSW4vnl7Lph6u12q/6ulQ4ZXOttlMAe8sDkgdWhpeYEBlcjVt0esZukSRIPIXtsOwY39oesuoll8fNzWjoWBT3B7yW14HBMUSoixw7bhvPOJRC1HrDQc5w+NiNZT6ZpkWegBdRvaT2etVDHKLc3XyZK3BANLfjvTWlfi0O2A0md408geZZ5fKQ1rnNed3xB00/gjqL56FU+mD8mtZKfijNgAWWjAWRcQcuZoxtTijifsqzuEh9UmOXW4aTt6V/Dvf8mqp4W0C4VSdJF4qmLdSPIheixj5SsmtMrWrvwF90Dk7sKxfW/OVq1BC3CSQWtTIuBvl53N5T6yKjYg+PmpD0kc3J8aV3TcSP71c2MztFkQ/FVrMu5XhC2Atd6duST53NyNRSAWuW7m1pNrhCqh2bbHA0fSSqe2ro8ZojwjWKCBBHNIaKGLjMim4LwNpt6imyDmkyDiKlRR7k53uCFE3r1Jf78HKokSKSW3gZjzmrBHWsOgAZC9etr1dnHPhlABm8zBBrBxTG85kbappcrfjzZsNMKA+1WLWDlsvN3kkPNx1hz761h+8ov5XX4+EabclwJYTn+Hgm78gFlN7rAT9r6xN8yy+62OTUkczw0LxJ4qo+osp+x5pRxzBtCHsVl173GyqhlqUM+n/YSmmS4otTFK6U9sh6pxGd7HFnCEOyO6pwwMnGpfRV7HRd33cCL5HXUl619okUkFi0uDacpj2tRb1NFv6lXU1uVe5RIozkETvQFVbi0FHutxvhqmS31jsIMnlfcpvWkJOVe5XzUGDre6mZhqLhYYRuecUrWkSpiS4Mr+t6b9/AmHI49njjC3uyRbIdMojDtk9FQVraGGPFW7WkbYQzyA1NCbuVN7JmSQcbzDzLW7q0t0YK4HmKDKbdGiibrBH8UpYDVyOXU5qy4kViEDkI7nBL9DKK8lSyocKLeXZuEju1FpMm7FReNzs7WbbbREgYMODhokUhPsWooHwqQ8PRFarxkZOet0IujVFlZFo8XM8NkzMGHxbhuWkHgGVVekhqfDrt6fpKxQPLycdit0Gd1YXpQKW2ZXwqndsmGfFTL0BWW7LyUo3iy4lpnP46CdhFpBUnlQdHspcGiOgrgku7LaPlkhgYmXO17ev2VjjeSi+1iNIQQmPWHJGck4RVfCvn9DvrWUttoO/7lcFSEZYdDvqwJ6mOXyW1fj8wrEEpt2Ssmwt5u44HlBK05MKJG1Qq9z1qwSCtjpBWrY9GEG33S1Ck0tj18sxE9pYqoLpS3ets3dX5Deu0IdxePdTnOExSzlLo1tXJjVfnDjPKRPWWsL0/635e7FS/M1eoH5JX3N1HvH7ZxznHnHZKQ2qGnBaByxKsko0DymrNiYmTpT7u+EoxCxe3jvrECsbGFiLhxFcsi93uDk7eWgfipq3JbpXzQWbroy05EZkz+C3fcmVMLhsOK5fYkdjnEFaiy1TgI/6ITIHjBqc4vLo0Ddq36irtmArGGN9NNRPGrIjnmmQjcaK0IqlRl5XipJ2INbYaCtzz1tTIixSl9hVoncxVAZ048U4PywHRNNrp94i26TaYRp6LIhSk9jhsrsVeGLWGWGLoPQ/tm+hLPWV5rm0XqkoTW/8gjxu4FlufBmtEzlB3ZhfyEVCJbux6VPgjrGcqlZws0DEHtIpepts4yrkxUrJT8JGij6fmfmHIDaSfoXvN3D2K1p0Jlit4jWT1Mt/4kA9l3oo8CRi0sdTiRIThEMIJrhu4UAYHjR4RVQisuyzYd4Qe+V1gxJriaD3LKk28UcSdveZRCqXGkrF3imbVgryZxks6+m0/AFDkNo1RouGejo3+0B6mpduZ07mGO2bEo6zzDY6nXZrhVyk2KkgJk2y8PxbedFTbEXMq2XJA8a/uFEFi6zZx79vALozp7FwImRCN+yYpdHnlBSO3RwBClPot1wVvBB3N5RowmKJOR/sS5yarRjJPFNdJZePz6V7cw12gD5y+2mbM9cgOLe2KRR0uNc0+BRVK0Eu47CqI2PHLpcIIInFdeqAmn1xphNba1kvqwliOHtNVZG/tkgj0sfI6FxO0addgRE2ZYawrd3UId7ric6QuDkFHnA6XaE1zyVXeJ9nlZvMif/cSlWyXYmPyG5LmsIpuNRyN2khR49h0tl19VKl6l+94p/PwZMku7RA9wvvdpnRz5Lj21o7Jg8ZMXR26Rh4zLJJ2Fyqd3L1wSALH5g6MdhtEyAbNi7PTxdEPc6lAj2qDUXSzyULOb6TDbe9tW5mzyS1KOyMnsxDBnAvQ82H9Lllu1uqeZ6fOdY8kbblSJYVrtTrH3GDFpUybe1/LFMqfRKdSpD3RnLbtvS+3fCIBC5F91uxOYw8fcAGdTNRxQDvD1uwxQffnQ3vKJiym9hKHdYlNgKkcZUxiy3I4ozg0aw3qHW2dY8KmGRgdig1M1SvcobllMxVW3aFTnxrhmtq5rrMM8YsynFfFIKrClTqh4lD3x2UhhbizR6SKBCPOtiD63QA3Zy6hJt0eM0MnLOIqhpBVUnBDGYhp7P0gckh6p0WHwJFYJlQuE3u8jf7ljnKej4xI3h1YCfUHh9nA5LXIq6SAM72imtGmS1QirIOn2H4vZaKA8gQsjUTsY5rW33QXyR0eCjcZdLJHNqXhCsAbbllBt8WGqk6DC5h1SjFg7gYrCua4FbASUjPfxE6qEZ48WXOjy4iIqNh0Ey7QihivclYOrbI6a2iktBGkNCyRTGv4tHQYM0FPXpz5KxmzlYpYH7gKZ6q9pmQdbQYyKuXYME5BIYYAXAUTp/k+kdvcLBq8xd2d0926s3aLlvddduNQN3MbNDvBfi9gfIw0RHvL7+f4YqMRXEGit1ZwZuvHll4fE6EWvJPjXHN4A6NxMkl3rSYVHm5vghjXdF8MN48uQH99X9mOrEN4mnUil0FkOKhistGnTd2xG9SqHImfao1rl/haaLTCKthyH5gXkkiJspfcWLr42na1Z7hBV4xUam+k0DmbXJKOza5pnSsXeDqu7uP9FFIVt89gUlkekrJE/V2bC10B4VpjWtvTicw8Ch9Ra7ksKMqOhLs9bFauYKwnjy0bibxI8OkcCRgKuZxQV/nkXcmqXdJOxm9K22PhwHbHNdY1q9Dn4rXd6yoxCA0qbf3zlqhNiCQQqOen6310U5sUPSgqN9xqrw0YpJvCuEprzRYp5r4MjixaHncKfrpSlmyc6jaiHbubDtORLsSztjKuTBHZF7ESGGu4Lbd1Mvh6Icecn0xYDzsJph2nZgruu8gf82MXIvC+stT+ZhXb/o6AyueKqzgOGP+EakG9qVmoPGR4HWOmlh1c83DerbbpPYHWpxa8tvHycFlqEVeRW5ggHFrIt95lUn32chOntbrC6yXhNOeaw+jdtVnpSA+TIhNf/K647I9wl+DVxjCRK+kOyZR76RDuTtGOXbd0iKw5/DjVZBcxGZWwTRVc+CPBGuw6O0qOZDSeNOIpVXjlYN7sE2Zz0z7Opm4gyHE39lrCcwHa5NOVZ8a12evUnmP3Dqee+YPFFN0u8bOOsG5jdSvYbYzE2YFY5kVSyWV2rqprvoJ7T7baEHMjAA6iEtLOMKxtrlbOS4S7pK7RkyHOTbver2+Nz5DDWCrYsiUblAwGyEJz4nYVyIttDBJlHiFxvQcuuoV6F0xxnF+rk0QXWX2f9pBWmKNK1PxShPC1v5sUVBEDWdD37Bbz8mvLtjyYvI5nLtpkSm8IiniqCLVe7waqjzLWdfIqc8Siod0BhS1T0LPYq/GEO56PEpbL+3Z7y/1Y6ygiqnoyj4YTxuj5mehY6VzCzmSgEgnv1j2bG1kM+exestlh3xwyX13akJU2Bl64YVjk6W48T2nLmRVUn8xTcDtGeLHt6PXaPs+VKybF4FSiZ5Ak8drfGsqUXJBrDevhxm2Ng9ny/KYXNEwnjv36Kpak3LZrrLTXaKXGgbT2dFOpZYiE9rt7Cp23ZLsprAZ3MUrK9bhEXCGSptjjSCOP5N4RHQcz01XHkIovYBbSyFd40xa7s8xBRun6YCRDU3/tUUIlYXtWvNEmGAHNgG5NRmg9/05HIkeDtiokz/Z0K8kpu+Sx2gX5pbMVjLt0wzSuL7nPD1RQ0n1EwKnaGdwmw/YbfhfpkKed2txjWWmDt6ftARWv92GpOJedUuarJNi1ezCL7y7H0zWQ5cLzTNy4HiOF38BRTbk71T4ez6EnOmtGUTbH4Eqyg+1TmtuIIl91rrWPSHpls7Fbtbwo7C2J1M3a9E40eZUnd4fm7cHFWIG/q9TeOZLbGLowZ/RQX4Ny5FdjM/EF5IKKP3YnB0fRyh07KikkranOZCWA9gzttlSOIUXZB+NwK80QwRy1ETi3JokRdgwQ6106EaWmntI43xf4qr4vt5PdI3cODCTYPuhr+iZbm/IE4xucbF3rSGB3ChEGXR+6eFMqxv6SnFJlKXbbLsNuxtDvOgeJXFuGNHmLNHSfhT512BbL47kC0HBhWwI+CPSSsbq9xNtWH4rjWTI2+Upv/W3HNtIGVq0SkvPLRunypeh02pRgMVKFOAKpVr4SG0ZJ9DSi1d0mofMbg1y5WD6zKOhpqZwAM7xDAJgiSsxlj63f8HhGO5pvEuFgYM7kHvOwFsLx0vtnwa/yNvF8Ud0U9D2ui81N94YLrhIJN+bGPgxLJrSX8VSYZ+RsbsqmWRtY0V2hE5WYkF+snEuXiIO4plt12NnZzT0kU+KY7dUalVVX1aOPIwFz9XifkY3ViuNZvj4xA6OpUmasje1uJEQTFD/BKkUCamwXL1bQyZNqqVzThm+sAfA2rgPzy12c2ULhr5SAHeTOMNiJaAtntJdUSbYVVNX3NQkULZ2N6BMXjHIECCrIsLoQ4tp2pcaX2yWlLKXMlI9ZNk130JOUyqViLx4Ks6lnQdGa9SQAJXt1HfQ4ZKNnz4rNaifgwZ6a0CPmOgjktDa/WpVBlNv6jZTO9hY9b6Cgp2mMZyPUbNMUJSTTvXtrc+McCbUf+nSdt+HhsqXvekyIcK84W53F70V7M0DPBLf5DuAgYVVD1V94Lm5Ffzy7o71rZTBKFfh5dVjKEe9wTm7mwt4VmV0XkJxDdxQZNBh07ZBC3MXBXpJa8dSQd30lHXNXPqdF7PlkumbFY3BqGWM18LhBRFyag+nwTCv+3nMxb92uISXv7YRuevbuQ+fCXtqHE0FfzrkogYLj7femllwnbDrdD97GEhBMksLA9NxUvVrUdrv9y8uHl29HpS//nUfG5oOd/7EzpOdR0JdnPx5Hgb7tfXzw+vjfkvKvH14qNwIyPk/T6rS9vR9C/c1Z2uu/cPo/Exyfz2p9Ofp9HnM39m1+8Pklyj2wtho/10X6eD4E7HDaen42sp4fn3XB+/cnnt+rOp982rX/uSk+P56u+7I/yueHP3wveq6Zv97eDx0/vHjvDyt9xojVZ78qZ/3fnykAamNv8Bv28sf/BV5Vb9q4LgAA -->
