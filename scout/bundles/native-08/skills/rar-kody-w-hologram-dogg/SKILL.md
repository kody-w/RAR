---
name: "rar-kody-w-hologram-dogg"
description: "Lists the public RAR hologram DOGG channel and asks a local RAPP Zoo to summon a named, hash-verified character or data projection. Downloads data only; the zoo owns the sandboxed renderer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hologram_dogg", "rar_sha256": "d775ce5751134da02ee2d825ef0a74d79192691d3f5f8a3621c13c8bddfd8bf2", "source_kind": "rar-agent", "source_commit": "0313216c95b75e5aa168f655108622ba549a6481", "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["hologram", "dogg", "rar", "rapp-zoo", "three-js", "summon"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/hologram_dogg`. The original RAPP
agent is preserved byte-for-byte in `hologram_dogg_agent.py` and in the RCI capsule.

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

List and summon data-only hologram DOGGs through a local RAPP Zoo.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "List, dimension-match, catch one DOGG, or inspect local bottles.",
      "enum": [
        "list",
        "match",
        "summon",
        "status"
      ],
      "type": "string"
    },
    "frame_json": {
      "description": "Optional RAPP frame whose payload supplies match dimensions.",
      "type": "string"
    },
    "hologram_id": {
      "description": "RAR DOGG id, for example holo-avatar.",
      "type": "string"
    },
    "query": {
      "description": "Natural-language dimensions to match against cached bottles.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hologram_dogg_agent.py` and embedded as the fenced Python below (sha256 d775ce5751134da0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hologram_dogg_agent.py` first:

```bash
python3 hologram_dogg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hologram_dogg_agent.py   # or on stdin
python3 hologram_dogg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""List and summon data-only hologram DOGGs through a local RAPP Zoo."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None:
                        self.name = name
                    if metadata is not None:
                        self.metadata = metadata

                def perform(self, **kwargs):
                    del kwargs
                    return "Not implemented."

                def to_tool(self):
                    return {
                        "type": "function",
                        "function": {
                            "name": self.name,
                            "description": self.metadata.get("description", ""),
                            "parameters": self.metadata.get("parameters", {}),
                        },
                    }


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/hologram_dogg",
    "version": "1.1.0",
    "display_name": "HologramDOGG",
    "description": (
        "Lists the public RAR hologram DOGG channel and asks a local RAPP Zoo "
        "to summon a named, hash-verified character or data projection. "
        "Downloads data only; the zoo owns the sandboxed renderer."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["hologram", "dogg", "rar", "rapp-zoo", "three-js", "summon"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


RAR_CATALOG = os.environ.get(
    "RAR_HOLOGRAM_INDEX_URL",
    "https://raw.githubusercontent.com/kody-w/RAR/main/doggs/holograms/index.json",
)
ZOO_BASE = os.environ.get("RAPP_ZOO_URL", "http://127.0.0.1:7070")
MAX_BYTES = 256 * 1024


def _json_request(url: str, *, payload: dict | None = None) -> dict:
    body = None
    headers = {
        "Accept": "application/json",
        "User-Agent": "hologram-dogg-agent/1.0",
    }
    method = "GET"
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
        method = "POST"
    request = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method=method,
    )
    with urllib.request.urlopen(request, timeout=12) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("response exceeds the hologram DOGG byte limit")
    parsed = json.loads(raw.decode("utf-8"))
    if not isinstance(parsed, dict):
        raise ValueError("response is not a JSON object")
    return parsed


class HologramDOGGAgent(BasicAgent):
    def __init__(self):
        self.name = "HologramDOGG"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["list", "match", "summon", "status"],
                        "description": "List, dimension-match, catch one DOGG, or inspect local bottles.",
                    },
                    "hologram_id": {
                        "type": "string",
                        "description": "RAR DOGG id, for example holo-avatar.",
                    },
                    "query": {
                        "type": "string",
                        "description": "Natural-language dimensions to match against cached bottles.",
                    },
                    "frame_json": {
                        "type": "string",
                        "description": "Optional RAPP frame whose payload supplies match dimensions.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action") or "list"
        hologram_id = kwargs.get("hologram_id") or ""
        try:
            if action in {"list", "match"}:
                catalog = _json_request(RAR_CATALOG)
                entries = catalog.get("entries") or []
                if action == "match":
                    if not entries:
                        raise ValueError("RAR hologram bottle index is empty")
                    tokens = set(re.findall(
                        r"[a-z0-9]+",
                        (kwargs.get("query") or "").lower(),
                    ))
                    frame_json = kwargs.get("frame_json") or ""
                    if frame_json:
                        frame = json.loads(frame_json)
                        tokens.update(re.findall(
                            r"[a-z0-9]+",
                            json.dumps(frame.get("payload") or {}).lower(),
                        ))
                    ranked = []
                    for entry in entries:
                        dimensions = set(entry.get("dimensions") or [])
                        matches = sorted(dimensions & tokens)
                        ranked.append((
                            len(matches),
                            entry.get("id") or "",
                            matches,
                            entry,
                        ))
                    ranked.sort(key=lambda item: (-item[0], item[1]))
                    score, _, matches, entry = ranked[0]
                    return json.dumps({
                        "status": "ok",
                        "mode": "dimensional" if score else "nearest-static",
                        "score": score,
                        "matched_dimensions": matches,
                        "bottle": entry,
                    })
                return json.dumps({
                    "status": "ok",
                    "source": RAR_CATALOG,
                    "count": len(entries),
                    "holograms": [
                        {
                            "id": entry.get("id"),
                            "name": entry.get("name"),
                            "kind": entry.get("kind"),
                            "rappid": entry.get("rappid"),
                            "bottle": entry.get("bottle"),
                            "dimensions": entry.get("dimensions") or [],
                        }
                        for entry in entries
                    ],
                })
            if action == "status":
                local = _json_request(f"{ZOO_BASE}/api/holograms")
                return json.dumps({
                    "status": "ok",
                    "zoo": ZOO_BASE,
                    "holograms": local.get("holograms") or [],
                })
            if action == "summon":
                if not hologram_id:
                    return json.dumps({
                        "status": "error",
                        "message": "hologram_id is required for summon.",
                    })
                result = _json_request(
                    f"{ZOO_BASE}/api/holograms/summon",
                    payload={"id": hologram_id},
                )
                return json.dumps({
                    "status": "ok",
                    "message": f"Caught hologram DOGG bottle {hologram_id}.",
                    "result": result,
                })
            return json.dumps({
                "status": "error",
                "message": "action must be list, match, summon, or status.",
            })
        except (OSError, ValueError, urllib.error.URLError) as exc:
            return json.dumps({
                "status": "error",
                "action": action,
                "message": str(exc),
                "hint": (
                    "Start RAPP Zoo for local status/summon, or verify that the "
                    "public RAR hologram DOGG catalog is reachable."
                ),
            })


if __name__ == "__main__":
    print(HologramDOGGAgent().perform(action="list"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71ad5OjSpL/KoQ2Yrdn1d1IIAT0xos45B1GXmL6xUwBhRNOGGH65rtfgdTmtZ272Fv9MS1BpfulqcyMeaiBJDb9sHZXm/pajm0tR9NhAsPadU2DkRpaQWz5Hno9s6I4wmITYkGiOJaKLbgFZvqOb4TAxXricIipJvA86GDA0zAQHSIMYI6vAgcdlSRM9n0s9rEocV3fQ6884ELtGjNBZN6cYGjpFtRKFiFQYxhifohpIAZYEPo2VEslbrGen3qOD7To/Mr3nPxflUoF4o3enfWLkHzFzxC3EHoaDGF4i6yBGXADB0a1u+9/Xtcs9L1291BTHRChR7XRxZDSDs6AXowoHOAZ6FWQI4A89DuAoe6HLnqkQR27/LqKoKNfY//85yEFoRF9u7v3sMsHVFpjf2DnV7cGjK/ua+en97VvpYX3NQfBel97JnpE9IelvaZ88eqJ/CVpHOYvpJcfS39UwvKwh0dh14jOBbFq3td+vSIoPyqCFglC0n/Yke/9COExgVF8hfz9o8utuJk4/PaWCkEWWjBCVBf6i9KX5xeFv//5lvJZyT/+eNbsHcUuhz0/fpT2waHyEwIrgtgGOAnsh6EfIlX+ErCKH8cORLhoMMOsCINuEOdIy/c5xv4BeqVxETIqhLc6ogOOc/WJ/Pvad3BTNG7YP+sI8o8PXv3FxwjqMH/h3W+3jp/C8OrbBxy+faCwjmyElf9eR9Hzm3eD6BXYz6c/wbo6hOSUx26r/Lx6pvv2Md0Z1dskQNkMfw/W/xW05afSSUvc4KLTBYUA5KWiFwgefn2F82dYh8A7wDJb34vuCh8koozYvEzDr0NXs1wEC0qIx4CraC+KP798SqlPEK6SqcrKyA9jqF294P33C/7fPkui0rJbEASokF594RYHelcXed++cMpLg/5SzL6gu7D/He7/Zz/elkhdHWD+hwNcRQOYFUP3Dru6Kf9+b/x5XT343vzzIzaR6ofwGvtx/aTuxfl/XCQgJh8oAOMk9F6G7MPHVtzXohjECQqDO/TdP3wKHiqrvgbPR59CADj3tTLHK4Ux6KB6eV/zIAhRtb8pmVvqF0wrypLr2eZP5VdYaD9exu/dbzj0vnau1OXpzxz76x1v/Daev40lOugnoVpp8+I+/PC06ideXB4uk+OS+d8+PP14OVV6fP8Yk4fP4/+cU3dvs+z6K7qyJXtNeX72Ne0B1e7XtOdnX9OGqMK81fnx6df0r0LkQv/49Gv6vwblF+X2E26/Prkj37kD3j/9noDX0f2qZ3qK3reU5wb8dS+n39ceZFH80eGW/V84CCz8Rez9hzIJ9ezlqUc1fi8rKnNe9cOfuuYr5Kpp5F3kLq3mi6777t9etmHZmn5VuWEUAeNSvF+OB6hrLf1phaj5KMPrbMvth+zeL5FR4sRv4uODPubjqMEfgfxA9qXf+uPhsTi9MOTXOzT/oRh8gS0yrgsSw4xfDbWXQeHhpcK3n7A8I1pyPH/7jZj8Lct+N3BeBcwl2N0kijEFYuUEeGlMri8Bc13mzpn3W7teqgozFQYxdiUuq4nq+sV0dY0loeNYym2l1+16Masef8NAVJLd/b/a+zhR310y+ytQoji8Qkp9e/ecaZ0v7KuP/LuMQRg/bzTKxDvX2LO6+AtQq61GjsUmiKvFxEdzFhpHPlypXIbxKteBagLFgbfv8fn2xnG1X9c1y0PGJhUq5Zbjb3/DeEsN/cjXY2yJmpMYC1GDgu64e+/eW5lIinXeoYQQKR9ZSNrl3PMaBvN17Od/HXwtv0mfCsAPzTeMn7fYCtH6oWVY3mXtc++Bcp1S8g1QQsDwhKqVksfwBiF3U34pL8Sff+HzoyK5DfKf1SoJvS9VWnTHCI4A5RRCAKm7NaF3UU4F6E7NoJogbmdn6JZTNt5Iou+cIKJH8qOD5ThougqRHT66iEveyPy7ktnPnz8VEJn33nnbQ2Ln1VeEowNP6mA3N8gG3bFQlbj3oGr62D8efv0D+2/sM6qKeSlDAtEjuEjDyVIUMDSXJ6jBiBHuyFMQaBW4D78uSCI2HrzEUblcKYkdq5whHmFdjrgbgmqj1NbLJt5yAzS9WB4KmPgWG+vYk75IaPmq3MmZPqoFGixnOuip5/i8956QLC+9CDX/kZ6jtI5gJfWnEoJKRfcHCsL4J8Z3JTQ/+k650kNqVocQse9ZCP4np5+fIybhPyKs88jiFhPK8EKXAmrxzBBcZOjg7BeUOY/kiDnAPJjee+XCDpZQgfMqsIQHHULIqBeX3pQ+x1TfdZFjo0fZ1RmARl9s5QMkPLz3oksco0EHoaL6SJUcMxJLA54K/3UJqcj0E0er8EOalpyedpRnr1QxWC5Fqzi6bDXLteRNuZb8axqXngt9dLm82YiWm0mU+ajHhLU7L3Gc66rhfrWRLJePoNxeIP2jcm2JsjGAyNGw+nUue+W3tyvb6+d1ws2l7KvlH8z3YKVbVamQXwKEykW585UXVVtTL3Frd9+rzSH6WXFAf8/mll+qolf787oW50GpNqo3KPzK2vO8AnqrmVh9ecThvD9KUVzCx0YBARoEThnzlcgXO5FSqzeyXlzOb4WVVbUqppZ2fe7Dz6vgykc34IR8Fr7LtVrGveUnIJND4NyU++EERerLhQ0K2LPCwKiCHYFdjr0vIX0lBsl57OLOq+nLe18p622pRuCA+Lx4fkDXWAzKILsEwaUko+MhCG+iMnLx5m0DSUG/zxUIvXu3WF/ORCZA9aPcadM0pUKKpppNsqWBBgEhoTEEBfUGoFsazTZZos02NVKndAaQbaKpNkmVUTRN1xhFJ8pgqGbjH2UKWqXcBtkkiWZbZSmFpiAFQLPN6G2KajaYNkEogGqxoN1ims+k5cB4MeasfAnP071RxfrZpoea0m6VWdKKxtz508XpjazscUUwZ3XaYTtMXzADBTBDfAnEjFW1CR81wngWMQN0Jerh3hrN+26jmLYOx+V2Z1MngJNpNsnlcZyv6YXY70bByj7xDMODdRiAdl/Y75yuNnEcdI1OeCI9MuRiJtjTDWDWOXOaHZvLWCj6ykQNG6Y9neey5VInz6adU3qU10Yw2je3S3ePbiLgTBdbaWxN87kVHLz+qWdPutTIJxnCUGOmHsjtJJgw8BhshoejYw12y+ORFdQNPqUPhE8NFgTujlNen8rbBA6zRuIu5EyW6j7Vw0fBPFaH+kDilwyfKAvdn3TtMPM2xRihPpOTlaGrwG/nrZljLbbDVvfAosZmlgxaS10cboDA2EDBhyums+svxFV3IQz2DDlvjlferC5OhUJy+7KQpvZMYfnCOmQ+u9/OfUsYD7h+XMinRR+fdocNIoPbo8/aE92YJQKymwrazaGTpNpmeowypV5fTfC5sAJs096pk1XLlhsnZ68e7IPHjonGfB1QHYd2l2uLXiwiebh0VlM6GPmi3ko0bQ/C/SAghe6GWMM9YwfBiD2dtmo9FUZJNrS50A64Q30UdzWY9f2dR84DLhFllxT8dCzPh4vM2PZG3f4cp0PFawtsJuX13ZAjtxJ5ZPQF6CwGQ/U06J64DjPUzd160jyJfXlOaVZ3TcW5SoppIZ0I3m+yvEa729zr0fyUBZN+GOubwK8b7o4fSnNGycbefKEeibW6O0wadd4aeCewcordND4dFprpyKK1m+6tzmHJKj6fWCuVQ347WDzLk/Wox3Q3jYzBx91IlBHsh7kt80obGKeBMfEsjsy2s5QPRtOWnQaOVHDKvD1YrVsnai3CZSD7cZrQqVZHd2y9txjZXiwAo7mZ1LkITKnU2RnDtmimjC6Dnbwcb+r1hd5yTtko4N2p08w2nj2IbN1Jl3li8zJUiWIAcq/ZafS5SDrwo5ZXtLmd2BcPp8DbqhuekXZrt7lwx5zV2baJ9maJLtBYnkYpgmuimNupLC93RitUgDFpDqZIc89j+x6kj+3Oxt91WjPaW7H91RYIOqdoaq9h1M3BLKfhTsnr0NjJE3I99sbzbkFMhyIBWhRQQ2LUYZmd1LAL9TQj6xPSqeOhs9oPB5Jf3+Yu0RdbA1dezQ4nYbMsOp6Q931pxAe5lbrbDU/1pIYDWsUmYvpA8oNMak2lsbQIm9quoYszl4l72tJ2V63VKdyl3rCx1CWysfWiIc7gbhERmid0bFaXBjNWynE6p04Gr69OZCZ5Qa+I2rpuKFsiBt1DLukHXln4xyFhc6O1Fww7ymrKUcv1IsolJso4fkYQ3pjlIE13O7kFPJOMLVygss4scdvGtBnO3FlkdIyW2muvLYNMik4MaNKX6CAEG9+gp7TGN9bRSNNZH091nlANlLuDnVNnVeYwwZkoIOMcnmaMLx6KccgK5qnH9HrRumi5E9kV9EYoThmLWSpaw1TRTCuQXWlCTiWF8yaBH7ChcsySk0uqzdlM8Xy9B7J21zVPKp2xhmuTgcQ6G1AX8QkaNgZ1cjYrAm6U8yYb6ZxX2LKN47A/nAyyrRwO6hrPMVzYaM7X670q0AchMXRlLdoDIyeT3T6uz5njeDofOzjRn3D6ckaY+VrzVydaaAQTvRWkrcDcSGKxyrL+YI2q0G7LCJOpPTH1UdegtxbcCMOGNVbztLUkOccLTeFgxLzV3O88PmtRzD7gKbF/IL3mkMclCQFNLJbpQg9bkd5bZNK0x5Hkaq1YERkxWxoy+Vgyw3w4jYhJKBDqwiPtzS5Zir0xRfd0TjaSuqLUGaKtRbG6ZtMI0LoSbqejfouN5z1npCctxeR86HWcoaH6I1VaBXNt1M6Oy32HGjuM1Nv6zKyQFGkw8etzixyupCyIR0OGc8Ul2EGBRHJ2cj0Vl73jYjk6tB1HtPqZbo7627RodEYRKw/TTnHqFmlzDA7kWGNdW+WJ0QZ2jhOKx/OcojqihO/n5ma+6fUG8/xQjGZxPFzj8qJhzlmwAVzRk4+wE7alaDg+ynvx0JRPVttMYWZx0LCtfWPk9RsyZ4B+Z64sqDHT1lubiYKf4g09c3Kb2hza680iaxF9uxu2fdDOBvQgVrRQrkc7Qphmm34TLrfSsR3b9YQTo/4xIEfjeVyMpH2TA8W+N2/XNyu/bZJGQTezOTUeGfPOLJ/sktDDE8sdSsfBwbWDGbFLWW6FD5cdOZ2y9Z7J6BzfVXaC0SPGCs9CWzsUYrfb3Rz7qeInU7LrHR2KWMYktG1faFPyZhBsZvhkPmgI6GrB8wVOdExlklG7YTQXI80I4Ebh9A7ViGwpH4VjaSVMDCuZmd2juXd9mpY1QRFOJKtIRzIhmNHRnan2dNnrmXiP40Gvw+S0kkyNLdPUCEg5qGOBLCUcClqkPZ0QNbgDQ1cg5H7/5O4Ea9uR5zM9PcwoOlnqaUN2l+HK221j0rboMSjwsGN3qDzcjqhTQEORmm1gOm91RcUbtOwj8Dgy0hzHWerNJrImOQZyPWCDbqRt3WA1ZoYrda/XBW1k5Ouu4K/TsM+tAtJurXuGKebOSHFwIFv5vL0x+xHe6swonB+2zMTVmIKGM2e4m5mdgQl7e6+VO3WSorUVLLq07mi9TNWW6XY8ajSPmx2RDpotjulYKMWiA9XgcHbDy0UgkXO20TBwvksfj71iM502t0lz0ksH5JSnZJKb8wPpMIVjUwn204CgwlarswbkYSnok0K3s7yJOhGlQ4zJumg2G2yT7Dqi3zxup4e9NjwSoUxE0ZJMrIwsSHmRqu5mFG/WxIlrUaoTh5R2ZA8TS9fCAoxp3s8i78QRBZB3K2do2tq83gjb8VY80BpHr0OWsGfLjTyWDHHUoQkW74pRt62S/Iilm6oyZ5LNagzXM6/XkFqHGEz1I5EUWXYIM5Ei7B2NRqzOrLDdwJzU5y0BcGzMUf3xxJzQjt0eFWue9Zsm0stL3SNrw/p8UzjbSJocPVc3c5FsTOdtIbZ5VQ/J0WHZHh/1WbOT9U9kIrb7xGS72zB0e1UYDG1FDXFtnloaqtMnb5DSUpv2u02QCISCK1EqkFRd2Z4U6lCEJ24lkWpvJa/skWNOM1/2BdQcoTsTXy8VfJfOohXq7iyfmERSRq70w1hu45a+ZbStIMkTfhjB1RImu7bUY9ltQitD1OJui/pmnUcoftW0za1aEw7vHNZtYxIn5pCQybkjKGm2kk+q0nfAfN4Qvda0MOfSyW7IYN9bScQi3NFef0brzCifNGUlWhYwGu6maYN30/WQW1hih6XC/QIfeRLHBacuv4aLBeV2/TXRM+qnLiekybFBN/OWymvHYVfCe63lfElKSTlUoLGkXClc5vH3N1Tl6PJvm6DOw45/QiI9FZZjdwiBdlfJuvtAPhoYQ9VC0s9jX+QkxmWAOg99N490N5ehL8rPWxzfi2EWPy4dYmCU/zPqycryv389DYnVv0FwU/h+Ob+aIYQ3dvS8BkA6VNvCahBt3paa/Pofl0eh01kmAAA= -->
