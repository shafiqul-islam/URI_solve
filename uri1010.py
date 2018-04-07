
p1_n,p1_u,p1_p=input().split()
p1_un=int(p1_u)
p1_pr=float(p1_p)
p1_cost=(p1_un*p1_pr)

p2_n,p2_u,p2_p=input().split()

p2_un=int(p2_u)
p2_pr=float(p2_p)
p2_cost=(p2_un*p2_pr)

total=p1_cost+p2_cost

print("VALOR A PAGAR: R$ %.2f" %total)