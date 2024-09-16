# PHYS 250: Computational Physics
Welcome to the University of Chicago PHYS 250 Computational Physics repository!

This repository will hold the Syllabus, Learning Goals, Code Examples, and Lecture Notes for the course. Periodically, some of these materials will be moved to the Canvas page for the course, which for the Autumn 2024 Academic Quarter is located here:

https://canvas.uchicago.edu/courses/58627

## Programming Languages, Software, and Platforms for the course
We will primarily be using Python for this course as it is a common, powerful, and high-levle language that is used across much of academia and industry in one form or another.

### Software

One of the primary "sets" of packages that we will be using is referred to as the "scipy stack"

* https://www.scipy.org/

The reason for this is that it includes these incredibly powerful, ubiquitous, and useful packages:

* `numpy`: http://www.numpy.org/
* `matplotlib`: https://matplotlib.org/
* `IPython`/`Jupyter`: http://ipython.org/
* `pandas`: http://pandas.pydata.org/

### Platform
One of the easiest to use applications for python-based computational physics is Jupyter Notebooks. 

* `Jupyter`:http://jupyter.org/

These are interactive, easy-to-use interfaces that make writing simple and moderately complex software programs enjoyable and straightforward. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.

We also have a platform that provisions (creates, maintains, and hosts) Jupyter Notebook instances on-demand:

* https://ml.maniac.uchicago.edu/

To use this service, you will need an account.

### Git, GitHub
As part of the tools of the trade that you will learn in this course, you will be expected to use the modern versioning system `git` for keeping tracking of your code and turning in homework.

* `git`: https://git-scm.com/

Most people interact with `git` using GitHub (that's this thing you're using now on the web):

* GitHub: https://github.com/

If you are using the J`upyterLab` platform described above, you should have direct access to the example code included in this repository. However, you are not only welcome, but *encouraged* to "fork" this repository directly to your own respository and develop it further

To do this:

1. Fork this repository by clicking on "Fork" button above
1. Clone your fork of the repository to your computer (find repository in your GitHub user profile, and clone it from there)

If there are updates to this repository that you want to get:

1. Check if your repository is in a clean state with `git status`
1. If it is not, you will need to clean it up (more info below)
1. If it is, then make sure you are on your `master` branch with `git branch`

If you aren't in a clean state, you need to check it out with `git checkout master`
Now you are ready to update:
```
git fetch
git merge
```

Now you should have the up-to-date repository.


1. On your computer you should make a new branch if you want to play aroud
```
git branch play
git checkout play
```
now you can make changes without conflicting with the `master` branch.
To save your changes 

There are a huge number of `git` and `GitHub` tutorials out there, but here are a few good ones:

* https://guides.github.com/activities/hello-world/
* https://guides.github.com/introduction/flow
* https://guides.github.com/activities/forking/


To have students complete assignments using forks (note: this setup means that **students will be able to see one another's work**):

### Homework submissions

#### 1. Homework repositories

I will **Create one repository per assignment**. That will include any boilerplate files that you will need to get started.

These will be *private repositories* and there will be one private repository per assignment.

#### 2. Completing assignments

Homework assignments will be distributed via [GitHub Classroom](https://classroom.github.com). 

#### 3. Reviewing assignments

We will then do code review with line-by-line feedback directly within the pull request. For assignments that allow for corrections, you can push fixes up to their forks, which will be reflected in the pull request that I (the professor) will receive.

Since I don't want any solutions in the original assignment repository, I will leave the pull request unmerged. When I am finished giving feedback, I will close the pull request and leave a :+1: (`:+1:`) in a final comment.

