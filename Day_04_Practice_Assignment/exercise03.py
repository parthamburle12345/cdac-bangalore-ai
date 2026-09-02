def compile_feedback(ratings_dict):
    for key in ratings_dict:
        result = []
        for item in ratings_dict[key]:
            try:    
                if type(item) == int:
                    result.append(float(item))
                else:
                    raise ValueError()
            except ValueError:
                print(f"Warning: Invalid rating value {item} in course {key} skipped.")
        try:    
            val1 = sum(result)*2
            val2 = int(val1/len(result))
            val3 = val2/2
            ratings_dict[key] = val3
        except ZeroDivisionError:
            print(f"Warning: No valid ratings found for course {key}. Rating set to 0.0.")
            ratings_dict[key] = 0.0
    print(ratings_dict)
                


feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

compile_feedback(feedback_data)

