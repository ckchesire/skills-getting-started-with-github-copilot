from src import app as app_module

activity = 'Chess Club'
email = 'tester+uifix@mergington.edu'

activities = app_module.activities
print('before contains?', email in activities[activity]['participants'])

resp = app_module.signup_for_activity(activity, email)
print('signup response:', resp)

print('after contains?', email in activities[activity]['participants'])
