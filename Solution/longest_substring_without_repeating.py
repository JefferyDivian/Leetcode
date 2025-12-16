def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        maxi = 0 
        text = ''

        for i in range(len(s)):
            if s[i] not in text:
                    text+=s[i]
            for j in range(i+1,len(s)):
                if s[j] not in text:
                    text+=s[j]
                elif s[j] in text:
                    if len(text)>maxi:
                        maxi = len(text)
                    text = ''
                    break
        return(max(maxi,len(text)))