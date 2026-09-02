---
name: "rar-cowork-cookbook-dashboard-issue-requests-for-quotation"
description: "Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_requests_for_quotation", "rar_sha256": "ea3268ea6554bbfbd9d46c19de8df7995a4b588b6beec3fd1939d63590375b56", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_issue_requests_for_quotation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-issue-requests-for-quotation:a634c5365edffdfa83f7e9e5824955cfd8542f841ccb07e751bf7c5430879697", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_issue_requests_for_quotation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_issue_requests_for_quotation_agent.py` is
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

Issue requests for quotation Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 ea3268ea6554bbfb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_requests_for_quotation_agent.py` first:

```bash
python3 dashboard_issue_requests_for_quotation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_requests_for_quotation_agent.py   # or on stdin
python3 dashboard_issue_requests_for_quotation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for quotation Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_requests_for_quotation',
    "version": '2.0.0',
    "display_name": 'Issue requests for quotation Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-issue-requests-for-quotation',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d958454cfca363d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-quotation'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-issue-requests-for-quotation', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIssueRequestsForQuotation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueRequestsForQuotation'
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
    print(DashboardIssueRequestsForQuotation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjVtbmX2Hy/WD7VVaKfcmOjhgkoQWxSCAhhKsjzQ5i3xeP//tcpMyscrvd056YD6MKV0lw7znPec56wb8+mU0dZOXT65Pqmim0MeM4DNwSMlMHWmZdVkbgnyyywH+QnaV1GVpNnZXV0/OT41Z2GeZ1mKVg+6HMnMZ2K8iEKjf2vkyLzTB1HShMa7c07TpsXWh7EgXIMavAyszSgbyshMKqalyodIvGrerqfqlostqc5EJfoCx30wrIAIgGyCqzrnLLZyjNoBVGEpBpA5UVlLquAzRZA1QHLtSGbueWLwCi25tJHrvV0+vP/3h+CsH3p9dfn+zYrMClp9UHjt0EQXlHsM7K44d+ICI2Ux+szQdA0/Q7d0sAMQGXHNeD3n/9OJn8DP33f0edWfrVT69fU+j98/Vp+qM06R1anZlVDZDaZm5aYRzWwwvExp05VICBuinTO3+A5dR/eez8JinLob9P9358KHnx3frHr0+An/KO9evTTxDg7utT2UzfXyYp+Y8/vcQZIOPHn77JqRrr5tr1JAygfnl7//0uFiz8tjT07lr/DqQ+vG25X5++M276PHBPdoKdTy+3LEx/fAjOy6x1UzO13R9/+jOxduDaURxW9X8k9+eH4MA1HWDTO/Cfnu8k/wOavRv0KfPP1ebArX/FErD8Q90z9E7Un8m+8/9PomOQCdUn4/9S3L/aMPs79POf2vbvNjxD3tenlRuDnCtNK3ZfoV/f1AO3/PkH59vFH/7xGxD9fxSjZk1p3yW8JWYaeiBJ3t5+/qG6X/7hHz//0OQg1lwzeWvK+F/J/Fe83vX8jsH3VT/+fi/Qf06jNOtS6DPSoV+z/H+Uv71AmhmHzrfr1Sv0fb5Mnxk0GfGh9EHBdzlTAazf8fjT02+gSqTAmsa+3wZZ/l//BYmhXWZV5tWQamdNDQEH12HiTuBPQVhBp/ek/kXd7wThJXF+AUXtnu6gRJhNXEOb0gxjCOTD5PHJgsyDfvmf9r2+gkr5qK/zz7r4dq+Jbx818Q2UmLfPmvjLC3QKgPKsDP0wNWNIYQ8HyPTdtJ7U3gOkapIv7aT5Xn7vUJTlbqo6VRO7f4N++c9Uvd2lvuTDZNDXFHjoUdFrN8mz0izDeIDMqWJZQ+1+AcUWVJUyi2PLtCNo+qvJXyaWLoGbvnNngybj9q7d1C4UZzaA74WgQD8D91dZDDpEPTFaRWEcQ05YArqycrh3I8D66yTsl19+sQD6r+mjJGPQowtVc7DgEzD05Uteul4c+kH9NXXtIIN++PW3H6D/Bf27XXfhk44DaBB31kBYxxCvyhIEcrRJwLKpFwFvm87dh7/+9nDHhC4FbRNkVuiF7n0zkPYtICYLHj76cBCweYLolu+afs8b1AWAFyisAVsg26vnr+kkIgNLyy6s3A8SH5sf1H94/KFn8kn1ziHwk1dmyX3tPRYnZ9pZ6bxAOw/6ZAqYC/xaTx4NsqoG4Quar+Om9tRXzfqbC9OshioQIpU3PENNBUydJP9iAdETOQkoU2b9CyQuD6DjZTH4ayLorh7sztJwcvx7yD4uAyHlDyDGFh8iXiDJBWxCuVmaeVCalXtf55mPiACd7mM/EG6CCaCDpv7uTj66B+898nb/brjY/fNg8jkQQF8bFEZw6P+/oWYyit1sFG7DnrgVxEkn5fqIwAnbRMhjoAOTxV3rPZ2+TRsfhemjZH9N4xB4rRz+9ljp3YPuseZRBpsSYFBYBfqwvXwYWIPQmWKhLKdwN7+mH73hGZAFHFdNloIMj6Z6kX0qnO5+IA0AZdPvb3MC9IjKKVtAvEN5Y8WhDXmAiHtq1EE5Jd67c0AcuVMSgkyxg99ZBQHpIEaAfAiACIEDQP+4UyeBBAKz1SMbPpeH0/SVP3ztQCDD3BfoMgU8CNoKslwwQk1rAAs/3EVBiQs4BhA/Ga4CM3+AmSbmd4Dm5IssMWv3ew+83wTBOzUhoO8zM4FU0zFrwGUHnAASr3949hPnu68A2GTKkvum37v73Vbo+yb2tyk7AcZvLQIM+VP//44cUNLLpLpXKdCZowrkf+K+BxCIhHurf3l068c48Inl9Q/HhB//2kni3n/Pv/fcKxTUdV69zuePHvnRIl/sLJmDGAlzt/rWLr/cs+3LR7Z9AbC/fGbb76Q/yHqF/hrC34l4D+1XCHmBX+DplhDa7hS77x9AyPLL4voFn+5+TRX3m6ffw2GqfqAig8T+aEIfS0An8kvXnxY/mlI19bIOtM97Lbw3lc9oeM8VUGpTf+qgVfZdDk82Tb59uO6zZoNb6dQNnGkG9N3pjBRP8Cv36TVt4vj5KTUT9z89G021GQQtYGQ6VoEEAnNVHbr3X58z1vTj90fFe2qBmuBkr1OGgT4I5uFn6HO0fYY+Dhv3M1zagNPWz9NYPakES8E/n2s/z6GW+wSOePWQT+gfJ6hpmnufsv8IYkosgPheaacO8p6pk8Y/CAFffN8t/yhEvn8x4/dyUdXm1D1B035P8grgdMDE9QwB/4HkA/kEymQDNvxRDdAzRTDo185k7jf+vpmVPWz57U5D/TiG/vr0UTam74/h4RE70xH1r415E7Ef7XlaAgiZAE7D2J3n+zD7BmwMpzb83S1/mineHgH59Aoqj/v8NLFZhmBCH+/n76cHJmDMtzEYSAA15Es1jRVzkE9AEmj2+WRIBOrfdwqmy6FzXz99ef3z2fnfFoNXk8RwmwBN1nU8z/FMGvMol3EJGsUZgrA9hyZw1KNxxLYtmHIpArE8yiZwDKYphmQoAGXyaWK+Q5kjkzeAEZ+U/19O9U8PKaCPoAQJxLgmhpK0a5IEgVuWZzmMg5M2wjgu7XgUwxAmbhE0bZGW69qY5yAMxjgkRjAwRhEWEAHkvU+UD2hvH9P7h38eleENVNQknICjpmnTNoXgDkOZpO1isIXZLoIiDoW5MMFgHk27ONj/ufXdR5MLH9ZPMQyGSTDMtJOeX999PsUliYOVW7zasY/Pcs5owBmC1Qf6bCS96+5GZ7yqXpNRrHXdDQdhf0ucoDcs17iJ/GJNL1WMvXFd2bDG2rwlp55Lb4sD3MyrxXGxuJTWiTyPN1vp1AZrUUqIaWKsBCXmYPnmJtx5EBAc7urLWsidtFTqCx0XeUSg51oSmcJVsWtNzlwPDF82JclrxyZmM1TXmUgovV3C4UZvRGqfbsyiFKJKsanI3mxdoTg6xBa1TnlSKJvI9+frYUD2tZWNRw65FkwbCmWPd2myFjo4C+xmOFtxwqyb3gyDJsCZbUbI6Smk5JQn5/K2lEeCpBsvG419N5yMYl9tLvOidvYDVmcMSZ1hQRa1E6otxvlSMlYXrbB0P0G44ExjCFNsrIZX18u12GV2WiiRvAgJUVj7ZIO5aZHwmM7tB4SXZVEqh7NK9DAbSc4SxbJ4p+/LcklqDYJKixLWRclmBEwl4+LciuPukifLmR4at/mSVo+NUalaFR2EannLF34q7YtzuUB4wSk3FxS7RQcfVRneicRl5F/1Gj2LUjwGnqztKets1pLURwlS8MPWpq6XS3WqgvHSJhfKT9fHM5lZCX4Ibns8qBebwboh5Sq5Xdp0aex1JNVkKfaA2fUMNITIuLC0x9IOXByRYLW1EWqEj2ilN1Z486SoANG7yk92dzjJgtU2jOpxZmM3iQTT23XqzHZFZQmIt14N6+vYCOLu1PT5MqjODmE4gWld1cMaC1zplJ2qRX4TZthWyzlCRnS02Dt73dTxW48ya6GPTtRmHRzQqpe5M+gUl709hONpHc2Tg65hMlo27X7cuOO4pMS5kOFnojJ2EX/pqtHE+NJs+WLT8vmSQBNLw7BgjIiRSbYko+q4yJPjOOMPOEz3dI6JC+CReSfdUo6cz/QtyR+N7ZoUxhKnWfVqeefWNE9iU0il2PHupoyVa5nk/VUiEhwN96Z47aXh6N4k36BPiVLqBcklNku0mhrjxEJIbc8nLf4sncTrPqmr9ChbDFu4t91ymQ1HXjWyiFpsqK3DBbtcrjkNU1LuYmqMfi5uh1VoyvxmmBNKsoDngj6ONxXPMYm/xqi64O3I5lK1SU5Vrwe3qDgdBmMMXJWQNG9Rc6VFpNrNCYODjKRkOR/n8CorSHp5dA5Dz3bzwiy7/qLj5GLTIUvDqK7a6STjyWBLvplKy+ui4bmGYTtPQjQpnQuymYzVMXRzTRN64YR2cZ3s9OWO7uauRkRruM0upbG5qunqqDRB1rbc1SCK2Rmr94ab1OZNo7FUYLvCvHQEbJAWkaknesdVpXXuQjVs9+ZN0AqvqzNC9GdakBNbHZGjMeYbQ7ZUfs6fDiQ/UNeaHw9UvIdRVUUVea7OotWa32l9aVKasUjR48E6ZmFmDd3qcgxw7FpkM2rYrmoxp0OXYouwUQd7FFRFORPHBG2IciN7hmTtzhIep9eGXfuHbs5rTb8/WjRMKs3pcD41e4mZuWtiEXFjtjFuKpHhN3SHIvSZ4uVrFqdK07or/CqGWImNAbplujNC7g+gzKB6le+EIzr61MLpZiKHD8R659JRIds+jEV9u72erE7LuoCudgVG7CxFLPO91yYKDpBxRLovvZ6ejbR2GQltf8vrhjhoWlwRuE9XS3K9ZpdnksVUwpmzN5hVy0XgysOJ3alRx5lwsOUQC2VqkmKCfbZofMlEsw2eKIu2lzStCUFNhkeO4/JNyNlGpHeVeqabTWXLG5ygd1qwUnPHgBdBAdOBiMgO0lFq12hjA1rzbC6f6Jnbjt0tMhfOEIW247VUzu/FpGSU3Ckr9eQfL+kpuxi+N0e74yG1mX6GLxdnfefPu3Y1p2jiKrYVqm/a+a0IkYU33wOoGkrREVIfux2+ONXqMZItnuo6v1moQm4PZley2LbzLl0jX4NuKWTriz2/2tjiekvIa5IPZuSeGTs4q2dpj61xNe5cLsOp5dKFV5Si1lpykvRF7qGwFktLBtbaVXA5ztVonHdob2RVHNu3XC1SG+XszGbs3eImU9Io6kjFnc/nKFs2ByKTR5zWcwv1TnkYy9bQX1pkVOGCmVO+L3IgYg66mITZ9uDebhJ+2mCbulx2ojqc0Uaeu4eRQ1XtyrQ8Oi5RxbmV+oHbOsN6czZjUHblLbXVOezqubtof9LIGe+IgXkUU1OJnOg21S8TH5zSS4aVv6WjC2x0+3Vx2Sxuq1RbSUebX4hOdCKPKHNSVsgqbVbMIRfO3No2nCPj7DaCAiv8brfazcxm3mzb1Xm92+ljrcioGrO7o8EtqstG3XbnlSGrNX5GjVLo6L5Eluo+TtikJKsE6QrJr2yDNlzDX05ljJLBWIQVvXbU6s5YZijN81Wpugl2uISFyyKV1ZzN+bEmNv3cSPhq4x0xGGVNLndr77xuqMuZQFYSf2YugxGdPL8gZMXdYQ55UJackDoFuj7Tc9PtBw6wGTsiOsvOdspsjhGWqGFRR6MtLZYZKzGZvywMpLgJ1kZNlzK58MRLpO97g4vC7kqqxC687oGczY3JOW/AE7ieAyCiSK9KUge+HDD4MCvIsd7uFudZzXJS5zput2rzo4EIJ22tLbATQZA7pz0hFKF2srDfJreFfXRI3mAueOqjcnLhKXQjS0hIOo6+rxnZQq1LiKcnVW8tKtXF1QIer/7RprYx1tDsLiy4ZcBipls37GbY2Cu5OsRFJQ7IisHj7UBXurG3NO5KEguS3WXBmQQHBX04sO7VgAPhshcvawXRCX8vO6PdAoe5zOoa35RmtmYvCC1ogqTVSoovtt2G3WHjZR77LJ74SYoyZnSMhxOzi7Rmq5w4V73qpJ/UHS9HrGwtq3g3P97UneGhEebfCg3tLZUzPYY3GlaPxuESHzB5UzkS3yt1IxzgdauSmYPAyp5MnEz3+bEi6P7q16eNEJ6DncF3zeKKbHiu05FEP+JVnfGhCtfsMZFE4Rr2GUevLi6Ha3ZJ5nGH7iMkP9Fp0Z+yPrfkMVb2jG3sxZTX6Io3AsEj1dCjDjnMk2GlXIL1sKWUERdbASm59bgxrQ1TzfKK1xZ7iujrswyTx3lIDgmOJLDjCLkRtlwoYXyKF4l3YajzmsKXw4WtSZLPynjX769nv5c3XjBb+J3Su5VzPqxZCzRGFeEN6XZNUF8XUXvnsIxBYZvxoMb0mCnh3EeoIs17Wd6vFdg7c2grbYY8UNg4y9B06bFk0bHHnajA6a7jLip25nUpzq9wFp92t8N+E6/KQ2FmtX6dlyNDJ13BXW8OaJ6KfSX5fmXsV1qHmgCshyZRcRHlGXfaubOmjuCFx4XN3B698Hz1rfzQ364nSoV5Z4x0u15uV3lvqt1xF5xwrSBO+9smZQclEBvLxAQsFI3ZsU/H4XDUDBYjHOqi1KrjUmgSs7wfpME4nlsyD5l6ZffUmfcw+2g1NxBAnXNF99qYBrTobmfxZe9rmCPyTUggkrhCs7mqpQsu87OqltOkQIxzxnaKEcw2bHfd5DuW1neit8xKSfMv+421HjI70bP60Br9osCbgl1oWxgu6T22W/nUrDWdxYmNd0i/E+ydfuls95DBar10Q1pQ2oQLbj1Wq8tBDzaK5msDZm164Gf9FKAOfco92m0kRtGQBRNfh3DPBUOgt2p86/WRjZfHmzgrtkXfnjLqwkuUZAWeR3utlnK0G9d1W6M5Jm+HUjnPUQV2dZ5ChLnfOJ2td8SZYlB1FVhoj58KITzyualfG5HJ+32OwDEI2ow88HN/wLfr+NRQjY12pN2T5Nos7WSOtJmyGSMzIvvDcmOGGGMNPNmxko8GnG5YK1zEIzl24BPrJ/SW0dsCY1tmRuxJs2RT0nMuQSdamIJ2lcXwwwypL5c2yE4StZ/NSH/TgVHPx8FJB15jDdXpGU0XI10jzLzT5seS3ZU3b04G85s1oG3r2DOkRKmjaMSuF8jr9igUmRqRYdvbzHJQhGVrtZza9Nbeg1dIBF+Xnj6Xw91lYGFwXKcXt9NtWA2J1FmKbfczSyTlmjD43GkIfTz015UNBovGWSl4w0pXk16PsqQ6QLd7pvFQVNNEiULD8BQ9liVrwKN2QSyZhq2d44HETOHWin4hCFu8pYIV7tSxow/r+XW+Q1VU2vkENzvmzmw45A3bOSs+LsVgZobmlQZpbWxnhHmbX3QjPMxqj+n6a0wpiHdWBFZSDJam5ipObmtwIHVnRmgtSgSttjfuYndSuTcSqzRn87i3CAWzRp8NmRZZNXJCxdS29ASe8ZPMZ+eO2abwlWe6kNS5i4zJ/BrhSmzNLHeXjLIrr9+QytHHRdHbR5jdN4PmEq6+Dy8OHrGkWBNjOOzcpWGhrNQaBkWzeKjDChGOfd0cKnbmLvzyIurBqqX3O3fuKPSsSdOUdnpqRRy35zDOrZY51eFl0V8dbnMtbC461iDeLqvxeD1x4tqs5wdyvXSURuVu87l4K3lyQS3bZI1Zl/HgEE7VXfDRmrlVjIJZvlSuzE4ePKsZFHwBB+3KJJTtLLed8ID022Y0CUyLMCoQ9WM+3Eia4zwagHXlRXW9yt6WCUUkxG8cSdVzD8USwXWLgQLT4QBfVsbZsf26q8mDJzdDjuRN21C6WpsbuXS0OMIb0LSYrdUdeX8L2mRDsrbELElKHrnQP+z6eZzydOFrdtrRbuSGFN8W6ZoI3JVQO2WwPuxUi3BX2/ZyodpOvtZ0S5b42OiK49KWtPCEWzqDm20SefC2MmcetdEvZTWPhTW2l9SZ1YTJSBG27TngXIDeqlmLkcKcHs5XOj7YDLaxdLiixw03Uxz8mIfsldbOBiyhwqzvs22GZp6oFSRRUPC+DWdGSl8T31yq521BzoTtdkZrykopcZe6wXs9UXVw8qFNq/fwrFvD7DmjdWUfFGnnwbJwurGo38lRdlzPio28lQ/HsRrWbl7veDfAWnOMKYNaH8DwxnY7FV3AB+I8OxEYu/Vxb9ufdCRTsOHUiluWFeqIB/yyl0SULU7TiBMF14WSHpOrOAz2cjuk1448r3kLPdcLmhlWtGMo4HAm07A8O1R6elzqvQWr2HKWEpFU2U1E6s24AoE/WyIlOPC0xPLsrOzl0KrRXpcSwSjNcpZzm2xeRUKie4dRH1jZQwZ8FbPSGJvOwVyCps07A8dRB+W0a0NhFaYCf1jLFTXr5W1xACfAmywrcMPYtxjBttmcZqOlXXBllbMs+/en56f7G+GnVwQmaez5aXpN8P6w/68/JvbHMH97l4dROPz89P/uyeXjKeLHK8H7o3/XdF7v2l//KtR/PD+VdghgPR4vV3Hjvz+y/KfntF/+syfIk4zh8Yp7eovZ1x/vTWrTvz/mDlOnqepyeKuyuHnfYTXV9L+7VG/vLxye7gYm+f3txYfab89V6+wtNyeW7y+ZE9cJzdp9/+mXHzCcAXgvtKs3jCTe3DKfTH1/OTU9zZ3eTj399r8BdUJOiOAnAAA= -->
