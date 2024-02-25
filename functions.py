import os, humanize

def get_dir_content(d):
    dir_content = os.listdir(d)
    folders = [item for item in dir_content if not os.path.isfile(d + "/" + item)]
    files = [item for item in dir_content if os.path.isfile(d + "/" + item)]
    return files, folders


# --- Total size ---
def dir_size(directory):
    files, folders = get_dir_content(directory)
    return sum([os.path.getsize(directory + "/" + file) for file in files]) + sum([dir_size(directory + "/" + folder) for folder in folders])

# humanize.filesize.naturalsize(dir_size("."))


# --- Display all extensions in the directory and subdirs ---
def get_all_extensions(directory):
	files, folders = get_dir_content(directory)
	return list(set([os.path.splitext(directory + "/" + file)[1].lower() for file in files] + sum([get_all_extensions(directory + "/" + dir) for dir in folders], start=[])))


# --- Find all path with given extension ---
def find_extension_occ(directory, extension):
	files, folders = get_dir_content(directory)
	return list(filter(lambda filename: os.path.splitext(directory + "/" + filename)[1].lower()[1:] == extension.replace(".", ""), map(lambda f: directory + "/" + f, files))) + sum([find_extension_occ(directory + "/" + folder, extension) for folder in folders], start=[])


# --- e ---
def get_all_filenames_with_given_extension(directory, extensions):
	files, folders = get_dir_content(directory)
	return list(set([os.path.splitext(directory + "/" + file)[0].lower() for file in files if os.path.splitext(directory + "/" + file)[1].lower() in extensions] + sum([get_all_extensions(directory + "/" + dir) for dir in folders], start=[])))


# --- Batch rename (replaces spaces with underscores) ---
def renamer(directory, previous_string, new_string):
    files, folders = get_dir_content(directory)
    for file in files:
        os.rename(directory + '/' + file, directory + '/' + file.replace(previous_string, new_string))
    for folder in folders:
        new_folder_name = folder.replace(previous_string, new_string)
        try:
            os.rename(directory + '/' + folder, directory + '/' + new_folder_name)
            renamer(directory + '/' + new_folder_name)
        except: ...


# --- Get total size of an open directory ---
def walk(path):
	global count
	if locals().get("count") == None:
            count = 0
	count += 1
	print("  ---", count, end="\r")
	if path[-1] != '/':
		path += '/'
	response = r.get(path)
	soup = BeautifulSoup(response.text)
	strings = list(map(lambda string: re.sub(r"\s+", " ", string.strip()), list(soup.body.strings)))
	strings = strings[4:]
	s = 0
	links = []
	for i in range(0, len(strings), 2):
		links.append(strings[i])
		val = strings[i+1].split(" ")[-1]
		if val.isdigit():
			s += int(val)
	return s + sum([walk(path + link) if link[-1] == '/' else 0 for link in links])
