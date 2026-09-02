---
name: "rar-cowork-cookbook-audit-collect-customer-feedback"
description: "Audits collect customer feedback records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_collect_customer_feedback", "rar_sha256": "d983142857aa1b1f99f2b4ee56dc7013db5397f3d0e3ba761ec66e8a43896f4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_collect_customer_feedback_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-collect-customer-feedback:41dab664e895d22069f324edd751243bda9866d10364efce5f54a9170a4a90ed", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_collect_customer_feedback`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_collect_customer_feedback_agent.py` is
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

Collect customer feedback Completeness Audit — Audits collect customer feedback records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 d983142857aa1b1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_collect_customer_feedback_agent.py` first:

```bash
python3 audit_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_collect_customer_feedback_agent.py   # or on stdin
python3 audit_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Completeness Audit — Audits collect customer feedback records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_collect_customer_feedback',
    "version": '2.0.0',
    "display_name": 'Collect customer feedback Completeness Audit',
    "description": 'Audits collect customer feedback records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ada539dbc4ed7ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditCollectCustomerFeedback(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCollectCustomerFeedback'
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
    print(AuditCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZPiVpbvV2Fy/rA9ZCVakISyoyMeILQvoA2Qy1HWLoE2tEt+/u7vCsiq8rQ93R0x8ZSRoOXes5/fOfeK317spo7y8uX9RfPtbMbYSRJHfjmzM2+2zbu8vIKv/OqA/5mbZ3UZO02dl9XL64vnV24ZF3WcZ2D6uvHiugJjksR365nbVHWeAkKB73uO7V5npe/mpVfNgrwEo9Ii8Ws/86vqzqrIk9gdHvdjO3P9mR3acVbVs7JJ/E+OXfnezI1891q9AdZ+b08Eqpf3n395fYnB+cv7by9uYlfVhyjbhyDbpxz0UwwwObGzEIwqBqB4Bq4LvwQypeCW5wez59WPlZ8Er7P/+q9rZ5dh9dP752z2PD6/TH9qk83qyJ/VuV3Vk3B2YTtxEtfD22yddPZQAY3rpsyAgrMK2C0L3x4zv1HKi9nfp2c/Ppi8hX794+eXHIhgT1b9/PLTDBjr80vZTOdvE5Xix5/ekrzzyx9/+kanapzLZHRADEj99uV5/SQLBn4bGgd3rn8HVB/+c/zPL98pNx0PuSc9wcyXt0seZz8+CBdl3vrZ5J8ff/orsncvJXFV/0t0f34QjnzbAzo9Bf/p9W7kX2bzp0Jfaf412wK49d/RBAz/YPc6exrqr2jf7f/fSCcxCN6vFv9Tcn82Yf732c9/qdv/NOF1Fnx+ofwkbkF0OIn/Pvvti7bfbX/+wft284dffgek/ykZLW9K907hS2pnceBX9ZcvP/9Q3W//8MvPPzQFiDXfTr80ZfJnNP/Mrnc+f7Dgc9SPf5wL+BvZNcu7bPY10me/5cV/lL+/zUw7ib1v96v32ff5Mh3z2aTEB9OHCb7LmQrI+p0df3r5HeADwJGyce+PQZb/53/OpNgt8yoP6pnm5s0EMlkdp/4kvB7F1Ux/JvWvmsCJ4lvq/ToDd6d0BxBhN0k9Y0o7TmYgHyaPTxrkwezX/+PeEfOT+0TMhT0h0ZcnJn75wMQvH5j469tMjwDXvIzDOLOTmbre7wHy+Vk98XvgXZN+aieWQJz4ATnqlpvgpgLI+LfZr/+Ex5c7ubdimFT4nAGfAFwFtGo/LfLSLuNkmNkTRjlD7X8CwApwpATE7pg9fTTF22SXY+RnT2u5oFD4ve82tT9LchfIHcQAjF+Bw6s8aQEmTjasrnGSzLwY4D4oGMMd5oGd3ydiv/76K4D06HP2AGF09qgk1QIM+Crw7NOnovSDJA6j+nPmu1E+++G333+Y/d/Z/zTrTnzisQfF4G4uEMjJjNcUeQaysknBsGo2hQSAnLvXfvv94YdJugxULJBLcRD798mA2rcQmDR4OOfDM0DnSUS/fHL6o91mXQTsMotrYC2Q39Xr52wikYOhZRdX/ocRH5Mfpv9w9YPP5JPqaUPgp6DM0/vYe/RNzpxK6tuMC2ZfLQXUBX6tJ49GOaifnl/4mednoLrWkV1/c2GW17MK5EwVDK+zpgKqTpR/dcp73fVTAEx2/etM2u5BjcsT8DEZ6M4ezM6zeHL8M1YftwGR8gcQY5sPEm8z2QfWnBV2aRdRCYr4fVxgPyIC1LaP+YC4Pcv8bjbVcn/y0T2b75G3/cuWYvt9G3Gv+rPPDQLBy9n/v25kknDNMOqOWes7araTdfX8CKepXZq0e3RYoDG4M7vnxrdm4QNXPhD3c5bEwAXl8LfHyOAeQY8xDxRrSsBcXat3+lMul3e6cQ3iYHJsWU6xa3/OPqD9FZgWeKGaUAqk63VK/vwrw+nph6QRyMnp+luZf9ppsgoI3lnROMAy36xYR+WURU+jg6Dwp4wCYe9Gf9BqBqgDhwP6MyDE5BkA/3fTySAbQGv0CO2vw+OpeQJSeI0LpAXp4r/NjlP0ggisZo4POqBpDLDCD3dSs9QHNgYifrVwFdnFQ5iphX0KaAOqbQyi7Dv7Px+BOJwqCOD2NckATduza2DJDrgA5FD/8OtXKZ+eAkTTKTruk/7o7Kems+8r0N+mRAMSfoN50HNPxfs70wB0LtNHLIKyeq1AKqf+M3xAHNzr9Nuj1D5q+VdZ3v+ha//x32vs78XT+KPf3mdRXRfV+2LxKHAf9e0NZMgCREhc+NWj1n16Ztynj4z79BErfyD7sNL77N8T7Q8knhH9PoPfoDdoeiTGrj+F7PMAlth+2pw/LaennzPV/+ZiwD5PAcBMlh8AyH4tJB9DQDUJSz+cBj8KSzXVow6UwDue3QvD1zB4pgiAyyycqmCVf5e6k06TUx8++4q74FE2Ibo3dW6hP61pkkn8yn95z5okeX3J7NT/52uZCVlBnAJbTAsgkDGgD6pj/34FdAIPYns6/+NaTbmf2MkjnqsaCGmXd1R45scT7l6nJjgDiDItOKbykX3fA01C10MxSflY30y91tdG7B+53hMY8PDy9ymPQekETfPr7Gv/+zr7WJHcl3hZA5ZkP0+996QnGAq+vo79uvx0/Jdf/kSMZyv+F0LEE4ZMqPNQ1/e+AcTdaYVdAxw0VBGIlLv3lmEqVtVwL2r/qDZgWPq3BpRpbxL5mw2+iZY/5Pn9rkr9WG/+9vIBMdP5o2d4hBuY8K+2dZNVPsrxl4muPc2+N193I91d9cUGUTGV3e8ehVMP8eURvC/vAJ781xcweYqYJB7va+uXhzBAi2+NLqAAgOZTNbURC5B7gBIo7sWkwRWA5HcMptuxdx8/nbz/eXf814jxvoQ928Hxpb8iMQ9BIJwMUGTpex6BwcgSdTybXOG4B0MoGBO4PhZgS5uECcgGXxDwBYgDEDGp/ZRhAU/2B9J/NfK/27C/PKaD4oJg+LRhQK5QeImsMMK2YQcOSDJAnKXvY7jnEhCMeg6GkkSAepCPOjaBw76L4/7KXqIrEg+Wk4QfPeNDpi8f/fmHRx64ASRK03iSGLFtd+US8NIjCRt3fRRyUNeHEdgjUB/CSDRYrfzlQ/fH1KdXJqc91J7CFbSLoFlrJz6/Pb08hSC+BCPZZcWtH8d2QZo2jhCOGjnzEvfP1onknNi4tbYmmp4tKjdcp7xtGlpyYzjhVhlUFqoOxuAOB8PRmFDHdhmx2Vf13Noicy072kSzWjNODI9WhbuKFbQB4+fcOmIw6HiMbTXWbKQ8x5Vx7FK1vwyY1QR0XfU7/iREst6UBpz2KApi4ERoopiMmcrzuSnKZn7altxSym5+JVKCRSjwOATyThKJVKpd00CN1LqwJy498Wqsn5RokMdiOW+dfum3zm2Z1sgqGE3svIp8wlCPfE+dK3N5OkICbzckArBWYy601hPihSeisrvpOMyftJaqBV7pl2m5GHaYOxjjUrCiAw8f62q/TxDbUCnslGubdXnD1mQ3MpiRiCElSPU4NwWcKQWFrcqEt+ix5OLGdW63NEZymGmxpVNSAezdGqEeJCQqzyjHxdKqRKRzoZthfWZ28CYkRFTcxNHJcY7agFsIe3BE+4p0zMYNL72Gs4O1PCn0fG7FtenILa8IVw2h5vVuHmM747YjOFfm8TZLKyMW0DO0WbkBA9GVgFCOJx/OZkoubd0oYNFUL8Y+Pg4JcrJafTUe3fIU0865EwpK2a0s9RSIGjUGstGK8twR1bHM2bXoHrdHT0bLSxXkUBhZKzaf1yxnS87JYvaX+TBeJG+0kVw2DylcLxljaEmrCuENDB2EBU2YwoYZGWTXjpVJX0N/jW5GqI2b6rwgWF5b0SMZqY5GX/baple4k1synmfmwYG3WAIkprZ17NsN5lpsT+3EHeE26paQdof5QLOlIjhJKpZeup/+Lxpu3JAN3YwUrdSCKzPEmZ8z1IpjmX3C8LkQQwuEol0su6BzNzizG8g2c/bc1PGAtDydrMY5R0LLVLPsUxZcyx2MVAl8OWBSS6hnJ2F3jHROMbFXl+h40vIrg+FtZBFbAYOkwlcOIo6US4VbicMtlYBNEepm7kSf2XZSiGixEDAYs9PrRB4kXBW2Gz6pfJGOQ5/OlAtVjBkVn5GWcZ3OZHqYtOrVsDrhXcs1vjjsq3hVLs/N4qTEsR5LhHAJMEw4HYFX0AxjOwG6HPpI9NvrYj4P4aEOw+WILMp1t5pXZVtb50A3GeQqO/WZhK6eCWUtY1x82daAgdcXLpnv0P2KpR2z1fgj1HSV6txEjRtveZ7TaoplPCFkPO8UG17FWtLnFrFLsId9t6p3KkYu5vpau0Vdmxk5j91WIiiTlOedIaGcF8qRtsxdElEhRjiguOuLbsd7hGGEVy8Oujo7opYiVAYIutXBQkJsRZ9odjMitJHKYbWVF8aFvHHFRmMJxDvyAm9yoVJkKrUcDpYhIK1Zpvt9y2EyP6yrzFnXlsb3/smU6yYVWMQdl7QtYKMwSg1vWVqytYQyvR0Kt+QrJGwlyGM6XhaaPSbAR9HW6xSD3KE+OzfMXSxdGne2JcopujCaUSK3a7dvls0q0AQPQIZN9svz3imRhdnO9WI9F0qE2hUkYki8NIQRUjtHaUN2l+WgUmVz6Pf4Ia/YdaUcicrqpLxXw1hcokdKTTYOPwTVyl1IaR9Dl7AwIqlHR4yg1XK+xJvu5mkjVy2Q7epgH2lhk6/di2FW14Gab2gHr0DKraoq3R9gLucuGLlWbilzcU2k5ES936wPfaEqy1Rl6uiYsE0seU46Cty22IY7p8DSMN4K8tGnidXZQ3EoKjhcHkc1tOfwwUYJfzW/rsa8WOqp7wWLfbVQRGzoKm1rFYbNpSPRrsibpl2WzVxo5dDXqFAzUD1vrFXQ1ud1STbKedEeDht2UPwRWu2VRcGyQ2RcFhm7PgkMpkLKtjoGaSPFu43FcZ5wPkajqvi2sVsLplum3sEKGbiPhbOl9id4rXqbW2cSVIwL1yPsXU3pApXdpbzqN80qj5yykgaqumDiMdfDdXCzhZzkQyEM9/DRPEl7IWyVXilcueudOTYfyeGQ1XMvvrYX43CLBmU/9+VdIR7xCinc1CTLGBrUZrArmVJRdUlAyzW1s5NaPElVm8uUd1GQpLqFZ6fr417xdbqB1CvZjv6FdtEzgi3Ly65wNkgkClquWEah3/RuYdqLzOEJdQcADUKRfZSI2iZzpF0kpecOammylOC2N/3jhdT2FL6jl0K23Zc6cbwlB9dcw9KVQlStkv0tRYu6TBiHBuJp3FrT8MJYRiVJV1Ggl2nbu8JRXozVdkuuHaXzhR2iLSMEXBE7nqKoJZdVjFsvM811+G61Od2oOKE4Kjz1Vncy6BStFAlx2x2+UST2KCdpJXkYWOAN0BKKOEfZpWmyUQJHbekjS+UdnEm0lwtu6RLVQMcQvdi3TMKdRL4nHbtP5jSHQjf7eOtum7ZCmyQ3Y4dwL9fzZUsj5/pwJlgnaIx1B6r+MRJa+8wWqHrF6LXLG+a8d+TT4BzYy7IIhfVJu9GYxAsVR+Z03Flzo6RjQ1M3wY0HbeMRCXP50N1c+cTPIXd+DfRDUmzqEF3oueuwoNAykKAOkrOnjc243QGM0fRwdNQ00U98EJfVhgA9LJmVcM862Pqiqu7eNTz76AUwp0d46Q8QhC8YfxhJvCw4kth7KBv21SUvLLKhosKOcuMohQxHOnC9UMtQpLVNBbGKs0hC8Xw0zgGxhTRxLRXa0lU1Mjjxvb4cxXSbjXKI8XU1JLqop2jMMVd0I+u6kAh8IQoi5e1AoSOQyLlmXIIO7BzPqG2h9caorL2TSYVyeo601MmxY5lodAzA4aZ5o0Tvb4ebnQkHTA8XxnWzwcIMX58FJi4ymJ7vvHpr5L0bpVcvzaFYSexI1iiv1mgBuXWXc32K1qC3LFbRQojHtWiuhbPIrLawEpKYsiJgkYxgRIbcE1add9mtkx2CJinlcHAZEU00HdF1i9hR2Gq+PZkK1xrRFr4OutxKrOSEF9XyJNLaZWcixLgII7FO2AdIuVfMgArovsJ3aOogNXsIzukVWcV22VCJbxzK4FRQJ5OHnV4xsSW0GuJjctaF1WkLV0yj8I45Cp2E2tnx0s7HUtvuRYVfB4tEMAMQ6pnXO7HiVOV1G6UcK88tL6oY/ubG2ZhWDqXrXtDZYEiBxTwHXY4HyxyPo49r/XgwzLWWEftWdPCzUS6Ox2vIFsU+6LCLfTXyfR4q8Jo+8vpZSuZFgepuCJOEn6hQ78mYcRqKQ5M5bY06hF6bHCxXdFCE0Sq7IAx6cZq5i9id4R79Xbe1QlU02fNJLEBwJXoVyd1WkwtXvBTVwr7NoZgztXV9xIZ+t1bgK3dZUkJjNOlKl4L93mG0xByic8ghhqHseiaVGFaDdzk88i6u6edip2N6cZF2xEbrkuJMD/Xe8OoN7V15lNtdM8Px84N45M+hXTBzUutE6wArW0uVuCBkdzcxO+so2aO6rsKsfdi7R4qupR17Xq5i/iZQO2KRHI/QZiAJq1EE5oInkrOOPWPOHARcu/VLfolC7gY0OCukPxCCYNeptaEUes+xlxo6UCfQ5zf0qRdAe8lIRBReT3JYwjuNj/Nbx9v+1YKSE3ux1IK0zMS5muYlcmE7nkvLSASrvJg1RUkOh9P+eiT3uy6z4Wt8vrKb4lBoCA0zvoVG+rnqwMJOvvHkoMHYuU6vZu6u1KhtiZu0RgTThs5rXO+d80KC5nkj14LDYBjKoGqjKabeD1kmqglSn3xuHTaBvxS3MR+oMVgd0L6zyOCDZsijfbKhMQtufumnlzmpO/qA30gxINl43aKbcrNbEN1SJqo5nqCJuXCpxEWcqmaGsbqs0RPjbOjrNvOaRZL3t+sBWsDR2ewcfU1muZRfhG1NrDyFIvi6t+bBQuJUIkwpLITYqKiXLkKW4Z6yhLg7eXNozpfNfqGrxrYRK9uSDmIuA3PZ0GVbmglWhniA6xUrZz2ZRyPKwp7dEFcmlOQc346r0paxTanzgxeJY1JBe/uyYPRrmu+DoIXoPbIhGNO6kUCO3lix22LUWeW4QG90D/Uwx20toLljpBC0lXsftFcbzD7d8o61cCzaC5bKSUioiSMeQGgKx9HZP+9zltuhfLvjwUpPIge35p0o6zqhd1nxatM32mxUyKeiEZGQLlR2rJO5IAkTSgn1c2ntTD6lgw4AVyznvnVao2qAtkXK72FHknuUDiJ608SnehWuq/mA3LAtUTiZCEWRxonzjGAKbNwXyHpZB0oSNlFjx7btZ+WeVXMfLHew7LQsFyWLNtJO7MQT424HaG0griy1HaxEpT2uxjrlmkvhzxGu0nk8gbaIVGTWXC4w/wQKJdXumxXFM+hROSMBMiIyOj/ozoYDOLMab6qzuWYE8JBLnSkDu2Y7VQa1uWdlpF9wZnuM2XDYdBedxBmCc7gSk8rzQV9Ztkrkl6TPj+uldNvKgZdj0sbQ/LROxRN7cg/4ZgXFybEz2ljglobtLuDDyg/2lsVwDrLujydGUiuIp/TzCt9yK86OMuwU5gbFWg4FPnGv3ws07kYXlB3LpTBGAkaN+6pFIBIN2IBOmi51T5aixElqdY5o6W6eou5yg/U8f4jbfUj3JWwfo/kOx+v2WpRegzLGKqJivV5KfJm1G0TK1sedxC4yjJHpeLmtCMdbjOk81VVfGMhbvhm6I2UVCiqk3dFTS6R108Ymo1vvQAZ1wGBR6mTWJOC109n7SLyyubLV2lZdiwTh7AZpK2wWFDy/7PgcOVyxver3YgLR+h4HWLgkSSTq290aEojg4DNhv6pwlHTO8q7CCTxoMh+Is1wzK40NTvjSEyLsoJDzkaoClwiOi1GQbetUBDrfS/t628N4udeFqlYW6HJNzitNcoe2UpyLXOJG5V6kALS8nKGuFd+47c8nacBK9OBe7ILqmUuelrAl09ByTswjW9ueaUFrxIxYrQx6U8h2V+dnwis9PGnQPK4QO/KXa1SHrvXZ9FV656/ytRIR1mq9h0EVyLaXze1IXU6dJZWnI7RqAgetrZisvXnuNGYobbk686hFIl7ndbdeKlnfmTCp7cjVlRijbr3Fra0ilgeav1zSnjbnFowzMDfmlMxalrC5YGbtkMLl2mBX0Qj2brhgjwczqEk/F4MNSsDnjVjVBO9dWnNAGIQB9djpVpGYJQv1DK0uDeKCFvqAUlKJyttksGLEgNXFNd0Ye4SyRr7O5i29ZhUcczd9yFoDWEjVG81krjdsv5VB7kFBR/ewhiXsNWPs+aAzGAmXGb/XLVTpB7vd36z9oZXM4zG5nYv1ev33l9eX+/vgl3cYwnHk9WXaq36+Jvg3dovDMS6+PAmhBA6/vvzvbWc+thY/Xh7et+9923u/c3//l2X85fWldGMgz2N7uUqa8LmB+d+2az/9kx3kafLweJc9veHs64+XK7Ud3ve3Y1DJqrocvlR50tx3t4GNm2r6JUs1/djJBd8vd5XSYnrncOc3UfXLNnb9L3X+5fnrm5fpZybTWzvfi+3af16Gz/cAry/eADwVu9UXFMe++GUxKfl8hTXt6k7vsF5+/3/BcbqrjicAAA== -->
