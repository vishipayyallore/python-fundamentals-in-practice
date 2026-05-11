# Filename: src/L1/S1/bytecode_demo.py
# Session 1 — optional "peek under the hood"
# Don't teach this line-by-line in 30 min. It's OK if output feels cryptic;
# the point is: "something" turns your source into lower-level steps.

# Preview: disassembly and functions — full story comes in later sessions.

import dis

print("🚀 Advanced Python Preview")
print("=" * 50)

# Demonstrate Python's compilation process (from our lesson!)
print("\n🔍 Python Magic: Compilation & Interpretation Demo")
print("Let's see Python's bytecode in action!")


def greet():
    print("Hello World")


print("\n📄 Your Python Code:")
print("def greet():")
print("    print('Hello World')")

print("\n💾 Python's Bytecode (what the compiler creates):")
dis.dis(greet)

print(
    "\n🎯 Your source became bytecode; the PVM runs it. No need to memorize this yet."
)

print("\n" + "=" * 50)
print("🚀 Amazing! You've just seen Python's internal magic!")
print("This bytecode runs on the Python Virtual Machine.")
print("Keep learning, and you'll discover even more Python secrets! 🐍✨")
