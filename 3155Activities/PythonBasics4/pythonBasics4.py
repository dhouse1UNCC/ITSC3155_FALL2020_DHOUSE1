# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    newContacts = {}
    if(len(emails) == 0):
        return contacts
    for i in range (0, len(contacts)):
        x = contacts.keys()
        y = iter(x)
        z = next(y)
        contacts.pop(z)
        newContacts[z] = emails[i]
    return newContacts

# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE
    newContacts = {}
    internalC = {}
    if(len(contact_info) < 2):
        return contacts
    for n in range (0, len(contact_info)):
        x = contacts.keys()
        y = iter(x)
        z = next(y)
        contacts.pop(z)
        internalC['email'] = contact_info[n][0]
        internalC['phone'] = contact_info[n][1]
        newContacts[z] = internalC
        internalC = {}
    return newContacts

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    return

