/*
TC : O(n)
SC : O(n)
*/
class Solution
{
public:
    string removeDuplicates(string s, int k)
    {
        if (k == 0)
        {
            return s;
        }

        stack<pair<char, int>> st;
        for (int i = 0; i < s.size(); i++)
        {
            if (st.empty())
            {
                st.push({s[i], 1});
            }
            else
            {
                if (st.top().first == s[i])
                {
                    st.top().second += 1;
                    if (st.top().second == k)
                    {
                        st.pop();
                    }
                }
                else
                {
                    st.push({s[i], 1});
                }
            }
        }

        string res = "";

        while (!st.empty())
        {
            for (int i = 0; i < st.top().second; i++)
            {
                res += st.top().first;
            }
            st.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};