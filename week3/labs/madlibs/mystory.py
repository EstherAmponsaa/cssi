print "\n\Mad Libs Assignment\n\n"
story = "Jack's {0} can make paper {1} come to {2} and {3} another animals to {4}"

print story.format("mother","animals","play","join","play")
noun = raw_input("Enter a noun:")
noun2 = raw_input("Enter a noun2:")
noun3 = raw_input("Enter a noun3:")
noun4 = raw_input("Enter a noun4:")
noun5 = raw_input("Enter a noun5:")
print (story.format(noun,noun2,noun3,noun4,noun5))
