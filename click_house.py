from clickhouse_driver import Client

client = Client(host='localhost', password='password')

print(client.execute('SHOW DATABASES'))
print(client.execute('SELECT * FROM system.numbers LIMIT 5'))
print(client.execute(
    "SELECT 'test' like '%%es%%', %(myvar)s",
    {'myvar': 1}
))