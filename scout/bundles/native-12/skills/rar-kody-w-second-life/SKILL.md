---
name: "rar-kody-w-second-life"
description: "Live in the RAPP Commons as a headless avatar through a real browser tab. The commons is a Second Life on the repo: your rappid is your avatar, the signed stream is chat, homes are land, worlds/games are venues. Use when the user wants the brainstem to JOIN / participate / post / look around the commons world itself. Actions: 'join' (open the commons in a headless tab, mint a rappid avatar, join, report presence + a screenshot at /tmp/commons_avatar.png); 'say' (text=<msg>: post a signed message into the commons by driving the page's post UI); 'read' (dump the room / signed stream); 'shot' (screenshot the world); 'watch' (seconds=<n>: hold a present avatar tab). It drives a Playwright headless browser, so it reaches the browser-only 3D/WebRTC surfaces. Posting writes to the live public commons stream."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/second_life_agent", "rar_sha256": "e67740d2ab1a489c29b4b274e2d20cb9df720603ba7963a10b0fde207f6c8aa1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "avatar", "virtual-world", "playwright", "second-life"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/second_life_agent`. The original RAPP
agent is preserved byte-for-byte in `second_life_agent.py` and in the RCI capsule.

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

SecondLife — send a headless avatar into the RAPP Commons (the Second Life on the repo) and act
through a real browser tab, all driven from /chat.

The commons is a persistent social world: your rappid is your avatar, the signed stream is chat,
homes are land, worlds/games are venues. This agent drives a headless browser tab (the console CLI
~/.brainstem/commons_tab.py, Playwright/chromium) so the brainstem can LIVE in the commons: join
as an avatar, speak in the stream, read the room, and screenshot what it sees - reaching the
browser-only surfaces (3D worlds, WebRTC presence) that a pure-Python client can't.

Drop-in (BasicAgent, no core changes). Requires Playwright in the brainstem venv (already installed).

Actions:
  join                      open + join the commons as an avatar; report presence + a screenshot
  say   text=<msg>          post a signed message in the commons (drives the page's post UI)
  read                      read the room (the signed stream)
  shot                      screenshot the world
  watch seconds=<n>         hold a present avatar tab for n seconds

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Default join.",
      "enum": [
        "join",
        "say",
        "read",
        "shot",
        "watch"
      ],
      "type": "string"
    },
    "seconds": {
      "description": "For watch: how long to stay present.",
      "type": "integer"
    },
    "text": {
      "description": "For say: the message to post in the commons.",
      "type": "string"
    },
    "url": {
      "description": "Optional commons URL (default the live commons).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `second_life_agent.py` and embedded as the fenced Python below (sha256 e67740d2ab1a489c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `second_life_agent.py` first:

```bash
python3 second_life_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 second_life_agent.py   # or on stdin
python3 second_life_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/second_life_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/second_life_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/second_life_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
SecondLife — send a headless avatar into the RAPP Commons (the Second Life on the repo) and act
through a real browser tab, all driven from /chat.

The commons is a persistent social world: your rappid is your avatar, the signed stream is chat,
homes are land, worlds/games are venues. This agent drives a headless browser tab (the console CLI
~/.brainstem/commons_tab.py, Playwright/chromium) so the brainstem can LIVE in the commons: join
as an avatar, speak in the stream, read the room, and screenshot what it sees - reaching the
browser-only surfaces (3D worlds, WebRTC presence) that a pure-Python client can't.

Drop-in (BasicAgent, no core changes). Requires Playwright in the brainstem venv (already installed).

Actions:
  join                      open + join the commons as an avatar; report presence + a screenshot
  say   text=<msg>          post a signed message in the commons (drives the page's post UI)
  read                      read the room (the signed stream)
  shot                      screenshot the world
  watch seconds=<n>         hold a present avatar tab for n seconds
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/second_life_agent",
    "version": "1.0.1",
    "display_name": "Second Life",
    "description": "Drives a headless Playwright browser tab into the live RAPP Commons to join as an avatar, post signed messages, read the stream, and screenshot.",
    "author": "kody-w",
    "tags": [
        "commons",
        "avatar",
        "virtual-world",
        "playwright",
        "second-life"
    ],
    "category": "creative",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

import os, subprocess, json

try:
    from agents.basic_agent import BasicAgent  # RAR layout
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None: self.name = name
                    if metadata is not None: self.metadata = metadata
                def perform(self, **k): return "Not implemented."

PY = os.path.expanduser("~/.brainstem/venv/bin/python")
CLI = os.path.expanduser("~/.brainstem/commons_tab.py")
LIVE = "https://kody-w.github.io/rapp-commons/"


class SecondLifeAgent(BasicAgent):
    def __init__(self):
        self.name = "SecondLife"
        self.metadata = {
            "name": self.name,
            "description": (
                "Live in the RAPP Commons as a headless avatar through a real browser tab. The commons is a "
                "Second Life on the repo: your rappid is your avatar, the signed stream is chat, homes are land, "
                "worlds/games are venues. Use when the user wants the brainstem to JOIN / participate / post / look "
                "around the commons world itself. Actions: 'join' (open the commons in a headless tab, mint a rappid "
                "avatar, join, report presence + a screenshot at /tmp/commons_avatar.png); 'say' (text=<msg>: post a "
                "signed message into the commons by driving the page's post UI); 'read' (dump the room / signed "
                "stream); 'shot' (screenshot the world); 'watch' (seconds=<n>: hold a present avatar tab). It drives "
                "a Playwright headless browser, so it reaches the browser-only 3D/WebRTC surfaces. Posting writes to "
                "the live public commons stream."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["join", "say", "read", "shot", "watch"], "description": "Default join."},
                    "text": {"type": "string", "description": "For say: the message to post in the commons."},
                    "url": {"type": "string", "description": "Optional commons URL (default the live commons)."},
                    "seconds": {"type": "integer", "description": "For watch: how long to stay present."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "join").strip().lower()
        url = (kwargs.get("url") or LIVE).strip()
        if not os.path.exists(CLI):
            return json.dumps({"status": "error", "error": "commons_tab.py CLI missing at ~/.brainstem/commons_tab.py"})
        args = [PY if os.path.exists(PY) else "python3", CLI, action]
        if action == "say":
            args.append(kwargs.get("text") or "gm, commons")
        if action == "watch":
            args.append(str(int(kwargs.get("seconds") or 20)))
        args.append(url)
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=120)
            out = (r.stdout or "").strip()
            err = (r.stderr or "").strip()
        except Exception as e:
            return json.dumps({"status": "error", "action": action, "error": str(e)})
        shot = {"join": "/tmp/commons_avatar.png", "say": "/tmp/commons_say.png", "shot": "/tmp/commons_shot.png"}.get(action)
        res = {"schema": "rapp-result/1.0", "agent": "SecondLife", "action": action, "status": "success" if r.returncode == 0 else "degraded",
               "report": out[:1500]}
        if shot and os.path.exists(shot):
            res["screenshot"] = shot
        if err and r.returncode != 0:
            res["stderr"] = err[:300]
        return json.dumps(res, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZaXfiSJb9Kxr3h7Qb22gBhFydc4ZF7AiQEALKdSq1hBa0ohXIzvnt80ICp52V2TNnZjh1yloi3nLfEvcpv96pWWqH8d3LnRsa56fi7vHOQIkeO1HqhAE8njk5IpyASG1EiJ3lkuiFvh8GCaHCf4SNVMNDCVzmaqrGsCoOM8uGNzFSPUKLwyJB8FjVnok1SNCvmx28WUJ6GBjEzDEREVYaYhSFL8Q5zGIiVqPIMfDK8rZS8FiuShwrQAaRpKDExyt0W00fCTv0EciNEeGpgfFIFGHsGUndUm+PcxRkKHkm5AQRhY0qlRk2sFCDNClvtVh1giRFPpGGxGQxFog6Ealx6uhOpKYI34VJCn+8MHRBapiBC+k710qthJMmyDOfiY6OcUxeiE+H0Ak+EfdhdNX7BkXwHkdA6pHwnSDFEFYI3DzHAh5LhOKUiGKUoEBHRA0WQrwQChI7hF1gWupH9av0P6vNz1FgPfxGfErUM5iQolP6+R9+Yv37S+WMekMUgEpUC8cbnH9vpHYmjNjJncAqH0ew6FNSbZbHWDJEwgDRRuZHVSDD0AeQPkSqtACMhHXvLMarS8zw60JNdRu/L1Mj+fyPAGy0QwBUvbqcvqWaqj08E+O0NAwHmFh66rmIHctOv+N5zcBHIgkhJjgrdRvdIl2+egoD70ww/bqCNHHdI5IsNlUdp8kS3MMeg8wU76kg8XBBRJnmOfobPJV/z1A86KT6EWi+e/n9j8c7B67vXr7e6Z6awKO7KuNxwncscAXWQ6Za8CI6QxUGcB+h2AxjHx4ZyCSud/c4lx6Jv//dLdTYSh5eXgPi+lPL/CI+E/fVu2cLpfevd9Xj17sHIoyJ1zucOnDzDHY60f3DsxcWKL5/+C4mi72/yIBnVwGz8YZ/2/x9k2MSAQQwTJ6hMuxndHKSNLnvzcbvDcS/GKVZHBCHJAyecYYk919f75JUTbPk9e4F7ENxHMavd4/fL/HTWw7j7hGdCRAMlZEkOCSQ5v9Zf36r1frHpa93396ZiV0C535f7rDFP1i73D0QyIN+8HqNAYPNAFWPV2j/+ODvDe7PsB6KCez86GkJH5QtCoyPYOKaewuH5T/eUgee/VJBWQz/UgWE5B5q9aOqa+1ctdHkw8MPYNx2Q4DfvUnj849hA9SSTIviEMoheY6z4B5vB9vVCAKK/gyzNMrSz+s4Q9CYcVe5Xjo+gnefKVD+USQ8xXkWQzIZ+LqE411mflwNufC2Gl//ejU66ShKCb78gwGE0wn9H7LwVj8v14B8yEyMOnp4n2JlI/tMfL1VGpb2izZcya9y58dV8PTdEpD5szXwuFr0rYx3Zd87W6BLVqYk0Ol8tRKBj5IneJN5aZ16Jq9O4h5Uvf/emH7t/3uokkzHOfF6h3M2fq6g1UMD4cwlbxVlICtWDWSAzI+hgB/YVJ5kWB5kwu8vVJMk//j2oRiqEw3O1x+KFj//a49Jfsc+386V17s/cPriq/cicRphiR9s/jew+efiyryrRMHF7y8M2Pge6h8zCrY9wulpALCf6Ye7b3AEQIOKs4oFQFf/29+IuaPHYRKaKSHpuAagrnDBvAavwdp2Sm5UUaEcxYmjeei6DurwgKr2EJrEl/+oCFu9Kvc/PYjdn2VEv1RUK4ST0AmAhGHW9hqUr7Ds8hiNcziVtXOKnuB8ecIXmId8+YssaKZfSrxuDLA3xtUPeYSescEKZlGVeboaQBkiPQNZXqiDYtPxMBygL/TgzEyxc4nreB5hODF4EsbnKhZZ8IKFffnyRVMT+zW4dmKi4qFJHRa8mUM8PYEHpoeP+dcA6XZIfPr67RPxT+Jf7SqFYx1LNbnBCxZOpIWAW2LmI8z/ysNENUp4v3674ghiAmCIEAzHdK7UwXMCF9L6Cqo06jzRzRahIQATgPRxXuNTykmBoJjEm71X8lYSZ0ydDIT7MNC4M0hVwZ03JPG5mqipk5jnR8xQS61f3s67PzHh/ULMe0tgJaGHqQmYWTE2NQgDB+B/C/l3mguUrXsT8UwIOMEwt1UjO1avOoD6lHGBVnvbDsJVIkDFa4DpDMJQqTgLK3hgESCjX0P6hGNenm0Q2OSmu1wD5Nkg1qEKyuPXILlmMqblsDEEU86ElTmGCqT2t2tKQfVmQP0wfniIsNEtCsY1KmUOfu9dxGtGk1SDAJpo/GQ4eWO1H+aYe/zkF6PIQ5mfAMlr8OvJBpgCTmnMQgPCjDHvxeF5rgr6h5knwjUNEACySag7IKnkvv/bmec1+B8PPWVvqWL6xph/pMnYnQoQgAOqFmEm9Br8C6r1+I51g9vgvZP5D5htfxymcHfANPKWElcpL+VUA6kK1gRv/iYRUt3byspj3EZU4220eCwD826KKAANTPATBI49VTz/Oq28Bh+Y/o3fE/dM/4rWI3Hl/rep6qGsRxwuoDlPy7KxELrnYPDAk09VcPtxGD2BlfddNXH0ktE/AiMG3wB2CE9goQRGFBEdMwefyu/mk6tv3/GBKOXEvephL89lI4KkQsZDqeg2ROKTB+NF/PRXTpa1asH72e09tr/9N/Mj1gAsBNPBtyHxu4ZfDYsf1N1fs+sncyKWXobxp78PAa6y8OP4WBqHg/3T389GSryjZNHEu4Hybccv50oC+jgR3PbgKc3RQTS6ewkyz3u8C6C4PkxzeHCDPuoj6G0JHvjgrIZKTx1U3lUcCl99/LbSR6YKjKwMWTk8BhlMfr+XJBJuIRDwfwwLvgHH4E/pzR2Mluk5wjZgJgwTJBCNm7V/0TII4woEPEkXcDbjsggBVIjz1Xes/CoQmiSyUIwl4hT4uTiw7KVE+ZYDIK8M8sdceCf2u50wdfxV6KK8gG54yyJZnEEmXfF5G7uvbx9+IvgbRqosNKOava/vQw2TJqw48tS0mq2/3kGkVAPCfY3VlVfB8liNnxJ8+GCajNFX44pEwLtfMq7rusRWgQbAQtRi2QZp0KpGqY02p9Oc1tBotoFogyZ1jTNMliZbJKOpLNdiVIrUSNNANMmaLb2tqhQON/R/Hf2JHXawbkhnF/x8gkpA31/DI+NqdGUIhuGN4JWpV9n+9U5rNWDlqJGMO9WvV69tdtqurp3sUe3i1U7RmtutR1s32JGO1T1TmWFPUHvbXUaXdBgOTvxAc4N4VXOSPJk55Iw65+dxfTxrk3nr0muaEz2i26zS6wxG7PwwZ9vtyzxhLryZ19MNc9lzZrAZaPNzLi7ooTaBycBJL51tf1bX4xofykayl8eGTcfrLmUmo3mgny4TK2FQrFxUSmloWz5tjXOz0R2y2VBmN4qn9Hy6CPYJ6xr8OGnEnuMbc9oJDqcdS6430mXmj6NZS3XpY4vi56edvA/3pwkzYDumsN8Nu/19ru/8xnQuBcuIvvRJCuUume43kxpKtuh8FtbKRXBYqmmI64GaxBIFfGOsxE3llNDcMr9QMyqcQd2R58mqiL2x7O2dhFS3UzMVxs0F61LxuW6Y1rxrnGMtUC4HT1vHqu3NPCDPnmO4vM5dwv2yNV3vY86v0c3hTlBkzuEszlvXnLbcsm3F7wl2nAj186HVkA7WQEsURnTN4am9nw26Te7AqUZA1QLzYJxNozY/8M5GVujzQkmVmRNlwvnEt7c1t72eib7hGItokSJnqB4GB5qlBhrdpcbr5t47tpp7MbX7i13kHIvzYuIICTpFF6HVWra7++kuPrl8sZdHfaqVy5p3sEXuzPOtsZyck+NwftKGuljUliMBkcfZ3GiIdqMn8Wsy3Qy7QynKUBsNz/vYOirHhB4Omp7Nt1v0LguEBVsb1xOtNstG7PKws8lUXDmcu7lMOK7QtqN8H3fsY33umvWlduoNd2ZfzRApbf1FvV4PtXlrNpbHrZXruYt6v19zJWGWHcXCQGGzEbpFUvgC6ozmktnpTvhz2Bu6c0l1BblPyekm6h9d1Ulam+Fa7KmK1uRJeZCeL2LHmk59Stf6s1WjtwomqsqMKBd17M4u782PgtRbe1pkCkkzGfQdaXxRsqCGjovgYu8Om0I5BtpglR/5TTTk1bi7lSyGT5VOg42olipt1PZwt594q86Qobq2Pjqc7ehYM5goaOutzrQoNmyGtoM2Dydh3p/NOlJrHXmbS2Bq2kaPJXpxmCxnqr2093Mog8iYMXo2M+tM6DD92LUDNhyuRF2wpXSsUxHqMhd5Umd6XnO5nNuyEl4MiT9NVxG9M3ZhOsinq8Jf9uxLbHfVQKX8ROWF1ahG8QPZzuWapwX+TGwu/Bntbdac20hirt3enxVpa0uRM+sIDbt3lMJsnXkLL5PWy2izmvLCbqt4w/0+mpvZZBQttsGGQhO5QPPxesZL3YhxlPwkSbsDTGBuU1noWndhHXputBDJVffop/WBC0mlhCDTsy7eIOEWiyPTrHNW1MwVoxZfTmc5Vcils6LbTZIP56NitBP3G6POGqfjpUY7bijLVJSuDEtuMEzKU0dZGOycbUAOYzNnZZlvSM122OS6uz5Dd6G7MhI7DJtt1PWdwDlbtDbzBKpdbOXDEuZLa9G57Ht7fcgW6/3GUrp1h2yKwijVxZWr9CiR9TrCYVAk9L6ud6WVLWT2TlunTF9Q4ChKYDnTPzaLzB0lJIIpRyhCTu55YldleW7p58M57U0bw63YW4SbKFAnxdzzVJSns6IhZRZqmH6LaUq47JXQ2tsF3w39sJHb8+XU9xqUgCz2MlfYebOrSBC0AWObQraQY4sbMStxoSTjvZjr3dxwNFK8NKealKGAtQrubE65eM3JqN7gmUm7xe9zNZejlJ563Lgxh/16YfuCqnEdS5NYe7/tDeXWcLPaDH1LaV0yd0BG2kIXFsPuyN+NNeTS/VzjGtJ6z/ub0FI76Xnf6HWmTV3xo8ZAXM/kLJUnl6Le4eWx5SRMwuhyakjLYTZFzGSXa0m8Cgtu5Uk5ucpXS7qwlkfFSRenEVcsEjT0U3qgkXtaaUVoIfWPEsUf3ZDUhim5HG2HQnO6mLJj3lD0Dncx0oxPzPXkdD7tLNSFXn3hnZzcGKLNCtvaTO1swnw2b3emdZ1ZpCdhxASx4fVmE3GynLaH6Vjy6IKZM4g+BSFki3FJKI1CgmLVhtbgSB53TL0ZZaw6VvmkKQ9nDB0FC+6c6CNbFNWDNGC4/ng0PfUUpkXZ7Wk0nJ5GfNBQu6ncFCZePBlLqbksHLuzr9fUgy7UDgydHXRuX1u68XpGphY+w6h4dKEuLoID7JAI3eYoPrW0pM72pEFRyFyfay+3Qi434fA1+hY3m6K1xfZ4j1plrUaDOU5i/TDpzxvk6rS3ED/vX2QjlCZ1b7g4L3fQOw/TkJUgmQ9aanYVvs+utgt3uECrQu2ydXO0PbnONqwb8XTTmchW3hRrpF0cN3tmR4XN+kB0OyfW7neGW701cPqrgXNoucxSV73cFvuMyxvHIus0amNN2tNc21js6DTyJqNlq6to/Kojr7NzoInLntZgJztRr+92bMdXBOUUeUHfczV5ZPfCzNYZkQqyUX+RA/GuOY3xWY3zlecpWnIU5pK4pOY7Gq2iobHoHOlDznt+oPIO2rHnw4q9RNtwJNusczpctCZXY4X2KQpWbGdgMJMBSa4W0Ymb6rkbHUWBLowBbTUss+j5m10jPkydNJOpvbad7424RW0Te5S1xpwbdvROnoQUJbbZhslrjXgkeutz0XZYYzFfW7Os25lZg9pcyoemlCWanhYTeyQ3lLGTibqYOn1nZLvWrjPLj3Yyy+q9bs5lfm8gcEJ/6NgZ2m80u5Y0zImzoMmutVRm3SA+m6uxZxfty+A45lNz0bYWaF0/cZvNIm+3NLWu87XI41nEUE29gxjaF+IDpY1EfVcwjrXZuT7ldMkdaZKBL3dm3OCozki56AisO6c43tgcVgXF9PtxW5+KzRVnUK1jx+ddOaWZpbxXMonZtPdG3wydTkMCarydcvOYEVqnKX9Y5yc5705oMusUYWocRn5TXI/5aCefs9QX5WljhPqomUZNB2jGakhHVDcg+YiuzRUS2n8HjXY7qqCO5+F5SAnivCmwxXipOf542zvSm17TrvszZWtPjjNylkyoUXQ49nuWFNQW6eFEnlI+0ics0+DpQm/Xh8dm+zAJpmQu9C/R1Fz1L9s1HZJMXZrTQcSwYpdEF9Od9lf21gpHwXY5aaYtoCX0MVsavFis2c2hkQ2bZ9Th3O6gw9SCpu5FcLFk/NOgP10eJgO2Lxr0YCLsN3N1JCQTZ9ubRLvGKBI3gVYTPdQ5orTOqUu9N78Il1a3Oe4O+93eXEiHa3Lda4z77OjAWl01JfOoph+kupr03PXoZJ/6iudv6+R8ri82Nr80nQZjebWWNh+uwtbKau1rbKveUfqpwJknK8jYZbrod0VjrlFTP/BI3zVR2+vCeTBZUlqvexlt15Og09q1URIvBup+OjU6dkOujxifjs6WZLdn4sKRz4kwh2xID+1VUrPHHUc012221s6jlk71R9wUSbvRkUWydhDbctec19iRPUW8MOamtVAJeL4XjelkKS6TkTj35osV31iaHLsIkh7ZOFicwF50d4vWaR1yq95FGRf485odwgjz+TOMQviL43Ug/9nn63J0/v+ay6rxKsxBYaAjPKrj6fyl1PXyU+0wiMa6A7qrcTLxMus6sFXD5FO168mrviIAiS4/74ZBNXxX3xtS1cL/oHz7B1FYV32rgIvcidNM9Z7Kzx135ZB7/cZ0d/skUMkGQ8p/TyinXDDmGbz5L50R9FD+IQAA -->
