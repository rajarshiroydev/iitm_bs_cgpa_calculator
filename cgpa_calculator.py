# foundation
maths1_credit = 4
stats1_credit = 4
eng1_credit = 4
ct_credit = 4
maths2_credit = 4
stats2_credit = 4
eng2_credit = 4
python_credit = 4

# diploma in programming
dbms_credit = 4
pdsa_credit = 4
mad1_credit = 4
java_credit = 4
mad2_credit = 4
sc_credit = 3
mad1_project_credit = 2
mad2_project_credit = 2

# diploma in data_science
mlf_credit = 4
bdm_credit = 4
bdm_project_credit = 2
mlt_credit = 4
mlp_credit = 4
mlp_project_credit = 2
tds_credit = 3
ba_credit = 4


maths1_grade = int(input("Enter maths1 grade point : "))
stats1_grade = int(input("Enter stats1 grade point : "))
eng1_grade = int(input("Enter eng1 grade point : "))
ct_grade = int(input("Enter ct grade point : "))
maths2_grade = int(input("Enter maths2 grade point : "))
stats2_grade = int(input("Enter stats2 grade point : "))
eng2_grade = int(input("Enter eng2 grade point : "))
python_grade = int(input("Enter python grade point : "))
dbms_grade = int(input("Enter dbms grade point : "))
pdsa_grade = int(input("Enter pdsa grade point : "))
mad1_grade = int(input("Enter mad1 grade point : "))
java_grade = int(input("Enter java grade point : "))
mad2_grade = int(input("Enter mad2 grade point : "))
sc_grade = int(input("Enter sc grade point : "))
mlf_grade = int(input("Enter mlf grade point : "))
bdm_grade = int(input("Enter bdm grade point : "))
mlt_grade = int(input("Enter mlt grade point : "))
mlp_grade = int(input("Enter mlp grade point : "))
tds_grade = int(input("Enter tds grade point : "))
ba_grade = int(input("Enter ba grade point : "))
mad1_project_grade = int(input("Enter mad1 project grade point : "))
mad2_project_grade = int(input("Enter mad2 project grade point : "))
bdm_project_grade = int(input("Enter bdm project grade point : "))
mlp_project_grade = int(input("Enter mlp project grade point : "))

cgpa = (
    maths1_credit * maths1_grade
    + stats1_credit * stats1_grade
    + eng1_credit * eng1_grade
    + ct_credit * ct_grade
    + maths2_credit * maths2_grade
    + stats2_credit * stats2_grade
    + eng2_credit * eng2_grade
    + python_credit * python_grade
    + dbms_credit * dbms_grade
    + pdsa_credit * pdsa_grade
    + mad1_credit * mad1_grade
    + mad1_project_credit * mad1_project_grade
    + java_credit * java_grade
    + mad2_credit * mad2_grade
    + mad2_project_credit * mad2_project_grade
    + sc_credit * sc_grade
    + mlf_credit * mlf_grade
    + bdm_credit * bdm_grade
    + bdm_project_credit * bdm_project_grade
    + mlt_credit * mlt_grade
    + mlp_credit * mlp_grade
    + mlp_project_credit * mlp_project_grade
    + tds_credit * tds_grade
    + ba_credit * ba_grade
) / 86

print("cgpa : ", cgpa)
