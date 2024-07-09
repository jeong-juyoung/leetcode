class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        plus = 0
        while len(students) > 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                plus = 0
            else:
                students.append(students.pop(0))
                plus += 1

            if plus == len(students):
                break        
        return len(students)
        