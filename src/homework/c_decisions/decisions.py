#
def get_options_ratio(option, total):
    ratio = option / total
    return ratio

def get_faculty_rating(ratio):
        rating = 0

        if(ratio >= .9 and ratio < 1):
            rating = "Excellent"
        elif(ratio >= .8 and ratio < .9):
            rating = "Very Good"
        elif(ratio >= .7 and ratio < .8):
            rating = "Good"
        elif(ratio >= .6 and ratio < .7):
            rating = "Needs Improvement"
        elif(ratio >=0 and ratio < .6):
            rating = "Unacceptable"
        
        return rating