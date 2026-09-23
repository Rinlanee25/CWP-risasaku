#!/usr/bin/env python3
import sys

if len(sys.argv) <= 1:
    print("none")
else:
    
    for param in sys.argv[1:]:
        # ตรวจสอบว่าไม่ได้ลงท้ายด้วย "ism"
        if not param.endswith("ism"):
            print(f"{param}ism")
            