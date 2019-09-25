class Solution:
    def getImportance(self, employees, id):
        employee_dict = {employee.id : employee for employee in employees}
        def dfs(id):
            return employee_dict[id].importance + sum(dfs(id) for id in employee_dict[id].subordinates)
        return dfs(id)
