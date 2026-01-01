#!/usr/bin/env python3
"""
Demo HTML Generator
Generates complete demo HTML pages that showcase your CSS themes with all components.
"""

import os
import re
from datetime import datetime
from pathlib import Path


class DemoHTMLGenerator:
    """Generates demo HTML pages for CSS themes"""
    
    def __init__(self, css_file):
        self.css_file = css_file
        self.css_filename = os.path.basename(css_file)
        self.theme_name = self.extract_theme_name()
        
    def extract_theme_name(self):
        """Extract theme name from CSS filename or content"""
        # Try to get from filename
        name = self.css_filename.replace('.css', '').replace('-', ' ').title()
        
        # Try to read from CSS file
        try:
            with open(self.css_file, 'r', encoding='utf-8') as f:
                content = f.read(500)  # Read first 500 chars
                match = re.search(r'Design Name:\s*(.+?)(?:\n|\*)', content)
                if match:
                    name = match.group(1).strip()
        except:
            pass
        
        return name
    
    def generate_demo_html(self):
        """Generate complete demo HTML"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Demo showcase for {self.theme_name} CSS theme">
    <title>{self.theme_name} - CSS Theme Demo</title>
    <link rel="stylesheet" href="{self.css_filename}">
    <style>
        /* Additional demo-specific styles */
        .demo-section {{
            margin-bottom: 4rem;
        }}
        
        .demo-header {{
            text-align: center;
            padding: 4rem 0;
            background: linear-gradient(135deg, var(--color-primary-500, #3b82f6), var(--color-secondary-500, #8b5cf6));
            color: white;
            margin-bottom: 4rem;
        }}
        
        .demo-header h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            color: white;
        }}
        
        .demo-header p {{
            font-size: 1.25rem;
            opacity: 0.9;
            color: white;
        }}
        
        .section-title {{
            font-size: 2rem;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid var(--color-gray-200, #e5e7eb);
        }}
        
        .component-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }}
        
        .color-swatch {{
            height: 100px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .code-preview {{
            background: var(--color-gray-100, #f3f4f6);
            border: 1px solid var(--color-gray-200, #e5e7eb);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
            overflow-x: auto;
        }}
        
        .code-preview code {{
            font-size: 0.875rem;
        }}
        
        .theme-switcher {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 1000;
        }}
        
        .demo-box {{
            padding: 2rem;
            border: 2px dashed var(--color-gray-300, #d1d5db);
            border-radius: 8px;
            text-align: center;
            background: var(--color-gray-50, #f9fafb);
        }}
    </style>
</head>
<body>
    <!-- Demo Header -->
    <div class="demo-header">
        <div class="container">
            <h1>{self.theme_name}</h1>
            <p>Complete CSS Theme Showcase</p>
            <p style="font-size: 1rem; margin-top: 1rem;">Generated on {datetime.now().strftime("%B %d, %Y")}</p>
        </div>
    </div>

    <!-- Main Content -->
    <div class="container">
        
        <!-- Typography Section -->
        <section class="demo-section">
            <h2 class="section-title">Typography</h2>
            
            <h1>Heading 1 - The quick brown fox</h1>
            <h2>Heading 2 - The quick brown fox</h2>
            <h3>Heading 3 - The quick brown fox</h3>
            <h4>Heading 4 - The quick brown fox</h4>
            <h5>Heading 5 - The quick brown fox</h5>
            <h6>Heading 6 - The quick brown fox</h6>
            
            <p>Regular paragraph text. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            
            <p class="text-lg">Large text. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            
            <p class="text-sm">Small text. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            
            <blockquote>
                "This is a blockquote. It's styled differently to stand out from regular text. Perfect for highlighting important quotes or testimonials."
            </blockquote>
            
            <div class="code-preview">
                <code>&lt;h1&gt;Heading 1&lt;/h1&gt;</code>
            </div>
        </section>

        <!-- Buttons Section -->
        <section class="demo-section">
            <h2 class="section-title">Buttons</h2>
            
            <div class="component-grid">
                <div>
                    <h3>Primary Buttons</h3>
                    <button class="btn btn-primary">Primary Button</button>
                    <button class="btn btn-primary btn-sm">Small Primary</button>
                    <button class="btn btn-primary btn-lg">Large Primary</button>
                    <button class="btn btn-primary" disabled>Disabled</button>
                </div>
                
                <div>
                    <h3>Secondary Buttons</h3>
                    <button class="btn btn-secondary">Secondary Button</button>
                    <button class="btn btn-secondary btn-sm">Small Secondary</button>
                    <button class="btn btn-secondary btn-lg">Large Secondary</button>
                </div>
                
                <div>
                    <h3>Outline Buttons</h3>
                    <button class="btn btn-outline">Outline Button</button>
                    <button class="btn btn-outline btn-sm">Small Outline</button>
                    <button class="btn btn-outline btn-lg">Large Outline</button>
                </div>
                
                <div>
                    <h3>Ghost Buttons</h3>
                    <button class="btn btn-ghost">Ghost Button</button>
                    <button class="btn btn-ghost btn-sm">Small Ghost</button>
                    <button class="btn btn-ghost btn-lg">Large Ghost</button>
                </div>
            </div>
            
            <div class="code-preview">
                <code>&lt;button class="btn btn-primary"&gt;Primary Button&lt;/button&gt;</code>
            </div>
        </section>

        <!-- Cards Section -->
        <section class="demo-section">
            <h2 class="section-title">Cards</h2>
            
            <div class="component-grid">
                <div class="card">
                    <div class="card-header">
                        <h3 class="card-title">Basic Card</h3>
                    </div>
                    <div class="card-body">
                        <p>This is a basic card with header, body, and footer sections. Cards are great for grouping related content.</p>
                    </div>
                    <div class="card-footer">
                        <button class="btn btn-primary btn-sm">Action</button>
                        <button class="btn btn-ghost btn-sm">Cancel</button>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-body">
                        <h3>Simple Card</h3>
                        <p>A card without header or footer. Perfect for simple content display.</p>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <h3 class="card-title">Featured Card</h3>
                    </div>
                    <div class="card-body">
                        <p>Cards can contain any content including images, forms, or other components.</p>
                        <div class="badge badge-primary">Featured</div>
                    </div>
                </div>
            </div>
            
            <div class="code-preview">
                <code>&lt;div class="card"&gt;...&lt;/div&gt;</code>
            </div>
        </section>

        <!-- Forms Section -->
        <section class="demo-section">
            <h2 class="section-title">Forms</h2>
            
            <div class="card">
                <div class="card-body">
                    <form>
                        <div class="form-group">
                            <label class="form-label" for="name">Full Name</label>
                            <input type="text" id="name" class="form-input" placeholder="Enter your name">
                            <span class="form-help">Please enter your full name</span>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="email">Email Address</label>
                            <input type="email" id="email" class="form-input" placeholder="you@example.com" required>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="message">Message</label>
                            <textarea id="message" class="form-textarea" placeholder="Your message here..."></textarea>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="country">Country</label>
                            <select id="country" class="form-select">
                                <option>United States</option>
                                <option>United Kingdom</option>
                                <option>Canada</option>
                                <option>Australia</option>
                            </select>
                        </div>
                        
                        <div class="form-check">
                            <input type="checkbox" id="agree" class="form-check-input">
                            <label for="agree">I agree to the terms and conditions</label>
                        </div>
                        
                        <div class="form-check">
                            <input type="checkbox" id="newsletter" class="form-check-input">
                            <label for="newsletter">Subscribe to newsletter</label>
                        </div>
                        
                        <button type="submit" class="btn btn-primary">Submit Form</button>
                        <button type="reset" class="btn btn-ghost">Reset</button>
                    </form>
                </div>
            </div>
            
            <div class="code-preview">
                <code>&lt;input type="text" class="form-input" placeholder="Enter text"&gt;</code>
            </div>
        </section>

        <!-- Alerts Section -->
        <section class="demo-section">
            <h2 class="section-title">Alerts & Badges</h2>
            
            <div class="alert alert-success">
                <strong>Success!</strong> Your action was completed successfully.
            </div>
            
            <div class="alert alert-warning">
                <strong>Warning!</strong> Please review this information carefully.
            </div>
            
            <div class="alert alert-error">
                <strong>Error!</strong> Something went wrong. Please try again.
            </div>
            
            <div class="alert alert-info">
                <strong>Info:</strong> Here's some helpful information for you.
            </div>
            
            <div style="margin-top: 2rem;">
                <h3>Badges</h3>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
                    <span class="badge badge-primary">Primary</span>
                    <span class="badge badge-secondary">Secondary</span>
                    <span class="badge badge-success">Success</span>
                    <span class="badge badge-warning">Warning</span>
                    <span class="badge badge-error">Error</span>
                </div>
            </div>
            
            <div class="code-preview">
                <code>&lt;div class="alert alert-success"&gt;Success message&lt;/div&gt;</code>
            </div>
        </section>

        <!-- Navigation Section -->
        <section class="demo-section">
            <h2 class="section-title">Navigation</h2>
            
            <nav class="navbar">
                <a href="#" class="navbar-brand">Brand</a>
                <ul class="navbar-nav">
                    <li><a href="#" class="nav-link active">Home</a></li>
                    <li><a href="#" class="nav-link">About</a></li>
                    <li><a href="#" class="nav-link">Services</a></li>
                    <li><a href="#" class="nav-link">Contact</a></li>
                </ul>
            </nav>
            
            <div style="margin-top: 2rem;">
                <h3>Navigation Tabs</h3>
                <ul class="nav">
                    <li><a href="#" class="nav-link active">Active Tab</a></li>
                    <li><a href="#" class="nav-link">Tab 2</a></li>
                    <li><a href="#" class="nav-link">Tab 3</a></li>
                    <li><a href="#" class="nav-link">Tab 4</a></li>
                </ul>
            </div>
            
            <div class="code-preview">
                <code>&lt;nav class="navbar"&gt;...&lt;/nav&gt;</code>
            </div>
        </section>

        <!-- Tables Section -->
        <section class="demo-section">
            <h2 class="section-title">Tables</h2>
            
            <table class="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>John Doe</td>
                        <td>john@example.com</td>
                        <td>Admin</td>
                        <td><span class="badge badge-success">Active</span></td>
                    </tr>
                    <tr>
                        <td>Jane Smith</td>
                        <td>jane@example.com</td>
                        <td>User</td>
                        <td><span class="badge badge-success">Active</span></td>
                    </tr>
                    <tr>
                        <td>Bob Johnson</td>
                        <td>bob@example.com</td>
                        <td>User</td>
                        <td><span class="badge badge-warning">Pending</span></td>
                    </tr>
                    <tr>
                        <td>Alice Williams</td>
                        <td>alice@example.com</td>
                        <td>Moderator</td>
                        <td><span class="badge badge-success">Active</span></td>
                    </tr>
                </tbody>
            </table>
            
            <div class="code-preview">
                <code>&lt;table class="table"&gt;...&lt;/table&gt;</code>
            </div>
        </section>

        <!-- Grid System Section -->
        <section class="demo-section">
            <h2 class="section-title">Grid System</h2>
            
            <div class="grid grid-cols-3 gap-4">
                <div class="demo-box">Column 1</div>
                <div class="demo-box">Column 2</div>
                <div class="demo-box">Column 3</div>
            </div>
            
            <div class="grid grid-cols-4 gap-4" style="margin-top: 2rem;">
                <div class="demo-box">1/4</div>
                <div class="demo-box">1/4</div>
                <div class="demo-box">1/4</div>
                <div class="demo-box">1/4</div>
            </div>
            
            <div class="grid grid-cols-12 gap-4" style="margin-top: 2rem;">
                <div class="col-span-8 demo-box">8 columns</div>
                <div class="col-span-4 demo-box">4 columns</div>
            </div>
            
            <div class="code-preview">
                <code>&lt;div class="grid grid-cols-3 gap-4"&gt;...&lt;/div&gt;</code>
            </div>
        </section>

        <!-- Utility Classes Section -->
        <section class="demo-section">
            <h2 class="section-title">Utility Classes</h2>
            
            <div class="card">
                <div class="card-body">
                    <h3>Text Utilities</h3>
                    <p class="text-left">Left aligned text</p>
                    <p class="text-center">Center aligned text</p>
                    <p class="text-right">Right aligned text</p>
                    <p class="text-primary">Primary color text</p>
                    <p class="text-secondary">Secondary color text</p>
                    <p class="font-bold">Bold text</p>
                    <p class="italic">Italic text</p>
                    <p class="uppercase">Uppercase text</p>
                </div>
            </div>
            
            <div class="card" style="margin-top: 2rem;">
                <div class="card-body">
                    <h3>Spacing Utilities</h3>
                    <div class="p-4 bg-primary" style="background-color: var(--color-gray-200, #e5e7eb);">
                        <div class="p-4 bg-secondary" style="background-color: white;">Padding: p-4</div>
                    </div>
                    <div class="m-4 p-4 bg-primary" style="background-color: var(--color-gray-200, #e5e7eb); margin-top: 1rem;">
                        Margin: m-4
                    </div>
                </div>
            </div>
            
            <div class="code-preview">
                <code>&lt;p class="text-center font-bold text-primary"&gt;Styled text&lt;/p&gt;</code>
            </div>
        </section>

        <!-- Responsive Section -->
        <section class="demo-section">
            <h2 class="section-title">Responsive Design</h2>
            
            <div class="card">
                <div class="card-body">
                    <p>This theme is fully responsive. Resize your browser to see how components adapt to different screen sizes:</p>
                    <ul style="margin-top: 1rem; margin-left: 2rem;">
                        <li>Mobile: &lt; 768px</li>
                        <li>Tablet: 768px - 1024px</li>
                        <li>Desktop: &gt; 1024px</li>
                    </ul>
                </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" style="margin-top: 2rem;">
                <div class="card">
                    <div class="card-body">
                        <h3>📱 Mobile</h3>
                        <p>Stacks vertically on mobile devices</p>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <h3>💻 Tablet</h3>
                        <p>2 columns on tablets</p>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <h3>🖥️ Desktop</h3>
                        <p>3 columns on desktop</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Color Palette Section -->
        <section class="demo-section">
            <h2 class="section-title">Color Palette</h2>
            
            <h3>Primary Colors</h3>
            <div class="component-grid">
                <div class="color-swatch" style="background-color: var(--color-primary-500, #3b82f6);">Primary</div>
                <div class="color-swatch" style="background-color: var(--color-secondary-500, #8b5cf6);">Secondary</div>
                <div class="color-swatch" style="background-color: var(--color-accent-500, #f59e0b);">Accent</div>
            </div>
            
            <h3>Semantic Colors</h3>
            <div class="component-grid">
                <div class="color-swatch" style="background-color: var(--color-success-500, #10b981);">Success</div>
                <div class="color-swatch" style="background-color: var(--color-warning-500, #f59e0b);">Warning</div>
                <div class="color-swatch" style="background-color: var(--color-error-500, #ef4444);">Error</div>
                <div class="color-swatch" style="background-color: var(--color-info-500, #3b82f6);">Info</div>
            </div>
            
            <h3>Gray Scale</h3>
            <div class="grid grid-cols-5 gap-2">
                <div class="color-swatch" style="background-color: var(--color-gray-100, #f3f4f6); color: #000;">100</div>
                <div class="color-swatch" style="background-color: var(--color-gray-300, #d1d5db); color: #000;">300</div>
                <div class="color-swatch" style="background-color: var(--color-gray-500, #6b7280);">500</div>
                <div class="color-swatch" style="background-color: var(--color-gray-700, #374151);">700</div>
                <div class="color-swatch" style="background-color: var(--color-gray-900, #111827);">900</div>
            </div>
        </section>

    </div>

    <!-- Footer -->
    <footer style="background: var(--color-gray-900, #111827); color: white; padding: 3rem 0; margin-top: 4rem;">
        <div class="container">
            <div class="text-center">
                <h3 style="color: white; margin-bottom: 1rem;">{self.theme_name}</h3>
                <p style="color: rgba(255, 255, 255, 0.7);">CSS Theme Demo - Generated on {datetime.now().strftime("%B %d, %Y")}</p>
                <p style="color: rgba(255, 255, 255, 0.7); margin-top: 1rem;">
                    Theme file: <code style="background: rgba(255, 255, 255, 0.1); padding: 0.25rem 0.5rem; border-radius: 4px;">{self.css_filename}</code>
                </p>
            </div>
        </div>
    </footer>

    <script>
        // Add basic interactivity
        console.log('Demo page loaded successfully!');
        
        // Example: Form validation
        const form = document.querySelector('form');
        if (form) {{
            form.addEventListener('submit', (e) => {{
                e.preventDefault();
                alert('Form submitted! (Demo only)');
            }});
        }}
        
        // Example: Show keyboard accessibility
        document.body.classList.add('user-is-tabbing');
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Tab') {{
                document.body.classList.add('user-is-tabbing');
            }}
        }});
        document.addEventListener('mousedown', () => {{
            document.body.classList.remove('user-is-tabbing');
        }});
    </script>
</body>
</html>"""
        return html


def select_css_files():
    """Interactive CSS file selection for demo generation"""
    print("╔═══════════════════════════════════════════════════╗")
    print("║   Demo HTML Generator                             ║")
    print("╚═══════════════════════════════════════════════════╝\n")
    
    # Look for CSS files
    search_dirs = ['generated_themes', 'generated_variations', 'improved_css', '.']
    css_files = []
    
    for directory in search_dirs:
        if os.path.exists(directory):
            files = [os.path.join(directory, f) for f in os.listdir(directory) 
                    if f.endswith('.css') and os.path.isfile(os.path.join(directory, f))]
            css_files.extend(files)
    
    if not css_files:
        print("❌ No CSS files found!")
        print("Please generate CSS themes first using css_generator.py\n")
        return None
    
    print(f"Found {len(css_files)} CSS file(s):\n")
    
    for idx, file in enumerate(css_files[:20], 1):
        size = os.path.getsize(file) / 1024
        print(f"  {idx}. {os.path.basename(file)} ({size:.1f} KB)")
    
    if len(css_files) > 20:
        print(f"  ... and {len(css_files) - 20} more files")
    
    print()
    print("Select CSS files to generate demos for:")
    print("  - Enter a number (e.g., 1)")
    print("  - Enter multiple numbers separated by commas (e.g., 1,2,3)")
    print("  - Enter 'all' to generate demos for all files")
    print()
    
    while True:
        try:
            choice = input("Your selection: ").strip().lower()
            
            if choice == 'all':
                return css_files
            
            if ',' in choice:
                indices = [int(x.strip()) for x in choice.split(',')]
                selected = [css_files[i-1] for i in indices if 1 <= i <= len(css_files)]
                if selected:
                    return selected
            else:
                index = int(choice)
                if 1 <= index <= len(css_files):
                    return [css_files[index-1]]
            
            print("Invalid selection. Please try again.\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid numbers.\n")


def main():
    """Main function"""
    selected_files = select_css_files()
    
    if not selected_files:
        return
    
    print(f"\n✅ Selected {len(selected_files)} file(s) for demo generation\n")
    print("=" * 60)
    
    # Create output directory
    output_dir = 'demo_pages'
    os.makedirs(output_dir, exist_ok=True)
    
    generated_demos = []
    
    for css_file in selected_files:
        print(f"\n📁 Generating demo for: {os.path.basename(css_file)}")
        
        try:
            # Generate demo HTML
            generator = DemoHTMLGenerator(css_file)
            html_content = generator.generate_demo_html()
            
            # Create output filename
            base_name = os.path.splitext(os.path.basename(css_file))[0]
            html_filename = os.path.join(output_dir, f"{base_name}-demo.html")
            
            # Copy CSS file to demo directory
            css_dest = os.path.join(output_dir, os.path.basename(css_file))
            if os.path.abspath(css_file) != os.path.abspath(css_dest):
                import shutil
                shutil.copy2(css_file, css_dest)
            
            # Write HTML file
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            generated_demos.append(html_filename)
            print(f"   ✅ Demo saved: {html_filename}")
            print(f"   📄 Theme: {generator.theme_name}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Generate index page
    if generated_demos:
        print(f"\n📝 Generating index page...")
        index_html = generate_index_page(generated_demos)
        index_file = os.path.join(output_dir, 'index.html')
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_html)
        print(f"   ✅ Index page saved: {index_file}")
    
    # Summary
    print("\n" + "=" * 60)
    print("╔═══════════════════════════════════════════════════╗")
    print("║  ✅ DEMO GENERATION COMPLETE!                     ║")
    print("╚═══════════════════════════════════════════════════╝\n")
    print(f"📦 Generated: {len(generated_demos)} demo page(s)")
    print(f"📁 Location: {output_dir}/\n")
    print("🌐 To view your demos:")
    print(f"   1. Open {output_dir}/index.html in your browser")
    print(f"   2. Or open individual demo HTML files\n")
    print("✨ Each demo showcases:")
    print("   • Typography styles")
    print("   • All button variants")
    print("   • Card components")
    print("   • Form elements")
    print("   • Navigation components")
    print("   • Tables and grids")
    print("   • Color palette")
    print("   • Utility classes")
    print("   • Responsive design\n")


def generate_index_page(demo_files):
    """Generate an index page linking to all demos"""
    demos_html = ""
    for demo_file in demo_files:
        filename = os.path.basename(demo_file)
        name = filename.replace('-demo.html', '').replace('-', ' ').title()
        demos_html += f"""
        <div class="demo-card">
            <h3>{name}</h3>
            <p>View the complete component showcase for this theme</p>
            <a href="{filename}" class="demo-link">View Demo →</a>
        </div>
"""
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Theme Demos - Index</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            color: white;
            margin-bottom: 3rem;
        }}
        
        .header h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        
        .header p {{
            font-size: 1.25rem;
            opacity: 0.9;
        }}
        
        .demo-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }}
        
        .demo-card {{
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .demo-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }}
        
        .demo-card h3 {{
            color: #667eea;
            margin-bottom: 0.5rem;
            font-size: 1.5rem;
        }}
        
        .demo-card p {{
            color: #666;
            margin-bottom: 1.5rem;
        }}
        
        .demo-link {{
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: transform 0.2s ease;
        }}
        
        .demo-link:hover {{
            transform: scale(1.05);
        }}
        
        .footer {{
            text-align: center;
            color: white;
            margin-top: 4rem;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎨 CSS Theme Demos</h1>
            <p>Explore your generated CSS themes with complete component showcases</p>
            <p style="font-size: 1rem; margin-top: 1rem;">Generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</p>
        </div>
        
        <div class="demo-grid">
            {demos_html}
        </div>
        
        <div class="footer">
            <p>Click any card to view the full demo with all components</p>
        </div>
    </div>
</body>
</html>"""
    return html


if __name__ == "__main__":
    main()
