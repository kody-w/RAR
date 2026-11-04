---
name: "rar-howardh-prompt-to-video"
description: "Renders videos from structured scene descriptions using Remotion \u2014 title, content, quote, and list scenes with style presets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/prompt_to_video_agent", "rar_sha256": "ed75b1d6e1bedafee181b2eefc0a1e98a64533df1c7067383cc10450bea4c83f", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.0", "author": "RAPP Contributor", "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt_to_video"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prompt_to_video_agent.py` and embedded as the fenced Python below (sha256 ed75b1d6e1bedafe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prompt_to_video_agent.py` first:

```bash
python3 prompt_to_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prompt_to_video_agent.py   # or on stdin
python3 prompt_to_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/prompt_to_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/prompt_to_video_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/prompt_to_video_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/617Z5PjxrLlX+HOi9g7epQE72bjRixAAiBAOJIgSOLphgTvvYdW+9u3yO6ZkRndD7vbMdMNU5WVlebkSUbx1w/O0MdV++HThzNrGJtdVfZt4g49ePT9Bz/ovDap+6QqnwOC0g/abjMmflB1m7Ctik3Xt4PXD23gbzovKIPN76Z0m6FLymhzDorqeb/5aUBhBN/0SZ8H3288sFRQ9t9vmqHqwb1T+ps86fo3Qd1mSvoYyF/yYFO3QRf03Y9ApWB2ijoPug+f/utf339IwPWHT79+8HKnA48+GECnujcr66kiGwHxYErulBF4Vy9goyW4r4M2rNoCPPKDcPN+97EL8vD7N93++dOHa/m68n/68P27Pv/UqhJo+VIIDHCr/Pnyp3Lzpx+gapUPz/2CUQhMw/VTxn/+ZzY5bdR99+nrjCTclFW/+bms/OBnZ3SS3HHz4OPvh7wJBPYtNx//utRPH/i2rdpPGw1I+DHtNkkHRjdD8nQH8OFLfFgNwLDA+gZrHn4Ec74lRyq73snzL4JGhN5uPsZ9X3efIOipYNr9WLXRdy8v9e2ycSInKX/8s7Tvfir/sL8EBACQXHrBxzcrPg3Y/nmHQN6nv2r1Hgb/3KRdVf6YV47fvQv57o+Dg9kL6v5tmHzRtX3gAYXfTPMt/7zM+cV2/3iT+Y9NMYDYc4ONsxmdPPE3T1Ebp22dZVOF79FduWnggUB87vsvjnxXuGpfd9/Y+jO6/8a7X9Rh+00eOEATEG3vi/7eq0m56ePgq9Iv/f6kTpcPETDbz8+/Sbh8fEXyHzzzV4NPVZt1teMFYOIzE378OSg7kNY/f3nx8XdWf7f4eQBZUrxZeuN0m+DbewvfNwcE9/0TEIb6DUO+rvpp82vw2x938ZScJ+VXhdwhyf2fPz/++I4iX8Nqed5+zb7fqfs2f2qTPvjZd3rn45d1v/+yzB/tU4Fs+DlsneIVgN0A4OG/fvrgD63zFC28Xvz04V8gucCuXk55FwNGvWkE3n73Z4EdCMzSf0r8wwLQ72eH9XPqv3dWNfQ/1w5Ax8+maV/I/PttPX3/f+0wkKIf/2iQb2MQcOyZ1/b8+eedrhoKb/KfNi/k3bwp9CwKg+cFXRcOeb78t5+AyA9/EWFJe17/+XpWPm2gt9IC/fpU/7cfixr/9pT9uyNA2PzBsp9+RMLfus3HX39v398273b+n2D0Z0P/A9j5H//6Dfz+7ttLnL8E0qffT5sSv4/BxPl3z+IgieIePPy2pMsrHoCUPCg/fp31nsH/+u7vpj0DGsx6BfZrzDeHSaqhn01WMz9tpHKzVEP7zIEaVF8QBUHhAh88AeMt397qMSihXp8v4DlAlsJpM7+ayk/fFv/f/us1818f/+qa734//LsPv4FqXL7RgWftB9X1P/5joyZeW3VV2G8uHojaTfsWgM/QMp+rg39P7dpgBMQiAdXvfVzdVk+gfZIGgL2//M+4AtXTj6H6Vd9/7qufX+r87DxL/C8/bkwgpGqTKCmdfPMkMj+Vr1fPBV7koR2fJXHpgx9Ayv7wvHhm7S/flPdjvfzyqnPvYHveSRvPqbshD358an6Lg/JdT88pgTkDbwDy8soDi4dJ/oSjFw6NwZuNuywBtdUHAO4BXrW8ZANLfHoK++WXX1yni38q3+gJtnmjTx0EBnxRZ/PDD2AXYf6Ms5/KwIurzT9+/e0fm/+1+XezXsKfaxiAHL3bGWj4XteioQDDnuDV9YHjv+z862/vtgRiyqDdAK8kYRK8TQZhmwFC9G7Yy4H9ASVIUDCBQYExi7pqX+Ce9D9upHDzRV+w6PNVB+pqXIG65gf1ExxK7xmADtjOF0u+aijI6y5cvgehGrxW/cVtnZeKxc8eGP7LRt0ZAD6rHPx6qvkaBCZXZQLM/8Xtb8+BkPYf3Yb7LOLHjfaMtE3ttE4dt877GqHz5pcnKL5PB8KdTRlMP5VPihk8TfVCnDfzgEHAMt67S394+hzQ2aJwnuj+vvZrjNODsDMrUM+D9ieQkm8h7bRPV3gVUGXZREPiP1nC/3gPqS6uhtx/2Q9o+srdNy/47155xeAfiO7mxXQ/0+v/V5r+ks92XVIAQvrU/ykBxOoPQOe3ET/4wQh9vtl8PAfAfu8I84LaZx36rA3IsAg8K4D1vPeyABb77i/igHfq53I/vKXkD331w5vEj93TN1/v66R+4wX//StFKADfy18y09hpe8CVuh4CPcHgBz98WSVLvAwQsrbffAS+Agj5tBkoo8A1wAb/ffN62CWvPb1HxHdvQBVsFEXduCB7smcYv0fVm6JvsfIG5v/jLd3fYuhFN16ZU7zH00/ll07oK916YcG7x8Ag1cB/3GyEpO1eYLnxwKLvYv44CQTmG2fvvmbUM1M//m8M7r4DMi6D2wHW+FTls/w2+JxVX0S9nP2qUJt+qZ9l6m+6syd3BSN/34592jyboM1HH5SQLQit777fFAnIF4AxH1+pv3XzIQBPy+AZJq9hURsEJXgE4Lx4f1S1oD8Lvns2aglQpAs+fCoBXfj+QwlC6c893bN9c54xBrzWPTs/4AXQwfVJ8Lr7Sv+ed39sXz8zk88jwPJB6Ax5/2nzatOeGgTlAPrC/3rr28A9hb7+jM8VALyAy64ZQPp+AL3n015ALEgtENDP8vcWBH9dWG/fuNC3e4knhyye+felTINVQOgU39ieA8hU2f/sVfmzY//zOodg3ryN2LyN+IaOruNlUftsCf+dlK+j/l7SZzL8mXv9VdJnlvZExM/U96vN8Rd5fo828nVTARO03XdfVwPecIP2RS0+G+SPS3AgUAKQg8+3m49PGb/7BOG73xvyL/q/P3g55eW9wX0p89dFLi/dHYDVfTAD9Pg8EnIrf4EAgLw+MHm2HN+y03POX2UaLciTLxLfxMWgDINJ0Cvj/lbWv/PbS9rfeuztwV929wrG3Fmexec15GsavBnk+w/vYACuXrq9UrXrv5EEYJXPrepr/pu4lwm+Dn4L/G/64Akv38rcbgCg8vvPgn4XSE8Q+n3uvmMQePJ8A/484Qf8eULON/P2b9z+hhevl5uPADj9V4w+a/0TmN4+CHm9fEXbN/z1Z2O8G/MdJr5lj2cFfPto6tcPAOKcZ7P6jgLvdBgMb532h+5JFSDkRxjIA/dvlA+8+/dE+X1wFzuAuYHRgU8RLuKTAQLaBCcMAoRGXDQIQg92kIChHRInMMwPEY+CSQqjMc9DYJyA3cDBPRoLn5sBDYcX/PwkP8lTAdeDQ4RkEBpIY1wUxUiYDuAQY0gqdMgAQwOfhmHY/To1S0r/fVdvSj7t9oWzv1DvbXO/fnBJ/BnoeCexbz87aIv4W6x15/YAlfB2tq/EXj3abCJLVmE6/lGRvIa45gdLHFBSbxQ26s5WFE36LrnMd5RcdM/AQN3jmcUubCzybsKQxkdgQ43O7uy9sEsb9SF1HR/3O8VB4wEbaQGixLSlZTYvS0PnidvVVNCHaS6hCsVtMiuoeNpejKjbrwlZSrdzT7kKjhkaQ0S3a1AmvqnqbFMXF1jGIM0lomHW0IPzOBeQWsVDjYYq4ZuiIC/GevLr4u7LkX8XNercpMfezlNuRjq9zsVSUXE81PH99nwzQ9u3Dx0nq8tDfYj0vuZmV4H2dmuvqr4OwVUgGXthmEnCRmmlKAOZWhROBEbNijCg7peK3gd6BlF3hLnV2FLAUGFKGLHnlSk64cmFIeIddjZg3Nne5pyPIKw54CqnEnsGa3M4XdesyEitRSeRKdftqV5so9umVLssj6WkeA/tB7WG9camePTRihykM6yarMk1ue697o5xTMBLp10r57rPuKqV2EeOJZXOIPS5IklAJMsAKh/O3R/O+gBsVaqoeT0fdSVd7vFiHLVteHd3VhZuUefBWJOG4x4JugWTOMJ5zZ9aDt5vJxG61NHan1UUx3h1ayaeIqFxjGfy7NsqUxHBST8UxjEKiwnf+2ZEixy5KrVIOqcj5+gngV7PNZOXpqZiBZ4W8nErr9DcWOL5Uuy8ox/DB7Vg0ksfozAfOzl7N3aoN+mYHNlaO2YP+hAgBUWJkMNwuB4dl+KUHu864M4nVIdCKVCpWeuE84ATDwhnILSDCxoTpUc56Mbk7yqir4L9w4Ao1MdcnkX2dCEL7ONMsOo5cY+H20VjpS45wzqpmwsqFXQQKNwi6Ung8TYiD8JWxFEx72dKhWkMJiNDc0cNsVkbNtGk68ZhaATxGnp+rJyF+ILY0LSkKinv59RR4eSBnnbFlRvsqHAd25Kma+A+4Ko+xfY1u3OHa7qP5Go7AiSgtCGgOQqhd4YK8fgyw8ODzgx44g4YIY1mWust6Q/llDvbk9fJaxTNRQST++Z4TIjycqKjloCWSzQzTUTx20jVtHrQDpxDDShjB7qEbgNpmyY2K8B8PsnERTZnbxKkWik7dZQuEe88eFM7zwVeDebxau4X7HAiK/LayLOUtu4E3U3PBgjId/VMwkcnux7Xa3ZTH1NY6t1hjYJ8b2wBHxEire4KiUihTD+mu3Thr97jaO127Jm88Il59ybyVGKJvEddbvdQead0H3u0eFRyxj5MR1zMe0Rx0xQl/slnl2iJ1nvakWG0I5HpEeORGazhzcWxPoMDACzXiazZa2hVolw+DtLuIim1UWvy43Y62CBKLtW0QiG0ZSCD2UNR6aP7dktgzAOyUQeDMOaER6reQg3BdrLextzFY32mxMWeMk7K/qydh/KQVxVNqffpFvFxd3QjCQ5SP2Ex0zy1eyvltg6bPpzDXsFZJr+bTmnzYcQ9IrfAikm2tpEMi8HjZOURol2aQZg08i7R1/4kVXZlLZ2qLsZ8jZz75W5yjYea8SzvnemycvRJWNzz0U2WjOJOj0WS/EvkOuw1CNQrzQfWRV9W0ZCNIg4SDU1a7jQmojtwJgVgYcTPZiABz16zPqkdvsBWa+9GrLqATeIxj+xF7izgAkIs7TnFJddiAg7OD4kvwhdfYkmE5cQ0Pd3U9JBPUU0G9nzQ8Com6ARuT1wY6h5jsk6mQiwSscyqsftCDW/SnEvODtvqa3mm1T07GQUxGfhlqIhUs8wZ/C8lIua5dWK5DqRitAVgBvMEvBV2u4ciqHjuPIpL4rYh7ssE68Fb+b6frg0TXw7I9k4+RpYyJw2Vq5S9WHtjuZ11DKa1xGcO6kVDlYleBRb35sJzoetIBNV6IKkibn2MwUdDQxmxxXY8O6c8MumOU5DwVbI8Z/GxzsMRJtVUSViL9Oq2nltB3uFM0f6hIHoKTXijOgcP7uJG58JqYV9sa+yhFxdVHceQk48QiqGIt7KdevfHIpKIYgWEg4H6A4tge8jh7opxRyT7HnBciMfVwAjGzsQLnhJUt9cP8wHEZtxm8gmlD7DeFdctVKAHV18X+RqyQnsnV6fBHKOCl+1Nw0CLSMpndFj6lojhwDB7946spnU+yRdL3GWnQ2xvpSWE4zOGPzIF0pTrro/0qI3DeGWc0E3StSe46UihAIRjC1HEePWKdXeCc14/6QKZDcSKbsG28dgPA2dgaoop+lFobzPgZ/khFjCI1c8J7ELz7eLvEAyx3aQjLlVrrU3XcQZP1rl5cdxisUT4pjMRIwbD2qDzPhkHF0G2p0Q1BzMdemQlHLULliENAeCOxP0MnJuOxgO2sRN3KwdYXddHgHmqBzMmZgEXEPVeuBnIzYMa9TD3C0YwmK0S4xWTItdHqcLgrhV2XVT2eNURu4yHvTpzs3Ldnu5ibBp3/TRJM4MrbGeJHZX0Lt1tPSphG5Zsw6h5MFt1PrPIbUmGvXzXWJ3MH6Mani7QogyskrHbQUq8LGuD9GwS/VTXj9O9kdwMau3+RjVFUkxNe0Ki/OqTzRDi3YrPk3DBLhoNAwJ5O43DUeyYiiZPY2Gat4yJjgeBhJrCOSF3KrxieVt4N2nYuuh165/pY5OhQnt2xBk2+glC71tm28KZgdD0NGoi58nu2hd7LfQcGVbJyYYssql5OzizSXjeFqf9gTkqqqntThN6X4LAO4V40jtXm3vQ/LWWqVRHjqJMeb4nj/Jju2so/CgfcGtyT848Ux2GjcYBzfdjOZ+nxeJCWtvu+tG6eY/yUdx3zARpZs6xwkzsz0Z+51AGgXqII3hZOqWhjbtdsE9hi3/I0RhL7v2KKrfguA3HM4D20U7t2fSqWlMnRlZ6ApVsw6xIfZ+IdcmEjtCBQn0x6eOCgJcH40bFSW+fdXOEm+IGRXGTS3lxsbJVcCD5QvI5Gz1cg0fiZvXkPsDJtl1JoY+87nLAIN1sOYp3jTheCDzdnbjicrowclPgeEXLUy/u5qY8lhwKCFIn5SF/CiZT6sw6GgYFB/HZ42KVOe7eIi9o1ewudvqAikG1u9upoSJsPilKzFuA8e72vXqTYCQLURnVAv8cq6FgzLudb9zEmQQ8V/FUvj+Ra8VV6q1/XP1Ebi/B2Gikq88SDXXpXQlystMc5lp4cw7fFJnZWktO4MqCSFUCkFkxhuJ+cI+8q1fqjt16Z2Je2OaRqTslZ+Rg9Fn4mGpxmfaV3QlEd0kNupUrjN81N9tJY+XRzqaDw48LqBDGsE8Vf+qo8uaf94ptBDS6no8XJJTFyKOlwt92WYyzDpxdhunYi0xIMvOpP6N6TdM9dqIRnLmM5PVoKbXKIlR/fGA9POKEM7Z1NqEixNv0RT0KhjtO252lyx2HOU1rxCId34bEDJKJXIQp1JT9Po/dhjRUZYGlY/yg0tOMa9WVr+Lyml1x71xi8T307UYB/WoIC9DDrHqBXS9D5iaPwwmS2NPxhuqLHi4IAXWgEqvHKq0z3j8+XNI/cztN3KtdJrZhr8oxbhNpUj0KO96mLS529IywmDFgDxWgz0lc0i1hLaVEnakDFVzQPWq54VnaC6oqRD3bTdUNO9UPg63uvZ0Y1PG2l8uzCt81ki32doLyUnk5bufEYKkyDohFbwIcCxrpQC+tfs0IXXVQqWebq3oJMZQKzxnzAPxmsM66gOaEdA/GQJfPJM0OXRpUWQeCurgx/D2KWRXuVmmwlVWCmZMHX3LlcLLEK9HvecoZNNY8ebFxPxe8ec/7YbtjCd9FuQt7DlQltDUkW3tzvdtx2EQrE64MDKhkXhTOVclvnDANZb6rjIyssz7K+UqI6yVue0y9CB4zznxzyU0r31vCdKbu5mN3Icaypo4cFFPSpEWX20URy55mI8PyypnSCgZZ2vzwiBeEku7i1MLued4hh0ZDlt3jQWYdrnYqrAaXNMNxpiaw9aaYfVt6cdX7kUSaFavAqY5H5eN00VcCqkVrZCJICDUmULbWnVrxUVjmDjlX3f1+2Z0j6nzdxUlUXrpR9yJxIpNwZGn7Tuf42ZWiZSfPvHFvYBiXlXwfNDidUdW9a1abAPVxhWcGAowTEwWhT1iBCE+S2fN5lmHAdSmR6D0ZwYtzdDjbUmae6iuGj/kMcYfL45Ri5JY95tMZ5Ep4yTByrC70RdYIUFAkyWEuc1t5NKPuHgeaagmO1g2lC0jmbmhBRpFK2zSkS3BZMvR8e24c0QwUVMCfEByMNeBR/ul0CIya1YvTTliPxw7N0/p26Yj0NjOXw9Ft3YBXJZb2BiY9Xphk689uVzXiuBBWhcjBzjo/O4yF9uBd2PKNYCMOq/YSDOoHOaApNDi65UGnrW2S+3sh7Q7nnAxxgCe3woIZRpkoohbc42mNbbRrCChVkR5ZbrmbFxUC6e0pwZs5HnNLHhiv1kfKLssIOzuCsVYR71NCqaBu7BccdMblwDlrzKGyHxSyLGstD9tu6Vb2rvZ3Ki4pOhtqJb4RCFwHIiw6uYzs7tkhKNIeIORdCUU0Lfb6Wq3qqINk67lLbR2ayOfT4LAP1L0slAdZ301cSID+Ls/z5XIVyEpSQxSvSbLJHXtSHr2MXrgZEx+yLqiP4+6maIjKxhJzvxcuOV0dxtXwBfCZiU5z2D70QZF7PJ8jpWPvL+rVz3b7yZsbJ8XNsDujzO1x3MZKCXUD57IyhEhj6vFYIxAQtJzsdIIPJdSDEL7eUqq/3a3IkzGvruhdQnkG6Eqp3apt49CvALE5I9rZaqYTlwYtksljuzPvsn1kgJR2aR3s5uEtWi/a0FRh5CzOKS+LDlOCVSFIZd53t3tGawF/n++0wsiOWJnVKZ3cg5FhWz6OSkcWHIdxxtt6PY0Wf1jxmE3xO6AEWw02tppn1wYvM9BNbzUS7vGFNA/Qmh72mK5TjDxdB9eqGce/NRDheDd1S3MMUnthkhEJe0O3xCJEwwRX10l8sEXqU6OIQnWKttq9txoUNHJGj54VdXVu670wNMfoVEbjlIea+HxpBt1DqopQ1Oi4TfbZZczXnWgUOroukH010/1pCcIkt+htr/d4fjQqlL0jZIce875vhcGwOWtUUWJnMr6bEMxAbCkWMuERKhMM2qlzeVMo0RDjx6D080zbc7+HAJWD5n0eYNBcgQiv6+3Vy+bjQ8X6QTTSx+NM1rf4qqxpFkVuKKkPnnmcKSppMDSMxXvgoU08PXIkJ8dyB2Etrl3lFZC/MhV7YiTKqY+OA/Bis1d9BO2Z3YyBBF+SiqrPGcpxUEEM7S7HGGdtIus0d1pNsPcytFxZiWJ+Sx9HMuD2tHEdIhWF9u2CjA437YbChNb6hArWPrqPvtGkGj9iOxuR66N79AW5mKcdwuK302UiaK4jqDAZeVuqTYzgWBRW1F089/2CW49YOq2Y3quKiRm01cAQb9oFKdtL11mBLO/b9iHbym7vnuaBNrZK0cCef4I7pw/6rYp6+5OzpxSV0Pf4SFf0HAFE8FjRGdrEvxiucPDKanKdA18fQ5IQ1DGR6SN3IOGMhtUBSqxYGoes1QdnBd0ce/Phae0uYwbIddvefWomtfuNBsUtJOkIJJuedGglliEjjweDsykBvM7HNTVuyACblA9DjxsVjNDOFEtLELr4Fl2w2+K2TDrCh3UfmkxG0YbkU2pH+Dbnl6R0WyHb0kAbulv2/alhiXq0ettZR00aSE+6JUrtE1i0yHM4gk6LoFEbh3SSClCGQ6SgsytNfTx2y2pJJJymTpuJnELk4VXaaethtmJNIaf22FlFQMCI30axv6Cxs03X4Sh10Zks8m3B3nMGNpwbbU3jIvmE7g92djguTYf6t4fbgC6bPkYISDRjVmJ6ypy5JEiuYJHr6D4AkTrL/ZE2rVUQkX1LZBS25CRqQZRwK2t4y5oFag0cdNMoeIK7QAxQNHH7jojsrOc6R9vpcQaRov9oS1wY4IgarUyHxcrrDwxgQNvQfRC43QWRJJR2odTbnSbELkeMu3FxGLwh4NBZKi8npcK7o5eD7y3VeppAZb94bZekS4Oareq7R3UyA7tW01Q0vQev2ex0U+6gzLZBzN8KUur2Bss91KYPvZuQAUsLcWHO6brY9mOPCixT+PdTkcI3Skf8dU9DA5P1bbLsZzbLzX7kHQaR2t1NujePUK/tEXt46CLvhBN6VOHH3lFqnMvI8cHyy6OFq8bmbSrNsezuALA+ZFbPUzda6mkHdRqRY874aJ25E31Oz7czOfHmooQMyin+tUVglLHvHMnvLmTEM6czBGeYoNg+PGaLK0etFJnKBbg6kTTC55SbbbDihU8nfUyoJO8peR+uCyni5ozC6V7bi9FtbvSF73bGOKb+gxjnlW9L45a3cUmwV73OmwslLdCU9QcpUTIIDk/BnUbY+OgiKj2Vs2UINX09qgT14HRpb+WT1tzUTPSLRK5tXbI9BzFk/QLdC62vUVhKcI+ragO+AuJ5DZIoPQS6U9x8CzK0ipoplRllclfxsr64SnfKtCRDtXV7PbUHKrppyEXiZfKMp4B3CTjNw+ZFoBujCE5obw9IzIUI5eTmCoUJJuHJFqq4lIMiKbaw+01ibrtW6rbCDi5Twdyb+2gr4AMtC9MFbaUrPKfCaI8aUxnlOSPJNLyHcswiZDU/NPhc+GktbxUZN6WGlg+37BCxJL5bmnqLofwZ3eZRlMgPvtawLM9hKuE9QxphFfBfRDb2izzasGnZCuqcJmN3lB/T4Gf5lfLCushrGVIVX8SkR5CGYyUeU32ifJIk/YTtjMpgUz/Utt525TphH57znE/wrQnfgzqd+RMPigPPJch2Aaz3QjS5mRydK7s9ZefE2BKHpuNb1JxItJb2dheZR4UF7VgXUYzxqGTvxIOGtFWp0qGoTtLhUT+FAb3re+VC7JZqe7CgLaz0Ih92pp5LOAkxis97WDjAulYynO/fiuMRnzKmYdPUY2oc5XtlvMnqzpxvKuHZHWQpJ9UPTG13nqmCopOVbjyDPqUpYgAKutWqRNpfD9tIOI9NjXth36fxESP4A7GOjh7mup+0W+Z40LvDwz2DgucUuT3PI8bzltzbJiRbWFaVbs4ZeqnLSBqr166VU/7WOPhWzLCGJ9HusISYJYnN3FKpSm+ru1VICC3ZeRCl4uVkZ5d7a5u3+C7ld3eyZHesOJHhG5+r+6J3Pe881Bjo2uDoXs1TBReWSoS85MLSPbnk25GL72b0OB+v1ryrRLf2+Hao1WM7ny6asdML8eFWU2EC5lkk54Kz0KaChc7Fl4M1INCRdYr9AzTtlVhPx7Pq7AGIkDdzd1SHDr3NA0xZuKghCrHgW9xt2qDtg0NpHCkaTycnr3gINz2d1KM03/KX9oiM1+QBldJ1ns+YoJ40ZuylNJ+XxzW6cYRTn/KLSZ3j1Uw5+767nZRzw9nhCtrJo4R6fCoEA90L9kx0R6+y95B4RtdGuLhq6hz8ZeF3QUoLqzhNjacUwpFxs0KJDowReZVqHJzjNOOk7I8Iz935akwNISd83+L72xJnoHHZ99QRN6RWxYU4cttGrmwK6a4K6+wbwbcsbSm9bqHiwHoQOsbQK1NJddXWcB40AaJIRjVnhnzaztjJWbawpPfdmZmu6iJeyWDI4FZUALCJQ9XJPNvHF9dWYRSz/MW4DCHr3a435I4oOxKH9xwCmztkuUvRTfeEbCUrOSsy4q7VD06k5B42HS/WmTmIKhKbVh0ZyMlCrpIloUMhXNetFF3V/EGDtmFKS+10DUU6OXcpZTDl8RLvBvPAMqcrg5JlK4fuHIaPZaHmHUNWnjR15iqWWhSsQuTGdWSfZOyByJErHvdEmzLG9MCmfb1NXUEXYLRf4Z5VDmqGSDjnm12xXcx0JUpLSgjQcKmzc50Pyu0mIMz1bBbEgYYSeHex/PscJ14YPALP5W4za9naUfYU26BXkaT2Oy80WsFETqNLCuYinIaWt5NTGRxaoSTkNltNbt+V3GkY0lbjJoZK6CUgZDxjq+gQXs3TSdraZyqSb9Nj3A5XxipVcrmWqh11oXCeOrLZw8nVH5JYiw5364LE2+q2v6c4L07p7YhoXCsE58EaeP8gM8tgyWiVIHHB1HcQH9mNUYhd4In8nVJh08P5R1+vo1jKN450ZND8mjIu6buGgwVLwvUEdvC6Yc3ZNvjetrKr0BRngvYbbnK69q7NB1axFs+/XJUSEdd5qGehIhshKw9jh9CTcMbd3EexBRUcvkqrRbpmU9/Zjt4XcFwjJ0kJLvCuy3On6hq7RzIMTjNO3O6sYWddseg6XDP3NLCaXPgmxTpcjuaH7UpwSytV+BnxJV5EpeIYTkSAhbK4NzSjv8wKoqajvZiu6bA7lrv6yL3Sbm0gmYTVLw9i3e+uEmfU9aDX4yEuKjGEQnY+90gwRCK8V3ZpjBkiwzon2tBWRS6x/coGFluEd+UwJweB3CrEgdLy6m7vDz1lb5FC9X00Spbh0Ey6fgPJNPmOb+hoATu34HCP4t6tz82+r7GCXXezNuqMXcgoFYmciRKe8OgfCmHdXW1UJuVg+fLdtUBzYymNlbSWwhAVETuaejjsugNWbcWDvdK0iHFwGLC2cDtMrmG0qbtskQY7plGYL4ywjfsjf/W7WiwD/HEhjEkNd0o2OJMUV/UdXTpQA6Db8VEzdsoDLNVvw85RBbPBafJ4LK7sBFlWfkq9xJMSxGBvWyqRg7gG+RbsQ7499KnKiah4C9S6iWyFx0t0VY9eSlK2vToyka47inbIdo2rMRor9qY3U46rTKbyWitipmS7Di6ty8C7tnA4thROjtQlVRmMyBKdsDnjqpx7r7Z463ReRAtSWDyeIS27COItqwAXSVXtCppMKiyOkzMV67BEt11VHudhLHgxqMtTvUP2FG8D/gHQDWbn/rqNVh5NyMtxO5RCr0/SQbdmuCbv15Zu8Au0nL17T2lHDz849G1f9LErLRl/y1WRmpNBGyq5qfLE5mRne5O0OOnms5GVWtFNo8sgs9jj0M1dCpaqnYPpSsduXkOnbdRyGtsZkeeuvrEMek+pa8BhonYWeZNELruAhoeOtFdJubcElWJX6wYYb3wQFWNXRPVi0QJJHXbrdXJ0uL9mxlmqtqwPssqB76S1bpksFgePGba8nBrj0POqdXQ8BCXQph8M5OBjawMYcP9w10zJQQHZlerW1pcKQ47HJXaMJLvISEGPOZrULunvqwYekNry+dxw58xe/cuRyhLznrrFYfVIpwvt1o52ROGXEHPX4VtK4ToWYx01m/W2dpcjh4rEvk6OukyW4x0CTfIxvvjngxOUAYygvu+dNULDPK3p7ha4P6WS9Nhu3cbmDml2OmsF2xP8ArItZVJPk3aNa+sCFUmtrBgUOfYkYlXGaWe1LWh0LyQ77xqr8qcprAylVhaAbseScqsGL8xqf8s6QvAVSsEZYx+RWF9BVGv4J2NOMqiZZWgv2IV68l0buYSUyLlbUEEvkJAydYWRt8qic8jpzKa0Gov32S2+E4qJZjBpd6BNjPbO3GPUDVFb6Edq17uINkd2WhttVGXZO1PlLO+hwrn1MtYzI72nLpiXO0zPsuw/P3z/4fPBruc3Bf/mWwHPQ0v/385OvR1zqkawaOkFzwNibeD4n15rffpbDf71/YfWS8D6b2e/nl/GeD889X7y68/np5+Dlrfj889DfM+ziG+na3snen6J8sPnUZ/PSb8un+eFwUVR418PrL2fyno/CP+6/YOST91eX+N4nVJDfnxq+Nv/AeSr84tgOgAA -->
