# REPORT CARD
  #### Video Demo:  <URL HERE>
  #### Description:
  This is a program that automates the process of making report sheets for students. It was inspired by the fact that long, long hours are being spent in preparing report cards fot student and ranking the students from highest to lowest at the end of each term in the school where I teach. The manual approach is slow,, takes days and sometimes more than a week to complete and it is also error prone. So I decided to try my hands on a **real world** hence, this code.

  The files in this project are:
  * project.py
  * main.py
  * test_project.py
  * README.md

    *project.py*

    This is like the brain of the whole project. It is where all the functions are implemented. It contains two classes viz. grade and student to represent a student's grade and the student's data. The data needed from the students are simply their name, subjects and scores in each subject.
    It contains:
     a get_subject method which prompts for the subjects a student offer and the respective scores they have
     rank students function which ranks the students from highest to lowest
     and many others.

     *main.py* 
     The code is run from this file, it imports the prok=ject file and executes it as appropriate.

    *test_project.py*
    This is where test cases for various functions in the project are written. All the functions have been tested and all passed.

This project, in that it prints output in the command line, challenged my understanding of strings manupulations in python especially when writing test cases. Also I had to read into the pytest documentation to have an in-depth understanding of the framework.

