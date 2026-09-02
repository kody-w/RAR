---
name: "rar-cowork-cookbook-audit-finalize-and-post-transactions"
description: "Audits finalize and post transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_finalize_and_post_transactions", "rar_sha256": "60771174cc7876eab0db22638f939f9d55174c303f99116cd4e7d6c0c7cd0109", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_finalize_and_post_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-finalize-and-post-transactions:dfa8ceee2019f1f1745bb10d1d7cf28572f975b17378749f3f5a68bbc6d7b547", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_finalize_and_post_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_finalize_and_post_transactions_agent.py` is
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

Finalize and post transactions Completeness Audit — Audits finalize and post transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 60771174cc7876ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_finalize_and_post_transactions_agent.py` first:

```bash
python3 audit_finalize_and_post_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_finalize_and_post_transactions_agent.py   # or on stdin
python3 audit_finalize_and_post_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize and post transactions Completeness Audit — Audits finalize and post transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_finalize_and_post_transactions',
    "version": '2.0.0',
    "display_name": 'Finalize and post transactions Completeness Audit',
    "description": 'Audits finalize and post transactions records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-finalize-and-post-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '960849d3925b9f07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/finalize-and-post-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-finalize-and-post-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditFinalizeAndPostTransactions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditFinalizeAndPostTransactions'
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
    print(AuditFinalizeAndPostTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOi2LbvV/Hl/aO6L1kpk4J5oiMeIiCCIDLb1ZHFDMo8KNi3v/vbqJlVdU/3uadfvHhWVCbC2mtev7X2Jn9/cro2Luqn1yc1cPIJ56RpEgf1xMn9CV1civoEfhUnF/yfeEXe1onbtUXdPD0/+UHj1UnZJkUOllOdn7TNJExyJ02uwY1BWTTtpK2dvHG8kayZ1IFX1D4gK2rALivToA3yoGke5GniDff7iZN7gEnkJDngUXdp8Nl1msCfeHHgnZoXID/onZFB8/T662/PTwm4fnr9/clLnaZ514d9aEPl/g7oon2nCmCQOnkEKMsBeCAH38ugBnpl4JYfhJPHt5+aIA2fJ//5n6eLU0fNz69f8snj8+Vp/Lfv8kkbB5O2cJp2VNApHTdJk3Z4mVDpxRlGq9uuBtY7kwY4MI9e7iu/cSrKyS/js5/uQl6ioP3py1MBVHBGZb88/TwBDvvyVHfj9cvIpfzp55e0uAT1Tz9/49N07jHw2pEZ0Prl7fH9wRYQfiNNwpvUXwDXeyDd4MvTd8aNn7veo51g5dPLsUjyn+6My7o4B/kYo59+/iu2t0ilSdP+W3x/vTOOA8cHNj0U//n55uTfJtDDoA+efy22BGH9O5YA8ndxz5OHo/6K983//411moAE/vD4n7L7swXQL5Nf/9K2f7XgeRJ+eVoFaXIG2eGmwevk9zd1x9C/fvK/3fz02x+A9f/IRi262rtxeMucPAmDpn17+/VTc7v96bdfP3UlyLXAyd66Ov0znn/m15ucHzz4oPrpx7VAvp6f8uKSTz4yffJ7Uf6v+o+XiQHq1v92v3mdfF8v4weajEa8C7274LuaaYCu3/nx56c/AEYALKm7R/2/Pv3Hf0y2iVcXTRG2E9UruhFo8jbJglF5LU6aifYo6q+qwIviS+Z/nYC7Y7kDiHC6tJ1wtZOkE1APY8RHC4pw8vV/ezfo/Ow9oHPqjGj09g6ObwDt3kZwfPseHL++TLQYiC7qJBoJJ3tqtwMQGOTtKPQOfF32+TzKBTold9zZ0/yIOQ2AyH9Mvv47gt5uPF/KYTTmSw6iA1AWMGyDrCxqp07SYeKMaOUObfAZwCxAlLpIU9fxTpPxR1e+jB4y4yB/+M0DvSPoA69rg0laeED5MAHQ/AxC3xTpGaDj6M3mlKTpxE9AFwA9ZLiBPvD468js69evAODjL/kdjrHJvbk0U0DwofDk8+eyDsI0ieL2Sx54cTH59Psfnyb/NflXq27MRxk70BpuPgMpnU42qixNQH12GSBrJmNyAPC5xe/3P+7BGLXLQTcEVZWESXBbDLh9S4bRgnuE3sMDbB5VDOqHpB/9NrnEwC+TpAXeApXePH/JRxYFIK0vSRO8O/G++O7693jf5YwxaR4+BHEK6yK70d7ycAzm2GBfJnw4+fAUMBfEtR0jGo8d2Q/KIPeDHPTaNnbabyHMi3bSgOppwuF50jXA1JHzV7e+deEgAxDltF8nW3oHul2Rgh+jg27iweoiT8bAPxL2fhswqT+BHFu+s3iZSAHw5qR0aqeMa9DSb3Shc88I0OXe1wPmziQPLpOxswdjjG51fcs89l9PGfT3k8VtEJh86VAYwSf/n6eUUVeK4/YMR2nMasJI2t6+J9Y4S4123scvMCzchN2q5NsA8Y417yj8JU8TEIx6+MedMrzl0p3mjmxdDYTvqf2N/1jV9Y1v0oKMGENc12MWO1/yd7h/Bk4G8WhG5AKFexphoPgQOD591zQG1Tl+/9b6H34avQLSeFJ2LvDMJAwC/5bxbVyP9fTwPEiPYKwtUABe/INVE8AdhB7wnwAlxvCAlnBznQTqAoxL9yT/IE/GAAEt/M4D2oLCCV4m5pjHIBebiRuAqWikAV74dGM1yQLgY6Dih4eb2Cnvyozz7UNBB3A9JyDfvvP/4xHIyLGrAGkf5QZ4Or7TAk9eQAhANfX3uH5o+YgUYJqN2XFb9GOwH5ZOvu9K/xhLDmj4DfXBQD429O9cA3C6zu65CFrtqQFFnQWP9AF5cOvdL/f2e+/vH7q8/tNI/9Pfm/pvDVX/MW6vk7hty+Z1Or03vfee9wIqZAoyJCmD5t7/Pr+X3Wcg5/NYdp+/L7sfeN9d9Tr5e/r9wOKR1q8T5AV+gcdHYuIFY94+PsAd9Oel/Rkfn37J98G3OAPxRQbwZnT/ADD3o6+8k4DmEtVBNBLf+0wztqcL6Ig3eLv1iY9ceNQJQM88GptiU3xXv6NNY2TvgfuAYfAoHwHeH0e6KBg3POmofhM8veZdmj4/5U4W/HsbnRFsQcICf4w7JFA6YEhqk+D2DdgFHiTOeP3jjk6+XTjpPbGbFijq1Dd4eBTKA/eexwk5B9Ay7kbGjpJ/PyCNirdDOWp63/yMg9jHlPbPUm+VDGT4xetY0KCbgon6efIxHD9P3rcrtz1g3oH92q/jYD7aCUjBrw/aj02qGzz99idqPOb0v1AiGcFkhJ+7uYH/DSlugSudFgCivheBSoV3myLG/tUMtz73z2YDgXVQdaBz+6PK33zwTbXirs8fN1Pa+2b096d3rBmv72PEPeXAgr817o2ueW/TbyNzZ2RxG8punrrF680BqTG24+8eReNs8XbP4qdXAFbB8xNYPKbNKHbcgT/dNQKmfBuFAQcAO5+bcbyYgiIEnEDTL0czTgAyvxMw3k78G/148frn8/P/gB+vfuiQXhAEIEiLEAkRAp+5LgL7iE94IUrOCDRcEDMXITCCJPBFiIUzZ066rjf3CXeGE0CRBuRO5jwUmSJjJIAJH+7+v5rrn+48QNNBZ3PAZA4TBAKU8zygxjxwXNh3UXSOkeECW4QLfzYbH2IwFi4WCDL3fDwg/LkHe4Tnwwi8GPk9psq7Ym/vE/x7bO5Q8gYAOEtGtVHH8UiPQHB/QThzL8BgF/MCBAWOwQJ4tsBCkgxwsP5j6SM+Y/juto/ZCwZKMM6dRzm/P+I9ZuQcB5RrvOGp+4eeLgxnjhNuH1tQPQ/s5gjBGXzU+yL3zQ43TXNq1sWa2foHOUKp45aRhg2PWnyWBqLQicuQVwKPJ1V3cT0UNjYEHe4oZ8bjhM0W22WWuLgW2nXHXbF9pV/h80xVHPU61ELPGF4CpyyXNoSizxanTEPUVE9NE68G2VcNaBqeLHJ+0gei2bFgRRIf3ea0YSx9kwVz4ZhbWXfYV8uBqSt2pQpyutb0jV2xLevswQZ711f+zkLmQbiGCcliDUhMIOcsrrFr71TIRaYsVm2SuZkFbJ0fSMO1zNKOT+JJ9uGVRFYEPbs2XaWv+aua7+2BE7GB6735SZ2JfqzsEcPHZVds4CZbzQ76xdwjM7vNWSWyYsNRbFfdV8a8asqCF/x5VRTalm+yxJkNXdPZczM3yDozZ2W3mJ1cxBCUtvUZxeECdrbW+dKuUn29rQvuOCyV5uJohKQn5qVss8avrfNAs6CfnPZuRDGDShykwhVzLtiLBro5HDYt2gzOFd/N8WOzAvs/S2AX0Hljnnw2ao1ThpQrUgm3wCDdX7Y7rtDN+Sx1j8dNkrWZZouJOUdR64BpZG9uLS8SkCsl9iuZH4zY9GqVvbaSfdYk1BWTaxmtl6vwROcQsIQs8oHd8aa8L46wu82MYX9sc1RVN6tMtIx4HuuNxskpdIS7WKtdQW5actWZBsLQx0LDE2PqLpMDf9nY8G7bdBeiz6/xvDKVKu94YRXAfR8w5jYP4gsB8uLM25I4rU206JDUNNLp7iDKwuqkYTnfHzKSCvwK4zPBEzKxobOOOwiU5rbLNLFaaa1a64vnI7CAFFaOH3fTfjVdDq031zs1WUQL3dNmi+l2B9PDIIupUVvG4LummqoBTDDBjOH2+rwmqwPaizzilIqwKLxmwwq7xXR5IritSp7ogrRX7qpnnFnWGats6WhlrHaCotjowpY9+KqWexs43lubjWLirIwVVJsySkdREpUzlXuyTzHr0frRVbNLdz6tT9DBOmQnKXGznaG78d7sEdJB4cH37H5JZYFCCRfmsKEjZ0b3G3NjqJbWnTTRJ5HECtQNFrnnU0FyGO+o22MHp1PUw/30YufDlts1RI3tUqE+Vd45LlZ0VtthH+imwWsNJG843kcqO1tQXGTgxmIeF5B7FjY7uIpXRx7RlYPOXkSzwTlvXlpLq7FdsQvIOhCEdC0vImqJGpfA2xFRUA1bTxwQmgEI3aAbls+1rXRBF5UaRKbBVj0q0lcrK4xuatBnJ0UKr6RKc7FpGONYp5cl4fN8YstBgEAqSaKRsUQPyW7VIEdIZGGkI7fGTsoZptHti7GC9rHhRx21vE6dfXYMOx70id4u0lah2iXCtPB+3807jpkfHJluJXVT7HNTLk4bGZV4Y3pCQY2cLuIIg7vpprr2U9bYV3BGHM72OitdLkIih4AWV0ZjL9llS8wHIT5aPuXsAgWGF8rmbArXM2xaK4THtzssjHp4TQwJ1Xehb9IradCZvrL2J3sXU1C39Mh0kZAaf9aoPrNWjR9tIWQfncRZjpSn+TKdDWFCelOavdLwvk+34VmWyEUAGRenUzRJtQan9NJuVS1W1MFaTg2uYZeNucvwYVfK+9RjKJpJZVpfIHUaoYlbbrDKvXiivhJKlUPYw7HU7TLtdKLK6S1e6MslQpX4dlPmdEwL7ZqnI1mWLwcv0iO/6VihkEIhasPmzIW2eYhPuN2fcgtbELtrAnmNGF1Pl4p3mm4KbYWWK2Zi01y1A8FSOM5Gp4U3PS+QwVAI8XBEVzP+xHtkuF4NyEAGfUlOz2tvGooRCdktwq7PvAPRpkbMa5Q2Kd2njktNxgNV0PSYVeedoe4xQyU89xoasbTZCaFHRAD9OUgmcsxel0OI1eddh9nIUj9IA7WRs/11KewyQpkLJb5KBJ3rKSunofmKb6rC0zH8gq+ctqlyFmKMnEPNfUS0mX4QjCTa7ge60xxlZjZE4oUqBbODU18EnU77FUdiBFe4RpViu6ZdZSUd7D0jax202xUtzKyEjaGYedae8D3T9em6YQOUsySBMXfFxlQ34mLGCse14C2rRRefXLnq/WqDCGkcbapAZPbaNXQB3CRusoppB8ISBUyQDMUeGp+H57GipOuKyWwpy4Ou3K9FZVUVUQVUtElEanUm0/3q5Pb7ZagYkbbeIpaYIYUhw4JIa6v1xkUv+0LmlCOT7umjgQnKdCrBalKtqrFR+GYmUDFVtfPY2bEzTlOzINE103FVdCGvUE7bqHW81bMBtL8VpW2RMLpuNZFmjyfN7PPD8bwhtFKcU9XG3upsGgt5UJULlMQHYymS6nItUDnMm/5VuLI6CD2Ua0eDEdPaDaVrkVy6wr3u2+vBMSLq5FgRKhoS5h1P9pHZYFdTP+gm7mNqTMcSpB7xI7OQq23OX6zpkJz7lVuze4ELww2/NAZIoAqY068C51DTLYfQAmLwTKTP9tvIX5d6ZW6XS3UqKEsykFBxisaiRrSKYMhT6HKWuniK5s6+mLF9nhQrJmUX6FGNIoJQK1FtvF7FhvRYQBjknV3+SDGOynHwdFhiRWiiLi2HxcKda1qxdYl8BQ9Q02AnFNsSh8ReR1XNEZic0ctVHEFRLDaB1tQMr3E2tWaWJ3guLcBMVdgcCu8Y094fVX4FCevjDO8ELyuHXmRXO9mMhlA7sdU891ZmFFFrX1c9R5cHSRoMf0hVKAhNS/XpWpdhitK0LR4k2S7ogmKjtLwyVIkjuPIRxjsa35rlMky0Kiis4YR5p6u6bpq10s7WubA88FRSVNs23CQVDQHgV0tNRjhEznhZmSVHZl0nx7ZGo2PZS2daYXCxh5bn4NhGW3bZ87rMH4BAbH5hxc4Vl2dP68Q6PzLU6WxaW9TeRD5Mr9oeQjaar+Nzebo+Y9iCynQyRRhYbUsqu86udLAe6O0mxWb6Psm0ij0lm1zLmYIqhmZY5edNfbSrdlVemVik+r0WJ1J3OlVDwGadtQuXg4PIq+AotCKTV7ZGcAHOKag+ROr11IPSwvirK4SyfIaMTFftbMvRU2ljs6t53ZBbBw16OU7xmOp3iWli2yLjByHYuMo2l0ykY+uMRwuy2/Pw4soj3Jq7ru2qp+B16QkbAFrD/JLPHAKNbYbCU621PUjS2oLFlLVX8MxGbubK9FpwqVWwIX9Fhql43ZwvCRRwxMF1p5jRNmiam3SHifV0Q5GxRJh+CxqKSZPq8ZJTssCuV6eg8zpm75wqYc6eKD5zFVtt0SWEbK90BeqamrcaR/O0L/H7tSJbOpgk8czaBluIr4QaZfbTY8IXpkCzMoMfKcQQT0EdcRmeJGsI7pnMW8YbnEbkLaTkiZOdvblqz0Dz2yAUplIrJLiyVKpZ10qlXMNQKDJZxjREeXrRzWLRgizfkETGL3Opt7fm6aKE5r536Fna8lPWzlqFabYLqB8UOLR7+MBeq7wXOItmzfUy4LrjhWfWVoJe60NUr/aVEvXLTUqSbZdQLr0JDxcLgoMIz1b0/NDv9aHpvQLeGCm/B226JGdHTZRsZr51nCrge08Rk8q2MDFhmpUxBelqug64tooCD9pSRjWaTZQtx9En0V5VuHcl6Ew5JPjh4p40Ao6F4eo0VK1M1WNHb3oL3xT2BikuMVnSMGH1DFx3m3h3XW8jKfUIFaKMakACHz4LBUh4dIpVgQ/liTVjjh0YS5Job7dd3i8XuT4b1u7FuIZDgPnnFQEx6/MRDpsBjDTndb5cAdTES5EkOVFCljhrTT2LJbn9GZQCjrInN892SuxujYO5oOGq15TKOdgkGAITl5BnqxY/DAa3XyHFrs0wMZ+dL9e0TqmLr6hH7yBhqxSTAh4S8ayXxcslM0T3OIVhlGqOrrUFAOSvGpwQLcp2HX8t27kPaWFEeMH6TMlrp2Onu6ZO1wpMNfMNunC1+byfBkebuJi851dQ2kM7d7O7zAdyig9QdY6UXJ2ekdWUw6hLaDqiC58X8yRSG6JhKGPhWo5uL9CZlC0ECl7kgeupWJbhkLRTN91eQiNrxcxDOOoIHt55/dQ+nlaXjMTA5lqfolcekgPSU1ZYP5wzH2xYqrm6xSpnR19iTKo3ypozEkIMbG+2BF66ChdlC5/PLnrK3Dpmzn0VTWXRBANajxFYfNbPu7UpUtbiklDno+0evFgmpVk+d3pDoPhdbFgJvHOk3rOndLXoraEQ2xINksLhIKQ+doTlOBjUTu3ePicFsPy6Zpgrz1hzXEYx7MwqPnqY7mGY2VlovTaWpgIGR5X1vMxG2/qgg2QvEGh22Ygist/3w7UZoF0XGJolSzOMDfu5m2HMBhKquZ4DPDrZibTfosZGZNyzHBK05JCRx1E7eCFj5zqJ+faoIgZFn48sYmBUYBphZMa5sjkSNc0Mm1iag+aKktqsX+CrQZkf3IAeSkMUcm0NddoJO2OhRGLrIZnF9FFZFvBsdwBtEaabytdCFl1BER+yMGvaU3RGdWDErjmrmSbnsygIPS2Spy2GID12sOyE7fjqnFdLKTlUAWauVb/Jc6tBPIzdr70KgSiU9S4JhmDr0EC8dktI0Mzc8Qq+R8k1h16siLCOkStwy/O1Zf11hEs84WKkd+FkPTDl3s+U5ay+LhtHRmWUlP1lje6arnXasrdTSFwxso/vQSM3rB18OLMUSnTUNiFKdiHC2/NgZBuc2prHaV/4qMGuZrsYX/CAzAgNkFolQLSLR26lKcV1mIvXEbQk+mkx3c4irCeqcyPj5AybrXjKhewDcV73yEC0nMtb+BHs3dFptbh0nJml5EyPZrm1Mx1yUSQ1XBP+2Z/Okn45VeWFm/EY2MuR05i67H1cKUnKJkvb6Tl/dcBw3lsI5aLnjoKkSfGMm3lTbi1ISwDdgoKKGDEMxowud85FKgpC4rYLlbBh5yhVhZFFue6rDhTzh10KrX26LHR4Ee3mkajkZLysTC3LoyTJLBeEbR5uWgmryy7dWQNvVLpI40lHrJGtU/L+cYkH8mq2qTySZufx0Kwv1Can2aYDm+aM5Ay9Ovfcuc4K7qBcl2gGBi8odZ1QjWZaYBK6l8qmzGVhCTZeso6cI4Kc2ZQ6F+Uhs9eoK8WL+HTJTRLlg1nvw85hV/iWf5L2sHTRhIWmlCFnk4aUnqFSYdaINsuLbg26VhTYMAyv2+hQSFgnGukisqt9GTMipdULI6oRXt3AXKTpzhQSj3N+d8zNXbi39ld4nm3qYLc/XxgUiUWBUE8URf3yy9Pz0+2N8tMrAhMY9vw0Hm0/3iz83cPl6JqUbw9uGEHiz0//78487+eP728eb0f+geO/3qS//j1Ff3t+qr0EKHU/km7SLnocdf63093P/86p88hhuL8cH1+U9u3765nWiW4H40nud01bD29NkXa3Y3Hg8q4Z/0imGf+OygO/n27GZeX4xuImdDzjvR23v7XF2/31/dP49yvjq7/AT5w2eHyNHu8Qnp/8AYQt8Zo3bD57C+pytPPxCmw8Ah7fgT398X8Ac6BusfAnAAA= -->
