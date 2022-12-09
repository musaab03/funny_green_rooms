import shelve

save_file = shelve.open("savedfile")
save_file["users"] = input("ur name: ")
save_file.close()


save_file = shelve.open("savedfile")
saveduser = save_file["users"]
save_file.close()

print(saveduser)
