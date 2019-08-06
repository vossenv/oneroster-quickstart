from pprint import pprint
import oneroster

connector = oneroster.CleverConnector(
    host="https://api.clever.com/v2.1/",
    access_token="TEST_TOKEN"
)

user_list = connector.get_users(user_filter='students')

print(str(len(user_list)) + " students in total.  First result:\n")
pprint(user_list[0])

class_name = "Fine Arts, Class 703 - Ortiz - 7"
ela_users = connector.get_users(user_filter='students',
                                group_filter='sections',
                                group_name=class_name)

print("")
print(str(len(ela_users)) + " users found for Fine Arts, Class 703 - Ortiz - 7")

class_id = "58da8c6a894273be680001d8"
ela_users = connector.get_users(user_filter='students',
                                group_filter='sections',
                                group_name=class_id)

print(str(len(ela_users)) + " users found for Fine Arts, Class 703 - Ortiz - 7 by Id")

hschool_users = connector.get_users(user_filter='students',
                                    group_filter='schools',
                                    group_name='Pineapple Elementary School')

mschool_users = connector.get_users(user_filter='students',
                                    group_filter='schools',
                                    group_name='58da8c58155b940248000008')

print(str(len(hschool_users)) + " elementary school students returned")
print(str(len(mschool_users)) + " middle school students returned")

r302_users = connector.get_users(user_filter='students',
                                 group_filter='sections',
                                 group_name='6',
                                 match_on='grade')

print(str(len(r302_users)) + " students in grade 6")
