class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # need: t 中每个字符需要多少个
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # window: 当前 sliding window 中的字符数量
        window = {}

        # have: 当前已经满足多少种字符
        # required: 总共需要满足多少种字符
        have = 0
        required = len(need)

        l = 0

        # 保存目前最短答案
        result_start = 0
        result_length = float("inf")

        for r in range(len(s)):
            right_char = s[r]

            # TODO 1:
            # 如果 right_char 是需要的字符
            # 把它加入 window
            if right_char in need:
                window[right_char] = window.get(right_char,0) + 1

            # TODO 2:
            # 如果这个字符的数量“刚好达到” need 的要求
            # have += 1
                if need[right_char] == window[right_char]:
                    have += 1

            # 当 window 已经 valid 时，开始 shrink
            while have == required:

                current_length = r - l + 1

                # TODO 3:
                # 如果当前窗口更短，更新答案
                if current_length < result_length:
                    result_length = current_length
                    result_start = l

                left_char = s[l]

                # TODO 4:
                # 如果 left_char 是需要的字符
                # 从 window 中移除它
                if left_char in need:
                    window[left_char] -= 1

                # TODO 5:
                # 如果移除后，数量低于 need
                # have -= 1


                    if window[left_char] < need[left_char]:
                        have -= 1

                # shrink left
                l += 1

        if result_length == float("inf"):
            return ""

        return s[result_start:result_start + result_length]