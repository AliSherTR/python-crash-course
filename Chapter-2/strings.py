# 2.3 Personal Message: Store a person’s name in a variable, and print a mes-sage to that person Your message should be simple, such as, “Hello Eric,would you like to learn some Python today?”

name = "Eric"

print("Hello " + name + ", would you like to learn some python today?")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecas

print(name.title() + " " + name.upper() + " " + name.lower())


# 2-5. Famous Quote: Find a quote from a famous person you admire Print the
# quote and the name of its author Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new

quote = 'Albert Einstien once said, "A person who never made a mistake never tried anything new " '

print(quote)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person Then compose your message and store it in a new variable called message Print your message

famous_person = "Albert Einstien"

message = ',once said, "A person who never made a mistake never tried anything new "'

print(famous_person + " " +message)

# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name Make sure you use each
# character combination, "\t" and "\n", at least once
# Print the name once, so the whitespace around the name is displayed
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip()

person = "\tAli Sher Khan\t"
print(person.rstrip())
print(person.lstrip())
print(person.strip())