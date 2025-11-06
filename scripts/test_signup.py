from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)
activity = 'Chess Club'
email = 'tester+uifix@mergington.edu'

resp = client.get('/activities')
data = resp.json()
participants = data[activity]['participants']
print('before contains?', email in participants)

resp = client.post(f"/activities/{activity}/signup?email={email}")
print('signup', resp.status_code, resp.json())

resp2 = client.get('/activities')
print('after contains?', email in resp2.json()[activity]['participants'])
