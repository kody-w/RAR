---
name: "rar-cowork-cookbook-report-develop-project-management-strategy"
description: "Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_project_management_strategy", "rar_sha256": "e50d4b60068fe0962b99c61d3f27de226daf37ea33c49b6ebf7335d523ac207a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_project_management_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-project-management-strategy:1e212e02ea4bcfa4e7004888c6954bda451bf79c6fba22f59c2abaf0f5594769", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_project_management_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_project_management_strategy_agent.py` is
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

Develop project management strategy Summary Report — Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-project-management-strategy
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 e50d4b60068fe096…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_project_management_strategy_agent.py` first:

```bash
python3 report_develop_project_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_project_management_strategy_agent.py   # or on stdin
python3 report_develop_project_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project management strategy Summary Report — Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-project-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_project_management_strategy',
    "version": '2.0.0',
    "display_name": 'Develop project management strategy Summary Report',
    "description": 'Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-project-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-project-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9dae150a2212296e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-management-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-develop-project-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDevelopProjectManagementStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopProjectManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportDevelopProjectManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aXPi2JL2X9F4PlT34DLaF9+4ES8IhMQmtACSujpc2iW0b2jp6f8+R4BdVTPdM33vTMSLwwakc3LPJzOP/NuT2dRBVj69PimumUIrM47DwC0hM3UgNmuzMgJvWWSBX8jO0roMrabOyurp+clxK7sM8zrMUrB93oSxU0EmVNVlY9dN6TpQ1SSJWfZQ6eZZWUOZBznu1Y2zHMrL7OLaNZSYqem7iZvW4z6zdv0eMu06vIZ1D7VhHUB1Vptx9QzVpZs64H0UzCpdM3KyNq1egBxuZyZ57FZPr7/8+vwUgs9Pr7892bFZgUtP8o334s73cGe7++CqPJgCMrGZ+mB93gN7pOB77pZeVibgkuN60OPbT5Ube8/Qv/1b1JqlX/38+iWFHq8vT+OP3KRQHbhAbLOqgQlsMzetMAbqvECzuDX7ClgDWCd9mCpM/Zf7zm+UgH3+Pt776c7kxXfrn748ZUAEczT2l6efoawE/Mpm/PwyUsl/+vklzlq3/Onnb3SqxroZGRADUr+8Pb4/yIKF35aG3o3r3wHVu1st98vTd8qNr7vco55g59PLJQvTn+6EgTevbmqmtvvTz39G1g5cO4rDqv5LdH+5Ew5c0wE6PQT/+flm5F+hyUOhD5p/zjYHbv1HNAHL39k9Qw9D/Rntm/3/E+k4TN3qw+J/SO6PNkz+Dv3yp7r9dxueIe/L08KNwyuIDit2X6Hf3pTDkv3lk/Pt4qdffwek/0cyStaU9o3CG8jL0HOr+u3tl0/V7fKnX3/51OQg1lwzeWvK+I9o/pFdb3x+sOBj1U8/7gX8j2mUgqSGPiId+i3L/6X8/QU6mXHofLtevULf58v4mkCjEu9M7yb4LmcqIOt3dvz56XeAFOkdqsbbIMv/9V+hXWiXWZV5NaTYWVNDwMF1mLij8GoQVpD6SOqvykbYbl8S5ysEro7pDiDCbOIaWpVmGL+j26gBwLyv/8++Aeln+wGk0zsevj3A8O2x/O0bGL69g+HXF0gNgABZGfphasaQPDscILAKACZgfQsSgLKfryN3IFl4Rx+ZFUbkqZrY/Rv09a+ze7tRfsn7UbEvKfCUCdznQLWbABJmGcYAnkfksvra/QyAF6BLmcWxZdoRNP5p8pfRWufATR82tEFVcTvXbmoXijMbqOCFAKyfQRhUWXwFSDlatorCOIacsASCZaBijCgPrP86Evv69atlVsGX9A7NGHQvO9UULPgQGPr8OS9dLw79oP6SunaQQZ9++/0T9O/Qf7frRnzkcQDF4mY5EN4xtFbEPQRytRmNU0FjoAAguvnyt9/vLhmlS0GdBBkWeqF72wyofQuMUYO7n96dBHQeRXTLB6cf7Qa1AbALFNbAWiDrq+cv6UgiA0vLNqzcdyPeN99N/+71O5/RJ9XDhsBPXpklt7W3mBydaWel8wIJHvRhqUdlHj0aZFUNwjgHVdZN7R7sNOtvLkwzUKBBJlVe/ww1FVB1pPzVAqRH4yQArsz6K7RjD6DyZTH4Mxroxh7sztJwdPwjbO+XAZHyE4ix+TuJF2gPArSEcrM086A0K/e2zjPvEQEq3vt+QNyEUreFxlp/C+Bbjt8ib/EXGgzl0ZbcWwPoS4PCCA79f2pgRqFnq5W8XM3U5QJa7lVZv0fY2G6NdO8d2kgPdCD3dPnWVbwD0Ds0f0njEHil7P92X+ndguq+5jvF5Jl8oz+md3mjG9YgNEZfl+UYzuaX9L0GAJHHMK9GOAMZHI14kH0wHO++SxqANB2/f+sHoHvUjUqDeIbyxopDG/Jc17mFfh2UY2I9PADixB1tDDLBDn7QCgLUgRsAfQgIEYKABba7mW4PEgT0UPdo/1gejl0WkMJpbCAtyCD3BTqPAQ2CsoIs4MF2XAOs8OlGCkpcYGMg4oeFq8DM78KMLfBDQPPhi+/t/7gFQnMsNYDbR94BmqZj1sCSLXABSKvu7tcPKR+eAqImYw7cNv3o7Iem0Pel6m9j7gEJvxUB0LOPVf470wDALpPqFmqg/kYVyO7EfYQPiINbQX+51+R70f+Q5fW/dP0//WODwa3KHn/02ysU1HVevU6n90r4Xghf7CwBxdAOc7d6FMXPjwT7/Eiwz98S7PN7gv3A4W6wV+gfk/IHEo/gfoWQF/gFHm9tQ9sdo/fxAkZhP8/1z/h490squ9+8DdhnCYCf0Qk9gOCPMvO+BNQav3T9cfG97FRjtWpBgbyh3a1sfETEI1sAmKb+WCOr7LssHnUa/Xt33wcqg1vpiPfO2O357jgRxaP4lfv0mjZx/PyUmon7j0xCIwKD4AVWGQcp4AjQRdWhe/tmNk44mmb8/OMAKN4+mPGYadlYRwGYhh/oelPDKYGMY2r6oMK55TMERPcBRI6atWN6js2CBTStAPC6zqhK3eej7PdJaezaPlq6/yrBLcMBNDnZ65jooNyC9vsZ+uikn6H32eY2NqYNGO5+Gbv4UWewFLx9rP2Yby336dc/EOPR1P+5EA/0ueO9aY11dFTxD3QC1Eq3aEDddkZ5vin4jW92Z/b7Tc76Ppb+9vQOMOPnexNxjzCw4Z9o+Ubt30v128jCHAndGrObMW4N7psJImEsyd/d8sf+4u0euk+vAKfc5yewGTRGoGsfbnP5010uoNC31niU0iw/V2OLMQWZByiBwp+PykQALb9jMF4Ondv68cPrn/TTfwU6XhEXRVAXRl0Tt2zPxF0KhnGapm2SIXDLMXECsTyKsUnPMlHUIxgbNS3Tgz2CYHCKZIA4FQiSxHyIM0VGrwBFPkz/v+j2n+6UQO1BCRKQcgnYwS0Shknac2GGRC0GSIY4mIdSjouipGN6GOWaGGbjjEW6QHIMIxwCxUwbhSlzpPfoMu/ivb139O9+umPJG8DhJByFR03Tpm0KwR2GMknbxWALs10ERRwKc2GCwTyadnGw/2Prw1ejK+8WGOMZNJigvbuOfH57+H6MURIHK3m8Emb3FztlTiaJUpYcWJOSdHVDmwpWeCxiFJ1vmprjbW89Ty5KuyOao+WzYr/m4Uo69nYv1eV55avEMqXmh6qmiR3VC1F6MGSLy/C93hsTa5doB2JI3RWbrX162TmFKl3lFd87fdZ0pzyxi/S8CRtuq8MVogmXobgi57zYi9yes6Kym5CTaWi6JzXYleslWuCl0G8C/qwO++Zc4lKv2EKMrfISU4il45KaEPVb9FTIpABvomt7Rs11Mq/iLXGgxfIQ6PyCxivNIPXrpSa9QyemZY3a08Dd1koW4QNcKJui7mO5Ueoq3G84D+SWf7YLQnUzc6pEfcMmfUPwhUSWybyNpnYnnMSTisY2WQz4sDtvsXOyEK4nQwncOJhXF85sW2nBw34dK6RflrnSiRWzTCpXO3NYMmg6fG4aIkoNzqN37akv1LPZ+bXqY6yM4L7onQ77c3dmw9OwOtGsAfvCmd8aWJL0W0vbdOi1rvCLME+TAG3nc01Za4xtqAed7KZJn59C3dsjYhelwWa9S09Sy5zoIjseejwqju3pbHE8T1L5JcKn+YwLrTNrGfu5joRUlGnqeuFq5bqEmWZqpmv8yh1b3uodce4IRptIoTIkeFChg7yH8cNgma7jzDr1uKOIvqdO3fRQdOiQbWXK2M1NXNd9HDMYNCoIDIweLSNvShHlOTcfQrI+i6eSMHecV9Hlsr/qqhAM09rPdsExFeUpvN7RV2IaHPh1WyZ6pKHL7cIN++6Aa7blKfQm3V8WPT+kTOMmWX46ywYq5unyuligJC3gGkxLCyqXnGbTm26n3n6dPoHLQMxdfDXEhkprEemEGi6tyU0wWS3oGbe61m6XRQtkirJSNOXVlDamnbvw1e1x0tUWcc5N87KlZRpH28rhOFPxkHjpNzGs16a2XZblOvA92dPl0IoCeqXKAwjlQNvFVYEL/F6k403XrzCxmM5RJDnPkKiN15ou1kupxiVsNlnYglAWewEObUVu5pgitDu9lDm/5fSVLKtc4ig6bqvzHidie4O34hXbuavabuiEXF+5KqQIM3OO9bFBtUzWkkVUyryx35Kuua4jO9+fVlNkol9shduKCE9q026/QpgCX7IydwhpgZyeY40rqmvgs3xfZFUWV2lswI3ICQvRPc2VuaUQ5oE2GoBQIrkRE2BLKzAmvb4rXIOl4YNz1LNsvtnjzGm6xbjzdrga7dwm65q/WBQpxmyy2pGMooqWMOi6iJxStTj0k8iXyaMZnfiuI64bvD9sonR1OE/gyDKU1UlztoaBUxFbRzKZmQuJnswotvLWGgeagK5dT/fStVs3iZGpIYcwUhZJl4Ode9HcE5bITje3jkPxbXJwl7TEGLh+vgpC7KAsOc+jLqIuO0eIPF/JipOY2i0xl43ATLZw5nfMOl0qUppoZwVfJpHK05SbHIs9OuzQgyMKu9o4OS2DEI5mwULiHYZdEe0PywW8z53TvkqrJEFy/uxdSofqtI5maJpnSthy3EWkS47ocuvNcYU613MhYZe9uLvKLDXdi/412zkAdYPpqfI3lSk1ksGTi2CXhXrUHTqGdeeqGhL4MAQiXyJ0ggnMJmrweMg6LDlbhSlIu/n2EkuzTOXKfIdO/SOObNBZV6WK5C/3is+uC5JiYVXlrmzZXtbDeToT6lyecxEha9k5JqpwdiTotuE5Yx4ud4QRhRm7rVc2d8Ztp+7xYD0vhoYcZlsx7qjtujcMaj3dwSk8zcr14aoRpH294NPS4gUz7xCaYdZrOYmvu2TwtvBFPzI4bC5TxhvaVDpHmHa0mxbWOZb31rHAAICZewc1w809j2HkxdsscPm4WlzLoc8bRZpx1PySqzos6kSRLUN0r2wDnSw5fgbqtqafNtse8ZeaZDa5O4OLkOCQk7FWgbFA0BMzKSlMpFl0K96n15cObZZkyxMRvZ2gUh8pjrQ6TpjIn5J0fzHL9RQtFM/XNFNV8Xh/9ipdKvJig4stmmCzQzq3431LlxJSVGkk5Xp5YFSV4nf+zBfqy8q/OkapKOcJv/N6UOIc26gkycmLAZj5qudHEmWk87X0HSWxJGuF4sJRcJQTGykFkeSHguc1AVsGtJQdkyszSXlj1/oG6PjXokmyfhb3dNlb7E4zZEzQMPY626+PYEK6UhaeFGvZ90L2jJcRWgcDHy4IflIzWp+0wi7SZ2mZbYawhu2GVVb2ij2d9tpiyg3qiVU2MbM92hWcS8ISPVdtorO8pF45heA3m6zWtIAID7C73qTS5pDm7ilLxc6UkoO873hflPycu+LasHUtbHNkclZIxM43vGVtTDPbadghP1aho+3zI7+QGgoFRTxZZ9bEiXsrqFRug0z8FVZ1hVbE5rmYbGZahU0uBRBtYg+2vmDncJ9UxumCnChspmSOtxPyqZKhe3IXzwC6CseSmZ9zv9gT052N83mx4DM5biQbVkh9X4HGSDgLgo+i3PLIn4rjVpz5iMdI/uS8pOIpJcegW/J3g1oy2Dz3Jbt2sUQXWTan27mMzQmUTNFVPE+PcXWSj/n+AEbIDqPt6/SEzfW2YGUf6UQkj0ByhO5CN/M1nx4J/FrxCtVTg7EQJ2k50wTSVWkLtMvGkTsn2pJdXAxyaiiSPIuk9iiQmDZgfGzlRrtjMkegg8v2ONMWkqZOiKuynBRssGfn+F5tCTgijb4YDpJiedVGVmjyOCdMdcvJGzoDVwNVUjSQMfZp3fUnODeXea/mvLzbyKG9nGPHU0hybFxG6pA61tn1aVy4JEFi6/FlmR877kDDAaFITL4+HhdOq/jtqlWV+fy0XwVtVyhrhVuH+Z7AIumQUnSyLFSliIyci4G/DmHvFE01gxfhpC4NHkZP2UCusiWtGhyM5d5GW/CYzcKHIK45ij2WiewWlp8K9sba8OJlXS64nPUvwToTrdqKe2XWLsoAKRSS5RCMwmdTp98VZysxekU0+Rq1dnbQLDxg+sX6fFr5m7xSFHfu+jA62HFDHpojjbs1EctLZdF5DD0zDglFV661jJMAUbasOPFPVnbeHrQTsljxq6vhHZWwjC9ZaYievbq0MHtqfZhGBtsVV1ooDlNyB3PrtYibYbLb9HphqarRRZddsOWxxYLwjjbTBOo2pvbaeSFNRXmo4pq64qvKgNFWKqet5pyXrriGLT3LWdBCFLPQly4bSzw0nazicgi63CqEkVYBIbTY7Pd+zsBmtj+V3LCK83BJDriOTIudeFkyczWz9FALV7DNG+wyCIXp0cVOnTUH08K0C1ZC29MFJcLMebs/06yjxCE9SS6mywuGIDfnIT6lApNc9ke3Wl933Prk6OY5lLCCswyNE8mWpXJkdlE6vkgGY1kUfIDTEYGapWDPemNYz/vgopJHB45l8QT6HjdApgLhbAZlp0iUhylzylvn66LyJ16rKUZ11g4gna+F0a5c+LL3t+qJ7iYoEeR66mXFbNfxK08SZNDzopi91pPpKU0v4l4pg2jjuK2BwHM91tCEFQ7sJNPdS56YuOn7SDIh0dNgsNd0YZ4ZiZTNzmoF08ubfWtzk3nDwIU3PSMn68CZfIM7E+14lQsKnZM2c3IaTeURLrVWk6bS8bnU9gnlLBfq5cRPMy4k0lPrXjA5bvc7FnHmdnQe5oQ4Garp0psbMexrHhIZq2Hm5bS4t/RkYsgNsnSPGy+YHtv1Kgvx2ZYjYsQrB6XS3eCUZ1fEBRMRN7nQCnU4US2H+GsNEZB5E1INdehLHzPYendYVGLt8Qu5kTExaPcHL51OqZNH+zs0mlvLBTNxPbxw1amD52m9drVi11UyfBQ2Bl6oxrGc4eyhc+uZUzZ+2ixb/thPZ1F0kAhyfwg2eXAM2HUHCpXCJzw+i3TnaOBbf8fKU853+TN9hdsCtanyom/Wij4IsOj6E0xfYRwuUgdC1a6bnZOpekEsT+tk6bV1T4NGlp5seYBbVFL0qdcypDihWDHnLofVIMISvqWu5aaRrhuRHPaCvlMqXEYbjkFS2xI3bN+eB3PfOXtxyJSLzqDbo0eRZKd4YGrCFhx7dtg9LS2rGcJFC4KYcN2AWq6XOHS3hLfbulaxlRCXi7rZ7ix+qK/qYO3NwjpR11nf1fCl2SdWPuUpTzjVfpS1y6lNJlG7RCbrED76HQtmsiUZ1rjsdquuHaYC5px2q5l2TapFx3B4bglF4JahjmZ+cV74l4RohlnQbofzkrXcvU/slhS7JRJ77eLUEBItFYI8nsz2sLy7ks0lJavVQsan7I6XPHaDgQExHurJKuoQYeniqjGLZSJz99SyHypSBbDYliUGo1lzvcCF3nhet7Q7Rm3oaV0iPYN6vB0YjYAyqSmKfZoYvjmcVTtLCNsUB3XdzcKrZVoBNmg7p9oj1QpVURJB2p5EBFsiGjHf01tJB5MKo0+PzkRMjznltEujhy3aI9xkYbqbru5Mzoa5GoV5Ex30tVhRTW0njcnkeYXi2U4ikK2gm5eQRGZWa2EBH+2l3dLwTugMC0RsDevL44JcUdjG4VWZXfg0z8PJUTuJTL6wV2m6ofgzLi/aS80UR2lRkoN1qJgJJRtIimxpGkwJbj3AenXwBrSvKOXqHtnrwQuQOUM7lkbvgxNjlXhzLCykzJgegeV9k5QWw1/7g4ZHwmS6nvj7Gt9qGOMrF5877zaZzx0K/VRuc4qOex6VwTimX2R4cFCb8+bMxsPh/QxeRvj2iNDH65Vp83B1yZdiXMUYggW0l9dOp1udNR1yrEFNXy2XWtQp+IHk51nXerMpUm+WG4vYa3yyyBzU2BRNPZyJUqzrPVbnDSmSOtGUfLLKVw52SGxGXVPsosXB/KEeEfx86JnLjm9na41d0lribwZvEMNNPsn2BKiQOWZsiN3uumEqpLeczSR2kXKLbedTXxSu/lmrTqi0njIYruCLLZXNVGww5ZwnwDDqEykIYWxCzbizRvGnlGIlmbYrutnBm/P6zK8sDqM7gVOnURGLaOOgaCXa1iVt+Q3r8LvOdOHV2jd1a9mu0UmeidPlGYBrdHRNrzt1lXi4chtiYCuaKg2KDmJU5P1Diwopf2U2s9ns6fnp9qT26RWBcQZ7fhoP9x9H9P/csa0/hPnbgyZG4vTz0//dCeL9NO/9cd7tvNw1ndcb99d/Rtxfn59KOwSi3Y98q7jxH8eH/+nc9PNfP9Ud6fT3x9Djk8iufn/yUZv+7fg5TJ0GLO7fqixubofPwAlNNf5rSjWKbYP3p5uiST4e/d9ZP30cV7/V2bjMC8drYTo+XXOdEPB+fPUfJ/bPT04PXBna1RtGEm9umY/6Pp4vjcer4wOmp9//A80ZwGx2JwAA -->
