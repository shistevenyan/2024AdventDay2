with open('advent-day-2.txt', 'r') as file:
    reports = file.read().strip().split('\n')

def isReportSafe(reportList):
    reportLength = len(reportList)

    # edge case, if there is only 0 or 1 level
    # report has to be safe
    if reportLength < 2:
        return True

    
    direction = ""

    for i in range(reportLength - 1):
        currLevel = int(reportList[i])
        nextLevel = int(reportList[i + 1])

        diff = currLevel - nextLevel

        # if the diff is not between 1 and 3
        # it is an unsafe report
        if not (1 <= abs(diff) <= 3):
            return False

        # set the direction on the first level pair
        if direction == "":
            if diff > 0:
                direction = "decrease"
            else:
                direction = "increase"
        else:
            # if curr level is less than next level
            # the direction is increasing
            # but if the direction set is decreasing
            # it is an unsafe report
            if currLevel < nextLevel and direction == "decrease":
                return False

            # same logic as above
            elif currLevel > nextLevel and direction == "increase":
                return False
            
    return True

# solve with dampener
def getSafeReports(reports):
    safeReports = 0
    for report in reports:
        reportList = report.split()
        # removing one element at a time
        # and check if its a safe report
        for i in range(len(reportList)):
            if isReportSafe(reportList[:i] + reportList[i+1:]):
                safeReports += 1
                break

    return safeReports

res = getSafeReports(reports)
print(res)
    
