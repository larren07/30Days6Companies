from ast import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = ['+','-','*','/']
        for i in tokens:
            if i not in ops:
                st.append(int(i))
            else:
                if(i == '+'):
                    res = st.pop(-1) + st.pop(-1)
                elif(i == '-'):
                    a = st.pop(-1)
                    b = st.pop(-1)
                    res =  b - a
                elif(i == '*'):
                    res = st.pop(-1) * st.pop(-1)
                else:
                    a = st.pop(-1)
                    b = st.pop(-1)
                    res =  int(b /a)

                st.append(res)
            # print(st)
        return st[0]