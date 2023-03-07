import uuid

# Generate a UUID version 4
uuid_1 = uuid.uuid4()
print(uuid_1)  # Output: f63e66f1-8e68-4d20-9e9d-849853899e47
uuid_2 = uuid.uuid4()
print(uuid_2)
# Generate a UUID version 5 from a namespace and a name
namespace = uuid.NAMESPACE_URL
name = 'https://www.example.com'
uuid_2 = uuid.uuid5(namespace, name)
print(uuid_2)  # Output: 45d28a9a-7913-5b75-a0e7-6d684e94a020
