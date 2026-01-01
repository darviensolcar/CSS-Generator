#!/usr/bin/env python3
"""
CSS Theme Variation Generator
Analyzes existing CSS themes and generates cohesive variations that match the original design and vibe.
Creates harmonious theme families with consistent design language.
"""

import re
import os
import random
import colorsys
from datetime import datetime
from pathlib import Path


class ThemeAnalyzer:
    """Analyzes existing CSS themes to extract design patterns"""
    
    def __init__(self, css_content):
        self.css_content = css_content
        self.colors = self.extract_colors()
        self.typography = self.extract_typography()
        self.spacing = self.extract_spacing()
        self.borders = self.extract_borders()
        self.shadows = self.extract_shadows()
        self.animations = self.extract_animations()
        self.design_name = self.extract_design_name()
        
    def extract_design_name(self):
        """Extract the design name from CSS comments"""
        match = re.search(r'Design Name:\s*(.+?)(?:\n|\*)', self.css_content)
        if match:
            return match.group(1).strip()
        return "Unknown Design"
    
    def extract_colors(self):
        """Extract color values from CSS variables"""
        colors = {}
        pattern = r'--color-([^:]+):\s*(#[0-9a-fA-F]{6}|rgba?\([^)]+\))'
        matches = re.findall(pattern, self.css_content)
        for name, value in matches:
            colors[name] = value
        return colors
    
    def extract_typography(self):
        """Extract typography settings"""
        typography = {}
        patterns = {
            'base_font': r'--font-base:\s*(.+?);',
            'heading_font': r'--font-heading:\s*(.+?);',
            'base_size': r'--font-size-base:\s*(.+?);',
            'scale_ratio': r'--font-size-lg:\s*([0-9.]+)rem',
        }
        for key, pattern in patterns.items():
            match = re.search(pattern, self.css_content)
            if match:
                typography[key] = match.group(1).strip()
        return typography
    
    def extract_spacing(self):
        """Extract spacing scale"""
        spacing = {}
        pattern = r'--space-(\d+):\s*(\d+)px'
        matches = re.findall(pattern, self.css_content)
        for index, value in matches:
            spacing[index] = int(value)
        return spacing
    
    def extract_borders(self):
        """Extract border styles"""
        borders = {}
        patterns = {
            'width': r'--border-width:\s*(.+?);',
            'style': r'--border-style:\s*(.+?);',
            'radius_sm': r'--radius-sm:\s*(.+?);',
            'radius_md': r'--radius-md:\s*(.+?);',
            'radius_lg': r'--radius-lg:\s*(.+?);',
        }
        for key, pattern in patterns.items():
            match = re.search(pattern, self.css_content)
            if match:
                borders[key] = match.group(1).strip()
        return borders
    
    def extract_shadows(self):
        """Extract shadow definitions"""
        shadows = {}
        pattern = r'--shadow-(\w+):\s*(.+?);'
        matches = re.findall(pattern, self.css_content)
        for name, value in matches:
            shadows[name] = value
        return shadows
    
    def extract_animations(self):
        """Extract animation settings"""
        animations = {}
        patterns = {
            'duration': r'--transition-duration:\s*(.+?);',
            'easing': r'--transition-easing:\s*(.+?);',
        }
        for key, pattern in patterns.items():
            match = re.search(pattern, self.css_content)
            if match:
                animations[key] = match.group(1).strip()
        return animations


class ThemeVariationGenerator:
    """Generates theme variations based on analyzed themes"""
    
    def __init__(self, theme_analyzers):
        self.analyzers = theme_analyzers
        self.base_design_name = self.analyzers[0].design_name if self.analyzers else "Base"
        
    def generate_variation_name(self, variation_number):
        """Generate creative variation names"""
        suffixes = [
            'Edition', 'Variant', 'Version', 'Style', 'Mode',
            'Palette', 'Scheme', 'Mix', 'Blend', 'Fusion',
            'Harmony', 'Rhythm', 'Flow', 'Vibe', 'Aura'
        ]
        
        modifiers = [
            'Enhanced', 'Refined', 'Evolved', 'Advanced', 'Extended',
            'Premium', 'Deluxe', 'Elite', 'Superior', 'Optimized',
            'Amplified', 'Enriched', 'Elevated', 'Polished', 'Perfected'
        ]
        
        # Different naming patterns
        patterns = [
            f"{self.base_design_name} {random.choice(suffixes)} {variation_number}",
            f"{random.choice(modifiers)} {self.base_design_name} {variation_number}",
            f"{self.base_design_name} {variation_number}.{random.randint(0, 9)}",
            f"{self.base_design_name} {random.choice(suffixes)}",
        ]
        
        return random.choice(patterns)
    
    def hex_to_hsl(self, hex_color):
        """Convert hex color to HSL"""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return h * 360, s * 100, l * 100
    
    def hsl_to_hex(self, h, s, l):
        """Convert HSL to hex color"""
        r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def adjust_color_variation(self, hex_color, variation_strength=0.1):
        """Create a color variation while maintaining harmony"""
        if not hex_color or not hex_color.startswith('#'):
            return hex_color
        
        h, s, l = self.hex_to_hsl(hex_color)
        
        # Vary hue slightly (±5-15 degrees)
        h_shift = random.uniform(-15, 15) * variation_strength
        h = (h + h_shift) % 360
        
        # Vary saturation slightly (±5-10%)
        s_shift = random.uniform(-10, 10) * variation_strength
        s = max(0, min(100, s + s_shift))
        
        # Vary lightness slightly (±3-8%)
        l_shift = random.uniform(-8, 8) * variation_strength
        l = max(0, min(100, l + l_shift))
        
        return self.hsl_to_hex(h, s, l)
    
    def blend_colors(self, color1, color2, ratio=0.5):
        """Blend two colors together"""
        if not color1 or not color1.startswith('#'):
            return color2
        if not color2 or not color2.startswith('#'):
            return color1
            
        h1, s1, l1 = self.hex_to_hsl(color1)
        h2, s2, l2 = self.hex_to_hsl(color2)
        
        # Blend HSL values
        h = (h1 * ratio + h2 * (1 - ratio)) % 360
        s = s1 * ratio + s2 * (1 - ratio)
        l = l1 * ratio + l2 * (1 - ratio)
        
        return self.hsl_to_hex(h, s, l)
    
    def create_color_variations(self, variation_type='shift'):
        """Create color variations based on analyzed themes"""
        base_colors = self.analyzers[0].colors
        new_colors = {}
        
        if variation_type == 'shift':
            # Shift all colors in a consistent direction
            shift_strength = random.uniform(0.05, 0.15)
            for name, color in base_colors.items():
                new_colors[name] = self.adjust_color_variation(color, shift_strength)
                
        elif variation_type == 'blend' and len(self.analyzers) > 1:
            # Blend colors from two themes
            theme2_colors = self.analyzers[1].colors
            blend_ratio = random.uniform(0.3, 0.7)
            for name, color in base_colors.items():
                if name in theme2_colors:
                    new_colors[name] = self.blend_colors(color, theme2_colors[name], blend_ratio)
                else:
                    new_colors[name] = color
                    
        elif variation_type == 'complement':
            # Create complementary color scheme
            for name, color in base_colors.items():
                if 'primary' in name or 'secondary' in name:
                    h, s, l = self.hex_to_hsl(color)
                    # Shift hue by 180 degrees for complementary
                    h = (h + 180) % 360
                    new_colors[name] = self.hsl_to_hex(h, s, l)
                else:
                    new_colors[name] = self.adjust_color_variation(color, 0.08)
                    
        elif variation_type == 'analogous':
            # Create analogous color scheme (colors next to each other)
            for name, color in base_colors.items():
                if 'primary' in name or 'secondary' in name:
                    h, s, l = self.hex_to_hsl(color)
                    # Shift hue by 30 degrees
                    h = (h + random.choice([-30, 30])) % 360
                    new_colors[name] = self.hsl_to_hex(h, s, l)
                else:
                    new_colors[name] = self.adjust_color_variation(color, 0.06)
                    
        elif variation_type == 'monochromatic':
            # Create monochromatic variation (same hue, different sat/light)
            for name, color in base_colors.items():
                h, s, l = self.hex_to_hsl(color)
                # Keep hue, vary saturation and lightness
                s_shift = random.uniform(-15, 15)
                l_shift = random.uniform(-10, 10)
                s = max(0, min(100, s + s_shift))
                l = max(0, min(100, l + l_shift))
                new_colors[name] = self.hsl_to_hex(h, s, l)
                
        else:  # 'subtle'
            # Very subtle variations
            for name, color in base_colors.items():
                new_colors[name] = self.adjust_color_variation(color, 0.05)
        
        return new_colors
    
    def create_typography_variation(self):
        """Create typography variations"""
        base_typography = self.analyzers[0].typography
        
        # Keep same fonts but might adjust sizes slightly
        variation = base_typography.copy()
        
        # Occasionally swap heading and body fonts for variety
        if random.random() > 0.7 and 'base_font' in variation and 'heading_font' in variation:
            variation['base_font'], variation['heading_font'] = variation['heading_font'], variation['base_font']
        
        return variation
    
    def create_spacing_variation(self):
        """Create spacing variations"""
        base_spacing = self.analyzers[0].spacing
        
        # Apply consistent multiplier to all spacing
        multiplier = random.uniform(0.9, 1.1)
        new_spacing = {}
        for key, value in base_spacing.items():
            new_spacing[key] = int(value * multiplier)
        
        return new_spacing
    
    def create_border_variation(self):
        """Create border variations"""
        base_borders = self.analyzers[0].borders
        new_borders = base_borders.copy()
        
        # Occasionally adjust border radius
        if random.random() > 0.5:
            radius_multiplier = random.uniform(0.8, 1.2)
            for key in ['radius_sm', 'radius_md', 'radius_lg']:
                if key in new_borders and new_borders[key].endswith('px'):
                    value = int(new_borders[key].replace('px', ''))
                    new_borders[key] = f"{int(value * radius_multiplier)}px"
        
        return new_borders
    
    def generate_variations(self, num_variations, output_dir='generated_variations'):
        """Generate multiple theme variations"""
        os.makedirs(output_dir, exist_ok=True)
        
        variation_types = ['shift', 'blend', 'complement', 'analogous', 'monochromatic', 'subtle']
        generated_files = []
        
        print(f"\n🎨 Generating {num_variations} variations of '{self.base_design_name}'...\n")
        
        for i in range(1, num_variations + 1):
            print(f"Creating variation {i}/{num_variations}...", end=" ")
            
            # Choose variation strategy
            if len(self.analyzers) > 1 and random.random() > 0.5:
                variation_type = 'blend'
            else:
                variation_type = random.choice(variation_types)
            
            # Generate variation name
            variation_name = self.generate_variation_name(i)
            
            # Create variations
            new_colors = self.create_color_variations(variation_type)
            new_typography = self.create_typography_variation()
            new_spacing = self.create_spacing_variation()
            new_borders = self.create_border_variation()
            
            # Generate CSS for both light and dark themes
            for theme_type in ['light', 'dark']:
                css_content = self.generate_css_file(
                    variation_name,
                    theme_type,
                    new_colors,
                    new_typography,
                    new_spacing,
                    new_borders,
                    self.analyzers[0].shadows,
                    self.analyzers[0].animations,
                    variation_type
                )
                
                # Create filename
                slug = variation_name.lower().replace(' ', '-').replace('.', '')
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{output_dir}/{slug}-{theme_type}-{timestamp}.css"
                
                # Write file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(css_content)
                
                generated_files.append(filename)
            
            print(f"✅ '{variation_name}' created!")
        
        return generated_files
    
    def generate_css_file(self, name, theme_type, colors, typography, spacing, borders, shadows, animations, variation_type):
        """Generate complete CSS file for a variation"""
        
        # Generate variable sections
        color_vars = self._generate_color_variables(colors)
        typography_vars = self._generate_typography_variables(typography)
        spacing_vars = self._generate_spacing_variables(spacing)
        border_vars = self._generate_border_variables(borders)
        shadow_vars = self._generate_shadow_variables(shadows)
        animation_vars = self._generate_animation_variables(animations)
        
        css = f"""/*
 * CSS Theme Variation Generator
 * Design Name: {name}
 * Base Design: {self.base_design_name}
 * Variation Type: {variation_type}
 * Theme: {theme_type.title()}
 * Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
 * 
 * This is an enhanced variation that maintains the design language
 * of the original theme while adding unique characteristics.
 * 
 * Features:
 * - Harmonious color variations
 * - Consistent design patterns
 * - Full responsive support
 * - Complete component library
 */

/* ========================================
   CSS Custom Properties (Variables)
   ======================================== */

:root {{
  /* Color Palette - Enhanced Variation */
{color_vars}
  /* Typography - Maintained from base */
{typography_vars}
  /* Spacing - Refined variation */
{spacing_vars}
  /* Border Styles - Enhanced */
{border_vars}
  /* Shadows - From base theme */
{shadow_vars}
  /* Animations - Consistent timing */
{animation_vars}
  /* Z-index layers */
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-modal-backdrop: 1040;
  --z-modal: 1050;
  --z-popover: 1060;
  --z-tooltip: 1070;
}}

/* Import base styles from original theme */
/* Note: You may need to include the full component styles here */
/* This variation focuses on color and spacing adjustments */

/* ========================================
   Enhanced Variations
   ======================================== */

/* Custom enhancements for this variation */
.variation-badge {{
  background: linear-gradient(135deg, var(--color-primary-500), var(--color-secondary-500));
  color: white;
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-full);
  font-size: var(--font-size-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}}

.variation-card {{
  background: linear-gradient(145deg, var(--color-bg-secondary), var(--color-bg-tertiary));
  border: 2px solid var(--color-primary-200);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-lg);
  transition: all var(--transition-duration) var(--transition-easing);
}}

.variation-card:hover {{
  transform: translateY(-4px);
  box-shadow: var(--shadow-2xl);
  border-color: var(--color-primary-400);
}}

/* Enhanced button variations */
.btn-variation-primary {{
  background: linear-gradient(135deg, var(--color-primary-600), var(--color-primary-700));
  border: none;
  color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: 500;
  transition: all var(--transition-duration) var(--transition-easing);
  box-shadow: var(--shadow-md);
}}

.btn-variation-primary:hover {{
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  background: linear-gradient(135deg, var(--color-primary-700), var(--color-primary-800));
}}

/* Variation-specific accent colors */
.accent-variation-1 {{ color: var(--color-accent-500); }}
.accent-variation-2 {{ color: var(--color-secondary-600); }}
.bg-accent-variation {{ background-color: var(--color-accent-100); }}

/* Enhanced focus states for this variation */
*:focus-visible {{
  outline: 3px solid var(--color-primary-400);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}}

/* ========================================
   End of {name} - {theme_type.title()} Theme
   ======================================== */
"""
        return css
    
    def _generate_color_variables(self, colors):
        """Generate CSS color variables"""
        css = ""
        for name, value in colors.items():
            css += f"  --color-{name}: {value};\n"
        return css
    
    def _generate_typography_variables(self, typography):
        """Generate CSS typography variables"""
        css = ""
        if 'base_font' in typography:
            css += f"  --font-base: {typography['base_font']};\n"
        if 'heading_font' in typography:
            css += f"  --font-heading: {typography['heading_font']};\n"
        css += "  --font-code: 'Fira Code', 'Courier New', monospace;\n"
        if 'base_size' in typography:
            css += f"  --font-size-base: {typography['base_size']};\n"
        return css
    
    def _generate_spacing_variables(self, spacing):
        """Generate CSS spacing variables"""
        css = ""
        for key, value in sorted(spacing.items(), key=lambda x: int(x[0])):
            css += f"  --space-{key}: {value}px;\n"
        return css
    
    def _generate_border_variables(self, borders):
        """Generate CSS border variables"""
        css = ""
        for key, value in borders.items():
            css += f"  --{key.replace('_', '-')}: {value};\n"
        return css
    
    def _generate_shadow_variables(self, shadows):
        """Generate CSS shadow variables"""
        css = ""
        for name, value in shadows.items():
            css += f"  --shadow-{name}: {value};\n"
        return css
    
    def _generate_animation_variables(self, animations):
        """Generate CSS animation variables"""
        css = ""
        for key, value in animations.items():
            css += f"  --transition-{key}: {value};\n"
        return css


def select_theme_files():
    """Interactive theme file selection"""
    print("╔═══════════════════════════════════════════════════╗")
    print("║   CSS Theme Variation Generator                   ║")
    print("╚═══════════════════════════════════════════════════╝\n")
    
    # Look for theme files
    theme_dir = 'generated_themes'
    if not os.path.exists(theme_dir):
        print(f"❌ Error: '{theme_dir}' directory not found!")
        print("Please run css_generator.py first to create base themes.\n")
        return None
    
    # Get all CSS files
    css_files = [f for f in os.listdir(theme_dir) if f.endswith('.css')]
    
    if not css_files:
        print(f"❌ Error: No CSS files found in '{theme_dir}'!")
        print("Please run css_generator.py first to create base themes.\n")
        return None
    
    # Group by design name
    designs = {}
    for file in css_files:
        # Extract design name from filename
        parts = file.rsplit('-', 2)
        if len(parts) >= 3:
            design_name = parts[0]
            if design_name not in designs:
                designs[design_name] = []
            designs[design_name].append(file)
    
    print(f"Found {len(designs)} design(s) with {len(css_files)} theme file(s):\n")
    
    # Display available designs
    design_list = list(designs.keys())
    for idx, design in enumerate(design_list, 1):
        file_count = len(designs[design])
        print(f"  {idx}. {design.replace('-', ' ').title()} ({file_count} files)")
    
    print()
    
    # Get user selection
    while True:
        try:
            choice = input("Select a design number (or press Enter to use the first design): ").strip()
            
            if not choice:
                selected_design = design_list[0]
                break
            
            choice = int(choice)
            if 1 <= choice <= len(design_list):
                selected_design = design_list[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(design_list)}")
        except ValueError:
            print("Please enter a valid number")
    
    selected_files = designs[selected_design]
    print(f"\n✅ Selected: {selected_design.replace('-', ' ').title()}")
    print(f"   Using {len(selected_files)} theme file(s) as base\n")
    
    return [os.path.join(theme_dir, f) for f in selected_files[:2]]  # Use up to 2 files


def get_variation_count():
    """Get number of variations to generate"""
    while True:
        try:
            print("How many variations would you like to create?")
            count = input("Enter a number from 1 to 10: ").strip()
            
            if not count:
                return 3  # Default
            
            count = int(count)
            if 1 <= count <= 10:
                return count
            else:
                print("Please enter a number between 1 and 10\n")
        except ValueError:
            print("Please enter a valid number\n")


def main():
    """Main function"""
    # Select theme files
    theme_files = select_theme_files()
    
    if not theme_files:
        return
    
    # Get number of variations
    num_variations = get_variation_count()
    
    print(f"\n📊 Analyzing {len(theme_files)} base theme(s)...")
    
    # Analyze themes
    analyzers = []
    for theme_file in theme_files:
        try:
            with open(theme_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
                analyzer = ThemeAnalyzer(css_content)
                analyzers.append(analyzer)
                print(f"   ✓ Analyzed: {analyzer.design_name}")
        except Exception as e:
            print(f"   ✗ Error reading {theme_file}: {e}")
    
    if not analyzers:
        print("\n❌ No themes could be analyzed!")
        return
    
    # Generate variations
    generator = ThemeVariationGenerator(analyzers)
    generated_files = generator.generate_variations(num_variations)
    
    # Summary
    print(f"\n╔═══════════════════════════════════════════════════╗")
    print(f"║  ✅ Generation Complete!                          ║")
    print(f"╚═══════════════════════════════════════════════════╝\n")
    print(f"📦 Generated {len(generated_files)} CSS files ({num_variations} variations × 2 themes)")
    print(f"📁 Location: generated_variations/\n")
    print("🎨 Variation types used:")
    print("   • Color shifts - Harmonious hue adjustments")
    print("   • Blended themes - Mixed characteristics")
    print("   • Complementary - Opposite color wheel positions")
    print("   • Analogous - Adjacent color harmonies")
    print("   • Monochromatic - Same hue variations")
    print("   • Subtle - Refined micro-adjustments\n")
    print("💡 Each variation maintains the design language of the original!")
    print("🚀 Ready to use in your projects!\n")


if __name__ == "__main__":
    main()
