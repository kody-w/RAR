---
name: "rar-cowork-cookbook-customer-adoption-materials"
description: "Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_adoption_materials", "rar_sha256": "15d44695ee41d1433201801bcba8bad95f3e37f2181a766389ae958b6721d612", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_adoption_materials`. The original RAPP
agent is preserved byte-for-byte in `customer_adoption_materials_agent.py` and in the RCI capsule.

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

Customer adoption materials — Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
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
    "customer_name": {
      "description": "The customer or organization the curriculum is being built for.",
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
    "product_and_vendor": {
      "description": "The product the curriculum covers and its vendor, whose public sources are used.",
      "type": "string"
    },
    "program_type": {
      "description": "Whether this supports a champion program, power user program, or broader enablement rollout.",
      "type": "string"
    },
    "skill_gaps_priorities": {
      "description": "Known skill gaps, priorities, or use cases to emphasize across the levels.",
      "type": "string"
    },
    "user_base": {
      "description": "Who the learners are \u2014 roles, personas, size, and context of the audience.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_adoption_materials_agent.py` and embedded as the fenced Python below (sha256 15d44695ee41d143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_adoption_materials_agent.py` first:

```bash
python3 customer_adoption_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_adoption_materials_agent.py   # or on stdin
python3 customer_adoption_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer adoption materials — Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_adoption_materials',
    "version": '3.0.3',
    "display_name": 'Customer adoption materials',
    "description": 'Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'customer-adoption-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-adoption-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55d78296864b5bc9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/customer-adoption-materials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', "Output matches: A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program."], 'confidence': 1.0, 'deliverable': "A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The customer or organization the curriculum is being built for.', 'product_and_vendor': 'The product the curriculum covers and its vendor, whose public sources are used.', 'program_type': 'Whether this supports a champion program, power user program, or broader enablement rollout.', 'skill_gaps_priorities': 'Known skill gaps, priorities, or use cases to emphasize across the levels.', 'user_base': 'Who the learners are — roles, personas, size, and context of the audience.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready. A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program.", 'expected_output': "A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "I need to build a role-relevant [Product] learning curriculum for [Customer Name] using publicly available resources that help users progress from foundational awareness to confident, practical use.\n\nBefore you start, ask me: who their user base is, whether this will be used in a champion or enablement program, and any known skill gaps or priorities.\n\nOnce I've answered, design three progressive learning paths using official [Product Vendor] sources only - no internal or tenant-specific content. Format the output in Markdown.\n\nFor each path:\n\nBeginner - foundational skills for users new to [Product]; focus on awareness, basic navigation, and first use cases\n\nIntermediate - practical, role-relevant application for users ready to build daily habits with [Product]\n\nAdvanced - deeper capability and workflow integration for power users and champions\n\nFor each level, produce a sequenced resource table with: title, source, link, estimated completion time (estimate and label clearly if not stated), 1-2 sentence summary, suggested audience, and prerequisites.\n\nWhere relevant, call out how [Customer Role/Persona] would apply each skill in practice - for example, preparing client proposals, summarizing documents, managing follow-ups, or building presentations.\n\nClose with a recommended rollout order and suggestions for how [Customer Name] could deploy this within a [Champion Program / Power User Program].\n\nUse only public, accessible resources from [Product Vendor] and reputable third-party training platforms.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.', 'example_request': 'Build a Copilot learning curriculum for Contoso — beginner to advanced, for our champion program.', 'inputs': [{'description': 'The product the curriculum covers and its vendor, whose public sources are used.', 'name': 'product_and_vendor'}, {'description': 'The customer or organization the curriculum is being built for.', 'name': 'customer_name'}, {'description': 'Who the learners are — roles, personas, size, and context of the audience.', 'name': 'user_base'}, {'description': 'Whether this supports a champion program, power user program, or broader enablement rollout.', 'name': 'program_type'}, {'description': 'Known skill gaps, priorities, or use cases to emphasize across the levels.', 'name': 'skill_gaps_priorities'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a customer needs a role-relevant product training curriculum built from public vendor and reputable third-party resources for a champion or enablement program.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CustomerAdoptionMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerAdoptionMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The customer or organization the curriculum is being built for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'product_and_vendor': {'description': 'The product the curriculum covers and its vendor, whose public sources are used.', 'type': 'string'}, 'program_type': {'description': 'Whether this supports a champion program, power user program, or broader enablement rollout.', 'type': 'string'}, 'skill_gaps_priorities': {'description': 'Known skill gaps, priorities, or use cases to emphasize across the levels.', 'type': 'string'}, 'user_base': {'description': 'Who the learners are — roles, personas, size, and context of the audience.', 'type': 'string'}},
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
    print(CustomerAdoptionMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
