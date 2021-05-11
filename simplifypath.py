from collections import deque


def simplifyPath(path: str) -> str:
    stack = deque()

    for element in path.split("/"):
        if stack and element == "..":
            stack.pop()
        elif element not in [".", "", ".."]:
            stack.append(element)

    return '/' + '/'.join(stack)

print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/../home/.../"))
print(simplifyPath("/home//foo"))
print(simplifyPath("/a/./b/../../c/"))
print(simplifyPath("/a/../../b/../c//.//"))