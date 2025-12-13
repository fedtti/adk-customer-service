from toon_format import decode
print("✅ Libraries imported.")


try:
    data = decode(input)
    print(f"✅ ")
    return data
except Exception as error:
    print(f"❌ ")
