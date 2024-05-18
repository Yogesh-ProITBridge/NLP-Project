CV Classifier Project :

I've collected a few resumes of various designations and converted the pdfs to dox. Save it as a CSV file. Then, choose a few classification models to develop models from and compare their accuracy.

Steps I followed:
- DE, DS, JD, MDE - These file names include original CV files downloaded from Google.
- Data Engineer, Data Scientist, Java Developer, Mechanical Design Engineer - These file names contain cv files that have been converted from pdf to docx.
- The resume classifier Python program will demonstrate how to alter the pdf to docx conversion and extract the text from the doxc file and save it as a csv file.
- The classification models Python file will show you what models I use for model development.
 
I'm sharing the accuracy of the models, I built : Accuracy.xlsx file

Overview

The Resume Classifier utilizes machine learning techniques to classify resumes into different categories. It employs eight different classification models initially, but through evaluation, XGBoost demonstrates best performance in terms of accuracy, precision, recall, and F1-score.

Performance Metrics:

-  Accuracy: Accuracy measures the proportion of correctly classified instances out of the total instances. In this context, an accuracy of 0.96 means that 96% of the resumes were correctly classified into their respective categories by the model.
  
Precision: Precision is the ratio of correctly predicted positive observations to the total predicted positives. It measures the accuracy of positive predictions.

-  For Class 0: Precision of 1.00 means that all resumes predicted as Class 0 were indeed Class 0.
-  For Class 1: Precision of 0.90 indicates that 90% of the resumes predicted as Class 1 were actually Class 1.
-  For Class 2: Precision of 0.96 suggests that 96% of the resumes predicted as Class 2 were actually Class 2.
-  For Class 3: Precision of 0.97 means that 97% of the resumes predicted as Class 3 were actually Class 3.

Recall: Recall, also known as sensitivity, is the ratio of correctly predicted positive observations to the all observations in actual class. It measures the ability of the classifier to find all positive instances.

-  For Class 0: Recall of 0.95 means that the model identified 95% of the actual Class 0 resumes.
-  For Class 1: Recall of 0.95 suggests that the model identified 95% of the actual Class 1 resumes.
-  For Class 2: Recall of 0.96 indicates that the model identified 96% of the actual Class 2 resumes.
-  For Class 3: Recall of 0.97 means that the model identified 97% of the actual Class 3 resumes.

F1-score: The F1-score is the harmonic mean of precision and recall. It provides a balance between precision and recall. 

- For Class 0: F1-score of 0.97 represents a balanced performance between precision and recall for Class 0.
- For Class 1: F1-score of 0.93 suggests a slightly lower balance between precision and recall for Class 1.
- For Class 2: F1-score of 0.96 indicates a balanced performance between precision and recall for Class 2.
- For Class 3: F1-score of 0.97 represents a balanced performance between precision and recall for Class 3.

--------------------------------------------------------------------------------------------------------------------------------
RESUME PARSER APP 

Description:

The Resume Parser App is a tool for extracting important information from uploaded PDF resumes. This application uses spaCy, a powerful natural language processing library, 
to identify and obtain crucial details from PDF resumes, including name, contact number, email address, talents, and education. Simply update the necessary skills list in the code and search for relevant skills for the job position in the submitted resume.


I added the source code (main.py) and requirements.txt file.


