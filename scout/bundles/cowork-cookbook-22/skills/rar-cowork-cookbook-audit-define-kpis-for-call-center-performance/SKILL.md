---
name: "rar-cowork-cookbook-audit-define-kpis-for-call-center-performance"
description: "Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_kpis_for_call_center_performance", "rar_sha256": "00d85df12a6778b8234a0f0043c189a1e1c70ac2839438bdfa3548fffb70a883", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_kpis_for_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_define_kpis_for_call_center_performance_agent.py` and in the RCI capsule.

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

Define KPIs for call center performance Completeness Audit — Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 00d85df12a6778b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_kpis_for_call_center_performance_agent.py` first:

```bash
python3 audit_define_kpis_for_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_kpis_for_call_center_performance_agent.py   # or on stdin
python3 audit_define_kpis_for_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define KPIs for call center performance Completeness Audit — Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_kpis_for_call_center_performance',
    "version": '2.0.0',
    "display_name": 'Define KPIs for call center performance Completeness Audit',
    "description": 'Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-kpis-for-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9cfc4ed357308d1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-kpis-for-call-center-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-define-kpis-for-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDefineKpisForCallCenterPerformance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineKpisForCallCenterPerformance'
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
    print(AuditDefineKpisForCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebei2JbnV7Fv/ZGZRcRlFoy33lotMggoiICiGbluMoPMkwjZ+d37oN4bkfUyqyure602BhX22fP+7X0O/vZid21U1C9fXnTfzmeCnaZx5NczO/dmq6Iv6gS8FYkD/s3cIm/r2Onaom5ePr14fuPWcdnGRQ6WLzsvbpuZ5wdx7s/kndjMgqKeuYDhzPXzFvAs/Rpcyuzc9We17xa196QpsjL1Wz/3m+YuuCzS2B0e1+M7uR3acd60s7pL/c+O3fjezI18N2legSL+zZ4YNC9ffv7l00sMPr98+e3FTe2meVeMvasll3HDF/UK6LS6q7T7phHgk9p5CBaUA/BIDr4/9QWXgFXv2v/Y+Gnwafbv/570dh02P335ms+er68v0599l8/ayJ+1hd20k552aTtxGrfD62yZ9vbQAOPbrs6BrbMGODQPXx8rv3Eqytk/p3s/PoS8hn7749eXAqhgT+7++vLTDPjt60vdTZ9fJy7ljz+9pkXv1z/+9I1P0zkX320nZkDr17fn9ydbQPiNNA7uUv8JuD4C6/hfX74zbno99J7sBCtfXi9FnP/4YFzWxdXPJz/++NNfsb0HLI2b9r/E9+cH48i3PWDTU/GfPt2d/MsMehr0wfOvxZYgrH/HEkD+Lu7T7Omov+J99/9/YJ2CRGs+PP6n7P5sAfTP2c9/adt/tuDTLPj6wvppfAXZ4aT+l9lvb/qOW/38g/ft4g+//A5Y/x/Z6EVXu3cOb6Ao4sBv2re3n39o7pd/+OXnH7oS5JpvZ29dnf4Zzz/z613OHzz4pPrxj2uBfDNP8qLPZx+ZPvutKP9H/fvr7GCnsfftevNl9n29TC9oNhnxLvThgu9qpgG6fufHn15+B1ABIKXu3PttUOX/9m+zbezWRVME7Ux3i27Cm7yNM39S3ojiZgb+TrVd+8CvTQwc+6QD+T9FeNK4CGa//k/3Dp2f3Sd0wvYEQm8PcHxLAAy9ASx5m8Dx7QGOb9+B46+vMwMIKeo4jHM7ne2Xu93X3A4B4aRAWfuNX18BtDhD638Gqz5PH2ZxPvv1b8l5u7N8LYdf76gbP3BrvxInzGoA0r5Odh8jP39a6YIO4d98twPS0gJwnQUxwN1PwB9NkV4B5k0+apIYYL4XA4gHnWK48wZ+/DIx+/XXXwF6R1/zB8jis0cLaWBA8KHO7PNnYGOQxmHUfs19NypmP/z2+w+z/zX7z1bdmU8ydgD3n1ECGkq6qsxA1XUZIAMBBCEHkHKP0m+/Pz0N2OSgP4GYxkHsPxaDrE18793t+nr5GSPnM8cHzgOuzsqibgFyz+L2dSYGsw99gdDp1oTtUQEalueXfu75OWhnbWQDcz48mRftrAGp2QTDp1nX+Hepvzr1vdH5GSh/u/11tl3tQCcpUvDfpOadCCwu8hi4/yMpHtcBk/qHZsa8s3idKVOezkq7tsuotp8yAvsRF9BB3pcD5vYs9/uv+dQ9/clV96J5uAcQAc+4z5B+nmI+9WaQQ17zLvtOY0/9zrj3vfpr3jwLwq4f7R6oMszCLvam3PvHM6WaqOhS7+4/oOnE6RkF7xmVew6y/8WpYvX9JHFv/LOvHYagxOz/13gyab8UhD0nLA2OnXGKsT89vDpNU5P3HwMYGA/uwu4V9G1keAecd9z9mqcxSJF6+MeD8h6LJ80Dy7oaCN8v93f+QCtg2MT3nqdT3tX1lOH21/wd4D+B0N/RDIQKFDVI+inX3gVOd981jUDlTt+/NfunnyavgFyclZ0DPDMLfN9zbDcBWtVTrT1DAJLWn+quj2I3+oNVM8Ad5AbgPwNKTHECTeDuOqUAZoIyC+oi+0YeTyMU0MLrXKAtGFf919kRlMuUMg2oUTAHTTTACz/cWc0yH/gYqPjh4Sayy4cy04T7VNCecD32++/9/7z1Lb3vmkzKA562Z7fAk/2EvZ5/e8T1Q8tnpADTbMqO+6I/Bvtp6ez7PvSPr/ldww+4n1J0auHfuWYG0jV75OIEUw2Amsx/pg/Ig3u3fn003EdH/9Dly78M9T/+vbn/3kLNP8btyyxq27L5AsOPtvfe9V5BhcAgQ+LSbx4d8POj/j5PneneuCbjPj/q7/N39fcHIQ+ffZn9PUX/wOKZ319m6Cvyiky3NjGQChzzfAG/rD4zp8/EdPdrvve/BRyILzKAhpOqA2i5H83nnQR0oLD2w4n40YyaqYf1oG3e0ReE5Gv+kRTPggHgnodT52yK7wr53oVBiB8R/GgS4FbeAtneNM2F/rTlSSf1G//lS96l6aeX3M78v7XVmVoCSGDglmmrBEoJOL+N/fs3YB64EdvT5z/u8dT7Bzt9JHrTAn3t+g4Xz8J54uCnaUbOAdRM+5Gp7z16BAi+3aXtpH87lJPCj+3PNIp9zGn/KvVe2UCGV3yZCvzTbJqpP80+xuNPs/cNy30zmHdgx/bzNJpPdgJS8PZB+7FtdfyXX/5Ejeek/hdKxBO4THD0MNf3viHHPX6l3QKANPcboFLh3ieOqcs2w70b/6vZQGDtVx1oq96k8jcffFOteOjz+92U9rEd/e3lHXuewXuOnoAcFPnnZmqsMMh0IBB8f+QkuPd/N5Q+mQHgBHMQ4IYgHk16AYrZc4qiHRrDCRsJEITAXZRe2KiPuhRiuxiNLwicdrzAxkmCDoLAAZdpGgf8Hmn+No0S8aQgZtsu7VIo4S0oe+76OOLgro9iqEfhPkIu8ICmfQL46mNpAnD3afXDysmlH/Px5J2n8b+9OHMCUK6JRlw+Xit4cbDnBOUokQNR8yCsLjSNLMoBAdHKJZSXSEVSsthhSgWJMamqNnsOo0cxSSQ5s8L1EtYiqNgvkiuuitYRdbEWb46xptRncV1StTeQA7fULwxWpdvhCPnX+hSnh26/Go3DVqtk0txHhkS00uFcb/fna4zqB7vcHvVWrRDdIlo/CHAhqLmLnxDl3j0S+nXubcyjLck7ybyNV9zaKVh3Ps2budkf7CrTsfQgdrISV4tGZSpvl5eIG1DFYpeTS3wNkbucZ+c8cU054sJ2o9nEFa7uhXTsoKq9FSuSkDtPK3euinNlV/flWRh8pEDN5jL6cx+jLnplV/iJ2x5S0mLGvZ/zSO9vOK4Sq+vGZPtO88JTrbPsittUqbNJ99zlpkdZTSND4lsDj2CWb3F+rZxpxzYC5GqwpEweUI/TbMHnyfa0129cVZ5X+UWGl9wqzOpd00W01af1xZ3jVyPhbKbxkr0TLoXBwOeedjzs3Ca2ateSSaXFtoOGrq5uftB6SKGrwlwPcGIb6ChWqX5Vaizc3W7ITXSYA5IRvX3zKmXD9Pk0wKCxVlzbTdVV7ejXc6E5IY2rYaPGDmzG3RLZDCxknR0rJVAvIYrjFy3sVoeAYBWQ6jXJrBNZ0Fq5hT1hlFI3IajzIkuqdGTqqqcZfNHPb0iLepnFSy1dUQPW++j8fOT4XLuMl0uPXFxCW63w6kii3gZe+SqYy8+x6RNaolDGWiAi99YuNmLlYupOC1TqWlnZKVWP0RnfnS9ccNlhJLfh+nCEC63NziW/crokdqzIso1m3aQr/f7di+XWJzwDRW+0ILXeqp1bJCR1/sqnQ/J4Vew5Z177YK7uG/8Kree+d1rzWIE2A6G2sGxGqqVSa3e1bxzrvMcOGSSR67JFpQLbY30r3E5Ux+pHV8/Op1YnwhDa+it1bB3RwOTQqAdNPXqnMxs6u6buTT5pz7HdGKwl1QKrLckCiyuRMmVGzInszGmhdsQ28qE/9Nw+cvhUyc6aL4VEexq7w+G0tuDywuqg12oNN+abvaCfV4It6qojHnWnOgpOA1zlcQ2/0+0rSiOGI5ZHqtpQbdsriIZyZB1cHTiFNMvZXXCJIyBjta63kOVm6A3KxW0nX0KhvopklvJIgeSnemjqlYOJMWNf1nApGGQXkyKk2661PVHM8WBkyWHt9WSV4POS629wTWEdUR0WqndZyZcMR7AzBMeSVt7C684sxsV8MTa6fFGzk5OmpJmw4k2uD1E/F1rnbEW6M7LV2bYYfa4Ph8FwigvvFdpKPp5GWmsgdkMn6Hmxqi8pRjNrqt5DUpkg0oo+73YbVIg5vU4NItzfxL5kN5eaHMkrjjeuCyJkYP3mGMY360IgzpG9RF1mUlqtm5WvkvVGt01Ry27xQk62wWE/aCeF5DNLZaTucoM3WYnKe8+Fm0tuRPxCl9rrBrqypcqQt/F0PGemUhO87XRr4H5OqfCjp85ZYueGpeWOtNSFcMd4a0snMYSz8FLTfb7L232FsfPeYB1cj7DBFIWcnQuG6TqI48pXQVznzPai8ex1zChudGFkHXIhdVM5+JRRJAmzY5JVtUpJ46LEsyPVOb2G7n1VE1cHbZ4YuyMc6gpauUxyVrPl0pT1jJZwG/IR43S+NvW8PqpVvJwfFA0q7dP8sGLPrqUOlZIvj5zW37StxVYbLjn0Z684i2Z6u6GbOhGSYy3yG51pqT3feq090sJwJpvmPBg1BV3XZ+is5CSi6eXB65Sj4cGGXe1l1azhbYND5F5VmUja6Q0eQVCzXGEYQUYQxTJcEOM+c4DrcrO7Xi+bMx5AWTuil07cMRoi0HRuSU7Dmct2Xu6WgtIvUjs6MiU6bz1+SJcbnNy1csbVGeHVoWhtcZ5b6PhRSY/SPkHFhqDIZcWV9rll9XIXuqWhZcc1tDSgxM1HpCDK454NDbqlsXBN74/uRTqbOCVdSVXsI5kruS1hUcbe1K2aNOysOvja8ZqpNk9XS9hfQITlsOTgQbFaCFuSRFwwUciWKzDo0b5JTbE5HslirrHGug8jUaii87pLEVIzXUPBiIIghVNyW2yiBD4P8CW1qgPvOcROyjabvDln16XBcJ1xZmW9IcnbjnJY60RxRzoqTtk1hTLKXt2WZ7+nZeHM7hlbNdHcd3y9qgFKixjRm4J6kDbEAmWzA1ebsZ6ubybTOkamEOW8xa3UkallpEvhKlNTt5OpPVyxxBiGWE3GZE10NKppeCVZ7npbzjNzyUU+gc4liEl5uY4bM0pT13SMHrolurrnjZJngq6JVvy4tdtNQaYEH6p9WORXCB8Cv8YlkypXYiXdQjvgeE08oAIedKmmw1x8S5dnjy1zZ6BHdA3yA0ELdL+ifIg1/LnYbmqMBgWDWuWJhQQwaMWodsBPpCDeVh6NZoJ1gF1vKKzC8XgnKW/5be4hpboP8+2hDELheowrREagcSlAJA2GK4yXx4htQytjrTWDcKZpKwfTXB+yQ50tw8PSNpgu22EUjkSUzbXLXbqDsfG6iJNYUrH9DVPynWqq/kqW2y677lGkNudpG5caH7d54cOwH9QuewtPnrSRZWlJIXxOSZGhIn7XSCSO+U7OIjp0pTMNv57nN17frRNYmON+d2WCsoaWYdUOQStxonYWtzzHdNvlJvJapCCFrN8lvna7xPwmqnYF5u3GLVSB7iqHrNxHQ24tLH4xjj6tLRGBLHoRKTTNselaS64NSwcxM0DHsynTe3jUasJbpWemcwENmohncy/zW0rXPYtJ1rytWURC5vK6KUNL2gKH7JiFtIvZiMkQoTcVcXs6HytBne/czaro5IzPjeVaJ2udW1/DS3FaRddyoVwFmRNXBjzk7uVWHMPVMAhsLDg6p2RJU3sjdapxjornJBEulc0hHYdudxK9ZUi4QSubKL9T68YIkrVk2pZZMPKQMOTOxq2bvTwz224hr8AAgHZForhk1dq86kob9XCtUUbx5ox3sl1qo7tb50AVsd1KWmNJHYQJdjZEoz9Uw02KM64bmE4i3S64WfogozthE55bVNXXObzB7fPWOlyWfprErAYzsMCKLZEYxcEXd4hBKFZAmSvozCtcUxx32cg7G35c2qZ/LFPZPqer6yGX1oubmFE8GD05eO3dPBdA0bnS58LytBEpbC06ZiUzDsrIhiymEnrV17AvHiqYqcmtf3NX9OCK4vVodNgRgxeo4yxKDw3rRqbgSguW2cIJ+gaxrwx03hPaFcy0vTnsPPm46qtaj6HovIvErM2EDVRf22CLyildBjKY5vsozA2d29NsMoqBDq3X7U4g6XNSLcLEB8P3wMZhtI9UMfQOOnmWHezA9AdXgqRmlbueJmk6UbjDMY+xq0jv7NPeUHoJGfDBoA9g3mZQk2zMQka23glx99dwxcmBScTzUgINiDdR+ohWlCoxMVIt2fmgBGZn8vEBltq11JPmWdjVVnSaSxcSkfKUdZBVwdsizQ8o7S5BqtAYZFinbT9XdEEQ+W1B5W2jreb7DS6zwajbXGxv0+h66PDNiCtxkaRyX2GVNBKb7LYiNYkmTekEFexJq4WFfRWOizID46ZI790S5/cRFinsopWOc2Lr2myo9WZECV6kuFBfNqpVCq5w5qCFpDcNVq9kZLUsnaisanqJrsw5YoJmvDmglxtCF63TgJ3ZNlFIar4CYNQvBrdwepqA6sE+tO66tkgsDiJxGXZ2FGkkt0B3+fGwDEd3XLqCbFgJ7eFMpCwkWsETsF3abRr/omAWnKFka3I0k41NBvsWA8kEZTtjsxnmgoS3l65ZM2Nb92tu21tb+ISXq/RoB4nB7cBsgPjG7oyLux17MBscuIOBXIxwYQUWvEtdNOsDL47TqfDcY4+X3UDK9CVbZGWkrU4wrFCJlKj0yJGK1W9OuwEz14JQGSPGY0FCD2rOXihtfYEUPuw7Fd4nPLuBYvcqIIvO3WAFpPb8EKh2ADaTl3FgXfV6hYftdR4uTXJA4K4JiIxe8864D5i2905oNuaOFtp1LVPHS9AhBb1u91J4mstUfF2lI34jIW2vKiHCFgTKzqMDoawveQymdDf0zTFjT5tLot7OawZsjWLOh9Q9PdKGKJCWhKtlQW+WoFibdOmi/qZZkNGYCW622db75VhB7PWok13HD/BaYCGiPnemJMHMVqEOCL+IVR52T41ICCpunRwaUT0la2xdM3lajAkroozrJmeJ82nHB3LYYfl5EKPCoY6dSrXeuQzm+CLn40i+CKAXe5qxDfdBHVJOwNAHBnfyxdrQtEVgN57Jn+V6QMXDbThfbGyR7gNKzy3KjhTCr1RVFcjcupH4MPiEFMbEDdoYNLaMdpFgVchKFJALt682wlAqp4tC9rCQe4O4WYYGujUWkEAUZ/mULCytz4lba9T0dSd2vWSNxRJzHfeyXZm6X1q5suMyN7AZGlllx/6wqyz2VnIkBKZZFwoMY7scPQYpOp3c1+Fge+uk2a9X7BFV0euqZvp+q8TzVb0NRj+cdxqyEXIabq6hIp/2K2dRuSOK3XDbOsV8d6rgvGOU2Mn8/rjWvSZPvZZ3oWx/6VB9sYT5zr05c+pyLeadn3kC7tZgu+sWqM+yzjzvvfqm8Sm7pEh4b2hEt6xVrKQjmotSPI1BtkPL7sj0lHwBe8SGzX17MeJyneU2gilu3KNMnmzPvaek40JwbqF0tZbM3kVUGlQbSssjR4eqeAvENUTJYeTmPe0nfkjJ12rrYDxtH4kO4gQ4ZC0nhXAtWC1OMBIo28E5LTDLwujFAV6ImjbS/YgHu7FOdjJj6UEvx74Htuww5S4VpZ7PSybfXaPFUFB70iotjGIoeARzRJQoc3zLdEHpQefVJuVwBkwRzLVPlXp9Ti95gB8GRL5inL0t0cWAJFY70ie3ROCxZkja2sEksRl4PUVD8rbH7JacZ+i4x1ysijp7FRgHeX2UdmIMI/OCV9gOL5awyTtcoZWKPngAz7uyK+njzbc8h2r38cLzUBF3kwaV+UsVd9R63PqluLgwhK+ypFS59IqcR0Oz7pdSvuLpTlnmGS0czKrucxwdTXZbncNxL/WnQPcqXA9Jwz9uTDdVzVZxicpXluoBvYYUQrpLfb4Bwet3veCw1FqK/JZotMUYU16dqCnuqSa+XuLM1rnKKx6xLzcT9wMuD4lNZY2bgx5c3TH0TwiCgKnmXCi9D2aURXiq9mWSbJbGBRLCGhV1CeUTw7Vh7JLM19h653rR2rsoke52N5Fcwz1XH8Jj466K5XL5z3++fHqZTmGfZ+H/vSfh09Hi/7MTzsdh5PuzsvuhtG97X+6yvvw39fvl00vtxkC7x/luk3bh8wD0P5zufv5bD1wmVsPjsfP0sO/Wvj9ZaO1w+l3VS5x7XdPWw1tTpN39sPnTi9M10087munXPy54f7mbm5XTKftd+nTybjf+W1u83X8h8L4wnsRnvgdmR//5NXyefH968QYQwdht3vA5+ebX5WTy8/nNdEY8PcB5+f1/A11dPsO4JgAA -->
