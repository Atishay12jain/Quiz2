# OUIZ
print("----------------Online Test------------------\n\n")
print("             Register as a user           ")
name=input("Enter your name: ").lower()
password=input("Enter your password:").lower()
n=False
l=False

print("              Login          ")
while l!=True:
    m=input("Enter your user name: ").lower()
    if m!=name:
       print("Invalid credentials\n Renter your details")
       l=False
    else:
        l=True
        while n!=True:
            k=input("Enter your password:").lower()
            print("\n")
            if k!=password:
               print("Invalid password")
               n=False
            else:
                n=True
                print("----------Quiz--------\n")


questions =("Which data structure can be used to implement function call recursion?",
           "In a directed acyclic graph (DAG), which of the following algorithms is used to find the topological ordering of the vertices?",
           "Which type of tree traversal visits the nodes in the order: root, left subtree, right subtree?",
           "Which collision resolution technique in hashing uses a linked list to store multiple values at the same hash index?",
           "Which of the following algorithms is used for finding the shortest path in an unweighted graph?")
options=(("A) Queue ","B) Stack ","C) Array ","D) Heap"),
         ("A) Kruskal's Algorithm","B) Dijkstra's Algorithm","C) Topological Sort ", "D) Floyd-Warshall Algorithm"),
         ('A) In-order ','B) Post-order ','C) Pre-order',' D) Level-order'),
         ( 'A) Linear probing ','B) Quadratic probing','C) Separate chaining ', 'D) Double hashing'),
         ("A) Dijkstra's Algorithm","B) Depth-First Search (DFS)", " C) Breadth-First Search (BFS)", "D) Prim's Algorithm"))
         
answers=("B","C","C","C","C")
gueses=[]
score=0
question_num=0

for question in questions :
  print("------------------------------------------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  
  guess=input("enter (A,B,C,D):").upper()
  gueses.append(guess)
  if guess==answers[question_num]:
    score+=1
    print("CORRECT")
  else:
    print("INCORRECT")
    print(f"{answers[question_num]} is the CORRECT")
  question_num+=1

print("--------------------------")
print("            RESULT        ")
print("--------------------------")

print("answers:",end="")
for answer in answers:
  print(answer,end=" ")
print()

print("gueses:",end="")
for guess in gueses:
  print(answer,end=" ")
print()

score=int(score/len(questions)*100)
print(f"your score is:{score}%")


  



