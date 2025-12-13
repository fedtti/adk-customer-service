from toon_format import encode
print("✅ Libraries imported.")


try:
    data = encode(input)
    print(f"✅ ")
    return data
except Exception as error:
    print(f"❌ ")
