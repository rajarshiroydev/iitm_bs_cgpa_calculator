from flask import Flask, render_template, request

app = Flask(__name__)

# Credits for different subjects
credits = {
    "Mathematics 1": 4,
    "Statistics 1": 4,
    "English 1": 4,
    "Computational Thinking": 4,
    "Mathematics 2": 4,
    "Statistics 2": 4,
    "English 2": 4,
    "Python": 4,
    "DBMS": 4,
    "PDSA": 4,
    "MAD 1": 4,
    "MAD 1 Project": 2,
    "JAVA": 4,
    "MAD 2": 4,
    "MAD 2 Project": 2,
    "SC": 3,
    "MLF": 4,
    "BDM": 4,
    "BDM Project": 2,
    "MLT": 4,
    "MLP": 4,
    "MLP Project": 2,
    "TDS": 3,
    "BA": 4,
}

# Grade values
grade_values = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 4}

# Categorize courses
foundation_courses = [
    "Mathematics 1",
    "Statistics 1",
    "English 1",
    "Computational Thinking",
    "Mathematics 2",
    "Statistics 2",
    "English 2",
    "Python",
]

diploma_programming_courses = [
    "DBMS",
    "PDSA",
    "MAD 1",
    "MAD 1 Project",
    "JAVA",
    "MAD 2",
    "MAD 2 Project",
    "SC",
]

diploma_data_science_courses = [
    "MLF",
    "BDM",
    "BDM Project",
    "MLT",
    "MLP",
    "MLP Project",
    "TDS",
    "BA",
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        grades = {subject: request.form.get(subject, "YTC") for subject in credits}

        # Calculate CGPA only for completed courses
        completed_credits = sum(
            credits[subject] for subject, grade in grades.items() if grade != "YTC"
        )
        cgpa_sum = sum(
            credits[subject] * grade_values[grade]
            for subject, grade in grades.items()
            if grade != "YTC"
        )

        cgpa = cgpa_sum / completed_credits if completed_credits > 0 else None

        return render_template(
            "index.html",
            grades=grades,
            cgpa=round(cgpa, 2) if cgpa is not None else None,
            credits=credits,
            foundation_courses=foundation_courses,
            diploma_programming_courses=diploma_programming_courses,
            diploma_data_science_courses=diploma_data_science_courses,
        )
    return render_template(
        "index.html",
        grades={subject: "YTC" for subject in credits},
        cgpa=None,
        credits=credits,
        foundation_courses=foundation_courses,
        diploma_programming_courses=diploma_programming_courses,
        diploma_data_science_courses=diploma_data_science_courses,
    )


if __name__ == "__main__":
    app.run(debug=True)
