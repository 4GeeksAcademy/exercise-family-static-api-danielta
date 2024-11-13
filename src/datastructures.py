
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask import request

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"]= self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        for i in range(0,len(self._members)):
            if self._members[i]["id"] == id:
                member = self._members.pop(i)
                return f"{member['first_name']} deleted"
        # for member in self._members:
        #     if member["id"] == id:
        #         self._members.remove(member)
        #         return f"{member['first_name']} deleted"
        return None
        
    # def patch_member(self, id):
    #     for i in range(0,len(self._members)):
    #         if self._members[i]["id"] == id:
    #             member = self._members[i]
    #         change_data = request.get_json()
    #         member.update(change_data)
    #         return member
    #     return "Update failed"
    def patch_member(self, id, change_data):
        for i in range(0,len(self._members)):  
            if self._members[i]["id"] == id:
                member = self._members[i]
                for key, value in change_data.items():
                    member[key] = value
                return member
        return "Update failed"

    def put_member(self, id, change_data):
        for i in range(0,len(self._members)):  
            if self._members[i]["id"] == id:
                self._members[i] = change_data
                return self._members[i]
        return "update failed"

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
