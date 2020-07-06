import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
from collections import Counter
import tkinter as tk
from tkinter.filedialog import askopenfilename

# Store the resume in a variable
filename = askopenfilename()
resume = docx2txt.process(filename)

# Print the resume
#print(resume)
stat = dict()

for filename in os.listdir("./test_job"):
    # Store the job description into a variable
    job_description = docx2txt.process("./test_job/"+filename)

    # Print the job description
    # print(job_description)

    # A list of text
    text = [resume, job_description]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    #Print the similarity scores
    #print("\nSimilarity Scores:")
    #print(cosine_similarity(count_matrix))

    #get the match percentage
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    stat[('1Amy.docx',filename)] = matchPercentage
    print("Your resume matches about "+ str(matchPercentage)+ "% of the job description:"+ filename)

match = Counter(stat)
top3 = match.most_common(3)
print('Your top job recommendations are:',top3)