---
name: "rar-cowork-cookbook-dashboard-revoke-users-access-to-systems"
description: "Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revoke_users_access_to_systems", "rar_sha256": "c3defef3a3d361ae88e7f4e202bc09ab8c1f793e64ec629ec1d04917cad23942", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_revoke_users_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `dashboard_revoke_users_access_to_systems_agent.py` and in the RCI capsule.

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

Revoke users access to systems Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revoke_users_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 c3defef3a3d361ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revoke_users_access_to_systems_agent.py` first:

```bash
python3 dashboard_revoke_users_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_revoke_users_access_to_systems_agent.py   # or on stdin
python3 dashboard_revoke_users_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revoke users access to systems Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_revoke_users_access_to_systems',
    "version": '2.0.1',
    "display_name": 'Revoke users access to systems Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-revoke-users-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '601d027a2f7368ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/revoke-users-access-to-systems'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-revoke-users-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRevokeUsersAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRevokeUsersAccessToSystems'
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
    print(DashboardRevokeUsersAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166bOiWLbvv8I790NmXTOPTIJkR0VcREUEBEEErKzIYp4HGWSoV//726jnZFVXd7+uG/fD9YRxRPZe8/qttTb++mK1TVhUL19eVM/KIdZK0yj0KsjKXYgpuqJKwL8iscEbcoq8qSK7bYqqfvn04nq1U0VlExU52C5Xhds6Xg1ZUO2l/udpsRXlngtFeeNVltNENw/anUQBcq06tAurciG/qKDKuxWJB7W1V4HNDiBRQ00B1UPdeFkNfYaK0strQAXINEB2VXRg5ScoL6A1RizeduSe5wJe9gA1oQfdIq/zqlcgpNdbWZl69cuXn37+9BKBzy9ffn1xUqsGX72s3yRR7kJokwz0neCpUB8CABqplQdgcTkAS+XguvQqIHgGvnI9H3pefZy0/gT9538mnVUF9Q9fvubQ8/X1ZfpT2vwuW1NYgLALOVZp2VEaNcMrRKedNdTAFE1b5XcTAkPnwetj53dKRQn9ON37+GDyGnjNx68vwECVNbnh68sPELDo15eqnT6/TlTKjz+8pgWwxscfvtOpWzv2nGYiBqR+/fa8fpIFC78vjfw71x8B1YfDbe/ry++Um14PuSc9wc6X17iI8o8PwmVV3Lzcyh3v4w//jKwTek6SRnXzb9H96UE49CwX6PQU/IdPdyP/DM2eCr3T/OdsS+DWv6IJWP7G7hP0NNQ/o323/9+RTkEy1O8W/4fk/tGG2Y/QT/9Ut3+14RPkf31ZeylIu8qyU+8L9Os3Vd4wP31wv3/54effAOn/Lxm1aCvnTuFbZuWR79XNt28/fajvX3/4+acPbQlizbOyb22V/iOa/8iudz5/sOBz1cc/7gX8tTzJiy6H3iMd+rUo/0/12yt0ttLI/f59/QX6fb5Mrxk0KfHG9GGC3+VMDWT9nR1/ePkNwEQOtGmd+22Q5f/xH5AYOVVRF34DqU7RNhBwcBNl3iT8KYwAOtX33AZYBhAkAoZ9rgPxP3l4krjwoV/+y7lDKgDHB6TO36Hw2wMGv91h8NsD1L41xbcnDP7yCp0A/aKKgii3UkihZflrbgVe3ky8y8oD+253AGy8zwCPPk8fJtD85d9l8e1O7bUcfrmDf/RAK4XhJqSq29R7nbTVQy9/6uaAeuH1ntMCRmnhAKn8CCDtJ2CFukgB2DeTZeokSlPIjSpghqIa7rSB9b5MxH755RcbSPc1f0ArBj0KSj0HC97FgT5/Bur5aRSEzdfcc8IC+vDrbx+g/wv9q1134hMP2arffAMk3KvSAQK51mZg2VRUgOqWe/fNr789jQzI5KACAk9GfuQ9NoNYTTz3zeLqjv6MLgjI9oClgZWzsqgagNdQ1LxCnA+9ywuYTrcmRA+LuoFcD9Qy18udqUxZQJ13S+ZFA9UgIGt/+DTVwjvXX+zKuouYgaS3ml8gkZFB/SjSqUBWz3oCNhd5BMz/Hg+P7yc3f6ih1RuJV+gwRSdUWpVVhpX15OFbD7+AuvG2HRC3QEHtvuZTvfQmU91T5WEesAhYxnm69PPkc9AZZAAX3PqN932NNVW5073aVV/z+pkGVjW5wgFlATAN2sidisPfniFVh0Wbunf7AUnvlfzhBffplXsMKv+6Y+D+vt94r/LQ1xaFERz639irTIrRLKtsWPq0WUObw0kxHwafpJsc8+jUQL9wF+WeXN97iDcEegPir3kageiphr89Vt7d9FzzALe2AjIotAK9aV/d6d5DeArJqpqC3/qavyH+J2CuO7wBL4J8B/kw6f7GcLr7JmkIjDZdf6/+d5cDI4IgAWEKla2dghDygSFsy0mAVNWUhk/3gHj2ppTswsgJ/6AVBKiDsAH0ISBEBBILVIW76Q4FUBNkoF8V2ffl0dRTlQ9vuxDoa71XSAeZNEVTDdIXNEbTGmCFD3dSUOYBGwMR3y1ch1b5EGZqhZ8CWpMvigwE+O898Lz5PfbvskziA6qWazXAlt2Eya7XPzz7LufTV0DYbMrW+6Y/uvupK/T70vS3r/ldxvcyAEAgnar674wDgXgGkTmh7oRhNcChzHsGEIiEewF/fdTgR5F/l+XLn/r/j39tRLhXVe2PnvsChU1T1l/m80clfCuErwBB5iBGotKrvxfFz498+3zPt8+P7PncFJ+f+fYH+g9zfYH+mox/IPEM7i8Q8gq/wtMtIXK8KXqfL2AS5vPK/IxPdycc+u7rZ0BMOJwOU2q/FaW3JaAyBZUXTIsfRaqealsHyukdlYE3vubv8fDMFgD6eTBV1Lr4XRbfqzPw7sN578UD3MobwNudervAm4afdBK/9l6+5G2afnrJrcz7t4eeqUyAuAX3poEJ5BBomJrIu1+9N0/TxR/HwHt2AVhwiy9Tkn2Cpkb3E/Tes36C3qaI+3SWt2CM+mnqlyeWYCn49772fca0vRcwvDVDOYn/GI2mNu3ZPv9ZiCm3gMRv8PyWrBPHPxEBH4LAq/5MRLp/sNInYtSNNRXyqHnL8xrI6YK26BMEHAjyD6QUQMoWbPgzG8Cn8q4tqJjupO53+31Xq3jo8tvdDM1jvvz15Q05nj549pJgOUjRz/VUM+cgWAFDcP0IK3Dvv91lPukAzAPdDSDkYGDA9XzMwlyMQCxvufRIH/dQGLUdmLLspYP4JIV5BO45BEp5DuLCOIWQjuWiGIWjgN4jSL9NDUI0yebBvodRCOoAiuhiMa1GLcq1cNKyXHi5JGHSd0FZ+L41AYD5VPih4GTN94Z3MsxT719fbAIHK3d4zdGPFzOnzhapk7YS2lRFeObFmHN2pBGq4duhvfeQne4cNsxpVbGk4m14ck876vlw2nHm2PAispaP4axQqCRGMDmJeK0ckqjT0eAic/k+Id0ZuWs9R9pqhkIIOn5OPeZwrrTstqk3SDEWi9izGFnPYvgWW+Hi0qqIeaCcmxzpsrclUrX0FrMRMzAqrtDr+YDEa+kgRfqmG89K0aqLzSidB7PpauOa2cjcbaTMKjdXld0uDWENp5VrStYmNQtq5g/CDdfOpUIvqKTARr7btAs7UppTb+1OA3nIqxp18i3qyughFyLKmfdtx3SEavM0FsfnrNTL6+HsqHXJmpcKC64MdmUxONQ1ND0xJO5tT3zj2ciCZMz2wuyY7aYvxEbWNGmNDHqtx+nCrl1hQwrZCheu+mVPKlnpDpytXrrtyZAERdurjeYWxlna+WacWOs8qs14R9ysXGvUdJHRqS1s6ZEbsGGzgBFr4LrG5CTtgvhHRuEdHS7PzNXUSdZMa8rQPSVIkL5VR4uhD3J8K4vT3oiuToUMg2JhOqarTrOyzktsJ52vnC76Tdgf0Yodg3xr6kRxSvB5E/BmVq/QmRUj1Yro1TaPrOutYq8Oyc91jItmiJ4mvE4vZXHmbq5HpJdZhx0JInANwRB6JM9GZLkkVknWmliVpiiJzcJt3GC0PhJLJ772jZ+UekPhLVNiq/rSsyy+0cyuWZsFOQInGHpXO4LMzywplDo2k3Mqk6qBG1w+v2kaobfarU9XM49JZ92lKZkuX2h4vuGkCtX4mjoRmzU/x+b2OeZR8eqfaoKJRmaU5kJNarMgUDi1DWOqqrOqErMGvKtimSkFQl3y83a2rA/AOiW69YNgnrBGbcp44JuSYmfHhD/Ly90ijlz/hsUUvzRXhz28u5k9J+Ywuyz93NUH8VYUp02OO2km7DVEqvgDbLDwcexjtmzVrabUWzlqh606M47JPMhTYoDzHXd1Fvlyd77wtQiHyXVdGXKgkehGGA4Brob7Y1lkzKnJmkEkFF4dtx5XZRVbLFINabzCwZ2T0nOo4TNwJ91IfqY71u5wXOyNraRa/WnTelrPxxsJNeqVkY7Jtd+JUrxergcDwDK+DxJ7ru9EO9D4Czqbo/4yjgL3bFwYNQ2XRpmxFK61B+TixvjGWweHJNFD7ZAb3dL0JBg+BTlo348cghXsiWh5WPKX9aK1xXFs1C5dp9ZpgdEdk4pWvb5YETKifkpFMDtT7BmNZl6y2cOLjWFiuVGJ4nLhXbFmffGyxhrdJZwLdC+eBXM5yC4Co/s9umUEF4fr0CQ2nobsjJ3nha4+LtjddT3Csnzl8ZtZLM5lJpRJJM+1E98ys1Y81ReEWiRpF8XLUVYZOjlvsTPMEiR/u2oe2gFb5WlowSEzz7CzmldC2/YdpvKGeG25fSV0dSqySJ6sBGQhKE5GRWle9wbf9gqcuHRElwsf4VDTZQ+tH+3HCxE1h9V4G4N2f6CjQD5Jdntl9tSw6nyE7U4EL1ySvJJDVae6cjGncD+aL8hmloVxYfTzq8ostx2pd1qCjQdJbBWGvB3EOOSk80KsenSDbraRKJiEMouw8GirTl7xNx89mb10wcqcs4/DzDOWqm7iGmGTOX0GgXEp7ILuDyeVlmm1Qtjh1tn6iueC3ljHmrjd7Xlm02/sY8pjlE2mNEeuVnTBXBuJb8uNaTnr8ixo4bVVxbHvnePmetAYcjy2kQnHhLPVcIdaDHi4p7PGIU+dIKUhKcXwgOW7q75Vi3lRbXxfjpeUh6UzJdqv+ouqS9INlIskZU1rfrZA/YJjc4P0MMGLnTxfbOkl2XoF6a6Clk+YpSeLnQ/8rcpIuZz5ieH3PrPCS38raLS99WaHk5kEW73jBpAru5xnBpgT23PE2VJGH04H98YiOBPLnEer1vocC8stJtr7dr1OEM5BSDwqkoJQSkG5yIFzPnUZt6NI00Hg4iJbFx5WN1SpLehZnt6EUD+78GyLwxVdbWZEwulczye6rskaJQWUdbpi2NXuVAAnrLhkKSeSMxhJHSKr9AyJztRQW2w0T8KZxCpMaZ7P1N5smTiHybFdcY1C2lkts+K2v1b+7jqcD3mZrbuBqvtmMdqWTuFByasFgl90KuQo/0Y5oxtSeHQsD7qN5/CwKOnBDdgTqvC2JSr7YobVWUSJkdTI9s5ZXbMzbTcXwpgdEukQRAMTknwGxpYwY2Bb29t9qdhduIoOxCYoYwZdXLYbrSxEQ0o3pyUWMsN2yWrni4aol4Q5rm5umCgwe9YNWXdYW0ybhacF21Avz8ORc6img9vzqeYPTMBhlkdfZlGkz0l/3xA1wm1th1W6Q0yrJAcHTIggpJUFYRsFTHaDPf5Yz9FL5KUpvKXkAE05Q7CHxr4iKXG+CINyOB9v60jabI0Lyis7rFWuohKKZK0X7ZA3JEbQ2YmAq3OYI4cYJotBi5ajpqQoXR8RjQ90A70Gwjl3TWzWgwYobgN93F6DodaZ/TFR6f04C6Sg2XGnQUaz1dxmbBWjCjXpRpheH32yXduahpNhpcFOsI2RLb0noyWBwjvBqserTlyvV0agfeG4pmaOIcfk6lh33lkUosPtpMu1tBXZHjmHslchY1vv1IpYaLcy93bb5LZPiBxtGrQk08zicYUjVrlAtgKzMbm1ogX2jl6buwYRTPVk+tjKKc8ha5aRvKkkY4G6WruEF7GOGwWTw7JyqtKCJ+T1uGaTvdWHCmxsU6Fd4S6crVOp3NqIrLaSKWhnBrOR4YpqArmVj8wqkfHqFiErto0zgyHI84x2zzbR06UDMpVz6u523h9sWvW5wNC3F/5YsZayFlo4XyrmgjB4mwxC7jLb6Ml6aaQyKbLORdr351sr2CIrDmTBXDBVP22ljdxvctWbHTlVX8SbntOSPMF1+qZHQ+TwVhKXDqsim35v6ymuStmlVrTjxlMqiRHFW0opOm6vThZczk+pWdZ7+pBf0HIrhTNbPYNS3S9wdWR0DE0TDPXH4IQ0eWwKheGsZrAzk/nB1btVTWWzfm6ZV3Xm3KRLdR4bOJnjkZjIuxqNq3Ir2ywL+sFWkRVXmtU4fBXmo7tZMuShPjkGo0QaXq0YRTa265Db8C52ErX12eUsXksb2oJ7WDHhS3fAmNVp1G0q5zBsH7MkfPD7q5cXBG6GjOI7zkUU7fNO4WldLS3xsKCvo8QENBwxXLOCtys3aM6o3gPdFD50usKGo3IxpufGPFfBHFug8MncEmIvDSlGB/LBNQPR5XbmuN7HJjqDL3Q+nuoQ5mX50EYZJzQZZWBreHk8XeUwt0/CyeDdMTXEcLUby+5abrgNXVI8sG+q5G7AF32226cVmnesOAcTxmKRFwwaHLSbW3FoKVUiedLDTXAcu3JZGWVk5m5dZZgVVigZCS7cwbK2EaRRlZw5tqqGua+OWnIl4dUBraWwDHTEINJLp/AcLwincqEXopMeWaYSD10nrUHdA007tspMd3e5JnR/HM32LOSae6hcm+UOxhY70nwxm6VVKPWSswOJjIDWOAk3bbmywwiH1+sFxTJ2oWtGwEibIak9kQLtuLrkOr7mWzBt6ccWnhP5LfYj6zzfzionsWfr6ioQYpiCHnCd8jcvqYyszUKJDTcXSpMBhC0ztBliLMqZOc0t50fR7wnQm8wMMLkWLtmm9uyya3BHvOm3rl1iK8JZI25rWM5he7PZsK1rPiiSsiEIQo93VyNWG0saqgLP2lEOXEk9OAqA2x5exghyQ/TFYaOvVxuKVa59ul3iKifcFs3RuDEAEm1udUnrOY4n9AzB0s2KIZcuKs0KZ5jjJFxdiZqVyjVl7eYXMPL4u/5GWILtGpaFbsMlWVf2CIqgsKI4ee0xN83w+mY1u4WDLA8YNie3p2Wgg+7LJaoWGefb0zDrb65DoSRBHJ1Z4nWptJdNvuU8lGDWg0OxiCLwtS3Xaqvagp8I82SjrcOcPES4TdMAYh1xH5/WM3rYHAa7P7p9e5KJdtVZi9Rp9/q4U5y1u28Jl5fizhGbflvscxA5ZNp7y8Vi2BbNXjy5zABQxCfoAENK3V8nNOmnLkHLgw/ba19xFZ09Kv6O2HWCL5C3AkwsreYiiXUcNZw47Qhqh+luX+PsQVD8tQlvYZiUM6uJMbNR5jehDndzfT7DzaW6LPJbQyMBW9SB595K111HcH65+WJ/CBHSNqgwEnSOBU0CJiKN7w3zg1uQ5aI7nj3sGmK7tTvOxr5Nl7PupB1XfluCgYtbzPDeFSKBtfNNRAwKsfDS7bjxb7qMXymuPtasJ6WqfzPzizCKlZAqsrxUaZdlqUtvbuSV05C0jtWmN6clLqUuM7NeWmRM0kKeFzwSbXFlOWeiOKeuu7jHKSaSzLm3IhL6Kni7hlryqCysingE0KOhTF3BY+fxq/XtEF63MTXrkvO1aY+pHy/Snu3jZWUic7ZNPGxBlsIB1bGMvIyIVo+HWLJHP2XQClmg7JZxOXtAPVOZc6Pgr11faRKkbSjrMFuq243kB168XhlzKiZ3q6DiN2t5MZrrldkWjdye7RnVXiJk1zYtY61A8oQoLBgcae49hBwaJ/MsMrjcULzQw7zCzoolCZXD3BTM2czMVcALBiXBO6/F3FwJlKOcmHNin3guzUunzrmpruImGJIfFo23thu3Crcyw8At4hqSHEt1C9/WzmhdfBRTfa9lqCVrcjLIawpLOxyJZ6BHMODeJGZIU1FnE6WUK7d1YQT1fe8W2dXRQ5FLDsY0xZ/nVJwHYHxu8dEiUhLjujwSbsxWPK6NCLTqcdvLHSbNLyyiLqJmdzoYXnleCkgIyoe1Kvb7o1dV+NXzyVDZuOwtpDLZb7zL3nFEDC1vWz/3aeO4VZMejP3s1VjNj3gjiWtrTRNqSBtEYeIOTq2lkTsTGRykxM6jQGvRxLU0PwfXVXFMReHqq+UsP2W0HHZzLALDd3e7JaTuSAF9trlT71r0TZzXKHfNhwArbW0txaJRpgm+Q1JpEcIVoWB1aVEXMtvhwxDtKbS5BP5ybjVSIN6WRpC3FmKN3MlauCtMdtFt61fLbeUPHnhvgmGDp6mTFlpt116vn41ZebTiWX9sL+5yjtgcvZgbQiBpNCZdStDBcSoHZwZ3PNUUD8czrpZ4p06WGjEaSxqf7degFxfx/U4nUXsrVEtZ8Tvab8OrR6oJTdM//vjy6WU6s36ePP/lR9HTKeD/2GHk49zw7YnU/djZs9wvd15f/rpoP396qZwICPY4gK3TNngeU/7d8evnf/d5xkRleDztnR6k9c3bwX1jBdMPmF6i3G3rphq+1UXa3g+CP73YbT39jqL+9jzwfrkrmZX30/M3xuCz5WZRHk3PYidtHifQ3sv0W4fpCZHnRt8vg+fhNCAwAM9FTv0NIxbfvKqclH4+JQG6oq/wK/Ly2/8DnRB0xUQmAAA= -->
