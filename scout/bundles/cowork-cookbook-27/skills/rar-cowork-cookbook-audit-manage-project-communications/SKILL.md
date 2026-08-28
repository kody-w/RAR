---
name: "rar-cowork-cookbook-audit-manage-project-communications"
description: "Audits manage project communications records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_project_communications", "rar_sha256": "53f3ac6c0b1eb0ec19d1edf7eb0702545749465b13296d31e5755dd430bd74a3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_project_communications`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_project_communications_agent.py` and in the RCI capsule.

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

Manage project communications Completeness Audit — Audits manage project communications records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-project-communications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 53f3ac6c0b1eb0ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_project_communications_agent.py` first:

```bash
python3 audit_manage_project_communications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_project_communications_agent.py   # or on stdin
python3 audit_manage_project_communications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project communications Completeness Audit — Audits manage project communications records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-project-communications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_project_communications',
    "version": '2.0.1',
    "display_name": 'Manage project communications Completeness Audit',
    "description": 'Audits manage project communications records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-project-communications',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-project-communications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5e75fd737b5b78d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-communications'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-manage-project-communications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditManageProjectCommunications(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageProjectCommunications'
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
    print(AuditManageProjectCommunications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abOb2JblX1Hd+mBnyb7MIPlFRjQgCSQxSYhJ6QwnM4hRDGLIzv/eB0m+tutlvnrZ0dHycAUc9l57WnsfuL+/2G0TFdXLpxfVt/MZZ6dpHPnVzM69GVt0RZWAH0XigH8zt8ibKnbapqjqlw8vnl+7VVw2cZGD2+nWi5t6ltm5HfqzsiouvtuAW7KszWPXnlbVs8p3i8qrZ0FRTZfK1G/83K/ru7qySGN3eJyP7dz1Z3Zox3ndzKo29T86du17Mzfy3aR+Ber93p4E1C+ffvn1w0sMvr98+v3FTe26/gpHvINRHljYH6AAAamdh2BlOQAH5OC49CuAKwOnPD+YPY/e134afJj9138lnV2F9U+fPuez5+fzy/Tn2OazJvJnTWHXzQTQLm0nTuNmeJ3RaWcPk9VNWwHr7VkN/JeHr487v0kqytnP07X3DyWvod+8//xSAAh3sJ9ffpoBh31+qdrp++skpXz/02tadH71/qdvcurWuXsdCAOoX788j59iwcJvS+PgrvVnIPURR8f//PKdcdPngXuyE9z58nop4vz9QzAI783Ppxi9/+mvxN4jlcZ182/J/eUhOPJtD9j0BP7Th7uTf53Nnwa9yfxrtSUI69+xBCz/qu7D7Omov5J99/9/E53GIIHfPP6n4v7shvnPs1/+0rZ/dcOHWfD5ZeWn8Q1kh5P6n2a/f1GVNfvLO+/byXe//gFE/49i1KKt3LuEL6Bu48Cvmy9ffnlX30+/+/WXd20Jcs23sy9tlf6ZzD/z613PDx58rnr/471Av5YnedHls7dMn/1elP9R/fE60+009r6drz/Nvq+X6TOfTUZ8VfpwwXc1UwOs3/nxp5c/AEcALqla91H/n17+8z9nYuxWRV0EzUx1i3YimryJM38Cf4riegb+TrVd+cCvdQwc+1z3pLcJcRHMfvtf7p0pP7pPpoTsiX2+PLjwy3Pxlx+58LfX2QmILqo4jHM7nR1pRfk8rc+bSW1Z+bVf3QChOEPjfwRU9HH6Movz2W//hvQvd0Gv5fDbnVrjB0cd2e3ETzWg09fJRiPy86dFLiB/v/fdFuhICxcACmJArh+A7XWR3gC/Tf6okzhNZ14MeBw0geEuG/js0yTst99+AxQdfc4fhIrNHt2hhsCCNzizjx+BZUEah1HzOffdqJi9+/2Pd7P/PftXd92FTzoUQO7PiACEO1WWZqDC2gwsA8EC4QX0cY/I7388/QvE5KCdgfjFQew/bgYZmvjeV2erPP0RJciZ4wMnAwdnZVE1gKVncfM62wazN7xA6XRp4vGoAF3J80s/9/wc9KwmsoE5b57Mi2ZWg0DUwfBh1tb+XetvTnXvZn4GSt1ufpuJrAK6RpGC/yaY90Xg5mIKYvqWCo/zQEj1rp4xX0W8zqQpJ2elXdllVNlPHYH9iAvoFl9vB8LtWe53n/OpRfqTq+4p8nAPWAQ84z5D+nGK+b1ng8DWX3Xf19hTbzvde1z1Oa+fyW9X/r2nAyjDLGxjb2oJ/3imVB0Vberd/QeQTpKeUfCeUbnnoPgvBwb2+yHh3tNnn1sURvDZ/995Y0JKc9xxzdGn9Wq2lk5H6+HBaSiaPP2Yo0Dbvyu7V8u3UeArkXzl0895GoN0qIZ/PFbe/f5c8+CotgLKj/TxLh+gAh6c5N5zcsqxqpqy2f6cfyXuDyDMd5YCYQEFDBJ8yquvCqerX5FGoEqn429N/OmnySsg72Zl6wDPzALf9xzbTQCqaqqrp+NBgvpTjXVR7EY/WDUD0kEeAPkzAGKKDiD3u+ukApgJSiqoiuzb8ngKEEDhtS5AC6ZO/3VmgNKY0qMG9Qjmm2kN8MK7u6hZ5gMfA4hvHq4ju3yAmQbVJ0B74uvY7773//PSt1S+I5nAA5m2ZzfAk93Erp7fP+L6hvIZKSA0m7LjftOPwX5aOvu+v/zjc35H+EbooKbTqTV/55oZqKXskYsTJdWAVjL/mT4gD+5d+PXRSB+d+g3Lp3+azd//vfH93hq1H+P2aRY1TVl/gqBHO/vazV5BhUAgQ+LSrx+d7eOj6j4+q+7jj1X3g+iHpz7N/h68H0Q8s/rTDHmFX+HpkhC7/pS2zw/wBvuRsT7i09XP+dH/FmagvsgArMn7A2ilb+3l6xLQY8LKD6fFj3ZTT12qA43xzq8gEJ/zt1R4lgmg7zycemNdfFe+9z4LAvuI21sbAJfyBuj2ptks9KedSzrBr/2XT3mbph9ecjvz/70dy8T2IF+BP6atDvA+mHaa2L8fAbvAhdievv+4M5PvX+z0kdd1A4Da1Z0dnnXypL0P06ibA2aZthVTS3vQP9gM2W3aTMCboZyQPnYx00T1Nm79s9Z7IQMdXvFpqucPs2k0/jB7m3I/zL7uO+6bubwFG69fpgl7shMsBT/e1r5tNh3/5dc/gfEcuP8CRDxxycQ+D3N97xtR3ANX2g3gQ+0oAEiFex8mpgZaD/dG+89mA4WVf21Bx/QmyN988A1a8cDzx92U5rGr/P3lK9U8g/ecIMFyUNMf66lnQiDFgUJw/EhGcO3/ZrZ8igDsCAYbIIPAAsx2SRd2EN+BfRdZeojvBRQ4oGCUwAkKX+Ik4SAYuiQ9DPEJiiA8D8dgx6NwGwPyHll91xNPsHw48LElgroeRqIEgS8RCrWXno1Ttu3BiwUFU4EHGsi3WxNArk9bH7ZNjnwbcyefPE3+/cUhcbCSx+st/fiw0FK3SZxy+sicV6RviZd5clJPe9W/4onQbJCyleyBQS+CedpK4Xbc0a7qy6nKX7lm37WbOloRdD7uFEw2+fh0E2ynSWhpR1i4iAZyLjbY7SJpa1q9lOOY24vNXnc6VXUN1araxiXyTo1s4twGm6bu1ztzH0mnttKQrMcwaDmalOrwt9yIDfVwNezqUG4OJOzmV78WVvszJSPjEEhrUaAysXF1DdOy84U3t5m5O8YnU44GaYxw6Fb1eKA4Ax416MIfU0JbRD6VHI1dv7JqHTcNeL+z2yUKmEAVYdW87azz7SBiQylWSePtXQ4r4JGLr7flYWz63UmJSpRhc11Fupo0z4THKZuDOhSxrruxj297d6+mXRStZQHxWB1ROPTYRpJIiXW8J/r2erUF+6LZUB61tRRY/hIrLi4vgUmU7YbuJpJRyltqEcJEnSDedr9GmHAhYAITR6bjGOpAnlH+4Ah2gnYc44ZVr5L8cMZ1eTOfn+NGd6TbLmkGFvJEMjzjTqGdtkHTd/WlWGyKtkaltcvzy5oRuCbksJNmSNbN51LEPh4Q2EJWYH9SShHiaJSCYCyKRwYqqtfDGK04DaF6+ICjI6L0yO3awy5JMOEe29BNdvLmBJUP4rYw3KPFoy53gA/Die1rBzPc86UVDIQh2zXaVPSAHueVl2UoXZhCwFCa3aw7zhZvJzrgYM1QaWaEFTlut1TPE+1iverzC8VtIsUQe3mtuZWvujqsq+WSJsLl8jRgVnkt97fzRVlTYuf6DUuIW3ehMkLh++4667MFessW2c0YyXl75tqECWqccArVpA83VA6iW0D7x4o8xTa99cxlGAfKuSCWWbBwQnKzh8faNPqjZSeeiQkSPuZqdNbzqi3h4+Kmn+PTWbzgg+ileb0WC7vfn9IQoVVaxb2kg2QE3kh4Wcqpx4xDiWkmthvzo6vB0W27N0hXxZtzZ3WMxsHGcVwsCusa1OdE5dnV4XB22xVzqDVh0Z41w5fXnXeSCWqs3FUx525VVubYJdD5swIfZXO5Dsy5mB/6XD0KI2OMRGvOfTVFsoCBCOWEGz5TE11aWVTAQZGxv0U0jKM36HKoyVsFRbYFmToHNHZQTqmMdz65V7lEOxdBrqqfnUpGgVQRG9000pd4Y9lEyfcHxDz0O32555W9d97smd0I3VLHjWEKq4Wl6CmnVIfcS+FWPZwlaw1PkSI4w2VN2sdWMSXVK+KhKEch8yJQkzm5WpNIcS1U+XgjuYtwbKD0sLPSwS046LCY78rY6chxqA/ZUWazoN77EqFFZ2GO1xGXrqv0AFnb5LDZF1rCUUGSjlSOFElYlHhxbLaHmkDYZrzWiEutWIdzPFba+ef0mJtiUu9kXUx1xCxgEAV+p2K2cbgUYnpV+HlpXzZNPx8X6t4xNAHRuAiSF33Ss7vuIqKtDrsHihZUapDqHE6zZZlrQbgveYRaQigO0ZQtUt56taJ5BtOS87baoxuFtgJOdc9ubChzVdpglrEarM1F6W/W3rUOvpHAzhjurfa0yFcYGRvrU7JAdsm52vpBlZyNqEhUSC6LlRJfRkfomXG7XmzCaLk+GuhxryzWZyW6OotTN2RbepUkUXy6IGBacbYNrDlJTSrcgpbRdE2pR86u95ibQHXfXD3DZOnNVqPHRhLXm31PXMcOoy6X22isEYHvs+5MVkcEH90lFZQYbxx5hbTHkSJI1xx7ytXWcXfG94LJG5CzyFPjqEGAGTfLesVqQRyH+HIJKSu9L0KvaXqHWcT7taDO5wID6SaJizW/CDC805fqZohazVvRlZ4TzWUb0ZbK8mqmFy6KKZLMhpt9q1/2pditXDxidBGnWDIU2zC1hGXYaRtVcdp4nx+vR+KIDLvN7gBXGh9yRwY/hlGdnPtOSXcbzU965GAEMqL17jKeU+JwWeSbBZoPB5/MtzEgEDAJ5IS0x9NsWy4KPbzJscZdPIPS2pPEwb192eOEZHKrAwzPY0YM2YN0nadVZuhws2t6OnF1lOLKHdeJ3eKU9Yx3WxObs4WBJtagYmvzbF8NnY8f1cTeyrp9DhOXwPw5gw4tfthq2Q1Z5tSZ7aKz0a+6Er/CRbw2yts5vi6uPJUFnLRVhFRlLtmI1AaZ4RkzbLcV+JrAl63e1ciYegckWCdnMTypc1jUEOOy6zqi7w7bdiOYOd4OSk1Lfu+TjKta5ZKVtpS7M+nVVuLq2K1xzPCdXbdg+JbZp6f9ShmH48HENsbY2i7q3rSYPoi8tjT2rbfswVQ1oPg6OjoynWTBTvaEoNkZClMclrmoB4UiXjyqHrgM3kBKIGdbk9/1jRn2KclJF1SXBN3SDyPqYCqyj/Zpe0SlY8SSIldLl0t1xey1d+Io4ZCa9foEk8XgXkKfvu4hS4OMdQavN3OjYySBOLIOuk4MzYfZ3pLAlBL39m4bRswG1lTBoTUeULnCzcO57QcqTxQqHA4HF6pyV1gxkCSjTj9IjsJoTMDyBpef3BAnVaNRzbMfNuKOJEUfsCgCn5w5kxxVSakPHpgcPAu/hCRvUDBMCNx83i/lW7VtMMXLlUvvXq4lsHiFlX5U4qZ4EOylPSx5g113Os104blpjSxqjowR3da8itfrAVmhXcrD+C3fyIGGWCRF46euRTXSFRtz8KzainhozafyNdtmSVLXUoN6yq3iN7IRxEKwD6h4KZKpgKxEiuF7Ddl4J1SnHNAHtepscyy1FuzhOLipeo0HLbNx6EgrgH53aHhkGetKto3JuYyijWUBc/pV3HtcSETtKQmX9tqX2uvWx4QIPx6i8HpLzl0xt1ceLaasXqwkKJa4y1KS5tRZWkYeJsGWSui4mNsuc3HQhJZp1UNNOI0JTh39Ob+cI8vjzZE3YcVuBD7PVgZgxx2dxXOcUMlNhl2ZZBASjF9fIcVvFjtvKdfOeiwc/6yoiJfpl+vFGXf7jJR14sQ2/ZhIuplv8g2B3eLTidvbnCSCGWZv0DaFI6UmUtvRu/qkfBtdb1sva6tmIN+96u25HJDRaIdzPbTaltvWHlZGLR+6WTlwrrzvb5LHIKdR3ZfEldjCCXo865Ax+rg/rA5nnfZzahsIFGlpFWQYSciXpRJ0xMVOtEIpQhmhOXR3shbpvAyZa2vZ8+XtUCy2bTZnBQIu9FMDYT6Hoo6OiidqYwDeDHbWMmpwlMJzJq11YZMzayYr1ipznHODbW82hEZtVxabjB66wueJgiL1zbqq2oE3Wzc80afIYbckM1DlroTEA3+hME0rdXer7liv5FfH7aE87UK40bcSSzptkoCSFOcaeegYuTPq0jCYxUVFTqZxzD1aV73dDmHhq8ahcbbmr31VazULa5IJpoKA3ohratMbVDyH0Da27fYKHaLVdbCkWxRSG36dKAm3w6hVvSzYtMJU19UkHpHPKEOT5WIb6XCkXzqzvxULlmEQvIlTVFv3jjhwvLu3D4opFCFXsWav7SH4AnOa1cmZdXCzzc04iuk+rtj0Gqt5bHpYU65zvTR134kNedPptkKOMd2aDrdv4LBHx96dRydkcWG9ijN2Ma1t0qHcWqZnEqbBSQPGlisYK3gK9L40Qu2zHu0IPltR9LEzUNXhYsaULQGUd5anbO8hhpUrhDXM1TxtYt+jLulZRnUBTEDdiSndJXSw+EQlk5QNmBpeuso1SwuqMWTkVsqODxnLgKcQplWw1OwdrFx0EiRI7j6HfJ5B9Aqj2vlVoUK3anuvDGHDq22O7MZi28Qa1aB7SZa0RM7s+kS3q6vNi8iqWZ8H/XY8XQ9BILWCMgb9Za/oXKeI+9DVJeySIc2CwZ3SNVgz2oix41wgGEboOqaM7LRmydW5R4zbtrsihG/jcj5PIGY8LwJ76y57z8yqluyL1cqWwxraoxf/YMODm1vqknGkFVpAfULsrmuwN6Q2JsTML/sakakKWpjBKurwcsyvAYWsaNKl6jUrghZbXzXfYTi8vXLrcLEUYK3gm7nY5akIJ5xwEDZXTyGPptfToN2YMJuoQYLFNM66WUD4atJ0I2FtrHaVDqKachW2JWUmXFKy4B55blWPrQZTQ5R3O5C/g5yMbIXbCNlxsHKsOqu4USNy0nKyQVmcGqou7sZQQOdH2nDOju4CflNGIWku6na9zql9RZz4Cu3gOmjTsD3GdkzaXl4J3BH3jQJCUrO4ga4D1aImdALG+qzarTTjoIgQjMpMbo81dQO8HpbzObJdOHtypa1Qt0zOrVQRczMtdL5R5AW7QyFNtkgPPc0VzNdGhxHX5XUxXPuASXKMq1KLsUYXT8y1KumS3PMCfGlNJQjEPa0FGcfng5QdsON275l0csF37ZEK87zfGizuXmnpdiaIBaOp8iXNKnPd4sTI7noeFMzVXxNabyUk5GRzDwx3wmLbNcy8aMVDaG8VLmeIcRN1R+SyQrxBt2SJieRDpxfYAivMvufy7VmCFld5fSuMWl1wlbT0XA/T0XHnRLucINWTlZ+zetOjIbUjbphCZ4jKLuTitFYC+2wmVnWV5yeDIMnF2esTeStiyZjJLMltB2+17RBPZnmRFJgu1TvshrvdZrgIzFVpdNfQWNwSdi2MmdlYSHK3RPT25En+DrIb0B4LF0szXI6vm/lFwnfrbtnRmikJt+38svT5Jj7Sq9SCwj3vgQ2QuRvEvFSKaLDJMFuq+drFZKILsYi2heDWY6suRM0l31t1lpneEjlj1U0EYzO7mgsrZUW4snSAwBaKIVboqUWVK9SO60akkOsuJDITEsAIYPBRaaLQkVp03pyO1hKBLaTmHGNLrFB6jk/5bLsruo105Xa1IN+C6kJKR88KrRVwqoQPGYcGkDQeJGYns4hkbk7jYrnfXjS+cQxXDFpDnA+8jiKGoxxMm6Uu5MmAt3UxJKIPy/whDeehgobl4Rwdu+U+YkpCnJtVNdjGrVlidekjcqCKZtxtooU1tsRyTK9H0+p87lTM93Z2o+e+659pdMXodMRviIJ1MUBYcRFcBTeSDiLpIoeMCyILDaxMUasSVENKbvIWX8UVvgPb+0rbQC3u7RdM6tvueo7IdQ9GP0e4yikIcUONTpic5z1ybrvssL3cUuTUXtQjO1B7t4D2R/YaQIxYtsh4O0bhqXJdmaYOp5A0KgcN+/VF3RwKRobgBRuQ8WFRLOJyPI37xWLXzpfYJdkFmgXCi9nYqjhDh1Y7gYaPqQlN0z///PLhZXp2+nx0/XdeSE8PBP+fPZd8PEL8+hrr/gDZt71Pd12f/haqXz+8VG4MMD2ewNZpGz4fVv63568f/403IJOA4fGmd3rn1jdfH/U3djj9vtJLnHtt3VTDl7pI2/tD4A8vTltPvzlRT1Bd8PPlblpWTk+/7zofJ+5WNMW0Krifi/PpNZLvxXbjPw/D5wPpDy/eAEIE9jtfMJL44lflZOfzfQowD32FX5GXP/4P8e6AXAUmAAA= -->
