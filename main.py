import library

santimeters = str(input('Enter sm: '))

result_inches = library.cm_to_inches(santimeters)
result_type = library.type_definitions(result_inches)
round_up = str(input('round up - yes or no')).lower()
if round_up=='yes':
    result_type = library.round_number(result_type)

print(result_type)
