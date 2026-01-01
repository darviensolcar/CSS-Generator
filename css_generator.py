#!/usr/bin/env python3
"""
Advanced CSS Theme Generator
Generates fully responsive, professional CSS themes with light and dark variants.
Each generation produces unique designs with different color schemes, typography, and styles.
"""

import random
import colorsys
from datetime import datetime
import os


class CSSThemeGenerator:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.design_name = self.generate_design_name()
        self.color_scheme = self.generate_color_scheme()
        self.typography = self.generate_typography()
        self.spacing = self.generate_spacing()
        self.borders = self.generate_borders()
        self.shadows = self.generate_shadows()
        self.animations = self.generate_animations()
        
    def generate_design_name(self):
        """Generate a creative, unique name for the design"""
        # Adjectives that describe design qualities
        adjectives = [
            'Modern', 'Elegant', 'Bold', 'Minimal', 'Classic', 'Vibrant',
            'Sleek', 'Dynamic', 'Fresh', 'Serene', 'Cosmic', 'Urban',
            'Nordic', 'Tropical', 'Azure', 'Crimson', 'Golden', 'Silver',
            'Midnight', 'Dawn', 'Sunset', 'Ocean', 'Forest', 'Mountain',
            'Desert', 'Arctic', 'Neon', 'Pastel', 'Royal', 'Electric',
            'Smooth', 'Sharp', 'Soft', 'Crisp', 'Warm', 'Cool',
            'Luxe', 'Neo', 'Retro', 'Futuristic', 'Organic', 'Digital',
            'Gradient', 'Matte', 'Glossy', 'Velvet', 'Crystal', 'Marble'
        ]
        
        # Nouns that represent design concepts
        nouns = [
            'Wave', 'Bloom', 'Pulse', 'Breeze', 'Echo', 'Horizon',
            'Aurora', 'Nebula', 'Zenith', 'Flux', 'Aura', 'Prism',
            'Cascade', 'Ember', 'Frost', 'Glow', 'Haze', 'Spark',
            'Storm', 'Tide', 'Vibe', 'Whisper', 'Zephyr', 'Canvas',
            'Dream', 'Edge', 'Flow', 'Grace', 'Haven', 'Mirage',
            'Oasis', 'Peak', 'Quest', 'Rhythm', 'Shade', 'Swift',
            'Terrain', 'Unity', 'Vision', 'Zen', 'Apex', 'Bliss',
            'Clarity', 'Depth', 'Essence', 'Fusion', 'Haven', 'Impulse'
        ]
        
        # Sometimes add a secondary descriptor
        secondary = [
            'Pro', 'Plus', 'Elite', 'Prime', 'Core', 'Max',
            'Studio', 'Lab', 'Works', 'Design', 'UI', 'System',
            'Kit', 'Suite', 'Collection', 'Palette'
        ]
        
        # Generate name with different patterns
        pattern = random.choice([1, 2, 3, 4])
        
        if pattern == 1:
            # Adjective + Noun (e.g., "Modern Wave")
            name = f"{random.choice(adjectives)} {random.choice(nouns)}"
        elif pattern == 2:
            # Adjective + Noun + Secondary (e.g., "Bold Pulse Pro")
            name = f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(secondary)}"
        elif pattern == 3:
            # Noun + Secondary (e.g., "Aurora Studio")
            name = f"{random.choice(nouns)} {random.choice(secondary)}"
        else:
            # Just Noun (e.g., "Nebula")
            name = random.choice(nouns)
        
        return name
        
    def generate_color_scheme(self):
        """Generate a harmonious color scheme"""
        # Generate base hue
        base_hue = random.randint(0, 360)
        
        # Generate complementary and analogous colors
        colors = {
            'primary_hue': base_hue,
            'secondary_hue': (base_hue + random.randint(150, 210)) % 360,
            'accent_hue': (base_hue + random.randint(30, 60)) % 360,
            'neutral_hue': random.randint(200, 240),
        }
        
        return colors
    
    def hsl_to_hex(self, h, s, l):
        """Convert HSL to HEX color"""
        r, g, b = colorsys.hls_to_rgb(h/360, l/100, s/100)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def generate_typography(self):
        """Generate typography settings"""
        font_stacks = [
            "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            "'Poppins', system-ui, -apple-system, sans-serif",
            "'Montserrat', 'Helvetica Neue', Arial, sans-serif",
            "'Raleway', 'Trebuchet MS', sans-serif",
            "'Work Sans', 'Segoe UI', Tahoma, sans-serif",
            "'DM Sans', system-ui, sans-serif",
        ]
        
        heading_fonts = [
            "'Playfair Display', Georgia, serif",
            "'Merriweather', Georgia, serif",
            "'Libre Baskerville', serif",
            "'Lora', Georgia, serif",
            "'Space Grotesk', monospace",
        ]
        
        return {
            'base_font': random.choice(font_stacks),
            'heading_font': random.choice(heading_fonts) if random.random() > 0.4 else random.choice(font_stacks),
            'code_font': "'Fira Code', 'Courier New', monospace",
            'base_size': random.choice(['16px', '17px', '18px']),
            'scale_ratio': random.choice([1.125, 1.2, 1.25, 1.333, 1.414, 1.5, 1.618]),
            'line_height': random.uniform(1.5, 1.75),
            'letter_spacing': random.uniform(-0.02, 0.02),
        }
    
    def generate_spacing(self):
        """Generate spacing scale"""
        base = random.choice([4, 6, 8])
        return {
            'base': base,
            'scale': [base * i for i in [0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 20, 24]]
        }
    
    def generate_borders(self):
        """Generate border styles"""
        return {
            'radius_style': random.choice(['minimal', 'moderate', 'rounded', 'pill']),
            'width': random.choice(['1px', '2px', '3px']),
            'style': random.choice(['solid', 'solid', 'solid', 'dashed']),
        }
    
    def generate_shadows(self):
        """Generate shadow styles"""
        intensity = random.choice(['subtle', 'moderate', 'strong'])
        return {
            'intensity': intensity,
            'colored': random.random() > 0.6,
        }
    
    def generate_animations(self):
        """Generate animation preferences"""
        return {
            'duration': random.choice(['0.2s', '0.3s', '0.4s']),
            'easing': random.choice([
                'ease-in-out',
                'cubic-bezier(0.4, 0, 0.2, 1)',
                'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
                'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
            ]),
        }
    
    def get_border_radius(self):
        """Get border radius values based on style"""
        styles = {
            'minimal': {'sm': '2px', 'md': '4px', 'lg': '6px', 'xl': '8px', 'full': '9999px'},
            'moderate': {'sm': '4px', 'md': '8px', 'lg': '12px', 'xl': '16px', 'full': '9999px'},
            'rounded': {'sm': '8px', 'md': '12px', 'lg': '16px', 'xl': '24px', 'full': '9999px'},
            'pill': {'sm': '12px', 'md': '16px', 'lg': '24px', 'xl': '32px', 'full': '9999px'},
        }
        return styles[self.borders['radius_style']]
    
    def get_shadows(self, theme='light'):
        """Generate shadow values"""
        if self.shadows['intensity'] == 'subtle':
            multiplier = 0.5
        elif self.shadows['intensity'] == 'moderate':
            multiplier = 1
        else:
            multiplier = 1.5
        
        if theme == 'light':
            base_color = 'rgba(0, 0, 0'
        else:
            base_color = 'rgba(0, 0, 0'
        
        return {
            'xs': f'0 1px 2px 0 {base_color}, {0.05 * multiplier})',
            'sm': f'0 1px 3px 0 {base_color}, {0.1 * multiplier}), 0 1px 2px 0 {base_color}, {0.06 * multiplier})',
            'md': f'0 4px 6px -1px {base_color}, {0.1 * multiplier}), 0 2px 4px -1px {base_color}, {0.06 * multiplier})',
            'lg': f'0 10px 15px -3px {base_color}, {0.1 * multiplier}), 0 4px 6px -2px {base_color}, {0.05 * multiplier})',
            'xl': f'0 20px 25px -5px {base_color}, {0.1 * multiplier}), 0 10px 10px -5px {base_color}, {0.04 * multiplier})',
            '2xl': f'0 25px 50px -12px {base_color}, {0.25 * multiplier})',
        }
    
    def generate_theme_colors(self, is_dark=False):
        """Generate color palette for light or dark theme"""
        colors = {}
        
        # Primary colors
        primary_sat = random.randint(60, 90)
        for i, shade in enumerate([50, 100, 200, 300, 400, 500, 600, 700, 800, 900]):
            lightness = 95 - (i * 8) if not is_dark else 15 + (i * 8)
            colors[f'primary-{shade}'] = self.hsl_to_hex(
                self.color_scheme['primary_hue'],
                primary_sat,
                lightness
            )
        
        # Secondary colors
        secondary_sat = random.randint(50, 80)
        for i, shade in enumerate([50, 100, 200, 300, 400, 500, 600, 700, 800, 900]):
            lightness = 95 - (i * 8) if not is_dark else 15 + (i * 8)
            colors[f'secondary-{shade}'] = self.hsl_to_hex(
                self.color_scheme['secondary_hue'],
                secondary_sat,
                lightness
            )
        
        # Accent colors
        accent_sat = random.randint(70, 100)
        for i, shade in enumerate([50, 100, 200, 300, 400, 500, 600, 700, 800, 900]):
            lightness = 95 - (i * 8) if not is_dark else 15 + (i * 8)
            colors[f'accent-{shade}'] = self.hsl_to_hex(
                self.color_scheme['accent_hue'],
                accent_sat,
                lightness
            )
        
        # Neutral/Gray colors
        neutral_sat = random.randint(5, 20)
        for i, shade in enumerate([50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]):
            if not is_dark:
                lightness = 98 - (i * 8.5)
            else:
                lightness = 10 + (i * 8)
            colors[f'gray-{shade}'] = self.hsl_to_hex(
                self.color_scheme['neutral_hue'],
                neutral_sat,
                lightness
            )
        
        # Semantic colors
        colors['success-500'] = self.hsl_to_hex(145, 65, 45 if not is_dark else 55)
        colors['warning-500'] = self.hsl_to_hex(38, 92, 50 if not is_dark else 60)
        colors['error-500'] = self.hsl_to_hex(0, 72, 51 if not is_dark else 61)
        colors['info-500'] = self.hsl_to_hex(210, 75, 55 if not is_dark else 65)
        
        # Background and text colors
        if is_dark:
            colors['bg-primary'] = colors['gray-900']
            colors['bg-secondary'] = colors['gray-800']
            colors['bg-tertiary'] = colors['gray-700']
            colors['text-primary'] = colors['gray-100']
            colors['text-secondary'] = colors['gray-300']
            colors['text-tertiary'] = colors['gray-400']
        else:
            colors['bg-primary'] = colors['gray-50']
            colors['bg-secondary'] = '#ffffff'
            colors['bg-tertiary'] = colors['gray-100']
            colors['text-primary'] = colors['gray-900']
            colors['text-secondary'] = colors['gray-700']
            colors['text-tertiary'] = colors['gray-600']
        
        return colors
    
    def generate_css_variables(self, theme='light'):
        """Generate CSS custom properties"""
        is_dark = theme == 'dark'
        colors = self.generate_theme_colors(is_dark)
        radius = self.get_border_radius()
        shadows = self.get_shadows(theme)
        spacing = self.spacing['scale']
        
        css = "  /* Color Palette */\n"
        for name, value in colors.items():
            css += f"  --color-{name}: {value};\n"
        
        css += "\n  /* Typography */\n"
        css += f"  --font-base: {self.typography['base_font']};\n"
        css += f"  --font-heading: {self.typography['heading_font']};\n"
        css += f"  --font-code: {self.typography['code_font']};\n"
        css += f"  --font-size-base: {self.typography['base_size']};\n"
        css += f"  --line-height-base: {self.typography['line_height']};\n"
        css += f"  --letter-spacing-base: {self.typography['letter_spacing']}em;\n"
        
        # Font sizes using scale ratio
        ratio = self.typography['scale_ratio']
        css += f"  --font-size-xs: {1 / (ratio ** 2):.3f}rem;\n"
        css += f"  --font-size-sm: {1 / ratio:.3f}rem;\n"
        css += f"  --font-size-base: 1rem;\n"
        css += f"  --font-size-lg: {ratio:.3f}rem;\n"
        css += f"  --font-size-xl: {ratio ** 2:.3f}rem;\n"
        css += f"  --font-size-2xl: {ratio ** 3:.3f}rem;\n"
        css += f"  --font-size-3xl: {ratio ** 4:.3f}rem;\n"
        css += f"  --font-size-4xl: {ratio ** 5:.3f}rem;\n"
        
        css += "\n  /* Spacing */\n"
        for i, value in enumerate(spacing):
            css += f"  --space-{i}: {value}px;\n"
        
        css += "\n  /* Border Radius */\n"
        for name, value in radius.items():
            css += f"  --radius-{name}: {value};\n"
        
        css += "\n  /* Shadows */\n"
        for name, value in shadows.items():
            css += f"  --shadow-{name}: {value};\n"
        
        css += "\n  /* Borders */\n"
        css += f"  --border-width: {self.borders['width']};\n"
        css += f"  --border-style: {self.borders['style']};\n"
        css += f"  --border-color: var(--color-gray-300);\n"
        
        css += "\n  /* Animations */\n"
        css += f"  --transition-duration: {self.animations['duration']};\n"
        css += f"  --transition-easing: {self.animations['easing']};\n"
        
        css += "\n  /* Z-index layers */\n"
        css += "  --z-dropdown: 1000;\n"
        css += "  --z-sticky: 1020;\n"
        css += "  --z-fixed: 1030;\n"
        css += "  --z-modal-backdrop: 1040;\n"
        css += "  --z-modal: 1050;\n"
        css += "  --z-popover: 1060;\n"
        css += "  --z-tooltip: 1070;\n"
        
        return css
    
    def generate_reset_and_base(self):
        """Generate CSS reset and base styles"""
        return """/* ========================================
   CSS Reset & Base Styles
   ======================================== */

/* Box sizing reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Remove default margins and paddings */
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

/* HTML5 display-role reset */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
  display: block;
}

/* Base HTML setup */
html {
  font-size: var(--font-size-base);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-base);
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
  letter-spacing: var(--letter-spacing-base);
  color: var(--color-text-primary);
  background-color: var(--color-bg-primary);
  min-height: 100vh;
  overflow-x: hidden;
}

/* Lists */
ol, ul {
  list-style: none;
}

/* Links */
a {
  color: inherit;
  text-decoration: none;
  transition: color var(--transition-duration) var(--transition-easing);
}

a:hover {
  color: var(--color-primary-600);
}

/* Images and media */
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
  height: auto;
}

/* Form elements */
input, button, textarea, select {
  font: inherit;
  color: inherit;
}

button {
  cursor: pointer;
  background: none;
  border: none;
}

/* Remove button focus outline in favor of custom styles */
button:focus-visible,
a:focus-visible,
input:focus-visible,
textarea:focus-visible,
select:focus-visible {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}

/* Prevent text overflow */
p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
  hyphens: auto;
}

/* Accessibility */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Smooth scrolling for internal links */
@media (prefers-reduced-motion: no-preference) {
  html {
    scroll-behavior: smooth;
  }
}

/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
"""
    
    def generate_typography_styles(self):
        """Generate typography styles"""
        return """
/* ========================================
   Typography
   ======================================== */

/* Headings */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  font-weight: 700;
  line-height: 1.2;
  color: var(--color-text-primary);
  margin-bottom: var(--space-4);
}

h1 {
  font-size: var(--font-size-4xl);
  letter-spacing: -0.02em;
}

h2 {
  font-size: var(--font-size-3xl);
  letter-spacing: -0.01em;
}

h3 {
  font-size: var(--font-size-2xl);
}

h4 {
  font-size: var(--font-size-xl);
}

h5 {
  font-size: var(--font-size-lg);
}

h6 {
  font-size: var(--font-size-base);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Paragraphs */
p {
  margin-bottom: var(--space-4);
  color: var(--color-text-secondary);
}

p:last-child {
  margin-bottom: 0;
}

/* Text utilities */
.text-xs { font-size: var(--font-size-xs); }
.text-sm { font-size: var(--font-size-sm); }
.text-base { font-size: var(--font-size-base); }
.text-lg { font-size: var(--font-size-lg); }
.text-xl { font-size: var(--font-size-xl); }
.text-2xl { font-size: var(--font-size-2xl); }
.text-3xl { font-size: var(--font-size-3xl); }
.text-4xl { font-size: var(--font-size-4xl); }

.font-light { font-weight: 300; }
.font-normal { font-weight: 400; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.font-extrabold { font-weight: 800; }

.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

.uppercase { text-transform: uppercase; }
.lowercase { text-transform: lowercase; }
.capitalize { text-transform: capitalize; }

.italic { font-style: italic; }
.underline { text-decoration: underline; }
.line-through { text-decoration: line-through; }

/* Code and pre */
code, pre {
  font-family: var(--font-code);
  font-size: 0.9em;
}

code {
  background-color: var(--color-gray-100);
  padding: 0.2em 0.4em;
  border-radius: var(--radius-sm);
  color: var(--color-text-primary);
}

pre {
  background-color: var(--color-gray-900);
  color: var(--color-gray-100);
  padding: var(--space-5);
  border-radius: var(--radius-md);
  overflow-x: auto;
  margin-bottom: var(--space-4);
}

pre code {
  background: none;
  padding: 0;
  color: inherit;
}

/* Blockquotes */
blockquote {
  border-left: 4px solid var(--color-primary-500);
  padding-left: var(--space-5);
  margin: var(--space-6) 0;
  font-style: italic;
  color: var(--color-text-secondary);
}

/* Links in content */
.content a {
  color: var(--color-primary-600);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 2px;
  transition: all var(--transition-duration) var(--transition-easing);
}

.content a:hover {
  color: var(--color-primary-700);
  text-decoration-thickness: 2px;
}

/* Lists in content */
.content ul,
.content ol {
  margin-bottom: var(--space-4);
  padding-left: var(--space-6);
}

.content ul {
  list-style: disc;
}

.content ol {
  list-style: decimal;
}

.content li {
  margin-bottom: var(--space-2);
  color: var(--color-text-secondary);
}

/* Horizontal rule */
hr {
  border: none;
  border-top: var(--border-width) var(--border-style) var(--border-color);
  margin: var(--space-8) 0;
}

/* Text color utilities */
.text-primary { color: var(--color-text-primary); }
.text-secondary { color: var(--color-text-secondary); }
.text-tertiary { color: var(--color-text-tertiary); }
.text-success { color: var(--color-success-500); }
.text-warning { color: var(--color-warning-500); }
.text-error { color: var(--color-error-500); }
.text-info { color: var(--color-info-500); }

/* Responsive typography */
@media (max-width: 768px) {
  h1 { font-size: var(--font-size-3xl); }
  h2 { font-size: var(--font-size-2xl); }
  h3 { font-size: var(--font-size-xl); }
  h4 { font-size: var(--font-size-lg); }
}

@media (max-width: 480px) {
  h1 { font-size: var(--font-size-2xl); }
  h2 { font-size: var(--font-size-xl); }
  h3 { font-size: var(--font-size-lg); }
}
"""
    
    def generate_layout_styles(self):
        """Generate layout and container styles"""
        return """
/* ========================================
   Layout & Containers
   ======================================== */

/* Container */
.container {
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

.container-fluid {
  width: 100%;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

.container-sm {
  max-width: 640px;
}

.container-md {
  max-width: 768px;
}

.container-lg {
  max-width: 1024px;
}

.container-xl {
  max-width: 1280px;
}

/* Grid system */
.grid {
  display: grid;
  gap: var(--space-4);
}

.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
.grid-cols-12 { grid-template-columns: repeat(12, minmax(0, 1fr)); }

.col-span-1 { grid-column: span 1 / span 1; }
.col-span-2 { grid-column: span 2 / span 2; }
.col-span-3 { grid-column: span 3 / span 3; }
.col-span-4 { grid-column: span 4 / span 4; }
.col-span-6 { grid-column: span 6 / span 6; }
.col-span-12 { grid-column: span 12 / span 12; }
.col-span-full { grid-column: 1 / -1; }

.gap-0 { gap: 0; }
.gap-1 { gap: var(--space-1); }
.gap-2 { gap: var(--space-2); }
.gap-3 { gap: var(--space-3); }
.gap-4 { gap: var(--space-4); }
.gap-6 { gap: var(--space-6); }
.gap-8 { gap: var(--space-8); }

/* Flexbox */
.flex {
  display: flex;
}

.inline-flex {
  display: inline-flex;
}

.flex-row { flex-direction: row; }
.flex-col { flex-direction: column; }
.flex-row-reverse { flex-direction: row-reverse; }
.flex-col-reverse { flex-direction: column-reverse; }

.flex-wrap { flex-wrap: wrap; }
.flex-nowrap { flex-wrap: nowrap; }

.items-start { align-items: flex-start; }
.items-center { align-items: center; }
.items-end { align-items: flex-end; }
.items-stretch { align-items: stretch; }
.items-baseline { align-items: baseline; }

.justify-start { justify-content: flex-start; }
.justify-center { justify-content: center; }
.justify-end { justify-content: flex-end; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }
.justify-evenly { justify-content: space-evenly; }

.flex-1 { flex: 1 1 0%; }
.flex-auto { flex: 1 1 auto; }
.flex-initial { flex: 0 1 auto; }
.flex-none { flex: none; }

.grow { flex-grow: 1; }
.grow-0 { flex-grow: 0; }
.shrink { flex-shrink: 1; }
.shrink-0 { flex-shrink: 0; }

/* Display utilities */
.block { display: block; }
.inline-block { display: inline-block; }
.inline { display: inline; }
.hidden { display: none; }

/* Position */
.static { position: static; }
.fixed { position: fixed; }
.absolute { position: absolute; }
.relative { position: relative; }
.sticky { position: sticky; }

/* Overflow */
.overflow-auto { overflow: auto; }
.overflow-hidden { overflow: hidden; }
.overflow-visible { overflow: visible; }
.overflow-scroll { overflow: scroll; }
.overflow-x-auto { overflow-x: auto; }
.overflow-y-auto { overflow-y: auto; }

/* Width & Height */
.w-full { width: 100%; }
.w-screen { width: 100vw; }
.w-auto { width: auto; }
.w-1-2 { width: 50%; }
.w-1-3 { width: 33.333333%; }
.w-2-3 { width: 66.666667%; }
.w-1-4 { width: 25%; }
.w-3-4 { width: 75%; }

.h-full { height: 100%; }
.h-screen { height: 100vh; }
.h-auto { height: auto; }

.min-h-screen { min-height: 100vh; }
.min-w-full { min-width: 100%; }

.max-w-xs { max-width: 20rem; }
.max-w-sm { max-width: 24rem; }
.max-w-md { max-width: 28rem; }
.max-w-lg { max-width: 32rem; }
.max-w-xl { max-width: 36rem; }
.max-w-2xl { max-width: 42rem; }
.max-w-full { max-width: 100%; }

/* Spacing utilities */
.m-0 { margin: 0; }
.m-auto { margin: auto; }
.mx-auto { margin-left: auto; margin-right: auto; }
.my-auto { margin-top: auto; margin-bottom: auto; }

.p-0 { padding: 0; }

/* Generate spacing utilities */
""" + self._generate_spacing_utilities() + """

/* Responsive grid */
@media (max-width: 1024px) {
  .lg\\:grid-cols-3 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .lg\\:grid-cols-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .lg\\:grid-cols-6 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

@media (max-width: 768px) {
  .md\\:grid-cols-2,
  .md\\:grid-cols-3,
  .md\\:grid-cols-4 { 
    grid-template-columns: repeat(1, minmax(0, 1fr)); 
  }
  
  .md\\:col-span-full {
    grid-column: 1 / -1;
  }
  
  .md\\:flex-col {
    flex-direction: column;
  }
}

@media (max-width: 480px) {
  .container {
    padding-left: var(--space-3);
    padding-right: var(--space-3);
  }
  
  .sm\\:hidden {
    display: none;
  }
  
  .sm\\:block {
    display: block;
  }
}
"""
    
    def _generate_spacing_utilities(self):
        """Generate margin and padding utilities"""
        css = ""
        for i in range(len(self.spacing['scale'])):
            value = f"var(--space-{i})"
            css += f".m-{i} {{ margin: {value}; }}\n"
            css += f".mt-{i} {{ margin-top: {value}; }}\n"
            css += f".mr-{i} {{ margin-right: {value}; }}\n"
            css += f".mb-{i} {{ margin-bottom: {value}; }}\n"
            css += f".ml-{i} {{ margin-left: {value}; }}\n"
            css += f".mx-{i} {{ margin-left: {value}; margin-right: {value}; }}\n"
            css += f".my-{i} {{ margin-top: {value}; margin-bottom: {value}; }}\n"
            
            css += f".p-{i} {{ padding: {value}; }}\n"
            css += f".pt-{i} {{ padding-top: {value}; }}\n"
            css += f".pr-{i} {{ padding-right: {value}; }}\n"
            css += f".pb-{i} {{ padding-bottom: {value}; }}\n"
            css += f".pl-{i} {{ padding-left: {value}; }}\n"
            css += f".px-{i} {{ padding-left: {value}; padding-right: {value}; }}\n"
            css += f".py-{i} {{ padding-top: {value}; padding-bottom: {value}; }}\n"
            css += "\n"
        return css
    
    def generate_component_styles(self):
        """Generate component styles"""
        return """
/* ========================================
   Components
   ======================================== */

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-3) var(--space-6);
  font-size: var(--font-size-base);
  font-weight: 500;
  line-height: 1.5;
  text-align: center;
  text-decoration: none;
  white-space: nowrap;
  border: var(--border-width) var(--border-style) transparent;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--transition-duration) var(--transition-easing);
  user-select: none;
  gap: var(--space-2);
}

.btn:focus-visible {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-primary {
  background-color: var(--color-primary-600);
  color: white;
  border-color: var(--color-primary-600);
}

.btn-primary:hover:not(:disabled) {
  background-color: var(--color-primary-700);
  border-color: var(--color-primary-700);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-primary:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}

.btn-secondary {
  background-color: var(--color-secondary-600);
  color: white;
  border-color: var(--color-secondary-600);
}

.btn-secondary:hover:not(:disabled) {
  background-color: var(--color-secondary-700);
  border-color: var(--color-secondary-700);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-outline {
  background-color: transparent;
  color: var(--color-primary-600);
  border-color: var(--color-primary-600);
}

.btn-outline:hover:not(:disabled) {
  background-color: var(--color-primary-50);
  border-color: var(--color-primary-700);
  color: var(--color-primary-700);
}

.btn-ghost {
  background-color: transparent;
  color: var(--color-text-primary);
  border-color: transparent;
}

.btn-ghost:hover:not(:disabled) {
  background-color: var(--color-gray-100);
}

.btn-sm {
  padding: var(--space-2) var(--space-4);
  font-size: var(--font-size-sm);
}

.btn-lg {
  padding: var(--space-4) var(--space-8);
  font-size: var(--font-size-lg);
}

.btn-block {
  display: flex;
  width: 100%;
}

/* Cards */
.card {
  background-color: var(--color-bg-secondary);
  border: var(--border-width) var(--border-style) var(--border-color);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-duration) var(--transition-easing);
}

.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.card-header {
  margin-bottom: var(--space-4);
  padding-bottom: var(--space-4);
  border-bottom: var(--border-width) var(--border-style) var(--border-color);
}

.card-title {
  font-size: var(--font-size-xl);
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.card-body {
  margin-bottom: var(--space-4);
}

.card-footer {
  margin-top: var(--space-4);
  padding-top: var(--space-4);
  border-top: var(--border-width) var(--border-style) var(--border-color);
}

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  font-size: var(--font-size-xs);
  font-weight: 600;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  border-radius: var(--radius-full);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge-primary {
  background-color: var(--color-primary-100);
  color: var(--color-primary-700);
}

.badge-secondary {
  background-color: var(--color-secondary-100);
  color: var(--color-secondary-700);
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fed7aa;
  color: #92400e;
}

.badge-error {
  background-color: #fee2e2;
  color: #991b1b;
}

/* Alerts */
.alert {
  padding: var(--space-4) var(--space-5);
  border-radius: var(--radius-md);
  border: var(--border-width) var(--border-style);
  margin-bottom: var(--space-4);
}

.alert-success {
  background-color: #d1fae5;
  border-color: #6ee7b7;
  color: #065f46;
}

.alert-warning {
  background-color: #fed7aa;
  border-color: #fbbf24;
  color: #92400e;
}

.alert-error {
  background-color: #fee2e2;
  border-color: #fca5a5;
  color: #991b1b;
}

.alert-info {
  background-color: #dbeafe;
  border-color: #93c5fd;
  color: #1e40af;
}

/* Forms */
.form-group {
  margin-bottom: var(--space-5);
}

.form-label {
  display: block;
  font-size: var(--font-size-sm);
  font-weight: 500;
  margin-bottom: var(--space-2);
  color: var(--color-text-primary);
}

.form-input,
.form-textarea,
.form-select {
  display: block;
  width: 100%;
  padding: var(--space-3) var(--space-4);
  font-size: var(--font-size-base);
  line-height: 1.5;
  color: var(--color-text-primary);
  background-color: var(--color-bg-secondary);
  background-clip: padding-box;
  border: var(--border-width) var(--border-style) var(--border-color);
  border-radius: var(--radius-md);
  transition: all var(--transition-duration) var(--transition-easing);
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
  border-color: var(--color-primary-500);
  outline: 0;
  box-shadow: 0 0 0 3px var(--color-primary-100);
}

.form-input:disabled,
.form-textarea:disabled,
.form-select:disabled {
  background-color: var(--color-gray-100);
  opacity: 0.6;
  cursor: not-allowed;
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

.form-check {
  display: flex;
  align-items: center;
  margin-bottom: var(--space-2);
}

.form-check-input {
  width: 1.25rem;
  height: 1.25rem;
  margin-right: var(--space-3);
  cursor: pointer;
}

.form-help {
  display: block;
  margin-top: var(--space-2);
  font-size: var(--font-size-sm);
  color: var(--color-text-tertiary);
}

.form-error {
  display: block;
  margin-top: var(--space-2);
  font-size: var(--font-size-sm);
  color: var(--color-error-500);
}

/* Navigation */
.nav {
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
  gap: var(--space-2);
}

.nav-link {
  display: block;
  padding: var(--space-3) var(--space-4);
  color: var(--color-text-secondary);
  text-decoration: none;
  border-radius: var(--radius-md);
  transition: all var(--transition-duration) var(--transition-easing);
}

.nav-link:hover {
  color: var(--color-primary-600);
  background-color: var(--color-gray-100);
}

.nav-link.active {
  color: var(--color-primary-600);
  background-color: var(--color-primary-100);
  font-weight: 500;
}

/* Navbar */
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  background-color: var(--color-bg-secondary);
  border-bottom: var(--border-width) var(--border-style) var(--border-color);
  box-shadow: var(--shadow-sm);
}

.navbar-brand {
  font-size: var(--font-size-xl);
  font-weight: 700;
  color: var(--color-text-primary);
  text-decoration: none;
}

.navbar-nav {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  list-style: none;
}

/* Tables */
.table {
  width: 100%;
  margin-bottom: var(--space-5);
  border-collapse: collapse;
}

.table thead th {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  font-weight: 600;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 2px solid var(--border-color);
  background-color: var(--color-bg-tertiary);
}

.table tbody td {
  padding: var(--space-4);
  border-bottom: var(--border-width) var(--border-style) var(--border-color);
  color: var(--color-text-primary);
}

.table tbody tr:hover {
  background-color: var(--color-gray-50);
}

.table tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  z-index: var(--z-modal);
  display: none;
  width: 100%;
  height: 100%;
  overflow: auto;
}

.modal.active {
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: var(--z-modal-backdrop);
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  position: relative;
  z-index: var(--z-modal);
  width: 90%;
  max-width: 600px;
  background-color: var(--color-bg-secondary);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-2xl);
  padding: var(--space-6);
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-5);
  padding-bottom: var(--space-4);
  border-bottom: var(--border-width) var(--border-style) var(--border-color);
}

.modal-title {
  font-size: var(--font-size-xl);
  font-weight: 600;
}

.modal-close {
  background: none;
  border: none;
  font-size: var(--font-size-2xl);
  cursor: pointer;
  color: var(--color-text-tertiary);
  padding: 0;
  line-height: 1;
}

.modal-close:hover {
  color: var(--color-text-primary);
}

.modal-body {
  margin-bottom: var(--space-5);
}

.modal-footer {
  display: flex;
  gap: var(--space-3);
  justify-content: flex-end;
  padding-top: var(--space-4);
  border-top: var(--border-width) var(--border-style) var(--border-color);
}

/* Tooltips */
.tooltip {
  position: relative;
  display: inline-block;
}

.tooltip-text {
  visibility: hidden;
  position: absolute;
  z-index: var(--z-tooltip);
  bottom: 125%;
  left: 50%;
  transform: translateX(-50%);
  background-color: var(--color-gray-900);
  color: white;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  font-size: var(--font-size-sm);
  white-space: nowrap;
  opacity: 0;
  transition: opacity var(--transition-duration) var(--transition-easing);
}

.tooltip:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
}

/* Dropdown */
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: var(--z-dropdown);
  display: none;
  min-width: 200px;
  padding: var(--space-2);
  margin-top: var(--space-2);
  background-color: var(--color-bg-secondary);
  border: var(--border-width) var(--border-style) var(--border-color);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
}

.dropdown.active .dropdown-menu {
  display: block;
}

.dropdown-item {
  display: block;
  width: 100%;
  padding: var(--space-3) var(--space-4);
  text-align: left;
  color: var(--color-text-primary);
  background: none;
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: background-color var(--transition-duration) var(--transition-easing);
}

.dropdown-item:hover {
  background-color: var(--color-gray-100);
}

/* Breadcrumbs */
.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  padding: var(--space-3) 0;
  list-style: none;
  gap: var(--space-2);
}

.breadcrumb-item {
  display: flex;
  align-items: center;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

.breadcrumb-item::after {
  content: "/";
  margin-left: var(--space-2);
  color: var(--color-text-tertiary);
}

.breadcrumb-item:last-child::after {
  content: "";
}

.breadcrumb-item.active {
  color: var(--color-text-primary);
  font-weight: 500;
}

/* Pagination */
.pagination {
  display: flex;
  list-style: none;
  gap: var(--space-2);
}

.pagination-item {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 40px;
  height: 40px;
  padding: 0 var(--space-3);
  color: var(--color-text-primary);
  background-color: var(--color-bg-secondary);
  border: var(--border-width) var(--border-style) var(--border-color);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--transition-duration) var(--transition-easing);
}

.pagination-item:hover {
  background-color: var(--color-primary-50);
  border-color: var(--color-primary-500);
  color: var(--color-primary-600);
}

.pagination-item.active {
  background-color: var(--color-primary-600);
  border-color: var(--color-primary-600);
  color: white;
}

.pagination-item:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Progress bars */
.progress {
  display: flex;
  height: 1rem;
  overflow: hidden;
  background-color: var(--color-gray-200);
  border-radius: var(--radius-full);
}

.progress-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
  text-align: center;
  white-space: nowrap;
  background-color: var(--color-primary-600);
  transition: width 0.6s ease;
}

/* Spinners */
.spinner {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  border: 3px solid var(--color-gray-300);
  border-top-color: var(--color-primary-600);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.spinner-sm {
  width: 1rem;
  height: 1rem;
  border-width: 2px;
}

.spinner-lg {
  width: 3rem;
  height: 3rem;
  border-width: 4px;
}

/* Responsive components */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    gap: var(--space-3);
  }
  
  .navbar-nav {
    flex-direction: column;
    width: 100%;
  }
  
  .modal-content {
    width: 95%;
    margin: var(--space-4);
  }
  
  .table {
    font-size: var(--font-size-sm);
  }
  
  .table thead th,
  .table tbody td {
    padding: var(--space-2) var(--space-3);
  }
}
"""
    
    def generate_utility_styles(self):
        """Generate utility classes"""
        return """
/* ========================================
   Utility Classes
   ======================================== */

/* Background colors */
.bg-primary { background-color: var(--color-primary-600); }
.bg-secondary { background-color: var(--color-secondary-600); }
.bg-white { background-color: #ffffff; }
.bg-transparent { background-color: transparent; }
.bg-gray-50 { background-color: var(--color-gray-50); }
.bg-gray-100 { background-color: var(--color-gray-100); }
.bg-gray-200 { background-color: var(--color-gray-200); }

/* Border utilities */
.border { border: var(--border-width) var(--border-style) var(--border-color); }
.border-t { border-top: var(--border-width) var(--border-style) var(--border-color); }
.border-r { border-right: var(--border-width) var(--border-style) var(--border-color); }
.border-b { border-bottom: var(--border-width) var(--border-style) var(--border-color); }
.border-l { border-left: var(--border-width) var(--border-style) var(--border-color); }
.border-0 { border: none; }

.border-primary { border-color: var(--color-primary-500); }
.border-secondary { border-color: var(--color-secondary-500); }

/* Border radius */
.rounded-none { border-radius: 0; }
.rounded-sm { border-radius: var(--radius-sm); }
.rounded { border-radius: var(--radius-md); }
.rounded-md { border-radius: var(--radius-md); }
.rounded-lg { border-radius: var(--radius-lg); }
.rounded-xl { border-radius: var(--radius-xl); }
.rounded-full { border-radius: var(--radius-full); }

/* Shadow utilities */
.shadow-none { box-shadow: none; }
.shadow-xs { box-shadow: var(--shadow-xs); }
.shadow-sm { box-shadow: var(--shadow-sm); }
.shadow { box-shadow: var(--shadow-md); }
.shadow-md { box-shadow: var(--shadow-md); }
.shadow-lg { box-shadow: var(--shadow-lg); }
.shadow-xl { box-shadow: var(--shadow-xl); }
.shadow-2xl { box-shadow: var(--shadow-2xl); }

/* Opacity */
.opacity-0 { opacity: 0; }
.opacity-25 { opacity: 0.25; }
.opacity-50 { opacity: 0.5; }
.opacity-75 { opacity: 0.75; }
.opacity-100 { opacity: 1; }

/* Cursor */
.cursor-pointer { cursor: pointer; }
.cursor-not-allowed { cursor: not-allowed; }
.cursor-default { cursor: default; }

/* Pointer events */
.pointer-events-none { pointer-events: none; }
.pointer-events-auto { pointer-events: auto; }

/* User select */
.select-none { user-select: none; }
.select-text { user-select: text; }
.select-all { user-select: all; }

/* Visibility */
.visible { visibility: visible; }
.invisible { visibility: hidden; }

/* Z-index */
.z-0 { z-index: 0; }
.z-10 { z-index: 10; }
.z-20 { z-index: 20; }
.z-30 { z-index: 30; }
.z-40 { z-index: 40; }
.z-50 { z-index: 50; }

/* Transitions */
.transition-none { transition: none; }
.transition-all { transition: all var(--transition-duration) var(--transition-easing); }
.transition-colors { transition: color, background-color, border-color var(--transition-duration) var(--transition-easing); }
.transition-opacity { transition: opacity var(--transition-duration) var(--transition-easing); }
.transition-transform { transition: transform var(--transition-duration) var(--transition-easing); }

/* Transform */
.scale-90 { transform: scale(0.9); }
.scale-95 { transform: scale(0.95); }
.scale-100 { transform: scale(1); }
.scale-105 { transform: scale(1.05); }
.scale-110 { transform: scale(1.1); }

.rotate-45 { transform: rotate(45deg); }
.rotate-90 { transform: rotate(90deg); }
.rotate-180 { transform: rotate(180deg); }

/* Hover effects */
.hover\\:shadow-lg:hover { box-shadow: var(--shadow-lg); }
.hover\\:scale-105:hover { transform: scale(1.05); }
.hover\\:bg-primary:hover { background-color: var(--color-primary-600); }

/* Focus effects */
.focus\\:outline-none:focus { outline: none; }
.focus\\:ring:focus { box-shadow: 0 0 0 3px var(--color-primary-100); }

/* Object fit */
.object-contain { object-fit: contain; }
.object-cover { object-fit: cover; }
.object-fill { object-fit: fill; }
.object-none { object-fit: none; }

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.animate-fadeIn { animation: fadeIn var(--transition-duration) var(--transition-easing); }
.animate-fadeOut { animation: fadeOut var(--transition-duration) var(--transition-easing); }
.animate-slideDown { animation: slideDown var(--transition-duration) var(--transition-easing); }
.animate-slideUp { animation: slideUp var(--transition-duration) var(--transition-easing); }
.animate-pulse { animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }

/* Responsive utilities */
@media (max-width: 480px) {
  .sm\\:text-center { text-align: center; }
  .sm\\:w-full { width: 100%; }
  .sm\\:flex-col { flex-direction: column; }
}

@media (max-width: 768px) {
  .md\\:hidden { display: none; }
  .md\\:block { display: block; }
  .md\\:flex { display: flex; }
  .md\\:text-center { text-align: center; }
}

@media (max-width: 1024px) {
  .lg\\:hidden { display: none; }
}
"""
    
    def generate_full_css(self, theme='light'):
        """Generate complete CSS file"""
        is_dark = 'dark' if theme == 'dark' else 'light'
        
        css = f"""/*
 * CSS Theme Generator
 * Design Name: {self.design_name}
 * Theme: {theme.title()}
 * Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
 * 
 * This CSS file is fully responsive and works on all screen sizes.
 * Features:
 * - Mobile-first responsive design
 * - Modern CSS variables for easy customization
 * - Comprehensive component library
 * - Utility-first classes
 * - Smooth animations and transitions
 * - Accessibility-focused
 */

/* ========================================
   CSS Custom Properties (Variables)
   ======================================== */

:root {{
{self.generate_css_variables(theme)}
}}

{self.generate_reset_and_base()}
{self.generate_typography_styles()}
{self.generate_layout_styles()}
{self.generate_component_styles()}
{self.generate_utility_styles()}

/* ========================================
   Print Styles
   ======================================== */

@media print {{
  *,
  *::before,
  *::after {{
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }}
  
  a,
  a:visited {{
    text-decoration: underline;
  }}
  
  a[href]::after {{
    content: " (" attr(href) ")";
  }}
  
  abbr[title]::after {{
    content: " (" attr(title) ")";
  }}
  
  pre,
  blockquote {{
    border: 1px solid #999;
    page-break-inside: avoid;
  }}
  
  thead {{
    display: table-header-group;
  }}
  
  tr,
  img {{
    page-break-inside: avoid;
  }}
  
  img {{
    max-width: 100% !important;
  }}
  
  p,
  h2,
  h3 {{
    orphans: 3;
    widows: 3;
  }}
  
  h2,
  h3 {{
    page-break-after: avoid;
  }}
}}

/* ========================================
   End of {self.design_name} - {theme.title()} Theme
   ======================================== */
"""
        return css
    
    def generate(self):
        """Generate both light and dark theme CSS files"""
        # Create output directory
        os.makedirs('generated_themes', exist_ok=True)
        
        # Create a URL-friendly slug from the design name
        design_slug = self.design_name.lower().replace(' ', '-')
        
        # Generate light theme
        light_css = self.generate_full_css('light')
        light_filename = f'generated_themes/{design_slug}-light-{self.timestamp}.css'
        with open(light_filename, 'w', encoding='utf-8') as f:
            f.write(light_css)
        
        # Generate dark theme
        dark_css = self.generate_full_css('dark')
        dark_filename = f'generated_themes/{design_slug}-dark-{self.timestamp}.css'
        with open(dark_filename, 'w', encoding='utf-8') as f:
            f.write(dark_css)
        
        return light_filename, dark_filename


def main():
    """Main function to run the generator"""
    print("╔═══════════════════════════════════════════════════╗")
    print("║     CSS Theme Generator                           ║")
    print("║     Generating responsive themes...               ║")
    print("╚═══════════════════════════════════════════════════╝\n")
    
    generator = CSSThemeGenerator()
    light_file, dark_file = generator.generate()
    
    print("✅ Generation complete!\n")
    print(f"🎨 Design Name: {generator.design_name}")
    print(f"📁 Light theme: {light_file}")
    print(f"📁 Dark theme: {dark_file}\n")
    print("Features included:")
    print("  ✓ Fully responsive (mobile, tablet, desktop)")
    print("  ✓ Modern CSS variables")
    print("  ✓ Complete component library")
    print("  ✓ Utility classes")
    print("  ✓ Smooth animations")
    print("  ✓ Accessibility features")
    print(f"\n🎨 Your unique design '{generator.design_name}' is ready to use!")
    print("💡 Run again to generate a completely different theme!")


if __name__ == "__main__":
    main()
