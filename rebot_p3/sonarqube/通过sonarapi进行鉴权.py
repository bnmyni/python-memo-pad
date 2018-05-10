from sonarqube_api import SonarAPIHandler

h = SonarAPIHandler(host='http://10.1.3.33', port=9000, user='admin', password='admin')

# gen = h.get_metrics()

gen = h.get_metrics()

print(gen.nex())

# while True:
#     print(gen.send(None))