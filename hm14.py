byte_string = b'r\xc3\xa9sum\xc3\xa9'

decoded_string_utf8 = byte_string.decode('utf-8')

print("Decoded string in UTF-8:", decoded_string_utf8)

reencoded_byte_string_latin1 = decoded_string_utf8.encode('latin1')

print("Reencoded byte string in Latin1:", reencoded_byte_string_latin1)

final_decoded_string = reencoded_byte_string_latin1.decode('latin1')

print("Final decoded string:", final_decoded_string)
