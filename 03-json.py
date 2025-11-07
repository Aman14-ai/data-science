book = {};
book['tom'] = {
    'name': 'tom',
    'address': '123 Main St, Springfield',
    'phone': '555-1234'
}
book['bob'] = {
    'name': 'bob',
    'address': '456 Elm St, Shelbyville',
    'phone': '555-5678'
}
# print(book);

import json;

book_string=json.dumps(book); # converting dictionary to string
with open('book.txt','w') as f:
    f.write(book_string);
print(book_string,type(book_string));



# print("____________________reding from file______________________");
# with open('book.txt','r') as f:
#     data = f.read();

data_loads_dict = json.loads(book_string); # this is  a dictionary
print(data_loads_dict,type(data_loads_dict));

print("tom phone number: ", data_loads_dict['tom']['phone'])
for person in data_loads_dict:
    print(f"{person} address is: {data_loads_dict[person]['address']}")
