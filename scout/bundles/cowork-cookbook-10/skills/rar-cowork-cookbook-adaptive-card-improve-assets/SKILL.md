---
name: "rar-cowork-cookbook-adaptive-card-improve-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_improve_assets", "rar_sha256": "55051c82010aa11493901bd2c97f28837501a72c61a445febbed46d8c9978274", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_improve_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-improve-assets:61ec71f46615fe5a18329922fbb080a19b3c9c87ed43fab732008496aafa6cca", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_improve_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_improve_assets_agent.py` is
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

Improve assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-improve-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_improve_assets_agent.py` and embedded as the fenced Python below (sha256 55051c82010aa114…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_improve_assets_agent.py` first:

```bash
python3 adaptive_card_improve_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_improve_assets_agent.py   # or on stdin
python3 adaptive_card_improve_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Improve assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-improve-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_improve_assets',
    "version": '2.0.0',
    "display_name": 'Improve assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-improve-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-improve-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8fe7b5cf53c063e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/improve-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-improve-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardImproveAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardImproveAssets'
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
    print(AdaptiveCardImproveAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+XPjRpLuv4LV/mB7qRZxH5qYiAeCJEiQIG4ShHtCxg0Q90kCfv7fX4GU1O61PTsTsRGPHS0RQFVm1peZX2YV9OuT3bVRUT+9Pmm+nUO8naZx5NeQnXsQV1yLOgG/isQB/yG3yNs6drq2qJun5yfPb9w6Ltu4yMF0uS68zvUbyIZqv2tsJ/Uh1rPB496HOLv2IEGTDlCT22UTFS1UBFCclXUBntpN47cN1LR22zVQUNSQnzm+58V5CMU55NlN5BRAQvMMHthxCn6DMbpvZ80LsMO/2VmZ+s3T68//eH4CQtOn11+f3BSIBXZ92DCZsH0oZO/6wMzUzkMwpBwABDm4Lv0aaM/ALc8PoPerHxs/DZ6h//qv5GrXYfPT69ccev98fZr+qV0OtZEPtYXdtL4HuXZpO3Eat8MLxKZXe2gAIm1X5xM2DUAwD18eM79JKkro79OzHx9KXkK//fHrUwFMsCd8vz79NC3561PdTd9fJinljz+9pMXVr3/86ZucpnMuvttOwoDVL2/v1+9iwcBvQ+PgrvXvQOrDk47/9el3i5s+D7undYKZTy+XIs5/fAi+A5nbuev/+NNfiXUj303SuGn/Jbk/PwRHvu2BNb0b/tPzHeR/QLP3BX3K/Gu1JXDrv7MSMPxD3TP0DtRfyb7j/99Ep3EOwv4D8T8V92cTZn+Hfv7Ltf2zCc9Q8PVp6acgqOspzV6hX980ecX9/IP37eYP//gNiP4fxWhFV7t3CW+ZnceB37Rvbz//0Nxv//CPn3/oShBrINPeujr9M5l/hutdz3cIvo/68fu5QL+RJ3lxzaHPSId+Lcr/qH97gY52Gnvf7jev0O/zZfrMoGkRH0ofEPwuZxpg6+9w/OnpN0AOOVhN594fgyz/z/+ExNiti6YIWkhzi66FgIPbOPMn4/UobiD9Pal/0Xbb/f4l836BwN0p3QFF2F3aQnwNKAkC+TB5fFoBYLZf/o97584v7jt3zu13GnpzAQ+9vTPf24P5fnmB9AioLOo4jHM7hVRWliE79PN2UnYPi6bLvvSTPmBL/OAbldtOXNN0qf836Jd/puDtLuulHCbjv+bAGzZwkQe1flYWtV3H6QBIGLCTM7T+F8CngEHqIk0d202g6UdXvkyInCI/f8fJBcXCv/lu1/pQWrjA6CAGHPwMXN0UKSD1dkKvSeI0hby4BtAU9XCvKgDh10nYL7/84gBm/5o/6BeDHtWkmYMBnwZDX76UtR+kcRi1X3PfjQroh19/+wH6v9A/m3UXPumQwfrvWIEQTh8FCORjl4FhDTQFAyCbu79+/e3hhMm6HJQ/kEVxEPv3yUDaN+dPK3h45sMtYM2TiX79rul73KBrBHCB4hagBTK7ef6aTyIKMLS+xo3/AeJj8gP6Dz8/9Ew+ad4xBH4K6iK7j73H3eRMt6i9F2gbQJ9IgeUCv7aTR6OiaUGoln7u+bk7gJl2+82FOSjEDciWJhieoa4BS50k/+IA0RM4GaAku/0FEjkZVLciBT8mgO7qwewijyfHvwfq4zYQUv8AYmzxIeIFOvgATai0a7uMarvx7+MC+xERoKp9zAfCbSj3r1NfkPqTj+55fI+87fetgvZoFb7vL752KIzg0P+nRmSykuV5dcWz+moJrQ66en6E1NQ2TSt8dFqgLbhLvufHt1bhg1U++PZrnsbADfXwt8fI4B5FjzEPDutqECIqq97lT/lc3+XGLYiFybl1PcWv/TX/IPZngAjwRDNxFEjZZCKA4lPh9PTD0ggsdLr+VuShR5hN4Q8CGCo7J41dKPB97x7rbVRPmfTuARAY/gQrCH03+m5VEJAOnA7kQ8CIGGANyP8O3QFkxATzPbw/h8dT61Q+HOpBIGX8F+g0RTCIwgZyfND/TGMACj/cRUGZDzAGJn4i3ER2+TBmamXfDbQnXxSZ3fq/98D7QxCNUwUB+j5TDUgF9NoCLK/ACSCTbg/Pftr57itgbDaF/X3S9+5+Xyv0+wr0tyndgI3fmB503/d4/QYO4Og6a+60A8pq0oCEzvz3AAKRcK/TL49S+6jln7a8/qF///Hfa/HvxdP43nOvUNS2ZfM6nz8K3Ed9e3GLbA5iJC795rPWfZlK0Zf35PrySK7vZD4geoX+Pbu+E/Ee0K8Q8gK/wNOjfez6U8S+fwAM3JfF+Qs+Pf2aq/43/74HwURigFid4bOWfAwBBSWs/XAa/KgtzVSSrqAK3intXhs+Y+A9QwBj5uFUCJvid5k7rWny6MNhn9QLHuUTqXtT2xb6024mncxv/KfXvEvT56fczvz/YRczMSuIUADEtO8Bz0AH1Mb+/eqzG5ouvt+w3fMIEIBXvE7pBKoY6Fyfoc8m9Bn62BbcN1l5B/ZFP08N8KQSDAW/Psd+7gYd/wnswdqhnIx+7HWmvuu9H/6jEVMWAYsBXTeTLR9pOWn8gxDwJQz9+o9CpPsXO33nBkDfU+0DJfc9oxtgpwe6JMDa/ZRpIHkAJ3Zgwh/VAD21X3Wg2nrTcr/h921ZxWMtv91haB8bxl+fPjhi+v4o/Y+QARP+pdZsgvOjpL5NQu1p6r2BuqN7bzbfwMriqXT+7lE49QFvj+h7egXk4j8/TRjWMeigx/u2+OlhCVjCtzYVSAA08aWZWoE5SB4gCRTocjI/ART3OwXT7di7j5++vP5lb/tn+f5KIr5LIQFOkggR+ISN0BjKMCgaOA5MwzbCOJjLuDTlezgW2A6FoTBM4wxp24FNuq4NDJj8l9nvBsyRCXlg+ie8/1av/fSYC8oCSpBgMkHABOLSIE5g20YQnMEYGHE81GWoAKVpjCJgxKZQl0RsHAcLcEA/gJMe7TIMRaMUPsl77/geBr19dNcfvnik/BsgyCyezEVt26UBJLjHUGCFPgYDBHwERTwK82GCwQKa9nEw/3Pquz8mdz3WPEUpaPZAq9VPen599+8UeSQORm7wZss+PtycOdqUuXdukcmMZHAuLnQhaHohbUyt8FtpvTqi2DnxLjMFTZAVTrLCOYm6xWkR7jX+jGRNuiTYfBSWGEZ1u+V2Z+CkqZC0G6KRhzL+3Jvlm74Lk5VyWRNd3ArubuDbo2Uc18SpseNWMtLU4AtGtqxsl2NzWnOupX4s8iEsSi09OvzJq0Sp79fMjF5fbDM6oo5Wxim8B4moSsxhd1QyJE4rlzCVzo1T8+zxcHxdXW/b3F/Px01WE6INVGyE+Bbk1sBIWEkwgkv4/YjN95HaI3CRCBVjmGFqHdFWJ7N671Yd0sY7NTrfELWZX0+4KXgnvl51Ap+dif3pRAZdke4vuozvrEgRkKNXpZqbE8Po79Lx6Ahn82zGlmIuLDsX2Eo6jPJRQ08FZyNDDWeVHtPX5IhEXmaeKT7DYFOSFGbZOoLgEUW25G/iohETZuOvqU1mUCujSuC0SY7edruy5rlLbGvRd+TTYNa5zO60YcCEdbpgr7STCUUgmFHnLmnLSzNH111L0BADP5BWXBvFMc7mZhMJaX5s1IoeXXhxdQN64G4rZ9F2WXGwb95AC+W5KepjgmpzF+GPVdl7amnt1FAeESlf8MnB1XfHVB29q1QSVYtTOuWQoPVjNUVdUO0wgNSeK9UNpYq9RXmiSg6WafEmGpTWzd2cTyvLqA7EWbzo2LAb+pNVHeheXI5ljOsLuxFcdxWcYDPDW/1qGLNDd65vx9vN2wnZfs1E3BXDG1eP15s1VfH8uaT0dTLPZPOISbe6qrkx88do4WZBip4zERZX9mpvnQKNYAxjZXlSoJYHU60RVa/rUTz1MFn0VyXozc1Vk8MiOPtqnWvhTu/pjXCJvaDPPWZFnzcCWo9V71NELfaqeTu2MUiRY2rRqKHtiFN5rFViG3tn+hDHtwsvLs/pgDP2OG9F7XAezCFN+vHELHbmJeEkL58tA5n16RM7pmvHks62NywCes3uD+p6eSp5w4wzJ/RgbcVl5FU16LW72BlNHGe1SEtCiCfOODvyZ1Ono0AW2s16R+LxdrNYEyqsS6uTNEeFTkEudLYdHdlA0b3Okxe1Dzcsj1LHZVr79WYuzEAXt1mralHT3SWqkdQbLGdDusWQ1LPNzTmph2MrR7dIvF2yZp/vDTRstnhBHvPZPix3fQXj18Us2Q+1Z2fxkKjJmRePsmcQpRPtDu6unZnoeierVLlucEVz0VmvjQKxquL5hqsIK5w3lXEaS9eB0XpWt/aqAmF9tBpWjuw9daw2R6NCGovf1bNsOxD24nbecYKb7xYBLMsxx2b0SSMbPb2ii3xebnbVMNsWemxShIvzt20klcHALhJ1nRkGT2KpnLmgRlpRMF6vF1tZqPMu3fuDhvSNKMAxb23rmLOwhh5wJE13vpDH3tosXNzRl25FbTY7Fd6d4bymW3s0y1s70tpBVnxhscHnCKEfzyLbXdhxX4u2tF02hzRADmHepBlT5IZ89vNF5MxoDA9YZrVRZfuCl6x7lLnkgu9N4Fws2USxnEVLl4G53SyszKTp+fF0Y0u1XBLLrMb2W1UVzbIKLoOErw/SltYTbNf0m5o4ZAqHLNRo36p6AqqrZG9Fhd8qVMUmhGJb9Ik2wsqumltkdf642WoJIJj0QB4ylN+7a7Tl91E0YyNKi52LytsR2xnoVaiscRGdxbV2DY8Iltk7d1vAFn68RD222ftcsiyzCMlDpKmXSHeDbyQ/Skv5dhFxcjavU9LL63gUNc4iklq0rJYCdN5kBbHp9IxG/YgVF+rZ9w+BvNwMN4UkqRxdI0rBXggaEZjNhRHShJ7pKsEwVU5irL8zbxqsiE2NIYA5GjZBBV5bMwWdEukx2t7IzlOF/Gg6tHkN1IskSG2xMlmtrcQzAwqCxRx4nfTF/MAf9ONMd+MVpayQJgRKZIdcYFwXe6teIX3OTy5wCXI3Mnh9qPShGZ3jgoGtdrv2Nd83F94y4byhUEZYMwNH4PYcdi5vx6WxlQmcY7GLk5DIXo/K7rI3rJyNqtHosWOQnHWNXbINhWqdZ5naCcVW3JrID9mu43lRNESVuZUUSyHHtjZbUhKcg9/GN3FTrWYlF87WqlsafRvhDHO4sWJ84HJ83zcpr7Rb2jKuuLm1JLO4UVGw7UibXrnGZknWrKw7qCF7muaxWLOSb6bgo1l83kpNcMSYU4UtQHewZTH9zO9tSg135spED6Al1lpktk+ihZgZe0IsDKIY2O2+WYJ8v4pyeOl26cBrnoA2/XJY98YG3uXnFW4eVaQq0PPBUTMhxjV8PZUu1KRuxx6J7cteU7S12uLacTzF/gHtT1JjrU7N3jqns/A29Do9rpzVagb2nedboaXkjaFOWHtzdNB+26WVJgJoS46InW51yeoOi3JBCqMpliXZt+iFh5WtfsyE/SxXOR22qsAXdnF949rrYMzCc35rQzJNraJah5qLq9hZIDg4Lk9FUcB1wg86OezSnlO0S57cHPZCdQSz9UGaKsuLMM7QG9MkAWMhw0lSYwLfhaIRNh21yGXlMFY6WheF2NXSYMjBvMOS+jQfeOMAqOOseCRHMSc4DDMp7wgM5oE7Y/IYmEIKSxRqNap7KRG5dJzexJUS7rYh4CDMxE4ou+U0notY1BYl4uxYO0nNmyXB2wuxVeaioHryJqMEzc6cVXP1YNvjC9KBS7PMFWnbzJSwXvClUpB1gh83EtNp5ULr/bh1bxXmVslg10mdoqVrCLOl2ixC7jBD+oMVnnVF1xNPLEmBNQUZ5pTW7apk6zajrAvoEC7k5LqzWLHdMdxhGyHBTegNT+raIVNLBD5m+GJmHgRSm7lnMyQrM7zs9YMnSpnYNfgxsfY73qizsxRwCB4ribrVU6LED0iyXW+bKherQiH1ZeIdJQ1QzXx3KM/O6rhSqMQ2Dzy/wdfoBY2uMGWlMihpl0XIIw3Zjdzt6BuIRglk6vbiydDQWVbks4H3uCDcI7riEUuiIOYLk6iQi0jEB/QWdRx6CHj0JAggGmIbu2wQVYODFYAcgUFvWJ0LFaMrP7Y95uoMyRhcV6s5h9fnLOxW9aq8aQv7mjW7Dadt4bFLZsUqHgx7d67ISNCswTdF1N16bG9R2Glcaik9FqAXjRCyysubJO2WKkwbLNpzKdCcsfv1sZVWMxYx0pM7a3fDFSXVy2W7Fq7t/uStKo8VCAUuGX2XXmvHpUNhPr+c1WVzLHYraujd5VZXG4uUqiuvy2FczY4eS416E8Fikle6Basbf8eYdFILysUI9B2auReMZ/apKQBmz/UQWRUXhbvA1fGyPvJWszSK7CwWCEb0oWiR6g0bh4A1T2xvzzCxt4XUzJ2KFlKb4/j5gIy7UjFl1tPqXjmOAbKpUaDrzHFUC+uttGT9Wc8upbHIG0T1fGc0Tsuxj0w3cZar9NbAbn6B06Hst6vQi0IJXYbXY6dHy8PtLOrVyEXKaEmySHDtvmQwWUg3S0RNDoVUXXTkNGPpjXX1VHTdcEYIONkqdLkNcTpYlGtyRRhEnweisOEvfb1acuZBHGq2TguU2KJ4Rs176bTifFA6jCPYBQ2LYrGPSPmU1LndR9HiduhGuPDiTeCpcHNzMA0dZhSONQiPz7uK1jAJO5GdptalQYBADUwzQPed2HtX93glXKJFUNAqoAN+idbKVsnbMUbWEkyuk46il/sGyaRRDheZsiVOVLnP22JzaWbVEbXnW5QdjBgQ3hi3VyE51jR63cPqUr+OLF/TeT2SV46p/K6jlrLhNdyspMmlsqf7ypVnspHNW/XsotKlC7cYsz7mOwTl2ugcSNQOpcnrbrj12gXH2Py6xhpKcWrajUZaYOazaDXfrg3rmNZzUPjjkggkrOv803HuFcvZ0DtKds2L9WUl7r2Fjnd+pMCyYmK7YlVXm1ifhcckW7K3igFFXEyufLrR83hLGq7iG2O3PO8viXyzNgus3x8O+xbbzQh0yzprLHNyBfb38dJAm9QYL0butjWWSpJruYY7SMm43OMgJfs9iPfhCtrtGW6P5Xx2UC9ddx1s9QxqzwiqYTyjyKFPajjomlHjtX4pW7OLskTywPEX4cDa+5m3cA8SZonMhrQPzNDu55I9P82ZM02pcbjvSnEWZkYYd+MCns04nNy0mDz4mRJTXo2gV4AAe4hOuZC1NYWa63nLe4For7GIKBjihomjR1ORJzdnlFVMvDo2zPLmxGeMJ5ZbDb+dc9e/EqDllm78AR3nK0zn4T0b6kmjM7M1XoLCKfi1QFCyohfXPMpXiUKviTpmD/1aoGgW55zZ1S1tnBov1HWThWcOXR5oZeh3UY4xvry5ILPN1o5m8ALZHizR6VtmT7iblXpVrLC5qgw3+jex2Ujxld+edyTDyNXOJpdOts0x2so5FSbpZd8jmI72slce4y1K647kZ2kmNNZ+4TAFfwuy2XjLL8LCl7CBk2n0TK2Cujp4GTN29aLHYqWJxnaDnLe7OdwEZ9pdnJWrN5P2K2u/vvIlg1KeQ6bZ3vVJFF8V6+v1tHGM1gXpnJKbftcOFlF3bUaZcXhb9k5TRpW8z41Fv7jOVr5yYK96ymDnpS+Zbq6GqiIX5zkvwEFr7KQL7M8T7kKVeSlQQ0NH2JnCuK2/OoBtz+C6AT+3qLQnfadr5ohTXE3zUGHhLWbnWLCZl4YssWZdX4ebPbu2NcOHfZCtubGr1pRskjqekX2eC04z6zF8P6eVxMBT2T1golWTbqMrjQObUXYOswtroIejN5+nPVzexF2NrmwptWc4V+PLfjfnqeKUhNlCS/qYmDGHta8Ymoy0N3izrzlZTDviYJENEnV5kJEXpKLUQimZPGUvsEjJBQu6A3F1PlldvJQxaQ+IH0YZx41SA51TqNE78qknm2N44Fb9ktxTcmDhZKjDrnzBi7qChX7Qe3EjsvsNt6Y3WrTXuc1hkCq6WJMimViwkC3FBpAtXaJnZrdMOiLdK4FMh8vNSbECT/fPm2CJ1aOx2BfNRnAu/cFFN6ika54zniMqX19vVjLTEWempBsFW4o1JnDpaMU3Gy7nKccZMqJbl7rN255gNzJJuIsx5ImhkS7NQjvyWUWw3OFS7sb5dX1DNALZJLlrBfklJueok0n8DXTjWJwZXYUz6zm7G2Cwq492Css+PT/d38Q+vSIwgTLPT9O5/vvp/L96wBuOcfn2LgWjEOT56X/vHPJxJvjxvu5+VO/b3utd++u/ZuA/np9qNwbGPI6Dm7QL348d/9sJ65d/duI7zRweL4+n14m39uNVRmuH98PoOPe6pq2Ht6ZIu/tRNIC2a6Y/Gmne3l8GPN0Xk5XTm4XvjJ+u3fv5/FtbvHlxUxaN/zT9Zcf0osz3Yrv9uAzfT+6fn7wBOCp2mzeMJN78upxW+v7iaDqQnd4cPf32/wCch5GECycAAA== -->
