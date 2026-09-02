---
name: "rar-cowork-cookbook-dashboard-develop-order-management-policies"
description: "Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_order_management_policies", "rar_sha256": "1d450ec284c842e9b180cec43bcee81190759c433ef5453f0ac544f4b193db35", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_order_management_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-order-management-policies:26a97977ab4abdf13f560b8fc8449db589467e2b5e158064ea347f36655042fa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_order_management_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_order_management_policies_agent.py` is
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

Develop order management policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 1d450ec284c842e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_order_management_policies_agent.py` first:

```bash
python3 dashboard_develop_order_management_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_order_management_policies_agent.py   # or on stdin
python3 dashboard_develop_order_management_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop order management policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_order_management_policies',
    "version": '2.0.0',
    "display_name": 'Develop order management policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-order-management-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bd3040feac9114e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-order-management-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-develop-order-management-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopOrderManagementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopOrderManagementPolicies'
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
    print(DashboardDevelopOrderManagementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjWJblX6G9P0Rky8PFjvCyMhtAG2gBAVogI82D5bGIVWwCcvK/z0OSe0RWVnZ11syHUVi4C3jc5dzl3Af+65NVV0FWPL0+acBKkYUVx2EACsRKXUTIrlkRwV9ZZMP/iJOlVRHadZUV5dPzkwtKpwjzKsxSeLtSZG7tgBKxkBLE3pdhsRWmwEXCtAKF5VRhA5ClvlkjrlUGdmYVLuJlBeKCBsRZjmSFC/UmVmr5IAFpheRZHDohlPgFyXKQllAQNKtD7CK7lqB4RtIMmRI0hVgO1FsiKQAuVGd3SBUApAnBFRQv0E7QWkkeg/Lp9edfnp9C+P3p9dcnJ7ZKeOpp+m7M9G6HPJix+bBCeRgB5cRW6sMb8g4ClsLjHBTQ/gSecoGHPI4+D84/I//1X9HVKvzyp9evKfL4fH0a/ql1erOvyqyyguY6Vm7ZYRxW3QvCxVerK5ECVHWR3pCEeKf+y/3O75IgWn8frn2+K3nxQfX56xMEqbCGaHx9+gmiCfUV9fD9ZZCSf/7pJc4gIp9/+i6nrO0zcKpBGLT65e1x/BALF35fGno3rX+HUu9xt8HXpx+cGz53uwc/4Z1PL+csTD/fBedF1oDUSh3w+ac/E+sEwInisKz+R3J/vgsOgAXD9flh+E/PN5B/QUYPhz5k/rnaHIb1r3gCl7+re0YeQP2Z7Bv+/yA6hjVRfiD+T8X9sxtGf0d+/lPf/rsbnhHv69MUxLD6CsuOwSvy65umzISfP7nfT3765Tco+l+K0bK6cG4S3mCdhh4oq7e3nz+Vt9Offvn5U53DXANW8lYX8T+T+c9wven5HYKPVZ9/fy/Uv0+jNLumyEemI79m+X8Uv70gBysO3e/ny1fkx3oZPiNkcOJd6R2CH2qmhLb+gONPT7/BVpFCb2rndhlW+X/+J7IJnSIrM69CNCerKwQGuAoTMBivB2GJ6I+i/qatxPX6JXG/IfDsUO6wRVh1XCGLwgpjBNbDEPHBg8xDvv0v59ZpYc+8d9rxR4d8e3THt1t3fPveHd/eu+O3F0QPoAVZEfphasWIyikKAlfBDgp137KkrJMvzaD+1o1v9qiCOLSeso7B35Bvf0Hf2030S94Nrn1NYazuXb4CSZ4VVhHGHWINvcvuKvAF9l7YX4osjm3LiZDhR52/DHgdA5A+UHQg8YAWOHUFkDhzoA9eCPv1M0yEMosha1QDtmUUxjHihgUELiu6G0NB/F8HYd++fbOhC1/Te3MmkDszlWO44MNg5MuXvABeHPpB9TUFTpAhn3797RPyv5H/7q6b8EGHAvniBh1M8BiRNHmLwGqtB3AGaoJxt9xbNH/97R6TwboUUhqssdAbeKwa4vRDagwe3AP1HiXo82AiKB6afo8bcg0gLkhYQbRg3ZfPX9NBRAaXFtewBO8g3m++Q/8e9rueISblA0MYJ6/IktvaW1YOwXRg3F8Q0UM+kILuwrhWQ0SDrKxgIkMudkHqDDRrVd9DmGYVUsJaKr3uGalL6Oog+ZsNRQ/gJLBhWdU3ZCMokPuyGP4YALqph3dnaTgE/pG399NQSPEJ5hj/LuIF2cL0LJDcKqw8KKwS3NZ51j0jIOe93w+FW3AguCID3d8S+Fblt8yb/suBQ/zHieVjSEC+1jiKkcj/p9PO4B63WKizBafPpshsq6vGPRcHAwc193EPThs3a26F9X0CeW9W7238axqHMH5F97f7Su+Wfvc199ZYF9AGlVORdwCKm9ywgkk0ZEVRDC5ZX9N3vniGiMEQlkPrg7UeDZ0j+1A4XH23NIC4DcffZwfknp9D3cDMR/LahpAhHgTiViRVUAwl+IgQzCgwlCOsGSf4nVcIlA6zBcpHoBEhTG3IKTfotrCU4Lx1r4uP5eEwkeX3gLsIrDXwghyH1IfpWyI2DOd1WANR+HQThSQAYgxN/EC4DKz8bswwTz8MtIZYZIlVgR8j8LgI03ggJqjvo0ahVMu1KojlFQYBlmB7j+yHnY9YQWOToV5uN/0+3A9fkR+J7W9DnUIbvzMG3AIMM8EP4MDmXiTlrV9Bto5K2AkS8EggmAk3+n+5M/h9RPiw5fUPm4jPf22fcePk/e8j94oEVZWXr+PxnTffafPFyZIxzJEwB+V3Cv3yKLkvt5L78r3kvryX3O9U3BF7Rf6amb8T8cjvVwR7QV/Q4dI6dMCQwI8PREX4whtfyOHq11QF38P9yImhGcIGDav7nZPel0Bi8gvgD4vvHFUO1HaFbHprjTeO+UiJR8HAzpv6A6GW2Q+FPPg0BPgev48WDi+lAzm4w3Dog2EHFQ/ml+DpNa3j+PkptRLwl3ZOQ7+G6QthGXZesJTg1FUNl+DRxwQ2HPx+S3krMtgd3Ox1qDXIjXBafkY+Bt9n5H0rctvmpTXci/08DN2DSrgU/vpY+7FftcET3AVWXT64cN9fDbPeYwb/oxFDiUGLbz13YJVHzQ4a/yAEfvF9UPxRiHz7YsWPxlFW1sCokMgf5V5CO104ij0jEEpYhtmNGmp4wx/VQD0FuNSQw93B3e/4fXcru/vy2w2G6r5J/fXpvYEM3+8DxT2Bhg3svzH/Dei+8/bboMMaJN2mtBvYt3n3DToaDvz8wyV/GDbe7qn59AobEXh+GiAtQjjE97d9+tPdMOjR90kZSoAt5Us5zBtjWFlQEpwC8sGbCLbDHxQMp0P3tn748vrn4/W/7g2vOG2xDMswlk1atuthhEfRqD3xnAlJsq5NTViSZgBuUwCjJihNAosgGY+gaYpCSdyzoD1DdBPrYc8YG+ICPfkA//9m+n+6i4IEg1M0lIW5JIUCB5+Q0D4csDY2QR3gkITtADDBMBZlKBYeEsCjSIrwUMuhSNIjbYwlXJugBnmPofNu39v7gP8eqXu3eIOtNgkH63HLciYOg5Euy1i0AwjUJhyA4ZjLEAClWMKbTAAJ7/+49RGtIZh3CIaUhvMmnHKaQc+vj+gPaUqTcOWSLEXu/hHG7MGiccZWA3tU0MAwT2PRDvcXy67Xp+ORvcglaRlcMjX7cp7tC0f0Ik26WOSZ63MerwyLU1DNK6NRS1CRpMWyGK1V2+AjMnRwW06Vhuovi3DFZ+y8AuGeP+hyACz7dJYOuHju8vxwyQVzLhrsCq8DcLDX1mQxAh4xOY4tIyGOl3rDmEU/Hl9j6hLrjsmm80RdLxzzcilrrZ33tX41tiQ4CcV20nhAWRwvs8ueFx17vd7XWH2eCzoW5ri8acaNlLZnxbEwP1dFpkBDvMBIydWI2dmdXq1Up1iQLkesomOj4xYf12us3U1aQGKxkU1qco+zh7g4HifVujGthWn34UXrs8WJPB8jLLZCgjRjXTwsZdYDO3yd7INrYJbWekWjx6lPNprAgwSTtKZIpnixOwRFlAFFXB0cId4q2QorMgPbS1q1d7OTXh0vTcaeOKrN6IydFIVFzTun2mwEtKO566XbuyRx0XfzuBL4LlWKktNX0/M6XmV7XSDM/pAndItRC+FcrN15Ysymx5E8SoJNDlab4FRUgXZBcWJhSpe9HvUUfq0q8WyyeAU2LMHJQrIBsy0jKowxS0Sbc4kkw6zWLNGiJVPtQBmY3uSnBUavm8rMTe3oK9NeWarKbOuc23TrTlxOrmImJumuNyc12HKdQezXaN/Bmm6MHck413llVktxUtopR1lVZTRCzgilhC0WSksY6FmtV/Jkk3TVtlwzQtc1ixyVLBFvD2Pz3E1CJ9Wigs5j7dClo/KyPfm5V64seodKo1jetgJfOV1wuKDyzt56I8aySuboHnBzdOyOuCGbSuum1lmeqpNglcwj25hvvNN8Y5+2m7peGUGtZIS8OG1xx2lxy/O9UyovS0MhfdcYHczET/vDmJwv+ovpjfspO8vqs8DOTNyueUnGmpWhbvPkcEiw1Iia6UHLyoO9p8ti3zo2WGrHjRWbYqDSV3+0WYvYGvMEfSHAAHWavFBPZm8Zddce+l137IL8RE0CDfiHXo3CVdbtpMjMIkbU3XMUit1CLeq5j5rUMjnoR4zZXH1HV1u6O3nCqpMbQkwS37Ddkyk1c1SzKBCVaKkx0zVerdtF6PZpvlWuigSSVePjwslj06Z30UCV6TE9GrPyZlkEGBFdNl7ejYNmg53axGmC6znu9Wu6wMLDdrGbyBtpQYOtb50X0iwgW65krxN3e3DltJlv3EVf2lhYSBNpB47KoVQFBm45lsTc7I1oQhMbqdjonCTN6EUxcaQ+XizHWh1VnbtjUGI9yevFfkltLSEsiV3K6PHS17bJuc3zuZXMtD3W6VZ23peVhJ5nqzkDAopVDZLRmERNjDrpFmM2kC/kuufaEQMaJYrq2f6MNe2cD4XAtU4CcWxjtp/i3cxIyUm5wzNxzxGr5Fj7FUNMBVfMw25FTZMy5VAUNY6ydfJOmypeerVRjmYrKkY3ss9m++sKNKy1TZZqYacwYWmQpbrvMKPJ2tDVa8ptmAVG7Nq07hyF3aEzNgwTc071ZLhVR9FkzBQeulHlZaCvx5sJs9iDmk78akE7bSQJCsPLW1nVloWknBNR9qkt3+IzYlbMDH+kzWNLmCuNYJa9grO7ySZmz1kfq7UCUqpkQase6oCMq/1mfohLk5jy5FKaiyKv7Q/NbHoe7zRDmm1WGmmf1oIqaCdeHS3aXq+k41jdbeTuurty1VSPiot6XCQcE2uY5E4jdsM6pc8dpoZTT9CVkYjiuOMy5pxW+EmcixFWMIuj1sd7NimZjTuaMNrusu+j9ARZSe5h5236LIpghnezQqq9tjpk8bKv6Hyf9OiKH3frQKLnY2+u8BHcQCSeQZgqv2zWp60yDq+mo8SZlHpEQ05mTbB09l5YFaiFjkaFha3FxZY/t7pFyoa0Jju/FZKTRkUYr66BNx2v50F7kM+Bw12YhOGOuzVm4PoeW+jGuV8W0UrU4vxI1Wo+OYv7SSGuq1gnohG6L/bmnsKu5EEuLg7RhywJVuGJgc0mYPxuybqVnzDoeMl7kODUhWb5EjlOfLo5YyBuzESOL/u24ebW+FRNVZ9OFI27+OZqQzmdJfrCcbxcHLt4m2zt04y3MCs6jGVIqih53lngVOHbmrPNcwP9siIgX2PdFiLTIfCRUF8TJiB3UVGRe4aWW046thMy3WDVenbl95ZBuEVz6aY0QYXHa+Rfgowzk43s7iEuHTljFqqST21sK8rj2mR8XVPQOBdnpOnuRq64KFQykPbZTC1bd+roylQ7KrvmTIdeFndezHfc1Ck3fs1RWmfSva+bSQXplqxRybwkO75SLhc7XeW40PspD5lDm81VVfEgPoBdWJVQXAQRNVvfciO6x3mKppb67tgIwIpPK9kTj1sm2aVbE3AeUVeH3UjrKm28KmyyPKdZbcGhHcuu/kmeHsq9b1A4iS6yZUZINBa6u+lIhdlwkvTVAe+LUaqudNSE+xzzsijw5UJAZ3KwSbswQgm5Qq3Y0EpyRxhzKiGrrjyqkpgtdlGtiaJw3QTTbGydFAI2+dO4Eo7J0uDoajsekVWFnsd5XS3VbhorhSlwhrKqI5VAc5SO80ty8c/c9QjOjI1S3ghfCD1k2+x6EpcgDD27lCj2nGchYNVz6pJ1cDp0hacnbIJlF4lEYzgvUhjqd+52eZ3JcjvfEgc/FnWey/wtnhJ2wpfBksOKKWUV0427Y0eSOqmLeKTGmHaUaw7AwczPXKU8XtpTVh9M8rxeLbbHGOZOeZ1P5Umy8cM8bRxcslC7CXbzyrMwoT/YGjXhdns+cLYTrKEszmR2ulo4rOYfx1Kd6RoxhbvwtVTa7E4/klIqwEoMjkIEIPeLroNH43B9XGutbmx5MUjJHb1TTGc/Lq95m5BwAhyRpcoZs3Xtu6k5BysVD2sxdqZNX2kr3FJFO6ZETj5GIi1eVkkXZqymB9qiTtW1haKCgrZFuCo5O9xufLG12CM2dXl8FR9y09PdQ25HOZ7PV8Shsg4RtSqiwN2I9jg5nBuTVebypUDVDM4LE3JDxieMxoMQ97cVJMwp2c0tOP9uUKJILUNqMMmcHiWTkasMJfVixJ3Z0GjmR4Lpz9a5UYSpFKrNSd2QDkWL2iRaStduPhXpcyU7TF6veC5JDvFKw90kLyvutKUdTvLtjGV6N22FUY5aGLiuKOyMssvlnM6slcTLRa+WF2O3k7QVlqNptz2Y/m63Xc/OS38/2xF76bCNc6sWA83XVutaWCRpfdhjplX341NXkfNrN3PPblzU8s6iqRFnWop7TXbHcaViXqeuL6k5vaDzkkhow1cXeuOVdMOv5IjJ5Pa83zGyPKupSNyACvD7Yynx3fKU46vDPo/aqcsZflec3FCYtkSwmDcKP2lDkXd4tlYBJh70lLmQUqwJ2cwznQm9knGtZNJFpIzqLCEqUfT3xg5dc2uqv45phR9h8zCbO0TDi5i63HVXRUtZrTTE2WZJzaMEWOk+7nJBKDYz35jy/qo8C/xRaMttapYRN9r1MM/XUQdnthEEapGHVMYd9t7U6q/9zo3U0WjkXIWLKe1O+7wJQhpbL8/0ZnbeJVkzNew2EA3SZfZ5tbqeNxcYE6uCY5LS2/Q5nPqT1uCbZsdNVmFxKai9Gs/23Tq9KMe0SOGoH89c4dCTmWfP3IuKlv0aEwhhLJDXceT0LX2gjiPCSgNDX5+I89I8qeQG8wq9mTRu65yu1IbJ7KVwrXpjAvPtvBMFK3Xnixql5jFnbbs8myR13/jKTFWYo81s4Th7Kkr8csatRpwlqB5IdmJFmKsIyjQkepPSsUAkXMtU3bhUQsYMqKIRxfn2ihEagSspEa6uOp0UAlHvvaR25eVUJXYzd8TElp24aWFYy7bu3EYunbJc4tloS7Ys7jIjlKbHS5Ecbz1vHJnKFUZ+T1rjUemRF+dEbJnLMj14hMUTmwL1pZ5nAg9yZ+1nk7RRm73WFYurPWPipCMoAUZ4ztHqqDfqxczXNi7swS0bjHhpvTS3ZCZnjJRWJ3XikG192qUUUSZqI1WuHB9hy1/KWFysYYuIJG/tsNS5r83IKLtqNlXWtDzJ+rVzXB4mctR44bqBPKGPQtIm1iu+65JT2/ITQMBBkp4qSd7ZJXrW9lt7eRG8Bt+xFTpf+7hpTWfeJavx1OyuWGQzyUVhTDcRxzTGprzfFni483b61uf1/IrT45Ckl3WqMAC/hMT6UFQ7ZSWmqu8e92e4hcGqsRSe6Lg+9QKf994lBFucKYuz3UQbDNUjcuHV7LS1ys3YoHQpZHhDO2qKClBKMc5zuh0vTtlxMvN3W2Y9xag5s7V3cQiKvCULzrt0yux4UlvqwEzJOZ1sFXCVprO0PParNDwBqaQm5LTVStPTtJnop64nnSejKU9R46UDrqM9j4n57jgam4wR+xA/jU9WF361W7sEH/sTcjFrXf609vqRv0v3thjI43Ev0v3RDw13zNekhZtMta4SgUhct8f8sq36rbVWchm3qQLfb3k52zIMgIPlNY9KADsDhruETDuLMeAF/Ohko4bnIde2bNHCjfKUI0iy5CPnNDNTwqtYebIwqtYucv/gr4PMkUe5RXkmVxANMO1Y13VPwtljqO9ltjYPW5VymHNF1st02keiEArjYsUxRMaE2oLHuEl7nuRHlcZUkVbU0USKl9hBsZTTgqfUuq1qcsdeGUC5853uyYzN6HB2AHQ/ZuozcEZLVmkbMiDqkUfoItjrjVFfmcW0AXiDXs4mnuyF7fq6xVljudCLPcApN8HAeMc07E6djmKWZxSzHO/m09LUW56I50t/mobZua4SY9wXy501tvrWr05LZdrsLnjBRh5/MXhDWumjoiBpy2V4deYeqVBY8nkDuw3hLerJse4JfnvNIv7C7mbSYdSHfkDP3GUkTNH9QqjnHBFIMbPYXvjLgW84xt+wtuE1J93VwHm5P8+4NbdUx4czLS/3M0Ck5EgQqCq0JmeWCihRQA2hngXXqvL1eLLYLw6wyGw/z/h0GotRq04ui+syVumInTF7JxaOoJ/Km7RwdB0w7XbiAW1FrWU6JteUvVXHiRSAmpwcRkncOAUswYZ2imY0zxK+X1+oVaeN6paZmwePFbkD3C8ETsdQuDHqpinr1Fy7WzvUMdVpLtictd1G1eoeVTTFCEltb5oSmbFxc+Jblt7qiczRPHGgSDJal0BRvXV35dD6mnMc9/en56fby+KnVwxlCPz5aXhl8Hjw/28+Lfb7MH97CCUYgnx++n/32PL+CPH9ReHtNQCw3Neb9td/y95fnp8KJxxsuz1qLuPafzy0/IfHtV/+wtPkQVB3fxk+vOVsq/dXKpXl3557h6lbl1XRvZVZXN+eesM41OXwJzLl2+M1xNPN1SS/vdN41w2/352qsjcHnnwa/nxleG0H3NCqwOPQf7wqgDd2MJihU74RNPUGu+fg7+O91fBQd3hx9fTb/wEmqJerHigAAA== -->
