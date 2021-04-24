
def workbook(n, k, arr):

    special_chapters = 0
    page_number = 1

    for q in range(n):
        
        total_problems = arr[q]
        group = 0

        for problem_no in range(1,total_problems+1):
            
            group += 1

            if problem_no == page_number:
                special_chapters += 1
        
            if group >= k:
                page_number += 1
                group = 0

            if problem_no == total_problems and group != 0:
                page_number += 1


    return special_chapters

n = 15
k = 20
arr = [1, 8, 19, 15, 2, 29, 3, 2, 25, 2, 19, 26, 17, 33, 22]
print(workbook(n, k, arr))