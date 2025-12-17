# Project Prompt: Giovanni Villanueva, Johnathan Medina, David Gil

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:
    # Enter a student’s full name
                                                            # make your own/make the program do it
    # Instantly see:

            # CPS ID
            # Homeroom
            # Grade Level
            # Primary Email
            # Students must:
            # Describe the search process  <---- dont worry about this


## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email 






# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

Student_data2 = []

cps_id = input ("Enter CPS ID: ")
first_name = input ("Enter First Name: ")
last_name = input ("Enter Last Name: ")
middle_name = input ("Enter Middle Name: ")
homeroom = input ("Enter Homeroom: ")
grade_level = input ("Enter Grade Level: ")
primary_email = input ("Enter Primary Email: ")
secondary_email = input ("Enter Secondary Email: ")

for student in Student_data2:
    if student["CPS ID"] == cps_id:
        print ("ERROR: CPS ID already exists.")
        exit()

full_name = last_name + " , " + first_name

new_student = {
"CPS ID": cps_id,
"Full Name" : full_name,
"Middle Name" : middle_name,
"Homeroom" : homeroom,
"Grade Level": grade_level,
"Primary Email" : primary_email,
"Secondary Email" : secondary_email
}

Student_data2.append(new_student)

print("\nStudent successfully added!")
print("Total number of students:", len(Student_data2))
print("New Student Record:")
print(new_student)