---
name: "rar-cowork-cookbook-adaptive-card-establish-banking-relationships"
description: "Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_banking_relationships", "rar_sha256": "c72ec9ba0105be9a5d4d8fa1ca6f29381bd13c91e1880ff68a6735697cdc6030", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_establish_banking_relationships`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_establish_banking_relationships_agent.py` and in the RCI capsule.

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

Establish banking relationships Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 c72ec9ba0105be9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_banking_relationships_agent.py` first:

```bash
python3 adaptive_card_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_banking_relationships_agent.py   # or on stdin
python3 adaptive_card_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_banking_relationships',
    "version": '2.0.0',
    "display_name": 'Establish banking relationships Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a32fcec0833829c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardEstablishBankingRelationships(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishBankingRelationships'
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
    print(AdaptiveCardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZfiyJLlX2GiP2RWKzMktKJ8p84ZSSBAaEFoAVFZJ0v7gja0Iamm/vu4gIis7Hqve6pnPgyZEYGQu7nZNbNr5i5+f7HbJiqqly8vmm/ns7WdpnHkVzM792ZccSuqC/hTXBzwM3OLvKlip22Kqn759OL5tVvFZRMXOZi+rwqvdf16Zs8qv61tJ/VnjGeD250/4+zKmwmaIs/q3C7rqGhmRTDz6wYMi+to5tj5Jc5DMDO1J3l1FJf1DNxu2noWFNXMzxzf86YhcT7z7DpyCiCy/gRu2HEK/oIxum9n9StQzO/trEz9+uXLL79+eonB+5cvv7+4qV2Dj17elJp0Wr1pwD4UOPx5fSAptfMQTCkHgFEOrku/Atpk4CPPD2bPq4+1nwafZv/+75ebXYX1T1++5rPn6+vL9O/Q5rMm8mdNYdeN781cu7SdOI2b4XXGpDd7qIHhTVvlE3g1gDgPXx8zv0sqytnP072Pj0VeQ7/5+PWlACrcFf768tMEwdeXqp3ev05Syo8/vabFza8+/vRdTt06ie82kzCg9eu35/VTLBj4fWgc3Ff9GUh9uNrxv778ybjp9dB7shPMfHlNijj/+BBcVkXn53bu+h9/+ldi3ch3LwD+5v9I7i8PwZFve8Cmp+I/fbqD/OsMehr0LvNfL1sCt/4dS8Dwt+U+zZ5A/SvZd/z/g+g0zkFevCH+T8X9swnQz7Nf/qVt/9mET7Pg68vST0GQV1Mefpn9/k3br7hfPnjfP/zw6x9A9H8pRivayr1L+JbZeRyAnP327ZcP9f3jD7/+8qEtQayBzPvWVuk/k/nPcL2v8wOCz1Eff5wL1jfyS17c8tl7pM9+L8r/Uf3xOjPtNPa+f15/mf05X6YXNJuMeFv0AcGfcqYGuv4Jx59e/gBkkQNrWvd+G2T5v/3bTIrdqqiLoJlpbtE2M+DgJs78SXk9iusZ+D/lduUDXOt4Yr3HOBD/k4cnjQHV/fY/3TuZfnafZArbTxr65gIe+vZOhd+eVPjtByr87XWmg0WKKg7j3E5nB2a//5rboZ83kwJl5dd+1QFqcYbG/wxI6fP0ZuLK3/7WOt/uIl/L4bd7AYgfvHXgthNn1W3qv052HyM/f1rpgprh977bgtXSwgWqBTFg3k8Aj7pIAfM3E0b1JU7TmRdXAJCiGu6yAY5fJmG//fabA/j8a/4gWWz2KCo1DAa8qzP7/BnYGKRxGDVfc9+NitmH3//4MPtfs/9s1l34tMYeMP/TS0DDex0CWddmYBhwIHA5oJS7l37/44k0EJODKgh8Ggex/5gMovbie2+waxvmM0qQM8cHcAOos7KomnuBal5n22D2ri9YdLo1cXtU1M3M80s/9/zcHYBUG5jzjmQOymINnFEHw6dZW/v3VX9zKvuuYgbS325+m0ncHlSSIgW/JjXvg8DkIo8B/O9B8fgcCKk+1DP2TcTrTJ7idFbalV1Glf1cI7AffgEV5G06EG7Pcv/2NZ/qpz9BdQ+TBzxgEEDGfbr08+Rz0B1kgCG8+m3t+xh7qnf6ve5VX/P6mRB2NbnCBQUCLBq2sTeViX88Qwp0B23q3fEDmk6Snl7wnl65x+Dqv+gdtEfv8GMH8rVFkTk++/+lVZnsYNbrw2rN6KvlbCXrB+uB79RpTX54NGegUbhLvufS9+bhjXreGPhrnsYgWKrhH4+Rd688xzxYra0AiAfmcJcPQgLgO8m9R+wUgVU1xbr9NX+j+k8AojuvAaeB9AbhP0Xd24LT3TdNI2DodP297N89DLAEMQGicla2AD93Fvi+59juBWhVTVn3dAkIX3/C+RbFbvSDVTMgHUQJkD8DSsQgj0A5uEMnF8BMAHNQFdn34fHUTJUPD3sz0Mr6r7MjSJwpeGqQraAjmsYAFD7cRc0yH2AMVHxHuI7s8qHM1P0+FbQnXxQZiOc/e+B583uo33WZ1AdSAfM2AMvbxMOe3z88+67n01dA2WxKzvukH939tHX255r0j6/5Xcd36gc5n94D+Ds4M5BrWX0n2YmyakA7mf8MIBAJ98r9+ii+j+r+rsuXv7T8H//eruBeTo0fPfdlFjVNWX+B4UcJfKuAr4AwYBAjcenX79Xw81SlPr9n2+dntn3+Idt+WOSB2ZfZ31P0BxHPCP8ym78ir8h0S4xdfwrh5wvgwn1mrc/4dPdrfvC/O/wZFRP3pgMov++F6G0IqEZh5YfT4Edhqqd6dgMl9M7EwCVf8/egeKYMIPo8nKpoXfwple8VGbj44cH3ggFu5Q1Y25s6u9CfNkDppH7tv3zJ2zT99JLbmf83Nz5TgQAhDICZtk4gnUDT1MT+/eq9gZouftwE3hMNMIRXfJny7dNsanY/zd771k+zt53EfZ+Wt2Ar9cvUM09LgqHgz/vY9x2m47+AbVwzlJMRj+3R1Ko9W+i/KjGlGdAYEHw96fKWt9OKfxEC3oShX/1ViHJ/Y6dP8gBwTSU8bt5SvgZ6eqAhArTeTakIsguQZgsm/HUZsE7lX1tQK73J3O/4fTereNjyxx2G5rHH/P3ljUSePnj2k2A4yNbP9VQtYRCyYEFw/QgucO//rtN8CgMcCJobIM2lUN+lHRuZI4Tj0zbh4d4isOeuTQYojS3mjjfHXHruzxcLJAjIhU1SGEHSlOu5JIJNyj3i9dvUH8STgqhtuwuXmuMeTdmk62OIg7n+HJ17FOYjBI0Fi4WPA6zepwI1vafVDysnSN+b3gmdp/G/vzgkDkZu8HrLPF4cTJs2iW2dpj9BI+kx8khvBV/Xaq9RtNT3hm1Vt5FEbeq0Ea7yTW4i77LSkNPudjpKWX1IZCJe9lF+1QPGYU9It0sRIl/jC10Tc/ZWNTCxrMOQW51ztGPwC1YtrZIIhtMoayXfb+fHVqZElZKEm4Gm6KUTuWHdsXqeneuGhqDzkd6lpi0Y2zGJUDOKmP64P+5jiPalEhvVDDKsY8X3m05BWrJOtesZlaxYP2bCyOc7WjsfV7ss9yU+jXKoJ6pTeOxR5RAH+7xEg73eEEFgyQrWEVA3bC4i5nOCXWDbxJV48pxo1xQ1M+IcS3MNS1iLyA8S3Ge1GF4b7hI5pS60ip5SFe+0wvY2xDAbxkVvaqnm5cTg1OaYWZ0Wl0Z2lhYyK/ipIPhSkwynHR1S0altD3YabReN4RYn75CcNojX2OMNlUoZEo0UFXPFF8KNq7E6POxZLPLV00k43tIDW40EU5CqtRUPNjGoAUmjbnRBKGWjnnbElr5I3CVeBigxtMqQhvn8Rl1LA8WsXuTmPO7v7LpAioMbQxi2XA5xdRJZ+9xeV3NpQ9ess27CNawbvmx1/ppHEM0059Zc74jTESVWc6hDzjEW7pf9Pj/sLrKr9ylbQ22xOS3m2sI78zW937PhWdiGzcCXB9p3Bh5tMfZgJ4h/9DA8q/q6IOhUThsnGZlkuCLZAVIkeHUdE6/Y5QO07XbV7iCxVcJj1qZveL7tjaMp71PnulscIOfEAO5FXVytBdhshRunHhfpcuMabZEM+z7fzy2xSdYZsu2IvbhyVtSi0+UDmhSDGnnsSIUNqJK9eEbm3njqwU85n+vYsj127P5CyVWoBaPaoecgDIMtg2GLcmWIDrmHlwLpj8KSkmC8PRUn8RDRxSUcggXFt5ClX8rzeol2KXJYdBrFZ9F5I6cFKW7OW7sa18VB2xlnadclmrZ04ROTc6Fpe/FwGHYVU7tMSeUMx8kmlbOIdnFNEj8gzBKX8WvcpnYSs+iI9qvzyo/AoqrIx7fCNzdStSzHI9tLWNC6zu3kJxWNqufKNI5FvJrzlyK2hotFS/NtJ6GrbtzHR3a5yCo6kA0yFpOWDCHK3DNtuUpzEaaVYNEteLQi+p0u71t8vhuxNUUd0Q1CsDlraILglbx5vJzEZHfoNql6Pto9wmJHDimzAHfN2oKul5OEVWEd1wPXrq7m+nIazj2jXlUNMnO4iwkiMHakSrCX4ipvApjQBamMu722E8wY+PWo6EpX24cDbGAbrpeireXON9kRqjYr+MraJm4sUo1cJZc5qkd1mBZbldN8a6eoC2hZDalJjJuTlG/mKzhO8/l6pC9Iel7CRBIpKdAoCS6iXGydXVEcUPhIFVdo6CuDN1LWRyNtWNWyGw2Uo7quUEedIFQxZxfZPO3Lk2QUotsIarWCi2t9M3aEiZmtcShUZrk/Eb6ZiU6H7cttWROHzi0cioSqAbXV/c07mpm55iCaxVoyQxPoMF6LORXUhbLECzJAdgErIptxqMLxHHjNci3WxXYUT+MxBIREk/pSzLQI3RmgnCUkqxuug9gLrluvNmnrHMNiCYsZLag0ZG2iFd8VsVE2cjXH4eSKiLuupQVLHnnNpw7OVh04Wb2sGZo4OLwEwYjZX8lsybvKPmSMs5bFAkZCuqG7XnfcLhNpaQiMl5YHGUTTLmfIVOtdNMqbk48Xas7hcbmXkFXYR6WzctNeIISK26XxGlnJFt9QJ6EN6Hi7SEbJHBf5EXIAJS9o/1TeiDV3NdKKndNoqmmWEzmgVjR5rS0z1VrraDfHXdi+LZ2T5t8CLw6X+2y3x664dtEHfNdsEoogISFYCXgV8MvD1tn4kKxbachXty1hYM0m30kDst0r5lU4S1cGChu6XKE4lMieK/DIumJPhdjjNYpKkW7ES72LuUZNy91RtsMFM1R7TjA8KpXEeHVNE5bQB4y5yaN8JVoeQs10nfincFeoFbsY4mVngp4eJ0/itQ27QSAL67YJxU3LzwHVGU0mAn7wTMcVlcjEumvAqTd1p61JWDPH5XZYbGx3y5dXhbIAX2FR7iU2dpT4sRTXt7OPWShxbnIDLSIuyqwlSkg2KotiDOeJq3sXehurJcSdqRy/peW290JQJUEeHVZOSxJcoxMwn3slzpT6NtyZDW3z6rCRVXUUJDq1DbS+6QJxs5cyYRQerloGxCqYWiVcJ/tarG4unhDj5yKGG1y9ZDonz1VEXmUms9qQ7FXN6h3ManQ6pt3qqo9nf5MKQWEsTCncp23Cmrvo6MzhPh9jXMP51Y22FH+D9J0cX5PtGO740MO1swXE0S1Lm5a7khciZKVRdN21lH9e8zUHB8faC1FBG21IGwOo7sZrZGupnRkWLMMFmaoXJJewdYGE3nqDHVN9fhKJpS4krlFfBwHWi0ggpV5uVvzWphlgHCs5enmrLNAJHte8XQusv/VqJWbss1HxoaGZXLYTyuJiI+p2qUMgqy8HaG5DF1lU04JtLjBMiXSt1GyvEDvQexBEwmztra838rK2jHIueqZhrE2EN7YaBMOdYGNQYvGrtDIK1lW9ta3T4zZJyQLWEGnANgo60tDlmrZ0LmMrq3eTq4lVHoWP+lLZIi6j8xRq4rS0Ei5Xho1CIg/01rM5Llj2hZLu6hVarEI8jgk/P2NasdQzwYz8xNTn2QooX2cBs0DGlDsuLOPAEnVpbPegJIZWOndzf3cNsOxKrw6dQru2ma2hRkeYC75UMgr3XC0Ajd22TbbkWTWHdavtK4MzUby8RGMlzY+pWTOCnbFOwSblKnTSy6qiLlgsZrk21x2XK0X5th5ifzeUMBH1SUooO3neO3o4KrnHr9rhPFjlkPgMHo/YeOK4uWS1/G51kfIlzl8N29XXBhqc2Z6gLH1FlPZmrkh9EotxqF8bx9KT+bAsjFFAzylWUkeNZ9rOuvhzqTevxnwOgqZt3fMCTzqZPylNjpHGUJzwiNxXK7paFB603y04bbDjdr51rpwU+TWoqCpypttt1e6Cw1Hc7rctqiel59MGYV3gwWzWAwX1xpDIMHrTb2KI9PLZFxThMKzEfSJrhsLVerkxxVFlW0QvyhhFaFEUNXoMcmZtrZSujRSbVLvWW9N7w3N1w9sLfX++KpEWYj1uIOVSsJgrbyCkjm9MzXTO67OPhgQXtoVxdUQDwdh1o8ZnQyZ1Y0FoJJqVIJASCjRJeLqTImWRY6tYPunHcwjXcpSGF8fH3dSlIky7UolmCs0VH4uLjlGss9CS1dLjUVmPA6eNxNa+op1a3kjOjlUt4ndBlpqSY5xPxdqSqma0lP6yEIujnHGQ7yzY8KYIJ39uOilUcbl+TPlUtzIcbEeQcSu2I62L+4M3Bj2fKq3QFeySaga9UZacD3frUZmXl3qhnvySttDVqAwdvx3sbZW427pLQA8tdFsrXI+MdWTcGx/p0ZLtz8eNhu7SpXLZLsbUXsyPThPods9dlzIZ2uQ+Nh1cUzXUIpLOsZhq7fOcw64gdMxvi7VhWEZxyHyfuyFbW6Fx/TjEZT4HQDTocM6IFSZcq2LwlWVJYKjPXSi7hY7qmTWYBoFPne0tqRNySwXywtPIvud80L7XSxM75mtsaS3go7zvSR71oMo59VAttq1t2AE8x9dgw35LcfQEERuFqjFbkuXc8ZeBd45YFVQSlKLQxDcGJYWQc3rrCYmeuyFjsss+xTBMPKv703k0TxJytiTeyA47QJIGakpxF0QwA7G6WSuYfowPJt3uGXggqbGxrd0aZwOc9nyiYfethjbkTYBS3V8c2RDCFUiOguZ6QtUr1i+WnJWf55hjCMfjEie4vBYobNflZL/ZLuBDAHdzHr7xpHu9GXATBL0HK9CpKSDyTNMG2FQG3u4kxQ0fMOq2315AQ9Orqj6Iw61AxpCNKWqF2oLAxjf62Pqmqh44uVpxKtQHzO5w6HV/uwx3uzPFE7sY023KHWvTj5kNY54zqiH3LMClddTDfmWyeUr7i4IY+bMpSp3GA37iA+Tcd6KhQBvQcy+upM95oIC58mgia3qwRWIRkoJDBZ53OA3zIekWycFPfS7v+yRYYnmw8dlQYwKx91iwmx7xbGn0aOe6uQaPWtd3OLSXuE3KNnSt+4wdDyyNQub8Ju8170jT/QrlT3u02OQrQ7oF1c7MLBCecEo4hI45BcnylH9dK8qRzrCewAbWwoWdxO8xn+Dr9SGopca8yWEjbrZBxnPbfCogLOac6OO4vanucb1PB6dVsYMoLnIxne8lGui7PuJWv7DTUNG5MDlhZ+kQH1EGFnMu8M8uDrksURx3Xcg7K1WEKryHKjbE3f1tZJH9nAninZF2NEqgorXho5tahvVNoznM68+WIrORYtzMKwZhhVK1cqtmQTdPXUFUK0unJRmXmzNmnZxt2iLoIidkJXYy83YSz7pbZQwR0mCDkWm7BZTAXBAPI4ZgJ4NegA0kDeHa/LZ1NecU3k4QGcFdEjrKOnRuNzyXLUW6KmsEJkUfW2/rzGpRmTmrItvUGeUkrqNEErJBzSPtIw2W0uK8sMim9456TFKcSS5ggckal+GFUfd6uFhA1NHKVGZ+3OM1IRIlyw/e8kDq5KZuoYIIbCpSHIPCDw4Ryod2v+A4/NQ5ULo4H5c6IEpAsk7bwVHBrCFt41Mk7NkRobKwgjJ0SrHmCR7rOX2x+ai5NFjQnfX56FLeOVFgB8F7apHScMttg6G77C2Kp0ghDBLJvyoSczqHO28Xw2do3EAdjrJHSpPXKh24rAmxKNuhLcmXWwHsBkS8CzqKOF32q5F3gogdSDwZBaeLFJ/yCmVeOSTC2PSxOFybJGcOiEIFIcMWw3FVaOc23iiYslGTy2jCjpWl2BGmTKvbnDx3RJV+zXLHrNnQ2b4mPXVLKZseMfhRX9F4To3syHCjtWw3pdrI4TKi16ZiLGnHvpwvbL6siwvb01eUMsUlUpICWhO2VNObtWsG8t53RYfBKAxlxbAGFoRdps3X652+o4PejeAs7TwKkaoOkoouY0bQysE70IjYyfqIXbtoyRniXCQoodmgLX/bS6RjLcfbxu7d9UAffGO9yshVzIcluXC2JnEppSEZmEAOwnmyaFeYjHjRyavki+u3w5ZYw7eVVGFbG+cuDMP8/PPLp5fpePp5yPzfe9w8HfX9PztxfBwOvj2Guh8w+7b35b7Wl/+mfr9+eqncGGj3OG+t0zZ8Hkj+h9PWz3/rScYkang8252eo/XN25F9Y4fT15de4txr66YavtVF2t4Pfz+9OG09fX+i/vY85H65m5uV04n5D+ZNZ7n3BwrfmuLb4yn0y/QVh+n5kO/FoMQ+L8PnefSnF28Afozd+htGEt/8qpwMfz4emU5up+cjL3/8bwhocTg1JgAA -->
