#STRING

data = "ini adl string"
print(data)
print(type(data))

'''
1. menggunakan single quote '...'
2. menggunakan double quote "..."
'''
print("menggunakan quote (\"/')")
data = 'ini menggunakan single quote'
print(data)

data = "ini menggunakan double quote"
print(data)

print('"Iori : hi keii si tampan"')
print("'keii : oh hi Iori'")

# 2. MENGGUNAKAN TANDA \
# fungsi : membuat tanda ' menjadi str
print("---menggunakan tanda (\)---")
print('ini adalah hari jum\'at')
print('g\'day, isn\'t it?')

#fungsi : backslash
print("C:\\user\\Ucup")

# TAB
# fungsi : menjauhkan text (memberi space pada text)
print("kei\tviana, berjauhan")

# BACKSPACE
# mendekatkan text
print("kei \bchel, jadi deketan")

# NEWLINE
# fungsi : membuat baris stlhnya

print("baris pertama.\nbaris kedua.") #LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") #cr -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #crlf -. windows

# 3. STRING LITERAL OR RAW

#hati-hati
print("C\new folder") #akan salah pathnya

# menggunakan raw string
print(r"C:\new folder") # apapun setelah "r" dianggap string

# MULTI LITERAL STRING
print("""
nama : Keii
kelas : SSS
""")

# MULTI LITERAL STRING DAN RAW
print(r"""
nama : Keii
kelas : SSS\new absolute
Domain : Reworld Manipulation
""")
