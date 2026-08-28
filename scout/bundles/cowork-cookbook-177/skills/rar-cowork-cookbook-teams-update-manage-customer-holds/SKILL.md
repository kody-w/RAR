---
name: "rar-cowork-cookbook-teams-update-manage-customer-holds"
description: "Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_customer_holds", "rar_sha256": "6281faa81e945c69aa5d373eb8e35f014c9fccc9fce53550fba5bfb367e4b9c6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_customer_holds_agent.py` and in the RCI capsule.

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

Manage customer holds Teams Channel Update — Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-customer-holds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 6281faa81e945c69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_customer_holds_agent.py` first:

```bash
python3 teams_update_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_customer_holds_agent.py   # or on stdin
python3 teams_update_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Teams Channel Update — Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_customer_holds',
    "version": '2.0.1',
    "display_name": 'Manage customer holds Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe08c03e5a7dbfb7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateManageCustomerHolds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageCustomerHolds'
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
    print(TeamsUpdateManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aebOiyJb/KsydP7p6rLqIbFIvXsQgICqCyi5dHVUsySKrLCL29HefRL23uqf7zZuemBjuIkvm2c/vnEz85cXt2risXz6/aMAtENHNsiQGNeIWAcKVfVmn8KNMPfiH+GXR1onXtWXdvHx8CUDj10nVJmUBp/O1G7YN4iI6cPMG8WO3KECGVGXTImWB5G7hRgDxu6Ytc0g/LrOgQZrWbbsG6ZM2hhyRpGhB7fptcgEIG7jV/YRz6wAJyxo5d4mfIlACSOgV8gdXN68y0Lx8/unnjy8JPH/5/MuLn7kNvPVyF8OoArcF8p0392S9GjnD6ZlbRHBcNUD9C3hdgRpyyeGtAITI8+pDA7LwI/Jv/5b2bh01P37+UiDP48vL+KN2BdLGAGlLt2lBgPhu5XpJlrTDK8JmvTs0SA3ari5G0zRQ+CJ6fcz8TqmskL+Pzz48mLxGoP3w5aWEIrijcb+8/IhA9b+81N14/jpSqT78+JqVPag//PidTtN5J+C3IzEo9evX5/WTLBz4fWgS3rn+HVJ9uNEDX15+o9x4POQe9YQzX15PZVJ8eBCu6vICCrfwwYcf/xFZPwZ+miVN+z+i+9ODcAzcAOr0FPzHj3cj/4xMngq90/zHbCvo1r+iCRz+xu4j8jTUP6J9t/9/IZ0lBWjeLf6n5P5swuTvyE//ULf/bsJHJPzywoMMZkbtehn4jPzyVdsL3E8/BN9v/vDzr5D0PyWjlV3t3yl8hemZhKBpv3796YfmfvuHn3/6oatgrME8+trV2Z/R/DO73vn8zoLPUR9+PxfyN4q0KPsCeY905Jey+pf611fEdLMk+H6/+Yz8Nl/GY4KMSrwxfZjgNznTQFl/Y8cfX36FCFFAbTr//hhm+b/+KyInfl02Zdgiml92LQId3CY5GIXX46RB4O+Y2zWAdm0SaNjnOBj/o4dHicsQ+fbv/h0oP/lPoETbEXu+dnfw+fpAvq9vyPf1jnzfXhEdUi7rJEoKN0NUdr//Mo4r2pFrVYMG1BeIJ97Qgk8QiT6NJxAgkW//nPjXO53Xavh2h/HkgVAqtx7Rqeky8DpqaMWgeOrjQ+wFV+B3kEVW+lCeMIHA+hFq3pQZxOB2tEaTJlmGBEkNVS/r4U4bWuzzSOzbt2+e28Rfigec4sijNDQoHPAuDvLpE1QszJIobr8UwI9L5Idffv0B+Q/kv5t1Jz7y2ENgf/oDSrjRdgoC86vL4TDoKuhcCB53f/zy69O8kEwBaw30XhIm4DEZxmcKgjdbayv204ykEA9AG0P75lVZtxCjkaR9RdYh8i4vZDo+GlE8HktaACpQBKDwB0jVheq8W7IoW6SBQdiEw0eka8Cd6zevdu8i5jDR3fYbInN7WDPKDP4bxbwPgpPLIoHmf4+Ex31IpP6hQRZvJF4RZYxIpHJrt4pr98kjdB9+gbXibTok7iIF6L8UY3kEo6nu6fEwDxwELeM/Xfpp9Dms8TmMqaB5430f446VTb9XuPpL0TxD361HV/iwFECmUZcEY0H42zOkmrjssuBuPyjpSOnpheDplXsMyn/aFTw6CO7ZQTxqOPKlm00xAvl/bjNGIVlRVAWR1QUeERRdPT6MNzZDo5Ef/ROs9/fJ90T53gO8IcgbkH4psgRGQj387THybvLnmAc4dTW0kMqqd/rQ31CHke49HMfwqusxkN0vxRtif4S2uMMT1B7mLoztMaTeGI5P3ySNYYKO19+r9919UG3ocBhySNV5GQyHEIDAc0cbxPWYUk/Lw9gEY3r1ceLHv9MKgdRhCED6owsS6B6I6nfTKSVUE2ZTWJf59+HJ2BNBKYLOh9LCbhO8IhbMijEyGpiKsLEZx0Ar/HAnheQA2hiK+G7hJnarhzBjg/oU0B19UeZjsPzGA8+H3+P4LssoPqTqwtCCtuxHZA3A9eHZdzmfvoLC5mPm3Sf93t1PXZHflpa/fSnuMr6DOUzobKzKvzEOAgMQRu+IoCMeNTBOc/AMIBgJ9wL8+qihjyL9LsvnP3TlH/5a436visbvPfcZidu2aj6j6KOSvRWyV4gGKIyRpALNo6h9etSdT488+/SWZ5/uefY7yg9DfUb+mnS/I/EM688I9jp9nY6PtokPxrh9HtAY3KfF8RMxPv1SqOC7l5+hMKJpNsAq+l5a3obA+hLVIBoHP0pNM1aoHhbFO7ZCP3wp3iPhmScj2kRjXWzK3+TvvcZCvz7c9l4C4KOihbyDsSt7rFiyUfwGvHwuuiz7+FK4OfifrFRGnIfBCq0xLnBg4sAup03A/eq94xkvfr8iu6cUxIKg/Dxm1kdk7E4/Iu+N5kfkrfW/r6aKDq59fhqb3JElHAo/3se+L/c88AIXW+1QjZI/1jNjb/Xsef8oxJhQUGIfjLW7fM/QkeMfiMCTKAL1H4ns7idu9oQJCOdjJU7at+RuoJwB7Gs+ItB3MOlgHsEA7eCEP7KBfGoAMR7i7Kjud/t9V6t86PLr3QztY1H4y8sbXDx98GwA4XCYl5+aseihME4hQ3j9iCj47H/RGj4pQIiDjQkkQc3mWOi6cwwwBOlTjOuSAU7jwJsDnAyh+j4T+v74D5A4SU5DzyW90MMpGhAe41OQ3iMyv461PRmlAtMQ4Aw28wOcmpEkwWD0zGUCl6BdN5jO5/SUDgNYBb5PTSE+PlV9qDba8b1LHU3y1PiXF48i4MgV0azZx8GhjOlSM9pTY29SU+Do2OjaS4yzB8WMvcrBVkbHB1waOUpneBG3G9TVtD0Y8UQ8+J4mRjopFPRi37RzUqavkh+su6AURNfa6fIs3DH6JRS1dB01mZ77nSKkWSvRil4Fibvd2knlrGlpTuFyw5ibmqiNLK3mQXO5EOWqMq+2mSbo+iLUXC7XR1u67oZaMWvpXHsnCzO9tb1L5sbZlKUL5iaeYiwvN77TrnqjuxlY2jUpVEZ1dCOfX5MAvRFEtzo1pL9fEcnqhsFbC07KsMY/cuypJrTmTE2rwLOLOjCtw2A6wzIuGHZATTP2l/TxXAIineJCNaBT2+uWrkNVThSZmNFamdbYy9nB2ma384rVVMukloSRLnvLKpezAfTGeWLWltf3s9a0Inwrk4p/tINs1u1Lz90XZlu2qEkZZG1LjkOUhlsLvag51VWe1xNF3syk1lxUW7mYbzkto/c8IIX82Na1T80OdCM4C59O01lnEqft7kjF8w6IQWJ7c41Stm0na3279Mk91auUl1nV4bJizMxN6hW0bWU5Llbyc8pvtF1vhJt2ZzWhW2uDvzm782NrpJMAbSQ+oOyzj4u9XRB2cc44rl0bRHICeipCkQzUFlVva956f6V1dARiYB3thImDU9tHFj4b5nm9aIeFSeeUCJzTYnW8JTI3OzpG7CpXtSCz1DnQZCgvUz3AcpNLuFDkwllvWsfq1lMuEHHZJG7MdZ6u41BFTxyLo42vX4WoIs7Wjqg8rUj3RSAvnW3jzs59QtgJccA3BRnmm1PAxnnMzQx76djWZecmOd1J+ck3FQAkKmpn++ws4RSMAmKzJ1yb2G17G292nodriSTYzOp2SsI9bfLoDiU6Oz0U1pUJVja515hkH3Kbs9FJdVtmqTo0Q2HGsbNacWtvWbSpnNEnY79Fq/UMrfuAy9azQe613KSclC9tXT206q1QdO7Y2uBonYxhsdZsVmUVITeCg+EutM1ksskP6VFQ2jRpCCnjhMpZrhTL6cVtRGZ0Me+Cvr1U2UAM8+E43caDyk3DtI8FjDhGxGopX/pTp1WrnjNx2t8LE2yrS+SJLE94zNysvpC6wNmit8nJl3ZL7WZqxN7PLHqHpnG3xZ1Ax3hmKqFAVcxMUVOsOMa1vawWtXfQDtqFvez93b6jpKRAK7VUJqqEL1DHXQtTodzPNlSg1WZ42DKXdK0CUJ9XDG4m5RRFmSxPh1yi5mmZWdv5lXRomeqwKrNJKISEnRVJ0g2Q0V3p62S5rI7STcuNU+bNcwpz2htbLgu50RUWo1bFdQOL4roKrM2Z8NgtirF7EaUPSTyZp9OTdjKkMiw3yyMnSetGm0VTLz9PnC2dJMaCATOWGgyB4zdZMHOOjU4WsnHA18upuSn03PGpYchIIdteXJKzb4rvZTzAnMU2qt10Hl4zy20dZk61J1w/r3irLCdF3J2PQK2zmyOagVPrPX/hG29WzwUmb/CWmwTD/jwF+GV/sZl1eClZHWePu1u7nZfrWMJver9DVYbS+S1uXSlJLTs5uSy0ievJbiPlubAqFkkdzheLbAgTajJJV5HA0cVV0nxlOgkv7OAIJ7PNzQuO73QnLHOZpaJjxZNrrc74POw93V1V8+EqmhEhHLlDttlKU83Ye20HZo5+4aY6K8obxVqKonU2Vgt9KxROt/e3cU8dhPOGkXFdV/KDVs+uSyB6TCPhkcNSZL1weiUUSyZMwgVvqc7gAEGcbWuS9C90Pzt2q81iKw9mpFhogOpcecpX15Nfy3S6YtPaP5WqJ09QJeX6nKQjdcotRHtttTgN8O3FQC0H5QcFQ1fFPlvNqzO/tBiarDrJYHl6ccL09XTnqjepT3JFr1uDPvN7braXdUOXpEKJUvvgwl6FdSgIaHR3liL1rJI6NizYVpvWsh3uwgWuX071dDNj98lZOYPBEKPdaVL3gz/1MNOaK8yR5jfHLsca3g90czVEy0uT9qRfR4RdpjWfxJmhaCyKHwShVTrNMy6dKFFmq1neINZbb+qeL4eJxbLxsqUG81ZvB2nwzmZzJUNikbiuNAuqGzabaVUCNpS7sHczxd1iKNA5y7vF5ErittNTrEH51ju18vyVo3u5F/Mx55r2zL6ktchlUrEVzgFOStGqHrx8mui3xa1fRIvKLBc9DWYDcdZUYmVBa0jq1ppPdUfiTvMzczYBsVHyI1tQ3u2qG7nC88tC4hfns11HYUzrNqdJwRydevNpdpCFmXXpM2IRRpgmbQZJDxyyuei39DJdelJxENtLnpwzpb1KUryLLtd1JJQLXUbzS6bO4zKuEjk9x8cVEAqfJop5cFaymlNv3TKxREEuBfqmXLew0IlocbLatb3dYrpXYEtsV1Xk2coLIyP2DKzJfuI7N2+wDlxpXMDA8OfETvZxnzDS9OokLlpO1ZTJ3QhPtPI8V/XT8XzsDZ4YWCVZOcdsEw0WeVgd4IJ8SlVW2ZZpwq8NW01M2xGjJVeQE8xd0XBlYKAtp6VLlz8zMhoP9FHBdxNxkAthYzAZK6RroAfoqXEkEtt4EFjE/tYuqX13uWE0tesXYnZVb/v5IRBtmsnWp1SEvUjDkHNxMrkyflOnE7rA+m537NSpVGMXvoftyEE8wn5GCAqHEpIrvzhEng7SuY51WcEOu3gaK1GOl/FOSMFlNSf0TNmZihO1B8xVDJnMtPq2N3zAk4Llrz14ubY30/NCIYNK4lLQZh6J6mCAfYrLSRdbyq4BPhX0SFyt7Rk+rw1x7+5Mjq8gM2MJEzG9YadolmDLNFcYpzsbC2eIF8VxmVRip5vsjhVpSvOwhQ6X0tUpB8HS6di5edOBcSlEhdi5GbHVMP245JuT7Km8LhrDKZPIjm/7AuxTUdA4Brgcn5HcatjOKlxyV4eUmMe1Mxxmzm2r3bZHYkgx2OxgPco681DwxBtEQjylZZtiAaA3Qa4k5/nJ3DbFWR9g+VG3HuUmIb2tZhV/1c6i4Zehwu8iF5Vn80XuL5r9ju+Ta1Nhi2WecPby1Nj2XEbLOPeDkqJ0XTUtfY0PWgu7k9Bvb1Vzm6Mqz3bUsK7rTL5KohHddgtBpTZRv7mCMjT2CjudGZl642bYVdh0VkOsblE8ned2YftAVprLpBOOVirug0nUCl1XVXRJ8nZ8psqBu9gVoMrzhsXdctZbAUsPB95Zy5dp4fVLRaPlyLb1aVNN9ev0UJlCcrpuzv6kZejbAlCH9mQpjkicbyi3MP12n3MQwFfyUejAhpY2OE/oylClgwayAFbZmqClcNCinAPmBHgWPpjHeGoGsVEZ8zzeFpq2SM+LvAoh1AKL2F05Lx4GzG/A+losBSXUI5R1p3yH9QGGL/TLtJpiJQV7nGHLWWRmlvZpgQ14q7boBVt0cucc15x+a7jTVTmRLnu57eXb+tgRsR7EaElzTqVRpi+pqezaW1clYXdSZzqIFusVzx5n7LE3VT3iA9OVMarnyMON3PF78lpJWIwamVseqPIaRqwaV5nKHI58l098QeyW64PRaPIkKEB/TC81e+KTeTk/XAcbaw/XEna0lZ2J26DAdJqa+LrP0Cld4vu9UBNpXhR6i4WhvGYjV3Ip5caUIrUsadYob0XJUEc5xo9Tnw6k+YmhL1dGpLGq2uEByL3Dgbl4reNOvX1MMavW2qMzutgS/skGOy8yxRneXNTL5YirhiT4dKdUJY7JenVsub4Xdk7p14JYGdrE7IKcoPINRfVuyeTddrden31Nnml+EYvxIkS9+ZLexHVJtqoJPJwOLT5kVtcVpybijmFRYxfuNgVbnkGzXZDbibuZE37Lt4KK0oC2DHpOujwx4WdBS84GMz0Bo6gmQjRgeMc7eyzYbcmJNUHRUkLXy94JshqlSDTxqEkeBgeGoinq2l1TQENg2h8ldx1eKU7v3ZvILPjyAtb9Bt/yy/1M3GnrtWrg87Yhq541BNr3N/yWnyyGpSx5V86PY31PQHxshNkF9+nscIwWrW05HQ30qS8vLHFmXtd6S4eSy5DqacF5S3zRak6Mz9kZTsRtcSUPydmkQ2W/4SfyNQk7uBDRjzfvjDXpPp/QtHZJaWwFyDyfS81SoWe7437iMAHB8Wu1a7JcwafelmamhldO93vYjlM1Y6PKid6dlqwVbJYM2zDscp/zGTMXq9k+7EKDUa7LGe8qsJEqhEUQ2/Yma+vVzDCJYBeAzhVWMZmSBOl19mFVhJJ6i/KSPaAB3dm9Uc03HG1HKos364RXF8wexGI9mN1sP0NzNYqIpvQyKmgP+IIL58UWu/EyrbGhKJM+MXcL1luEh82J7sTDdTtZyh1J5Hhuy+tC8F3sVBF6ceMTukaPOH7BExDG4qoMz+wEZkrehTMnVzqeWxPrpjeIzfrkWn3TrHZ5L559iWLml7Pk0qdDvrHxuVNw5nQ9F8LC6xZtDGiNFjSFKHCfWdey5w8WXJVpQTbBig0bNqVA6XYqhMQpVcy4SylxX6cOvbnMkkMT35qinh42KEMweDUoxemwJ9BGzdsVLIsrPxxQWbnWkmKtAo/dWdzUc3UvUzsF1XKSWkmF1VE5PcTLay6CS2DxArCjqXqxr+Rm3rtsFF2oKtowhoI5J3aIQHSFvixR92j5RUoDQ0tWdVFxq9mVWHfYrhOEyXpr0Tc4ayKLM+IQzgfc8dDpLt2hPlYwk61hUwRJBN6VLFfMLpXDoeYxWNK9Od97h7NS6x01n+z2tnJTsNifE+zttLoM0HTG+opKEzWIiS30w6GJjoEBjlF+Y42ZYga3ML8Q5lWRmp3g7jJ3Qg71lG8kVCxKK43yjZZeEmYy2S0Xh7kWYe2VXG0vYC93HRmQVItFoLyk53Tn0mp5qPgiY09Tmd6X7KKkZFiF3C7R9/huezgZ0xnq+XEGP2jMuKxwC80bM1E44cJTK1oOnSkVwazbn6bnuptuaHKDF3zKLuuYB9v6oFSnU3xdmsCYMHmgyZR8VXOgR8fZjPZBpmoWk22NoO2O+1O9llc4wPIFeoO924QdJtWOA0Rt+M1VqbOhcInd0SKxtg+csGHssFltxMXtdiZvh8rHjr61ky7kITL3E7iEpGgSP5J9dZ3sUNYvl41f8xV6OOabqmgObOFRRcwnquGd9+tqPt1H3nIIL50kk7zTUl4zIemhroP9OvQOtQcbtYpl2b+/fHwZN6Kf28l/4f3wuL/3f7bN+NgRfHu1dN9KBm7w+c7r818R6uePL7WfQJEe26lN1kXPrcf/spn66Z+/khjnD4/XruNbsGv7tvfeutH4xaGXpAjghHr42pRZd9/Q/fjidc34JYbm63Pj+uWuWF6Nu+C/VQRelnUAFWjLr77bxC/jdwzGNzsgSB6Px8voub/88SWA0ZInfvMVp8ivoK5GTZ/vOKCCs9fpK/by638CbkyWzpIlAAA= -->
