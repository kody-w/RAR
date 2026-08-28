---
name: "rar-cowork-cookbook-audit-analyze-inventory-levels"
description: "Audits analyze inventory levels records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_inventory_levels", "rar_sha256": "c158fbe93d5b477ea29bf937f42a3bb2f89bc1d032f59c3530efd0204c667765", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_inventory_levels_agent.py` and in the RCI capsule.

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

Analyze inventory levels Completeness Audit — Audits analyze inventory levels records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 c158fbe93d5b477e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_inventory_levels_agent.py` first:

```bash
python3 audit_analyze_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_inventory_levels_agent.py   # or on stdin
python3 audit_analyze_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze inventory levels Completeness Audit — Audits analyze inventory levels records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_inventory_levels',
    "version": '2.0.1',
    "display_name": 'Analyze inventory levels Completeness Audit',
    "description": 'Audits analyze inventory levels records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2a74e65298afbf7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/analyze-inventory-levels'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-analyze-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAnalyzeInventoryLevels(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeInventoryLevels'
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
    print(AuditAnalyzeInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71a+7OiyJL+V9yzP/TM2n3kjfSNiVhEkJeiKIhMT/TwBnm/wdn537dQz+mevTN3743YWPuhQFVW5peZX2aV/vZitU2YVy+fX46elc02VpJEoVfNrMydMXmfVzF4y2Mb/Js5edZUkd02eVW/fHxxvdqpoqKJ8gxMp1s3amowz0rGmzeLss7LwMBxlnidl9SzynPyyq1nfl4BQWmReI2XeXV9X6nIk8gZH/cjK3O8mRVYUVY3s6pNvE+2VXvuzAk9J65fwcreYE0C6pfPP//y8SUCn18+//biJFZdv2lCP/QQ3tSQ71qAuYmVBWBQMQKzM3BdeBVQKQW3XM+fPa9+qL3E/zj7j/+Ie6sK6h8/f8lmz9eXl+mP2mazJvRmTW7VzaSbVVh2lETN+Dqjk94aJ4ObtsqAfbMaoJYFr4+Z3yTlxeyn6dkPj0VeA6/54ctLDlSwJky/vPw4A1h9eana6fPrJKX44cfXJO+96ocfv8mpW/vqOc0kDGj9+vV5/RQLBn4bGvn3VX8CUh/es70vL98ZN70eek92gpkvr9c8yn54CC6qHKA5ueeHH/9K7N1JSVQ3/5Tcnx+CQ89ygU1PxX/8eAf5l9n8adC7zL9etgBu/VcsAcPflvs4ewL1V7Lv+P8P0UkEYvcd8T8V92cT5j/Nfv5L2/7RhI8z/8vL2kuiDkSHnXifZ799Pe5Z5ucP7rebH375HYj+X8Uc87Zy7hK+plYW+V7dfP3684f6fvvDLz9/aAsQa56Vfm2r5M9k/hmu93X+gOBz1A9/nAvW17I4y/ts9h7ps9/y4t+q319nupVE7rf79efZ9/kyveazyYi3RR8QfJczNdD1Oxx/fPkd0AOgkap17o9Blv/7v8+2kVPlde43s6OTtxPHZE2UepPypzCqZ+DvlNsVoIyqjgCwz3Eg/icPTxrn/uzX/3Tu/PjJefLjwpqI5+uTAb++M+DXBwP++jo7Aal5FQURGDJT6f3+S2YFYNC0YlF5tVd1gEvssfE+ARb6NH0ARDr79R8L/nqX8VqMv965NHowk8oIEyvVgD9fJ8vOoZc97XAA0XuD57RAfJI7QBc/Amz6EVhc50kHWG1CoY6jJJm5ESDuO49PsgFSnydhv/76K+Dk8Ev2oFF09qgE9QIMeFdn9ukTMMpPoiBsvmSeE+azD7/9/mH2X7N/NOsufFpjD9j86QegoXhUdjOQV20KhgEXAacC0rj74bffn9ACMRkoXcBrkR95j8kgLmPPfcP5yNOfEJyY2R7AF2CbFnnVAG6eRc3rTPBn7/qCRadHE3uHOShDrld4metloEg1oQXMeUcyy5tZDYKv9sePs7b27qv+alf38uWlIMGt5tfZltmDWpEn4L9JzfsgMDnPIgD/exQ87gMh1Yd6tnoT8TrbTZE4K6zKKsLKeq7hWw+/gBrxNh0It2aZ13/JpproTVDd0+IBDxgEkHGeLv00+XyquIAD3Ppt7fsYa6pop3tlq75k9TPkrcq7F3GgyjgL2sidCsHfniFVh3mbuHf8gKaTpKcX3KdX7jFI/1VzwHzfENzr9+xLi0AwNvt/ayvu+m02KruhT+x6xu5O6uWB29T2TPg+OiVQ4u+L3XPkW9l/I4037vySJREIgmr822PkHe3nmAcftRVYXKXVu3ygFcBtknuPxCmyqmqKYetL9kbSH4Fz74wEnAHSFoT1FE1vC05P3zQNQW5O198K9hOnCRUQbbOitQEyM9/zXNtyYqBVNWXTE3MQlt6UWX0YOeEfrJoB6QB7IH8GlJgcA4j8Dt0uB2aCRPKrPP02PJocBLRwWwdoC/pK73V2BgkxBUUNshD0MtMYgMKHu6hZ6gGMgYrvCNehVTyUmVrRp4LWxM2R13+P//PRtwC+azIpD2RartUAJPspgFxvePj1Xcunp4DQdIqO+6Q/Ovtp6ez7WvK3L9ldw3cGB5mcTGX4O2hmIIPSRyxORFQDMkm9Z/iAOLhX3NdH0XxU5XddPv9d9/3Dv9ag38ug9ke/fZ6FTVPUnxeLR+l6q1yvIEMWIEKiwqsfVezTM+E+vSfcp0fC/UHqA6TPs39Nsz+IeAb05xn8Cr1C0yM5crwpYp8vAATzaXX5hE1Pv2Sq983DYPk8BQQ3AT+CsvleT96GgKISVF4wDX7Ul3oqSz2ohHdCBT74kr1HwTNDAF9nwVQM6/y7zL0XVuDTh8veeR88yhqwtju1YIE37U2SSf3ae/mctUny8SWzUu9/3ZNMzA6iFEAx7WNAvoB+pom8+xUwCTyIrOnzH3dcyv2DlTyiuW6AjlZ154RndjzJ7uPUzGaAT6aNw1S+HlQPtjtWmzSTzs1YTEo+9ilTz/TeUP39qvf0BWu4+ecpiz/Opub34+y9j/04e9tZ3HdqWQu2Vj9PPfRkJxgK3t7Hvm8ibe/llz9R49lS/4US0cQgE+c8zPXcb/Rw91lhNYAFNVUGKuXOvXGYimU93ovq35sNFqy8sgXV0Z1U/obBN9Xyhz6/301pHvvG317eCObpvGePCIaDTP5UT/VxAaIbLAiuH3EInv2L3eNzNqBD0L+A6Q6ML33bo1AXtzGS9CyEsn0KJX0MsVDbRvwlZTuwC6GIj1MOiqOQ57sQAmEOQZAkgQN5j1j+OrUA0aSRB/keSsGI46IEguMYBZOIRbkWRlqWCy2XJET6LqgY36bGgE2fZj7MmjB8b2QnOJ7W/vZiExgYyWO1QD9ezILSLQKX7SY05hXh0qm6OIqhnLRyCjmVd6LOAOzaHPabNkudYdNjQixuOTk+qatzYiJudNnHR38bLw7kar7Skcw4NiIiDlic0NcAU0S/82lPw9H0WsOHdD7MdUhJ7MQ0zVr1RK+sj8KSuNkmkWulIW147jzYudYtblC9gONQHqqztYkqIdqdN2cukvPIXJXynm2gRvb3jdZfRU+1iOao5WVw3B3aRLM3wi4qiV2H5+7ejkfP4GJyZ3DwXIrmXidXC3Sw2l3fChob12GJSifOrpwlbCdqWKujPm6UksvmnBk5xdmuk9WoQAV03obRYhkqhpKwsL7t80sllfVaSRDPkFdYWV5kjmgE4wTVghyUjSPYql6aRKH1OKdLS/1iqOdjeZTlakNcxaop9+q5nu92q47IQsc8bc98c71EEXbrO7oIOZk7SgGeuDTiCgyXngnXLOMjwlbt7nq1qGUfCmENhWeIXjlxhByRzYgPmZIQJFfWEUKe1Z1d83NH1Vc3DCoTZj5HoGj00oItRbFW0V2/WLMym9QcsrSuQ7VKBVSpjrrp1Eh+ZBuqbLzOykSiw7yBSZpoox8ZV9Bum7o4XvmLLlc73NzfbEtxXRoTzShwfQjwuiKO4XHk4r7NYuhSo3Ga3rZdvDxuHKmpTjBbXspmbQ9sQbkbW5Yap2GZDnF19phdTkJkLGRONQX+gmOKZ1IJHO0XLC4B9IyIkU/HehgkXlte3fCAVbgg4IEzdHMctyIWNvH0MmSQt9zycuUrJ4bfbwIHMdI4Eys8ESu4PJ1vknnWiQi+QfJyVyEEm9x6uT7xi2C/oDXLI7RQdeR8sd3KOLnn0Rpa9opcaJU+H0C3phdHa01CZ4wbL6XLEZZ3gpJYaeDcvUDKeY1u1gtfwC7DlUVFqtxvqBE75Tm8hZfFFjNVJWjEYRSNs7ZY9aD5T7arUDoiPcjz0O6xrXfZ9NqK18tVzmLcybkquZrRjGkTwP36MlhmJEs4+O2SUtWgbzBdrV3/LC22oPZc9P6kcBp/jWqGuLTjWRmVYyg4Pbb04SUc2XuRJ/OVvdhADMJam9owUWwxdDXcdTYjKY0Pt1vYa+T2ZF78k74ZE7+nrlh/1mXVmcIUYJ5DKUVLgYbpFBHmC7uT1D0UFsyVa8kEjg8ldljaBXWyyuYiLK8liXRsVmw9EuEw3syCG05RmzKI+HHuaiGfViDlro1uQuOVKgqJNdlNwalLl2uas2SSGttXcNFI3DbnJJSSiyRHUCfQ8+O40xijan2NH3a5m7jn46nnd6f9QHdpLAcROselkGc3HecvgnZ1hQ75MpAt6thelgv6eoqOcagqSHi8xSdrXnJnBLnkvnldQzKkC5memhfieEhzoZe7Y0ElY+mY+hrsS7FdEFmnpT/ompUUCmJnq1uJhG2Z3BZhbxSQFFABvq22JVsU2BrGEY4yEEYbjtU5cxfHFeEqGekuBpjhYc2jnetmU5LxIDPGBtBauW9iY3PMdZ9IV27EcR6WuD1Spc5adLWLEFEmcbEEYS0rt6VxJXsNwU5HpS6uV9xrswq9pftM4/Aop0ZKjDuIiYMjlzB82sdnSab2gXrmNoa7ulyPeLdUmAMnlNJtfV2cdEVKlaRJNXO71sTVBmbxa0HLxtgJlKaGlZNyKq0LUriBLBHLg+NVzUKv2/Cu1wjWQULO2qaWdaRcawuSTCA+Mk1F8m63YkntbQpbdBKjCkJkapcb0g28FicbyaVA236hYp6OC+V6WKLlfEHldJti5LWF1jRwxpxbzRd5RpA7hfcXiGwI5+oGI0HL6l5AKstlgorCgXOCECoCi9/pN2GI2pVawReiDGUaaYXDcVBENsl5g2YarhVwjwk3TaKLpwAWlhiB8UKaWXq5bm/7gMyHHiYEgjaGg8klxVBdAphLTma1tWDRc0v9QJBFj1f4rhP7lgvWXJm0hoT51+WtHpw63xZ5LhGM0BuZVl2HuqBuZXaCSyG9ojvTLkfqGmUwn4w0T+/l9Ny6In9EUpRlTcSwt65z2F7M4XAlx8FuBNG9WI2ednZtHZXj3N7Il73GqJEuMcfjoBe+vDTs0o/4cGNRfHnq2MWGTeTNLuqjXWYGLI3omJtyhqjDFE/S5IqEiv5gIGZxtbW66N2GZpa60V7XiczKwtmSxyKRuSxbRUx1LI7wAFLDYVioFxlssJCNxHe3jlkPtNv2jgQciIUjc6NhfvBWUaydej2ybkdL2ceCR99gkXJEhDnJUIPJ4f6WNvstQEmQFHVnuPskrU+uGDc5g8UQQFxhQxcRKreBhqA8ntQdqHZK7+GIiZjRqkN31fqyiy41UnU5QqWyQsnntHTTkpNXi5xo9Ni5bslzAAUNzVWIVrvakTzcIhZtTRB6FU8p0TbLey2I6m5w3Xy1Uji921RrISQ09ZSLXHSc5lx2PCgJw1kI6N0qchQxviTSLRBWBmr1e1dUcH8OrY6+mTMSdJvzQY+2GZiFpWEcEP42YDn2aHagIaXHc6FYUuD5umuu0QV6JUWjIsOEv2QniOW9uDI0VxCkK0yZikLCVbv1jzJB3Lz1wr65qRy458KRL5S1wbg06ViGvhrLxcU6rGjl0GvCZnHyUaa2C6vfUrkn1P1V1vbVUvPX4+BouHvirucLQ8FWGJ8RUtLZ7iwDyyTfZzeIUqbFJq2j1kSENjOonMkOFbzukj03nJ02UVedse2HXsoEdadKya5Sx8YIL5pUB00BY7SJj6edY5RB0V0FdnHgV3Sd7HymUllN8InjmtY3qZvJ0iZXIVWTy8OpK0e6KZsm4yRIoKs2zJj1otyxNKyJZbA1Rhki1uoWlbs4Q3jUz/IopfbYNpW8y62xRoYPVgpZ3dTBsWWTXlCnMgvORZCYo4BnjZ1hRqCKdRt5LAgJvWhPt3XU3S52ZENLwpgnqIbcqjUX2jeR0O34UuOafRYlI+5JLQHpedaljDvjMYJGx7Wz3zNXfZ7bq80hdEciyDdufWp0tGNRdOVLg3ThOtHf1C1tS7xTYYuSLF26wlfL0d967m45yHKsIUcquuxOO32+KhSBSJaidSoO9XWU503sUuj6djB0ADNGdbKZSBKMJEIpiNmWr0hnnqg5u2p7/hKux/1ZJ7d+cpsHMIj/TEVhfydoRqk6XSZXDUXhOUJ648leGWQs+GJPhQ2GkCO/S+s1m2ThfrlkGQXLidE090y5k1xtLS6HLUQFyL68UpUse1KcrHGdAC6tWewM2CRwWtAB+SNEODZOlnlOHXIVu7Qyx1widbWRYkqVTBXfGtb5gtORX55osc80SRO623qrF1bXFfI6DQmcyWPCtGFxLuVwSBOliUjayubcU+2oVchAjHPMO7fYkHA7WlabEuM6Y4PBVlcr0uS5GNAmfsMqrS8Z2EfmtaXvsnHrntU1Id6kMMFC7VzHzN6l1sw66OXdrsl30VDkonI53OaeNPS9rbFdTEgLZq+W/ipo2CLAhcrDY4uzyphNx0JqU9CbnJuTeyxc3RCp5ZZbJw5StsuLPY9T3YbXUZMhmC0qkJ57RaHAoOIMubI6ro5ZTZZ6mXncLhqp4dYjeZYVspFEiKWeAwLmHcZV1eAMR9UmCnnmItu2vzkREQRCc6vfyBYvI7HeuFuJcZurYXHwQlmOtwrmHP1gaNtGwVanFDbnGmtS3RUjz+2BVG3YhrY+aq0vHqobiY3mTi6DJnmuKvOlst6Qp5Z0cd1HadzYpaSyqmtS6HfwjdeE+iBBZL22HKtgdjvuUlsKZVn8Fl6HrCkl3UEuad/etfL+5g8ZbaFi0B52V4fbNdcU3UnCHPDfsKJAPoJtKubDyppWkJauOGx1uJH2yagiVmziU9re2mWhxC7SrdGI590bt9g3xkYJLqoK6Q2BxPoQztsTS87Pm7VbzBNxvgU9Uj8ulwvsOL8YuaQPGUodFrdGELhbWu5JeB6hMGGtme0xqqizN68kEZ9bzDrLwWYzWSzT0Rhw6iAzO9AaiRd3TSQUsjxJ1I2n6AT0qity7y1YEV2kMb73tu1hXcG9AzpIOAelULnl1l4ZVihrigeZJhNKWebDsN5FSapCkZmAXfxutUVP27ZbNdG8kyA79q8dmq39RHe6SxH6aCSsvV3S6COHXlDFKE6cFuwjLyq7ZOt19vo4zDfnOb4RS7koEC+qTT7ErevC0K3Snzf+vB98mW63IiTK9E416bnnt6273sAZjvpbdbc+UVSuXkYDMnKuHszMnO8K3DOSXF+3nZtvTrt57gxLss6WfrsMNwCBW1sYV7hPWum6POljuI9WkRuJMLvGtQPYMzq1D7NotVr1Jk3KEOnNW4YviblabmjeP/PFbjs6LScGIU1V7IBDa23chDDin9nMcfGBxq7wkQD4MIyQn1y/WFPeetVj3pyk6r3ODQwki6stROwLn1GYTYfNdUjEAwo60/g69I1OTFQ3Ey7QUCOLZY1FbVCBTmGDJHMSI+O8HjQ0JlcDrNU3hRJt2U5oxEa3Ctg9qIJ9I1bbI2VysRe2bW7jio1WxZAs2AMWgzIbWRga6Fex313XKooRQ6ZeFF5SkIVP+Xt9tOQB7NJ3tHde9rYoIjiLMrdi5yWLBL6eGu4s+1EwrLNDfQtLpTJKGg0gn+noS0Di4nzBrrp+V5+EXsj5BWoQ2216NZlTTHEk2xoHnV0U3KW8oqjFb5aH9QFQ+Aaz1jxI9gVSBNDxVnVlSbgwSvU9PUT0glzw60LjlT0a7If5MJ/r825RChfbNEr0tAL77mYcQDe+T0UDWXgkdQspbM7ucHS5ajrRnN8YLo7k/npiWQhjUjhykCTbN8VAbXIlPm7DkjTPkAFaPM0PS2t14aRDW1UYdnH4lckS/TK3yCaiiCQd83kNW4NFLNAdGu8OOhxJ40KkeXcdQfhhn6/hQsIYX6v5Y37QkJTICjtetgSaWbeEvJCV2uIaDQnHJZr7cehmSbni1X6uHMu2PGRdjHqOcqDPLStgbUNrqaLYrG7giZHfSjU7pNZ2HB0AV2Y2UKkcyfTQqEtqXC9d09PnSEIEzZJ3Oz1g2xGtE2RHmfLFvpi7HdytR7b1DIpLTzivtzhjbkNFsg3J4mSW5AEBdwtdWB0W+jZVUsJPlxrtkFXS8xvarSTUViBO1CwLGCQgSswf97TBg+bh4DHOUC2KdDegpbGP4GXm2LxYQvMipjYUzQOgyjGmafqnn14+vkzHps8D63/yK+fpLPD/7EjycXr49pXV/djYs9zP97U+/7MK/fLxpXIioM7jyLVO2uB5RPk/Dlw//eMvOqa54+Mb3OlbtaF5O9FvrGD64dFLlLlt3QAN6jxp7we+H1/stp5+B1FPP5VxwPvL3aC0mE6678u9TL9HeFO9yb8+f71xvz19V+S5kdV4z8vgef788cUdgVsip/6KEvhXryomK5/fnADjkFfoFX75/b8BVD9W+swlAAA= -->
