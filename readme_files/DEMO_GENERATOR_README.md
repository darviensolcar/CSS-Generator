# Demo HTML Generator

A powerful Python tool that automatically generates beautiful, comprehensive demo HTML pages showcasing all components and features of your CSS themes.

## 🎯 What It Does

Creates **production-ready demo pages** that showcase:
- ✅ Complete component library
- ✅ Typography samples
- ✅ Interactive elements
- ✅ Color palettes
- ✅ Responsive behavior
- ✅ Form examples
- ✅ Navigation patterns
- ✅ Utility classes

## 🌟 Key Features

### 📱 **Fully Responsive**
- Mobile-first design
- Adapts to all screen sizes
- Touch-friendly interactions

### 🎨 **Complete Showcase**
- Typography (H1-H6, paragraphs, blockquotes)
- Buttons (all variants and sizes)
- Cards (multiple layouts)
- Forms (inputs, textareas, selects, checkboxes)
- Alerts & Badges
- Navigation (navbar, tabs)
- Tables
- Grid system examples
- Color palette display
- Utility classes

### 🚀 **Easy to Use**
- Interactive file selection
- Automatic CSS file copying
- Index page generation
- Opens directly in browser

### 📦 **Multiple Demos**
- Generate demos for single or multiple themes
- Index page links all demos together
- Each demo is self-contained

## 📋 Requirements

- Python 3.6 or higher
- CSS theme files (from css_generator.py)
- No external dependencies!

## 💻 Usage

### Basic Usage

```bash
python generate_demo.py
```

### Interactive Selection

The script will show all available CSS files:

```
╔═══════════════════════════════════════════════════╗
║   Demo HTML Generator                             ║
╚═══════════════════════════════════════════════════╝

Found 14 CSS file(s):

  1. theme-light-20251231_123635.css (43.1 KB)
  2. desert-vision-dark-20251231_125343.css (43.1 KB)
  3. modern-zephyr-light-20251231_125347.css (43.2 KB)
  ...

Select CSS files to generate demos for:
  - Enter a number (e.g., 1)
  - Enter multiple numbers separated by commas (e.g., 1,2,3)
  - Enter 'all' to generate demos for all files

Your selection:
```

### Selection Options

**Single demo:**
```
Your selection: 1
```

**Multiple demos:**
```
Your selection: 1,3,5
```

**All demos:**
```
Your selection: all
```

### Output

```
✅ Selected 1 file(s) for demo generation

============================================================

📁 Generating demo for: modern-zephyr-light.css
   ✅ Demo saved: demo_pages/modern-zephyr-light-demo.html
   📄 Theme: Modern Zephyr

📝 Generating index page...
   ✅ Index page saved: demo_pages/index.html

============================================================
╔═══════════════════════════════════════════════════╗
║  ✅ DEMO GENERATION COMPLETE!                     ║
╚═══════════════════════════════════════════════════╝

📦 Generated: 1 demo page(s)
📁 Location: demo_pages/

🌐 To view your demos:
   1. Open demo_pages/index.html in your browser
   2. Or open individual demo HTML files
```

## 📁 File Structure

```
your-project/
├── generate_demo.py
├── generated_themes/
│   └── modern-zephyr-light.css
└── demo_pages/
    ├── index.html (📍 Start here!)
    ├── modern-zephyr-light.css (copied)
    ├── modern-zephyr-light-demo.html
    ├── desert-vision-dark.css (copied)
    └── desert-vision-dark-demo.html
```

## 🌐 Viewing Demos

### Method 1: Index Page (Recommended)
1. Open `demo_pages/index.html` in your browser
2. Click on any theme card to view its demo
3. Navigate between demos using browser back button

### Method 2: Direct Access
Open individual demo HTML files directly:
- `demo_pages/theme-name-demo.html`

### Method 3: Local Server (Optional)
```bash
cd demo_pages
python -m http.server 8000
# Open http://localhost:8000 in browser
```

## 📊 What's Included in Each Demo

### 1. **Header Section**
- Theme name display
- Generation date
- Beautiful gradient banner

### 2. **Typography Showcase**
```html
- Headings H1-H6
- Paragraphs (regular, large, small)
- Blockquotes
- Code blocks
- Lists
```

### 3. **Button Components**
```html
- Primary, Secondary, Outline, Ghost
- Small, Medium, Large sizes
- Disabled states
- Hover effects
```

### 4. **Card Components**
```html
- Basic cards
- Cards with headers/footers
- Simple cards
- Hoverable cards
```

### 5. **Form Elements**
```html
- Text inputs
- Email inputs
- Textareas
- Select dropdowns
- Checkboxes
- Labels and help text
- Submit buttons
```

### 6. **Alerts & Badges**
```html
- Success alerts
- Warning alerts
- Error alerts
- Info alerts
- Colored badges
```

### 7. **Navigation**
```html
- Navbar with brand
- Navigation tabs
- Active states
- Hover effects
```

### 8. **Tables**
```html
- Header rows
- Data rows
- Hover effects
- Badge integration
```

### 9. **Grid System**
```html
- 3-column grids
- 4-column grids
- 12-column system
- Responsive behavior
```

### 10. **Color Palette**
```html
- Primary colors
- Secondary colors
- Semantic colors (success, warning, error, info)
- Gray scale
```

### 11. **Utility Classes**
```html
- Text alignment
- Text colors
- Font weights
- Text transforms
- Spacing examples
```

### 12. **Responsive Design**
```html
- Mobile preview
- Tablet preview
- Desktop preview
- Responsive grid examples
```

## 🎨 Customizing Demos

### Modify the Generator

Edit `generate_demo.py` to customize:

```python
# Add custom sections
def generate_demo_html(self):
    html = f"""
    <!-- Add your custom section here -->
    <section class="demo-section">
        <h2 class="section-title">Custom Section</h2>
        <!-- Your content -->
    </section>
    """
```

### Add Custom Components

```python
# Example: Add a pricing table section
<section class="demo-section">
    <h2 class="section-title">Pricing Tables</h2>
    <div class="grid grid-cols-3 gap-4">
        <div class="card">
            <div class="card-body">
                <h3>Basic</h3>
                <p class="text-3xl">$9</p>
                <button class="btn btn-primary">Choose</button>
            </div>
        </div>
        <!-- More pricing tiers -->
    </div>
</section>
```

## 🔧 Integration with Other Tools

### Complete Workflow

```bash
# 1. Generate base themes
python css_generator.py

# 2. Create variations (optional)
python theme_variation_generator.py

# 3. Improve CSS (optional)
python css_improver.py

# 4. Generate demos
python generate_demo.py
```

### Presenting to Clients

1. Generate demos for all themes
2. Open `demo_pages/index.html`
3. Present professionally organized theme options
4. Let clients interact with live components

### Testing Themes

1. Generate demo for your theme
2. Open in multiple browsers
3. Test responsive behavior
4. Check component consistency
5. Verify color accessibility

## 💡 Tips & Best Practices

### 1. Generate Demos Early
```bash
# Generate demos during development
python generate_demo.py
# Review and iterate
```

### 2. Test Across Devices
- Open demos on mobile devices
- Test tablet views
- Check desktop displays
- Verify touch interactions

### 3. Use for Documentation
- Share demo links with team
- Include in project documentation
- Send to clients for approval

### 4. Compare Themes
```bash
# Generate demos for multiple themes
python generate_demo.py
# Select: all
# Compare side-by-side in browser tabs
```

### 5. Check Accessibility
- Test keyboard navigation (Tab key)
- Verify focus indicators
- Check color contrast
- Test with screen readers

## 🎯 Use Cases

### 1. **Client Presentations**
- Professional showcase of theme options
- Interactive components
- Easy theme comparison

### 2. **Team Collaboration**
- Share demos with developers
- Get feedback on designs
- Document component usage

### 3. **QA Testing**
- Test all components systematically
- Verify responsive behavior
- Check browser compatibility

### 4. **Style Guide**
- Use as living style guide
- Reference for developers
- Component documentation

### 5. **Portfolio**
- Showcase your theme designs
- Demonstrate CSS skills
- Present to potential clients

## 📱 Responsive Features

### Mobile (< 768px)
- Single column layouts
- Stacked components
- Touch-optimized buttons
- Mobile navigation patterns

### Tablet (768px - 1024px)
- 2-column grids
- Optimized spacing
- Comfortable touch targets

### Desktop (> 1024px)
- Multi-column layouts
- Full grid systems
- Hover interactions
- Maximum component density

## 🎓 Example Demo Sections

### Typography Example
```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
<p>Body text with proper line height and spacing.</p>
<blockquote>Important quote styled distinctively.</blockquote>
```

### Button Grid Example
```html
<div class="component-grid">
    <button class="btn btn-primary">Primary</button>
    <button class="btn btn-secondary">Secondary</button>
    <button class="btn btn-outline">Outline</button>
    <button class="btn btn-ghost">Ghost</button>
</div>
```

### Card Example
```html
<div class="card">
    <div class="card-header">
        <h3 class="card-title">Card Title</h3>
    </div>
    <div class="card-body">
        <p>Card content goes here</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-primary btn-sm">Action</button>
    </div>
</div>
```

## 🚀 Advanced Features

### Index Page
- Beautiful gradient background
- Grid layout of theme cards
- Hover effects on cards
- Direct links to each demo

### Interactive Elements
- Form submission (demo mode)
- Keyboard navigation support
- Focus indicators
- Hover states

### Professional Design
- Clean, modern layout
- Proper spacing
- Beautiful typography
- Consistent styling

## 🔍 Troubleshooting

### Demo not displaying correctly?
1. Ensure CSS file is in the same directory as HTML
2. Check browser console for errors
3. Verify CSS file path in HTML

### Components look broken?
1. Make sure you're using a complete CSS theme
2. Check if CSS variables are defined
3. Verify class names match your CSS

### Responsive not working?
1. Check viewport meta tag is present
2. Test in browser dev tools
3. Resize browser window slowly

## 📊 Statistics

Each demo includes:
- **20+ component examples**
- **50+ CSS classes demonstrated**
- **10+ responsive breakpoint examples**
- **Full color palette showcase**
- **Typography scale display**

## 🎉 Benefits

✅ **Save Time** - Automatic demo generation
✅ **Professional** - Beautiful, polished demos
✅ **Complete** - All components showcased
✅ **Responsive** - Works on all devices
✅ **Interactive** - Click and explore
✅ **Organized** - Index page for easy navigation
✅ **Self-Contained** - HTML + CSS, no dependencies

## 📚 Resources

- Open demos in browser to see live examples
- View page source to see HTML structure
- Inspect elements to understand CSS classes
- Use as reference for your own projects

---

**Generate beautiful demo pages for your CSS themes in seconds!** 🚀

Perfect for presentations, testing, documentation, and client approvals!
