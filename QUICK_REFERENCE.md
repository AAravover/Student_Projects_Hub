# Quick Reference Guide

## 📁 File Structure

```
Student_Projects_Hub/
├── README.md                          # Main guide for students (start here!)
├── CONTRIBUTING.md                    # Detailed contribution guidelines
├── PROJECT_TEMPLATE.md               # Template for project structure
├── INSTRUCTOR_GUIDE.md               # Guide for instructors
├── .gitignore                        # Git ignore rules
└── 2026/                             # Year folder
    ├── Python_for_Data_Analytics_II/
    │   ├── README.md                 # Course-specific guide
    │   └── .gitkeep.md               # Placeholder
    └── Data_Analysis_using_Python/
        ├── README.md                 # Course-specific guide
        └── .gitkeep.md               # Placeholder
```

## 👨‍🎓 For Students

### First Time?
1. Read [README.md](README.md) - Complete guide with step-by-step PR instructions
2. Check your course folder: `2026/[Your_Course_Name]/README.md`
3. Use [PROJECT_TEMPLATE.md](PROJECT_TEMPLATE.md) as a guide for your notebook

### Submission Checklist
- [ ] Created personal folder: `2026/[Course]/[your_name]/`
- [ ] Uploaded `.ipynb` file with descriptive name
- [ ] Notebook runs without errors
- [ ] Includes title, name, and documentation
- [ ] Created pull request with clear description

### Quick Links
- How to make a pull request: See [README.md](README.md#step-by-step-instructions)
- Project guidelines: See [README.md](README.md#project-guidelines)
- Getting help: See [README.md](README.md#getting-help)

## 👨‍🏫 For Instructors

### Essential Files
- [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) - Complete management guide
- [README.md](README.md) - What students see

### Common Tasks
- Review PR: Check folder location, notebook quality, documentation
- Add course: Create folder, write README, update main README
- Manage conflicts: Guide student to sync fork and resolve

### Quick Commands
```bash
# List students in a course
ls 2026/Python_for_Data_Analytics_II/

# Count submissions
find 2026/Python_for_Data_Analytics_II/ -name "*.ipynb" | wc -l
```

## 📚 Document Purposes

| File | Purpose | Audience |
|------|---------|----------|
| README.md | Main documentation with PR tutorial | Students |
| CONTRIBUTING.md | Detailed contribution guidelines | Students |
| PROJECT_TEMPLATE.md | Notebook structure template | Students |
| INSTRUCTOR_GUIDE.md | Repository management guide | Instructors |
| Course README.md | Course-specific guidelines | Students |

## 🎯 Current Courses (2026)

1. **Python for Data Analytics II**
   - Location: `2026/Python_for_Data_Analytics_II/`
   - Focus: Advanced data manipulation, statistical analysis, visualization

2. **Data Analysis using Python**
   - Location: `2026/Data_Analysis_using_Python/`
   - Focus: Fundamentals of data analysis, EDA, insights

## 🔧 Future Enhancements

- [ ] GitHub Pages website to showcase projects
- [ ] GitHub Actions for notebook validation
- [ ] Automatic labeling of PRs
- [ ] Project gallery/showcase page
- [ ] Additional courses as needed

## 📞 Support

- Students: See [Getting Help](README.md#getting-help) section
- Instructors: See [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)

---

**Last Updated**: February 2026
