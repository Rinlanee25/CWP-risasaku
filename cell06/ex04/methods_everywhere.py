#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    # ต่อท้ายด้วย 'Z' จนกว่าความยาวจะครบ 8 ตัวอักษร
    print(s + 'Z' * (8 - len(s)))

def main():
    if len(sys.argv) < 2:
        print("none")
        return

    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()
    