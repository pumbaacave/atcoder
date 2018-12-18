"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
Solution
want to put info (ori_data, target_data) in one cell
set INFO = ori_data * N + target_data
can retrieve info using oridata, target_data = divmod(INFO, N)
if val > N that is an INFO
edge case: ori_data = 0
so INFO = INOF' + N
"""
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        N = len(A)
        for i in range(N):
            target = (A[A[i]] // N) -1 if A[A[i]]> N else A[A[i]]
            A[i] = A[i] * N + target + N
        # print(A)
        for i in range(N):
            A[i] = A[i] % N
        return A
