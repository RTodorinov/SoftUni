number_of_pages = int(input())
pages_for_one_hour = int(input())
total_days = int(input())

time_to_read_book = number_of_pages // pages_for_one_hour
hours_to_read_in_one_day = time_to_read_book // total_days

print(time_to_read_book)
print(hours_to_read_in_one_day)


