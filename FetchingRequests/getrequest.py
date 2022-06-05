# importing the requests library
import requests

# api-endpoint
URL = "http://localhost:5000/api/getCourseDescription/6279265412431d82277b0327"

# sending get request and saving the response as response object
r = requests.get(URL)
print(r.json())
x= r.json()
y = x['message']
module_table = y['Module_table']
text_book_table = y['text_Book_table']
semester = y['semester']
course_ref = y['course_ref']
faculty_table = course_ref['faculty_table']
course_code = course_ref['course_code']
course_name = course_ref['course_name']
course_credit = course_ref['course_credits']
branch = course_ref['Branch']
course_outcome = course_ref['course_outcome']
reference_book_table = y['reference_books_table']

