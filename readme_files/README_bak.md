# CSS Theme Generator

A powerful Python script that generates professional, fully responsive CSS themes with both light and dark variants. Each generation produces unique designs with different color schemes, typography, spacing, and styles.

## 🌟 Features

### Responsive Design
- **Mobile-first approach** - Optimized for all screen sizes
- **Multiple breakpoints** - Support for phones, tablets, and desktops
- **Fluid layouts** - Flexible grid and flexbox systems
- **Adaptive components** - Components that work seamlessly across devices

### Modern CSS
- **CSS Custom Properties** - Easy theme customization through variables
- **Modern layout systems** - Grid and Flexbox
- **Smooth animations** - Performant transitions and keyframe animations
- **Modern selectors** - :focus-visible, :not(), and more

### Comprehensive Components
- Buttons (primary, secondary, outline, ghost)
- Cards with hover effects
- Forms (inputs, textareas, selects, checkboxes)
- Navigation (navbar, nav links, breadcrumbs)
- Alerts and badges
- Modals and dropdowns
- Tables with hover states
- Pagination
- Progress bars and spinners
- Tooltips

### Utility Classes
- Spacing utilities (margin, padding)
- Typography utilities (sizes, weights, alignment)
- Color utilities (text, background)
- Layout utilities (display, position, flexbox, grid)
- Border and shadow utilities
- Transition and animation utilities

### Theme Variations
- **Light theme** - Clean, bright design perfect for daytime use
- **Dark theme** - Eye-friendly dark mode for low-light environments
- **Randomization** - Each generation creates unique:
  - Color palettes (harmonious, complementary colors)
  - Typography systems (font stacks, scale ratios)
  - Spacing scales
  - Border styles
  - Shadow intensities
  - Animation preferences

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🚀 Installation

1. Clone or download this repository
2. Make sure you have Python 3.6+ installed
3. That's it! No additional packages needed.

## 💻 Usage

### Basic Usage

Run the script from your terminal:

```bash
python css_generator.py
```

This will generate two CSS files in the `generated_themes` directory:
- `theme-light-YYYYMMDD_HHMMSS.css` - Light theme
- `theme-dark-YYYYMMDD_HHMMSS.css` - Dark theme

### Using in Your Project

1. **Copy the generated CSS file** to your project directory
2. **Link it in your HTML**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Project</title>
    <!-- Light theme -->
    <link rel="stylesheet" href="theme-light-20250101_120000.css">
</head>
<body>
    <!-- Your content here -->
</body>
</html>
```

3. **For theme switching**, you can dynamically load themes:

```html
<link rel="stylesheet" id="theme-stylesheet" href="theme-light-20250101_120000.css">

<script>
function switchTheme(theme) {
    const stylesheet = document.getElementById('theme-stylesheet');
    if (theme === 'dark') {
        stylesheet.href = 'theme-dark-20250101_120000.css';
    } else {
        stylesheet.href = 'theme-light-20250101_120000.css';
    }
}
</script>
```

## 📱 Responsive Breakpoints

The generated CSS includes the following breakpoints:

| Breakpoint | Max Width | Target Devices |
|------------|-----------|----------------|
| Small (sm) | 480px | Mobile phones |
| Medium (md) | 768px | Tablets |
| Large (lg) | 1024px | Small laptops |
| Default | 1200px+ | Desktops |

### Responsive Classes

Use responsive modifiers to change styles at different breakpoints:

```html
<!-- Hidden on mobile, visible on tablet and up -->
<div class="sm:hidden md:block">...</div>

<!-- Full width on mobile, half width on tablet -->
<div class="w-full md:w-1-2">...</div>

<!-- Column layout on mobile, row on desktop -->
<div class="flex flex-col md:flex-row">...</div>
```

## 🎨 Component Examples

### Buttons

```html
<button class="btn btn-primary">Primary Button</button>
<button class="btn btn-secondary">Secondary Button</button>
<button class="btn btn-outline">Outline Button</button>
<button class="btn btn-ghost">Ghost Button</button>
<button class="btn btn-primary btn-sm">Small Button</button>
<button class="btn btn-primary btn-lg">Large Button</button>
```

### Cards

```html
<div class="card">
    <div class="card-header">
        <h3 class="card-title">Card Title</h3>
    </div>
    <div class="card-body">
        <p>Card content goes here...</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-primary">Action</button>
    </div>
</div>
```

### Forms

```html
<form>
    <div class="form-group">
        <label class="form-label" for="email">Email</label>
        <input type="email" id="email" class="form-input" placeholder="Enter your email">
        <span class="form-help">We'll never share your email.</span>
    </div>
    
    <div class="form-group">
        <label class="form-label" for="message">Message</label>
        <textarea id="message" class="form-textarea" placeholder="Your message"></textarea>
    </div>
    
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### Grid Layout

```html
<div class="container">
    <div class="grid grid-cols-3 gap-4">
        <div class="card">Column 1</div>
        <div class="card">Column 2</div>
        <div class="card">Column 3</div>
    </div>
</div>
```

### Navigation

```html
<nav class="navbar">
    <a href="#" class="navbar-brand">Brand</a>
    <ul class="navbar-nav">
        <li><a href="#" class="nav-link active">Home</a></li>
        <li><a href="#" class="nav-link">About</a></li>
        <li><a href="#" class="nav-link">Contact</a></li>
    </ul>
</nav>
```

## 🎯 Customization

### CSS Variables

All themes use CSS custom properties (variables) for easy customization. You can override these in your own CSS:

```css
:root {
    /* Override primary color */
    --color-primary-600: #your-color;
    
    /* Override font family */
    --font-base: 'Your Font', sans-serif;
    
    /* Override spacing */
    --space-4: 20px;
    
    /* Override border radius */
    --radius-md: 12px;
}
```

### Generating Multiple Themes

Run the script multiple times to generate different themes:

```bash
python css_generator.py  # Run 1 - Theme A
python css_generator.py  # Run 2 - Theme B
python css_generator.py  # Run 3 - Theme C
```

Each run creates a completely different design with unique:
- Color schemes
- Typography
- Spacing systems
- Border styles
- Shadows

## 🔧 Advanced Features

### Print Styles

The generated CSS includes print-optimized styles that automatically apply when users print your pages.

### Accessibility

- Focus visible states for keyboard navigation
- Proper semantic HTML support
- Screen reader-only utilities (.sr-only)
- Reduced motion support for users who prefer minimal animations

### Performance

- Mobile-first approach (loads faster on mobile)
- Minimal CSS reset (only what's necessary)
- Optimized selectors
- Hardware-accelerated animations

## 📦 File Structure

After running the generator:

```
your-project/
├── css_generator.py
├── README.md
├── TODO.md
└── generated_themes/
    ├── theme-light-20250101_120000.css
    ├── theme-dark-20250101_120000.css
    ├── theme-light-20250102_143000.css
    └── theme-dark-20250102_143000.css
```

## 🐛 Troubleshooting

### Theme not applying correctly

1. Make sure the CSS file is properly linked in your HTML
2. Check browser console for any errors
3. Ensure viewport meta tag is present: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

### Components not styling properly

1. Verify you're using the correct class names
2. Check if there are conflicting styles from other CSS files
3. Make sure the CSS file is loaded after any CSS reset

### Responsive breakpoints not working

1. Confirm viewport meta tag is present
2. Test on actual devices or browser dev tools
3. Check if any parent elements have fixed widths

## 🤝 Contributing

Feel free to modify the generator script to add:
- More color schemes
- Additional components
- Custom breakpoints
- Different animation styles
- New utility classes

## 📄 License

This project is free to use for personal and commercial projects.

## 🙏 Credits

Created with ❤️ using Python's standard library.

## 📞 Support

If you encounter any issues or have questions:
1. Check the TODO.md file for known issues
2. Review the generated CSS comments for guidance
3. Experiment with different generations to find the perfect theme

---

**Happy styling! 🎨**

Generated CSS files are production-ready and optimized for modern browsers (Chrome, Firefox, Safari, Edge).
