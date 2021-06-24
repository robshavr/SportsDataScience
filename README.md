# Sports Science goes Open Source: A repositorium for educational resources
In this project we are going to create resources, that will help you to understand and code common analyses in the sport sciences. We will cover a broad range from simple to advanced topics. You are welcome to contribute!

## Current State: Baby Shoes

The first ressources (python notebooks) are available, but still require your feedback to improve! The topics we are going to work on are listed under *Topics*. Feel free to contact us on Discord (https://discord.gg/hn6vFAV6Z2) if you like to collaborate. 

## Guide for newbies
We would advise you to start learning some basic python.
It is not necessary but it gives you a deeper understanding in the language, therefore the modules you'll be using are much easier to understand.
After learning the basics, the next step is to look up the modules:

- Numpy           (important for math)
- Matplotlib      (Helpfull for visualizing the Data)
- Pandas          (Used for reading out the .csv Data)

### Resources to start with
We have gathered some Recourcess to to learn with.
For the basics:
Websites:
- https://www.coursera.org/learn/python-crash-course
- https://www.learnpython.org/

Videos:
- https://www.youtube.com/watch?v=rfscVS0vtbw
- https://www.youtube.com/watch?v=8DvywoWv6fI

GitHub:
- https://github.com/anvinh01/LearningPython 

If you want to skip the basics and move on to Data Analyisis, here is a usefull video: https://www.youtube.com/watch?v=r-uOLxNrNk8

For Module documentation:
- https://numpy.org/
- https://matplotlib.org/
- https://pandas.pydata.org/docs/


### Starting your own project

## Guide for contributors

As Contributor you should first install git from: https://git-scm.com/
For all important commands: https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html

- After the first install. You have to open "Git Bash" and give in your github username and email:<br> 'git config --global user.name "Example Name"' and <br>'git config --global user.email name@example.com'

- Create a directory for our Project.
- press Right Click and open "Git Bash"
- create a connection to our GitHub: "git remote add origin https://github.com/RobShaver21/SportsDataScience.git"
- Pull our project from the github with: "git pull https://github.com/RobShaver21/SportsDataScience.git"
- You can now make changes.
- After you are done type into the git bash: "git add ."
- Then commit: 'git commit -m "text of your changes" '
- At last push in the changes: "git push origin main"

You have succesfully comitted into our GitHub.

## Topics

### Athlete Montitoring 

In many sports, sensor data (e.g. position data from GPS, heart rate, accelerometer) is used to quantify and monitor training load. While there are several possible features to extract from those data, we aimed at automating the workflow from downloading, processing and reporting of those data. We developed scripts and an app in Matlab. The aim is to explain the concepts of the processing and analysis steps in separate notebooks, convert the application to an open-source language like Python and expand the analysis by advanced concepts and smart data visualization.

-	Data from elite athletes (handball, hockey, football)
-	Rebuild a framework for downloading, processing, reporting sensor data from training sessions
   * Monitoring Dashboards (e.g. Ind. Speed Thresholds, Energy Level, heat maps)
   * Build References to past sessions
   * Internal / External Ratio
   * Individualizing Loads (e.g. TRIMP) via mixed models
-	Build a software application with UI


### Deutscher Motorik Test (DMT)

The DMT consists of 8 motor skill tests (e.g. push-ups, jumping, balancing, flexibility) for adolescents. Results are rated based on population reference values. Currently, there is no easy way to compute standardized scores for a larger database. A notebook should show

-	Calculation of standardized scores from absolute values forth and back
-	Automated processing based on one input and a reference table
-	Output for several purposes
   * Dashboard or overview charts for teachers
   * Certificate for adolescents


### Lactate thresholds

Lactate and spirometric values are commonly used in incremental tests to determine performance and derive training recommendations. While the most simple analysis's haven't changed much in the recent 20 to 30 years, we often still rely on proprietary software – which is bad in processing a larger amount of test data. The aim is to create notebooks and a software module that show the basic calculations and aid automation of the analysis accompanied by smart data visualizations. The notebooks are going to be used as an educational tool in Master and Bachelor classes.

-	Automation of current analyses
-	Dashboard, Visualization
-	Advanced concepts 
   * Physiology models (Mader)
   * Mixed models for training zones?


### Basic Analyses

There are other common data analysis tasks in the field of sports science. The aim is to explain them neatly in notebooks. These can later be integrated into a software package or as a module of an integrative software application. Some of these analyses are:

-	Countermovement Jumps on a force plate
-	Center of Pressure on a force plate
-	Combination of both
-	Two or more jumps on a force plate
-	Processing of EMG data


### Gait analysis (Chambers, Sutherland (2002))

Via 3-dimensional kinematic data, it is possible to calculate joint angles and velocities. Involving this method, gait analyses are commonly taught in Bachelor and Master classes. Chambers, Sutherland et al. (2002) provide a comprehensive guide that does not yet involve coding. The aim is to create a comprehensive, understandable notebook that aids teaching of the analyses. 

-	Calculate joint angles
-	Duration and normalization of gate cycles
-	Range of motion



### Data Merging - Wearables and other data

Sensor and user data are generated daily and might help to answer activity- and health-related questions. To develop these analyses and take multiple data sources into account, it is important to understand the analysis process. This project interacts closely with actual research and offers room to explore big data sets, ask data-related questions and answering them by modelling and visualizing.
-	Process large data files (accelerometer, latitude/longitude, electrodermal activity, muscle activity, heart rate (variability))
-	Aggregate and merge with questionnaire data
-	Calculate features (eg, energy, movements)
-	Advance existing software in cooperation with software engineers
-	Possible relationships:
   * Activity ~ well-beeing
   * Electodermal activty ~ stress
   * EMG ~ psychosocial parameters
   * Activity ~ EDA
   * Activity ~ HR(V)

### Framework for sports analyses modules

To make the developed tools (eg, analyses of Lactate Thresholds, CMJ, gait analysis) available for a non-coding population, a modular software with a GUI could implement these. Therefore, the single tools could be condensed to software packages, which build a module consequently

### Energy expenditure in intermittent sports games

The instantenous energy expenditure of intermittent running is modelled via the biomechanical-physiological model of Metabolic Power (Osgnach & di Prampero). However, acyclic actions like jumps, passes or player collisions, side and backward movements are not considered, thus, the modelled energy expenditure underestimates the actual demands. Goals in this research branch are:

- Automatic recognition of movement patterns (eg, passes, shots, jumps, tacklings)
- Improved estimation of energy expenditure, eventually based on recognized pattern
- Further approaches to quantify mechanical load opposed to metabolic requirements (eg, player load, mechanical power, tacklings)

### Health-Navigation portal
- Meta-Database of all health-related activities: prevention/rehabilitation courses, recreational sports, dietary consultance, etc.
   Merge existing data  
   Merge user-generated data  
   Data Mining: anamnesis, evidence - treatment tailorment based on prediction models  




