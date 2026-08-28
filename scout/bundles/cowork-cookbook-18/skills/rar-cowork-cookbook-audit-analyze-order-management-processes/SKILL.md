---
name: "rar-cowork-cookbook-audit-analyze-order-management-processes"
description: "Audits analyze order management processes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_order_management_processes", "rar_sha256": "8598e4c49a70fa8271b628ba63333bb604901a4f0efdeefe3ffc5a0696b67ecc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_order_management_processes`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_order_management_processes_agent.py` and in the RCI capsule.

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

Analyze order management processes Completeness Audit — Audits analyze order management processes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-order-management-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 8598e4c49a70fa82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_order_management_processes_agent.py` first:

```bash
python3 audit_analyze_order_management_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_order_management_processes_agent.py   # or on stdin
python3 audit_analyze_order_management_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze order management processes Completeness Audit — Audits analyze order management processes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-order-management-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_order_management_processes',
    "version": '2.0.0',
    "display_name": 'Analyze order management processes Completeness Audit',
    "description": 'Audits analyze order management processes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-analyze-order-management-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-order-management-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58000345806d3718',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-order-management-processes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-analyze-order-management-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAnalyzeOrderManagementProcesses(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeOrderManagementProcesses'
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
    print(AuditAnalyzeOrderManagementProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Va+ZOi2Jb+V5ycH6p6rEoBBaRevIgBEWVHEBG7OqpZLptssoo9/b/PRc2s7nndM68nJmKsJUEu53xn+865kL+8OG0TFdXLlxcDOPlk46RpHIFq4uT+ZFX0RXWGP4qzC/9NvCJvqthtm6KqXz69+KD2qrhs4iKHt9OtHzc1vM9JhxuYFJUPpWTwNAQZyJtJWRUeqGtQTyrgwav1JCgqKDIrU9CAHF666yyLNPaGx/exk3tg4oROnNfNpGpT8Nl1auBPvAh45/oVYgBXZxRQv3z58adPLzE8fvnyy4uXOnX9hol+IFJHQPI7Hu0NDhSSOnkIV5cD9EQOz0tQQWwZ/MoHweR59rEGafBp8m//du6dKqx/+PI1nzw/X1/GP3qbT5oITJrCqZsRpFM6bpzGzfA6odPeGUbLm7bKoaGTGjoyD18fd36XVJSTv4/XPj6UvIag+fj1pYAQnNHNX19+gI6F+qp2PH4dpZQff3hNix5UH3/4Lqdu3QR4zSgMon799jx/ioULvy+Ng7vWv0Opj4C64OvLb4wbPw/co53wzpfXpIjzjw/BMKodyMc4ffzhz8Teo5XGdfNPyf3xITgCDozXxyfwHz7dnfzTZPo06F3mn6stYVj/iiVw+Zu6T5Ono/5M9t3//0V0GsMkfvf4H4r7oxumf5/8+Ke2/Xc3fJoEX19YkMYdzA43BV8mv3wztPXqxw/+9y8//PQrFP0/ijGKtvLuEr7Bko0DUDffvv34ob5//eGnHz+0Jcw14GTf2ir9I5l/5Ne7nt958Lnq4+/vhfrN/JwXfT55z/TJL0X5L9Wvr5ODk8b+9+/rL5Pf1sv4mU5GI96UPlzwm5qpIdbf+PGHl18hT0A+qVrvfhlW+b/+60SOvaqoi6CZGF7RjmSTN3EGRvD7KK4n8O9Y2xWAfq1j6NjnOpj/Y4RHxEUw+fnfvTtlfvaelDlzRgb69iTFb3dS/PadFL+9k+LPr5N9NLJmHMZw8USnNe3ruAwyJ9RdVqAGVQdZxR0a8Bny0efxYBLnk5//WRXf7tJey+HnO9HGD7bSV/zIVDUk19fRWisC+dM2D/YDcAVeCxWlhQdRBTGk2k/QC3WRdpDpRs/U5zhNJ34MWR32heEuG3rvyyjs559/hoQdfc0f1DqfPBpGPYML3uFMPn+G5gVpHEbN1xx4UTH58MuvHyb/Mfnv7roLH3VokOqfsYEIBUNVJrDW2tF2GDYYaEgk99j88uvTyVBMDnsTjGQcxOBxM8zVM/DfPG5s6c8YTkxcAD0NvZyVRdVAvp7EzeuEDybveKHS8dLI6FEBe5QPSpD7IIcdrIkcaM67J/OimdQwIetg+DRpa3DX+rNb3XsbyGDRO83PE3mlwf5RpPC/EeZ9Eby5yGPo/vd8eHwPhVQf6gnzJuJ1oozZOSmdyimjynnqCJxHXGDfeLsdCncmOei/5mPDvKfJvVQe7oGLoGe8Z0g/jzEf2zFMKb9+031f44xdbn/vdtXXvH6WgVOBe4eHUIZJ2Mb+2Bz+9kypOira1L/7DyIdJT2j4D+jcs9B+n+eIVa/nRvubX7ytcUQdDH5f5hD7pg3G329ofdrdrJW9rr98OU4MY1KH0MWHAXuyu518308eCOXN479mqcxTIxq+Ntj5T0CzzUP3morqFyn9bt8iApaOMq9Z+eYbVU15rXzNX8j808w4HfmggGCpQxTfcywN4Xj1TekEazX8fx7Y3/6afQKzMBJ2brQM5MAAN91vDNEVY0V9vQ+TFUwVlsfxV70O6smUDrMCCh/AkGMIYKEf3edUkAzYXEFVZF9Xx6PAYIo/NaDaOFICl4nFiySMVFqWJlw5hnXQC98uIuaZAD6GEJ893AdOeUDzDjFPgE6I4fHoP+t/5+Xvif1HckIHsp0fKeBnuxHsvXB9RHXd5TPSEGh2Zgd95t+H+ynpZPf9py/fc3vCN/5HVZ3Orbr37hmAqsqe+TiSE41JJgMPNMH5sG9M78+muuje79j+fIPg/vHvzbb39ul+fu4fZlETVPWX2azR4t763CvsEJmMEPiEtSPbvf5WXqf76X3+XvpfX4vvd/Jf7jry+SvYfydiGdqf5mgr8grMl6SYg+Mufv8QJesPjP258V49Wuug++xhuqLDNLfGIIBttf3bvO2BLacsALhuPjRfeqxafWwT97pFkbja/6eD89agWyeh2OrrIvf1PC97cLoPoL33hXgpbyBuv1xaAvBuK1JR/g1ePmSt2n66SV3MvDPb2fGBgATF/pk3AtBp8NRqInB/QzaBi/Eznj8+/2bej9w0keC1w0E61R3mngWzJP/Po1zcA4pZtxzjF3u0RHgTslp02YE3wzliPaxxRnHrfdZ7B+13isa6vCLL2Nhf5qMc/OnyfsI/Gnytim57/byFu7KfhzH79FOuBT+eF/7viV1wctPfwDjOY3/CYh4JJWRhh7mAv87Y9yDVzoNJEZTlyCkwrvPF2NPrYd77/1Hs6HCClxa2ET9EfJ3H3yHVjzw/Ho3pXlsOX95eeOcZ/Ce4yVcDov7cz220RlMc6gQnj8SEl77Xw+eTzmQK+HAAwUtcWoJFt6CckgkcJYYiboEtnQdYg4/rksgCwpBnUWAgMAHsIvPg8DDHYSgCJcggedBeY/0/jbODPGIDXMcb+mR6MKnSIfwwBxx5x5AMdQn5wDBqXmwhCqhm95vPUOqfRr8MHD05vsMPDrmafcvLy6xgCu3i5qnH5/VjDo4BEa6euROKwLYeEDs5uuLmd1cf5eeO6KKWuW82jNngtDBWiQF2jN0ZS+wDauna4WeY7yWbYKTtLxxFHGeK6Uvsafewc83b3ryurkahTFtw1F1ic2WsSVyRuHHFj7vmyYWO0vMRH0TNopUF01mZmK5TfbzEyhJIe5mMyKbYefNcTmnDdOoNhdMjHSprfVFXonDsDGGZrlMb1eNmQqVdOR8GT1l9vUwSOnKdM/+rfDYHRHM9gXRSfrU7qSKSlLk6h+1xb6+mm7ocaSeukOrFJaB+rh3sLDzKTx3wOhvoHBmYja0BoqUvQuSveyIlxnCtvN1Kk83c3ut+gfpuLodgvywsJcWLyx07mTxx8YLXcZY19J1bRmWSGwqEWh1emAcLsmluN1tSqKNWxu3tNPSrZIAUdA9YrT6xhHrBKlD/jatbSNbV7wv2sItCFe6bhQzazmI24rzm+YkSeXgKbQFMEEJZfYklHGKKOm+7/iUmJ2M6Oj6lXyup+y0WZM0jtjF2pU6BR+QPKutmLjZiE7w2s1ZY9yJbqZZYTo3sFSEwbyEbn8ttteDb5BSQZRTv9pw3XXVeDZXRPlalctqFhUMPs8vx6gh/ajHkZ4N025gjmrmon2+HRSNtxSGCCpm2NIbZmGoCcBuiez1DlFrhzBDG5s4DsF1UyPYlfNw19ZAfCgy+hZFpJsssGTV7xjT3cWEuIiDdZDd+qO2AZrHW2sqvHEL3R4aXLge9YOYL9jMn6OS5MfZ5XyhMnm5927MFUekdR/dpvy6jXB8iF3VWbkb+E+xN5jTC3WM4xfizE1vtNpeDW8zzGxhypWAvxxcbBcP67mvEUlid24fUWluMVc/9t1VK1X28nwxiM6r54nqi1xqgZaY69uBOmSCkg1KIjKYBebhLc3XpWVtTcBvpNjas0vyuDPxOF8TxZmN8gMWDtitU2M7KiVgW5XZp4NDhQMtx0pRh1tHN67y3Cb5eL1iD8lpmbEMXR8lL3PtzNRie1MdPXJxsBh05gDktuydQS8yzzSEJBVD1Gh29gn0vHqENXRsz6YGi8at5ClLDtwMieQNwa+cpvKp7YwWFpRAubOYP2tLhJl1rVAlvna0EYZlDzNbJyveiYRa2xyTVnEMTFMuZRYs2hVSTWujMZrEti7mpQj10Oip875ad2aYB8v5tFucRNWVLlvOMuICWc6661I4wBxIyno9pQCHlfIy38tKc5sdc5FuL5ddL9ea7cUHjmjAYSplltFGPC5S/CU7JBXK09OOX1u2ARh0anBLIjJPuY3QiYdW0+GEYPFKSTWpaCCj6eaBXUZbhgaXVA+rchblGzPINGZVs1FsUcxK0awhz8pkwwbyqXZiXkbTU5ZvGu9q0A1vIqkVrQZ6DzAWMOUODSItABq+Qi3JqZqcOjtGujRWxbUIyIAL5UB1+Vtapo22boBSULhm7gnnChAynzN+lugKTlELP576XKVGyWDsfPYmOjLCpe7xmHpaxcN9g7ds1oMY0df9eci3QRL0B/7KLOtLP7/uuqXgSKuZ2zOLk7Rfh7lulUtCzhOO2JTp/GYpZUod2v0pCLfdDj0cePq6652w4Vv7uODtju770zE9h6HAnnONsUlcJAYfV/QqOMSrZWFKNlJubUO8HS81IXkmlSapt6x3xUoM4y53DJuv0jARF/2CjKIrawioyw85bXFVhLE3WF5XfM5Z161q+AGpLBadVC6XXWzsxctZkAapmtmoIej1IeDm2VVzmP4qpTwh5cGWJM2dpJJJtiXt9Rp43VRCKG2/v83Yajnb72czbNAD1fSHqJA5z5sJ6OnQryzapMx0xWYEhZehGZXp0Jw4IUePxFLl98dkpZ1AAaSeMdOOUsh8SankctbOHc/HyCJeIPZ5Z/t17KzMU9VuceYcAtPZucIGhLFu6IdtKRumsEH8g7xX6G56q4v9dWg3x5ZGmRuQNzW3KbltmNa5S22dFaFEXpby5dK+Fo2K5VyFuguk9uWsjJ2dgeKNs8lpdNskNJJEPqF3J8HRgRQkDG1XTabuLWQ1v2z4hALHSt/oFn8gUpT0ExfuuAuULDRTGgxhcxJLjYnVbG5NmRaS42oXCYGGBV1RrdfcycvWuCLxPapd1pmt5B2Y+tdtsttcSv5SlzyFasxhW9gecc6RJnXwbLW/aWi8mKGI1KwMIqMZLJgB3nH1RrzifbizW+5mawtM38iF5lz9YbU1dgW7VngSXRGMZTqHQSduieLjdb5FFprHmalcyrgR3IbWri3mdpy6MhbIa5vR5aM7y6Z155d1UqwKvLjuLPVc5/iBxuYzy65V5dBLqi3Od+lpLqe1kxx7dkahl5gbBs9O8fMpKIsrwWdpVTuFvVfY3kmzs9z6rcJcGEIWPeXEXsROUSVPOjfx1bzqpFHMFUKOpL6Cc8eeYthTKPh443GhdjBEdweikkf1bRMiDmOIqV3HmaHyycVxhE1jr9jzNMtY2KSaY1duLURyQv/iBxHSKh0zQzvHKnAOzS8FzXGbA1YZaYiR+0u6Pwpm6dnGHJntZ9qRTJiQzqiGs1c4jyNXEcejrYaorVCWU0yhbgmBm5hOZoBsXS4+bVNjX3nbYM+xx74PdsYcawQklHkhqWkmDinXb5TUWa07FuPVVLeFZODZCI4QU1ITV1i5gKNSUmuse3JLbIX6bsclu124rS/iQRHzIjuTcqNU3hIE2PHmy+TaQWj6to9kiuNj1sB3h1XJ74ZL7IgncF4Tbbo2JSRsrsJcNuty5+3Nm7Gtve0uwde5yKQ8HRcXzQ9OhshMB9lTNmVBJNM8KlS7jLv1toqTU4rrOYbL3Ypfy3xObVV8e9t5FzbbFR59c3dRiURl1R1dtvOkWj+eEmY1XE/ZXNo0ySXcUbGAocAY8r2BWekiv4rBIMaksNlF2gkn/VOmrwrhjJxMY2odM9RML/m2RYud059r/LjsTBO9FRwo0JNlZYV9aa76GrU8Q/HMXRVEAqscIM0N6gG3EdSIN2m15zwYtHrbqoKb3pRexoj8ynZTNDEUTVIiGnSpePAzoJob9UKm2U3Ed10f9TnIDrZPDI7Bn8KFv1niyNadrhE7vmTGScji40muewczMXGvUEx2ZMWu6ojTuQJW2WKcvDlTJJsqF92jqSlNpvTsunKlc4fLTKMP7JFoKDkZ4sGl+G5vRJY6n7ntHKvgjBCDxWVutOwyTYjNPDkVjMr6To5x6mpLKju+NhOPykJEFIZ1zrNb7HzLtjQ3XSiYdHZS0T5ouQv3Es6wjzqaz4SBNJliRtV4ckWJyzluFrocth4R82veFNaEYV3ibAtzqMxwvc9hgDb+FV2ljDT0kuBYpUuueLIIUpjF+V4KBM11BzsE1Sa7GqGk79HQcOSL6u4STpQ6T59DYjrsD1hCHBDPYLkGkbdFsYiY5dU8B7V1w2rxkAdggfKOdjGHeoWiO6ykKwZuNMI8Ca49vWKTm8uxdV9eMGe9VneitdO2eztMZ6tj5PFdbLvsem3vE6/0MDati7POiX5kVbKeG4Hib4ho7xCVmAj2IRJrB829jYudeRFdJNdNf/TAgUUVjfUb0ZJMuRalaLfbxeTu5OYb30GmgoTdeLYWXf8cWaZ7iDbOFls7dLs8tLybqTFm7jDrOg70a6RqlHDqghPtyltUwoG1L6tyiRedZJza+riz1bBlRXtBh6eZJKCCLdQbck+Gs8Gxwo2LgFtgANK/aeR0i9pbfgZSze8AajFbaoFyyI0cFppuzX0aKGhwpHGNak91uFD9BqxxmsR79XKAGwoly31+uBm8ZE9LGKKQVXVKtZoUN3ezlbsEfjabsWeVlJhDo2w4vV3W0yucWtoFISKWwkrR6nwgZ9HsjJs0FS/yTcCvLtopsuCsusPmjuqRao6krI7Bvo3xnjI9STcj7kyf3a1uRU6ipVZVHOVFEhbWO8L1Z9IecdpDkFANOruGVNH1SN7MumE2VVM6TFTH6ZkWjl6JT3vORSSm62N3QVcOgy3qlXxicGd/ufTaicIjzThdeTkLHQnFAkTOqDi2A1sLt8L6JnRrWBInmRq8hiejPOyFq7cVzu7mwh3aAwLYCGYe1ofqcisMqrcgb8x5JyzdepVsbquOAHDDYXFqdaRJPZh3uSVo6FaWrnMuiFimi4/+IqS96dAOOO3i7lVA0MgQ+aOGacch09yG0Z2ZLzEeZCIOW5KqtVGT3XKuz/Zidz3OjlrqyOutaTvlUlBoxSjp6W1mLBYbUKlkOy3gbJO7pJkMdVXgO60cznpmY00O8ykyW2Tq9sLWpXb6dUrWA6Z0Uz05Mvy2rOpbqbvMeUtq1cFjbcnYDfpFtIaSs5MG72dC2tnmNhwYnN1TBEcKjmib/nEX5osBZecRCNatLZbZjmtIQVV7QecJGvNQz3Cv7Hl9i9WTG5nLApc4uHkg6/2C6o5ex641MjwJUrIWGkQg9/aSWPFLw4k7VKF1WwVcqB69Yz/vkSLHhw1l39zginkCbByyMZPdbeDXPoJapORe1TNO2IY91891imK5y5HUVtFVsYAHu3pHIacMgLgtSFx18y6/NpgYXZl8mV36/mjeLLY+iZum6DXQxbS9PSw5bro0GRm5nhTmVMEtYihFoZeROwrkaoiQ7tyy8APSLw5TtEBkZXcq9POibRc4qJTFVUYomj4cqTUigiIHRthrxTaUjwR/y276en/GN2QfmzvUpMrcq6qQmMNhYLWdsg7p1PAA7ytteYjWh1ul1RhBzPPZ1pMwmZ6RmsYWiKbS85I5cQs5M1N3dq2JMrcyjmLMkMrmkMR5qmbM8oiRzHw2YIMUnRViLgs1blBL2d5fN3Nmk/VM16dMtT2db3kX+wMq1urakUt0OnjIcZ+S2jTbb7VOR69gpsZJuNB5yRIa7ujXSH4BpJWEp+awWiPreersMUSQi6GWiYJTWGxe0DOTc9fF7qQYg4/UNPQ0GUxbycCppqUUONuThB4vrdDW1oe5PcVjVJFqXmMFJBCUfR4dA0M99ATNnOToKOU7QUiSFN2UyxJfZoSQmfLCK82zqJUO1pkXzczLBIUTWFoFpip24WXu1FgozHzKFj0um6a2RCHNKY7XCHaUA2mHR26XYnDLjm8PGMme6FidmqhKKMJCkupmqJYFx+1nizKVsalPyN7Kc5OyV8wVqR5ibBryex5JE44W4PFiT64PqyEZxFzZyhxCZ+TtmKk7uF9jwTz384Ua5dRmdu0Ttj+IIU2/fHoZH64+n2//5TfZ4xPD/7MHl49njG9vve6PmYHjf7nr+vLXof306aXyYgjs8bC2Ttvw+Ujzvzyq/fzPvjUZpQyPl8Xjy7pr8/Z6oHHC8RegXuLcb+umGr7VRdreHxp/enHbevw1jPoN4svdyKwcn5bfFcOfD3Oa4pvn1NHL+OsR47sn4MdOA56n4fPh9acXf4DRir3625zAv4GqHA19vn8Zn/WOL2Befv1P0bzj61cmAAA= -->
