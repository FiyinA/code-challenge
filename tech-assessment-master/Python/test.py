data = [
    {
        "customerID" : "1",
        "firstName": "Carol",
        "lastName": "Danvers",
        "age": 33,
        "address":
        {
            "streetAddress": "417 5th Avenue Apt 10B",
            "city": "New York",
            "state": "NY",
            "postalCode": "10016"
        },
        "phoneNumber": "2125551234"
    },
    {
        "customerID" : "2",
        "firstName": "Tony",
        "lastName": "Stark",
        "age": 48,
        "address":
        {
            "streetAddress": "890 Fifth Avenue",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021"
        },
        "phoneNumber": "2125554567"
    },
    {
        "customerID" : "3",
        "firstName": "Steve",
        "lastName": "Rogers",
        "age": 93,
        "address":
        {
            "streetAddress": "890 Fifth Avenue",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021"
        },
        "phoneNumber": "6781367092"
    }
]

orders = [
    {
        "CustomerID": "1",
        "order": "phone"
    },
     {
        "CustomerID": "2",
        "order": "books"
    },
     {
        "CustomerID": "3",
        "order": "car"
    },
]


# for x in data:
#     y = x["customerID"]
#     print (y)

# for x in data:
#     for y in orders:
#         if x['customerID'] == y['CustomerID']:
#             x['orders'] = y['order']

def update (CID, order):
        for x in orders:
            if CID == x['CustomerID']:
                x['order'] = order 


update ('1', "elephant")

print (orders)