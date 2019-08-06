from pprint import pprint
import oneroster

connector = oneroster.ClasslinkConnector(
    host="https://example.oneroster.com/ims/oneroster/v1p1/",
    client_id='your_client_id',
    client_secret='your_client_secret',
)

user_list = connector.get_users(user_filter='students')

print(str(len(user_list)) + " students in total.  First result:\n")
pprint(user_list[0])

class_name = "ELA 6 (6A ELA)"
ela_users = connector.get_users(user_filter='students',
                                group_filter='classes',
                                group_name=class_name)

print("")
print(str(len(ela_users)) + " users found for ELA 6")

class_id = "31763"
ela_users = connector.get_users(user_filter='students',
                                group_filter='classes',
                                group_name=class_id)

print(str(len(ela_users)) + " users found for ELA 6 (1 section)")

hschool_users = connector.get_users(user_filter='students',
                                    group_filter='schools',
                                    group_name='Classlink HS')

mschool_users = connector.get_users(user_filter='students',
                                    group_filter='schools',
                                    group_name='7')

print(str(len(hschool_users)) + " high school students returned")
print(str(len(mschool_users)) + " middle school students returned")

r302_users = connector.get_users(user_filter='students',
                                 group_filter='classes',
                                 group_name='302',
                                 match_on='location')

print(str(len(r302_users)) + " students with classes in room 302")
