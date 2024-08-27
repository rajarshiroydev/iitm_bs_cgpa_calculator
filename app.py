from flask import Flask, render_template, request

app = Flask(__name__)

# Credits for different subjects
credits = {
    "maths1": 4,
    "stats1": 4,
    "eng1": 4,
    "ct": 4,
    "maths2": 4,
    "stats2": 4,
    "eng2": 4,
    "python": 4,
    "dbms": 4,
    "pdsa": 4,
    "mad1": 4,
    "mad1_project": 2,
    "java": 4,
    "mad2": 4,
    "mad2_project": 2,
    "sc": 3,
    "mlf": 4,
    "bdm": 4,
    "bdm_project": 2,
    "mlt": 4,
    "mlp": 4,
    "mlp_project": 2,
    "tds": 3,
    "ba": 4,
}

# Grade values
grade_values = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 4}

# Categorize courses
foundation_courses = [
    "maths1",
    "stats1",
    "eng1",
    "ct",
    "maths2",
    "stats2",
    "eng2",
    "python",
]

diploma_programming_courses = [
    "dbms",
    "pdsa",
    "mad1",
    "mad1_project",
    "java",
    "mad2",
    "mad2_project",
    "sc",
]

diploma_data_science_courses = [
    "mlf",
    "bdm",
    "bdm_project",
    "mlt",
    "mlp",
    "mlp_project",
    "tds",
    "ba",
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
