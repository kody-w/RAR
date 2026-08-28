---
name: "rar-cowork-cookbook-scheduled-brief-monitor-service-assets"
description: "Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_service_assets", "rar_sha256": "bb3815b5db90efa669934689260c5ae71ed08777cdcc7d70637135e241008113", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Scheduled Email Brief — Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 bb3815b5db90efa6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_service_assets_agent.py` first:

```bash
python3 scheduled_brief_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_service_assets_agent.py   # or on stdin
python3 scheduled_brief_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Scheduled Email Brief — Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_service_assets',
    "version": '2.0.0',
    "display_name": 'Monitor service assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b39251510a4eaee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMonitorServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorServiceAssets'
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
    print(ScheduledBriefMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxrbnV+HV+6PbT90lEJvUNxwxaEESAiRWIdyONkuyiH0Ti8fffRJJVW1f+753PTERo+6KEnDy7Od3Tib164vV1EFWvnx5UYCVIlsrjsMAlIiVusgqa7Mygr+yyIY/iJOldRnaTZ2V1cunFxdUThnmdZil43InAG4TW3YMkCQr0zD1P9tlCDwEJFYYI1WTJFYZDvA+fJ6GkAlSgfIWOgCxqgrUFeLBW3UAkBJUeZZW4cgqa1NQ/gOBskI/BS5SZ0jZpIgLWfYIpG8BiOL+FaoDOivJY1C9fPnp508vIfz+8uXXFyeGzL+rB9zlqJPwUEB5yGfu4iGL2Ep9SJv30CUpvM5BCXVK4C0X2vG8+liB2PuE/Nd/Ra1V+tUPX76myPPz9WX8J0P9RjPqzKpqqLJj5ZYdxmHdvyJM3Fp9BS2smzKtEAupoEdT//Wx8junLEd+HJ99fAh59UH98etLBlWwRn9/fflhNP7rC/QF/P46csk//vAaZy0oP/7wnU/V2Ffg1CMzqPXrt+f1ky0k/E4aenepP0Kuj8ja4OvL74wbPw+9RzvhypfXaxamHx+M8zK7gdRKHfDxh3/FFobAieKwqv8tvj89GAfAcqFNT8V/+HR38s/I5GnQO89/LTaHYf07lkDyN3GfkKej/hXvu///iXUcpqB69/hfsvurBZMfkZ/+pW3/3YJPiPf1ZQ3i8AazA9bMF+TXb8pps/rpg/v95oeff4Os/0c2StaUzp3Dt8RKQw9U9bdvP32o7rc//PzThyaHuQas5FtTxn/F86/8epfzBw8+qT7+cS2Ur6VRCkseec905Ncs/4/yt1dEt+LQ/X6/+oL8vl7GzwQZjXgT+nDB72qmgrr+zo8/vPwGUSKF1jTO/TGs8v/8T0QInTKrMq9GFCdr6hFs6jABo/JqEFYI/P+AKOjXB0I96GD+jxEeNc485Jf/5dyx87PzxM5p9YY/3+6g+O0Jgd+eEPjtAYG/vCIq5J6VoR+mVozIzOn0NbV8kNaj5BwiI6SHmGL3NfgM0ejz+AUJU+SXf0/Atzuv17z/5Y7w4QOp5NV+RKkKLn8dLT0HIH3a5cCmADrgNFBMnDlQJy+EIPtpBOksvkGUG71SRWEcI25YQhdkZX/nDT33ZWT2yy+/2FYVfE0fsIojj65RTSHBuzrI58/QOC8O/aD+mgInyJAPv/72AfnfyH+36s58lHGC1j3jAjXklKOIwDprEkgGQwaDDEHkHpdff3u6GLKBjQWBUQy9EDwWwzyNgPvmb2XHfJ6RFGID6Gfo4yTPynrsXmH9iuw95F1fKHR8NKJ5kFU17FU5SF2QOj3kakFz3j2ZZjVSwWSsvP4T0lTgLvUXu7TuKiaw4K36F0RYnWDvyOK3XjcSwcUwntD979nwuA+ZlB8qZPnG4hURx8xEcqu08qC0njI86xEX2DPelkPmFpKC9ms6tkowuupeJg/3QCLoGecZ0s9jzGH7hx08das32Xcaa+xw6r3TlV/T6lkCVjmGwoEtAQr1m9AdG8M/nilVBVkTu3f/gUfDf0bBfUblnoPCX88I730c2dzHins7R742MxQjkP+/M8ioNbPdypsto27WyEZU5cvDm+PgNHr9MWvBQeApBlbO9+HgDVreEPZrGocwNcr+Hw/KewyeNA/UakqojMzId/4wAaA3R773/BzzrSzHzLa+pm9Q/gmG/I5bMESwmKOHLW8Cx6dvmgawYsfr7239Hs/SHUsb5iCSN3YM88MDwLUtJ4JalWONPQMBkxWM9dYGoRP8wSoEcoc5AfkjUIkQehx69+46MYNmwsB4ZZZ8Jw/HYQlq4TYO1BZOpuAVOcMyGSNQwdqEE89IA73w4c4KSQD0MVTx3cNVYOUPZcZh9qmgNcYiS2D2/j4Cz4ffE/uuy6g+5Gq5Vg192Y5w64LuEdl3PZ+xgsomYyneF/0x3E9bkd/3nH98Te86viM8rPBH+n53DgIrK6nukDoCVAVBJgHvefrozK+P5vro3u+6fPnTBP/x7w3593ap/TFyX5CgrvPqy3T6aHFvHe4VwsMU5kiYg+p7t3uU3+dnsX1+FtvnR7H9gfvDWV+Qv6fhH1g8U/sLgr2ir+j4iIfCxtx9fqBDVp+Xl8/E+PRrKoPvkX6mwwixsKjt/r3fvJHApuOXwB+JH/2nGttWCzvlHXBhLL6m79nwrBWI56k/Nssq+10N3xsvjO0jdO99AT5KayjbHUc2H4xbmnhUvwIvX9Imjj+9pFYC/t2tzNgAYNJCj4y7IFhAcAyqQ3C/eh+Jxos/7uLupQUxwc2+jBX2CRnH10/I+yT6CXnbG9y3XGkDN0c/jVPwKBKSwl/vtO9bRBu8wB1Z3eej9o8Nzzh8PYfiPysxFhbU2AFjU8/eK3WU+Ccm8Ivvg/LPTI73L1b8hIuqtsYWHdZvRf6Wop8QGD9YfLCeIEw2cMGfxUA5JSga2Avd0dzv/vtuVvaw5be7G+rHrvHXlzfYeMbgOSFCclifn6uxG05hrkKB8PqRVfDZ/+Xs+OQC4Q5OLZCNbeNzjLRJ116gwLMoarHACWq+mFGoQ1qAxoCLzmmadlzHoV0apXAaw0kwIzAUnWMYDvk9MvTb2PjDUbOZZTlzh8YId0FblANw1MYdgM0wl8YBSi5wbz4HBHTS+9IIYuXT3Id5oy/fx9jRLU+rf32xKQJS7ohqzzw+q+lCt+gzbcuBvSgpcDGN6d4OtUJxK1avo4oq86MYrdRlas7C+V6frTZkVFjJkel314NgLW+Z5Dn7SW+StDn1AyW1FD6w+GVEhM7MbnA+8kiSoPUls8k6J8FILQ90Iz6TaLa3MD2WNaPXi9i1TMWxLfkYiF6MZXUHJtNpbQn9OlAvyelgHGE+OP01TDwLlEc59wh2GNiJdvKVK1Vgm+LcB05Sc/EuOcZefCE3RYE5ZF3MhMOxdvLlimTNYFq6sl772C4jxXSY06c0n81Pt3qb8tjc88j1gSXX+pbvleasR7szJhbnpk4J1da0cNWl5ZWjA3FR4HzS6YcyMk01a0w7XtCrSyN6aqsNq0AtCipY2Sk3cSoDjrT9lsPYS5mykmIceUd3SkVudKI4o7MNu4UBsA1OPlvKAQdH81pZtic7Ct0kOHFTbuyZHJbHXk74gy748x1gyd3ZoTZaE6Oxn+gLhtvE3Ezakn2yrfKydqgzmDgyuuwbxTAZP8/Oy/wcODHY5u2JjsOzWYtiF8V84OHqMdsCCzsX2q6fxoFh4pf8YgLLIps1cekukegXM1UD9QVgFhsRqoZRnZXzlT1YvZbOSnQeHFojINJrFivbZh9RSUUefUuvFurCIcmqNk7H1j3sC7InSdNdTDP1UuoDO++aHbG4iHQUHugTLnSgTDV9kzuFyGni9TodDmFpmMX6kpVWyssCW0jx0HaYJTeqj3mirF4oMpwu9R2LlgkRJDOUZzyl6477CzCOmWkqaSUk3tRauNDlh6aoTieTP27ZUJ8bXHIZJFTNpDoxbZOXObfU8oXx+NF1r+FPqrHrHS9FuVM2pESyI/a7nonOk25DnPNpK17TDTWdJjtqKZk7kiqHkpgz6sX2IJ6VNssXWXkYzCiLdKpWynPQd1uqv9gsK26FS0LuT3KCChOu22NXzjuozdLBi1yBQBQPxal1RdIO80AwZWO2LvUND1Zce2LwVXhIQkXc39gNvh+yDcOabnhcN1JwOMuyqidgu2kdVSRp/urw2WR1S9Nzek0rIt7YVTQPKe62qUKSPHTs5Cgq5h5EamKTVDKTFQvX7JPYEcvugAokg9/IKbYg7Fzu545Heay0EZuqbGzu4qnRVhCVfXDGIlW31a3jqMKFLFd9PxN9juK80Eub3TUvrhk6Z7CpENC5ysnF9XBY4UXhtPtVfC42l9uJXgW7wkUT3NnXR/ukkgY9EXQ2EViMIpcn0cjrQZkbeXluDA/juJanCvQSCH6sOhjPYzWXq4VqYQGuXWN7kmjhwtIDaS+RflKsrujpVhyyVDAUqlJipVmlXsjBhNau7HpKFsEh3saxMr2oqMQXmiyltRs2QKWuu3RL7nfhomKwdF/maHHeXcirPEs0zMeaC5cBceCu28bNJaW0rMTQga+GqSD3ZbVx5juJvDbg1pOlCNItfur2+ZyUjmg0w/OpwQmZH/i0UAqNwNXUurxh7NVAw2ShleebG0S7WupONT69Bs6JDrg1tgGLYMVys/MGE22zcHYZMxEiqZ9ie2sSHQSsFei4w4V2WxdZJ3PUMA9nsmQpTpoVN69bXwJRoAUl3Q3ELS3RU6JG+IIMsqloJLNUOfUtzwiav6zyuvUNg1jmV2XjC8a+zzardZQsw3NQt/V25tp9TV8oUxSlFXu46K6Fdlp2LJMzx0dHV+C7zjpvDk0j0KoqJpJWEuQBawm6jNulwmLDgRp8/qjL9MmkYM6YODvWr+t6dj1fHIe4c1Nuudd67NpTN+ukKJoZG13qlCczwhm/Pl6lamZOJrzAxiI+2/EVzy6lwJgr3nSCy3E7mXqngPGKbaRdSWl6OPidvgATiw4jZnlsL5SGiuukcPpqX161ntKPlN+24mK6w6I+nK8vSxbdlo3hc7usgUU1k7X+pNxWoJFWXJHUdjhfSsRppTluEpza5UTvwuWyYBn0qB9NSzp14YLcHMIAH/Yn3smWZYLrEbqI3MIO/Cu238saqm+Pk2tnh7Z+RvkhL5oTr+WGEBTD5YaLXi5d9gy6WpzMA4nFLt/bjsTdEmd2CYns0g5Zl5I5yczRqWtr2VzWS9T2UNLBLkIWJ8VccDcg34chpzvq+RothlsiNlyzARsuwj3zOFGry0qrLpWWz/Roo6ww0k1igzVFaTdd0RJPaK2xqsrt7liwB99frQyiSJtS1cXNRjvW9DSP7TgullfGXxZFsnTaRejH63TpY/qgt9POQWdSFMaegu148aBtlmJcOlzBBPPNpDOOcq/mJywmgFOtfHmpUUw/WxTHXNsObEkJc6FkaIbddPPdxKOHpsH6sw83GwO7jAkFjlFhr6PeNqw4z1L25iUBgcQzKZlezi2/oG0JZnzMYyXJ1FMzBDd9hWLKUDJqhU/KQl8pE2eorKuyRIekMo0rdqXxjZKpgD0ot05UUSpTnOtCIWVZ0cGWyUOXW5zW2npWrgY5KpmIJIKmtTu2WMob8ZKh7XV2uBbDIU4ZybpRkeypVzukF5kSBYO0SvPpdLZc1Mr8oJbHjXNlh15nlGFJ6rPh2ATLVItrQ5ZM1yujDEynwOMto/Pb5iBjhQIh/uBVoaqsLpSrpjfFIoyQz/WFmxgSfTOpju2PqTaJ62bh1P4suRpznOl1cia2zSpbRoUkhn4OvGTWl7HJM1N5myn8RsDWG0/urGbQZsWuK/cbCHIZZqhdfLgJk66bpeGmvlywA2vITqpkBF7PqP1Bp9DLbesfiB3JcjHGkwZfn4n2SrDrivVX4gTzDvUSO/tJeqDyQvElrJcXrX8w7LBY7U7CoFFORTASWa0S6bpTd34q70VjodDkSuVLkFMKcGO9ZqZxp0z8Ot1y5PEQk3yPSxeXq60DPR6J7klpHjk7liaIYNOrWz7UAoHkWthPsR3n4Esx6I9laq4vKRNzaCtfD7O934un5Lpez1d1N5cy4FZhujhqsG2sJzN3ZwaXiKPiSF3EVe/IZ6UscaunF0eT4BeSeq5XdCbO1mkX49ds5i8SYgY2jRBbzb4KFDtuF5VhzCs0K44BdS1N8Ujrc3VP9+qp08UJQdqamZJ9rzAuFskmrAWKudnyYW3IE8aXzAFAgDixG3SmBfKgK2gXXRrorA29ZEryxh+bCwpKYC+wrDtCZ+BzBw8pKkmbujgmsUIM/aE0covIDibstj7erlyG7qW1Sex7dMe27MQihdZLVTTKtDWJSVy+CQfsWDjzquanzNnST1dNVLZEqHor0nBqfrsy4VAraEkzEbkDOayJYN/mEaWCTJjdTjtxAfuQtueuOOWmCVdPTIUDLJwNqMv+YB+ImZSdFX8e6EOPTda1lFycCsMFIxTMibxOUdrzRcAQqyk+LwMOL1PbQjl2dbY2wcLpC5TrWs/paY3z6IVE13x7PmvS2fUTkPuu2rLz1kxMtsatAx/NXQGsjrFBxOagRK2m2anaNoNpHLbYMgwmW+YqiVdZpo8SN9eJ4VxKa3YtVqRwKzl0dsPnm6vupO6GAczaOk/ONsu1burhRyYPlA3Lb66nGFWcvUwF+1Lyj1ehmksBFWFu1GZmuszTmOXc23m4yXY46ZdTF1eDw3HPCXPlWlYq1QTRRlJOXOxx3LmVXaC4kuWWmCTDmVDh6wtnNDrQJ7JMTY250VEHsvBsUe3JpmxYe27uXMLhjPNtQtH4EnPWrNcYB0Zkb/Y2aKoLJxsK2pCOS6tXfTPkZr1tM+LETf2e2LGx2rgNSFqq6Sias0onmQ7Hy/5qKgLlXtJg3XX2vA43iw0z2ThtWNzEEYYjvHYXCkPY/no6YBgdotsJeaAmJZNSl+k5bAUbl6m2gltJZRpNSttoUS5ZxLbrSqJ18VLJoSOFCmncvaxRAEx6MplNpoTvbQ5z8UDh04U2HdB5ndO4Dce22Q3VIATiqFyUxJKyuOORuc4NQ+v9OcHbicNghtdyU01S1ssrfSZTPWCwdpZv1F3Cwz2SBCIcbmTWfuR15q4bbvxCPNTpcUJuuaUd05G9k1BA++vzuYq0dWqk87zE460QcZXhrFbJsD5RRycd1vwp7hkx4WfU5aac5vL65LrLCg27ZsryEJjjBT5jPQ4/pK65jYT4eMzUxemwK4/zmbNeRv5cn1srylo0CmftZqg9pJYxAdiknlJdh15jRnftYLoUgiW7aNZ5Pd916M5svGohBOyMNq41HJn2G3t1Ow6ibeBVw3vWEe7YUf7GdzI9BA3ZkCS+oryL2TDMbdBKk9itpluzYdutVA++fGwjUHi5rHRbt++mmKecNrulv65uak1tib1OxyQoOBMPpTUcL9R0F0kEa/LUUhw3cduVF2Az/rhJHdfs5sS6UyrTWx3A3jEWQN1Nqu1aJqYrYSd5BUNvkiZuboOXzMPViplzFaMQXJuaqQ8hZyfba227W0zaVNd5Jzh4u4EnjmqwJZLJbkZbs46+lZW2wrcqWFfpTZYHgTixWTDRaJjqJ4nTOD+8GTIdGERVLSoRq7eNmpAYRgxkt3ckElybCyHCae7YEZdDHzDDxJkx7ZnPTiodoxN8pgpnYoHVrSnxgV8dJ7lFpuayJG5At6NBNcC1ntVsUOzAVDZgxurHjAfr5fwwZ6y1n/I0kLaTWdMJVyb0vZaciEO2sPaOt8umTtSXVJ7WIr+OJgkuEXjIgI178yYr3/POtE2XlyXZUMNUa1LgOijvDdv9eurOvUksQe8C7MTY25JOIB5Za3FSaKeGyuxq6t3w0C594FDHgZp6/m3aruQh1BYd7nTJLe+7fNVVPt0G8oYhCaugM1q4TfXrRZTry/zC69gQ4y3rsRPu1GIiM99G+5OOzV3xtGizMCmNhG5Okghczg1nOJbfWOd6EnWC14hBC1V+BzeimTO7wZFu6buc5A9w1nMaBwQ7My6oBFvzeU3N5gswa0gOJaasFS0v28jGLxN6wBi4G/XWnWSwtWqE3k04CYy9ZliHVwPbZnYiJRRCtqOqWWRGy3RdZRHTzYsZgXFrtKAiWnNOQrXYbR3TE0+uk9oMTk+pJe9XdG74twh2/tlBVRZedwmmCXtz7eho4PZRS3cMvhTs6WGl41a41PD8FvArjcdsMs3rXd2Q7UmgTGc9tHCz7sDpsgPadptQq571835+bvUFqnDYLjIcy2tvV4o5NVZGrzmIznAGI+g1nNwksKHZ3aaAuw2G+fHHl08v46H082j5b75EHs/5/p8dNz5OBt9eN92PlYHlfrnL+vJ3Ffv500vphFCtx/FqFTf+8xjynw5XP/97rypGHv3jHe34hqyr387ka8sf/+LoJUzdpqrL/luVxc39kPfTi91U418+VN+eh9kvdwOTfDwZ/yeDxjtPU+rs2/PvNl7GP1AY3/4AN7Rq8Lz0n2fPn17cHoYtdKpvOEV+A2U+Wv18BzIe1o4vQV5++z9u42Nj4iUAAA== -->
