![Open Graph, Homepage (2) (1)](https://github.com/basehub-ai/marketing-website-template/assets/40034115/e8566293-9c58-4467-a4c7-7a700eea10c8)

[BaseHub Templates](https://basehub.com/templates) are production-ready website templates, powered by BaseHub.

# Marketing Website Template

[![Use template](https://basehub.com/template-button.svg)](https://basehub.com/basehub/marketing-website)

Fully featured marketing website.

- 🔸 Perfect for startups and indie hackers looking to showcase their SaaS
- 🔸 Fully editable from BaseHub
- 🔸 Comes with Search, Dark/Light Mode, Analytics, and more
- 🔸 Requires just a BaseHub account and a deployment platform—no other service

## Stack

- Next.js
- BaseHub
- Tailwind CSS

## One Click Deployment

[![Deploy with Vercel](https://vercel.com/button)]([](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fbasehub-ai%2Fmarketing-website-template&integration-ids=oac_xwgyJe0UwFLtsKIvIScYh0rY&env=&demo-url=https%3A%2F%2Fnextjs-marketing-website.basehub.com%2F&demo-description=Introducing%20the%20%E2%80%9CCMS%20Marketing%20Website%20Template%E2%80%9D%20by%20BaseHub%E2%80%94a%20sleek%2C%20modern%2C%20and%20fully%20responsive%20solution%20for%20your%20marketing%20needs.%20This%20template%20is%20designed%20to%20empower%20businesses%20with%20an%20intuitive%2C%20easy-to-navigate%20interface%20that%20seamlessly%20integrates%20with%20any%20CMS%20platform.%0A%0AKey%20Features%3A%0A%0A%09%E2%80%A2%09Responsive%20Design%3A%20Ensures%20optimal%20viewing%20experience%20across%20all%20devices%2C%20from%20desktops%20to%20smartphones.%0A%09%E2%80%A2%09Customizable%20Layouts%3A%20Offers%20flexible%20and%20dynamic%20layout%20options%20to%20suit%20various%20content%20needs%20and%20styles.%0A%09%E2%80%A2%09SEO%20Friendly%3A%20Built%20with%20SEO%20best%20practices%20in%20mind%20to%20improve%20your%20search%20engine%20rankings%20and%20drive%20organic%20traffic.%0A%09%E2%80%A2%09Blog%20and%20Changelog%3A%20Blog%20and%20changelog%20integrated%20to%20have%20a%20nice%20experience.%0A%09%E2%80%A2%09Integrated%20Analytics%3A%20Easy%20integration%20with%20popular%20analytics%20tools%20to%20track%20and%20analyze%20website%20performance.%0A%09%E2%80%A2%09Social%20Media%20Integration%3A%20Connect%20and%20engage%20with%20your%20audience%20through%20seamless%20social%20media%20integration.%0A%09%E2%80%A2%09Text%20based%20Search%3A%20Out%20of%20the%20box%20integrated%20search%20with%20BaseHub%0A%0AWhether%20you%20are%20launching%20a%20new%20product%2C%20promoting%20a%20service%2C%20or%20building%20brand%20awareness%2C%20the%20%E2%80%9CCMS%20Marketing%20Website%20Template%22%20will%20fits%20perfectly.&demo-image=https%3A%2F%2Fbasehub.earth%2Ffa068a12%2FuK8Uaibmc32TOGypkLvBu%2Freadme-(2).png&external-id=mly6i259eym3jkyvq6txyciu%3AViwfZNGQgCUccNVudPIns))

_You can deploy this anywhere. Vercel works nicely and with one click._

## Local Development

**Install dependencies**
\`\`\`bash
pnpm i
\`\`\`

**Add your BASEHUB_TOKEN to `.env.local`**
\`\`\`txt
# .env.local

BASEHUB_TOKEN="<get-it-from-your-basehub-repo>"
\`\`\`

**Start the dev server**
\`\`\`bash
pnpm dev
\`\`\`

# 🎓 Beautiful Timetable Viewer

A stunning, modern web application for viewing academic timetables with an incredibly beautiful and interactive frontend.

## ✨ Features

- **Gorgeous UI**: Glassmorphism design with animated gradients and floating particles
- **Responsive Design**: Perfect on all devices from mobile to desktop
- **Interactive Elements**: Smooth animations, hover effects, and micro-interactions
- **Real-time Statistics**: Live counters showing classes, days, subjects, and teachers
- **Beautiful PDFs**: Professionally styled PDF downloads
- **Modern Tech Stack**: Flask backend with pandas for data processing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- wkhtmltopdf (for PDF generation)

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone <repository-url>
   cd timetable-viewer
   \`\`\`

2. **Install Python dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Install wkhtmltopdf**
   
   **Ubuntu/Debian:**
   \`\`\`bash
   sudo apt-get install wkhtmltopdf
   \`\`\`
   
   **macOS:**
   \`\`\`bash
   brew install wkhtmltopdf
   \`\`\`
   
   **Windows:**
   Download from: https://wkhtmltopdf.org/downloads.html

4. **Run the application**
   \`\`\`bash
   python app.py
   \`\`\`

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

\`\`\`
timetable-viewer/
├── app.py                 # Main Flask application
├── run.py                 # Production runner
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── templates/
│   └── index.html        # Beautiful frontend template
├── data/                 # CSV timetable files
│   ├── 2023/
│   │   ├── batch1.csv
│   │   └── batch2.csv
│   └── 2024/
│       ├── batchA.csv
│       └── batchB.csv
└── README.md
\`\`\`

## 🎨 Design Features

- **Animated Background**: Dynamic gradient with floating particles
- **Glassmorphism**: Modern glass-like UI elements with blur effects
- **Smooth Animations**: CSS transitions and keyframe animations
- **Interactive Statistics**: Real-time counters with smooth number animations
- **Responsive Tables**: Beautiful, mobile-friendly timetable display
- **Custom Icons**: Font Awesome icons with emoji accents
- **Professional Typography**: Inter and JetBrains Mono fonts

## 📊 CSV Format

Your CSV files should follow this structure:

\`\`\`csv
Day,Time,Subject,Room,Teacher
Monday,9:00-10:00,Mathematics,Room 101,Dr. Sarah Johnson
Monday,10:00-11:00,Physics,Lab 201,Prof. Michael Chen
...
\`\`\`

## 🚀 Deployment

### Heroku Deployment

1. **Create a Heroku app**
   \`\`\`bash
   heroku create your-timetable-app
   \`\`\`

2. **Add buildpacks**
   \`\`\`bash
   heroku buildpacks:add --index 1 https://github.com/dscout/wkhtmltopdf-buildpack.git
   heroku buildpacks:add --index 2 heroku/python
   \`\`\`

3. **Deploy**
   \`\`\`bash
   git push heroku main
   \`\`\`

### Other Platforms

The application is compatible with:
- **Vercel**: Use `run.py` as entry point
- **Railway**: Automatic deployment from Git
- **DigitalOcean App Platform**: Configure with `run.py`

## 🎯 API Endpoints

- `GET /` - Main application page
- `GET /timetable/<year>/<batch>` - JSON timetable data
- `GET /download/<year>/<batch>` - PDF download

## 🛠️ Customization

### Colors & Themes
Edit the CSS variables in `templates/index.html`:

\`\`\`css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    /* ... more variables */
}
\`\`\`

### Adding New Data
Simply add CSV files to the `data/<year>/` directory following the required format.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🎉 Acknowledgments

- Beautiful design inspired by modern web trends
- Icons by Font Awesome
- Fonts by Google Fonts
- Built with love and attention to detail

---

**Made with ❤️ for beautiful academic scheduling**
