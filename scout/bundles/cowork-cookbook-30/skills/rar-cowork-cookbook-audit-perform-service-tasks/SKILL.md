---
name: "rar-cowork-cookbook-audit-perform-service-tasks"
description: "Audits perform service tasks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_service_tasks", "rar_sha256": "0d86b97cde42c4bae87e32a1d371c6e46d39bd1cbeb3b4d639883f03de4bb0ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_service_tasks`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_service_tasks_agent.py` and in the RCI capsule.

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

Perform service tasks Completeness Audit — Audits perform service tasks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-service-tasks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_service_tasks_agent.py` and embedded as the fenced Python below (sha256 0d86b97cde42c4ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_service_tasks_agent.py` first:

```bash
python3 audit_perform_service_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_service_tasks_agent.py   # or on stdin
python3 audit_perform_service_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform service tasks Completeness Audit — Audits perform service tasks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-service-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_service_tasks',
    "version": '2.0.1',
    "display_name": 'Perform service tasks Completeness Audit',
    "description": 'Audits perform service tasks records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-service-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-service-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b7e3ed2c596d569',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/perform-service-tasks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-perform-service-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPerformServiceTasks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformServiceTasks'
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
    print(AuditPerformServiceTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZPi1pbtX6GzP5TdVCVCI6objngINIBGJCGEXI6yZgmNaBZu//c+AjKr3Nf2uzfixaMqMwGds/fa09r7CH57sdsmKqqXzy+ab+cz1k7TOPKrmZ17s03RF1UC/hSJA35mbpE3Vey0TVHVLx9fPL92q7hs4iIH29etFzf1rPSroKiyWe1XXez6s8auk3pW+W5RefUMXAJSsjL1Gz/36/qupizS2B0f78d2DjbZoR3ndTOr2tT/5Ni1783cyHeT+hWo9Qd7ElC/fP75l48vMXj+8vm3Fze16/oNhvIAoT0w6BMEsDG18xCsKEdgcA5eP6GCtzw/eAP+Q+2nwcfZf/1X0ttVWP/4+Us+ez6+vEz/1DafNREwrLDrZgJml7YTp3Ezvs7WaW+Pk7VNW+XAuFkN/JWHr4+d3yQV5eyn6doPDyWvod/88OWlABDsyZtfXn6cAUd9eana6fnrJKX84cfXtOj96ocfv8mpW+fiu80kDKB+/fp8/RQLFn5bGgd3rT8BqY+4Of6Xl++Mmx4P3JOdYOfL66WI8x8egsuq6Px8is0PP/6V2HuE0rhu/iW5Pz8ER77tAZuewH/8eHfyL7P506B3mX+ttgRh/XcsAcvf1H2cPR31V7Lv/v9fotMYJO67x/9U3J9tmP80+/kvbfu7DR9nwZeXrZ/GHcgOJ/U/z377qin05ucP3rc3P/zyOxD9fxWjFW3l3iV8zew8Dvy6+fr15w/1/e0Pv/z8oS1Brvl29rWt0j+T+Wd+vev5gwefq374416g/5gnedHns/dMn/1WlP9R/f46M+w09r69X3+efV8v02M+m4x4U/pwwXc1UwOs3/nxx5ffATcADqla934ZVPl//udMjN2qqIugmWlu0U4Ekzdx5k/g9SiuZ+D/VNuVD/xax8Cxz3Ug/6cIT4iLYPbr/3HvzPjJfTLjwp5Y5+uTQr4+ue/rnft+fZ3pQGRRxWGc2+lMXSvKl9wO/byZ1JWVPy0HROKMjf8J7P80PZnF+ezXv5H69S7gtRx/vVNo/OAkdbOb+KgGtPk62XSK/PxpgQvI3R98twWy08IFQIIYkOhHYGtdpB3gs8n+OonTdObFgK8ByY932cBHnydhv/76K6Di6Ev+IFBk9mD/egEWvMOZffoELArSOIyaL7nvRsXsw2+/f5j99+zvdt2FTzoUQOLPCACEe02WZqCi2gwsA8EB4QR0cY/Ab78//QrE5KBdgXjFQew/NoOMTHzvzckat/4EY/jM8YEbgWOzsqgawMqzuHmd7YLZO16gdLo08XZUgO7j+aWfe34OelMT2cCcd0/mRTOrQdrVwfhx1tb+XeuvTnXvWn4GSttufp2JGwV0iSIFvyaY90Vgc5HHwP3vKfB4HwipPtQz6k3E60yacnBW2pVdRpX91BHYj7iA7vC2HQi3Z7nff8mnVuhPrroXxMM9YBHwjPsM6acp5lOjBdXv1W+672vsqZfp955WfcnrZ7LblX/v3QDKOAvb2JtawD+eKVVHRZt6d/8BpJOkZxS8Z1TuOaj86UCw+X4IuPfs2ZcWhpbo7P/PHDEhW7OsSrNrnd7OaElXzw+PTUPO5NnHXATa+l3ZvTq+tfo3onjjyy95GoPwV+M/Hivvfn6ueXBQWwHl6lq9yweogMcmufccnHKqqqbstb/kb8T8EYT1zkIgDKBgQUJPefSmcLr6hjQCVTm9/takn36avALybFa2DvDMLPB9z7HdBKCqpjp6OhwkpD/VVB/FbvQHq2ZAOog7kD8DIKaoAPK+u04qgJmghIKqyL4tj6cAARRe6wK0YIr0X2cnUApTOtSg/sD8Mq0BXvhwFzXLfOBjAPHdw3Vklw8w0+D5BGhPfBz7/ff+f176lrp3JBN4INP27AZ4sp9Y1POHR1zfUT4jBYRmU3bcN/0x2E9LZ9/3j398ye8I34kb1HA6td7vXDMDtZM9cnGioBrQSOY/0wfkwb3Lvj4a5aMTv2P5/E+z9g//3jh+b33HP8bt8yxqmrL+vFg82tVbt3oFFbIAGRKXfv3oXJ+e1fbpWW2f7tX2B5EPD32e/Xuw/iDimc2fZ8tX6BWaLglA15SuzwfwwuYTdf6ETle/5Kr/LbxAfZEBXpu8PoJW+d5G3paAXhJWfjgtfrSVeupGPWiAdx4FAfiSv6fAszwATefh1APr4ruyvfdTENBHvN7pHlzKG6Dbm2au0J9OIukEv/ZfPudtmn58ye3M//sTyMTmID+BH6YjC6gU4Pcm9u+vgD3gQmxPz/94spLvT+z0kcd1AwDa1Z0NnnXxpLmP0+iaAyaZjglTy3rQOzjc2G3aTICbsZwQPk4l04T0Pj79s9Z74QIdXvF5qt+Ps2nU/Th7n1o/zt7OEfdDWd6Cg9TP08Q82QmWgj/va98Pi47/8sufwHgO0H8BIp64Y2Kbh7m+940Y7gEr7Qbw31EVAKTCvQ8LU4Osx3sj/WezgcLKv7agI3oT5G8++AateOD5/W5K8zgl/vbyRi3P4D0nQrAc1PCneuqJC5DaQCF4/UhCcO3fmRWfWwELgoEF7IW8Fe6QhOv5KOyiju2vCB+B7aWHEEsX91HcQ0jHW7qO7yAO6uEIuVohAYSA9Y4DBQGQ98jir1PPjyc4PhT4CLmEXQ/BYQxDySUB26Rno4Rte9BqRUBE4IFG8W1rAkj0aePDpsmB72Pr5Iunqb+9ODgKVnJovVs/HpsFadg4IjhDZM5veHDeXcjdXtMLWTgShd3IDG0MiiWiXJOW+6vUJ+tTv5fczdoMTVFcXqW9zI2UkmnB1et8itVy224uypKnWAbRlwSZjvMVBjHhuD53KnU17LCBIJ5Mz2nIeIGZlZAJ33Z66sbMsh1rPTOZoOtSY9Hs64VQsPFJO1xP9vkcpkhwXOnL1LK2ggXPfQ1bXujl8pa1GX+91YcaS6+JIGU7jLlyBclZEO6bDLRQzHS5GjTc74hqJZ60Tgp5wYXimuXnlW4zSaN7jqG25cndC1zdinnLdptSqY6px69kqEgILra7Ba2nt72uhGXGrHPDhvvV3LRKlVbS82E8Z0ejzlyD2tQp5aI93O3BSUZry2K8NdC+PPmHmsf2VcXjvHWpbdIs21YiDgh+vCJF5XISmCw3/dh3Ih6l3FkrQgirk6W34+klFeICIlBxZDrOSRtxC+YOjmAncM9SbugA27jRQk2Zmc+tuDEcqdsnzbhZeCIeWqhTHPVd0ER9nV9bsH08J97NVcaBdjV4XVmSii4j8mybRiltTLUz5I02T0+C2egJaa4UK06D83CN1nIinnUkZ9Rbd1boBSPPO069dDkbXtxjPJ4lE8nbThziSB2ZYmxzdBStfJCkiz2/3XZ+j8ONYoTpUjqzZmzdBtnO4HVhCgFFHO2G7llb7PRDwELH04YbbpAix+2OGDisXTHbIdcJlomUkzjI9NGtfM01IEMryTXWeaQ+IufyWvKddVFoQuxdv9lg4s5daZRQ+L5LZ122yirwU2ara1FBapn3Jh4cU2gv5DuTkJT+EITrHUmGO7QUyX51kvckOfeV+jaErnmuTlcvxmFlzyeViQgSesu1yDLyqi0hddUZVqxb4gUdai/Na1rc2QOvpvPl9uKXR3ZEg9TGN8kKqlNZDgkMcoo9USO3ItvZByRjKkPcu6cWFXoKv9jCDoOPx9qQYBHfbymq3NWtSYXhiU/npnjdKlx8lkvOXWBGRkGLnbEc3RsxKEXk5vgup1YxivrDaV7XmlgHfWEH89Yvl6zJkhhrLmxuDV97c3ndy2S3Yu0OyaSKKgA7maccIwfPta/4gtUU0dYbjGvr6CrXDTrW1lBpp5Lp2T3djZm1iFFB6/CBhwxYCAdvYNNdLCLQUraON14wNvy4kMiK2o967mORu88LXFC4y8hHY8dpV0sNF1V58G/l0YLgy6psbRqxmFTVM1TYmk1NDANNHtAEalJvo47SQoMtWyqgghLFWl+uDZzLB+qg25x5MuLdjeyPNzIWhqrYkrlSxRh9PeoH47a6wBFHXlP9UKXzW87Ng0weKOESRadVtKk7/Zqxpc5sO9Gq7Y4WAclkJtu4gxbW1nE0jkbb9f31YKaOQ5xp9qIxKzK4GqUI32hCwfhSMg6dtbK5FdLz242Qj+JgW7o+cIVeC50Ax6Z6quDcUxwK8ySEaBb1+rBFr+1Z5Kk0I5IbvzmxUIPW3HLcXvbJpsFuClpu4sTVQtSZk8la1Vl2pFtQbCJOU0qOzW8CNySw6GcOw2f7lJ0H3aGQbgvOWKZ6crKYfN4b8ZYdi4Ow2fqAe+lWDvp1FHQFdDabLBlGuqQo1lQ6CjoiJ0fLBivauJuCaqXrHqG19dI3LJUo4u6E1GO8tg8FxY6+VfBhrBt55C1Yzpk3O1uTL84KQtmqgdhyjnRKrog479NYnpuLG6Hc4rlbC3SY4AYb7+s5sVDsJCnmQhdXtzOXhCidkBAuZAFHEKc1jziXTCESeq2u4u08XkRiuZ7rKrZa6NGKXDQ9E6f1UVKiq1HhlU6H6+REcVq6LFY3U2k2VJjyraHLhRgKZ1SVWLGABTzcteHyvCOpeUCPgt2OfKLaHqoao5Du6WVFcy477CEVTQtoD28Ug2GOfgLojM6sc+tQgZRZ2tq8XPL0RpJNnltooK/kdKXZjD7XhqC6FSklIka7FJLRa/pTpjWtbkSFLeMc1S0SmY4KE2rcfpRrU5J3jB63yNlYJ3AUMbFLxIKH5jtCyMi5jbVDc+tPrMTD22jDHiP1PJb6hb5Yc3xJyrCJxPtNssS6OtD5U7LlYSIhxdO5hzoGq8RlNxj+6UJulC1MMzV/4WmlsXmDGiCQE0qgwUaVnfcHQBOJ7i+PXLcJx/QwqP7Q0ucFdebN4wqramebbrcrog+TA+vUnFayibxzw+4gqhu379sNRQyXvY+tcnY8SiGDh33pDms6JU8u01FYid9uUi5QbKjrDHTB1OsCsZ2dvW5lTzywerkrEVe1YOjcM9ENdynrFjk2hciI7OxCk5TcmzMUWgoPbgCy0NIvaoPxGXNt+T7ApSq1mAI4sSDp3SHyssplxAFbEelO2DtGVsT5cn9ZEcV4DMNWvPLBucuESCoWBNqG+97Urgwl7vl6RxZM3FvwsWLio6ZS3nUP5sETHBbSob66kr6fQ+48CfRDWlJRCC/0wnWULdmwCK7GoqMwR6racDwcaEJ4cw5Zqpv7IL7WFIGjPplXyxvnROuLarmye/RswwuMnR7hYNiFIHTB+uONRKtyRxKKh3DhUF+K0iLbbVSeovPxJIbMjnSWDaHmocBoVA0xsrNIXeF8Op4DYgNpwlrca6iramRg7gfdvQnZpruJa2zfFGOqC2qGxDs2QSjxpvMJvi8Fnr8FdK4jxBg5cb5LkZGb48F2U2rYcZTXLmJsQyk7R1qmF/CpSjUmrnbCVfNuIsNdg6uV8wdMDxfHS0Rh6w5TaoZSjwTBqzuhV29lcWS5K3312BCLW+UYkjbtec11x8JVhKqHKOQ71+qLFb4x1ny6oYqttIgl+RJI0pywJDLyEAk6nzAaFXN7RZlOA63ltebBJpTGMKzdqDl7UdF52aTZcZ/1kYZhWIjlzvaq78E5Vw6Vi8hiB1EOfPaAZYiFwR0m1KWUnzNya99K3CS2SVslumcNLjLEqYB6BQ9aUeXuYkJhkbmmHcftubviJykce8oM2pKncocmlt5l8HCnQbFU2iphpxPJSEJVW9XGEqRgZqyiNaZc5EY69OI2MebuEFm2bFWtYrpUs5dUl0yuGCZI8ujktinzNlWsd6jlkUFwkVOfh5F0Pez2BMxJhBulaklTcM/F0cZBkwoWe+Mw3gCX2B4nGCvIUIN9OuJu2yJB57GweDvCvYGnGwR3lZ3jSS2G38qcUiOD0EMqoZLy6EWHFlC+bcg4jaypHZz2oUwT81KAx11n7TeGnguJuybYQ6Ssd1cMTJ9DDY4xUujwhrlntF1sUS6m09q5L9T9cewMkSGunJQlqhKJmYseakZZn9LixNOkDvqlCR9yzx01T5XgeN0cszjKEqcahLXXbI5HKafDdLEW7bKVIinYKoHkcUfv3M+HHW1A/Tm4bGE+24ai3o0nizgyYGjvULRwlOt5rDUG0gtjW5WbKxd2caCumM226h1GqYt9DFvJTkaPfTQn+WiNF/tgCRWLvVDw5yH0RDFEVns/0SzeYDRa0JJUOba4X532cnVqr/XYVCshuibOMj8ybhutDAKj4iZlUXKTX7ETjZ/cWqPBqC+kp0PfEpvRr0VneaU1s2kPCnw8LYRNncDVRoElcX8L1P4Eaw4bU6Z8FgSLzMx0M3jL0zmXLyiMM2ZabubnCsX4QwPZREslTI8Hkn9cbzE6q/Zr/WaT8nXLR1dbI9iL5GA6RHTLgBvNU6uopmrOyzRYLE6GvUPAoDQQbowcO4In8HDVRWODSzBLRRY8ordiXYdJVyLhkhMhlMlklN3MFe3MFeiaPHq9cbE2GOob0lyUb90iwjmH7hWB7W+4lJsZDOZ6hGDUU3wrlJzkJQpZOHihHCTE4GLJXwvLuUkccdAgHbPAqxUU8DeL9hx0hQ4kIpS+01Y6dxDXBc7DC0fj0SEwdxoZCVsqgxZjQrJVnKOE5wWrtXxKYTb18sXcXAzQGbDczeBIfIBsqYGpNSwclvBeUbwkAYcrijrIVopbyCYbOeuGR/rGAWQD9y038AQJajWPd7gq75QNh1A1s9cUtN6PPmm5IVcj+wFl98corYC+A+RLl22DIuGaAaCvHqbeku3yCtykMalRM8EKFTyWLufScbvE7GV3aPgF5UqkgTKBtabm/rkWRbFp2x6kDJYRwg6KKG9PjIBiBnzoJGKLlmdwrMzCNsstfIyKgDOuMll6mBDgxKLiuI3IIj1HZ/V6oBMdEUmpCy02JGSCvOwL3u8aX2Y37cXrrYTHZAscwbwU8zm1Mm/dunU7hstlzsoWtwFOoXmvq5uzUl9rM1QFMsyIU3gSEZ+ihyQ/KttEHUnaG5cL1IqOm0vdD6tWbUYW35HbK0YnztqEbHyPhTrTX1m2V2yY9731UowK3YuX0R7hfPcg78hjm5p9eI33NGLixwUS9q7MndWLvV2q7jnajAcNsP8tES5hVGXKNPWfZY8J5cPKLBAIKkxsZDkRnHD7SqarghX9OeZQC2/lQcaJ4J1BSjDc1s65mtQpCYeORBicsk5TbbOahzrdHfcWVzjVlZ3rGYnjrhUMtLwXkRDNWh5lzqO7BeOTN5dZ0RaonrFGhJgTUuNm8cqICPXApWHNAvZqJamv8a1ZBph3hojAiBC0YKPL1bQOtlzlVwpY529MUTmIdBpYGWVmV2QPnenjFmcrkqV0tYhAjl3IUecLO/OhU60NBNKAI+OOQlV4jqMCdSPPy2516vm9tcwh0/NX+AIHLdoXtsqFdOXmsCo4l8QiWGkNpQqgnG3EC4SUwCAOps74Qs/BMQfuPGK19hc1RcuYCXENloEB8igOmZJwJ5ovQka5HplaaHXXuJ1ktTlG54sK3Ty0yFrcWXiLg6T4Y++ZzOW2mvO7y5FpnJMrBq0hzkfOgJuToxwQa04EuHaCdnUxJqIPydwhDeehAoflwYrUHvAuVWLi3Kyq0T51DYnUpb+UA000YzD9rc63tiRv6VU1z73P6sWct7NuPfdd31rDW8pYRxyDFRsX6W9FXARXwY2kg4i7y0PGBtEZDs6ZolWl3lgjubkh7n4wVoxBBF6xCRaezPibsQO/Fh5xPBeRJKUIN0Ly+URi3UGTF6CDIGd9Rw+LHt8jKphMHY+RTwGzvhgKEgIWsjEz7PtyWcvc2iv2fSAsU+xwjvUSL7R1DviX4hbq7nT0VRcrsah2klvbuRC2yVe5tL26cAlh7KIXtL5rOTdO1uv1Tz+9fHyZ7pU+b1H/Kx8sTzcA/5/dh3zcMnz7eOp+o9i3vc93XZ//JTS/fHyp3BhgedxhrdM2fN6U/F/3Vz/9zSca08bx8Qnt9NnZ0Lzdum/scPo+0Uuce23dVOPXukjb+83djy9OW0/fcKinL8G44O/L3ZSsnO5q33VNUt9AF1+f38p4mb5+MH0e5Hux3fjPl+HzTvPHF28EsYjd+iuCY1/9qpwMfH5AAuyCX6HX5cvv/wPWiS/VniUAAA== -->
