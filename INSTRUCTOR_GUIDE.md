# Instructor Guide

This guide is for course instructors managing student project submissions.

## 📋 Overview

This repository is set up to receive student project submissions via pull requests. Each course has its own folder organized by year.

## 🗂️ Repository Organization

```
Student_Projects_Hub/
├── README.md                          # Main documentation for students
├── CONTRIBUTING.md                    # Contribution guidelines
├── PROJECT_TEMPLATE.md               # Project structure template
├── .gitignore                        # Excludes checkpoints, data files
└── [YEAR]/                           # e.g., 2026/
    └── [COURSE_NAME]/                # e.g., Python_for_Data_Analytics_II/
        ├── README.md                 # Course-specific guidelines
        └── [student_name]/           # e.g., john_doe/
            └── project.ipynb         # Student's Jupyter notebook
```

## 👨‍🏫 Managing Student Submissions

### Reviewing Pull Requests

When a student submits a pull request:

1. **Check PR Details**
   - Verify the PR title and description are clear
   - Ensure they're submitting to the correct course folder
   - Confirm they're only adding files in their own folder

2. **Review the Notebook**
   - Open the `.ipynb` file in the PR
   - Check that the code runs (look for obvious errors)
   - Verify the notebook includes:
     - Student name and project title
     - Clear documentation
     - Visualizations
     - Conclusions

3. **Provide Feedback**
   - Use PR comments to provide feedback
   - Request changes if needed
   - Be specific about what needs improvement

4. **Merge or Request Changes**
   - If satisfactory, approve and merge the PR
   - If changes needed, request changes with clear instructions
   - Once revised, merge the PR

### Common Issues to Check

- ✅ Files are in correct folder: `[year]/[course]/[student_name]/`
- ✅ No large data files (> 10MB)
- ✅ No modifications to other students' work
- ✅ Notebook has proper structure and documentation
- ✅ All code cells can run without errors
- ✅ No sensitive or proprietary information

### Managing Merge Conflicts

If a student's PR has conflicts:
1. Add a comment explaining the conflict
2. Ask them to:
   - Pull the latest changes from the main repository
   - Resolve conflicts in their fork
   - Push the updates (PR will auto-update)

## 📁 Adding New Courses

To add a new course:

1. Create the course folder:
   ```bash
   mkdir -p [YEAR]/[New_Course_Name]
   ```

2. Create a README for the course:
   - Copy from an existing course README
   - Update course-specific information
   - Include learning objectives and guidelines

3. Update the main README.md:
   - Add the course to the "Available Courses" section

4. Commit and push changes

## 📊 Tracking Student Progress

### Viewing All Submissions

```bash
# List all students in a course
ls 2026/Python_for_Data_Analytics_II/

# Count submissions per course
find 2026/Python_for_Data_Analytics_II/ -name "*.ipynb" | wc -l
```

### Creating a Student Roster

You can create a simple script to list all students:

```bash
#!/bin/bash
echo "Students in Python for Data Analytics II (2026):"
for dir in 2026/Python_for_Data_Analytics_II/*/; do
    if [ -d "$dir" ]; then
        basename "$dir"
    fi
done
```

## 🌐 Building a Website (Future)

The repository is structured to support automatic website generation:

1. **Static Site Generator**: Use tools like Jekyll, Hugo, or MkDocs
2. **GitHub Pages**: Enable GitHub Pages in repository settings
3. **Automation**: Set up GitHub Actions to rebuild on each merge
4. **Student Gallery**: Display projects with previews and links

Example structure:
- Homepage: List of courses
- Course page: List of student projects
- Project page: Rendered notebook or link to view

### Recommended Tools
- **nbconvert**: Convert Jupyter notebooks to HTML
- **GitHub Pages**: Free hosting
- **GitHub Actions**: Automatic deployment on PR merge

## 🔒 Repository Settings

### Recommended Settings

1. **Branch Protection** (for main branch):
   - Require pull request reviews before merging
   - Require status checks to pass (optional)
   - Prevent force pushes
   
2. **Merge Settings**:
   - Allow squash merging (recommended)
   - Delete head branches automatically after merge

3. **Issues**:
   - Enable issues for student questions
   - Create issue templates for common questions

### Collaborator Access

- Students: No direct write access (PR only)
- Teaching Assistants: Write access (can review PRs)
- Instructors: Admin access

## 📧 Communication Templates

### PR Approval Comment
```
Great work, [Student Name]! Your project is well-documented and demonstrates good understanding of [concepts]. Merging now. ✅
```

### Requesting Changes
```
Hi [Student Name], thanks for your submission! Before I can merge this, please address:
1. [Specific issue 1]
2. [Specific issue 2]

Please make these changes and push updates to your branch. The PR will update automatically.
```

### Common Student Questions

**Q: How do I update my PR?**
A: Make changes in your forked repository and commit. The PR updates automatically.

**Q: My PR has conflicts. What do I do?**
A: You need to sync your fork with the main repository. See [this guide](link).

**Q: Can I submit multiple projects?**
A: Yes! Put each project in a separate file in your folder, or create a new PR.

## 📈 Best Practices

1. **Regular Reviews**: Review PRs within 1-2 days to maintain momentum
2. **Consistent Feedback**: Use similar standards for all students
3. **Encourage Iteration**: Students can improve and resubmit
4. **Showcase Excellence**: Highlight exceptional projects as examples
5. **Keep Structure Clean**: Ensure students follow folder conventions
6. **Backup Important Work**: Periodically backup the repository

## 🛠️ Automation Ideas

### GitHub Actions Workflows

1. **Notebook Validation**
   - Check that .ipynb files are valid JSON
   - Ensure notebooks can be executed

2. **Auto-labeling**
   - Auto-label PRs by course
   - Label by status (needs-review, approved, etc.)

3. **Website Deployment**
   - Convert notebooks to HTML
   - Deploy to GitHub Pages
   - Update project gallery

## 📞 Support

For technical issues with the repository:
- Check GitHub documentation
- Contact GitHub support
- Consult with IT/technical staff

---

**Happy Teaching! 🎓**
