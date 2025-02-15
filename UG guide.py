class CourseInfo:
    def __init__(self, aggregate, fee):
        self.aggregate = aggregate
        self.fee = fee
    
universities = ["GCU", "NUST", "UAF"]
courses = [
    "Bioinformatics",
    "Microbiology",
    "Biotechnology",
    "Zoology",
    "Computer Science",
    "IR",
    "Law",
    "Economics",
    "Pharm D",
    "Botany",
    "Chemistry",
    "Biochemistry",
    "Business Administration",
    "Defense and Strategic Studies",
    "English Literatute",
    "Environmental Sciences",
    "Fine Arts",
    "History",
    "Geography",
    "Information Technology",
    "Mathematics",
    "Pakistan Studies",
    "Physics",
    "Political Sciences",
    "Public Administration",
    "Sociology",
    "Statistics",
    "Psychology"
    ]

universitiesData = {
    "GCU": [
        CourseInfo(65, 49000),
        CourseInfo(73.46, 49000),
        CourseInfo(74.46, 49000),
        CourseInfo(73.64, 49000),
        CourseInfo(74.18, 66000),
        CourseInfo(47.46, 42000),
        CourseInfo(67.09, 58000),
        CourseInfo(52.36, 42000),
        CourseInfo(83.27, 111000),
        CourseInfo(65.46, 42000),
        CourseInfo(68.36, 49000),
        CourseInfo(52.73, 42000),
        CourseInfo(65, 69000),
        CourseInfo(69, 69000),
        CourseInfo(62, 42000),
        CourseInfo(54.36, 49000),
        CourseInfo(52.73, 69000),
        CourseInfo(45.36, 42000),
        CourseInfo(46.27, 49000),
        CourseInfo(67.55, 76000),
        CourseInfo(74.46, 49000),
        CourseInfo(45, 42000),
        CourseInfo(73.55, 49000),
        CourseInfo(45.46, 42000),
        CourseInfo(45.18, 690000),
        CourseInfo(45.27, 42000),
        CourseInfo(46.27, 49000),
        CourseInfo(68.36, 42000),
    ],
    "UAF": [
        CourseInfo(86.758, 30550),
        CourseInfo(86.155, 30550),
        CourseInfo(86.124, 30550),
        CourseInfo(86.766, 30550),
        CourseInfo(86.619, 31000),
        CourseInfo(80.91, 28550),
        CourseInfo(85.54, 28550),
        CourseInfo(71.459, 28550),
        CourseInfo(90.381, 30550),
        CourseInfo(71.777, 30550),
        CourseInfo(89.94, 31000),
        CourseInfo(74.9, 30550),
        CourseInfo(77.01, 42000),
        CourseInfo(75.22, 28000),
        CourseInfo(51.1, 28000),
        CourseInfo(86.184, 30550),
        CourseInfo(66.4, 28000),
        CourseInfo(59.445, 28000),
        CourseInfo(58.649, 28000),
        CourseInfo(84.87, 31000),
        CourseInfo(74.691, 30550),
        CourseInfo(65.991, 28000),
        CourseInfo(56.609, 30550),
        CourseInfo(72.111, 28000),
        CourseInfo(73.45, 28000),
        CourseInfo(72.051, 28550),
        CourseInfo(71.934, 28000),
        CourseInfo(71.857, 28550),
    ],
    "NUST": [
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 100000),
        CourseInfo(55, 100000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(65, 100000),
        CourseInfo(55, 100000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 87000),
        CourseInfo(55, 100000),
        CourseInfo(55, 100000),
        CourseInfo(55, 100000),
        CourseInfo(55, 100000),
    ],
}
aggregateWeightages = {
    "GCU":[0,0.6,0.4],
    "NUST":[0.1,0.15,0.75],
    "UAF":[0.3,0.3,0.4]
}

def isValidCourseName(course):
    return course in courses
def isFinanciallyEligible(course, fee, university):
    return universitiesData[university][courses.index(course)].fee <= fee
def isAggregateEligible(course, aggregate, university):
    return universitiesData[university][courses.index(course)].aggregate <= aggregate
def returnAggregate(weightage, matric, fsc, entryTest):
    return weightage[0]*matric + weightage[1]*fsc + weightage[2]*entryTest

course = input("Enter Course you are interested in: ")
if(not isValidCourseName(course)):
    print("We do not have information for ",course)
    exit()
fee = int(input("Enter Fee you can afford:"))
matric = int(input("Enter Matric Percentage:"))
fsc = int(input("Enter FSc Percentage:"))
entryTest = int(input("Enter Entry Test Percentage:"))

for university in universities:
    if(isFinanciallyEligible(course, fee, university) and isAggregateEligible
    (course, returnAggregate(aggregateWeightages[university], matric, fsc, entryTest), university)):
        print("Congratulations! You are eligible in ", university)
    else:
        print("Oops! You are not eligible in ", university)

