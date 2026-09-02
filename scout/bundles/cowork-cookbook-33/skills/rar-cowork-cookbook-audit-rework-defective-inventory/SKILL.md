---
name: "rar-cowork-cookbook-audit-rework-defective-inventory"
description: "Audits rework defective inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rework_defective_inventory", "rar_sha256": "47e6880ec4b802c8e1b89b1fb8d13f901bd8cf0863474bdcf37326fa75ac5f7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_rework_defective_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-rework-defective-inventory:104d15a826e6299965b0b19c4015d27a1e354298b1992a9dccebda824b7ffdee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_rework_defective_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_rework_defective_inventory_agent.py` is
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

Rework defective inventory Completeness Audit — Audits rework defective inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-rework-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 47e6880ec4b802c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rework_defective_inventory_agent.py` first:

```bash
python3 audit_rework_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_rework_defective_inventory_agent.py   # or on stdin
python3 audit_rework_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rework defective inventory Completeness Audit — Audits rework defective inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-rework-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_rework_defective_inventory',
    "version": '2.0.0',
    "display_name": 'Rework defective inventory Completeness Audit',
    "description": 'Audits rework defective inventory records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-rework-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-rework-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44ba930729715ef3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/rework-defective-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-rework-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditReworkDefectiveInventory(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReworkDefectiveInventory'
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
    print(AuditReworkDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716Z3Pj1rblX+HofbD9qBaRg27dqkFiABEIggQJuF0ycg5EIAh4/N/ngJTU7XftG6qmhl0tkcQ5O++11wH025PdtVFZP70+6b5dzFZ2lsWRX8/swptxZV/WKfhVpg74P3PLoq1jp2vLunl6fvL8xq3jqo3LAmxnOi9um1nt3/d4fuC7bXz1Z3Fx9QuwYwCX3LL2mllQ1kBUXmV+6xd+09x1VWUWu8Pj+9guXH9mh3ZcNO2s7jL/i2M3vjdzI99Nmxeg27/Zk4Dm6fXnX56fYvD+6fW3Jzezm+bDlv3dEv7DkM2HHWB3ZhchWFYNwPUCfK78GhiVg6+A3bP3Tz82fhY8z/77v9PersPmp9evxez99fVp+rfvilkb+bO2tJt2ss6ubCfO4nZ4mTFZbw9TNNquLoCHswZErghfHju/SSqr2d+naz8+lLyEfvvj16cSmGBPcf369NMMROvrU91N718mKdWPP71kZe/XP/70TU7TOQnwcxIGrH55e//8LhYs/LY0Du5a/w6kPjLo+F+fvnNuej3snvwEO59ekjIufnwIruoSxHFK0I8//ZXYe5qyuGn/Lbk/PwRHvu0Bn94N/+n5HuRfZvN3hz5l/rXaCqT1P/EELP9Q9zx7D9Rfyb7H/3+IzmJQvZ8R/1Nxf7Zh/vfZz3/p2z/b8DwLvj7xfgaKubadzH+d/fam7wTu5x+8b1/+8MvvQPS/FKOXXe3eJbzldhEHftO+vf38Q3P/+odffv6hq0Ct+Xb+1tXZn8n8s7je9fwhgu+rfvzjXqD/WKRF2Rezz0qf/VZW/6v+/WVm2Fnsffu+eZ193y/Taz6bnPhQ+gjBdz3TAFu/i+NPT78DgABAUnfu/TLo8v/6r5kcu3XZlEE7092ym1CmaOPcn4w/RHEzO7w39a/6diNJL7n36wx8O7U7gAi7y9rZqrbjbAb6Ycr45EEZzH793+4dM7+475i5sCcoenug4tsnKr59ouKvL7NDBNSWdRzGhZ3N9sxuB7APXJ0UPhCvy79cJ53AnviBOXtuM+FNA7Dxb7Nf/5WSt7u8l2qYnPhagKwAaAXCWj+vytqu42yY2RNKOUPrfwHYCpCkLrPMsd10Nv3oqpcpMqfIL97j5YJh4d98t2v9WVa6wPAgBnj8DFLelBnA/XaKYpPGWTbzYgD99xEwIT2I9Osk7NdffwWoHn0tHjCMzh7TpFmABZ8Gz758qWo/yOIwar8WvhuVsx9++/2H2f+Z/bNdd+GTjh2YB/d4gVLOZqKuKjPQl10OljWzqSgA6Nzz9tvvj0RM1hVg/IFuioPYv28G0r4VweTBIzsfqQE+Tyb69bumP8Zt1kcgLrO4BdECHd48fy0mESVYWvdx438E8bH5EfqPXD/0TDlp3mMI8hTUZX5fe6+/KZnTVH2ZbYLZZ6SAuyCv7ZTRqAQj1PMrv/D8AgzYNrLbbyksynbWgK5pguF51jXA1Unyr059H71+DqDJbn+dydwOTLkyAz+mAN3Vg91lEU+Jfy/Wx9dASP0DqDH2Q8TLTPFBNGeVXdtVVIM5fl8X2I+KANPtYz8Qbs8Kv59N49yfcnTv53vl7f+aVnDfU4n75J997RAIxmb/HynJZCOzWu2FFXMQ+JmgHPbmo6Am0jT59+BZgBzcld274xth+MCWD9T9WmQxSEI9/O2xMrjX0GPNA8m6GijfM/u7/Kmb67vcuAWVMKW2rqfqtb8WH/D+DIIL8tBMSAUaNp3av/xUOF39sDQCXTl9/jbq3+M0RQWU76zqHBCZWeD73r3S26ie+ug96qAs/KmnQOG70R+8mgHpIOhA/gwYMaUGjIB76BTQD4AePYr7c3k85Q5Y4XUusBY0jP8yO031C2qwmTk+YEHTGhCFH+6iZrkPYgxM/IxwE9nVw5ipAt4NtIHUawzq7Lv4v18ClThNEaDts82ATNuzWxDJfqocz7898vpp5XumgNB8qo77pj8m+93T2fdT6G9TqwELvyE9YN7TAP8uNACf6/xRi2C0pg1o5tx/Lx9QB/dZ/fIYt495/mnL6z9w9x//M3p/H6DHP+btdRa1bdW8LhaPIfcx415AhyxAhcSV3zzm3ZdHy335bLkvny33B7mPML3O/jPb/iDivaRfZ/AL9AJNl6TY9aeafX+BUHBfWPMLNl2dgORbjoH6MgcYM4V+ADj7OUs+loCBEtZ+OC1+zJZmGkk9mIJ3SLvPhs86eO8RgJhFOA3Cpvyudyefpqw+kvYJveBSMYG6N9G30J9ONtlkfuM/vRZdlj0/FXbu/xsnmgldQaWCYEznINAzgA21sX//BJwCF2J7ev/HM5t6f2Nnj4puWmClXd9x4b1D3gHveaLCBcCU6dgxjZDieyY0Wd0O1WTm45QzMa5POvaPWu8tDHR45evUyWB8Aur8PPtkwc+zj3PJ/aRXdOBg9vPEwCc/wVLw63Pt5zHU8Z9++RMz3gn5XxgRTygy4c7DXd/7BhH3rFV2C5DwuJeASaV7pw3TwGqG+2D7R7eBwtq/dGBUe5PJ32LwzbTyYc/vd1fax6nzt6cPkJneP3jDo97Ahn+b201h+ZjJb5Nge9p+Z2D3KN1z9WaDsphm73eXwolIvD3K9+kVIJT//AQ2TyWTxeP9jP30sAa48Y3vAgkAa740E5dYgO4DksCEryYXUoCT3ymYvo69+/rpzeufk+R/AhqvMIR5MG5TCOETCE3TBO5ADky7GATjHkLasI/iGEJT4DsasWnPdX3HA8sxhwwCz/eBEQ2omdx+N2IBTxkA5n+G+T8m7k+P/WDCIDgBBGCkT1AU5LuYQ0GIS/mwQ9EOHDiUB6MBDcGOR7kBRBEoRmKO5wYoiSJEYJO47eIBaU/y3qnjw6i3D5r+kZMHdrwBtM3jyWTEtl3KJWHMo0mbcH0UclDXhxHYI1Efwmk0oCgfA/s/t77nZUrbw++pYgFrBJztOun57T3PUxUSGFi5xpoN83hxC9qwCYx0lMiZk0QQXpJFY58gXLeak3c2T8WRyBGNbVfpqEvmpSqNje4c5ETvy+oWCCrbRTzNFKS4a7xzoY8ykiNd3zYpbyM6iwHQa9FrKuPcRtpXXmgQ1SUz45Ou19j+oFrX/RIz7Gahxghixcc61fIWMS7+YNaLxby60pWYETS0ydJ0m+UXaHuztp0gEkXN9UPuj61LFeOe5+Z4Ip2XhgKLuXmDBzEbjmYKj6WbuIS/k3LKX0sI1W1uHZog1HVbpBLqctyobpxlfN1iSGRJBprfDMfe55xO4xKvEFFOGWLrZ3V1CBFYyE3qbCyqldeJW4tayn15JC6nfF0MpCJtbtiFO52FIa7Sw9BsjLTcFqsVhDuZyxmwsjp510jZDsMyO4mKZ573Z8VLDhfau/VXe32t9CrcoEppD+owMMmOuEUrU28iqAoLmGZEIRMT0hk3rN6eHMnfD7aFrkNHlHkrlYeIkeIMUY8jUss8TiWGczlJzqFyUtkfAjgsIJQJM+3qJFG1M1wKjtP9kczLXZJgUNhGpx4svvDbBr1Kup0qrahohOgQB9M7wepIe33bbYw2ES6pjGm3TPEpb6VisWY4BBSs5ohrD2yvk8sQvuoeQZHr7VLanA4cESTakF8FGPESbNe0GC/5CJ1zxnHZOL5YyPV4dpbLa1SGxlxCLganxHKzD3KT2G2Ydnnli8pfKu5tkauHJSYVJJMjqcT56SF2tQ4/yRdiz+5KQS4WpY/UrJIZBtEYVFHFy9hozpsoyGPGs7gELbIlNObwMIp1lh/OInwzSkny4jUAaQOTRbT3iTVNieRqB3JUShy0QNiVixfnBQXN+4EPN/WpoWMC2YnbtClQScHGQo8so6i7CtpTV8OKD5acYAPjZUUryKZ92xrZAl4nAX7cDliQ2QRXuFCa7dUQw6FFud015FjmG1tD82VtKOaeQKO+Z0OlLOMCv+1vAmmNZqgKp4QZLHPN3czyXJljSWGu2BO5l4zFCVvvKSM4SePuulI7eeDLxK76veJiptqv1YQ7JMy+0HfQPJMSdZ4s+tW615Fkz0aO3yBzdsHVdMDcoqxd5Ks93nrnYIvc5vlFhreLiEKRNCaGnMGQwmHH86kSCcFjqt5ZQDw7R63jKej443KdH6mEKMEBIVolyF5FdFiP9WREaXezi10MdXed3K73FU4tko12uUFdccAk3Ibj7aHdW9A8IbvOFKxMyKJDCifSqXXH8Sbge+x8bDKPOwwKqveWr16OIe9Rob4MK2x9htfMeFoecy9sOGU8JnQyVpEtkKx33m7F4yZcXc43Hh+YvbHNk7OESGpn0rIYC9dCYlqLW9780lDA+N+uT+aIwfoGT7aj3Cm2FWeRZdfpJay8ugqhcLFBPGJc5PBhReH+ZdkqyCgTO2tVKrDbBZQvUEWf8w2fDg1sWgen5+W6k65rCMC0UZ+u7nzNI8R8B5OLbGXu4sucue1QdWQjMT8KV6W2b+muS88rfWMEQ855OryMsSzrUbqWWVCZTbgJjs413JTdjirWKC1Qci6W3WGTHG8UjR4yYhVpEqblyIbeLsTmCnFQqIcGt+40oTYA4PWHoyrU3W3Nb/ErqXLacjNIx4hgO64QDxWHshTbs4ettm8t2bwcV3hciLsDKOjCyLSQ1ZeQjB4OLMs1vt24CoFhZA9Hin5zrXJlXyDPltGdDxHeDU734zxvKGQeFBkYXeiS3TSrIxejYrKY+4Yo7inHW57zfieyvbhNagiVqd0ZKRgYQdfNGe5LJsFJSTWDRVFddcoPdsVyYXoxbafSUnJLe8Wf6vXNyS2GUZqVmskHDY863z4K2tZw69zTgFXwLd661v6GwszeYy+9QbLJZZueYC815ASq+6QGyK1b9clUKRnhm4SUTuHhGvoXe1vSYnJhTmui5qp83apnEIejssGVvGq2R+TQqdTZHpk1stjg1Jm9oMfotlxfyXUM4bh72hnXRBOhmx2KRSudc1SGBA7QB5mNVqGpwwtJ2sojavaH+TYwkxStzNXO3IzW+nqOnVi+2b1xHYjckUd9pRindceBdO39VXXYHGPPp5CFihxRfcmlGXFtFoF4EqQtIlicmVdZxQpMe7DHpUEbu5xZyHXvi5ea2dUOcZIV3Q0YGBLWSGLoRB6fNnLaKufW40gttauQMc90Ea8y6LxasSphL5Z9a2ILBdpbGzDkeVgrBn25Yw7V2o5Ec2OxyzY7ZFeBOIyWus63lKaklaWZp7m95ci+ROjhlo8ZljIiHhJt2cI3slNSY3VC2VRMrD5Ne1qEJactuxumcOsGD2uFDVKn8HKNOoVXHMchnMMsVd06uXzt8e0c0BMYQIBM5zTU6qUekamXHE2tS9iaP/dE2KLR6njrBkg0yFVLeIK124cSaxhOo0L7VmyZNMhkZs/Nj1roReIyW7dMc+K1TXRZpgIcNt1aQKBhafWCWmOtsG5S1OwWtlBtXIhhbW/Bh65z4en2RO32A2PtDI1F4o2GnP1TeHK0HD4fRTbumgglqTmdSYDqOgsh2Q/Qzk1N50SfsU2S4bw6h6E6EHydnBNSK9EO76LncmgOTW3RF661TlEt6Lvw5C5srmdXENMYm9Wo+VbTnbQ2svbRopH2m4YZDQnUoYTjQbHcoXJnbisZ5tMcQbaG3O4cfxPaB1eAYfliMHkal60C6/7uDDc2Kqm35TXdwfA+V/SsjHI3HJlLsbHk/TaTpT3SnjnQfyftDF1wVrbUgyIHVXjY6Jt0oQl7YJSyh2teZArCgiCVX8OCpSaaeTubhOa3nOoXy6XjWDfKLDWANjdALQJ6b4VLIlpBbDy/nQoNW+Vzj8rn/ZzMCVlyc4o7tLbQtZXKrhlRJSVC38tr0boGXNRTi2rcFHJeHjjjuknzwDdVS2VX+UCIxLhc1Tl/vKyK9ZUvfclpKPxMddBxNTYHv7paEL1tY/VsD2LXYJ2F7fWMSqClf0TP3QmvVwWi6RB5mpAHuVlMfS2OGTO2iTdcUGxOKwoVjvkt6c84PlgnIkA3iEzM8/ywJbTQTW6Fn+PmiR22163VU9VKhtF1PWeQNL904QBAKSt0y0ObuqhkAxIyV67m3e6G6Nel7QyplQo4wSN0pw0lHDOkyed9pHQnUM+urcboGVJ8f10ZNOTtPXE5J1z1gqBolzg2fXE2W1qPAkpdp3KHoK5oYWOIQRe67JmBGY4XFSrPvNm228TlnJRNJR03zzy0WC7J5mgIGbstR0AxGSURtSIUDBn35BIJFKCiczw9M/pok4pI6ipCxGVyzuvwMUTx6mzrh+NFGPFDxTNgJNtDBmjMAAixilmjtj8muu5p7TZj27KKWKKxySWYycu1gYvVGpQFq95co8PaK1mDM1JdotBGI5qcdwC5AfxI5HE29uY9ubOZyqa79XrJ7+kD4AKaegm4jeFtDJNaUg6xY0LN8yWz8jJWPo1yFKFcnq7RFmLWRiRRl+WO2NvcXDalwwZT19z5ouV6tj9GgAmKB1jqLhwcHy5wfall1OE5zK5WtAWzZ6laLk/zvVlbRbfTKqIzIjUrJCESJC7GjVSWun1T1/yKtiMhI52Up7PldehrUbn0cZskPIRC7rJN8xvgwWPODYhkVbjWnD0jF0fopFwTFieNNhOQi95CBImx6bInLCU4sgdczUuLaUfb2634Y3SxL6SaRA5+QKR2GZyHwul2+w6p6YNJifN1h+6vW2g3DtjOv/qkgcIsHvCZA9UNtebGNuoLc+lEYqFftU6zqtsWFGOybGy8D/Y925VUX28HeqRoSMJAuTpzHlOxqo9P2h4AYFyrjQ0pUK4m7TLRFsH8yPHXOUprUS91NRgpFLPB6ZMCEWXGOvaGqCnE3Y644DkYhd1g1Kl861Ina01mSmKLLBx9i92C80ana4lnc2gxpPSqTlBs4XgBtfcoiVK2pEPOz4uxNTfLMY93NDx2kFNfeM7Vs5o6+V2tiJhqc0vGHCQIOi+9yB/RG9cfB06zlVAILke0ppV6x2jQ4Gr+Uep4c3tIdzfrkOLEgDM7qzvHvXwqBee8Jf2opCRm7UZXlgG89iyQY1JsVm2a3lRI2tab7QIPT6TsHyi75K8DfA2Sy37BYQ5Zh9vFIPA0FZmWKTqeFxmDMZ6vTaKvlmpy3Tqtva7VOerycdYTp5hY4bZSV9tTC45dIY5ki7wNkuu8cf1NfxiZtrN6fqPtA7OHkDmfEuuW3A1qrkXEPMNI8zLIaOxr9fGWKzWOnDPMX7VnlRrwnkptD6NjaxHszPOBZJV0GarxZfQjoUH0oLGjY++V8mGle/vV3BAkIbiedqTbEpDmrnQ11b2rhlo8rQRidmC4a1RURV6pZy40s/BWmguXZAmL0+LFrubOvmfdeIy/6YThsO6wqQ7toRoXJ9rvKT9aLcsdzN7i41phAXHa+WajctsG85OrXrN9KSvDiqtWCwTn5v4GEnmxWwDgyVpuGa/TtZVcL0k37xBR8kSZVHU9WJLyLez8fmUF8gXHGOiiHSJYd0MyRCUqYd09ijjo7nBKnE6ObmxB5WbfB8frim+s1epa9vxCjRlTMqglPifI4LxlmlU5h7OboUlR2OTknvYdNYSIGjVOuALBWEpf4NLcRqNzckJiW54JGQ3TA48y7N6FSiogdjDqI6LAqEYyZy40Ani2W2wGP53Ha7G+bB2IdLWDSxYc7wts2RILzt1xvBXAAa+Dk7+HoMba76iRkszNDmsAX856DObn4TJdFzcTIc/zZH6RXWi4GgCKcycg2lhqj/4qCxx6fR3FNRoLGloEPQLnUoCY4UIw/aNvhnnCHJHSyIkGp2lVLeElHIPj6NlR0Jgwd9aCQhUGElJMOsKA2O5GrIwVzYFbq78h+HkkN97ZEa2GZtpS6sRKIrV4SLbajdQwjzvxBANIS8bmyzUPXYRVkY64313Fyp6jqD9k5BGnNzdfAlz7lqhkgaqnauklLCB7CVZdbIrH8Rue8qa8PHKCe85DcQx4Nd4WtOZAyoUtDvlF6AdKWg3kESYMZUOe3Ou+oUfWBTWHLcy41c5zsoMu/crAq/5AqsR1KYht05XEORo59Kp03L4g10ZOchYTq/OzoRKKKEhSUw01VQrbakEJQ06eVXrixO2tx/iWVfnKbq82L+iKRHOaQC6CfrO4iPyQDNtC2ck8OOl78KIpNtq8sNr2kMNxYY5z1k+Q3XF722oM8/T8dH80/PQKA5hHn5+mW9bvjwv+k5vG4RhXb++SUJLAn5/+393TfNxf/HiMeL+N79ve6137679v5C/PT7UbA4Met5mbrAvfb2P+j7u2X/7VneRp9/B4sj097by1H89ZWju83+gGR++uaYHypsy6+21uEOaumf6ypZn++MkFv5/uTuXV9PThrvD9wcRbW769P658mv7mZHp853ux3X58DN8fBzw/eQPIVOw2byiBv/l1Nbn4/ihrurM7Pct6+v3/Amczti2dJwAA -->
