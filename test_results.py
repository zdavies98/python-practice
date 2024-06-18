# ######################################################################################################### #
# Load in a data file, and print the answers to the following questions                                     #
#                                                                                                           #
#   1. How many females have been tested and how many of them tested positive?                              #
#   2. How many males have been tested and how many of them tested positive?                                #
#   3. What is the average age of the females who tested positive?                                          #
#   4. What is the average age of the males who tested positive?                                            #
#   5. What is the youngest age of a person who tested positive?                                            #
#   6. What is the oldest age of a person who tested positive?                                              #
#   7. Compare the average age of the females who tested positive to the average age of the females         #
#       who did not test positive.                                                                          #
#   8. Compare the average age of the males who tested positive to the average age of the males who         #
#       did not test positive.                                                                              #
#   9. What's the average weight of the females who tested positive?                                        #
#   10. What's the average weight of the males who tested positive?                                         #
#   11. The formula for BMI is weight in kilograms divided by height in meters squared. When using          #
#       English measurements, pounds should be divided by inches squared. This should then be               #
#       multiplied by 703 to convert from lbs/inches2 to kg/m2. Determine the average BMI for the           #
#       females who tested positive.                                                                        #
#   12. Determine the average BMI for the males who tested positive.                                        #
#   13. A BMI of 30 or higher means that the person is obese. There is a possibility that this is a greater #
#       chance that Covid-19 can be fatal if you are obese. Determine how many of the females who           #
#       tested positive are obese.                                                                          #
#   14. Determine how many of the males who tested positive are obese.                                      #
#   15. Determine how many people who are 80 or older who tested positive are obese.                        #
#   16. Determine what the average BMI is for females who tested positive in the following three            #
#       groups: under 30, between 30-60, and over 60.                                                       #
#   17. Determine what the average BMI is for males who tested positive in the following three groups:      #
#       under 30, between 30-60, and over 60.                                                               #
#   18. What is the average rate of infection for all of the people who were tested?                        #
# ######################################################################################################### #                                                                             

# Load in file
infile = open("C:\\Users\\zdavi\\Documents\\dev\\python_practice\\_data\\data_set.txt", "r")
# Read first line
line = infile.readline()

# initialize variables
age = 0

femalesTested = 0
malesTested = 0

positiveFemales = 0
positiveMales = 0

ageOfPositiveFemales = 0
ageOfPositiveMales = 0

negativeFemales = 0
negativeMales = 0

ageOfNegativeFemales = 0
ageOfNegativeMales = 0

weightPositiveFemales = 0
weightPositiveMales = 0

weightNegativeFemales = 0
weightNegativeMales = 0

heightPositiveFemales = 0
heightPositiveMales = 0

heightNegativeFemales = 0
heightNegativeMales = 0

obesePositiveFemales = 0
obesePositiveMales = 0

oldObesePositive = 0

bmiPositiveFemalesUnder30 = 0
bmiPositiveMalesUnder30 = 0

bmiPositiveFemales30To60 = 0
bmiPositiveMales30To60 = 0

bmiPositiveFemalesOver60 = 0
bmiPositiveMalesOver60 = 0

positiveFemalesUnder30 = 0
positiveMalesUnder30 = 0

positiveFemales30To60 = 0
positiveMales30To60 = 0

positiveFemalesOver60 = 0
positiveMalesOver60 = 0

totalBMIPositiveFemalesUnder30 = 0
totalBMIPositiveMalesUnder30 = 0

totalBMIPositiveFemales30To60 = 0
totalBMIPositiveMales30To60 = 0

totalBMIPositiveFemalesOver60 = 0
totalBMIPositiveMalesOver60 = 0

maxAgePositive = 0
minAgePositive = 150

'''
    File Format:
        gender  age testResult  weight - height
        ...
        M       66  60          209    - 33620
        M       60  59          170    - 33612
        F       49  59          222    - 33687
        ...
'''

# loop through entire file
while (line != ""):
    gender = line[0]
    age = int(line[2:4])
    testResult = line[13]
    weight = int(line[9:12])
    height = int(line[6:8])

    # Loop for female data
    if (gender == "F"):
        femalesTested += 1
        if (testResult == "+"):
            positiveFemales += 1
            ageOfPositiveFemales += age
            if age >= 80:
                oldObesePositive += 1
            if age < 30:
                positiveFemalesUnder30 += 1
            if age >= 30:
                if age <= 60:
                    positiveFemales30To60 += 1
            if age > 60:
                positiveFemalesOver60 += 1
            heightPositiveFemales = height
            weightPositiveFemales = weight
            bmiPositiveFemales = (weightPositiveFemales / (heightPositiveFemales ** 2) * 703)
            if bmiPositiveFemales > 30:
                obesePositiveFemales += 1
            if age < 30:
                heightPositiveFemalesUnder30 = 0
                heightPositiveFemalesUnder30 += height
                weightPositiveFemalesUnder30 = 0
                weightPositiveFemalesUnder30 += weight
                bmiPositiveFemalesUnder30 = (weightPositiveFemalesUnder30 / (heightPositiveFemalesUnder30 ** 2 )) * 703
                totalBMIPositiveFemalesUnder30 += bmiPositiveFemalesUnder30
            if age >= 30:
                if age <= 60:
                    heightPositiveFemales30To60 = 0
                    heightPositiveFemales30To60 += height
                    weightPositiveFemales30To60 = 0
                    weightPositiveFemales30To60 += weight
                    bmiPositiveFemales30To60 = (weightPositiveFemales30To60 / (heightPositiveFemales30To60 ** 2)) * 703
                    totalBMIPositiveFemales30To60 += bmiPositiveFemales30To60
            if age > 60:
                heightPositiveFemalesOver60 = 0
                heightPositiveFemalesOver60 += height
                weightPositiveFemalesOver60 = 0
                weightPositiveFemalesOver60 += weight
                bmiPositiveFemalesOver60 = (weightPositiveFemalesOver60 / (heightPositiveFemalesOver60 ** 2)) * 703
                totalBMIPositiveFemalesOver60 += bmiPositiveFemalesOver60
        if (testResult == "-"):
            negativeFemales += 1
            ageOfNegativeFemales += age
            heightNegativeFemales += height
            weightNegativeFemales += weight
    
    # Loop for male data
    if (gender == "M"):
        malesTested += 1
        if (testResult == "+"):
            positiveMales += 1
            ageOfPositiveMales += age
            if age >= 80:
                oldObesePositive += 1
            if age < 30:
                positiveMalesUnder30 += 1
            if age >= 30:
                if age <= 60:
                    positiveMales30To60 += 1
            if age > 60:
                positiveMalesOver60 += 1
            heightPositiveMales += height
            weightPositiveMales += weight
            bmiPositiveMales = (((weightPositiveMales / heightPositiveMales) ** 2) * 703)
            if bmiPositiveMales > 30:
                obesePositiveMales += 1
            if age < 30:
                heightPositiveMalesUnder30 = 0
                heightPositiveMalesUnder30 += height
                weightPositiveMalesUnder30 = 0
                weightPositiveMalesUnder30 += weight
                bmiPositiveMalesUnder30 = (weightPositiveMalesUnder30 / (heightPositiveMalesUnder30 ** 2)) * 703
                totalBMIPositiveMalesUnder30 += bmiPositiveMalesUnder30
            if age >= 30:
                if age <= 60:
                    heightPositiveMales30To60 = 0
                    heightPositiveMales30To60 += height
                    weightPositiveMales30To60 = 0
                    weightPositiveMales30To60 += weight
                    bmiPositiveMales30To60 = (weightPositiveMales30To60 / (heightPositiveMales30To60 ** 2)) * 703
                    totalBMIPositiveMales30To60 += bmiPositiveMales30To60
            if age > 60:
                heightPositiveMalesOver60 = 0
                heightPositiveMalesOver60 += height
                weightPositiveMalesOver60 = 0
                weightPositiveMalesOver60 += weight
                bmiPositiveMalesOver60 = (weightPositiveMalesOver60 / (heightPositiveMalesOver60 ** 2)) * 703
                totalBMIPositiveMalesOver60 += bmiPositiveMalesOver60
        if (testResult == "-"):
            negativeMales += 1
            ageOfNegativeMales += age
            heightNegativeMales += height
            weightNegativeMales += weight

    if (testResult == '+'):
        if age > maxAgePositive:
            maxAgePositive = age
        if age < minAgePositive:
            minAgePositive = age

    # read next line
    line = infile.readline()

#Pt. 1:
print("1. Total number of females tested:", femalesTested)

#Pt. 2:
print("2. Total number of males tested:", malesTested)

#Pt. 3: What is the avg. age of the females who tested positive?
print("3. The average age of the females who tested positive is {0:.2f}.".format(ageOfPositiveFemales/positiveMales))

#Pt. 4: What is the avg. of the males who tested positive?
print("4. The average age of the males who tested positive is {0:.2f}.".format(ageOfPositiveMales/positiveMales))

#Pt. 5: What is the youngest age of a person who tested positive?
print("5. The youngest age of a person who tested positive is {0:1}.".format(minAgePositive))

#Pt. 6: What is the oldest age of a person who tested positive?
print("6. The oldest age of a person who tested positive is {0:1}.".format(maxAgePositive))

#Pt. 7: Compare the average age of the females who tested positive to the average age of the females who did not test postiive
print("7. The average age of the females who tested positive is {0:.2f}, compared to the average age of the females who tested negative at {1:.2f}."
      .format((ageOfPositiveFemales/positiveFemales), (ageOfNegativeFemales/negativeFemales)))

#Pt. 8: COmpare the avg age of the males who tested pos. to the avg age of the males who did not test positive
print("8. The average age of the females who tested positive is {0:.2f}, compared to the average age of the males who tested negative at {1:.2f}."
      .format((ageOfPositiveMales/positiveMales), (ageOfNegativeMales/negativeMales)))

#Pt. 9: Avg weight of the females who tested positive
print("9. The average weight of the females who tested positive is {0:.2f} pounds.".format(weightPositiveFemales/positiveFemales))

#Pt. 10: Avg weight of the males who tested positive
print("10. The average weight of the males who tested positive is {0:.2f} pounds.".format(weightPositiveMales/positiveFemales))

#Pt. 11: Avg BMI for the females who tested positive
print("11. The average BMI for females that tested positive is {0:.2f} pounds.".format(bmiPositiveFemales/positiveFemales))

#Pt. 12: Avg BMI for the males who tested positive
print("12. The average BMI for males that tested positive is {0:.2f} pounds.".format(bmiPositiveMales/positiveMales))

#Pt. 13: How many females tested positive were obese
print("13. There are {0} obese females that tested positive.".format(obesePositiveFemales))

#Pt. 14: How many males tested positive were obese
print("14. There are {0} obese males that tested positive.".format(obesePositiveMales))

#Pt. 15: How many people who are 80+ tested positive are obese
print("15. There are {0} people that are 80 years and older that tested positive and are obese.".format(oldObesePositive))

#Pt. 16: Avg BMI for females who tested positive in:
    #Under 30, between 30-60, and over 60
avgBMIPositiveFemalesUnder30 = totalBMIPositiveFemalesUnder30 / positiveFemalesUnder30
avgBMIPositiveFemales30To60 = totalBMIPositiveFemales30To60 / positiveFemales30To60
avgBMIPositiveFemalesOver60 = totalBMIPositiveFemalesOver60 / positiveFemalesOver60

print("16. The average BMI for positive females under 30 is {0:.2f}. The average BMI for positive females 30-60 y/o is {1:.2f}. The average"
      "BMI for females over the age of 60 is {2:.2f}.".format(avgBMIPositiveFemalesUnder30, avgBMIPositiveFemales30To60, avgBMIPositiveFemalesOver60))

#Pt. 17: Avg BMI for males tho tested positive in:
    #Under 30, between 30-60, and over 60
avgBMIPositiveMalesUnder30 = totalBMIPositiveMalesUnder30 / positiveMalesUnder30
avgBMIPositiveMales30To60 = totalBMIPositiveMales30To60 / positiveMales30To60
avgBMIPositiveMalesOver60 = totalBMIPositiveMalesOver60 / positiveMalesOver60

print("17. The average BMI for positive males under 30 is {0:.2f}. The average BMI for positive males 30-60 y/o is {1:.2f}. The average"
      "BMI for males over the age of 60 is {2:.2f}.".format(avgBMIPositiveMalesUnder30, avgBMIPositiveMales30To60, avgBMIPositiveMalesOver60))

#Pt. 18: Avg rate of infection for all of the people who were tested
rateOfInfection = (positiveFemales + positiveMales) / (femalesTested + malesTested)

print("18. The average rate of infection for all people tested is {0:.2f}%.".format(rateOfInfection))
