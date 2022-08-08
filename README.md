# observations-of-the-relationship-between-temperatures-and-precipitation-Italy-1951-2040
<H3>Project made for a university exam</H3>

<H1>INTRODUCTION</H1>
This project aims at the statistical analysis of critical variables affecting the environment such as rainfall and temperatures, observing the measurements made from 1901 to 2020.
The purpose of the analysis of these two variables is to find a correlation that causes changes between them and to observe the forecasts made by models to understand their trend for the next 20 years.
Before entering the project areas, I decided to introduce the key concepts that orbit around it.

<H1>STATISTICAL DATA ANALYSIS</H1>
Statistical analysis can be defined as that set of reasoned steps that allow us to transform data into useful information to better understand the reality that surrounds us and to make decisions more consciously.
The reason why statistical data analysis is so important is related to the need to make different kinds of decisions regarding different measurable phenomena.
Among other things, the measurement and observation of phenomena through statistical analysis is becoming one of the businesses that is most requested by the market, because it allows you to identify any emerging trends or particular conditions in real time.

<H1>DATASET: STARTING BASE FOR ANALYSIS</H1>
What is a dataset? The dataset is a collection of data, more commonly it constitutes a set of data structured in relation form, that is, it corresponds to the content of a single database table, or to a single matrix of statistical data, in which each column of the table represents a particular variable, and each row corresponds to a particular member of the dataset in question.

<H1>EXCEL</H1>
Excel is a program produced by Microsoft, dedicated to the production and management of spreadsheets.
In particular, it can be used to open downloaded datasets in tabular format, which are usually .csv, and to organize the data within them.

<H1>PYTHON, PANDAS, MATHPLOTLIB</H1>
Python is an open source language that comes with a solid ecosystem of computer science libraries. It is a high-level language, with a very simple and intuitive syntax.
Pandas is one of the most versatile Python libraries. It is based on NumPy and, in turn, offers many other working environments. Its operation is characterized by two data structures: the Data Frame, a sort of table, structured on columns where the data is distributed by rows. And the other is the Series which is used to represent rows or columns of a Data Frame.
Finally, MatPlotlib is a charting library for Python that provides APIs that allow you to insert graphics into applications using generic GUI toolkits.

<H1>PROJECT ROADMAP</H1>
1. CONSTRUCTION OF DATASETS
• Data acquisition from the Climate Change Knowledge Portal For Development Practitioners and Policy Makers website [https://climateknowledgeportal.worldbank.org/download-data]
o In particular, I will build the datasets of the historical series ranging from 1901 to 2020 of the variables rainfall, average temperatures, maximum temperatures and minimum temperatures in Italy
o And I will build the datasets on climate projections calculated with multi-ensemble models ranging from 2020 to 2039 with aggregated data based on the year-season, 10th, 90th and median (50th) percentiles, with RCP 2.6 and RCP 8.5 scenarios
• Troubleshooting and consistent data formatting
• Creation of Excel files organized by climatic variables

2. DATASET ANALYSIS
• Python for data analysis, using some of its libraries, such as: Pandas, NumPy and MatPlotlib
• Creation of Datasets and creation of Data Frames with Pandas. Thanks to Pandas it was possible to read the Excel files by creating Data Frames necessary for the various analyzes
• Creation of graphs with MatPlotlib and NumPy, once the necessary Data Frames were created, the previous libraries were used to create the graphs to carry out the necessary analyzes

3. CONSIDERATIONS ON RESULTS
• Visualization of the graphs produced, created the graphs relating to the analyzes, it was possible to observe the results through the graphs produced
• Discussion on the results obtained, taking into consideration the graphs produced, it is possible to draw conclusions regarding the trend and trends of the variables taken into consideration
