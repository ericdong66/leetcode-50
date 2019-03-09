# Time:  O(n)
# Space: O(1)
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it
# returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n)
# that reads n characters from the file.
#
# Note:
# The read function will only be called once for each test case.
#


# The read4 API is already defined for you.
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf += [file_content[i]]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i


class Solution(object):
    @staticmethod
    def read(buf, n):
        read_bytes = 0
        for i in range(n // 4 + 1):
            buffer = []
            size = read4(buffer)
            if size:
                read_bytes += size
                extra = read_bytes - n
                if extra <= 0:
                    buf += buffer
                else:
                    buf += buffer[0: size - extra]
            else:
                break
        return min(read_bytes, n)


if __name__ == "__main__":
    global file_content
    buf = []
    file_content = "abcdefghijklmnop"
    print(Solution().read(buf, 80), buf)
