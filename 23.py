authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = [name.strip() for name in authors.split (',')] 
author_last_names = [name.split()[-1] for name in author_names]
print("Список фамилий авторов:")
print(author_last_names)