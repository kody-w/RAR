---
name: "rar-discreetrappers-powerpoint-generator"
description: "Generate professional PowerPoint presentations using Microsoft templates.\n\nTemplates available:\n- BaseTemplateBlue: Microsoft corporate template (recommended)\n- ZavaTemplate: Modern business template\n- BaseTemplateDynamics: Dynamics-style template\n\nActions:\n- create_presentation: Create multi-slide presentation\n- list_templates: List available templates and their layouts\n- list_layouts: List layouts for a specific template\n\nSlide types: title, section, content, two_column, comparison, quote, stats, pipeline, blank\n\nExample:\n{\n  \"action\": \"create_presentation\",\n  \"customer\": \"Contoso\",\n  \"template\": \"BaseTemplateBlue\",\n  \"output_filename\": \"my_presentation\",\n  \"slides\": [\n    {\"type\": \"title\", \"title\": \"My Presentation\", \"subtitle\": \"Subtitle here\"},\n    {\"type\": \"content\", \"title\": \"Key Points\", \"bullets\": [\"Point 1\", \"Point 2\"]},\n    {\"type\": \"comparison\", \"title\": \"Before vs After\", \"left_label\": \"Before\", \"right_label\": \"After\", \"left_items\": [\"Old way\"], \"right_items\": [\"New way\"]}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/powerpoint_generator_agent", "rar_sha256": "5a9fc79dfbf2038ba411e2789dc988713389b2219ff5ce721b02d684d88a23f5", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Bill Whalen", "tags": ["productivity", "powerpoint", "presentations", "templates", "microsoft"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/powerpoint_generator_agent`. The original RAPP
agent is preserved byte-for-byte in `powerpoint_generator_agent.py` and in the RCI capsule.

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

PowerPoint Generator Agent V2 - Template-Based Microsoft Design
Purpose: Generate professional PowerPoint presentations using Microsoft templates

Design principles:
- Template-based generation for consistent branding
- Supports multiple templates (BaseTemplateBlue, ZavaTemplate, etc.)
- Smart layout selection based on content type
- Proper placeholder population
- Fallback to programmatic generation if template not available

Templates supported:
- BaseTemplateBlue.pptx: Microsoft corporate template (113 layouts)
- ZavaTemplate.pptx: Modern business template (62 layouts)
- BaseTemplateDynamics.pptx: Dynamics-style template

Usage:
1. With template: action="create_presentation", template="BaseTemplateBlue", slides=[...]
2. Without template: action="create_presentation", slides=[...] (uses default styling)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "create_presentation",
        "list_templates",
        "list_layouts"
      ],
      "type": "string"
    },
    "customer": {
      "description": "Customer name - creates a subfolder in docs/ppt for this customer",
      "type": "string"
    },
    "output_filename": {
      "type": "string"
    },
    "slides": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "template": {
      "description": "Template name (BaseTemplateBlue, ZavaTemplate, BaseTemplateDynamics)",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `powerpoint_generator_agent.py` and embedded as the fenced Python below (sha256 5a9fc79dfbf2038b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `powerpoint_generator_agent.py` first:

```bash
python3 powerpoint_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 powerpoint_generator_agent.py   # or on stdin
python3 powerpoint_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PowerPoint Generator Agent V2 - Template-Based Microsoft Design
Purpose: Generate professional PowerPoint presentations using Microsoft templates

Design principles:
- Template-based generation for consistent branding
- Supports multiple templates (BaseTemplateBlue, ZavaTemplate, etc.)
- Smart layout selection based on content type
- Proper placeholder population
- Fallback to programmatic generation if template not available

Templates supported:
- BaseTemplateBlue.pptx: Microsoft corporate template (113 layouts)
- ZavaTemplate.pptx: Modern business template (62 layouts)
- BaseTemplateDynamics.pptx: Dynamics-style template

Usage:
1. With template: action="create_presentation", template="BaseTemplateBlue", slides=[...]
2. Without template: action="create_presentation", slides=[...] (uses default styling)
"""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/powerpoint_generator_agent",
    "version": "1.0.2",
    "display_name": "PowerPointGeneratorV2",
    "description": "Generates PowerPoint decks from slide specs with python-pptx, using Microsoft templates and smart layout selection.",
    "author": "Bill Whalen",
    "tags": ["productivity", "powerpoint", "presentations", "templates", "microsoft"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

# Import python-pptx
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
    from pptx.oxml.ns import nsmap
    PPTX_AVAILABLE = True
except ImportError as e:
    PPTX_AVAILABLE = False
    PPTX_IMPORT_ERROR = str(e)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PowerPointGeneratorAgentV2(BasicAgent):
    """
    Agent for generating professional presentations using Microsoft templates.
    """

    # Template configurations - maps template names to layout indexes
    TEMPLATE_CONFIGS = {
        "PowerpointTemplateBlue": {
            "file": "docs/ppt/ppt_templates/PowerpointTemplateBlue.pptx",
            "layouts": {
                "title": 2,  # "Title Slide"
                "title_photo": 0,  # "Title square photo"
                "section": 102,  # "Section Divider"
                "content": 9,  # "Title and Content"
                "two_column": 11,  # "Two Column Bullet text"
                "three_column": 15,  # "Three Column Bullet with Subtitles"
                "four_column": 16,  # "Four Column Bullet with Subtitles"
                "comparison": 11,  # "Two Column Bullet text"
                "quote": 64,  # "Quote slide 1b"
                "code": 94,  # "Developer Code Layout full page"
                "demo": 100,  # "Demo slide"
                "blank": 108,  # "Blank 12 Column"
                "closing": 111,  # "Closing logo slide"
                "title_only": 18,  # "Title Only"
            }
        },
        "BaseTemplateBlueV2": {
            "file": "docs/ppt/BaseTemplateBlueV2.pptx",
            "layouts": {
                "title": 2,  # "Title Slide"
                "title_photo": 0,  # "Title square photo"
                "section": 102,  # "Section Divider"
                "content": 9,  # "Title and Content"
                "two_column": 11,  # "Two Column Bullet text"
                "three_column": 15,  # "Three Column Bullet with Subtitles"
                "four_column": 16,  # "Four Column Bullet with Subtitles"
                "comparison": 11,  # "Two Column Bullet text"
                "quote": 64,  # "Quote slide 1b"
                "code": 94,  # "Developer Code Layout full page"
                "demo": 100,  # "Demo slide"
                "blank": 108,  # "Blank 12 Column"
                "closing": 111,  # "Closing logo slide"
                "title_only": 18,  # "Title Only"
            }
        },
        "BaseTemplateBlue": {
            "file": "docs/ppt/BaseTemplateBlue.pptx",
            "layouts": {
                "title": 2,  # "Title Slide"
                "title_photo": 0,  # "Title square photo"
                "section": 102,  # "Section Divider"
                "content": 9,  # "Title and Content"
                "two_column": 11,  # "Two Column Bullet text"
                "three_column": 15,  # "Three Column Bullet with Subtitles"
                "four_column": 16,  # "Four Column Bullet with Subtitles"
                "comparison": 11,  # "Two Column Bullet text"
                "quote": 64,  # "Quote slide 1b"
                "code": 94,  # "Developer Code Layout full page"
                "demo": 100,  # "Demo slide"
                "blank": 108,  # "Blank 12 Column"
                "closing": 111,  # "Closing logo slide"
                "title_only": 18,  # "Title Only"
            }
        },
        "ZavaTemplate": {
            "file": "docs/ppt/ZavaTemplate.pptx",
            "layouts": {
                "title": 0,  # "Title 1"
                "title_photo": 10,  # "Title Photo 1"
                "section": 14,  # "Section Header 1"
                "content": 24,  # "Content 1"
                "two_column": 41,  # "Two Content"
                "comparison": 43,  # "Comparison"
                "quote": 59,  # "Quote"
                "statement": 56,  # "Statement"
                "number": 53,  # "Number Large"
                "conclusion": 48,  # "Conclusion 1"
                "blank": 45,  # "Blank"
                "title_only": 44,  # "Title Only"
                "agenda": 20,  # "Agenda"
            }
        },
        "BaseTemplateDynamics": {
            "file": "docs/ppt/BaseTemplateDynamics.pptx",
            "layouts": {
                "title": 0,
                "content": 1,
                "blank": 6,
            }
        }
    }

    # Microsoft color palette
    COLORS = {
        "ms_blue": "0078D4",
        "ms_dark_blue": "004578",
        "ms_light_blue": "50E6FF",
        "ms_green": "107C10",
        "ms_red": "D13438",
        "ms_orange": "FF8C00",
        "ms_purple": "5C2D91",
        "black": "000000",
        "dark_gray": "323130",
        "medium_gray": "605E5C",
        "light_gray": "A19F9D",
        "white": "FFFFFF",
    }

    # Segoe UI fonts (Microsoft standard)
    FONTS = {
        "title": {"name": "Segoe UI Semibold", "size": 44, "bold": False},
        "subtitle": {"name": "Segoe UI", "size": 24, "bold": False},
        "heading": {"name": "Segoe UI Semibold", "size": 28, "bold": False},
        "body": {"name": "Segoe UI", "size": 18, "bold": False},
        "caption": {"name": "Segoe UI", "size": 14, "bold": False},
    }

    def __init__(self):
        self.name = 'PowerPointGeneratorV2'
        self.metadata = {
            "name": self.name,
            "description": """Generate professional PowerPoint presentations using Microsoft templates.

Templates available:
- BaseTemplateBlue: Microsoft corporate template (recommended)
- ZavaTemplate: Modern business template
- BaseTemplateDynamics: Dynamics-style template

Actions:
- create_presentation: Create multi-slide presentation
- list_templates: List available templates and their layouts
- list_layouts: List layouts for a specific template

Slide types: title, section, content, two_column, comparison, quote, stats, pipeline, blank

Example:
{
  "action": "create_presentation",
  "customer": "Contoso",
  "template": "BaseTemplateBlue",
  "output_filename": "my_presentation",
  "slides": [
    {"type": "title", "title": "My Presentation", "subtitle": "Subtitle here"},
    {"type": "content", "title": "Key Points", "bullets": ["Point 1", "Point 2"]},
    {"type": "comparison", "title": "Before vs After", "left_label": "Before", "right_label": "After", "left_items": ["Old way"], "right_items": ["New way"]}
  ]
}""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["create_presentation", "list_templates", "list_layouts"]
                    },
                    "customer": {
                        "type": "string",
                        "description": "Customer name - creates a subfolder in docs/ppt for this customer"
                    },
                    "template": {
                        "type": "string",
                        "description": "Template name (BaseTemplateBlue, ZavaTemplate, BaseTemplateDynamics)"
                    },
                    "slides": {
                        "type": "array",
                        "items": {"type": "object"}
                    },
                    "output_filename": {"type": "string"},
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)

        try:
            self.storage = get_storage_manager()
        except Exception as e:
            logger.warning(f"Storage not available: {e}")
            self.storage = None

        # Find base path for templates
        self.base_path = self._find_base_path()

    def _find_base_path(self) -> str:
        """Find the base path for the RAPP project."""
        # Try common locations
        possible_paths = [
            os.getcwd(),
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "c:/Users/billwhalen/OneDrive - Microsoft/Documents/GitHub/RAPP/CommunityRAPP-main",
        ]
        for path in possible_paths:
            if os.path.exists(os.path.join(path, "docs", "ppt")):
                return path
        return os.getcwd()

    def perform(self, **kwargs) -> str:
        """Execute the requested action."""
        if not PPTX_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": f"python-pptx library not available: {PPTX_IMPORT_ERROR}",
                "suggestion": "Install with: pip install python-pptx"
            })

        action = kwargs.get('action', 'create_presentation')

        try:
            if action == 'list_templates':
                return self._list_templates()
            elif action == 'list_layouts':
                return self._list_layouts(kwargs.get('template', 'BaseTemplateBlue'))
            elif action == 'create_presentation':
                return self._create_presentation(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}",
                    "available_actions": ["create_presentation", "list_templates", "list_layouts"]
                })
        except Exception as e:
            logger.error(f"PowerPoint generation error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })

    def _list_templates(self) -> str:
        """List available templates."""
        templates = {}
        for name, config in self.TEMPLATE_CONFIGS.items():
            # Normalize path separators for Windows
            template_rel_path = config["file"].replace("/", os.sep)
            template_path = os.path.join(self.base_path, template_rel_path)
            templates[name] = {
                "file": config["file"],
                "exists": os.path.exists(template_path),
                "layouts": list(config["layouts"].keys())
            }
        return json.dumps({"status": "success", "templates": templates}, indent=2)

    def _list_layouts(self, template_name: str) -> str:
        """List layouts for a specific template."""
        if template_name not in self.TEMPLATE_CONFIGS:
            return json.dumps({
                "status": "error",
                "error": f"Unknown template: {template_name}",
                "available": list(self.TEMPLATE_CONFIGS.keys())
            })

        config = self.TEMPLATE_CONFIGS[template_name]
        # Normalize path separators for Windows
        template_rel_path = config["file"].replace("/", os.sep)
        template_path = os.path.join(self.base_path, template_rel_path)

        if not os.path.exists(template_path):
            return json.dumps({
                "status": "error",
                "error": f"Template file not found: {template_path}"
            })

        # Handle .potx files by converting to .pptx in temp location
        import tempfile
        import shutil
        
        actual_path = template_path
        if template_path.lower().endswith('.potx'):
            temp_dir = tempfile.gettempdir()
            temp_pptx = os.path.join(temp_dir, f"temp_template_{template_name}.pptx")
            shutil.copy2(template_path, temp_pptx)
            actual_path = temp_pptx

        prs = Presentation(actual_path)
        layouts = []
        for i, layout in enumerate(prs.slide_layouts):
            layouts.append({"index": i, "name": layout.name})

        return json.dumps({
            "status": "success",
            "template": template_name,
            "layout_count": len(layouts),
            "mapped_layouts": config["layouts"],
            "all_layouts": layouts
        }, indent=2)

    def _hex_to_rgb(self, hex_color: str) -> RGBColor:
        """Convert hex color to RGBColor."""
        hex_color = hex_color.lstrip('#')
        return RGBColor(
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16)
        )

    def _create_presentation(self, **kwargs) -> str:
        """Create a presentation using templates."""
        template_name = kwargs.get('template', 'BaseTemplateBlue')
        slides = kwargs.get('slides', [])
        output_filename = kwargs.get('output_filename', 'presentation')

        if not slides:
            return json.dumps({
                "status": "error",
                "error": "No slides provided. Use 'slides' parameter with array of slide configs."
            })

        # Load template or create blank presentation
        prs = self._load_template(template_name)
        if prs is None:
            return json.dumps({
                "status": "error",
                "error": f"Could not load template: {template_name}"
            })

        config = self.TEMPLATE_CONFIGS.get(template_name, {})
        layout_map = config.get("layouts", {})

        # Process each slide
        for i, slide_config in enumerate(slides):
            slide_type = slide_config.get('type', 'content')
            self._add_slide(prs, slide_config, slide_type, layout_map, i + 1)

        return self._save_presentation(prs, output_filename, kwargs)

    def _remove_placeholder_shapes(self, slide) -> None:
        """Remove placeholder shapes from a slide to avoid template artifacts."""
        shapes_to_remove = []
        for shape in slide.shapes:
            # Check if it's a placeholder shape
            if hasattr(shape, 'placeholder_format') and shape.placeholder_format is not None:
                shapes_to_remove.append(shape)
        
        # Remove the placeholder shapes
        for shape in shapes_to_remove:
            sp = shape._element
            sp.getparent().remove(sp)

    def _load_template(self, template_name: str) -> Optional[Presentation]:
        """Load a PowerPoint template."""
        if template_name not in self.TEMPLATE_CONFIGS:
            logger.warning(f"Unknown template {template_name}, using blank presentation")
            prs = Presentation()
            prs.slide_width = Inches(13.333)
            prs.slide_height = Inches(7.5)
            return prs

        config = self.TEMPLATE_CONFIGS[template_name]
        # Normalize path separators for Windows
        template_rel_path = config["file"].replace("/", os.sep)
        template_path = os.path.join(self.base_path, template_rel_path)

        if not os.path.exists(template_path):
            logger.warning(f"Template file not found: {template_path}")
            prs = Presentation()
            prs.slide_width = Inches(13.333)
            prs.slide_height = Inches(7.5)
            return prs

        try:
            # Handle .potx files by converting to .pptx in temp location
            import tempfile
            import shutil
            
            if template_path.lower().endswith('.potx'):
                # Copy .potx to temp .pptx file (python-pptx doesn't support .potx directly)
                temp_dir = tempfile.gettempdir()
                temp_pptx = os.path.join(temp_dir, f"temp_template_{template_name}.pptx")
                shutil.copy2(template_path, temp_pptx)
                template_path = temp_pptx
            
            prs = Presentation(template_path)
            # Remove any existing slides from template
            while len(prs.slides) > 0:
                rId = prs.slides._sldIdLst[0].rId
                prs.part.drop_rel(rId)
                del prs.slides._sldIdLst[0]
            return prs
        except Exception as e:
            logger.error(f"Error loading template: {e}")
            return None

    def _add_slide(self, prs: Presentation, config: Dict, slide_type: str, 
                   layout_map: Dict, page_num: int) -> None:
        """Add a slide based on type and configuration."""
        # Get the appropriate layout
        layout_idx = layout_map.get(slide_type, layout_map.get('content', 0))

        # Ensure layout index is valid
        if layout_idx >= len(prs.slide_layouts):
            layout_idx = 0

        layout = prs.slide_layouts[layout_idx]
        slide = prs.slides.add_slide(layout)

        # Populate the slide based on type
        if slide_type == 'title':
            self._populate_title_slide(slide, config)
        elif slide_type == 'section':
            self._populate_section_slide(slide, config)
        elif slide_type == 'content':
            self._populate_content_slide(slide, config)
        elif slide_type in ['two_column', 'comparison']:
            self._populate_comparison_slide(slide, config)
        elif slide_type == 'quote':
            self._populate_quote_slide(slide, config)
        elif slide_type == 'stats':
            self._populate_stats_slide(slide, prs, config)
        elif slide_type == 'pipeline':
            self._populate_pipeline_slide(slide, prs, config)
        elif slide_type == 'image':
            self._populate_image_slide(slide, config)
        elif slide_type == 'title_image':
            self._populate_title_image_slide(slide, config)
        elif slide_type == 'value_cards':
            self._populate_value_cards_slide(slide, config)
        elif slide_type == 'before_after':
            self._populate_before_after_slide(slide, config)
        elif slide_type == 'agent_cards':
            self._populate_agent_cards_slide(slide, config)
        elif slide_type == 'metric_boxes':
            self._populate_metric_boxes_slide(slide, config)
        elif slide_type == 'process_flow':
            self._populate_process_flow_slide(slide, config)
        else:
            # Default content slide
            self._populate_content_slide(slide, config)

    def _populate_image_slide(self, slide, config: Dict) -> None:
        """Populate a slide with an image."""
        title = config.get('title', '')
        image_path = config.get('image_path', '')
        caption = config.get('caption', '')
        
        # Remove non-title placeholders to avoid artifacts
        shapes_to_remove = []
        title_shape = None
        for shape in slide.shapes:
            if hasattr(shape, 'placeholder_format') and shape.placeholder_format is not None:
                if shape.placeholder_format.type == 1:  # Title placeholder
                    title_shape = shape
                else:
                    shapes_to_remove.append(shape)
        
        for shape in shapes_to_remove:
            sp = shape._element
            sp.getparent().remove(sp)
        
        # Set title
        if title_shape and title:
            title_shape.text_frame.paragraphs[0].text = title
            self._style_text(title_shape.text_frame.paragraphs[0], "heading")
        elif title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Add image if path exists
        if image_path and os.path.exists(image_path):
            # Calculate centered position
            img_width = Inches(10)
            img_left = Inches(1.667)  # Center on 13.333" wide slide
            img_top = Inches(1.3)
            img_height = Inches(5.5)
            
            slide.shapes.add_picture(image_path, img_left, img_top, width=img_width)
        
        # Add caption if provided
        if caption:
            caption_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.9), Inches(12.333), Inches(0.4))
            tf = caption_box.text_frame
            p = tf.paragraphs[0]
            p.text = caption
            p.font.size = Pt(12)
            p.font.italic = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.CENTER

    def _populate_title_image_slide(self, slide, config: Dict) -> None:
        """Populate a slide with title, content bullets, and an image side by side."""
        title = config.get('title', '')
        content = config.get('content', [])
        image_path = config.get('image_path', '')
        
        # Set title
        title_set = False
        for shape in slide.shapes:
            if shape.has_text_frame and shape.placeholder_format:
                if shape.placeholder_format.type == 1:
                    shape.text_frame.paragraphs[0].text = title
                    self._style_text(shape.text_frame.paragraphs[0], "heading")
                    title_set = True
                    break
        
        if not title_set and title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Add content on left side
        if content:
            self._add_bullet_textbox(slide, content, 0.5, 1.3, 5.5, 5.5)
        
        # Add image on right side
        if image_path and os.path.exists(image_path):
            img_left = Inches(6.5)
            img_top = Inches(1.3)
            img_width = Inches(6.3)
            slide.shapes.add_picture(image_path, img_left, img_top, width=img_width)

    def _populate_title_slide(self, slide, config: Dict) -> None:
        """Populate a title slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        subtitle = config.get('subtitle', '')

        # Title slides have dark background - use white text
        self._add_title_textbox(slide, title, 0.5, 2.5, 12.333, color="#FFFFFF")
        if subtitle:
            self._add_subtitle_textbox(slide, subtitle, 0.5, 3.5, 12.333, color="#CCCCCC")

    def _populate_section_slide(self, slide, config: Dict) -> None:
        """Populate a section divider slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')

        # Section slides have dark background - use white text
        self._add_title_textbox(slide, title, 0.5, 3.0, 12.333, size=36, color="#FFFFFF")

    def _populate_content_slide(self, slide, config: Dict) -> None:
        """Populate a content slide with bullets."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        bullets = config.get('bullets', config.get('content', []))

        # Add title and content as textboxes (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.5, 12.333, size=28)
        if bullets:
            self._add_bullet_textbox(slide, bullets, 0.5, 1.5, 12.333, 5.5)

    def _populate_comparison_slide(self, slide, config: Dict) -> None:
        """Populate a comparison/two-column slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        
        # Support both old format (left_label/right_label) and new format (left/right objects)
        left_data = config.get('left', {})
        right_data = config.get('right', {})
        
        if isinstance(left_data, dict):
            # New format with nested title/content
            left_label = left_data.get('title', config.get('left_label', 'Left'))
            left_items = left_data.get('content', config.get('left_items', []))
        else:
            left_label = config.get('left_label', 'Before')
            left_items = config.get('left_items', [])
            
        if isinstance(right_data, dict):
            right_label = right_data.get('title', config.get('right_label', 'Right'))
            right_items = right_data.get('content', config.get('right_items', []))
        else:
            right_label = config.get('right_label', 'After')
            right_items = config.get('right_items', [])

        # Add title as textbox (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)

        # Add comparison content via text boxes
        self._add_two_column_content(slide, left_label, right_label, left_items, right_items)

    def _populate_quote_slide(self, slide, config: Dict) -> None:
        """Populate a quote slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        quote = config.get('quote', '')
        author = config.get('author', config.get('quote_author', ''))

        # Add quote box directly (placeholders removed)
        self._add_quote_box(slide, quote, author)

    def _populate_stats_slide(self, slide, prs, config: Dict) -> None:
        """Populate a stats/metrics slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        stats = config.get('stats', config.get('metrics', []))

        # Add title as textbox (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)

        # Add stats boxes
        self._add_stats_boxes(slide, prs, stats)

    def _populate_pipeline_slide(self, slide, prs, config: Dict) -> None:
        """Populate a pipeline/process slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        steps = config.get('steps', [])

        # Add title as textbox (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)

        # Add pipeline visualization
        self._add_pipeline_boxes(slide, prs, steps)

    def _populate_value_cards_slide(self, slide, config: Dict) -> None:
        """Populate a slide with value proposition cards (like the HTML demo)."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        cards = config.get('cards', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Calculate card positions (up to 4 cards per row)
        num_cards = len(cards)
        card_width = 3.8
        card_height = 2.8
        gap = 0.3
        
        if num_cards <= 3:
            start_x = (13.333 - (num_cards * card_width + (num_cards - 1) * gap)) / 2
            cards_per_row = num_cards
        else:
            start_x = (13.333 - (3 * card_width + 2 * gap)) / 2
            cards_per_row = 3
        
        for i, card in enumerate(cards):
            row = i // cards_per_row
            col = i % cards_per_row
            x = start_x + col * (card_width + gap)
            y = 1.3 + row * (card_height + 0.3)
            
            self._add_value_card(slide, card, x, y, card_width, card_height)

    def _add_value_card(self, slide, card: Dict, x: float, y: float, 
                        width: float, height: float) -> None:
        """Add a single value card with icon, title, description, and before/after."""
        icon = card.get('icon', '📊')
        title = card.get('title', '')
        description = card.get('description', '')
        before = card.get('before', '')
        after = card.get('after', '')
        
        # Card background
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(255, 255, 255)
        shape.line.color.rgb = self._hex_to_rgb(self.COLORS["light_gray"])
        shape.line.width = Pt(1)
        shape.shadow.inherit = False
        
        # Icon
        icon_box = slide.shapes.add_textbox(Inches(x), Inches(y + 0.15), Inches(width), Inches(0.5))
        tf = icon_box.text_frame
        p = tf.paragraphs[0]
        p.text = icon
        p.font.size = Pt(32)
        p.alignment = PP_ALIGN.CENTER
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.65), Inches(width - 0.2), Inches(0.4))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 1.05), Inches(width - 0.2), Inches(0.6))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(10)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.CENTER
        
        # Before/After if provided
        if before and after:
            ba_y = y + height - 0.6
            
            # Before (red, strikethrough)
            before_box = slide.shapes.add_textbox(Inches(x + 0.15), Inches(ba_y), Inches(1.2), Inches(0.35))
            tf = before_box.text_frame
            p = tf.paragraphs[0]
            p.text = before
            p.font.size = Pt(11)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_red"])
            p.alignment = PP_ALIGN.CENTER
            
            # Arrow
            arrow_box = slide.shapes.add_textbox(Inches(x + 1.4), Inches(ba_y), Inches(0.6), Inches(0.35))
            tf = arrow_box.text_frame
            p = tf.paragraphs[0]
            p.text = "→"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_green"])
            p.alignment = PP_ALIGN.CENTER
            
            # After (green)
            after_box = slide.shapes.add_textbox(Inches(x + 2.0), Inches(ba_y), Inches(1.5), Inches(0.35))
            tf = after_box.text_frame
            p = tf.paragraphs[0]
            p.text = after
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_green"])
            p.alignment = PP_ALIGN.CENTER

    def _populate_before_after_slide(self, slide, config: Dict) -> None:
        """Populate a slide showing before/after transformation."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        items = config.get('items', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Create table-like layout with before/after
        y_start = 1.3
        row_height = 0.7
        
        # Headers
        self._add_ba_header(slide, "Challenge", 0.5, y_start, 4.5, "ms_red")
        self._add_ba_header(slide, "", 5.1, y_start, 1.0, "ms_green")  # Arrow column
        self._add_ba_header(slide, "Solution", 6.2, y_start, 6.5, "ms_green")
        
        for i, item in enumerate(items):
            row_y = y_start + 0.5 + (i * row_height)
            before = item.get('before', '')
            after = item.get('after', '')
            
            # Before text
            self._add_ba_item(slide, before, 0.5, row_y, 4.5, "dark_gray")
            
            # Arrow
            arrow = slide.shapes.add_textbox(Inches(5.1), Inches(row_y), Inches(1.0), Inches(0.5))
            tf = arrow.text_frame
            p = tf.paragraphs[0]
            p.text = "→"
            p.font.size = Pt(24)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_green"])
            p.alignment = PP_ALIGN.CENTER
            
            # After text
            self._add_ba_item(slide, after, 6.2, row_y, 6.5, "ms_green", bold=True)

    def _add_ba_header(self, slide, text: str, x: float, y: float, 
                       width: float, color: str) -> None:
        """Add a before/after header."""
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.45))
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS[color])

    def _add_ba_item(self, slide, text: str, x: float, y: float, 
                     width: float, color: str, bold: bool = False) -> None:
        """Add a before/after item."""
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.5))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"• {text}"
        p.font.size = Pt(14)
        p.font.bold = bold
        p.font.color.rgb = self._hex_to_rgb(self.COLORS[color])

    def _populate_agent_cards_slide(self, slide, config: Dict) -> None:
        """Populate a slide with agent cards (colored boxes like HTML demo)."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        agents = config.get('agents', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Layout agents in a grid
        num_agents = len(agents)
        cols = min(3, num_agents)
        card_width = 3.9
        card_height = 2.0
        gap = 0.2
        
        start_x = (13.333 - (cols * card_width + (cols - 1) * gap)) / 2
        
        for i, agent in enumerate(agents):
            row = i // cols
            col = i % cols
            x = start_x + col * (card_width + gap)
            y = 1.3 + row * (card_height + 0.2)
            
            self._add_agent_card(slide, agent, x, y, card_width, card_height)

    def _add_agent_card(self, slide, agent: Dict, x: float, y: float, 
                        width: float, height: float) -> None:
        """Add a single agent card with gradient-like appearance."""
        name = agent.get('name', '')
        level = agent.get('level', 1)
        description = agent.get('description', '')
        competitors = agent.get('competitors', [])
        
        # Color based on level
        if level == 0:
            bg_color = "#11998e"  # Green for orchestrator
        elif level == 2:
            bg_color = "#667eea"  # Purple for synthesizer
        else:
            bg_color = "#0078d4"  # Blue for Level 1
        
        # Card background
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = self._hex_to_rgb(bg_color)
        shape.line.fill.background()
        
        # Level badge
        badge = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.1), Inches(1.0), Inches(0.25))
        tf = badge.text_frame
        p = tf.paragraphs[0]
        p.text = f"LEVEL {level}"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        
        # Agent name
        name_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.4), Inches(width - 0.2), Inches(0.4))
        tf = name_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.85), Inches(width - 0.2), Inches(0.6))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(10)
            p.font.color.rgb = RGBColor(230, 230, 230)
        
        # Competitors (if any)
        if competitors:
            comp_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + height - 0.4), Inches(width - 0.2), Inches(0.3))
            tf = comp_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = " | ".join(competitors[:4])  # Max 4 competitors
            p.font.size = Pt(8)
            p.font.color.rgb = RGBColor(200, 200, 200)

    def _populate_metric_boxes_slide(self, slide, config: Dict) -> None:
        """Populate a slide with large metric/stat boxes."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        metrics = config.get('metrics', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Calculate positions
        num_metrics = len(metrics)
        box_width = 3.5
        box_height = 2.5
        gap = 0.4
        
        total_width = num_metrics * box_width + (num_metrics - 1) * gap
        start_x = (13.333 - total_width) / 2
        
        for i, metric in enumerate(metrics):
            x = start_x + i * (box_width + gap)
            self._add_metric_box(slide, metric, x, 2.0, box_width, box_height)

    def _add_metric_box(self, slide, metric: Dict, x: float, y: float,
                        width: float, height: float) -> None:
        """Add a single metric box with large number and label."""
        value = metric.get('value', '')
        label = metric.get('label', '')
        description = metric.get('description', '')
        color = metric.get('color', 'ms_blue')
        
        # Box background
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS.get(color, self.COLORS["ms_blue"]))
        shape.line.fill.background()
        
        # Large value
        val_box = slide.shapes.add_textbox(Inches(x), Inches(y + 0.3), Inches(width), Inches(1.0))
        tf = val_box.text_frame
        p = tf.paragraphs[0]
        p.text = str(value)
        p.font.size = Pt(48)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        
        # Label
        label_box = slide.shapes.add_textbox(Inches(x), Inches(y + 1.4), Inches(width), Inches(0.5))
        tf = label_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = label
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 1.9), Inches(width - 0.2), Inches(0.5))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(10)
            p.font.color.rgb = RGBColor(220, 220, 220)
            p.alignment = PP_ALIGN.CENTER

    def _populate_process_flow_slide(self, slide, config: Dict) -> None:
        """Populate a slide with a horizontal process flow."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        steps = config.get('steps', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        num_steps = len(steps)
        if num_steps == 0:
            return
            
        # Calculate positions
        step_width = 2.0
        arrow_width = 0.8
        total_width = num_steps * step_width + (num_steps - 1) * arrow_width
        start_x = (13.333 - total_width) / 2
        
        for i, step in enumerate(steps):
            x = start_x + i * (step_width + arrow_width)
            self._add_process_step(slide, step, x, 2.5, step_width, i + 1)
            
            # Add arrow between steps
            if i < num_steps - 1:
                arrow_x = x + step_width + 0.1
                self._add_flow_arrow(slide, arrow_x, 3.5, arrow_width - 0.2)

    def _add_process_step(self, slide, step: Dict, x: float, y: float,
                          width: float, number: int) -> None:
        """Add a single process step with number circle and description."""
        title = step.get('title', step) if isinstance(step, dict) else step
        description = step.get('description', '') if isinstance(step, dict) else ''
        duration = step.get('duration', '') if isinstance(step, dict) else ''
        
        # Number circle
        circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(x + width/2 - 0.3), Inches(y), Inches(0.6), Inches(0.6)
        )
        circle.fill.solid()
        circle.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        circle.line.fill.background()
        
        # Number text
        num_box = slide.shapes.add_textbox(Inches(x + width/2 - 0.3), Inches(y + 0.08), Inches(0.6), Inches(0.5))
        tf = num_box.text_frame
        p = tf.paragraphs[0]
        p.text = str(number)
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(x), Inches(y + 0.8), Inches(width), Inches(0.6))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x), Inches(y + 1.4), Inches(width), Inches(0.8))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(9)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.CENTER
        
        # Duration badge
        if duration:
            dur_box = slide.shapes.add_textbox(Inches(x + width/2 - 0.4), Inches(y + 2.2), Inches(0.8), Inches(0.3))
            tf = dur_box.text_frame
            p = tf.paragraphs[0]
            p.text = duration
            p.font.size = Pt(9)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_orange"])
            p.alignment = PP_ALIGN.CENTER

    def _add_flow_arrow(self, slide, x: float, y: float, width: float) -> None:
        """Add a flow arrow between process steps."""
        arrow = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.5))
        tf = arrow.text_frame
        p = tf.paragraphs[0]
        p.text = "→"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER

    def _populate_bullets(self, text_frame, bullets: List[str]) -> None:
        """Populate a text frame with bullet points."""
        # Clear existing paragraphs except first
        while len(text_frame.paragraphs) > 1:
            p = text_frame.paragraphs[-1]._p
            text_frame._txBody.remove(p)

        for i, bullet in enumerate(bullets):
            if i == 0:
                p = text_frame.paragraphs[0]
            else:
                p = text_frame.paragraphs[-1]._p.addnext(text_frame.paragraphs[0]._p.makeelement('{http://schemas.openxmlformats.org/drawingml/2006/main}p', {}))
                p = text_frame.paragraphs[-1]

            p.text = bullet
            self._style_text(p, "body")

    def _style_text(self, paragraph, style: str) -> None:
        """Apply font styling to a paragraph."""
        font_config = self.FONTS.get(style, self.FONTS["body"])
        if paragraph.runs:
            for run in paragraph.runs:
                run.font.name = font_config["name"]
                run.font.size = Pt(font_config["size"])
        else:
            paragraph.font.name = font_config["name"]
            paragraph.font.size = Pt(font_config["size"])

    # ==================== HELPER METHODS FOR CONTENT ====================

    def _add_title_textbox(self, slide, text: str, x: float, y: float, width: float, 
                            size: int = 44, color: str = None) -> None:
        """Add a title text box."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(1))
        tf = textbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = self.FONTS["title"]["name"]
        p.font.size = Pt(size)
        # Use provided color or default to dark_gray
        text_color = color if color else self.COLORS["dark_gray"]
        p.font.color.rgb = self._hex_to_rgb(text_color)

    def _add_subtitle_textbox(self, slide, text: str, x: float, y: float, width: float,
                              color: str = None) -> None:
        """Add a subtitle text box."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.6))
        tf = textbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = self.FONTS["subtitle"]["name"]
        p.font.size = Pt(self.FONTS["subtitle"]["size"])
        # Use provided color or default to medium_gray
        text_color = color if color else self.COLORS["medium_gray"]
        p.font.color.rgb = self._hex_to_rgb(text_color)

    def _add_bullet_textbox(self, slide, bullets: List[str], x: float, y: float, 
                            width: float, height: float, color: str = None) -> None:
        """Add a text box with bullet points."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(height))
        tf = textbox.text_frame
        tf.word_wrap = True
        # Use provided color or default to dark_gray
        text_color = color if color else self.COLORS["dark_gray"]

        for i, bullet in enumerate(bullets):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = f"• {bullet}"
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(self.FONTS["body"]["size"])
            p.font.color.rgb = self._hex_to_rgb(text_color)
            p.space_after = Pt(12)

    def _add_two_column_content(self, slide, left_title: str, right_title: str,
                                left_items: List[str], right_items: List[str]) -> None:
        """Add two-column content with titles and bullet points."""
        # Left column title
        left_header = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(5.8), Inches(0.5))
        tf = left_header.text_frame
        p = tf.paragraphs[0]
        p.text = left_title
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        
        # Right column title
        right_header = slide.shapes.add_textbox(Inches(6.8), Inches(1.3), Inches(5.8), Inches(0.5))
        tf = right_header.text_frame
        p = tf.paragraphs[0]
        p.text = right_title
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        
        # Left column bullets
        if left_items:
            left_content = slide.shapes.add_textbox(Inches(0.5), Inches(1.9), Inches(5.8), Inches(4.5))
            tf = left_content.text_frame
            tf.word_wrap = True
            for i, item in enumerate(left_items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {item}"
                p.font.name = self.FONTS["body"]["name"]
                p.font.size = Pt(16)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
                p.space_after = Pt(10)
        
        # Right column bullets
        if right_items:
            right_content = slide.shapes.add_textbox(Inches(6.8), Inches(1.9), Inches(5.8), Inches(4.5))
            tf = right_content.text_frame
            tf.word_wrap = True
            for i, item in enumerate(right_items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {item}"
                p.font.name = self.FONTS["body"]["name"]
                p.font.size = Pt(16)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
                p.space_after = Pt(10)

    def _add_comparison_content(self, slide, left_label: str, right_label: str,
                                left_items: List[str], right_items: List[str]) -> None:
        """Add comparison content to a slide."""
        # Left column header
        self._add_column_header(slide, left_label, 0.5, 1.8, 5.5, "ms_red")
        # Right column header
        self._add_column_header(slide, right_label, 7.0, 1.8, 5.5, "ms_blue")

        # Left items
        y_start = 2.5
        for i, item in enumerate(left_items):
            self._add_comparison_item(slide, item, 0.5, y_start + (i * 0.7), 5.5, "ms_red")

        # Right items
        for i, item in enumerate(right_items):
            self._add_comparison_item(slide, item, 7.0, y_start + (i * 0.7), 5.5, "ms_blue")

        # Arrow in the middle
        self._add_arrow(slide, 6.0, 3.5)

    def _add_column_header(self, slide, text: str, x: float, y: float, 
                           width: float, color: str) -> None:
        """Add a column header."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.5))
        tf = textbox.text_frame
        p = tf.paragraphs[0]
        p.text = text.upper()
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS[color])

    def _add_comparison_item(self, slide, text: str, x: float, y: float,
                             width: float, color: str) -> None:
        """Add a comparison item with bullet."""
        # Bullet circle
        bullet = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(x), Inches(y + 0.1),
            Inches(0.15), Inches(0.15)
        )
        bullet.fill.solid()
        bullet.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS[color])
        bullet.line.fill.background()

        # Text
        textbox = slide.shapes.add_textbox(Inches(x + 0.25), Inches(y), Inches(width - 0.25), Inches(0.6))
        tf = textbox.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(16)
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])

    def _add_arrow(self, slide, x: float, y: float) -> None:
        """Add an arrow shape."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(1), Inches(0.5))
        tf = textbox.text_frame
        p = tf.paragraphs[0]
        p.text = "→"
        p.font.size = Pt(36)
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER

    def _add_quote_box(self, slide, quote: str, author: str) -> None:
        """Add a quote box."""
        # Quote background
        box = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(1), Inches(2),
            Inches(11.333), Inches(3)
        )
        box.fill.solid()
        box.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        box.line.fill.background()

        # Quote text
        textbox = slide.shapes.add_textbox(Inches(1.5), Inches(2.5), Inches(10.333), Inches(2))
        tf = textbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f'"{quote}"'
        p.font.name = "Segoe UI Light"
        p.font.size = Pt(28)
        p.font.italic = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["white"])
        p.alignment = PP_ALIGN.CENTER

        # Author
        if author:
            author_box = slide.shapes.add_textbox(Inches(1), Inches(5.2), Inches(11.333), Inches(0.5))
            tf = author_box.text_frame
            p = tf.paragraphs[0]
            p.text = f"— {author}"
            p.font.name = self.FONTS["caption"]["name"]
            p.font.size = Pt(16)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.RIGHT

    def _add_stats_boxes(self, slide, prs, stats: List[Dict]) -> None:
        """Add statistics/metric boxes."""
        num_stats = len(stats)
        if num_stats == 0:
            return

        box_width = min(3.5, 11.0 / num_stats)
        spacing = (12.333 - (box_width * num_stats)) / (num_stats + 1)
        y_start = 2.0

        for i, stat in enumerate(stats):
            x = 0.5 + spacing + (i * (box_width + spacing))
            value = stat.get('value', '')
            label = stat.get('label', '')
            sublabel = stat.get('sublabel', '')

            # Box background
            box = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(x), Inches(y_start),
                Inches(box_width), Inches(2.5)
            )
            box.fill.solid()
            box.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["white"])
            box.line.color.rgb = self._hex_to_rgb(self.COLORS["light_gray"])
            box.line.width = Pt(1)

            # Value
            value_box = slide.shapes.add_textbox(
                Inches(x), Inches(y_start + 0.4),
                Inches(box_width), Inches(0.8)
            )
            tf = value_box.text_frame
            p = tf.paragraphs[0]
            p.text = str(value)
            p.font.name = "Segoe UI Light"
            p.font.size = Pt(48)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
            p.alignment = PP_ALIGN.CENTER

            # Label
            label_box = slide.shapes.add_textbox(
                Inches(x), Inches(y_start + 1.4),
                Inches(box_width), Inches(0.5)
            )
            tf = label_box.text_frame
            p = tf.paragraphs[0]
            p.text = label
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
            p.alignment = PP_ALIGN.CENTER

            # Sublabel
            if sublabel:
                sub_box = slide.shapes.add_textbox(
                    Inches(x), Inches(y_start + 1.9),
                    Inches(box_width), Inches(0.5)
                )
                tf = sub_box.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = sublabel
                p.font.name = self.FONTS["caption"]["name"]
                p.font.size = Pt(12)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
                p.alignment = PP_ALIGN.CENTER

    def _add_pipeline_boxes(self, slide, prs, steps: List[Dict]) -> None:
        """Add pipeline/process flow boxes."""
        num_steps = len(steps)
        if num_steps == 0:
            return

        # Calculate dimensions
        total_width = 12.333
        step_width = (total_width - 1) / num_steps
        y_start = 2.5

        for i, step in enumerate(steps):
            x = 0.5 + (i * step_width)
            label = step.get('label', f'Step {i+1}')
            description = step.get('description', '')
            number = step.get('number', i + 1)

            # Circle with number
            circle = slide.shapes.add_shape(
                MSO_SHAPE.OVAL,
                Inches(x + (step_width/2) - 0.3), Inches(y_start),
                Inches(0.6), Inches(0.6)
            )
            circle.fill.solid()
            circle.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
            circle.line.fill.background()

            # Number in circle
            tf = circle.text_frame
            p = tf.paragraphs[0]
            p.text = str(number)
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["white"])
            p.alignment = PP_ALIGN.CENTER

            # Label below circle
            label_box = slide.shapes.add_textbox(
                Inches(x), Inches(y_start + 0.8),
                Inches(step_width), Inches(0.5)
            )
            tf = label_box.text_frame
            p = tf.paragraphs[0]
            p.text = label
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
            p.alignment = PP_ALIGN.CENTER

            # Description
            if description:
                desc_box = slide.shapes.add_textbox(
                    Inches(x), Inches(y_start + 1.3),
                    Inches(step_width), Inches(0.5)
                )
                tf = desc_box.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = description
                p.font.name = self.FONTS["caption"]["name"]
                p.font.size = Pt(12)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
                p.alignment = PP_ALIGN.CENTER

            # Arrow to next step
            if i < num_steps - 1:
                arrow_x = x + step_width - 0.3
                arrow_box = slide.shapes.add_textbox(
                    Inches(arrow_x), Inches(y_start + 0.1),
                    Inches(0.5), Inches(0.5)
                )
                tf = arrow_box.text_frame
                p = tf.paragraphs[0]
                p.text = "→"
                p.font.size = Pt(24)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["light_gray"])
                p.alignment = PP_ALIGN.CENTER

    def _save_presentation(self, prs: Presentation, filename: str, kwargs: Dict) -> str:
        """Save the presentation to file."""
        if not filename.endswith('.pptx'):
            filename = f"{filename}.pptx"

        # Get customer name for subfolder organization
        customer = kwargs.get('customer', '')
        
        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'ppt'))
        if customer:
            # Sanitize customer name for folder (lowercase, replace spaces with underscores)
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir
            
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        local_path = os.path.join(output_dir, filename)

        try:
            prs.save(local_path)
        except Exception as e:
            # Fallback to temp directory
            import tempfile
            local_path = os.path.join(tempfile.gettempdir(), filename)
            prs.save(local_path)

        result = {
            "status": "success",
            "filename": filename,
            "local_path": os.path.abspath(local_path),
            "customer": customer if customer else "none",
            "customer_folder": output_dir,
            "template_used": kwargs.get('template', 'BaseTemplateBlue')
        }

        return json.dumps(result, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
