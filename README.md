# SEN122A- Statistical Analysis of Choice Behaviour 2025

## 1. Introduction

Welcome to the *Choice behaviour modelling* section of the SEN112A course repository. In this repository, you will find Jupyter notebooks for the lab sessions, step-by-step instructions for setting up your Python environment, and a discussion forum where you can ask questions related to the course content.
   

## 2. Course description

Mathematical models of choice behaviour –henceforth referred to as "Discrete Choice Models" (DCMs)– are widely used to study the decision-making behaviour of individuals across numerous domains, including transportation, marketing, and health. DCMs are used to infer preferences over attributes and alternatives and predict the impact of new policies.

This course aims to equip students in the socio-technical domain with a comprehensive understanding of DCMs. You will learn the theoretical underpinnings of choice models and gain practical hands-on experience in estimating and applying these models to solve real-world problems.  

The course consists of oral lectures and lab sessions. During the lab sessions, students will work with Python-based tools to estimate models and analyze datasets. Attendance at both the lectures and lab sessions is highly recommended to keep up with the course content, although it is not mandatory.

Below, you can find the dates for the lab sessions and the partial exams:

| **Event**                    | **Date**              | **Time**    |.  *Remarks*  |
|-----------------------       |--------------------   |-------------|--------------|
| Python env support hour      | November 17, 2025     | 09:45-10:45 | *optional*   |
| Lab session 1 (MNL)          | November 17, 2025     | 10:45-12:30 |              |
| Lab session 2 (MXL)          | November 24, 2025     | 10:45-12:30 |              |
| Lab session 3 (ML)           | December 01, 2025     | 10:45-12:30 |              |
| Partial Exam                 | December 08, 2025     | 13:30-15:30 |              |
| Inspection Partial Exam      | December 17, 2026     | 12:45-13:30 | No other opportunity will be offered |
| Resit Partial Exam           | January 16, 2026      | 13:30-15:30 |              |
| Inspection Resit Partial Exam| January 16, 2026      | 11:45-12:30 | No other opportunity will be offered |
| Theoretical Exam             | January 29, 2026      | 09:00-12:00 |              |
| Resit Theoretical Exam       | April 09, 2026        | 09:00-12:00 |              |


Please review the information below carefully.


## Lab sessions
Lab sessions are offered in the form of Jupyter notebooks and aim to demonstrate and reinforce knowledge about discrete choice models, the underlying assumptions, estimation techniques, and how to interpret outcomes. They provide **hands-on** experience in discrete choice modelling, which is essential to master the method. Each lab session comprises two parts: A and B, and include a series of **exercises**.

`Lab session 1` introduces discrete choice models, focusing specifically on the Multinomial Logit (MNL) model based on random utility theory. You will acquire skills to explore choice datasets, build and estimate choice models using specialised Python package called Biogeme, and perform statistical tests to compare different model specifications.

`Lab session 2` focuses on the Mixed Logit models. You will gain proficiency in building and estimating various types of Mixed Logit models by altering assumptions about unobserved preference and taste heterogeneity. Furthermore, you will explore the impact of the number of draws on the estimation outcomes. 

`Lab session 3` focuses on the latest developments in the field: combining discrete choice modelling and machine learning for choice behaviour analysis. You will work with neural networks and explore how they can be integrated within utility-based choice models.   

For the lab sessions, we use Python notebooks (aka Jupyter Notebooks). You have two options to work with them. 
A. Anaconda
B. Pip 
For each option, **instructions** to set up your Python environment are given at the **end of this page**.

If you are **unfamiliar with Python**, we recommend completing **lab session 0**, which provides the necessary tools to conduct the lab sessions. It covers topics such as data structures, utilising external libraries, data exploration, visualisation, etc. 

## Tutorials
Tutorials are supplementary materials, offered to help you deepen your understanding of key concepts in choice modelling. These ([tutorials](https://github.com/SEN1221TUD/Tutorials)) aim to reinforce your understanding of the topics covered. They do not contain exercises, but are part of the SEN122A course material.<br>

Here, you will find tutorials. Tutorials aim to explain concepts that are important to choice modelling. The current list of topics is:

[Tutorial 1](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial1/tutorial1_DGP_and_bias.ipynb): The data generating process and bias <br>
[Tutorial 2](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial2/tutorial2_The_loglikelihood_function.ipynb): The loglikelihood function<br>
[Tutorial 3](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial3/tutorial3_concave_likelihood_MNL.ipynb): The concave likelihood function of the linear-additive RUM-MNL model<br>
[Tutorial 4](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial4/tutorial4_Local_vs_global_maxima.ipynb): Local versus global maxima<br>
[Tutorial 5](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial5/tutorial5_Ignoring_panel_structure.ipynb): The impact of ignoring the panel structure of choice data<br>
[Tutorial 6](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial6/tutorial6_Expected_max_utility.ipynb): The expected maximum utility and the LogSum formula<br>

The list of tutorials may be further extended in the future.

## 4. Q&A forum

We use the [Issues](https://github.com/SEN1221TUD/Q2_2025/issues) section as the Q&A platform of this course (Part 1: Choice Behaviour Modelling). This is where you can post questions related to lecture content, lab sessions, or technical issues with Python. Before you create a new issue, please make sure that the same question hasn’t already been raised by one of your peers. You can also contribute to ongoing discussions by commenting on existing issues to continue the conversation or provide additional insights. As an example, we have already created the first issue; see [Issues](https://github.com/SEN1221TUD/Q2_2025/issues).

To create a new issue (question or problem) in the course repository, follow these steps:

1. Go to the "Issues" section of the course repository.
2. Click on "New issue" in the green button located at the upper right corner of your screen.
3. Add an informative title to your question or problem (e.g., "logit model of BIOGEME does not import in my notebook").
4. Describe your issue clearly and concisely. 
5. Add a topic label from the right-hand side. Click on the gear icon next to "Labels" and choose the label based on the topic of your question. 
6. Click on "Submit new issue" in the green button below the text description.

After that, the lecturer or teaching assistant will reply to your question. Also, you are encouraged to reply to questions posted by your fellow students! If you know how to help your fellow student with an issue, share your thoughts!

## 5. Instructions to set up your workspace

In this section, we will guide you through the configuration of your Python environment for the Choice Behaviour Modelling part of the course. You have to set up your environment once. This environment will work for all lab sessions.

### Setting up Python environment using Anaconda

Anaconda is a popular platform for managing Python environments. It is **strongly** recommended to create a **fresh** environment that uses Python version **3.12.11**.Other versions of Python, such as **3.10, 3.9 or  older**, are known to give some problems. Also, reusing an environment from another course is a recipe for installation troubles.

Step-by-Step Instructions:


#### A. Download the lab session files

1. **Go** to: github.com/SEN1221TUD/Q2_2025

2. **Download the materials**
   - Click the green Code button (top right of the file list)
   - In the dropdown, select Download ZIP
   ![img1](./Assets/A-2.png)

3. **Locate the ZIP file**
   - By default, the file will be saved in Downloads
   - The file is named: Q2_2025-main.zip

4. **Copy to your course folder**
   - Open File Explorer in Windows (or Finder in Mac).
   - Move the ZIP file to a convenient location, e.g. 

5. **Unpack (extract) the ZIP**
   - Right-click the ZIP file → choose **Extract All...**
   - Inside the extracted folder you should see the subfolders **\Lab_sessions\lab_session_01**
      
#### B. Download the requirements.txt file into your Downloads folder 

1. **Go** to: github.com/SEN1221TUD/Q2_2025
   
2. In the file list, click on **requirements.txt**

   ![img2](./Assets/B-2.png)

3. On the top-right of the file view, click the **Download raw file** icon ()

   ![img3](./Assets/B-3.png)

4. The file will be saved to your **Downloads** folder 

5. Check in your **Downloads** folder to confirm the file is there.


#### C. Create an **empty** Python 3.12.11 environment

0. **Install Anaconda**: 
   - Go to the [Anaconda download page](https://docs.anaconda.com/anaconda/install/).
   - Choose the appropriate version and click Download.
   - Run the installer and follow the  instructions.

1. Open **Anaconda Navigator**, then Go to the **Environments**

2. Click **Create:** (bottom left) Do not reuse an old env!!
  
3. Enter a name for yoour environment (e.g., SEN122A)

4. Tick **Python** and **select** version 3.12.11 from the dropdown

5. Click **Create** and wait (be patient)

   ![img4](./Assets/C-5.png)

**IF Python 3.12.11 is Not listed**

1. Open the command line terminal (cmd)

2. Type the following command and press Enter: 
   ```conda create -n py312 python=3.12.11```

   ![img5](./Assets/C2-2.png)

3. After installing, close and restart Anaconda Navigator

#### D. Install the required Python packages

1. In Anaconda Navigator, LEFT-click the green (image of button) button next to the environment name

2. Choose **Open Terminal**

3. In the terminal, go to your downloads folder:
   ``cd Downloads``

   ![img6](./Assets/D-3.png) 

4. Install the required packages by typing:
   ``pip install –r requirements.txt``

5. Wait until the installation is finished (be patient)

6. Close the terminal


#### E. Install and launch Jupyter Notebook

1. Go to **Home** (top left)

2. In the dropdown at the top, select the created environment (e.g. SEN122A_2025)

   ![img7](./Assets/E-2.png) 

3. Scroll through the list or use the search bar to find Jupyter Notebook

4. Click **Install** (be patient)

5. When the installation is complete, the button will change from **Install** → **Launch**.

6. Click **Launch** to start Jupyter by double-clicking the launch button


#### F. Start your lab session

1. After launching **Jupyter Notebook**, a new browser tab will open automatically.

2. In the Jupyter file browser, **navigate to the course folder** where you unpacked the materials (e.g. Documents\Courses\SEN122A\Q2_2025-main\Lab_sessions).

3. Locate the lab notebook you want to work on (file ending in .ipynb).

4. **Double-click** the file to open it in a new tab.

5. You can now start running the notebook cells.

   ![img8](./Assets/F-4.png) 
   

