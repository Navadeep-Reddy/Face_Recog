import face_recognition as fr
import glob
import os
import sys

#List for paths of known faces
face_path = []

#List for known face encodings 
encoding_store = []

#List for names
name_store = []

#List for possible file types
file_types = ["*.jpg", "*.png", "*.svg", "*.gif", "*.webp", "*.avif"]

location = "Faces/"

#Get path of photos of all recorded people from the stored location
for i in file_types:
    face_path.extend(glob.glob(os.path.join(location, i)))
    
for p in face_path:
    #Load face
    face = fr.load_image_file(p)
    #Get encoding of the first face found
    encoding = fr.face_encodings(face)[0]

    #Store the encoding of the face
    encoding_store.append(encoding)

    #Store the name of the face
    name_store.append(p[len(location): -4:])

#Loading unknown faces and getting its encodings
unknown_face = fr.load_image_file(sys.argv[1])
unknown_encoding = fr.face_encodings(unknown_face)

#variable for numbering unknown individuals
var = 1

#Looping through the encodings found and checking if they match
for single_encoding in unknown_encoding:
    #Variable for tracking if any faces have been found
    found = True

    #Boolean list after comparing unknown_encoding to every encoding in data set
    match_list = fr.compare_faces(encoding_store, single_encoding)

    if True in match_list:
        first_match_index = match_list.index(True)
        print(name_store[first_match_index])
        found = False
    else:

        print(f"Unknown Individual {var}")
        print(single_encoding)
        var += 1



