import json
import sys

# Pass scheduling variables to the script with action create/delete.
arguments = sys.argv
action_p=None
action_p = arguments[1]
proider_a=arguments[2]
address_a=arguments[3]
phone_a=arguments[4]
file=arguments[5]

#Load json data.
json_file = open(file)
data=json.load(json_file)

## Methods to work on Json data from a file.


def AddProvider(provider:str=None, street:str=None, phone:str=None ):
    providerAddresses=data["Addresses"]
    new_address={provider:{"Street":street,"Phone":phone}}
    providerAddresses.append(new_address)
    new_file=open(file,"w")
    json.dump(data, new_file,indent=3)
    new_file.close()
    print(f"Added new address {new_address}")

def DeleteProvider(provider:str=None, street:str=None, phone:str=None):
    providerAddresses=data["Addresses"]
    address_to_delete={provider:{"Street":street,"Phone":phone}}
    if address_to_delete in providerAddresses:
        providerAddresses.remove(address_to_delete)
        new_file=open(file,"w")
        json.dump(data,new_file,indent=3)
        new_file.close()
        print(f"Deleted {address_to_delete}")
        exit()
    print(f"Address {address_to_delete} does not exist.")
    


if __name__=="__main__":
    if action_p=="create":
        AddProvider(proider_a,address_a,phone_a)
    if action_p=="delete":
        DeleteProvider(proider_a,address_a,phone_a)

