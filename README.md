# Student Projects Hub 🎓

Welcome to the Student Projects Hub! This repository is a central location for students to submit their course projects and showcase their work.

## 📚 Repository Structure

Projects are organized by **year** and **course**:

```
Student_Projects_Hub/
├── 2026/
│   ├── Python_for_Data_Analytics_II/
│   │   ├── README.md
│   │   └── [student_name]/
│   │       └── project_name.ipynb
│   └── Data_Analysis_using_Python/
│       ├── README.md
│       └── [student_name]/
│           └── project_name.ipynb
└── [future_years]/
    └── [future_courses]/
```

## 🎯 Available Courses

### 2026
- **Python for Data Analytics II**
- **Data Analysis using Python**

## 📝 How to Submit Your Project

This is a step-by-step guide for students who are new to GitHub and pull requests.

### Prerequisites
- A GitHub account (create one at https://github.com/signup if you don't have one)
- Your project file (Jupyter notebook `.ipynb` file)

### Step-by-Step Instructions

#### Step 1: Fork the Repository
1. Navigate to the main repository: [Student_Projects_Hub](https://github.com/chandraveshchaudhari/Student_Projects_Hub)
2. Click the **Fork** button in the top-right corner of the page
3. This creates a copy of the repository in your own GitHub account

#### Step 2: Navigate to Your Course Folder
1. In your forked repository, navigate to the appropriate year and course folder
   - Example: `2026/Python_for_Data_Analytics_II/` or `2026/Data_Analysis_using_Python/`

#### Step 3: Create Your Project Folder
1. Click on **Add file** → **Create new file**
2. In the file name field, type: `your_name/your_project_name.ipynb`
   - Replace `your_name` with your actual name (use underscores instead of spaces)
   - Replace `your_project_name` with your project's name
   - Example: `john_doe/sales_analysis.ipynb`
3. This will automatically create a folder with your name

#### Step 4: Upload Your Jupyter Notebook
1. You can either:
   - **Option A**: Copy and paste your notebook content directly into the file
   - **Option B**: Use **Add file** → **Upload files** to upload your `.ipynb` file
2. Make sure your file is in your personal folder: `2026/[Course_Name]/your_name/`

#### Step 5: Commit Your Changes
1. Scroll down to the **Commit changes** section
2. Add a commit message, for example: "Add [Your Name]'s [Project Name]"
3. Add a description (optional): "Submitted project for [Course Name]"
4. Select **Commit directly to the main branch**
5. Click **Commit changes**

#### Step 6: Create a Pull Request
1. Go back to the main page of your forked repository
2. Click on **Contribute** → **Open pull request**
3. You'll see a comparison between your fork and the original repository
4. Click **Create pull request**
5. Fill in the pull request details:
   - **Title**: "Add [Your Name]'s [Project Name] - [Course Name]"
   - **Description**: Briefly describe your project
   - Example:
     ```
     **Student Name**: John Doe
     **Course**: Python for Data Analytics II
     **Project**: Sales Data Analysis
     **Description**: Analysis of retail sales data using pandas and visualization libraries.
     ```
6. Click **Create pull request**

#### Step 7: Wait for Review
- Your instructor will review your pull request
- You may receive feedback or requests for changes
- Once approved, your project will be merged into the main repository!

## 📋 Project Guidelines

### File Naming Convention
- Use your name for the folder: `firstname_lastname/`
- Use descriptive names for your project: `descriptive_project_name.ipynb`
- Avoid spaces; use underscores instead

### Project Requirements
- All code should be in Jupyter Notebook format (`.ipynb`)
- Include comments and markdown cells to explain your work
- Make sure all cells run without errors
- Include a brief introduction in the first markdown cell:
  - Your name
  - Project title
  - Project objective
  - Dataset information (if applicable)

### Best Practices
- ✅ Test your notebook before submitting (run all cells)
- ✅ Remove unnecessary output or large data files
- ✅ Include visualizations and insights
- ✅ Write clear comments and documentation
- ✅ Use meaningful variable names
- ❌ Don't include large dataset files (> 10MB)
- ❌ Don't modify other students' projects

## 🆘 Getting Help

### Common Issues

**Q: I can't create a pull request**
- Make sure you've forked the repository first
- Ensure you've committed your changes to your fork
- Check that you're creating a pull request from your fork to the original repository

**Q: My notebook file is too large**
- Remove unnecessary output cells
- Don't include large datasets in the repository
- Consider using `.gitignore` to exclude data files

**Q: I need to update my submitted project**
- Make changes in your forked repository
- Commit the changes
- The pull request will automatically update

**Q: I get merge conflicts**
- Contact your instructor for assistance
- Make sure you're only modifying files in your own folder

### Contact
If you need help, please:
- Open an issue in this repository, or
- Contact your course instructor

## 🏆 Showcase
Once your pull request is approved, your project will be visible on this repository, showcasing your work to peers and potential employers!

## 🌐 Auto-generated showcase website

This repository includes a GitHub Actions workflow that automatically builds a static website from student Jupyter notebooks and deploys it to GitHub Pages.

How it works:
- A CI job runs on push to `main` (or `initial_setup`) — merging a student's PR into `main` will trigger a site rebuild automatically.
- `scripts/build_site.py` converts each `.ipynb` into an HTML page and generates a central `index.html`.
- Projects are grouped by course → student; each student's projects and filenames are shown on the main page. The builder reads the first markdown cell of each notebook as the dataset name and displays it on the project card.
- The site is deployed to the `gh-pages` branch using the Actions `peaceiris/actions-gh-pages` action.

Preview the generated site at: https://<your-github-username>.github.io/Student_Projects_Hub (enable Pages in repo settings if not already enabled)

Developers: to preview locally run:

```bash
python -m pip install -r requirements.txt
python scripts/build_site.py
# open site/index.html in your browser
```


---

**Happy Coding! 💻✨**