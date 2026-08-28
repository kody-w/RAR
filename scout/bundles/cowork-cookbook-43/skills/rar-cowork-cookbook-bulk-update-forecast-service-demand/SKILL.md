---
name: "rar-cowork-cookbook-bulk-update-forecast-service-demand"
description: "Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_service_demand", "rar_sha256": "2c782790ef283dae3793c594a3461524ae8cdc4f14f0aabd8c860afd578af2c6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_forecast_service_demand`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_forecast_service_demand_agent.py` and in the RCI capsule.

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

Forecast service demand Bulk Field Update — Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 2c782790ef283dae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_forecast_service_demand_agent.py` first:

```bash
python3 bulk_update_forecast_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_forecast_service_demand_agent.py   # or on stdin
python3 bulk_update_forecast_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service demand Bulk Field Update — Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_forecast_service_demand',
    "version": '2.0.1',
    "display_name": 'Forecast service demand Bulk Field Update',
    "description": 'Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-forecast-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8663fa48784bd1b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/forecast-service-demand'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-forecast-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateForecastServiceDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateForecastServiceDemand'
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
    print(BulkUpdateForecastServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxpbvV2Fq/rA9qi52EH3DEQ8kITYhCQRIcjva7CCxbwL8/N1fIqmq7fH1zPXERDz1IiAzz35+52SiX1/stony6uXzi+7bGbS2kySO/AqyMw9a5Le8uoKv/OqAf5CbZ00VO22TV/XL64vn124VF02cZ2A5WxRJ7NeQDTltcoWC2E88qC08u/Eh263yuoaCvPJdu26g2q+62PUhz08nPuBpXnlgvMpTwBiKs6JtoCSum1foFjcR5FXDp6rNoKLyu9i/QY4/kQLypGncvAFR/N5Oi8SvXz7/9PPrSwyuXz7/+uImdg0evXBAIOMuCf+UQH8IsLzzB+sTOwvBxGIAtsjAfeFXgEMKHnl+AD3vvq/9JHiF/uM/rje7CusfPn/JoOfny8v0RwMiNpEPNTlg4XuQaxe2EydxM7xBbHKzhxqo2rRVNlmpBqbMwrfHym+U8gL6cRr7/sHkLfSb77+85EAEezL0l5cfoLwC/IA5wPXbRKX4/oe3JL/51fc/fKNTt87Fd5uJGJD67evz/kkWTPw2NQ7uXH8EVB8udfwvL79Tbvo85J70BCtf3i55nH3/IFxUeedndub63//wV2TdyHevkz//Jbo/PQhHvu0BnZ6C//B6N/LP0Oyp0AfNv2ZbALf+HU3A9Hd2r9DTUH9F+27//0Q6iTOQAO8W/6fk/tmC2Y/QT3+p23+14BUKvrws/STuQHQ4if8Z+vWrvlstfvrO+/bwu59/A6T/WzJ63lbuncJXkBNx4NfN168/fVffH3/380/ftQWINd9Ov7ZV8s9o/jO73vn8wYLPWd//cS3gb2TXLL9l0EekQ7/mxb9Vv71Bpp3E3rfn9Wfo9/kyfWbQpMQ704cJfpczNZD1d3b84eU3ABEZ0KZ178Mgy//936FNPIFUHjSQ7uYAfoCDmzj1J+EPUVxD4O+U2wCB/KqOgWGf80D8Tx6eJM4D6Jf/495B85P7BE14QsOvDxz8+g6AX58A+PUBgL+8QQdAOq/iMM7sBNLY3e5LZod+1kxsAepN8wGgOEPjfwJEPk0XACahX/4F6l/vhN6K4Zc7qMcPjNIW4oRPdZv4b5OOVuRnT41cAMF+77st4JHkLhAoiAG2vgLd6zzpAL5N9qivcZJAXgx4gnow3GkDm32eiP3yyy+OXUdfsgeg4tCjUNQwmPAhDvTpE9AsSOIwar5kvhvl0He//vYd9H+h/2rVnfjEYwew/ekRIKGkb1UIZFibgmnAWcC9AD7uHvn1t6d9AZkMVDbgvziYKtW0GETo1ffeja0L7CeMpN7rC6gjedUAlIZAlYHEAPqQFzCdhiYcj3JQ0Dy/8DPPz9wBULWBOh+WzHJQ7kAY1sHwCrW1f+f6i1PZdxFTkOp28wu0WexA1cgT8N8k5n0SWJxnMTD/Ryg8ngMi1Xc1xL2TeIPUKSahwq7sIqrsJ4/AfvgFVIv35YC4DWX+7Us2VUh/MtU9QR7mAZOAZdynSz9NPr9XWODY+p33fY491bbDvcZVX7L6Gfx25d8LORBlgMI29qaS8I9nSNVR3oJ2YLIfkHSi9PSC9/TKPQb5v+gPpvoN8feG4lHGoS8thqAE9P+v55jEZddrbbVmD6sltFIP2ulhxqlJmsz96KtA7Z9EeKTMt37gHU3eQfVLlsQgJqrhH4+Zd+M/5zyAqq2ArTRWu9MHngdmnOjeA3MKtKq6G+JL9o7er8Aqd6gCvgFZDKJ8Cq53htPou6QRSNXp/lslf1pnymkQfFDROgkIjMD3Pcd2r0CqakqupxNAlPpTot2i2I3+oBUEqINgAPQhIEQM0gUg/N10ag7UBHl1t/7H9Hjqj4AUXusCaUEX6r9BFsiPKUZq4ADQ5ExzgBW+u5OCUh/YGIj4YeE6souHMFPj+hTQnnyRp1NQ/M4Dz8FvEX2XZRIfULVBCAFb3iaQ9fz+4dkPOZ++AsKmUw7eF/3R3U9dod+XmX98ye4yfuA6SO1kqtC/Mw4EUiqt71g6IVMN0CX1nwEEIuFejN8e9fRRsD9k+fynbv37v9fQ3yuk8UfPfYaipinqzzD8qGrvRe0NZAEMYiQu/Ppe4D49ku7Te7Z9embbp0e2/YH0w1Kfob8n3h9IPOP6M4S+IW/INKQAZlPgPj/AGotP3OkTMY1+yTT/m5ufsTABazKAivpRZd6ngFITVn44TX5UnXoqVjdQH+8wCxzxJfsIhWeiABTPwqlE1vnvEvheboFjH377qAZgKGsAb29q0UJ/2r8kk/i1//I5a5Pk9SWzU/9f2rdMmA/CFZhj2u+A1AE9TxP797uP/me6+eNe7Z5UAA28/POUW6/Q1Ku+Qh9t5yv0vhG4b66yFuyEfppa3oklmAq+PuZ+bAQd/wXsvZqhmER/7G6mTuvZAf9ZiCmlgMSuP9Xx/CNHJ45/IgIuwtCv/kxke7+wkydQ1I09VeW4eU/vGsjpgR7nFQLOA2kHMgmYrgUL/swG8Kn8sgXlz5vU/Wa/b2rlD11+u5uheWwRf315B4ynD57tIJgOMvNTPRVAGAQqYAjuHyEFxv4njeKTBEA50KUAGphLzzGaQfwAm+Oe7eM0g7skQ9g4QaEkRtj+3PVcIkCJALFtx5u7cwqxA4+k53aAuRSg94jNr4+yBkj6SODjDIq5Hk5hJEkwKI3ZjGcTtG17yHxOI3TggULwbekVQORT14dukyE/etbJJk+Vf31xKALMFIhaZB+fBcyYNkXQjho5M5oKwvIynyNwpTcq2hLWzcqMW4rtOXUdHwr+apalpK2w2SjmcSGnx1Bg4X00yzXm2uFbUc+kOvaPSmQrXLPdasN+t5zDyZaZRcLqqFHyujAXRaPYQ3lsGyM2+uZ8XkszBJ3JGlkmVhC3o3xoNBmG4dLZLjrluKirYhXlweZ4uWjt0basmrcbh9vKRXmQNyZ2qs4LHjEONjooViPNJBntW810mgLV9LhStaqyyVV+jQ19g2LlrDvbwgGjVGGMES9Thrkfi22mkDC84TadOmouKpd5ZI3lxU6QTt/wmoJrZqkPiZhtKS2blZc1KVuoJztXjzyUxVmxaGqwW0+mF/yqz5GqBHrafjai2dwUj2Uq98hqM6/iNVE2oSyS/abq997+VB3LSrH5hYhTummhlONdrvYyi5pChTXcOmfHsmD55XZfs2RzFce+uyZDdipNI6kvyOpScPvaWSvIEEV8KpUEulXxLludOZc2YixkZaovZxUbn2k7W8xOLVrjV3qt6y0PO5s0OhOOaafnmUBc7JtQWWTIqKiLcHM3qIdFbzpco6a5ao/+4EnliSok84ppcE0ZN4pPPa05yX29G8dFwlnXrattDiKiWfUxPZSXQL2WJIMvi4N76w5bJehaRg9Wduu2qYr7gsO37hW1zi2ctcYYYhsizhPHRAs5qg2vt93j2pGsHY9ffJW3ytPSiI7dUjCLNb9denNUUC9KtJtLCOnL4uEmYkN0OsysrdQvliWDsJVqMNF+6JgORw2ppqoSieHrnDxZxXH0lt1mrq2cwvCupKRmx0Ldo6QamKR6NEn0HNQXZb8XqLN7JOQdcbKIDdwgTJysu5rf8vJuJgx9v6tw+AbvlaVI+eWcIvEOsyuFOAwGfWpUKXF8L9Lj8UghZWMflc2ukkc39/b9hcWkvb/BwuVtcebbs8JbXqjsmJ1sXK67mbelFinRLdj17Waqh9O22ewb4uSIxNIBwbOMartvF36r4bo4yCcHW5B2LMf6+ZAknn8i3IPWE8TRlfNh2+F2m+6doF4yMUnMidlih8F57O3mZz+q3GscXDdNdTtkaWAnVeb21nrHzJ3AzLmh6I4LGJ+JAqcNhuFTAX9xo8BCj3xbBxdjzV90MeTR+uDR+5l7OmwMwl7AMaqG57AIInWEud5izm0jGCKsJa6hNYRIeWIu+1Su9EfAcqS2c/TUKN11i4cLErdnu00H92VVRreus8SCLBm1sbcXgIBI3MG6Lspkq9ryBWEwe5/PF9qmZIz2ImPmxXSGdDWQDk+e5Jb3ry53Yy40lW6lW4a0lSEZwbXAiWtWmegpPs/mV+M6Xg5D3hESfrUX5trg6eCkZLugORrErRDrY5MbNamqPmK3lLI5bZEhGUQaW9lyMkqjWqgrUZalwvRzc0HzsljfYLkltSH0OMCXgisuRynXcWE+ysaEo+2DMcs4fzj1LKxhJ8w0iAN+k1PYOHK7SlDT0Wr822y1c6oZ7jUzVjwFuL0SRHZcw8aVzB0J5cOCCNa6e16H4S3i4bN84dwlS7pcn7JIYK4XclDPTs0JWW8yaabMxrnobCQpO5cbcRZIBOmO0jWNDGHTZ2Qe4wOydylO38oE79gppksanCPlaqiZ+LwFMCL61+tKd6PrAnFcvo3p+CKK/DKUWyQP42IpgGzzrW0rUmOLsydWv5psdRHd1MyS7RhVu2XQbn1YPe2RRdCpbH2whHqXkngzy3Sf1P0zgnZXHJSeLqsoQpSE0KjPZSYc8Z7S9Qtfzjan41m4hsQq8RBKSE87uDuztdb6Oe1Ft3A7t2czeKeMSTDGJc0wjGHpuJHM813EG6eW6naSOuorLpIlUdOLZUq4Q0OUrFEy1jZFB1Yd4xVvjmVuRMRayhuN2+3NsK9TtHTTYpPmDCOxyup6WtvnymB3rMEebikruPsDVvvmxjE8AzdE2dyCLdoSO1vz2DzzDlkjoyGObrLGLcIJV7TTkU6QEmfF04WNFS3EEb9ZijvaES7ZnmqSR1tYkElnryNxLBl+6NlEPEa0fNy6Y+Uxh5iv5j02bszVZb12I5Zh5vrZbB1V2GzbiqL567m+pVGbXEyx3hT2JU2vptwxiKL2ai9upFHo7QXRGe3C6MS10p50JcH6yI4QsMU/uokpGAouzgh2L/Yltpaqy2jgzV5vWKxeyXYRltGhJ0GjoBBY6YV7fYVwailoUngjVE0SxJjmS8LK/aAkxJ2gJNRwLMFGK4wGjuZcQp8fWKI4hrXbXA2QG8qe3juJzOvksHCUWZ4iiLNhaewc924hLmJ7pjqbhpSOa3J34CORjENsLsl01wsYjV4krU5Pa2m+bjE1m42qbm9EH1Su7b4VDpcY5yqFOu8Oo6aqoEW87aimupI8cdnjObMS95E/R7PVrJ+rdLfa5Y6VllYzZBoWIGd5v7dSo8lKzhs5wx5yd+0KhWZaIWJJ0qgp3nShFckpvlyMk6ENgSVZHbFYGoyRKjjo9I67QjCwE8IigxdEyLYpObjC6lgbNsedYnJcLSTHYE7ai9bTLfyyOKgktWvgrMIR77bYiH1GBXlII91IKZHA1V4wP2QV4zjKEinn3cGxnWONn2NaOJSBjO2smOW0IuzZiECZXVtf2f1iteEXXINQXr+zKMtd7mxhWA3y2Y7oGhXmRJPx24NBntCU61nztMgRktSLcXvzDzwSKZasAi3RI4vzMjGQ+pWXGYo9MgVBBlWibYVj1hg5WlHG5rbgwg3htFo1HvP1BlshvXBI9VBDB425hdLRicuFsFNHBNvXhNjbsaZIuuqmuuht5kOAcpescIuO8lXp3O6P17G3kg5frAk/vRKFhRyEhCuPu1JrgpWGFZnMp2xxawIJO22uRUwg1wM7GFJoogdXWNAHwo3K86Bjp22uWUlT9yamOZu5eKNgrhs8BFukDlIwh4Q9r06gH+SHU2SuPcks50p6aJWBPwe0pcMHy1/MQJAy+c7lZog725Sxp/eo04x7V/RPMu/uzgsLrzLnJHXJuTgY3oURLN32lTJiL520gXkDp5Om2aRBR4snDje1DemSa/GgX9fSTUn403rJCTw1UhGSL8vh6ssrHfP52Ly1GYu7orkYeRJFhT1jKzenWR+w2OS7hMyLnSaeMYqEl3P82Elrku7lNJJv7TBPrMRGcp1U+JLFiYW6Ysb98nISY0TQEWEmo+qwq6zVqjZXBamdi6nPXoOtde0qnXi0zeXV6g9qb0bD6pAKNrZaLeMNdhIab65QhrJdc4u+MAssHZxsGR5oGF0d44Krt/ChcVGzi1JNiZtl0lVh2DTVRVvEpMwNScJGdYgTac4VKj5ewtojtAuNUoHBRqxjBJm1R4f1mceobqEZRcqtfHwez7P8egx2na50B/RAo1yKgV7f0qIE5s7eZQ++0NhpzsjGDvKg2WscKC+UwQxazGpKV+XkKkmUxND2Yu5F4WbNDba8k4Yl2GusHdTmTvm5zqQGbKZTJIKv6boKqeIm3NhKR4bKzbbLlpo5CH9NSSnkbhJKcHNytuQltNyg12OSRfnWwPA65YXFidv6xinDGO2AICpOR2wb8wTh7FKu9FUFNPzMKh9C+ZT0XkbvzY03dt4OJ/PFZTuT6dreZGDnHM18jYL3NNxTik0FDnpEXdW0hoauQcFsF3h1nPkMFjHuMgna43mj8p2zjtr6pPSGjrSk51SHi8k7BdksbjG1k4j9jVjDid7SrUfdKKKnqN6u3HQct7UY50NNsXkWsXzfMc5Wmons9uR2cpE30XwNEyt+KynsTR3McK+ieJJby9hEE19ikWjWCCsXay9JfMJnY9IJjWV1UX5QaRmbUSHoZ2FfQ5ooSJXOwULYREguo2kaZuKI2dfcraoCeDzAwkHHqs5z4aUCVD94ie9GW6bbH/zcWlFx0LvMcqPht+zAMd5srnsIn14RYkt1Z4/YbzZcISE0sVTVnQh6apxr+GLcDWc8GdrK21TMKPentcI6Z9V0LhriLyMhKZpkM4aG4LYVnuy27hn0IIN6XcoV6FHzXg02CTpXb0JBrsZyRXOw5qqMyXOn3o0ZUDriOS3b3VVhhNbF9bVcsWY7i8KRSQPH58Jh5Siat3SZNeLD3oqi1OXACLM2vRgwc4JpMNMCsMOE15pF+euSJGcrEtk6fpAy836FKceu0Xdr8eKwTatsHAFvOuc2V+XS4dExBOBN9fhqZObwxeuuKwzZG8TWA3suyY6v8KpEjWu/NLc9MB9Pnv1ekJABlrL8vF2FC3W0JGqWnpLqlGh+VZCgVQlA2Eegn3ZnvHTp2KZaZR7FuZo0o32jdr2mX+bCCLbHtubORPcYaQxO1rsOR+o5k9YkiGjBCBGjR2Yo6JpvriZofKrTnGgoprPCbhiyXpFL7mh1JLPPnVxdn9IAHnJKn6XbMJmlbW/jJN0cT3HaGhicNZIXO6mNHHf2ss5wx625GehFosadX+BVuyetNXHpzo1bYbjT3DIl3xMSNRdW8Djtd7bc/GRvO7ARctGQ0HOKRmljTuLrvDNPHj5nSVvh6mLb+hZxZHZVEZwNGsE13Icb68xdStza9wKo6gvQuc9X8Ym7LeSsUXF+dlG9oxdr7DIhZn2WE+3BrC8F5YdefJTysg6QU70ZbSdYqr7I5R7GVK7CLUmn6WApaDYd5ZCC38bUHOH85UxY7paku1VPcE7vBzjxV0oF412/WzKLi9VadM6TvNvSJV0plUvMcGoH1013ng/reUXxGB42gQbii9VIjYwX9oY7nFATt2Y2nOArpAwJLafMiq7KDqRVNbf9yNYXJ17WZ0pGz+cGz2myazkXbHs8xj5pesOZRs+KEmjBMhGXJrE/uaDtb5YXRCR2+UbI5c2qVtFglR5rFyvWhbGeL9v9iDbFjGlUjEHEeWJfuRNb7ug64EgqPGDu7oKUSoxJVa/gmZCy/CVctEKxT5rwkjJrc2swjHXWNxQ7apilh6eZSVtLPSel9qyjwgiL1qXaykJ2wDOABszAcKxOKw1S3I6kZC8VQSr8hvD30TjQnnPdHnFna2QZO3K1E9YLHrdj7ngsul7hDAVVyKyqhKblb7sN2Povx9uaGrz1UPe+sV6n1GIBdl7DfHszGUTn8VV9dO1gFsQksLgq++NVXTYaQC27wLZwuBkcHvED/cqy7I8/vry+TEfSz4Plv/PWeDro+187b3wcDb6/ZrofKvu29/nO6/Pfkurn15fKjYFMj5PVOmnD5yHkfzpX/fQvvJ+YCAyP17HTO7G+eT+Ib+xw+k3RS5x5bd1Uw9c6T9r74e4rMGI9/byh/vo8xH65q5YWzX3sQ5WJ9lOHJv/6/GHGy/QLhOldj+/FjznTbfg8b3598Qbgqditv+IU+RUA4qTu86XH5IY35A19+e3/Aa8QdBi8JQAA -->
