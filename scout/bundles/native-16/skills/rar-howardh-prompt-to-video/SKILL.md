---
name: "rar-howardh-prompt-to-video"
description: "Renders videos from structured scene descriptions using Remotion \u2014 title, content, quote, and list scenes with style presets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/prompt_to_video_agent", "rar_sha256": "3bcdd845998ff84158cc2c2ab54fefcb54b0e3a6106fd4bfb8e59252b58694c6", "source_kind": "rar-agent", "source_commit": "fd516f31dfe3dc22441098daa43af4b5af84e047", "version": "1.1.0", "author": "RAPP Contributor", "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt_to_video"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/prompt_to_video_agent`. The original RAPP
agent is preserved byte-for-byte in `prompt_to_video_agent.py` and in the RCI capsule.

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

PromptToVideo Agent — Renders videos from structured scene descriptions using Remotion.

Assimilated from:
- remotion-dev/remotion (React video framework — programmatic rendering)
- remotion-dev/template-prompt-to-video (story-to-video pipeline & timeline model)
- jhartquist/claude-remotion-kickstart (component patterns & composition factory)

The LLM breaks a user's prompt into scenes; this agent writes them into a
Remotion workspace and renders to MP4.  First run creates the workspace and
installs dependencies (~30s).  Subsequent renders reuse the workspace.

Scene types: title, content, quote, list
Style presets: bold (dark+red), minimal (light+blue), neon (dark+green), warm (dark+orange)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "resolution": {
      "description": "Video resolution (default: 1080p)",
      "enum": [
        "1080p",
        "720p",
        "vertical",
        "square"
      ],
      "type": "string"
    },
    "scenes": {
      "description": "Ordered array of scene objects forming the video",
      "items": {
        "properties": {
          "accent_color": {
            "description": "Hex accent color",
            "type": "string"
          },
          "background_color": {
            "description": "Hex background color",
            "type": "string"
          },
          "duration_seconds": {
            "description": "Duration in seconds (default: 4 for title, 6 for others)",
            "type": "number"
          },
          "items": {
            "description": "Bullet items (for list scenes)",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "subtitle": {
            "description": "Secondary text (subtitle/body/attribution)",
            "type": "string"
          },
          "text": {
            "description": "Primary text (title/heading/quote)",
            "type": "string"
          },
          "text_color": {
            "description": "Hex text color",
            "type": "string"
          },
          "type": {
            "description": "Scene layout type",
            "enum": [
              "title",
              "content",
              "quote",
              "list"
            ],
            "type": "string"
          }
        },
        "required": [
          "type",
          "text"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "style": {
      "description": "Visual style preset (default: bold)",
      "enum": [
        "minimal",
        "bold",
        "neon",
        "warm"
      ],
      "type": "string"
    },
    "title": {
      "description": "Video title (used for filename and title scene)",
      "type": "string"
    }
  },
  "required": [
    "title",
    "scenes"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prompt_to_video_agent.py` and embedded as the fenced Python below (sha256 3bcdd845998ff841…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prompt_to_video_agent.py` first:

```bash
python3 prompt_to_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prompt_to_video_agent.py   # or on stdin
python3 prompt_to_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PromptToVideo Agent — Renders videos from structured scene descriptions using Remotion.

Assimilated from:
- remotion-dev/remotion (React video framework — programmatic rendering)
- remotion-dev/template-prompt-to-video (story-to-video pipeline & timeline model)
- jhartquist/claude-remotion-kickstart (component patterns & composition factory)

The LLM breaks a user's prompt into scenes; this agent writes them into a
Remotion workspace and renders to MP4.  First run creates the workspace and
installs dependencies (~30s).  Subsequent renders reuse the workspace.

Scene types: title, content, quote, list
Style presets: bold (dark+red), minimal (light+blue), neon (dark+green), warm (dark+orange)
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/prompt_to_video_agent",
    "version": "1.1.0",
    "display_name": "PromptToVideo",
    "description": "Renders videos from structured scene descriptions using Remotion — title, content, quote, and list scenes with style presets.",
    "author": "RAPP Contributor",
    "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt_to_video"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@howardh/markdown_to_slides_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import os
import re
import subprocess

try:
    from openrappter.agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        from agents.basic_agent import BasicAgent

# ── Paths ────────────────────────────────────────────────────────────────────

_BRAINSTEM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_WORKSPACE = os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "remotion_workspace")
_VIDEOS_DIR = os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "videos")
_WORKSPACE_VERSION = "2"

# ── Style & resolution presets ───────────────────────────────────────────────

_STYLES = {
    "bold": {
        "backgrounds": ["#1a1a2e", "#16213e", "#0f3460", "#533483", "#1a1a2e"],
        "text_color": "#ffffff",
        "accent_color": "#e94560",
    },
    "minimal": {
        "backgrounds": ["#ffffff", "#f8f9fa", "#e9ecef", "#dee2e6", "#f8f9fa"],
        "text_color": "#212529",
        "accent_color": "#0066cc",
    },
    "neon": {
        "backgrounds": ["#0a0a0a", "#0d0d1a", "#1a0a2e", "#0a1a2e", "#0d0d1a"],
        "text_color": "#ffffff",
        "accent_color": "#00ff88",
    },
    "warm": {
        "backgrounds": ["#2d1b00", "#3d2400", "#1a0f00", "#4a2d00", "#2d1b00"],
        "text_color": "#ffe4c4",
        "accent_color": "#ff6b35",
    },
}

_RESOLUTIONS = {
    "1080p": (1920, 1080),
    "720p": (1280, 720),
    "vertical": (1080, 1920),
    "square": (1080, 1080),
}

# ── Remotion project template files ──────────────────────────────────────────

_PACKAGE_JSON = """{
  "name": "brainstem-video",
  "private": true,
  "dependencies": {
    "@remotion/cli": "^4.0.0",
    "playwright": "^1.49.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "remotion": "^4.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "typescript": "^5.5.0"
  }
}"""

_TSCONFIG = """{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": false,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true
  },
  "include": ["src"]
}"""

_INDEX_TS = """import {registerRoot} from 'remotion';
import {RemotionRoot} from './Root';
registerRoot(RemotionRoot);
"""

_ROOT_TSX = """import React from 'react';
import {Composition} from 'remotion';
import {Video} from './Video';
import {DemoVideo} from './DemoVideo';
import {timeline} from './data';

let demoCapture: any = null;
try { demoCapture = require('./demo_data').capture; } catch(e) {}

export const RemotionRoot: React.FC = () => {
  const totalFrames = timeline.scenes.reduce(
    (sum: number, s: any) => sum + s.durationFrames, 0
  );

  const demoFrames = demoCapture?.totalFrames || 300;
  const demoFps = demoCapture?.fps || 30;
  const demoW = demoCapture?.width || 1920;
  const demoH = demoCapture?.height || 1080;

  return (
    <>
      <Composition
        id="BrainstemVideo"
        component={Video}
        durationInFrames={totalFrames}
        fps={timeline.fps}
        width={timeline.width}
        height={timeline.height}
        defaultProps={{timeline}}
      />
      <Composition
        id="BrainstemDemo"
        component={DemoVideo}
        durationInFrames={demoFrames}
        fps={demoFps}
        width={demoW}
        height={demoH}
        defaultProps={{capture: demoCapture || {steps: [], viewport: {width: 1920, height: 1080}, fps: 30, width: 1920, height: 1080, totalFrames: 300, framesPerStep: 120, capturePrefix: ''}}}
      />
    </>
  );
};
"""

_VIDEO_TSX = r"""import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
} from 'remotion';

/* ── Types ─────────────────────────────────────────────────────────────── */

interface Scene {
  type: 'title' | 'content' | 'quote' | 'list';
  text: string;
  subtitle?: string;
  items?: string[];
  durationFrames: number;
  backgroundColor: string;
  textColor: string;
  accentColor: string;
}

interface TimelineData {
  title: string;
  scenes: Scene[];
  fps: number;
  width: number;
  height: number;
}

/* ── Shared animation ──────────────────────────────────────────────────── */

const FadeIn: React.FC<{delay?: number; children: React.ReactNode}> = ({
  delay = 0,
  children,
}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame - delay, [0, 15], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const y = interpolate(frame - delay, [0, 15], [30, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  return (
    <div style={{opacity, transform: `translateY(${y}px)`}}>{children}</div>
  );
};

const useExitOpacity = (durationFrames: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [durationFrames - 15, durationFrames], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
};

/* ── Scene components ──────────────────────────────────────────────────── */

const TitleSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const scale = spring({frame, fps, config: {damping: 100, stiffness: 200}});
  const subOp = interpolate(frame, [20, 40], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const exitOp = useExitOpacity(scene.durationFrames);
  const lineW = interpolate(frame, [10, 40], [0, 200], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        alignItems: 'center',
        opacity: exitOp,
      }}
    >
      <div
        style={{
          transform: `scale(${scale})`,
          color: scene.textColor,
          fontSize: 80,
          fontWeight: 800,
          textAlign: 'center',
          padding: '0 100px',
          lineHeight: 1.2,
          fontFamily: 'Inter, Segoe UI, sans-serif',
        }}
      >
        {scene.text}
      </div>
      {scene.subtitle && (
        <div
          style={{
            opacity: subOp,
            color: scene.accentColor,
            fontSize: 36,
            marginTop: 30,
            fontFamily: 'Inter, Segoe UI, sans-serif',
            letterSpacing: 2,
          }}
        >
          {scene.subtitle}
        </div>
      )}
      <div
        style={{
          position: 'absolute',
          bottom: 100,
          width: lineW,
          height: 4,
          backgroundColor: scene.accentColor,
          borderRadius: 2,
        }}
      />
    </AbsoluteFill>
  );
};

const ContentSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const exitOp = useExitOpacity(scene.durationFrames);
  const barH = interpolate(frame, [0, 20], [0, 200], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        padding: '0 140px',
        opacity: exitOp,
      }}
    >
      <FadeIn>
        <div
          style={{
            color: scene.accentColor,
            fontSize: 52,
            fontWeight: 700,
            marginBottom: 30,
            fontFamily: 'Inter, Segoe UI, sans-serif',
          }}
        >
          {scene.text}
        </div>
      </FadeIn>
      {scene.subtitle && (
        <FadeIn delay={10}>
          <div
            style={{
              color: scene.textColor,
              fontSize: 28,
              lineHeight: 1.6,
              fontFamily: 'Inter, Segoe UI, sans-serif',
              opacity: 0.9,
              maxWidth: 900,
            }}
          >
            {scene.subtitle}
          </div>
        </FadeIn>
      )}
      <div
        style={{
          position: 'absolute',
          left: 100,
          top: '30%',
          width: 6,
          height: barH,
          backgroundColor: scene.accentColor,
          borderRadius: 3,
        }}
      />
    </AbsoluteFill>
  );
};

const QuoteSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const exitOp = useExitOpacity(scene.durationFrames);
  const qOp = interpolate(frame, [0, 15], [0, 0.15], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        alignItems: 'center',
        opacity: exitOp,
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: 150,
          left: 100,
          fontSize: 300,
          color: scene.accentColor,
          opacity: qOp,
          fontFamily: 'Georgia, serif',
          lineHeight: 1,
        }}
      >
        {'\u201C'}
      </div>
      <FadeIn>
        <div
          style={{
            color: scene.textColor,
            fontSize: 42,
            fontStyle: 'italic',
            textAlign: 'center',
            padding: '0 160px',
            lineHeight: 1.6,
            fontFamily: 'Georgia, Times New Roman, serif',
          }}
        >
          {scene.text}
        </div>
      </FadeIn>
      {scene.subtitle && (
        <FadeIn delay={15}>
          <div
            style={{
              color: scene.accentColor,
              fontSize: 24,
              marginTop: 40,
              fontFamily: 'Inter, Segoe UI, sans-serif',
            }}
          >
            {'\u2014'} {scene.subtitle}
          </div>
        </FadeIn>
      )}
    </AbsoluteFill>
  );
};

const ListSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const exitOp = useExitOpacity(scene.durationFrames);
  const items = scene.items || [];

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        padding: '0 140px',
        opacity: exitOp,
      }}
    >
      <FadeIn>
        <div
          style={{
            color: scene.accentColor,
            fontSize: 48,
            fontWeight: 700,
            marginBottom: 50,
            fontFamily: 'Inter, Segoe UI, sans-serif',
          }}
        >
          {scene.text}
        </div>
      </FadeIn>
      {items.map((item, i) => (
        <FadeIn key={i} delay={15 + i * 12}>
          <div
            style={{
              color: scene.textColor,
              fontSize: 30,
              marginBottom: 22,
              display: 'flex',
              alignItems: 'center',
              fontFamily: 'Inter, Segoe UI, sans-serif',
            }}
          >
            <div
              style={{
                width: 12,
                height: 12,
                borderRadius: 6,
                backgroundColor: scene.accentColor,
                marginRight: 20,
                flexShrink: 0,
              }}
            />
            {item}
          </div>
        </FadeIn>
      ))}
    </AbsoluteFill>
  );
};

/* ── Main composition ──────────────────────────────────────────────────── */

export const Video: React.FC<{timeline: TimelineData}> = ({timeline}) => {
  let offset = 0;
  return (
    <AbsoluteFill>
      {timeline.scenes.map((scene, i) => {
        const from = offset;
        offset += scene.durationFrames;
        return (
          <Sequence key={i} from={from} durationInFrames={scene.durationFrames}>
            {scene.type === 'title' && <TitleSlide scene={scene} />}
            {scene.type === 'content' && <ContentSlide scene={scene} />}
            {scene.type === 'quote' && <QuoteSlide scene={scene} />}
            {scene.type === 'list' && <ListSlide scene={scene} />}
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
"""

_DEFAULT_DATA_TS = """export const timeline: any = {
  title: "Test",
  fps: 30,
  width: 1920,
  height: 1080,
  scenes: [
    {
      type: "title",
      text: "Hello World",
      subtitle: "Brainstem Video",
      durationFrames: 90,
      backgroundColor: "#1a1a2e",
      textColor: "#ffffff",
      accentColor: "#e94560",
    },
  ],
};
"""

_DEMO_VIDEO_STUB = """import React from 'react';
import {AbsoluteFill} from 'remotion';
export const DemoVideo: React.FC<{capture: any}> = () => (
  <AbsoluteFill style={{backgroundColor: '#000', justifyContent: 'center', alignItems: 'center'}}>
    <div style={{color: '#fff', fontSize: 40}}>No demo data loaded</div>
  </AbsoluteFill>
);
"""

# ── Helpers ──────────────────────────────────────────────────────────────

def _slugify(text):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')
    return slug[:60] or 'video'


def _node_available():
    for cmd in ('node', 'node.exe'):
        try:
            r = subprocess.run([cmd, '--version'], capture_output=True, timeout=10)
            if r.returncode == 0:
                return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return False


def _run(cmd, cwd, timeout=300):
    """Run a shell command. Returns (ok, stdout, stderr)."""
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, shell=True)
        return r.returncode == 0, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return False, '', f'Command timed out after {timeout}s'
    except Exception as e:
        return False, '', str(e)


# ── Agent ────────────────────────────────────────────────────────────────

class PromptToVideoAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Video title (used for filename and title scene)"
                    },
                    "scenes": {
                        "type": "array",
                        "description": "Ordered array of scene objects forming the video",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["title", "content", "quote", "list"],
                                    "description": "Scene layout type"
                                },
                                "text": {
                                    "type": "string",
                                    "description": "Primary text (title/heading/quote)"
                                },
                                "subtitle": {
                                    "type": "string",
                                    "description": "Secondary text (subtitle/body/attribution)"
                                },
                                "items": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "Bullet items (for list scenes)"
                                },
                                "duration_seconds": {
                                    "type": "number",
                                    "description": "Duration in seconds (default: 4 for title, 6 for others)"
                                },
                                "background_color": {
                                    "type": "string",
                                    "description": "Hex background color"
                                },
                                "text_color": {
                                    "type": "string",
                                    "description": "Hex text color"
                                },
                                "accent_color": {
                                    "type": "string",
                                    "description": "Hex accent color"
                                }
                            },
                            "required": ["type", "text"]
                        }
                    },
                    "style": {
                        "type": "string",
                        "enum": ["minimal", "bold", "neon", "warm"],
                        "description": "Visual style preset (default: bold)"
                    },
                    "resolution": {
                        "type": "string",
                        "enum": ["1080p", "720p", "vertical", "square"],
                        "description": "Video resolution (default: 1080p)"
                    }
                },
                "required": ["title", "scenes"]
            }
        }
        super().__init__(self.name, self.metadata)

    # ── Workspace management ─────────────────────────────────────────────

    def _workspace_version_path(self):
        return os.path.join(_WORKSPACE, ".workspace_version")

    def _workspace_current(self):
        vpath = self._workspace_version_path()
        if not os.path.isfile(vpath):
            return False
        try:
            with open(vpath, "r") as f:
                return f.read().strip() == _WORKSPACE_VERSION
        except OSError:
            return False

    def _ensure_workspace(self):
        """Create or update the Remotion workspace. Returns workspace path."""
        need_npm = not os.path.isdir(os.path.join(_WORKSPACE, "node_modules"))
        need_files = not self._workspace_current()

        if not need_npm and not need_files:
            return _WORKSPACE

        src_dir = os.path.join(_WORKSPACE, "src")
        os.makedirs(src_dir, exist_ok=True)

        if need_files:
            files = {
                "package.json": _PACKAGE_JSON,
                "tsconfig.json": _TSCONFIG,
                os.path.join("src", "index.ts"): _INDEX_TS,
                os.path.join("src", "Root.tsx"): _ROOT_TSX,
                os.path.join("src", "Video.tsx"): _VIDEO_TSX,
                os.path.join("src", "data.ts"): _DEFAULT_DATA_TS,
                os.path.join("src", "DemoVideo.tsx"): _DEMO_VIDEO_STUB,
            }
            for relpath, content in files.items():
                fpath = os.path.join(_WORKSPACE, relpath)
                os.makedirs(os.path.dirname(fpath), exist_ok=True)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
            with open(self._workspace_version_path(), "w") as f:
                f.write(_WORKSPACE_VERSION)

        if need_npm:
            ok, _out, err = _run("npm install --no-fund --no-audit",
                                 _WORKSPACE, timeout=120)
            if not ok:
                raise RuntimeError(f"npm install failed:\n{err[:600]}")

        return _WORKSPACE

    # ── Timeline builder ─────────────────────────────────────────────────

    def _build_timeline(self, title, scenes, style, resolution):
        preset = _STYLES.get(style, _STYLES["bold"])
        w, h = _RESOLUTIONS.get(resolution, _RESOLUTIONS["1080p"])
        fps = 30
        bgs = preset["backgrounds"]

        built = []
        for i, s in enumerate(scenes):
            stype = s.get("type", "content")
            default_dur = 4 if stype == "title" else 6
            dur_s = s.get("duration_seconds", default_dur)
            dur_frames = max(int(dur_s * fps), 30)

            built.append({
                "type": stype,
                "text": s.get("text", ""),
                "subtitle": s.get("subtitle", ""),
                "items": s.get("items", []),
                "durationFrames": dur_frames,
                "backgroundColor": s.get("background_color", bgs[i % len(bgs)]),
                "textColor": s.get("text_color", preset["text_color"]),
                "accentColor": s.get("accent_color", preset["accent_color"]),
            })

        return {"title": title, "fps": fps, "width": w, "height": h, "scenes": built}

    # ── Data writer ──────────────────────────────────────────────────────

    def _write_data(self, workspace, timeline):
        data_path = os.path.join(workspace, "src", "data.ts")
        json_str = json.dumps(timeline, indent=2, ensure_ascii=False)
        with open(data_path, "w", encoding="utf-8") as f:
            f.write(f"export const timeline: any = {json_str};\n")

    # ── Renderer ─────────────────────────────────────────────────────────

    def _render(self, workspace, slug):
        os.makedirs(_VIDEOS_DIR, exist_ok=True)
        out_path = os.path.join(_VIDEOS_DIR, f"{slug}.mp4")

        cmd = (
            f'npx remotion render src/index.ts BrainstemVideo '
            f'"{out_path}" --overwrite --log=error --port=9876'
        )
        ok, stdout, stderr = _run(cmd, workspace, timeout=300)
        if not ok:
            detail = (stderr or stdout)[-800:]
            raise RuntimeError(f"Render failed:\n{detail}")

        if not os.path.isfile(out_path):
            raise RuntimeError("Render command succeeded but output file not found.")

        return out_path

    # ── Main entry ───────────────────────────────────────────────────────

    def perform(self, title="Untitled", scenes=None, style="bold",
                resolution="1080p", **kwargs):
        if not _node_available():
            return (
                "Error: Node.js is required but not found on PATH. "
                "Install Node.js v18+ (https://nodejs.org) and try again."
            )

        if isinstance(scenes, str):
            try:
                scenes = json.loads(scenes)
            except json.JSONDecodeError:
                return "Error: 'scenes' must be a valid JSON array of scene objects."

        if not scenes or not isinstance(scenes, list):
            return "Error: At least one scene is required in the 'scenes' array."

        slug = _slugify(title)

        try:
            workspace = self._ensure_workspace()
        except RuntimeError as e:
            return f"Error setting up video workspace: {e}"

        timeline = self._build_timeline(title, scenes, style, resolution)
        self._write_data(workspace, timeline)

        total_frames = sum(s["durationFrames"] for s in timeline["scenes"])
        total_seconds = total_frames / timeline["fps"]

        try:
            out_path = self._render(workspace, slug)
        except RuntimeError as e:
            return str(e)

        return (
            f"RENDER_COMPLETE: Video rendered successfully!\n"
            f"VIDEO_URL: /videos/{slug}.mp4\n"
            f"Duration: {total_seconds:.1f}s ({total_frames} frames @ {timeline['fps']}fps)\n"
            f"Resolution: {timeline['width']}x{timeline['height']}\n"
            f"Scenes: {len(timeline['scenes'])}\n"
            f"Style: {style}\n\n"
            f"IMPORTANT: In your response, embed the video using exactly this markdown:\n"
            f"![video](/videos/{slug}.mp4)"
        )


if __name__ == "__main__":
    agent = PromptToVideoAgent()
    print(agent.perform())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
