import sys
sys.path.insert(0, r"./src")

import textanalysis_tool

result = textanalysis_tool.hello("My Name")

if result == "Hello, My Name!":
    print("Test Passed!")
else:
    print("Test Failed")