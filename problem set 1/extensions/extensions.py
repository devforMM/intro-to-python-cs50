file=input("File name :").lower().rstrip()


if file.endswith("gif") or file.endswith("jpg") or file.endswith("jpeg") or file.endswith("png") or  file.endswith("gif"):
    print("image/jpeg")
elif file.endswith("pdf"):
    print("application/pdf")
elif file.endswith("txt"):
    print("text/plain")
elif file.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
