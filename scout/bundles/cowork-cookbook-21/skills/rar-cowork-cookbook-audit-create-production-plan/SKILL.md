---
name: "rar-cowork-cookbook-audit-create-production-plan"
description: "Audits create production plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_production_plan", "rar_sha256": "c26dd65fb4324a69f5b6d0dbc6daecfb98f45d2322144ecffc91abff968b6d97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_create_production_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_create_production_plan_agent.py` and in the RCI capsule.

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

Create production plan Completeness Audit — Audits create production plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 c26dd65fb4324a69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_production_plan_agent.py` first:

```bash
python3 audit_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_create_production_plan_agent.py   # or on stdin
python3 audit_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Completeness Audit — Audits create production plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_create_production_plan',
    "version": '2.0.0',
    "display_name": 'Create production plan Completeness Audit',
    "description": 'Audits create production plan records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '515745bb20bb5cfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditCreateProductionPlan(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCreateProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+bObSLbmv6K574eqetgWq5Dc0RGDQCCEBIhFgMoVLnYQq9ihpv73SST5uup1db/XERMj29cCMk9+Z/vOyeT+9ma3TVRUb5/fVN/OF5ydpnHkVws79xZ00RdVAv4rEgf8W7hF3lSx0zZFVb99ePP82q3isomLHEynWi9u6oVb+XbjL8qq8Fp3frQoUyC38t2i8upFUFRATFamfuPnfl0/1imLNHbH5/3Yzl1/YYd2nNfNompT/6Nj1763cCPfTepPYF1/sGcB9dvnn3/58BaD72+ff3tzU7uuv+GgHyjkdxAywABmgp8hGFKOQOX5uvQrACgDtzw/WLyufqz9NPiw+M//THq7CuufPn/JF6/Pl7f5j9LmiybyF01h182MzC5tJ07jZvy0oNLeHmugbtNWOdBuUQOL5eGn58zvkopy8ff52Y/PRT6FfvPjl7cCQLBnvF/efloAS315q9r5+6dZSvnjT5/SoverH3/6LqdunZvvNrMwgPrT19f1SywY+H1oHDxW/TuQ+vSc4395+4Ny8+eJe9YTzHz7dCvi/MenYODQzs9n5/z40z8T+3BRGtfN/0juz0/BkW97QKcX8J8+PIz8ywJ6KfQu858vOwfYv6MJGP5tuQ+Ll6H+meyH/f+L6DQGkftu8b8U91cToL8vfv6nuv2rCR8WwZc3xk/jDkSHk/qfF799VeUd/fMP3vebP/zyOxD934pRi7ZyHxK+ZnYeB37dfP368w/14/YPv/z8Q1uCWPPt7GtbpX8l86/s+ljnTxZ8jfrxz3PB+nqe5EWfL94jffFbUf6v6vdPi4udxt73+/XnxR/zZf5Ai1mJb4s+TfCHnKkB1j/Y8ae33wE5ABKpnhQwc8N//MfiFLtVURdBs1Ddop0ZJm/izJ/Ba1FcL8DfObcrH9i1joFhX+NA/M8enhEXweLX/+0+uPGj++LGpT3Tztcn+339zn6P8Pj100IDMosqDuPcThcKJctfcjv082Zer6z82q86wCTO2PgfAQd9nL8s4nzx678S+/Uh4VM5/vpg0fjJSgrNz4xUA+b8NGtlRH7+0sEFROwPvtsC4WnhAiRBDHj0A9C2LtIOMNpsgTqJ03ThxYCyAdGPD9nASp9nYb/++itg4+hL/qRQbPGsAPUSDHiHs/j4EagUpHEYNV9y342KxQ+//f7D4v8s/tWsh/B5DRnw+MsHAOFBlcQFyKk2A8OAe4BDAWE8fPDb7y/DAjE5KFnAY3EQ+8/JICYT3/tmZXVPfUSJ1cLxgXWBZbOyqBrAy4u4+bTgg8U7XrDo/Ghm7qgABcjzSz/3/ByUpyaygTrvlsyLZlGDwKuD8cOirf3Hqr861aNw+RlIbrv5dXGiZVAnihT8mGE+BoHJRR4D87/HwPM+EFL9UC+230R8WohzFC5Ku7LLqLJfawT20y+gPnybDoTbi9zvv+RzNfRnUz1S4mkeMAhYxn259OPs87nWgvz36m9rP8bYczXTHlWt+pLXr3C3K/9RvgGUcRG2sTcXgb+9QqqOijb1HvYDSGdJLy94L688YpD+66aA/mMj8Kjbiy8tCiP44v9TMzFjozhO2XGUtmMWO1FTrKfN5lZntu2zOwKl/bHYIz++l/tvZPGNM7/kaQwCoBr/9hz5sPRrzJOH2gosrlDKQz5ABWw2y31E4RxVVTXHr/0l/0bOH4BjH0wEdAcpC0J6jqRvC85PvyGNQF7O198L9ctOs1VApC3K1gGWWQS+7zm2mwBU1ZxJL4uDkPTnrOqj2I3+pNUCSAeeB/IXAMTsFkDgD9OJBVATJFFQFdn34fHc/jxdBtCCXtL/tDBAMswBUYMMBD3MPAZY4YeHqEXmAxsDiO8WriO7fIKZ288XQHvm5Njv/2j/16PvwftAMoMHMm3PboAl+5lIPX94+vUd5ctTQGg2R8dj0p+d/dJ08cca8rcv+QPhO3eDLE7n8vsH0yxA9mTPWJxJqAZEkvmv8AFx8Ki0n57F8lmN37F8/oeO+8d/ryl/lD/9z377vIiapqw/L5fPkvWtYn0CGbIEERKXfv2sXh+f6fbxe7p9fLRWf5T5NNHnxb+H608iXuH8eYF8gj/B86Nj7PpzvL4+wAz0x631EZ+ffskV/7t/wfJFBqhtNvsIyuV7Jfk2BJSTsPLDefCzstRzQepBDXxQKfDAl/w9Bl75AZg6D+cyWBd/yNtHSQUefTrsnfHBo7wBa3tz4xX6834kneHX/tvnvE3TD2+5nfn/zT5kZnQQocAQ884F2Bv0ME3sP66AQuBBbM/f/7zDkh5f7PQZyXUDENrVgw9emfEiug9zA5sDLpk3C3PZelI82OLYbdrMiJuxnCE+9yZzn/TeRP3jqo/UBWt4xec5gz88KPjD4r13/bD4tpt47M3yFmynfp775lnPp7rvY983jY7/9stfwHi10f8ERDyzx8w3T3V97zs1PDxW2g1gQF05AkiF+2gY5iJZj49i+o9qgwUr/96CqujNkL/b4Du04onn94cqzXOv+NvbN3J5Oe/VF4LhIIs/1nNdXILYBguC62cUgmf/Vsf4mguIEHQtYLKLrjxvRQQOjqG4vdoEhLPyYM9xV57tu4GzWQc44aEYiiI4Dm4E7gaxnSDYrNZg4IYE8p5x/HUu/PGMB7Vtd+2SCA4e2yvXx2AHc30ERTwS82FigwXrtY8D07xPTQCPvpR8KjVb8L15nY3x0vW3N2eFg5F7vOap54debi72CiedITKhauVbpxuUaKomeO3JSI4Ni5StaI/b4XY0NV4MeYZe32yn11UXOqeNyVJ5xssc55fimjiRg9Bitt0k1IkjLPyEBtJGq82xk9awkxmWmrJFICVx0l6uqwPfw6NLbEDq2uapZPZxtSt1wSQ3kBKQo3XDIXrX4EifK/dhPPp8G2rbo3LgcqEhHWKsTlac054djnpfeqXJG5FuZXxD8pBY4cVmf61R32TXS8lMN2tBJfzuSK57xe/EQdifEKpWLvElQ8bKrTdmqtRsWvPxjVWEaUk3g2TfT7SJYzyhsn56JomldVPby5gXR7FglmorZyMpHg8hZJScPd47jV0Pwq65WOqpGFHLvhpwqWg7q8T0qFWlNXazib5dQ9bKuGMExivZeQNF9707WiuuuSXhjZ/Gjo8jthKUU3GjoW0ChcmRzupp1PgUOmC6w2YEvqZKDcmz8HjaMdm4d68X2YojbLoa9wHuMhg7I3xT2XuKgK/3ldV14siWsnaKkyyDigk+B+txN7BXullnhW5P14g304MYmBNb8HEL6dj+gmj10jwdbc4cVWPr89fhxCfHk6wwt0redbmPVvtoKhNuewwSGhszB/gpH7cyCP7rdDgp7mC3quvV0HQWeSJGEMstSo+wB7i5eBm2OzQbgRjR3kfI0tgd8nM1xbcevtFYCNHY3Sc2rrIs8oPQ52ZQWBV71PYs7zmjONjKxbja2InOQD4fHf2ckXw9cTx0W6YheSKJmNeJ5W53geuBie/jlbGHK4eEE33vWxWkdxREjbnXS0n0vJgPIGq53l4qwqhVzfT2UBh28hUeNlmOioNHp84dOt6DbWvEjbphN6yfsTFgF23yk/pcNYDss3TqT9YQVNx+i56uKXHMFBxLTWXaZdPWUSeJVbUqUn3hzNuoZ4nreoSbqD6ol5YpFf7oc0utp1A65Fc1daLy3d1JrCTiXOrgdWejj+QI1gcLc7JEjB2002tsd69vFdSLZX5RKo6jhT4KG+tMKWlMUjjJekdCWWk7KM9i5ug0IVHhCi5WZ3hr51oVL0cfrwwI6xLdXE5Od68hE/eqcCPqVnEht1PXUQSXsgwP5VY0XJSIJUvxbC03pykQe+NgwkKlVD0t8OzVJ/QjlCljHNtXWwijoCK5kMxp2iNXbMceuttkDvhej4Jb6Z/yoSOQqnMT3fdOPbR0hFjr6aRIDaMobKRJfTADlg9N6Zzh0AVmNpjjkIzs9lCmJ4Vn5MCHeNp3zqvk3pRk19poEB9ccdN18YFwrTDRtiu3DXAJ64MUKVzRk416hWtTtNpRrYRubXhHjxtFcJzdSRfrIXFYW2HSy93WbVONjtQAG+UFinFIOmpUx8OmvVxngbxfNzaZNCw6Qb10MXYmYmXXdStAh/BIOnsxva6uZxQLJQXTJSQIBe2S1Stv2LT7G4bjQQ1tS0FOWpLq65N0lOks3TGGATJ7vS+T3IiLVCuz8KwSLG2lCY5VmLVlpbNzUFGbuGtdyPpBjreJTJVevzldib4ixymQTbkENcc9piUzHWtMXYYHP+JPVUTGIbTZ2tFa3VDKAdtmIIzQMt4nkrpbnyZ7o4+af2gSh2oPbXSlBo87o3FWX+gY0MNBZq3m0h63IUUX9rGs07uqJLsCrU/iiFtkiMTsWeHWPVV5llRJTi5bslRMqkzEWrWUupwY3M5M4bN6UXbthTt7ARToqm5fgxCalseGsvQbk1zoCeo2y6hm0GPVcEdLpttzdBvW0LLt8ttKLmDrVPjR2JX7k+6towo/XOQuXl4P1vYA0yf2SN4IIRnFAxfpd8IQ7oN6bm63Hawpu+nee8dwa9LLHX1VPaNJLwclRPl1vyKohMtttmVaTQzJou8RnCdw8x6uyR621gXD0tl0KpcX40jWpHBIXGPS8uMG62O4K09yAyno0HKqloRrVvRVmSVQHW8cIXD3Wzi2vUMuHGtx6uGCNqFxR22pUb8KxCUr+VqETpZXZ5gF4xcr7DcKPcVD0Fhl6qyMQjRFSDrbzg4tfItq1e22iBOCH7hqM3ZrL65a3ub4igzKCA3rs3GpZXWb7c8uF93XJ3LjRHeg90aRWnRk0dgobzaOIwfO4LOwT/NlJNhnKe2dphYCAU3yUk4Yiq1F9XoUqvPF3gvjeKtvl8nKeXsp4byQMkeUac83xcalc2bv9Vq7XRV1h1cp34/3owh6nIBp9lmc6nFSDRfAzIRx8C8jMq3VgsP3kYbAK2KTQdh4kVZ8ouzoeDXFyjF3xtJFMasPOziK8Yi++fZ2kpCEaPjj8tBcK6WIWXTjJhkGDxdTEfE7Stwb9SyvxYq4svc0bZXVSYlpEj+epExY8aRnXc7oeDRLMxJua7IY9RvdWqUaUHKu0YbdC5sxlHwWaUM1O/CIsm9CWN3KfOrG9PZ8z2Pa4g5Za9FMQhoZg9BBY3YlY2CTHWqCs7w1rkMzUMNhGyWWK5nTpVbg4hpK7O0aDS92VtKpWsNpVUAYBBLhupEgkQtT3CN4HK6EFRZiMsw117IcW3Fzu60G0/BJzielSz3UzFCWm5ZpUiN0LEMuBGIFaw4expR55BmrOMrZsYl428h6WVfVYYq5o+TLYep2x/WqPA/ZnksuNqP7aGZf+cY3cOXc74grKfT4Wb0KfdHjV7ctutzclG5O5cS+Y2W+DyVTvxvYLREUCinVna6PjYrCbnZp0u3Wj/fthbfjdMuHw6g1rtmHQRDzO+wM4rtOG9+uLidHj870Vj9vtPsUpUzM20G0JUF6rRwdacRDA7DcqDGoT2TsE5dpz59bymoKHbalw6ndB9uulpvjsUrac1gb5v5g3WoTpvfhIMGVourYyh+3SyJWM3gsd4CXeA31EbBHi88+fRW5yy5Jk8u91RAm7hDLWjuj4VUbjRRsAgG9AHLNjDSz/Kba7hBbyUaXQzKr7ErhXjvZybbLLdPqTjzESC8wewP3zgkjQiKqVsebQ+YdjZwcttr6aaHaV7hpsZZftUJ6FtbngM+nvamZujpeWZEPzidTzO5tKN52V1D24pstKjd1RKorE/C4sqKTZqMH+4DYXNV145WqQNPWtF2hmHzXbYly4C1yj3gQdVAmo5N/Q1rGVIvNusvC8ZjwnaFFKApBG8SxpusVC6taIORYlYujL3KbHSFe4mAXr/kgj6Mze92j1WFrGVp5oPqrXB6yqKWFdRw0KF8JWn8PhPykUGmYM/5OOTHpVGgKZN5aOderUr9j4Q5sJUaBis/ROZL0sLmoBHE3Ez3pj+1p0LPIaSTKKA+JeiI0A9vngpuL0p2XUG6lBKsS5Wv2zhH3pBfg0rb9W33izZ6JU7aqD6Y+YYipIIwhNlbNCLYlShUFrcMQxuB97KGsbTjxWAyZiXbUANpipDBFgUPv7FlAFV6ssJNFU9R6jULn1Ymz62zYbpN1fdGiHuMPPueY0mkZ2TZN26dI6fSGvIZ6ebkcBC8ySm2yC5mrGE8txYt5SJC1iLt3bqNgt6OL8ITZ7jIJ1o8t6P/8NJLQ/JjGO4Nlx4LnNW8S8ozzbBg6HOGJZ+q7c00iQ3cu4c7en1I2gOBLSzvbWHGEwjnyYuasI1YgJ/e0hit2Kq6eKAeJmjBseSKVY0uQuenZ2+M6Y1bhcLd7yWqk3NzCuU6s9xasaIHq557HrKBktRxWAn4KNvJxubzsKnu3ItW1fM1k7+4hlwDbEbKYOHEIS15jc8QQZfiFtDcny520IrW2xZnIgEmxO05tEo9Mb7agr+WKW3L5tVuO0NZjext1MmbtaEextusrbrJKEm+KO2jAV/5WF+VkX0urkSEksxeWQXqHpJN4zjJJrpeH1c6FNA4dZc51JSKivP5mCZzZUITvNSu3MJtkkJbskBt20PjB7TBqLteBlU/d6jbqZQ+TbR3g2Xq/JSbFFNJlp8vM9Vbi560JN96gaZMzYOxKD0tSoNuVJ4sd6H/cZGxCp6FcI9OXZeVVu13nD8FZUA+o4k9TN4xXkiUEBWPkPXUY3P0hubb3vZJdYJ+JJpRC1+F5LXWJWw5Yxkn4oXZq+sZN625lEL7AqUuhomy8c6AadE4ZKZIDRnjGnpMEs8FDUHUc5+qG4rUlVfFgwXFDaK6jr8scIUNX7/ARNs+YqTSNqMHerdD3ItytizvkQMhtMBllbbBC5tKTRekrS8IwrMjPG+y6VGBkF2hwZV53hpptRHXrucYZbfKrYUb4HfFXleYzYMtSxegB2fh+3+TQzp6gExQn664TTFxjx0am2Zbf7pz4WuQKyhNtK+MjWV631u7mE7HfdibLXI3N7b6idx0t3j03JWqVoNJgHzLOUNOn/qAcVkfDQtyri0frLXEQpaY7eHrORGo5bQxmwNd+q5Fdh1CjeqFV7VoMUjoIx/42HCp7KeDUunfXR95v+27AqFUpafUpHlp0ua6JmCvkHmy8HQXzam80DDy+on6Bk7xxxfy6SRGwFWUna7+9ShKI6w1VqxsFSfy2bYuKkBysSocG4qPhkK05dOiDM6DO0BG4qOrxsY17l7t4mxXU+/4w2sJgMG1M7WUfF+OEdG0HbKq5zt2Md6JEA/Fmgi7ufEVunLvXLu5SydZWDLbCTGJ6B5lrb6IX14PMMzFsQsw+m9QdkxCcCYc6RVw218lPj7cY3RA9hUGUTbpdRzN47+whp98Zk7NvoVVEThu9W55MSoamqV+JzHRDVpgrdb4ZZ0gHlQwTHDaSbdk3hmRqX4IJor94d6xdumRAOhEDpRualAcjuB+iMLwNWySiq36rrVLWoa4jCD5HIbH7juFst0Yk9pgv2RyyTiHMHm5ZOeJtEOT3805IukoA+/Qa0acN7908uzayG0pAtoxsZeMgH+OaIgtEpNF9sl3CB2sXJIWorlz4zrel1CyNwTA8h+wUdeN7SIG4B8plVQRTlteYkI76TpqitVsqbjKcIEXa4MR5a+HUFI2FnvXKuLzt7pcbpDoxUW4lU9IPcY4b4r29mHcdLhHQarJX8p4Ol2Zlkmca2QZke9maYV2NZthhCMIJvKZd3WHdMBnb+RXMZdiGu6ATdQ0zEc0VbiVu8crpjrE2FCyiLZkLbTYuebKsHY7tndAuRKw+XppNaGVK0SQHSus2NXVD+Zi9sKEm2fI43dzcA7GidT2ZEkWpccg5L7A1o4UKG+R1SVHU398+vM0HpK+D6f/RK+X51O//2eHj85zw22upx/Gwb3ufH2t9/p/B+eXDW+XGAMzzYLVO2/B1FPlfjlU//qtXGfPM8fl2dn5rNjTfzuwbO5x/negtzr22bqrxa12k7eNQ98Ob09bz7zfUMzgX/P/2UCYr59Psx2Kvg+6vTfHC77/Nv3kwvwYCHRiA8boMX8fLH968Efgiduuv2Ir46lflrN7rtch8Mju/F3n7/f8CNUzo6ZslAAA= -->
