---
name: "rar-cowork-cookbook-adaptive-card-revalue-and-adjust-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_and_adjust_assets", "rar_sha256": "fdb1648fc0b993f33075ca5ac752013394f0310462b320ec00a8ae6eb22d32be", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_revalue_and_adjust_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_revalue_and_adjust_assets_agent.py` and in the RCI capsule.

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

Revalue and adjust assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 fdb1648fc0b993f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_and_adjust_assets_agent.py` first:

```bash
python3 adaptive_card_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_and_adjust_assets_agent.py   # or on stdin
python3 adaptive_card_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_and_adjust_assets',
    "version": '2.0.1',
    "display_name": 'Revalue and adjust assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e509bc95d41b7804',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardRevalueAndAdjustAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueAndAdjustAssets'
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
    print(AdaptiveCardRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPaWJPuX2FqPrh7sAvti9/oiCsBEloQIIQQtDuqtRzt+4IQffu/3yOg7Pb02zNvT0zExS4XQke5PJn5ZJ6Df3uxuzYs6pfPL3tg5xPRTtMoBPXEzr3JvOiLOoG/isSBPxO3yNs6crq2qJuXjy8eaNw6KtuoyOHj27rwOhc0E3tSg66xnRRMOM+Gty9gMrdrbyLvN9qkye2yCYt2Uvhw3cVOO3DXZXtx17QTu2lA20ya1m67ZuIX9QRkDvC8KA8mUT7x7CZ0Ciis+Qhv2FEKf8M1BrCz5hWaBK52Vqagefn88y8fXyL4/uXzby9uCsVCE9/NGa3RH7q53OPumrm7YigitfMAri0HCEsOr0tQQzMy+JEH/Mnz6ocGpP7HyX/8R9LbddD8+PlLPnm+vryMf/Qun7QhmLSF3bTAm7h2aTtRGrXD64RLe3tooPdtV+cjXg1ENQ9eH09+k1SUk5/Gez88lLwGoP3hy0sBTbBHzL+8/Dj6/uWl7sb3r6OU8ocfX9OiB/UPP36T03RODNx2FAatfn17Xj/FwoXflkb+XetPUOojug748vIH58bXw+7RT/jky2tcRPkPD8FlXVxAbucu+OHHvxLrhsBN0qhp/yW5Pz8Eh8D2oE9Pw3/8eAf5l8n06dBXmX+ttoRh/TuewOXv6j5OnkD9lew7/v9JdBrlsBTeEf+n4v7ZA9OfJj//pW//1QMfJ/6XlwVIYXbXY+l9nvz2tt8u5z9/8L59+OGX36Ho/1bMvuhq9y7hLbPzyAdN+/b284fm/vGHX37+0JUw12DJvXV1+s9k/jNc73q+Q/C56ofvn4X6D3mSF30++Zrpk9+K8t/q318npp1G3rfPm8+TP9bL+JpORifelT4g+EPNNNDWP+D448vvkCVy6E3n3m/DKv/3f5+sI7cumsJvJ3u36NoJDHAbZWA03gijZgL/jrUN6QvUTTQS3WMdzP8xwqPFkN1+/T/unT8/uU/+nNlP/nlzIQG9PdnvDbLf24P93h7s9+vrxIDiizoKotxOJzq33X7J7QDk7ai6rEED6gskFWdowSdIR5/GNyM9/vovani7C3sth1/v3Bs9uEqfSyNPNV0KXkdfjyHIn565sDWAK3A7qCctXGiUH0Ga/QgxaIoUEnw74tIkUZpOvKiGIBT1cJcNsfs8Cvv1118dSN5f8gex4pNH72hmcMFXcyafPkHv/DQKwvZLDtywmHz47fcPk/87+a+eugsfdWyhd8/IQAvv7QZWWpfBZTBoMMyQRu6R+e33J8ZQTA6bHYxj5Efg8TDM1AR474DvV9wnjKQmDoBAQ5CzsqjbezdqXyeSP/lqL1Q63hr5PCxgJ/NACXIP5O4ApdrQna9I5rD7NTAdG3/4OOkacNf6q1PbdxMzWPJ2++tkPd/C7lGk8J/RzPsi+HCRRxD+r+nw+BwKqT80E/5dxOtEG3NzUtq1XYa1/dTh24+4wK7x/jgUbk9y0H/Jx2YJRqjuhfKABy6CyLjPkH4aYw6HgAyygte8676vscceZ9x7Xf0lb55FYNdjKFzYFKDSoIu8sTX845lScAjoUu+OH7R0lPSMgveMyj0H9b8cEfaPEeH7EeNLhyEoMfn/P4uMtnOiqC9FzlguJkvN0E8PTMchasT+MXfBgeAu+V4/34aEd4p5Z9oveRrBBKmHfzxW3iPxXPNgr66GwOmcfpcP0wBiOsq9Z+mYdXU95rf9JX+n9I8QnDt/wUDBkoYpP2bau8Lx7rulIXR0vP7W3u9RhShCsGAmTsrOSWGW+AB4ju0m0Kp6rLRnMGDKghHhPozc8DuvJlA6zAwofwKNiCDWkPbv0GkFdBPC7NdF9m15NA5N5SO23gROqeB1coTFMiZMAysUTj7jGojCh7uoSQYgxtDErwg3oV0+jBkH26eB9hiLIoM5/McIPG9+S++7LaP5UCrk2RZi2Y+s64HrI7Jf7XzGChqbjQV5f+j7cD99nfyx9/zjS3638SvRwzpP76n7DZwJrK+suSfpSFMNpJoMPBMIZsK9Q78+muyji3+15fOfpvkf/t7Af2+bh+8j93kStm3ZfJ7NHq3uvdO9QpKYwRyJStB87Xqfxp706Vlnn6C6T486+/Sos+/EP9D6PPl7Jn4n4pnbnyfoK/KKjLfUyAVj8j5fEJH5J/70iRjvjkzzLdTPfBiZNh1gm/3adt6XwN4T1CAYFz/aUDN2rx42zDvvwmB8yb+mw7NYIK3nwdgzm+IPRXzvvyPLPML13h7grbyFur1xdgvAuLdJR/Mb8PI579L040tuZ+Bf3dOMfQBmLURk3A7BCoLzUBuB+9XX2Wi8+H5Ld68tSApe8XkssY+TcY79OPk6kn6cvG8S7nuvvIO7pJ/HcXhUCZfCX1/Xft0vOuAFbs3aoRytf+x8xinsOR3/2YixsqDFkM2b0Zb3Uh01/kkIfBMEoP6zkM39jZ0++QJS+tipo/a9yhtopwfnHsjkl7H6YEFBnuzgA39WA/XUoOpgS/RGd7/h982t4uHL73cY2sf28beXd954xuA5KsLlsEA/NWNTnMFchQrh9SOr4L3/6RD5FAMJD04vUI7vOShFML6LOCyL+ziO0KRrk7ZLkxABHGcJH8FRhKAwB8cQ4CKIzdiAAg6GeTgGgwZDdE/Rt3EAiEbTAOIDnEUx18MpjCQJFqUxm/VsgrZtD2EYGqF9D/aEb48mkC2f/j78G8H8Os+OuDzd/u3FoQi4ckU0Evd4zWesadOW6lxDi71R/qmImULe60mHr+y1cMijSKHpZr+54ooz7AP3zC2bwTE5VeoFWV3bN7ALmUInk5KkvZnAJ7LaeovKA+Le6TsaXKxmdotRvN9zkl7NDql7reTjHszLbFodkbRUj1XTKUySmu31kFQRUvqKtawG1GCml/WFyMwSiUvdTEK9amtlI2wWR58hZlNKaNSkodfloY/6nqZIr9ba9HSoQrQWlAOJXEKXFJQOqbSQz+RrtNs021m21ezBOWg6tTFKhPVzA2GBhWOxEdKMX5sLSiAuphStrSx1m6iryEPpOWbYeaZyJFfSrjlRBeYTtasmXc2bc0uMjTVI1YXnd0WixmBLKOdwJ6OmV6V7ZpPnAlFZG9OFmyz9qJyvh2VKHbITcTuuW1c92428WG3SfdVqaqwYliijZ69ubdXQXcJcIB0r2DZ5UC/asjcVOdiZYcWLAMXFbEkLO6VAUzfIPGm9JCUDkNI4LOL7AYurbbDRhx0tCYI27xsn35wcyeI7sHB1kB4tYLievBdcKq7MqDwUVjQlj40u5LnZ7Ko16yI84/rNML+aNd9uskKzUTC4cnViStlMMH3WkLZJpZ2nlyfl2mxv6Dzlj8nGNcRDqrOgByVVeQxl1BYNNia33505usUGGiWZXUVi9Gnl0OQpRBOkG9Z5Mxtu4WZDdNK+NOvhKp4p/7aPSvOsXJkLow7lgBi8nSguw3jH5JwQmnU7HLB1d5r1Jj/1FLKTyrad9yukcY1IXKW3SjweSnou5zN865iGMlRVPb8V1GYpDOepdY5OrL6MdqGvrJLMP6Xa0lrUqGhYgpNurIMJfyy8vKXcjbGWChtZxEam5HAqLhhOEC/tUS7iGPWxuYZMc2uL9LN+mPflatMvekFL26kE5lpz6KqoSXwtXQZdSpk20u2l2dFYnAqtv8YcJu/BGosW/f4sNmeVPHCcXIM6Va6D6G9Kn0etZIOoy9MAW1ruygmpK91C4rFiCKsm3itXVSREbxlyZdcsBZo3uH2qSkVZ4ZvlsncNjaRVmGrFdH7J8yyPc/aUL/0kYWJKLoRV4vMSmRMDuxJZbXk5SGx+O22XU1Q1FDI6l+w2oA7HIVcwL74w2+mKOpyuAmEnCOMKp3ozTZJORXUv5jgdUWKga2aqkdfr9rqIOtVYnLEgKMJOs0FhbylKiQy0AUTgyxhaWUpVrnXxhJutYOT62q2EXbwqL37ah8YFAVRwbJFTtZ75PkEcssM1zy/msrn6WS4vwmnX2qY5OyLt/ELF+yjAuLnGqbVZ+empQpvzSqmnkcSwthXuJJsMUmV+Q7aXSpW2UpWip1RNGX4722/NE8qwu4toqANCiDclnQZJGZS7MrqqinN22RzVfbcpwsAZeu1o8CHapc3mNohxuy6Z6EjySjR4SLOmSDQNFayMQ0/wq4TIhyUT0bI13yOb0yyvmdY2nOKq3WZ7bbEDslYSHkoZCrHmsHhzU+ONDbjZkg1dlC3SxozYEt/5EZ0SZ5qdURIrsPRAsEdRPNHJTJkr07ZB9wt0dRGL4dR7M2wPaWiBAENyjbUzVy7iQtgnvtvmy3mXl1O1XvU7jADXjbEudHZ7O1MkV5rCVoSVvDXOZHsuAraXWn5ZLA6peEkGmtW31xIQ6rxwy4jboXIhpZQTqHq7ObLqZb4uFu6aS7BUsI7dGlX4pmyDnR/nzrx3j2nO1fVljRwI3S1ipPYXcTe1OFmyrPWl1riGOqwaamuoHgOu50yOp1Gjs8x0c0Np1yJFqRGRWDsQ1NTG9/vDObWuuVtvQeJwedvFO53BGUZChLTFsZXaaIK+CynotjpVk4jxy3M/i7ezWdof3elhO0SFZPrWJeuIkuMOjbhJNXVHFvm6nisMKnWC0VUNVlzzbjq396Yhyh0X2UsLZdZifKPc7Sph/K19OlN0EZHIGQlK+sTBnT6wisUgrDmm3HHYaTklLPYgFtqysOqwsUg7O2YL1t8CXYGTKzMsKFzlIIXDVN510xPdGU1DAtKfK8dS6fNIWgGtM+pDuVlNqU17yNxBrIX9zENBtljv1EhVrrmKH4/ILr1cg0y8WTVs2fb6ZM9PC5oWeLYvj2Hr41KfNliGaddeL86QQYWdKdx2VO8jXXfGJIDoxeHCt2xMnF0kvprGNkTCglRitRPYrVOG+p7qucw8iXm9waZ1Fe0JSQmyTpHVTOx5ZVWAYo63+wIPecYoBN5YbNZ2baLKlgObJquzIZKndZBa685UlaSyy3rgpFWjWeG2X0tRAean4Qh8eWjahRSGhyqRc0K45OYZrSSCsOf5LoHtITjcFtftGb/sbNaSq3Ura5Il4qFscKK0XrmsbV8T/bi7pJFFCbgC03ujt4FBYVgai6Fi1avBczpcEDYdWVZpdthlRKFZZnWIGhI/IWKyKmLNHa55PeDVOttVjHpAncjGS2SXsCKVYlGUFAw/WJqwqHW5P0sAtY/UkjwlubZsscWxh91ciBTFU2ge46bNEJ775bKelZKF9hjRzexlKbkId7H9mRf4DsgXrneexsmuA0Mwd4it0rk6jhQMlbQRBcNQTpl2gfs3lqT3zFYU8n2X7nYt5dVsh6RBtqltkkbETiMCCub2uUTWNDI9RaxoVP4ew+3cvTpFzi/jQjxdIHOJOz9YC3u+QTTyJmGU6cbqaTVI6Pxsh7Jkx9T2lmL7FNUz7Rx0LrrTTISV952xZVxXJkL+KGr70EQsGak2Gu3183kKWsEhb3pHHuQUXZeW2h6J24Lgu9OCX6oE3LZZPCYGWS5RJyM58t3cKZdXm3CFtU7KkZ8ZZcrtfSmwjvxZMWih0hfVJTNAAVxPTTWhnycNLqmDzKj7fBYu1ltj75q1fU7MADdzdC11kV0eYL8eeHJtXXJlGcv7U6ctloibziWBPLCoLtL7kxdXV2yXybdzZGpbYmgj6RQYZHPrL7x62O7kleUo5cXIBenA82y+w05Hud5Xl6OsmgN6zW6RMqCmS2O+Xxpr3q+UMy/5Hr8hwGydMV7GCA2+lXvtmtNRlKraSnf3x967oIKsu17crqw9dbLrSF8BOIooZY6vVDtfz9aHPaN2TaQCcr/eZ4KkFSuKKVyZC4xuuqMCv5L1pozqzE3LWCJd/NzzyNy0bkeH9STrpsQijggX9MRuz2ivK2J47IeBsCCpIAXENa16PJnXS2rI2tY9ZvTu5Mp82fENxDHZF+ZGEVmpOrql4DhCGPoEQwO5mbPiDhf3dK+LTltLOw5It3NgmfjVK63NyUOULEHSfT3t1ntevczMK1ASMaDLzfV22E9VedmRZOGyynJRoiebOyihwRyqMpZj+8qhnLnpprwkxjNxvd3YBnltduJqQV0P9FGrEsrFW63idqbPZ32SJmaUw7lDTKxpV2V4tdq2rs6dRNG6ZRmlTRcsepSzNNf9chrbrZodED6f7RuyOEqKqholacmlmhru7srRC05vVteiYHJpeVWQc24WQhRmg5tZ15Jy9jS216tuUcWcqbMsHIrY4UBskNhBA+V0CLnuKt16zLX5EJnG8wWmDnFvrubOHhNEP1PEBBxOAiZYalj3ujdb43rkkaCRD4y0PxNLwTqsMHMB+TQBO4Wldi2wqdOS2CFbvwqowmQC2sbli1e56mwat9MLkYeIiWFTzK7dm466Ck4NW2Mgdt3FZ1C0WTDUSqFBd9udVIBtF95pkOdZWrZTgsDyZZVb+9TWYr0/6jifDptayV3BZTWeIWMUBeiR3M5Eo9BFKjsf9tdttHEi/GoPMiXxDkeGqefXMbElylaipWYRYMiKjeMa312mXakQNr2Mqdozwxti4wC7NSob7i+JXqvGFTlns9TRwU6zT/5KOjsJICPn1p7gwAJSf0YNzIzgXFxpNJWycMba0hjDpjRubS+DGGIGDQ74wQvVgqfsothyN8TaLruIITan1J0jRx9R8YTbLfyO7DJpVuJexS+vZDQNhOWqlOlgyvXyijnyhOcMM2Nen29tx0e7I+y84hXRVhnBo0ktCxyJkjPFZkk9lueOgHNB2fRwMsllpidvxClYnBm2y+ZIPBOCG27tDE1qnMt0j8xz0vfY0BrQIcSPermQ9bhcWzXme2dcvAWnphEYLd5ZhtFMhQrbehG6mk47xrywzowO41BVAnGKLI6cHQ08wcyME7HS6s0NTM+Rw9cY1tLx8ugGIi5kXk5heUtesvagUew1OLs4FeKrm9dPY/aSHrDeOEhzv2uPt9OcmAo6UHdS4OTrCNL50troqxui46p1czwpMJrM3Q6siBROEVrASSkiTEDJbePMXLtTgQ/QoC2WPUvzzFmerrBTw+jelU2EW4wI9lVkZI0OdR2fHRcswWxCXZScjmOP/HGx9WjLn1s8uWyW4KS6XLrz4s5Q+b5Ya4w4rxr/Ng2zrsDkuTmdJWaftBzLq2zpYWhzw13rFJHdMpvlpexFTnbq8xlYNDleNsmGGwIjbOHwMlO73fRIEXF9bt16gzptn6vFDgYVLOY+Xa2wzYrD1trKj8OraPcuL7peNrtOPTJC86rphg3nNkKAHVaWpLoqiPFb21Se7dR0hyH1OrihTtWc4ojCuBrxcH6bLXacAPcZ6sKHG7Nbc5XgGLi2rrG3onfzOGFWKpIfrLPGnm7AxoOBtmxiZ/RBq3aWGcfErVZbut+uscxiBSTH6+wCWDh/+2qcd0i3ygIfcYuzP1zmKXo5WedLsAm92tI8HGH0xvLIGSobLoXhxHbWdBen0BfAm/GOMxwv1Sk8SwMcj6+8tpmXjV3RS1/zsTZwTKeTEE9CPcq0+i0wpxq+03h+PU9lX7jNyLPiBkWa1nRMY9axAmfNG040eoaOGj4nSFuTiPtwT2+VxarQEX8nbfXDSerXrL/MrMbFSrEsWwIjVaVsZ3hTAmyT4URjBltYNnNqhW/8EiGDBeFuWaKsbUalyQ2aLwqIZzgHar0Tzhc204XD9CAymbZbUw3qZqIV+tiRXHepv8/ta0qjeUcYkUrIFzgvrxezCynIDJ/6FbNke6zC9LljqdWGpJteo2d+EA2z89DMiCMnxZc0NboYMvxArN2Dvw/nlc+k65JFb5srnBxrxgUcvTN2dJY7WHBdxoa1C/gNjsXzLRXtpgUT1TdjqjQWf2V7E1+ftDj36Nxqmq7tWX6KSdMpqKKE47iffnr5+DKeUD/Pmf/uN8vjod//2tnj45jw/dun+yEzsL3Pd12f/7Zlv3x8qd0I2vU4bW3SLngeSv6ns9ZP/+JXF6OQ4fHV7fiV2bV9P6Nv7WD8r0gvUe7B1fXw1hRpdz/0/fjiwMkpB03z9jzcfrm7mJXjSfl3Lo3X7v28+a0t3ryoKYtmPI6N8vHLIOBFdvt+GTxPoj++eAOMW+Q2bzhFvoG6HJ1+fiMCfcVekVf05ff/B6fDz5v9JQAA -->
