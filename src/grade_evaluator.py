# Import dependecies
import gspread, math

# Defining constants, making it simple to change parameters if needed
SHEET_ID = "1rcfARGZuyUQan3rqcIqn-kogGZBKvcYmlF_QOUKNb68"
CREDENTIALS_FILE = "./src/tunts-rocks-vbd-cd15afc8809d.json"
MAX_ABSENCES = 60 * 0.25

# Authentication and connection, as instructed in gspread's documentation
gc = gspread.service_account(filename=CREDENTIALS_FILE)
sh = gc.open_by_key(SHEET_ID)

# Get necessary rows
rows = sh.sheet1.get_values("A4:F")

# In gupy's description it said that it should be average < 5, but I believe 
# that to be a typo, considering that the grades were given in a 0-100 range, 
# instead of a 0-10 range. So I'll change the code accordingly.

# Calculate the grade needed with the formula 5 <= (avg + X)/2, which is basically
# 10 <= avg + X, which is the same as 10 - avg. Read the comment above to understand
# why its 100 instead of 10
def calculate_final_approval_grade(average):
  return (100 - average) 

# Calculate the situation in which the student is presently in
def get_situation(average, absences):
  if int(absences) > MAX_ABSENCES:
    return "Reprovado por Falta"
  elif average < 50:
    return "Reprovado por Nota"
  elif average < 70: 
    return "Exame Final"
  else:
    return "Aprovado"
  
# Transfer the list values to cells, and updates the sheet's collumn with the desired data
def transfer_values_to_cells(cell_range, values):
  cells = sh.sheet1.range(cell_range)
  for i, cell in enumerate(cells):
    cell.value = values[i]
  sh.sheet1.update_cells(cells)

# Prepare update lists for batch updating
update_situations = []
update_grades = []

# Process each row
for row in rows:
  # Get student data by unpacking the values. In larger sheets, where performance
  # is a concern, you would normally access it directly. But since it's a small
  # sheet, I chose to prioritize readability
  student_id, student_name, absences, p1, p2, p3 = row

  # Calculate average with math.ceil to round up to the nearest integer if needed
  average = math.ceil((int(p1) + int(p2) + int(p3)) / 3)

  # Calculate situation
  situation = get_situation(average, absences)

  # Calculate final approval grade
  final_approval_grade = 0 if situation != "Exame Final" else calculate_final_approval_grade(average)

  # Update lists with results
  update_situations.append(situation)
  update_grades.append(final_approval_grade)

  # Print logs
  print(f"Aluno: {student_name} - Média: {average} - Situação: {situation} - Nota para Aprovação Final: {final_approval_grade}")

# Instead of updating the cells directly in the for loop for rows, I chose to  make
# only 2 API calls, making the code more friendly to the server and more readable
transfer_values_to_cells("G4:G27", update_situations)
transfer_values_to_cells("H4:H27", update_grades)