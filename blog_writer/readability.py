import textstat

def evaluate_readability(content):
    readability_score = textstat.flesch_reading_ease(content)
    grade_level = textstat.text_standard(content)
    return {
        "readability_score": readability_score,
        "grade_level": grade_level
    }